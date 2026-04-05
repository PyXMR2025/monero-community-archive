---
title: pause-on-active does not work
source_url: https://github.com/xmrig/xmrig/issues/3276
author: NoahGNielsen
assignees: []
labels: []
created_at: '2023-05-27T17:09:13+00:00'
updated_at: '2023-05-28T14:34:23+00:00'
type: issue
status: closed
closed_at: '2023-05-28T14:34:22+00:00'
---

# Original Description
**Describe the bug**
The feature pause-on-active does not work, idk why

**To Reproduce**
activate pause-on-active

**Expected behavior**
pause xmrig if the pc is active

**Required data**
 - Miner log as text or screenshot:
 `* ABOUT        XMRig/6.19.2-mo1 gcc/11.2.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz (1) 64-bit AES
                L2:2.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       5.7/15.7 GB (36%)
                DIMM_A0: 8 GB DDR4 @ 3200 MHz M471A1G44AB0-CWE    
                DIMM_B0: 8 GB DDR4 @ 3200 MHz HMA81GS6DJR8N-XN    
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - X415JAB
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      gulf.moneroocean.stream:10004  algo auto
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-05-27 18:38:07.638]  net      use pool gulf.moneroocean.stream:10004  51.75.64.249
[2023-05-27 18:38:07.639]  net      new job from gulf.moneroocean.stream:10004 diff 9427 algo panthera height 741118 (1 tx)
[2023-05-27 18:38:07.639]  cpu      use argon2 implementation AVX-512F
[2023-05-27 18:38:07.795]  msr      register values for "intel" preset have been set successfully (157 ms)
[2023-05-27 18:38:07.795]  randomx  init dataset algo panthera (8 threads) seed 5caa3232d9b0aa03...
[2023-05-27 18:38:07.796]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2023-05-27 18:38:07.913]  randomx  dataset ready (118 ms)
[2023-05-27 18:38:07.913]  cpu      use profile  panthera  (4 threads) scratchpad 256 KB
[2023-05-27 18:38:07.959]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 1024 KB (46 ms)
[2023-05-27 18:38:15.509]  cpu      accepted (1/0) diff 9427 (66 ms)
[2023-05-27 18:38:16.099]  cpu      accepted (2/0) diff 9427 (41 ms)
[2023-05-27 18:38:16.968]  cpu      accepted (3/0) diff 9427 (66 ms)
[2023-05-27 18:38:22.591]  net      new job from gulf.moneroocean.stream:10004 diff 56743 algo panthera height 741118 (1 tx)
[2023-05-27 18:38:51.115]  cpu      accepted (4/0) diff 56743 (110 ms)
[2023-05-27 18:39:08.628]  miner    speed 10s/60s/15m 2216.6 2094.4 n/a H/s max 2265.2 H/s
[2023-05-27 18:39:22.649]  net      new job from gulf.moneroocean.stream:10004 diff 34011 algo panthera height 741118 (1 tx)
[2023-05-27 18:39:40.557]  cpu      accepted (5/0) diff 34011 (70 ms)
[2023-05-27 18:39:55.846]  cpu      accepted (6/0) diff 34011 (68 ms)
[2023-05-27 18:40:07.210]  cpu      accepted (7/0) diff 34011 (138 ms)
[2023-05-27 18:40:09.284]  miner    speed 10s/60s/15m 1748.8 2147.9 n/a H/s max 2330.8 H/s
[2023-05-27 18:40:10.844]  cpu      accepted (8/0) diff 34011 (67 ms)
[2023-05-27 18:40:22.917]  net      new job from gulf.moneroocean.stream:10004 diff 49025 algo panthera height 741118 (1 tx)
[2023-05-27 18:40:29.330]  cpu      accepted (9/0) diff 49025 (25 ms)
[2023-05-27 18:40:33.226]  cpu      accepted (10/0) diff 49025 (120 ms)
[2023-05-27 18:40:44.938]  cpu      accepted (11/0) diff 49025 (66 ms)
[2023-05-27 18:41:09.963]  miner    speed 10s/60s/15m 1684.1 1700.2 n/a H/s max 2330.8 H/s
[2023-05-27 18:41:11.207]  cpu      accepted (12/0) diff 49025 (154 ms)
[2023-05-27 18:41:14.228]  cpu      accepted (13/0) diff 49025 (125 ms)
[2023-05-27 18:41:23.149]  net      new job from gulf.moneroocean.stream:10004 diff 71535 algo panthera height 741118 (1 tx)
[2023-05-27 18:42:10.698]  miner    speed 10s/60s/15m 1733.3 1667.6 n/a H/s max 2330.8 H/s
[2023-05-27 18:42:23.392]  net      new job from gulf.moneroocean.stream:10004 diff 54685 algo panthera height 741118 (1 tx)
[2023-05-27 18:43:11.356]  miner    speed 10s/60s/15m 1726.0 1729.9 n/a H/s max 2330.8 H/s
[2023-05-27 18:44:04.535]  cpu      accepted (14/0) diff 54685 (69 ms)
[2023-05-27 18:44:12.048]  miner    speed 10s/60s/15m 2154.2 1819.9 n/a H/s max 2330.8 H/s
[2023-05-27 18:44:18.627]  cpu      accepted (15/0) diff 54685 (79 ms)
[2023-05-27 18:44:33.138]  cpu      accepted (16/0) diff 54685 (68 ms)
[2023-05-27 18:44:43.377]  cpu      accepted (17/0) diff 54685 (66 ms)
[2023-05-27 18:45:12.779]  miner    speed 10s/60s/15m 2392.4 2348.8 n/a H/s max 2398.3 H/s
[2023-05-27 18:45:43.657]  cpu      accepted (18/0) diff 54685 (27 ms)
[2023-05-27 18:45:45.879]  cpu      accepted (19/0) diff 54685 (68 ms)
[2023-05-27 18:45:47.635]  cpu      accepted (20/0) diff 54685 (66 ms)
[2023-05-27 18:46:13.685]  miner    speed 10s/60s/15m 2336.9 2370.8 n/a H/s max 2411.6 H/s
[2023-05-27 18:46:44.418]  net      new job from gulf.moneroocean.stream:10004 diff 51359 algo panthera height 741119 (5 tx)
[2023-05-27 18:46:49.679]  cpu      accepted (21/0) diff 51359 (66 ms)
[2023-05-27 18:47:05.119]  cpu      accepted (22/0) diff 51359 (69 ms)
[2023-05-27 18:47:14.349]  miner    speed 10s/60s/15m 1894.8 2222.5 n/a H/s max 2411.6 H/s
[2023-05-27 18:47:17.892]  miner    on battery power
[2023-05-27 18:47:17.892]  miner    paused
[2023-05-27 18:47:29.058]  miner    on AC power
[2023-05-27 18:47:29.058]  miner    resumed
[2023-05-27 18:47:35.866]  cpu      accepted (23/0) diff 51359 (66 ms)
[2023-05-27 18:47:38.485]  cpu      accepted (24/0) diff 51359 (68 ms)
[2023-05-27 18:47:51.165]  cpu      accepted (25/0) diff 51359 (65 ms)
[2023-05-27 18:48:15.247]  miner    speed 10s/60s/15m 2441.0 1764.5 n/a H/s max 2441.0 H/s
[2023-05-27 18:48:17.256]  cpu      accepted (26/0) diff 51359 (80 ms)
[2023-05-27 18:48:20.285]  cpu      accepted (27/0) diff 51359 (25 ms)
[2023-05-27 18:48:43.999]  cpu      accepted (28/0) diff 51359 (67 ms)
[2023-05-27 18:48:48.693]  cpu      accepted (29/0) diff 51359 (67 ms)
[2023-05-27 18:48:56.653]  cpu      accepted (30/0) diff 51359 (67 ms)
[2023-05-27 18:49:16.059]  miner    speed 10s/60s/15m 2245.6 2286.5 n/a H/s max 2443.9 H/s
[2023-05-27 18:49:22.052]  cpu      accepted (31/0) diff 51359 (25 ms)
[2023-05-27 18:49:23.545]  net      new job from gulf.moneroocean.stream:10004 diff 62757 algo panthera height 741119 (5 tx)
[2023-05-27 18:49:26.690]  cpu      accepted (32/0) diff 62757 (90 ms)
[2023-05-27 18:49:40.123]  cpu      accepted (33/0) diff 62757 (25 ms)
[2023-05-27 18:49:50.409]  cpu      accepted (34/0) diff 62757 (66 ms)
[2023-05-27 18:50:02.728]  cpu      accepted (35/0) diff 62757 (26 ms)
[2023-05-27 18:50:16.779]  miner    speed 10s/60s/15m 2217.9 2260.8 n/a H/s max 2443.9 H/s
[2023-05-27 18:50:25.580]  cpu      accepted (36/0) diff 62757 (29 ms)
[2023-05-27 18:50:26.972]  cpu      accepted (37/0) diff 62757 (26 ms)
[2023-05-27 18:51:17.490]  miner    speed 10s/60s/15m 2392.4 2289.3 n/a H/s max 2443.9 H/s
[2023-05-27 18:51:35.784]  cpu      accepted (38/0) diff 62757 (32 ms)
[2023-05-27 18:52:10.496]  cpu      accepted (39/0) diff 62757 (25 ms)
[2023-05-27 18:52:12.716]  cpu      accepted (40/0) diff 62757 (66 ms)
[2023-05-27 18:52:14.702]  net      new job from gulf.moneroocean.stream:10004 diff 67488 algo panthera height 741120 (1 tx)
[2023-05-27 18:52:18.415]  miner    speed 10s/60s/15m 2265.8 2219.4 n/a H/s max 2443.9 H/s
[2023-05-27 18:53:07.615]  net      new job from gulf.moneroocean.stream:10004 diff 69355 algo panthera height 741121 (1 tx)
[2023-05-27 18:53:19.091]  miner    speed 10s/60s/15m 2230.3 2264.4 2079.6 H/s max 2443.9 H/s
[2023-05-27 18:53:27.403]  config   "C:\Users\noahg\moneroocean\config.json" was changed, reloading configuration
[2023-05-27 18:53:27.415]     },
[2023-05-27 18:53:27.415]     "pause-on-battery": t,
[2023-05-27 18:53:27.415]                          ^
[2023-05-27 18:53:27.415] C:\Users\noahg\moneroocean\config.json<line:202, position:26>: "Invalid value."
[2023-05-27 18:53:27.415]  config   reloading failed
[2023-05-27 18:53:29.955]  config   "C:\Users\noahg\moneroocean\config.json" was changed, reloading configuration
[2023-05-27 18:53:31.858]  cpu      accepted (41/0) diff 69355 (24 ms)
[2023-05-27 18:53:37.915]  cpu      accepted (42/0) diff 69355 (26 ms)
[2023-05-27 18:53:41.897]  cpu      accepted (43/0) diff 69355 (33 ms)
[2023-05-27 18:54:19.935]  miner    speed 10s/60s/15m 2129.3 2199.4 2084.3 H/s max 2443.9 H/s
[2023-05-27 18:54:29.251]  cpu      accepted (44/0) diff 69355 (28 ms)
[2023-05-27 18:54:55.052]  net      new job from gulf.moneroocean.stream:10004 diff 67224 algo panthera height 741122 (1 tx)
[2023-05-27 18:55:20.037]  cpu      accepted (45/0) diff 67224 (71 ms)
[2023-05-27 18:55:20.747]  miner    speed 10s/60s/15m 2332.7 2307.9 2101.7 H/s max 2443.9 H/s
[2023-05-27 18:56:03.636]  cpu      accepted (46/0) diff 67224 (27 ms)
[2023-05-27 18:56:11.067]  cpu      accepted (47/0) diff 67224 (135 ms)
[2023-05-27 18:56:21.544]  miner    speed 10s/60s/15m 2312.8 2211.8 2136.5 H/s max 2443.9 H/s
[2023-05-27 18:56:23.497]  cpu      accepted (48/0) diff 67224 (67 ms)
[2023-05-27 18:56:58.051]  cpu      accepted (49/0) diff 67224 (105 ms)
[2023-05-27 18:57:17.202]  cpu      accepted (50/0) diff 67224 (74 ms)
[2023-05-27 18:57:22.293]  miner    speed 10s/60s/15m 2247.2 2226.3 2173.3 H/s max 2443.9 H/s
[2023-05-27 18:57:32.607]  config   "C:\Users\noahg\moneroocean\config.json" was changed, reloading configuration
[2023-05-27 18:57:45.825]  cpu      accepted (51/0) diff 67224 (25 ms)
[2023-05-27 18:58:10.536]  cpu      accepted (52/0) diff 67224 (148 ms)
[2023-05-27 18:58:23.115]  miner    speed 10s/60s/15m 2350.4 2236.4 2207.8 H/s max 2443.9 H/s
[2023-05-27 18:58:35.261]  cpu      accepted (53/0) diff 67224 (39 ms)
[2023-05-27 18:59:23.864]  miner    speed 10s/60s/15m 2234.4 2245.2 2228.8 H/s max 2443.9 H/s
[2023-05-27 18:59:51.000]  cpu      accepted (54/0) diff 67224 (25 ms)
[2023-05-27 19:00:21.613]  net      new job from gulf.moneroocean.stream:10004 diff 67274 algo panthera height 741123 (1 tx)
[2023-05-27 19:00:24.654]  miner    speed 10s/60s/15m 2197.5 1899.8 2197.7 H/s max 2443.9 H/s
[2023-05-27 19:00:40.689]  cpu      accepted (55/0) diff 67274 (57 ms)
[2023-05-27 19:01:07.858]  cpu      accepted (56/0) diff 67274 (130 ms)
[2023-05-27 19:01:25.378]  miner    speed 10s/60s/15m 2282.1 2224.5 2188.8 H/s max 2443.9 H/s
[2023-05-27 19:02:12.188]  net      new job from gulf.moneroocean.stream:10004 diff 65827 algo panthera height 741124 (1 tx)
[2023-05-27 19:02:20.063]  cpu      accepted (57/0) diff 65827 (147 ms)
[2023-05-27 19:02:26.200]  miner    speed 10s/60s/15m 2399.0 2347.8 2221.3 H/s max 2443.9 H/s
[2023-05-27 19:02:29.544]  cpu      accepted (58/0) diff 65827 (66 ms)
[2023-05-27 19:02:31.837]  cpu      accepted (59/0) diff 65827 (24 ms)
[2023-05-27 19:02:58.637]  cpu      accepted (60/0) diff 65827 (66 ms)
[2023-05-27 19:03:26.947]  miner    speed 10s/60s/15m 2360.6 2367.2 2237.5 H/s max 2443.9 H/s
[2023-05-27 19:04:14.759]  cpu      accepted (61/0) diff 65827 (70 ms)
[2023-05-27 19:04:19.087]  cpu      accepted (62/0) diff 65827 (109 ms)
[2023-05-27 19:04:27.696]  miner    speed 10s/60s/15m 2312.2 2316.1 2239.4 H/s max 2443.9 H/s
[2023-05-27 19:04:47.712]  cpu      accepted (63/0) diff 65827 (71 ms)
[2023-05-27 19:05:13.294]  cpu      accepted (64/0) diff 65827 (67 ms)
[2023-05-27 19:05:28.527]  miner    speed 10s/60s/15m 2153.8 2319.1 2244.1 H/s max 2443.9 H/s
[2023-05-27 19:05:36.966]  cpu      accepted (65/0) diff 65827 (258 ms)
[2023-05-27 19:06:14.201]  cpu      accepted (66/0) diff 65827 (32 ms)
[2023-05-27 19:06:29.273]  miner    speed 10s/60s/15m 1938.5 2006.4 2223.3 H/s max 2443.9 H/s
[2023-05-27 19:06:47.068]  cpu      accepted (67/0) diff 65827 (27 ms)
[2023-05-27 19:06:49.036]  cpu      accepted (68/0) diff 65827 (24 ms)
[2023-05-27 19:06:52.222]  net      new job from gulf.moneroocean.stream:10004 diff 65827 algo panthera height 741125 (6 tx)
[2023-05-27 19:07:30.076]  miner    speed 10s/60s/15m 2251.7 2169.0 2221.1 H/s max 2443.9 H/s
[2023-05-27 19:07:54.514]  cpu      accepted (69/0) diff 65827 (67 ms)
`
 - Config file or command line (without wallets):
 `{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": true,
    "colors": false,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": 0,
        "mode": "auto",
        "1gb-pages": false,
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
        "memory-pool": true,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "cn/2": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
        ],
        "cn/gpu": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6]
        ],
        "panthera": [0, 2, 4, 6],
        "rx": [0, 2, 4, 6],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn-lite/0": false,
        "cn/0": false,
        "panthera": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn-lite/0": false,
        "cn/0": false,
        "panthera": false
    },
    "log-file": "C:\\Users\\noahg\\moneroocean\\xmrig.log",
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "gulf.moneroocean.stream:10004 ",
            "user": "",
            "pass": "",
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
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "rebench-algo": false,
    "bench-algo-time": 20,
    "algo-min-time": 0,
    "algo-perf": {
        "cn/0": 101.93534198372554,
        "cn/1": 118.18281575770877,
        "cn/2": 118.18281575770877,
        "cn/r": 118.18281575770877,
        "cn/fast": 236.36563151541753,
        "cn/half": 236.36563151541753,
        "cn/xao": 118.18281575770877,
        "cn/rto": 118.18281575770877,
        "cn/rwz": 157.577087676945,
        "cn/zls": 157.577087676945,
        "cn/double": 59.09140787885438,
        "cn/ccx": 203.87068396745107,
        "cn-lite/0": 520.0869745288879,
        "cn-lite/1": 520.0869745288879,
        "cn-heavy/xhv": 53.69718309859155,
        "cn-pico": 4231.399468556245,
        "cn-pico/tlo": 4231.399468556245,
        "cn/gpu": 37.79732811990876,
        "rx/0": 645.2720274628108,
        "rx/arq": 7451.046377116416,
        "rx/graft": 1004.7036688617121,
        "rx/sfx": 645.2720274628108,
        "panthera": 1901.7407718120805,
        "argon2/chukwav2": 4262.510513036164,
        "kawpow": 1.94918958868285e-153,
        "ghostrider": 181.025534565082
    },
    "pause-on-battery": true,
    "pause-on-active": 120
}`
 - OS: Windoes 10 Home
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2023-05-28T09:48:56+00:00
```
[2023-05-27 18:53:27.415] "pause-on-battery": t,
[2023-05-27 18:53:27.415] ^
[2023-05-27 18:53:27.415] C:\Users\noahg\moneroocean\config.json<line:202, position:26>: "Invalid value."
[2023-05-27 18:53:27.415] config reloading failed
```
Maybe this is why. Double check that your config file is valid. Also, this is MO version, it's not supported. Try with the official release.

## NoahGNielsen | 2023-05-28T14:34:22+00:00
ok thx

# Action History
- Created by: NoahGNielsen | 2023-05-27T17:09:13+00:00
- Closed at: 2023-05-28T14:34:22+00:00
