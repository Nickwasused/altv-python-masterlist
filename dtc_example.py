#!/usr/bin/env python3

import masterlist as altv
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

# get the server dtc url
server = altv.get_server_by_id("bb7228a0d366fc575a5682a99359424f")
print(server.get_dtc_url(password="test"))

# locked example without password
server = altv.get_server_by_id("562d1e7d5d0198accf4f3e7953111505")
print(server.get_dtc_url())

# locked example with password
server = altv.get_server_by_id("562d1e7d5d0198accf4f3e7953111505")
print(server.get_dtc_url(password="test"))