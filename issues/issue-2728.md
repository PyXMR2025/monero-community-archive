---
title: unable to open "C:\Users\username\.xmrig.json".
source_url: https://github.com/xmrig/xmrig/issues/2728
author: QiangWei-Wade
assignees: []
labels: []
created_at: '2021-11-27T09:35:04+00:00'
updated_at: '2021-12-01T07:51:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
C:\qskg\xmrig-6.16.0-5t>xmrig.exe -a gr -o stratum+tcps://us-west.flockpool.com:5555 -u wallet.workername --tls --threads=5 --config=C:\qskg\xmrig-6.16.0-5t\config.json
[2021-11-27 17:33:40.755] unable to open "C:\Users\username\.xmrig.json".
[2021-11-27 17:33:40.756] unable to open "C:\Users\username\.config\xmrig.json".
[2021-11-27 17:33:40.756] no valid configuration found, try https://xmrig.com/wizard

What is xmrig.json at all? Please advise.

# Discussion History
## SChernykh | 2021-11-27T11:23:40+00:00
This command line is wrong. If you use `--config=...`, you put everything else in config.json, not in the command line. You need to put config.json next to xmrig.exe in the same folder, then you don't have to use any command line at all and just start xmrig.exe

## p178899 | 2021-11-29T17:54:44+00:00
My config.json is in the same folder of xmrig.exe, but when execute it got the same error:

[2021-11-27 17:33:40.755] unable to open "C:\Users\username.xmrig.json".
[2021-11-27 17:33:40.756] unable to open "C:\Users\username.config\xmrig.json".
[2021-11-27 17:33:40.756] no valid configuration found, try https://xmrig.com/wizard


## p178899 | 2021-12-01T07:51:46+00:00
@QiangWei-Wade have you solved your problem? (The same of mine!)

# Action History
- Created by: QiangWei-Wade | 2021-11-27T09:35:04+00:00
