---
title: connect to xmrig-proxy using ipv6
source_url: https://github.com/xmrig/xmrig/issues/496
author: adi3yz
assignees: []
labels: []
created_at: '2018-04-04T08:44:29+00:00'
updated_at: '2018-04-04T10:25:57+00:00'
type: issue
status: closed
closed_at: '2018-04-04T10:25:57+00:00'
---

# Original Description
    "pools": [
	{
            "url": "fe80::c132:2c9b:7794:38c3%10:7777",
            "user": "XMRig",
            "pass": "x",
            "keepalive": true,
            "nicehash": true,
	},

XMRig\config.json:532: Invalid value.
No pool URL supplied. Exiting.

how can i connect to xmrig-proxy using ipv6?

# Discussion History
## xmrig | 2018-04-04T08:55:35+00:00
Url should looks like `"[fe80::c132:2c9b:7794:38c3%10]:7777"` or `"[fe80::c132:2c9b:7794:38c3]:7777"`.
But in your config some other error at offset 532 from file start, you can use https://config.xmrig.com/ to generate config file.
Thank you.

# Action History
- Created by: adi3yz | 2018-04-04T08:44:29+00:00
- Closed at: 2018-04-04T10:25:57+00:00
