#!/usr/bin/env python3

from altvmasterlist import masterlist as altv
import logging 
import time

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

# Valid id
print(altv.validate_id("mXFlJSM"))

# Invalid id
print(altv.validate_id("mXFlJSMaaaaaaaaaaaaaaaa"))

print(altv.get_servers())

# get the server cdn connect json
server = altv.Server("mXFlJSM")
print(server.connect_json)

# get the server and print it
server = altv.Server("mXFlJSM")
print(server)

# get the server connect json (without cdn)
server = altv.Server("mXFlJSM")
print(server.connect_json)

# get all servers as server object
altv.get_servers()

# get all server stats
altv.get_server_stats()

# get server with update
server = altv.Server("mXFlJSM")
print(server.lastTimeUpdate)
time.sleep(120)
server.update()
print(server.lastTimeUpdate)

# get the server permissions
server = altv.Server("mXFlJSM")
print(server.permissions)