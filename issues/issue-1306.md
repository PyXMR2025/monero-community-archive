---
title: Double connection to the pool?
source_url: https://github.com/xmrig/xmrig/issues/1306
author: MoneroOcean
assignees: []
labels:
- bug
created_at: '2019-11-20T02:51:36+00:00'
updated_at: '2020-06-02T14:34:39+00:00'
type: issue
status: closed
closed_at: '2020-06-02T14:34:39+00:00'
---

# Original Description
Looks like after current pool is dead v5.0.0 miner tries to do two connections to the pool (not sure if important that it is the same DNS but different IP) that is visible from the identical date stamps (14:08:25.530) of two jobs sent by the pool:

```
[2019-11-18 14:02:15.376]  cpu  accepted (26839/268) diff 24349 (124 ms)
[2019-11-18 14:03:14.749] speed 10s/60s/15m 764.8 764.3 755.8 H/s max 6244.0 H/s
[2019-11-18 14:04:13.774]  net  no active pools, stop mining
[2019-11-18 14:04:14.783] speed 10s/60s/15m 762.7 764.3 757.4 H/s max 6244.0 H/s
[2019-11-18 14:05:08.944]  cpu  accepted (26840/268) diff 24349 (75640 ms)
[2019-11-18 14:05:14.865] speed 10s/60s/15m n/a n/a 758.3 H/s max 6244.0 H/s
[2019-11-18 14:05:16.427]  net  use pool gulf.moneroocean.stream:10064  95.216.209.67
[2019-11-18 14:05:16.427]  net  new job from gulf.moneroocean.stream:10064 diff 64000 algo cn/r height 1969680
[2019-11-18 14:05:23.355]  net  use pool gulf.moneroocean.stream:10064  95.216.209.67
[2019-11-18 14:05:23.355]  net  new job from gulf.moneroocean.stream:10064 diff 64000 algo cn/r height 1969680
[2019-11-18 14:06:14.925] speed 10s/60s/15m 764.5 764.5 706.5 H/s max 6244.0 H/s
[2019-11-18 14:07:14.984] speed 10s/60s/15m 762.7 763.4 707.5 H/s max 6244.0 H/s
[2019-11-18 14:08:15.045] speed 10s/60s/15m 762.1 762.6 708.1 H/s max 6244.0 H/s
[2019-11-18 14:08:25.530]  net  new job from gulf.moneroocean.stream:10064 diff 42154 algo cn/r height 1969680
[2019-11-18 14:08:25.530]  net  new job from gulf.moneroocean.stream:10064 diff 40611 algo cn/r height 1969680
[2019-11-18 14:09:04.283]  cpu  rejected (26840/269) diff 40611 "Invalid job id" (92 ms)

```

That causes xmrig to go to persistent rejected share mode due to "Invalid job id" and can only be cured by miner restart.

# Discussion History
## xmrig | 2019-11-20T07:26:55+00:00
Pretty strange, how looks pools part in config?
Thank you.

## MoneroOcean | 2019-11-20T16:56:07+00:00
Nothing unusual as far as I can tell:

```
   "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "gulf.moneroocean.stream:10064",
            "user": "ADDR",
            "pass": "MON10006:xxx@gmail.com",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
```

## xmrig | 2019-11-20T18:34:26+00:00
I unable to reproduce the issue, can you rebuild miner with `-DWITH_DEBUG_LOG=ON`?

But this issue looks like memory corruption is some other place, there is other strange thing `cpu  accepted (26840/268) diff 24349 (75640 ms)`

## MoneroOcean | 2019-11-20T23:49:20+00:00
Will rebuild with -DWITH_DEBUG_LOG=ON. Thank you!

## MoneroOcean | 2019-12-05T15:41:22+00:00
Problem reproduced on debug miner (v5.1.1):

