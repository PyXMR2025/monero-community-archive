---
title: After donate pool xmrig reset nonce for main pool job causing duplicate shares
source_url: https://github.com/xmrig/xmrig/issues/3669
author: MoneroOcean
assignees: []
labels:
- bug
created_at: '2025-06-17T05:58:23+00:00'
updated_at: '2026-02-28T09:55:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After donate pool xmrig reset nonce for main pool job causing duplicate shares. Reproduced using XMRig/6.22.2. See nonce 6e060000:

```
[2025-06-16 18:56:25.517] [gulf.moneroocean.stream:20001] received (369 bytes): "{"method":"job","params":{"blob":"00000081f7c6601ecb0ccc2ef90444148e448c227b590022778dcb471174a766d42112000000000000000002000005d19ace9700000000000000000000000000000000000000000000000000","algo":"rx/0","height":30294,"seed_hash":"a8e801d8bed47e68d2196986dfebbef5dfa6bcd1215c831e48cee4b82c2ea89e","job_id":"30810294","target":"f5760000","id":"30597809"},"jsonrpc":"2.0"}"
[2025-06-16 18:56:25.517]  net      new job from gulf.moneroocean.stream:20001 diff 141035 algo rx/0 height 30294
[2025-06-16 18:56:27.204]  miner    speed 10s/60s/15m 5466.8 5617.0 5615.1 H/s max 6108.9 H/s

[2025-06-16 18:56:27.954] [gulf.moneroocean.stream:20001] send (187 bytes): "{"id":172,"jsonrpc":"2.0","method":"submit","params":{"id":"30597809","job_id":"30810294","nonce":"6e060000","result":"d71d75a140ca41f8667de7bcfecebc98e9064b389eb2c3cd56eb101561240000"}}"

[2025-06-16 18:56:27.954] [gulf.moneroocean.stream:20001] TLS send     (209 bytes)
[2025-06-16 18:56:28.072] [gulf.moneroocean.stream:20001] TLS received (87 bytes)
[2025-06-16 18:56:28.072] [gulf.moneroocean.stream:20001] received (64 bytes): "{"jsonrpc":"2.0","id":172,"error":null,"result":{"status":"OK"}}"
[2025-06-16 18:56:28.072]  cpu      accepted (171/0) diff 141035 (118 ms)
[2025-06-16 18:56:39.783] [gulf.moneroocean.stream:20001] send (187 bytes): "{"id":173,"jsonrpc":"2.0","method":"submit","params":{"id":"30597809","job_id":"30810294","nonce":"2ba80100","result":"09e8c78e6e6a855ad289c7ce669dbd0da92fb2ffe8452de0c61645da9e330000"}}"
[2025-06-16 18:56:39.783] [gulf.moneroocean.stream:20001] TLS send     (209 bytes)
[2025-06-16 18:56:40.090] [gulf.moneroocean.stream:20001] TLS received (87 bytes)
[2025-06-16 18:56:40.090] [gulf.moneroocean.stream:20001] received (64 bytes): "{"jsonrpc":"2.0","id":173,"error":null,"result":{"status":"OK"}}"
[2025-06-16 18:56:40.090]  cpu      accepted (172/0) diff 141035 (307 ms)
[2025-06-16 18:56:44.864] [gulf.moneroocean.stream:20001] send (187 bytes): "{"id":174,"jsonrpc":"2.0","method":"submit","params":{"id":"30597809","job_id":"30810294","nonce":"b6360200","result":"965d5aff293368003fabfe7c340969fe08b24cb92f193b5dfec847c13f610000"}}"
[2025-06-16 18:56:44.864] [gulf.moneroocean.stream:20001] TLS send     (209 bytes)
[2025-06-16 18:56:45.177] [gulf.moneroocean.stream:20001] TLS received (87 bytes)
[2025-06-16 18:56:45.177] [gulf.moneroocean.stream:20001] received (64 bytes): "{"jsonrpc":"2.0","id":174,"error":null,"result":{"status":"OK"}}"
[2025-06-16 18:56:45.177]  cpu      accepted (173/0) diff 141035 (313 ms)
[2025-06-16 18:56:58.720] [gulf.moneroocean.stream:20001] send (187 bytes): "{"id":175,"jsonrpc":"2.0","method":"submit","params":{"id":"30597809","job_id":"30810294","nonce":"7e5e0100","result":"6af39eb5c86434edf5d93420e588209672b2bfafa2b1af4dd8fe20d8bd1b0000"}}"
[2025-06-16 18:56:58.720] [gulf.moneroocean.stream:20001] TLS send     (209 bytes)
[2025-06-16 18:56:58.867] [gulf.moneroocean.stream:20001] TLS received (87 bytes)
[2025-06-16 18:56:58.867] [gulf.moneroocean.stream:20001] received (64 bytes): "{"jsonrpc":"2.0","id":175,"error":null,"result":{"status":"OK"}}"
[2025-06-16 18:56:58.867]  cpu      accepted (174/0) diff 141035 (147 ms)
[2025-06-16 18:57:27.238]  miner    speed 10s/60s/15m 5846.4 5815.1 5615.1 H/s max 6108.9 H/s
[2025-06-16 18:57:28.400] [gulf.moneroocean.stream:20001] send (187 bytes): "{"id":176,"jsonrpc":"2.0","method":"submit","params":{"id":"30597809","job_id":"30810294","nonce":"25b30500","result":"7e11daff782de728f97a53b135f08e119d86340a5b0196bd4bf717638b2c0000"}}"
[2025-06-16 18:57:28.400] [gulf.moneroocean.stream:20001] TLS send     (209 bytes)
[2025-06-16 18:57:28.759] [gulf.moneroocean.stream:20001] TLS received (87 bytes)
[2025-06-16 18:57:28.759] [gulf.moneroocean.stream:20001] received (64 bytes): "{"jsonrpc":"2.0","id":176,"error":null,"result":{"status":"OK"}}"
[2025-06-16 18:57:28.760]  cpu      accepted (175/0) diff 141035 (359 ms)
[2025-06-16 18:57:52.965] [donate.ssl.xmrig.com:443] state: "unconnected" -> "host-lookup"
[2025-06-16 18:57:53.000] [donate.ssl.xmrig.com:443] state: "host-lookup" -> "connecting"
[2025-06-16 18:57:53.156] [donate.ssl.xmrig.com:443] state: "connecting" -> "connected"
[2025-06-16 18:57:53.157] [donate.ssl.xmrig.com:443] TLS send     (293 bytes)
[2025-06-16 18:57:53.316] [donate.ssl.xmrig.com:443] TLS received (1448 bytes)
[2025-06-16 18:57:53.317] [donate.ssl.xmrig.com:443] TLS received (1448 bytes)
[2025-06-16 18:57:53.317] [donate.ssl.xmrig.com:443] TLS received (1668 bytes)
[2025-06-16 18:57:53.318] [donate.ssl.xmrig.com:443] send (623 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"794ea9caef8d996bb4da0f676b6b1f829b35b4f40a459e69db3bf0810fd05206","pass":"x","agent":"XMRig/6.22.2 (Linux x86_64) libuv/1.48.0 gcc/13.3.0","algo":["rx/0","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","cn/1","rx/wow","rx/arq","rx/graft","rx/sfx","rx/yada","argon2/chukwa","argon2/chukwav2","argon2/ninja","ghostrider"],"diff":141035,"height":30294,"seed_hash":"a8e801d8bed47e68d2196986dfebbef5dfa6bcd1215c831e48cee4b82c2ea89e"}}"
[2025-06-16 18:57:53.318] [donate.ssl.xmrig.com:443] TLS send     (725 bytes)
[2025-06-16 18:57:53.494] [donate.ssl.xmrig.com:443] TLS received (478 bytes)
[2025-06-16 18:57:53.494] [donate.ssl.xmrig.com:443] TLS received (510 bytes)
[2025-06-16 18:57:53.494] [donate.ssl.xmrig.com:443] received (487 bytes): "{"jsonrpc":"2.0","id":1,"error":null,"result":{"id":"e917c8bfac8fdb4e","job":{"blob":"10109d97c3c20639e4a88de37e69f8af1235afa0f50a20a02d9ad6d0b979c642bc68aa746bebf40000008fafef566106b728e059a9c4f304d99f81bd7a3804a5bdc2a63f088008f97c382a27","job_id":"d0xdXRIBKUD+0cON2Cs4EziVY6XL","target":"c6100000","algo":"rx/0","height":3435647,"seed_hash":"27318467c624a537d02531b291e253a2a02a9dc194810178586f536e3391c66f"},"extensions":["algo","nicehash","connect","tls","keepalive"],"status":"OK"}}"
[2025-06-16 18:57:53.494]  net      dev donate started
[2025-06-16 18:57:53.494]  net      new job from donate.ssl.xmrig.com:443 diff 1000K algo rx/0 height 3435647 (39 tx)
[2025-06-16 18:57:53.494]  randomx  init dataset algo rx/0 (16 threads) seed 27318467c624a537...
[2025-06-16 18:57:55.148]  randomx  dataset ready (1654 ms)
[2025-06-16 18:58:00.371] [donate.ssl.xmrig.com:443] TLS received (398 bytes)
[2025-06-16 18:58:00.371] [donate.ssl.xmrig.com:443] received (375 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"1010a897c3c20639e4a88de37e69f8af1235afa0f50a20a02d9ad6d0b979c642bc68aa746bebf40000008f3fb48a6d6a9d3b4b1254d26085f720f0672c9115d3e57aa41bf4ab5004abb2b229","job_id":"Cuwt9pVBjBvBxY8GvbVZzr37NB8B","target":"c6100000","algo":"rx/0","height":3435647,"seed_hash":"27318467c624a537d02531b291e253a2a02a9dc194810178586f536e3391c66f"}}"
[2025-06-16 18:58:00.371]  net      new job from donate.ssl.xmrig.com:443 diff 1000K algo rx/0 height 3435647 (41 tx)
[2025-06-16 18:58:10.486] [donate.ssl.xmrig.com:443] TLS received (398 bytes)
[2025-06-16 18:58:10.486] [donate.ssl.xmrig.com:443] received (375 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"1010b297c3c20639e4a88de37e69f8af1235afa0f50a20a02d9ad6d0b979c642bc68aa746bebf40000008f3591c31699bc91664f05ad4ad6b3fb175b60992e0e9ed945092969373249e8cb2b","job_id":"Rmt4VXWLhn4PBOYlJKeG2naBcq3D","target":"c6100000","algo":"rx/0","height":3435647,"seed_hash":"27318467c624a537d02531b291e253a2a02a9dc194810178586f536e3391c66f"}}"
[2025-06-16 18:58:10.486]  net      new job from donate.ssl.xmrig.com:443 diff 1000K algo rx/0 height 3435647 (43 tx)
[2025-06-16 18:58:21.662] [donate.ssl.xmrig.com:443] TLS received (398 bytes)
[2025-06-16 18:58:21.662] [donate.ssl.xmrig.com:443] received (375 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"1010bd97c3c20639e4a88de37e69f8af1235afa0f50a20a02d9ad6d0b979c642bc68aa746bebf40000008fdf130671818cead10a7b1e18d59f609f84b69a9a672cf7440f641e40b160e9ae2c","job_id":"BVxIwio9ve6xscE5cbzxLm4Q4l8V","target":"c6100000","algo":"rx/0","height":3435647,"seed_hash":"27318467c624a537d02531b291e253a2a02a9dc194810178586f536e3391c66f"}}"
[2025-06-16 18:58:21.662]  net      new job from donate.ssl.xmrig.com:443 diff 1000K algo rx/0 height 3435647 (44 tx)
[2025-06-16 18:58:27.278]  miner    speed 10s/60s/15m 5876.7 5701.5 5604.3 H/s max 6108.9 H/s

[2025-06-16 18:58:31.997] [donate.ssl.xmrig.com:443] TLS received (398 bytes)
[2025-06-16 18:58:31.997] [donate.ssl.xmrig.com:443] received (375 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"1010c797c3c20639e4a88de37e69f8af1235afa0f50a20a02d9ad6d0b979c642bc68aa746bebf40000008f7172d08e299533908cd61665a7b692d212901797aca8aa62db19ae4340adef022f","job_id":"9d5+qpBw74qqh+vf3CVEVc/vep43","target":"c6100000","algo":"rx/0","height":3435647,"seed_hash":"27318467c624a537d02531b291e253a2a02a9dc194810178586f536e3391c66f"}}"
[2025-06-16 18:58:31.997]  net      new job from donate.ssl.xmrig.com:443 diff 1000K algo rx/0 height 3435647 (47 tx)
[2025-06-16 18:58:42.432] [donate.ssl.xmrig.com:443] TLS received (398 bytes)
[2025-06-16 18:58:42.432] [donate.ssl.xmrig.com:443] received (375 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"1010d297c3c20639e4a88de37e69f8af1235afa0f50a20a02d9ad6d0b979c642bc68aa746bebf40000008f014fcf3734fd62166199882da2b245eff3349498c43b2b6ac392b261c1eb061430","job_id":"mRhBIjSs5nbDjUZ69tLBbG4PjRAo","target":"c6100000","algo":"rx/0","height":3435647,"seed_hash":"27318467c624a537d02531b291e253a2a02a9dc194810178586f536e3391c66f"}}"
[2025-06-16 18:58:42.432]  net      new job from donate.ssl.xmrig.com:443 diff 1000K algo rx/0 height 3435647 (48 tx)
[2025-06-16 18:58:52.718] [donate.ssl.xmrig.com:443] TLS received (398 bytes)
[2025-06-16 18:58:52.718] [donate.ssl.xmrig.com:443] received (375 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"1010dc97c3c20639e4a88de37e69f8af1235afa0f50a20a02d9ad6d0b979c642bc68aa746bebf40000008fdcde879c3ac8d2e20940dda6d3d186b311b4842399fe952cb97ec01e7a179fb031","job_id":"D9Kdu1k8ZXryZ8X3oVmcQLo/aFzq","target":"c6100000","algo":"rx/0","height":3435647,"seed_hash":"27318467c624a537d02531b291e253a2a02a9dc194810178586f536e3391c66f"}}"
[2025-06-16 18:58:52.718]  net      new job from donate.ssl.xmrig.com:443 diff 1000K algo rx/0 height 3435647 (49 tx)
[2025-06-16 18:58:53.495]  net      dev donate finished
[2025-06-16 18:58:53.495]  net      new job from gulf.moneroocean.stream:20001 diff 141035 algo rx/0 height 30294
[2025-06-16 18:58:53.495]  randomx  init dataset algo rx/0 (16 threads) seed a8e801d8bed47e68...
[2025-06-16 18:58:55.152]  randomx  dataset ready (1657 ms)
[2025-06-16 18:58:55.778] [donate.ssl.xmrig.com:443] state: "connected" -> "closing"
[2025-06-16 18:58:55.778] [donate.ssl.xmrig.com:443] state: "closing" -> "unconnected"


[2025-06-16 18:58:58.914] [gulf.moneroocean.stream:20001] send (187 bytes): "{"id":178,"jsonrpc":"2.0","method":"submit","params":{"id":"30597809","job_id":"30810294","nonce":"6e060000","result":"d71d75a140ca41f8667de7bcfecebc98e9064b389eb2c3cd56eb101561240000"}}"

[2025-06-16 18:58:58.914] [gulf.moneroocean.stream:20001] TLS send     (209 bytes)
[2025-06-16 18:58:59.013] [gulf.moneroocean.stream:20001] TLS received (97 bytes)
[2025-06-16 18:58:59.013] [gulf.moneroocean.stream:20001] received (74 bytes): "{"jsonrpc":"2.0","id":178,"error":{"code":-1,"message":"Duplicate share"}}"
[2025-06-16 18:58:59.013]  cpu      rejected (175/1) diff 141035 "Duplicate share" (99 ms)
[2025-06-16 18:59:12.095] [gulf.moneroocean.stream:20001] send (187 bytes): "{"id":179,"jsonrpc":"2.0","method":"submit","params":{"id":"30597809","job_id":"30810294","nonce":"2ba80100","result":"09e8c78e6e6a855ad289c7ce669dbd0da92fb2ffe8452de0c61645da9e330000"}}"
[2025-06-16 18:59:12.095] [gulf.moneroocean.stream:20001] TLS send     (209 bytes)
[2025-06-16 18:59:12.177] [gulf.moneroocean.stream:20001] TLS received (97 bytes)
[2025-06-16 18:59:12.178] [gulf.moneroocean.stream:20001] received (74 bytes): "{"jsonrpc":"2.0","id":179,"error":{"code":-1,"message":"Duplicate share"}}"
[2025-06-16 18:59:12.178]  cpu      rejected (175/2) diff 141035 "Duplicate share" (82 ms)
[2025-06-16 18:59:17.856] [gulf.moneroocean.stream:20001] send (187 bytes): "{"id":180,"jsonrpc":"2.0","method":"submit","params":{"id":"30597809","job_id":"30810294","nonce":"b6360200","result":"965d5aff293368003fabfe7c340969fe08b24cb92f193b5dfec847c13f610000"}}"
[2025-06-16 18:59:17.856] [gulf.moneroocean.stream:20001] TLS send     (209 bytes)
[2025-06-16 18:59:17.940] [gulf.moneroocean.stream:20001] TLS received (97 bytes)
[2025-06-16 18:59:17.940] [gulf.moneroocean.stream:20001] received (74 bytes): "{"jsonrpc":"2.0","id":180,"error":{"code":-1,"message":"Duplicate share"}}"
[2025-06-16 18:59:17.940]  cpu      rejected (175/3) diff 141035 "Duplicate share" (84 ms)
```

