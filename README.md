server
======

The server serves the [offline-build branch][offline-build].
If it runs locally, this allows the [intro] page to serve offline content.

[offline-build]: https://github.com/CoderDojoPotsdam/intro/tree/offline-build
[intro]: https://coderdojopotsdam.github.io/intro/

Installation
------------

If you want to install the server, you will need to have Python 3 and the
corresponding pip installer.
Under Ubuntu, do the following:

    sudo apt-get install python3 pip-python3

To install the offline server, do this:

    pip3 install https://github.com/CoderDojoPotsdam/intro/archive/server.zip

Windows:

    py -3 -m pip install https://github.com/CoderDojoPotsdam/intro/archive/server.zip

**Note:** You might want to use the `--user` switch if you do not have
administrator rights. You can use the `--upgrade` argument of pip to update you installation.


Also, either download or clone the offline version of the website.

- [Download][download]
- Clone:
  ```shell
  git clone --depth=1 --branch offline-build \
            https://github.com/CoderDojoPotsdam/intro.git offline-build
  ```
  You will need to replace `path/to/offline-build` with the
  path to the cloned repository in the following.

Run the server
--------------

In order to run the server, you can use this command after installation and
when you are in the directory of this file.

    export OFFLINE_BUILD_DIRECTORY=path/to/offline-build
    python3 -m intro_offline_server
    
Windows:

    set OFFLINE_BUILD_DIRECTORY=path/to/offline-build
    py -3 -m intro_offline_server

This yields the following output:

```
 * Running on http://[::]:25444/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 278-881-192
```

These are all configuration variables:

- `OFFLINE_BUILD_DIRECTORY` - If given, this is the directory the server serves the offline content from.
  Only if this variable is set, the server sends announcements to the servers in the [servers][servers] file.
  These announcements include all HTTP addresses the server could possibly reached in the local network.
- `PORT` defaults to `25444` - This is the port at which the HTTP server listens for connections with both IPv4 and IPv6.
- Announcements
  - `SECONDS_TO_CONNECT` defaults to `20` - These are the seconds to establish a connection to
    the servers in the [servers][servers] file for announcement.
  - `SECONDS_TO_UNTIL_OUTDATED` defaults to 10 Minutes - This is the time an announcement is valid.
    This is only interesting to servers which receive announcements.
  - `SECONDS_TO_REPORT` defaults to 3 Minutes, 20 Seconds - This is the time interval in which
    a server announces its exitence to the servers in the [servers][servers] file.

You can set these variables before the server is started in the same command line, like this under Ubuntu:

    export PORT=25444

Windows:

    set PORT=25444

Automated Updated Start
-----------------------

If you would like to run an updated version of the server,
have a look at the [intro special][startup-script]:
You can run this script as root to run an up-to-date version of the server with the updated `offline-build` branch.

Development
-----------

If you like to develop on this server, you can install `virtualenv`

    pip3 install --user virtualenv

Setup your python environment:

    virtualenv -p python3 ENV
    source ENV/bin/activate
    pip install -r requirements.txt

If you add a new package to requirements.txt, also run this command:

    pip install pip-tools
    pip-compile requirements.txt

For development of the offline features, you can use the following setup:

- folder `intro` - checkout with the server branch
- folder `intro/intro` checkout with the `master` branch running
  `jekyll serve --trace` to check the ability of localhost to use the
  offline links at http://localhost:4000 and
  `jekyll serve --trace --port 4001 --destination _site-offline`
- folder `intro/_site-offline/offline` checkout with the `offline` branch

[download]: https://github.com/CoderDojoPotsdam/intro/archive/server.zip
[startup-script]: https://github.com/CoderDojoPotsdam/CoderDojoOS/tree/master/specials/software/intro

Docker
------

You can also run and start the docker container:

    docker run --rm -p 25444:25444 coderdojopotsdam/intro

You may want to add this server to the [servers][servers] file if it has
an external reachability.

To build the container, run

    docker build --tag coderdojopotsdam/intro .

[servers]: servers.txt
