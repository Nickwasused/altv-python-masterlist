#!/usr/bin/env python3

import altstats as altv
import logging
import time

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

# Valid id
print(altv.validate_id(86))

# Invalid id
print(altv.validate_id("ag567"))

# get the server cdn connect json
server = altv.get_server_by_id(86)
print(server.fetch_connect_json())

# get the server connect json (without cdn)
server = altv.get_server_by_id(26)
print(server.fetch_connect_json())

# get all servers as server object
servers = altv.get_servers()

for server in servers:
    print(server.get_json())

# get all server stats
altv.get_server_stats()

# get server with update
server = altv.get_server_by_id(86)
print(server.LastActivity)
time.sleep(120)
server.update()
print(server.LastActivity)

# get the server permissions
server = altv.get_server_by_id(86)
print(server.get_permissions())