---
title: xmrig.json error
source_url: https://github.com/xmrig/xmrig/issues/2809
author: RJ-Frosty
assignees: []
labels:
- question
created_at: '2021-12-14T00:15:59+00:00'
updated_at: '2022-04-03T14:37:15+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:37:15+00:00'
---

# Original Description
**Describe the bug**
Running ./xmrig produces errors
**To Reproduce**
sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone https://github.com/xmrig/xmrig.git
Edit donation file path: xmrig/src/donate.h
mkdir xmrig/build && cd xmrig/build
cmake ..
make -j$(nproc)
Chmod +x ./xmrig
cd ..
cd src
rm config.json
cd
touch config.json
nano config.json
add
{
    "api": {
        "worker-id": "foo"
    },
    "http": {
        "enabled": true,
        "host": "0.0.0.0",
        "port": 0,
        "access-token": "foo",
        "restricted": false
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "fast",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": false,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 0,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": "monero",
            "url": "127.0.0.1:18081",
            "user": "foo",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": false,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": true,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "retries": 5,
    "retry-pause": 5,
    "syslog": true,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "verbose": 1,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
cd ~/xmrig/build
./xmrig

**Expected behavior**
After pressing return it would run normal.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows] Ubuntu server
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.
$  ./xmrig
[2021-12-14 00:02:37.250] unable to open "/home/ubuntu/.xmrig.json".
[2021-12-14 00:02:37.250] unable to open "/home/ubuntu/.config/xmrig.json".
[2021-12-14 00:02:37.250] no valid configuration found, try https://xmrig.com/wizard

# Discussion History
## Spudz76 | 2021-12-14T02:06:51+00:00
Your pool entry was `enable: false` and `http->port` should be an actual port (otherwise it random selects one every run, which seems pointless).  Not really sure exactly which things made it unparseable, but here is a minimal version that should be what you want (swap in actual user/wallet of course).  Specifying things that are already default don't help and expand room for error.

```
{
   "api" : {
      "worker-id" : "foo"
   },
   "http" : {
      "enabled" : true,
      "host" : "0.0.0.0",
      "port" : 6969,
      "access-token" : "foo",
      "restricted" : false
   },
   "randomx" : {
      "mode" : "fast"
   },
   "cpu" : {
      "enabled" : true,
      "huge-pages" : true,
      "huge-pages-jit" : true,
      "memory-pool" : true,
      "yield" : false,
      "max-threads-hint" : 100
   },
   "opencl" : {
      "enabled" : false
   },
   "cuda" : {
      "enabled" : false
   },
   "donate-level" : 0,
   "donate-over-proxy" : 0,
   "pools" : [
      {
         "enabled" : true,
         "daemon" : true,
         "coin" : "monero",
         "url" : "127.0.0.1:18081",
         "user" : "foo",
         "pass" : "x"
      }
   ],
   "syslog" : true,
   "verbose" : 1
}
```

## RJ-Frosty | 2021-12-14T02:45:25+00:00
In my main it is specified.  I am not using a pool so you would think that it would be disabled, but I will change it.  
The main problem is that when I run it I get this error and it doesn't run
[2021-12-14 00:02:37.250] unable to open "/home/ubuntu/.xmrig.json".
[2021-12-14 00:02:37.250] unable to open "/home/ubuntu/.config/xmrig.json".
[2021-12-14 00:02:37.250] no valid configuration found, try https://xmrig.com/wizard
What is xmrig.json, and why is there two in separate locations?  How do I fix it?

## Spudz76 | 2021-12-14T03:16:33+00:00
When any of the files is not correct it just tries the next one (as if the corrupt one didn't exist).

Those are just the other default places you could put a config file, besides the obvious first default of `./config.json`

# Action History
- Created by: RJ-Frosty | 2021-12-14T00:15:59+00:00
- Closed at: 2022-04-03T14:37:15+00:00
