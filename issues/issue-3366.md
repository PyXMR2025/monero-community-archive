---
title: I get  “permission denied”
source_url: https://github.com/xmrig/xmrig/issues/3366
author: Adam55G
assignees: []
labels: []
created_at: '2023-11-22T14:46:06+00:00'
updated_at: '2025-06-18T22:32:27+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:32:27+00:00'
---

# Original Description
When I try to mine on my computer, I get the “permission denied” error. I tried to mine with Monero ocean but I get my pool+port+ip and the permission denied.

This is what is on my start file
@echo off
xmrig.exe —donate-level 1 -o gulf.moneroocean.stream:10128 -u WALLET ADDRESS -p MY USER NAME -a rx/0 -k
pause
*from Xmrig.exe to -k is in one line
I feel that the error is because of my ip as the computer I’m setting this up from is at a different location.


# Discussion History
## lesjokolat | 2024-01-06T16:45:46+00:00
This line here below see you may just need to add stratum type.

xmrig.exe —donate-level 1 -o stratum+tcp://gulf.moneroocean.stream:10128 -u WALLET ADDRESS -p MY USER NAME -a rx/0 -k



## koitsu | 2024-01-14T08:01:16+00:00
Wrong: `xmrig.exe —donate-level 1`
Right: `xmrig.exe --donate-level=1`

Look closely at the two changes.  Use `xmrig -h` to see the proper syntax for all arguments.

# Action History
- Created by: Adam55G | 2023-11-22T14:46:06+00:00
- Closed at: 2025-06-18T22:32:27+00:00
