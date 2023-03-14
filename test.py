#!/usr/bin/env python3


import src.masterlist as altv
import src.altstats as altv2

server = altv.Server("bb7228a0d366fc575a5682a99359424f")
print(server)

server2 = altv2.get_server_by_id(127)
print(server2)
