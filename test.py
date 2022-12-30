#!/usr/bin/env python3

import src.altstats as altv

server = altv.get_server_by_id("127")

print(server.get_resource_size("gamemode"))