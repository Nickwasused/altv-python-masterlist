# Examples

# Get the version info of different files
```python3
#!/usr/bin/env python3
from altvcdn import get_version_info, Branch, Files, Platform
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)

# linux
logging.info(get_version_info(Branch.Release, Files.JSByte, Platform.Linux))
logging.info(get_version_info(Branch.Release, Files.Csharp, Platform.Linux))
logging.info(get_version_info(Branch.Release, Files.GameServer, Platform.Linux))
logging.info(get_version_info(Branch.Release, Files.VoiceServer, Platform.Linux))
logging.info(get_version_info(Branch.Release, Files.JavaScript, Platform.Linux))

# windows
logging.info(get_version_info(Branch.Release, Files.JSByte, Platform.Windows))
logging.info(get_version_info(Branch.Release, Files.Csharp, Platform.Windows))
logging.info(get_version_info(Branch.Release, Files.GameServer, Platform.Windows))
logging.info(get_version_info(Branch.Release, Files.VoiceServer, Platform.Windows))
logging.info(get_version_info(Branch.Release, Files.JavaScript, Platform.Windows))

# client
logging.info(get_version_info(Branch.Release, Files.GameClient, Platform.Windows))
logging.info(get_version_info(Branch.RC, Files.GameClient, Platform.Windows))
logging.info(get_version_info(Branch.Dev, Files.GameClient, Platform.Windows))
```

# Use of Enums

```python3
from altvcdn import Branch, Platform, Files

print(Branch.Release.value)
print(Platform.Windows.value)
print(Files.JSByte.value)
```