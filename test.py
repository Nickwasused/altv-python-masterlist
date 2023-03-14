#!/usr/bin/env python3
# example id = bb7228a0d366fc575a5682a99359424f
# same as 127 for altv2

import src.masterlist as altv
import src.altstats as altv2

server = altv2.Server(127)
print(server.connect_json)
print(server.dtc_url)
print(server.permissions)
