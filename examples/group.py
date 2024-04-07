#!/usr/bin/env python3

from altvmasterlist import masterlist as altv
import logging
import time

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

tmp_server = altv.Server("YMRctiN")
print(tmp_server.group)