```
[2019-12-05 07:48:39.609] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10454,"jsonrpc":"2.0","method":"submit","params":{"id":"11cbdc9
[2019-12-05 07:48:59.794] [gulf.moneroocean.stream:10064] timeout
[2019-12-05 07:48:59.794] [gulf.moneroocean.stream:10064] state: "closing"
[2019-12-05 07:48:59.794] [gulf.moneroocean.stream:10064] state: "unconnected"
[2019-12-05 07:48:59.794] [gulf.moneroocean.stream:10064] state: "reconnecting"
[2019-12-05 07:48:59.794]  net  no active pools, stop mining
[2019-12-05 07:49:04.799] [gulf.moneroocean.stream:10064] state: "host-lookup"
[2019-12-05 07:49:04.858] [gulf.moneroocean.stream:10064] state: "connecting"
[2019-12-05 07:49:11.837] speed 10s/60s/15m n/a 6308.2 6220.1 H/s max 6371.7 H/s
[2019-12-05 07:49:25.819] [gulf.moneroocean.stream:10064] state: "reconnecting"
[2019-12-05 07:49:30.824] [gulf.moneroocean.stream:10064] state: "host-lookup"
[2019-12-05 07:49:30.825] [gulf.moneroocean.stream:10064] state: "connecting"
[2019-12-05 07:49:30.935] [gulf.moneroocean.stream:10064] state: "connected"
[2019-12-05 07:49:30.935] [gulf.moneroocean.stream:10064] send (1191 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"45DxHBnc
[2019-12-05 07:49:30.996] [gulf.moneroocean.stream:10064] received (490 bytes): "{"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"e1d351bd-30a
[2019-12-05 07:49:30.996]  net  use pool gulf.moneroocean.stream:10064  95.216.209.67
[2019-12-05 07:49:30.996]  net  new job from gulf.moneroocean.stream:10064 diff 64000 algo rx/0 height 1982033
[2019-12-05 07:49:36.394] [gulf.moneroocean.stream:10064] state: "connected"
[2019-12-05 07:49:36.394] [gulf.moneroocean.stream:10064] send (1191 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"45DxHBnc
[2019-12-05 07:49:36.455] [gulf.moneroocean.stream:10064] received (490 bytes): "{"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"c0119007-a15
[2019-12-05 07:49:36.455]  net  use pool gulf.moneroocean.stream:10064  95.216.209.67
[2019-12-05 07:49:36.455]  net  new job from gulf.moneroocean.stream:10064 diff 64000 algo rx/0 height 1982033
[2019-12-05 07:49:36.870] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10457,"jsonrpc":"2.0","method":"submit","params":{"id":"c011900
[2019-12-05 07:49:37.024] [gulf.moneroocean.stream:10064] received (66 bytes): "{"id":10457,"jsonrpc":"2.0","error":null,"result":{"status":"OK"}}
[2019-12-05 07:49:37.024]  cpu  accepted (10447/0) diff 64000 (154 ms)
[2019-12-05 07:49:38.536] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10458,"jsonrpc":"2.0","method":"submit","params":{"id":"c011900
[2019-12-05 07:49:38.663] [gulf.moneroocean.stream:10064] received (66 bytes): "{"id":10458,"jsonrpc":"2.0","error":null,"result":{"status":"OK"}}
[2019-12-05 07:49:38.664]  cpu  accepted (10448/0) diff 64000 (127 ms)
[2019-12-05 07:49:44.162] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10459,"jsonrpc":"2.0","method":"submit","params":{"id":"c011900
[2019-12-05 07:49:44.236] [gulf.moneroocean.stream:10064] received (66 bytes): "{"id":10459,"jsonrpc":"2.0","error":null,"result":{"status":"OK"}}
[2019-12-05 07:49:44.236]  cpu  accepted (10449/0) diff 64000 (74 ms)
[2019-12-05 07:49:58.141] [gulf.moneroocean.stream:10064] received (419 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0c0cd8eca2ef050
[2019-12-05 07:49:58.141]  net  new job from gulf.moneroocean.stream:10064 diff 265646 algo rx/0 height 1982033
[2019-12-05 07:50:11.904] speed 10s/60s/15m 6314.4 6321.1 6002.6 H/s max 6371.7 H/s
[2019-12-05 07:50:36.776] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10460,"jsonrpc":"2.0","method":"submit","params":{"id":"c011900
[2019-12-05 07:50:37.053] [gulf.moneroocean.stream:10064] received (66 bytes): "{"id":10460,"jsonrpc":"2.0","error":null,"result":{"status":"OK"}}
[2019-12-05 07:50:37.053]  cpu  accepted (10450/0) diff 265646 (277 ms)
[2019-12-05 07:50:58.149] [gulf.moneroocean.stream:10064] received (419 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0c0cd8eca2ef050
[2019-12-05 07:50:58.149]  net  new job from gulf.moneroocean.stream:10064 diff 168054 algo rx/0 height 1982033
[2019-12-05 07:51:11.495] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10461,"jsonrpc":"2.0","method":"submit","params":{"id":"c011900
[2019-12-05 07:51:11.650] [gulf.moneroocean.stream:10064] received (66 bytes): "{"id":10461,"jsonrpc":"2.0","error":null,"result":{"status":"OK"}}
[2019-12-05 07:51:11.650]  cpu  accepted (10451/0) diff 168054 (156 ms)
[2019-12-05 07:51:11.948] speed 10s/60s/15m 6307.8 6310.1 6002.7 H/s max 6371.7 H/s
[2019-12-05 07:51:58.169] [gulf.moneroocean.stream:10064] received (419 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0c0cd8eca2ef050
[2019-12-05 07:51:58.169]  net  new job from gulf.moneroocean.stream:10064 diff 132458 algo rx/0 height 1982033
[2019-12-05 07:52:12.007] speed 10s/60s/15m 6308.3 6308.9 6002.7 H/s max 6371.7 H/s
[2019-12-05 07:52:48.092] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10462,"jsonrpc":"2.0","method":"submit","params":{"id":"c011900
[2019-12-05 07:52:48.223] [gulf.moneroocean.stream:10064] received (66 bytes): "{"id":10462,"jsonrpc":"2.0","error":null,"result":{"status":"OK"}}
[2019-12-05 07:52:48.223]  cpu  accepted (10452/0) diff 132458 (132 ms)
[2019-12-05 07:52:51.865] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10463,"jsonrpc":"2.0","method":"submit","params":{"id":"c011900
[2019-12-05 07:52:51.982] [gulf.moneroocean.stream:10064] received (66 bytes): "{"id":10463,"jsonrpc":"2.0","error":null,"result":{"status":"OK"}}
[2019-12-05 07:52:51.982]  cpu  accepted (10453/0) diff 132458 (118 ms)
[2019-12-05 07:52:52.026] [gulf.moneroocean.stream:10064] received (419 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0c0cd8eca2ef050
[2019-12-05 07:52:52.026]  net  new job from gulf.moneroocean.stream:10064 diff 38204 algo rx/0 height 1982033




[2019-12-05 07:53:00.931] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10464,"jsonrpc":"2.0","method":"submit","params":{"id":"c011900
[2019-12-05 07:53:00.993] [gulf.moneroocean.stream:10064] received (75 bytes): "{"id":10464,"jsonrpc":"2.0","error":{"code":-1,"message":"Invalid
[2019-12-05 07:53:00.993]  cpu  rejected (10453/1) diff 38204 "Invalid job id" (62 ms)
[2019-12-05 07:53:05.603] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10465,"jsonrpc":"2.0","method":"submit","params":{"id":"c011900
[2019-12-05 07:53:05.662] [gulf.moneroocean.stream:10064] received (75 bytes): "{"id":10465,"jsonrpc":"2.0","error":{"code":-1,"message":"Invalid
[2019-12-05 07:53:05.662]  cpu  rejected (10453/2) diff 38204 "Invalid job id" (60 ms)
[2019-12-05 07:53:07.724] [gulf.moneroocean.stream:10064] received (419 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0c0ce3eea2ef059
[2019-12-05 07:53:07.724]  net  new job from gulf.moneroocean.stream:10064 diff 38204 algo rx/0 height 1982034
[2019-12-05 07:53:07.741] [gulf.moneroocean.stream:10064] received (419 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0c0ce3eea2ef059
[2019-12-05 07:53:07.741]  net  new job from gulf.moneroocean.stream:10064 diff 132446 algo rx/0 height 1982034
[2019-12-05 07:53:08.169] [gulf.moneroocean.stream:10064] send (237 bytes): "{"id":10466,"jsonrpc":"2.0","method":"submit","params":{"id":"c011900
[2019-12-05 07:53:08.456] [gulf.moneroocean.stream:10064] received (66 bytes): "{"id":10466,"jsonrpc":"2.0","error":null,"result":{"status":"OK"}}
[2019-12-05 07:53:08.456]  cpu  accepted (10454/2) diff 132446 (288 ms)
```

