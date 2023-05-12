#!/usr/bin/env python3

from altvmasterlist import masterlist as altv
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

skins = altv.get_launcher_skins()

skin = altv.get_launcher_skin(skins[0].fileName)
print(skin.servers[0])
print(skin.rss)
print(skin.servers[0].id)
