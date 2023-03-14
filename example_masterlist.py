#!/usr/bin/env python3

import masterlist as altv
import logging 
import time

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

# Valid id
print(altv.validate_id("bb7228a0d366fc575a5682a99359424f"))

# Invalid id
print(altv.validate_id("abcdefghijklmnop123"))

# get the server cdn connect json
server = altv.Server("bb7228a0d366fc575a5682a99359424f")
print(server.connect_json)

# get the server and print it
server = altv.Server("bb7228a0d366fc575a5682a99359424f")
print(server)

# get the server connect json (without cdn)
server = altv.Server("3009f762b255336fed101d97b026fcfa")
print(server.connect_json)

# get all servers as server object
altv.get_servers()

# get all server stats
altv.get_server_stats()

# get server with update
server = altv.Server("bb7228a0d366fc575a5682a99359424f")
print(server.lastUpdate)
time.sleep(120)
server.update()
print(server.lastUpdate)

# get the server permissions
server = altv.Server("0330ffff0c5e97e277d038a707701024")
print(server.permissions)