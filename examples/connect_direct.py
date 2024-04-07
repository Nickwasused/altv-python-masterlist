#!/usr/bin/env python3

from altvmasterlist import masterlist as altv
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

# get the server cdn connect json
server = altv.Server()
server.set_public_id("0GLQLkG")
print(server.connect_json)
