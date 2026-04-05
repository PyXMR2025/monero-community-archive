---
title: Error "JSON decode failed"
source_url: https://github.com/xmrig/xmrig/issues/456
author: ltCypher
assignees:
- xmrig
labels:
- bug
created_at: '2018-03-16T13:57:20+00:00'
updated_at: '2018-03-17T11:10:03+00:00'
type: issue
status: closed
closed_at: '2018-03-17T11:10:03+00:00'
---

# Original Description
Updated XMRIG to version 2.5 today and now I'm getting a bunch of error messages every five or six seconds:

Example:
2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed
[2018-03-16 14:54:50] [thanks.xmrig.com:80] JSON decode failed

After starting the miner it runs for some time without these errors, but after a while this message appears in the GUI.
Mining still seems to work though, hash rate report still works and it shows a normal hash rate.

Any idea?

# Discussion History
## xmrig | 2018-03-16T17:42:31+00:00
In version 2.5 I change address of donation pool from fee.xmrig.com:443 to thanks.xmrig.com:80, but looks like use port 80 is bad idea in your case. Try open https://thanks.xmrig.com/ in your browser probably you will see some page from your ISP.

Second bug is you should never see any troubles with donation pool, but I forgot silence this error, also was added in 2.5. It not affect mining. For temporary solution you can add line `0.0.0.0 thanks.xmrig.com` to your `hosts` file, it will disable donation.

Thank you.

## xmrig | 2018-03-17T11:10:03+00:00
Fixed, it will be included to next bugfix release v2.5.1.
Thank you.

# Action History
- Created by: ltCypher | 2018-03-16T13:57:20+00:00
- Closed at: 2018-03-17T11:10:03+00:00
