/*
 * This file enables discovery of servers in the LAN.
 * If you like to add test servers, either run the server from the server branch
 * and serve content or execute the following to add a server:
 *
 *    connectedLanServer({ hostname: "programming", offline: "http://10.137.2.20:25444/", info: "http://10.137.2.20:25444/announce/info", id: "programming" })
 *
 */

var REFRESH_LOCAL_SERVERS_AFTER_MILLISECONDS = 30000;
var SERVERS_LISTING = "https://raw.githubusercontent.com/CoderDojoPotsdam/intro/server/servers.txt";

if (document.location.protocol != "http:") {
  console.log("NOTICE: an http website is required to detect local servers.");
}

function httpGetAsync(theUrl, callback)
{
  // from https://stackoverflow.com/a/4033310/1320237
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
      callback(xmlHttp.responseText);
  }
  xmlHttp.open("GET", theUrl, true); // true for asynchronous
  xmlHttp.send(null);
}

function checkServerAvailability(server) {
  console.log("Checking offline server availability of " + server.hostname + " at " + server.address);
  httpGetAsync(server.info, function(_){
    connectedLanServer(server);
  })
}

var servers = {};
var serverIds = [];

function connectedLanServer(server) {
  console.log("Server " + server.hostname + " responded.");
  servers[server.id] = server;
  for(var i = serverIds.length - 1; i >= 0; i--) {
    // remove element from array, see https://stackoverflow.com/a/5767335/1320237
    if(serverIds[i] == server.id) {
       serverIds.splice(i, 1);
    }
  }
  serverIds.push(server.id);
  updateServers();
}

function updateServers() {
  select = document.getElementById("offline-servers");
  if (serverIds.length == 0) {
    select.classList.add("invisible");
    return;
  }
  select.classList.remove("invisible");
  while (select.children.length > 0) {
    select.removeChild(select.lastChild);
  }
  option = document.createElement("option");
  option.text = document.location.hostname;
  option.selected = true;
  option.server = {
    "offline": document.location.protocol + "//" + document.location.host,
    "hostname": document.location.hostname
  };
  select.appendChild(option);
  for (var i = serverIds.length - 1; i >= 0; i -= 1) {
    var serverId = serverIds[i];
    var server = servers[serverId];
    option = document.createElement("option");
    option.text = server.hostname;
    option.server = server;
    select.appendChild(option);
  }
}

function switchOfflineServer(select) {
  // form https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_option_text
  var server = select.options[select.selectedIndex].server;
  var offline = server.offline;
  if (offline[offline.length - 1] == "/" ) {
    offline = offline.slice(0, -1);
  }
  var url = offline + document.location.pathname;
  console.log("Switching to offline server " + server.hostname + " at " + url);
  document.location = url;
}

function requestLanServersFrom(url) {
  console.log("Requesting LAN servers from " + url);
  httpGetAsync(url, function(announcementsString){
    var announcements = JSON.parse(announcementsString);
    console.log("Got announcements from " + announcements.host.hostname + " at " + url);
    announcements.servers.forEach(function(server){
      checkServerAvailability(server);
    })
  });
}

function refreshServersLoop(){
  httpGetAsync(SERVERS_LISTING, function(serverString){
    serverString.split("\n").forEach(function(server){
      var url = server.replace(/\s/g, "");
      if (url.length > 0) {
        requestLanServersFrom(url);
      }
    });
  })
  window.setTimeout(refreshServersLoop, REFRESH_LOCAL_SERVERS_AFTER_MILLISECONDS);
}

window.setTimeout(refreshServersLoop, 200);
