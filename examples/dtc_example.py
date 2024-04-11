#!/usr/bin/env python3
from altvmasterlist import masterlist as altv
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)
server = altv.Server("mXFlJSM")


# get the server dtc url
print(server.get_dtc_url(password="test"))

# locked example without password
print(server.get_dtc_url())

# locked example with password
print(server.get_dtc_url(password="test"))