# Discussion History
## SChernykh | 2025-06-17T06:03:39+00:00
Thanks, I'll look into it.

## SChernykh | 2025-07-27T22:24:02+00:00
@MoneroOcean sorry that I took so long to look at it. It seems that your pool doesn't send job updates often enough, so XMRig switches back to the same job after the donation round. All other pools update their jobs every 15-30 seconds, so it's not an issue for them. So a quick fix on your side would be to force send new jobs after 30 seconds.

Having said that, it's still a bug in XMRig - it should detect that the job didn't change, and don't reset the nonce in this case.

## MoneroOcean | 2025-07-28T14:55:01+00:00
It is quite normal to keep jobs for several minutes for coins that do not have many transactions since block template stays the same.

## SChernykh | 2025-07-28T17:34:55+00:00
Well, it seems that the previous fix created this bug: https://github.com/xmrig/xmrig/blob/master/src/core/Miner.cpp#L593
I need to think how to rewrite this logic in a better way.

## blackmennewstyle | 2026-02-26T07:15:45+00:00
I can confirm the issue exists and `MoneroOcean` is spot on about the root cause, only happens on slower POW network with few activities (transaction, new blocks), literally most `Monero (XMR)` forks.

Right after the end of the `dev fee session`, if the pool does not send a new job, the miner will send the same solution resulting in a `rejected share`.

Maybe time to consider recording nonce temporarily at least until the mining software is stopped or closed.

Happy midweek.

## SChernykh | 2026-02-27T17:53:16+00:00
#3785 will hopefully fix this

## blackmennewstyle | 2026-02-28T09:55:10+00:00
Thank you. In the meantime, i can confirm that forcing rebroadcast of job at least every 30s somehow potentially totally mitigates that behavior 👍🏽 

# Action History
- Created by: MoneroOcean | 2025-06-17T05:58:23+00:00
