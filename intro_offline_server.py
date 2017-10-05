import os
from flask import Flask, send_from_directory, request, make_response
from concurrent.futures import ThreadPoolExecutor
import json
from urllib.parse import urlparse
from urllib.request import urlopen
import time
import heapq
import socket
import netifaces
import traceback
import threading

OFFLINE_BUILD_DIRECTORY = os.environ.get("OFFLINE_BUILD_DIRECTORY", "")
SECONDS_TO_CONNECT = int(os.environ.get("SECONDS_TO_CONNECT", 20))
SECONDS_TO_UNTIL_OUTDATED = int(os.environ.get("SECONDS_TO_UNTIL_OUTDATED", 600))
SECONDS_TO_REPORT = int(os.environ.get("SECONDS_TO_REPORT", 200))
PORT = int(os.environ.get("PORT", 25444))

app = Flask(__name__)

################################################################################
#
# Serve the folder content if given
#

if OFFLINE_BUILD_DIRECTORY:
    @app.route('/<path:path>')
    @app.route('/')
    def display(path=""):
        if path.endswith("/") or not path:
            path += "index.html"
        return send_from_directory(OFFLINE_BUILD_DIRECTORY, path)
else:
    print("Set the OFFLINE_BUILD_DIRECTORY variable to "
          "point to the directory to serve the offline "
          "build from.")


################################################################################
#
# Announce the server gloablly to allow local connections to it.
#

def is_ipv4_address(ip):
    """Return whether ip is an ipv4 address."""
    split = ip.split(".")
    return len(split) == 4 and all(s.isdigit() and 0 <= int(s) <= 255 for s in split)

def is_local_ipv4_address(ip):
    """Return whether this ip is from a LAN.

    10.*
    172.16/12
    192.168.*
    169.254.*
    """
    return is_ipv4_address(ip) and (ip.startswith("10.") or (ip.startswith("172.") and 16 <= int(ip.split(".")[1]) <= 31) or ip.startswith("192.168.") or ip.startswith("169.254."))

def is_ipv6_address(ip):
    """Return whether ip is an ipv4 address."""
    split = ip.split(":")
    return 3 <= len(split) <= 8 and all(len(s) <= 4 and all(c in "0123456789abcdef" for c in s) for s in split) and split.count("") <= (2 if split[-1] == "" or split[0] == "" else 1)

assert is_ipv6_address("::1")
assert is_ipv6_address("dee1::1")
assert is_ipv6_address("dee1::")
assert not is_ipv6_address("des1::1")
assert not is_ipv6_address("daaa1::1")

def is_local_ipv6_address(ip):
    """Return whether this ip is from a LAN.

    https://en.wikipedia.org/wiki/IPv6_address#Local_addresses
    ::1/128 - we can exclude this
    fe80::/10
    fc00::/7
    """
    return is_ipv6_address(ip) and (ip.startswith("fc") or ip.startswith("fd") or ip.startswith("fe8") or ip.startswith("fe9") or ip.startswith("fea") or ip.startswith("feb"))

def is_local_address(ip):
    """Return whether the address is a local ipv4 or ipv6 address"""
    return is_local_ipv4_address(ip) or is_local_ipv6_address(ip)

def server_is_local(server):
    """Return whether a server is from a local ip."""
    host = urlparse(server).hostname
    return is_local_address(host)


announced_servers = [] # outdated time, address

def dumps(data):
    """Dump some json data."""
    return json.dumps(data, indent=2) + "\r\n"

def allow_javascript_json(data):
    """Allow browser access"""
    response = make_response(dumps(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route("/announce", methods=["POST"])
def announe():
    data = json.loads(request.get_data())
    servers = data["servers"]
    hostname = data["hostname"]
    outdated = time.time() + SECONDS_TO_UNTIL_OUTDATED
    result_servers = []
    result = {"hostname": hostname, "servers":result_servers}
    for server in servers[:]:
        if server_is_local(server):
            entry = (outdated, hostname, server)
            heapq.heappush(announced_servers, entry)
            result_servers.append(server)
    remove_outdated()
    return dumps(result)

def remove_outdated():
    """Remove outdated server information."""
    now = time.time()
    while announced_servers:
        item = heapq.heappop(announced_servers)
        if item[0] >= now:
            heapq.heappush(announced_servers, item)
            break

@app.route("/announce", methods=["GET"])
def get_annournced():
    remove_outdated()
    addresses = set()
    servers = []
    for server in announced_servers:
        hostname, address = server[1], server[2]
        if address not in addresses:
            servers.append({"hostname": server[1], "address": server[2]})
        else:
            addresses.add(address)
    result = {"servers": servers, "host": get_info()}
    return allow_javascript_json(result)

def get_interface_addresses():
    """Return the addresses from the local interfaces."""
    return [addr["addr"].split("%")[0]
        for iface in netifaces.interfaces()
            for addrs in netifaces.ifaddresses(iface).values()
                for addr in addrs
                    if is_local_address(addr["addr"].split("%")[0])]

@app.route("/announce/info")
def serve_info():
    return allow_javascript_json(get_info())

def get_info():
    hostname = socket.gethostname()
    return {
        "hostname": hostname,
        "servers": ["http://{}:{}/".format("[{}]".format(addr) if is_ipv6_address(addr) else addr, PORT) for addr in get_interface_addresses()]
    }


def post_server_info_to(url):
    """Post the server information to the url."""
    data = dumps(get_info()).encode("UTF-8")
    try:
        urlopen(url, data=data, timeout=SECONDS_TO_CONNECT)
    except:
        traceback.print_exc()

def announce_loop():
    time.sleep(1) # wait for the servr to start
    while True:
        try:
            with open("servers.txt") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        post_server_info_to(line)
            time.sleep(SECONDS_TO_REPORT)
        except:
            traceback.print_exc()

thread = threading.Thread(target=announce_loop, daemon=True)
thread.start()

app.run(debug=True, host='::', port=PORT)