## MoneroOcean | 2019-12-05T15:45:17+00:00
Also it seems to be issue that miner does not try to reconnect after submitting the same jobs and getting endless "Invalid job id" from the pool. I can try to drop connection from the pool in this case.

## xmrig | 2019-12-05T16:28:59+00:00
I will more detailed look into this issue tomorrow, but after quick log overview (it truncated at line ends, but seems contains all required data):

1. Miner not reconnect because `Invalid job id` not listed as critical error https://github.com/xmrig/xmrig/blob/master/src/base/net/stratum/Client.cpp#L323
2. Seems `onConnect` callback called twice (main bug, need investigate) and handler did't check for client is already connected (second bug). https://github.com/xmrig/xmrig/blob/master/src/base/net/stratum/Client.cpp#L966

Miner sent login request twice, you can simulate what happen in that case.
Thank you.

## MoneroOcean | 2019-12-05T16:41:11+00:00
If miner is sending login twice pool will assign two internal workers with different miner ids for that connection. This logic is for all nodejs-pool (it will happen even if "id" parameter in login request is the same). This is needed for stuff like Atreides proxies that bundles many miners into one TCP/IP connection.

Do you still need full/not truncated log? I have some difficulties getting it from the server :)

## xmrig | 2019-12-06T00:38:48+00:00
> Do you still need full/not truncated log?

Current log is OK.
Thank you

## xmrig | 2019-12-06T07:21:22+00:00
I added some workarounds, but still can't catch the root cause.
Thank you.

## MoneroOcean | 2019-12-06T08:28:31+00:00
You can add extra debug log messages that can help to understand this better. I will continue testing.

## xmrig | 2020-04-23T05:15:01+00:00
Should be fixed by https://github.com/xmrig/xmrig/commit/ca7ff4e90b1806c48e7327a71e3adcb8e5884a2e
Thank you

# Action History
- Created by: MoneroOcean | 2019-11-20T02:51:36+00:00
- Closed at: 2020-06-02T14:34:39+00:00
