---
title: Configure directories for data & cache
source_url: https://github.com/Cuprate/cuprate/issues/409
author: physics515
assignees: []
labels:
- C-request
created_at: '2025-03-18T19:44:24+00:00'
updated_at: '2025-04-05T14:33:57+00:00'
type: issue
status: closed
closed_at: '2025-04-05T14:33:57+00:00'
---

# Original Description
## Feature
Add a key to the configuration file to set the location of the data and cache directories.

## Why
I only have a 1TB OS drive on my PC but I an 86TB RAID10 setup where I would like the blockchain to be stored. I often flash my OS drive about every 3 months to start over clean and it would suck to have to resync every time.


# Discussion History
## Boog900 | 2025-03-18T20:23:32+00:00
The default config file generated does not generate all keys, we also are yet to document the full config in the user book.

You can change the paths by putting this in the config:

```toml
[fs]
data_directory = "path/to/folder"
cache_directory = "path/to/folder"
```

Hopefully that should work, I'll prioritize documenting the config for the user book.

# Action History
- Created by: physics515 | 2025-03-18T19:44:24+00:00
- Closed at: 2025-04-05T14:33:57+00:00
