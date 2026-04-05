---
title: 'xmrig 2.5 unable to open config.json: no such file or directory'
source_url: https://github.com/xmrig/xmrig/issues/474
author: DediCATeD20
assignees: []
labels: []
created_at: '2018-03-24T11:18:54+00:00'
updated_at: '2018-03-24T17:13:58+00:00'
type: issue
status: closed
closed_at: '2018-03-24T17:13:58+00:00'
---

# Original Description
Using a freshly installed xmrig 2.5 on debian linux. I would like to use the config file option, but everything i try gives me unable to open config.json: no such file or directory.

I tried https, http, and wget download with local file.

**Examples:**

**Web**
/opt/xmrig/build/xmrig -c https://server/uploads/conf/xmrig-1-config.json

**Local**
rm /opt/xmrig/build/config.json
wget https://server//uploads/conf/xmrig-1-config.json -O /opt/xmrig/build/config.json
/opt/xmrig/build/xmrig

**Config**

{
    "algo": "cryptonight",
    "background": false,
    "colors": true,
    "retries": 5,
    "retry-pause": 5,
    "donate-level": 5,
    "syslog": false,
    "log-file": null,
    "print-time": 60,
    "av": 0,
    "safe": false,
    "max-cpu-usage": 90,
    "cpu-priority": 3,
    "threads": null,
    "pools": [
        {
            "url": "cryptonight.eu.nicehash.com:3355",
            "user": "xxx",
            "pass": "xxx",
            "keepalive": true,
            "nicehash": false
        }
    ],
    "api": {
        "port": 8080,
        "access-token": null,
        "worker-id": "W1"
    }
}

# Discussion History
## xmrig | 2018-03-24T16:38:52+00:00
Load config via http/https not supported, but with local file should no any troubles, newer reported issues with it.

* If not specify `-c` config should located in same directory with executable, if not you will get error with absolute path to config.json (starts with `/`).
* Same with `-c /opt/xmrig/build/config.json`
* If just `-c config.json` miner will looks for file in current working directory, for `/opt/xmrig/build/xmrig` it will be `/`.

Thank you.

## DediCATeD20 | 2018-03-24T17:13:58+00:00
Ok this clarifys it for me. Thank you very much. wget and -c config.json working.


# Action History
- Created by: DediCATeD20 | 2018-03-24T11:18:54+00:00
- Closed at: 2018-03-24T17:13:58+00:00
