---
title: DERO doesn't work in 6.11.0 - incompatible/disabled algorithm "cn/0" detected,
  reconnect
source_url: https://github.com/xmrig/xmrig/issues/2238
author: Robyer
assignees: []
labels: []
created_at: '2021-04-06T20:29:07+00:00'
updated_at: '2021-04-07T21:18:06+00:00'
type: issue
status: closed
closed_at: '2021-04-07T21:18:06+00:00'
---

# Original Description
**Describe the bug**
After installing and starting XMRig 6.11.0 with config set to mining DERO it shows error: `incompatible/disabled algorithm "cn/0" detected, reconnect`.
With XMRig 6.10.0 it works correctly.

**To Reproduce**
In config.json define pool with this and start the XMRig:
```
{
"algo": "astrobwt",
"coin": "dero",
...
}
```

Actually, when specifying only "algo", it works!
```
{
"algo": "astrobwt",
"coin": null,
...
}
```

**Expected behavior**
XMRig starts mining without error, as before.

**Required data**
```
    "pools": [
        {
            "algo": "astrobwt",
            "coin": "dero",
            "url": "dero.miner.rocks:30182",
            "user": "WALLET",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
         }
    }
```

**Additional context**

Maybe it is caused by commit d578a3828f66c275a7c48b867753d5d830d2e890 ?


# Discussion History
## SChernykh | 2021-04-06T20:36:53+00:00
I can confirm, that commit broke "coin" setting functionality.

# Action History
- Created by: Robyer | 2021-04-06T20:29:07+00:00
- Closed at: 2021-04-07T21:18:06+00:00
