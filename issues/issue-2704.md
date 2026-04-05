---
title: CUDA disabled (no devices) - GTX 570
source_url: https://github.com/xmrig/xmrig/issues/2704
author: asw2012
assignees: []
labels: []
created_at: '2021-11-18T06:27:50+00:00'
updated_at: '2021-11-19T03:56:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I saw a reply earlier that stated:

CUDA Toolkit 8.0GA2

Build against it.

Now, I've downloaded and installed that particular CUDA revision.  I've been reading I have to compile a new .exe for XMRig with the CUDA I just downloaded?

Little lost here.  I'm just tryin to use my GTX570 card for mining - did not even fathom that it's this involved.

# Discussion History
## Spudz76 | 2021-11-18T07:07:52+00:00
Well if you're Windows then you can grab the precompiled `xmrig-cuda-6.15.1-cuda8_0-win64.zip` release [from here](https://github.com/xmrig/xmrig-cuda/releases) instead.  But for some reason I assumed you were on Linux.

## asw2012 | 2021-11-19T00:03:24+00:00
Yes, sir. Those files worked.  Thank you :)

## asw2012 | 2021-11-19T01:13:58+00:00
Ok, when I change to xmrpool.eu:9999 I get READ ERROR "end of file"

    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "xmrpool.eu:9999",
            "user": "MY****USER****INFO", 
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false


## asw2012 | 2021-11-19T03:56:33+00:00
Ok, learning curve here lol ...  got it to work on different algo and port number @ xmrpool

# Action History
- Created by: asw2012 | 2021-11-18T06:27:50+00:00
