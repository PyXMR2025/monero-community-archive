---
title: --api-no-restricted does not work via command prompt?
source_url: https://github.com/xmrig/xmrig/issues/498
author: d3c0d3d
assignees: []
labels: []
created_at: '2018-04-04T11:58:38+00:00'
updated_at: '2018-04-04T12:20:10+00:00'
type: issue
status: closed
closed_at: '2018-04-04T12:20:10+00:00'
---

# Original Description
I have tried in several ways' xmrig.exe: option does not take an argument '--api-no-restricted' does not always work showing the same message at startup of 'XMRig/2.6.0-beta1 libuv/1.19.2 MSVC/2017'.

--api-no-restricted=0
--api-no-restricted=1
--api-no-restricted="false"
--api-no-restricted="true"
????

> xmrig.exe: option doesn't take an argument -- api-no-restricted

... it looks like there is a gap between '-' and 'a' and this is causing the error!


# Discussion History
## xmrig | 2018-04-04T12:07:10+00:00
Just `--api-no-restricted` without any additional arguments, if it not work too it may a bug, I will check later, via config file should work:
```json
    "api": {
        "port": 4466,
        "access-token": "TOKEN",
        "worker-id": null,
        "ipv6": true,
        "restricted": false
    },
```

## d3c0d3d | 2018-04-04T12:20:10+00:00
It worked perfectly, I got the settings, thanks for the quick support!

# Action History
- Created by: d3c0d3d | 2018-04-04T11:58:38+00:00
- Closed at: 2018-04-04T12:20:10+00:00
