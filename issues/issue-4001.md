---
title: Can't start P2Pool (Flatpak)
source_url: https://github.com/monero-project/monero-gui/issues/4001
author: ghost
assignees: []
labels: []
created_at: '2022-08-11T04:36:01+00:00'
updated_at: '2022-08-11T05:35:16+00:00'
type: issue
status: closed
closed_at: '2022-08-11T05:35:16+00:00'
---

# Original Description
I'm trying to mine with P2Pool, but P2Pool doesn't work.

Logs:

```
...
2022-08-11 04:28:58.7335 Log started
2022-08-11 04:28:58.7336 Log failed to open p2pool.log
2022-08-11 04:28:58.7337 P2Pool v2.2.1 (built with GCC/11.3.0 on Aug  6 2022)
2022-08-11 04:28:58.7340 P2Pool API path /app/bin/stats/ doesn't exist
2022-08-11 04:28:58.7340 Log stopped
...
```
OS: Fedora Silverblue 36.20220810.0
GUI: 0.18.0.0


# Discussion History
## q7nm | 2022-08-11T05:29:56+00:00
Hello. Use option `--data-api "path"`. Instead of `"path"`, you can write for example, path to the `Monero` directory in $HOME. 
Or create new directory and give flatpak permission. (`flatpak --user override --filesystem=~/example_directory org.getmonero.Monero`)

# Action History
- Created by: ghost | 2022-08-11T04:36:01+00:00
- Closed at: 2022-08-11T05:35:16+00:00
