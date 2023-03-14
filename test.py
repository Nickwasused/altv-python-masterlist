#!/usr/bin/env python3
# example id = bb7228a0d366fc575a5682a99359424f

import src.masterlist as altv
import src.altstats as altv2

server = altv.Server("bb7228a0d366fc575a5682a99359424f")

print(server)

server.update()
print(server)