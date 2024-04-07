#!/usr/bin/env python3

from altvmasterlist import masterlist as altv
import logging
import time

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

# Valid id
logging.info(altv.validate_id("mXFlJSM"))

# Invalid id
logging.info(altv.validate_id("mXFlJSMaaaaaaaaaaaaaaaa"))

logging.info(altv.get_servers())

# get the server cdn connect json
server = altv.Server("EnLAA0O")
logging.info(server.connect_json)

# check the server group
server = altv.Server("YMRctiN")
logging.info(server.group)

# get the server and print it
server = altv.Server("mXFlJSM")
logging.info(server)

# get the server connect json (without cdn)
server = altv.Server("mXFlJSM")
logging.info(server.connect_json)

# get all servers as server object
altv.get_servers()

# get all server stats
altv.get_server_stats()

# get server with update
server = altv.Server("mXFlJSM")
logging.info(server.lastTimeUpdate)
time.sleep(120)
server.update()
logging.info(server.lastTimeUpdate)

# get the server permissions
server = altv.Server("mXFlJSM")
logging.info(server.permissions)
