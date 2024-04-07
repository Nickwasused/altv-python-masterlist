#!/usr/bin/env python3
from altvmasterlist import masterlist as altv
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

# get the server dtc url
server = altv.Server("mXFlJSM")
print(server.get_dtc_url(password="test"))

# locked example without password
server = altv.Server("mXFlJSM")
print(server.get_dtc_url())

# locked example with password
server = altv.Server("mXFlJSM")
print(server.get_dtc_url(password="test"))
