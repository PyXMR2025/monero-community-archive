---
title: v6.16.2; gr (RTM); " Invalid job id "
source_url: https://github.com/xmrig/xmrig/issues/2810
author: mynerzulu
assignees: []
labels: []
created_at: '2021-12-14T06:25:03+00:00'
updated_at: '2025-06-20T11:07:09+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:07:09+00:00'
---

# Original Description
**Describe the bug**
Notice in the mining output log, xmrig shows " Invalid job id " wile mining RTM with ghostrider algorithm.

**To Reproduce**
Running for a few days.   See this issue on different machines (Intel and AMD cpu's)

**Expected behavior**
Invalid job id"
- why does it occur?
- should it be avoided?
- does it affect hash rate and submitted shares 
- Anything I can do to help figure this out?

**Required data**
- OS:  ubuntu server 20.04.3 / linux mint
- CPU:  AMD Ryzen Threadripper 3960X;  Intel Core i9-10900T;  Intel Xeon E5-1650 v2;  Intel Xeon X5650 (vm)

Obtain info via:   cat xmrighash.log | grep rejected

Intel i9:
```
[2021-12-11 20:52:26.188]  cpu      rejected (4828/30) diff 9831 "Invalid job id" (41 ms)
[2021-12-11 21:34:12.946]  cpu      rejected (4894/31) diff 9831 "Invalid job id" (41 ms)
[2021-12-12 02:48:48.152]  cpu      rejected (5485/32) diff 19661 "Invalid job id" (53 ms)
[2021-12-12 02:49:30.507]  cpu      rejected (5488/33) diff 19661 "Invalid job id" (83 ms)
[2021-12-12 05:33:48.415]  cpu      rejected (5821/34) diff 9831 "Invalid job id" (43 ms)
[2021-12-12 07:50:45.419]  cpu      rejected (6148/35) diff 9831 "Invalid job id" (41 ms)
[2021-12-12 08:35:40.682]  cpu      rejected (6292/36) diff 9831 "Invalid job id" (42 ms)
[2021-12-12 08:39:12.779]  cpu      rejected (6303/37) diff 9831 "Invalid job id" (60 ms)
[2021-12-12 09:14:41.096]  cpu      rejected (6381/38) diff 9831 "Invalid job id" (42 ms)
[2021-12-12 10:02:23.294]  cpu      rejected (6472/39) diff 19661 "Invalid job id" (59 ms)
[2021-12-12 13:03:46.571]  cpu      rejected (6790/40) diff 9831 "Invalid job id" (41 ms)
[2021-12-12 15:09:54.155]  cpu      rejected (7001/41) diff 19661 "Invalid job id" (42 ms)
[2021-12-12 15:20:29.823]  cpu      rejected (7019/42) diff 19661 "Invalid job id" (47 ms)
[2021-12-12 16:35:29.202]  cpu      rejected (7143/43) diff 9831 "Invalid job id" (42 ms)
[2021-12-12 16:51:22.299]  cpu      rejected (7171/44) diff 14681 "Invalid job id" (45 ms)
[2021-12-13 01:33:53.323]  cpu      rejected (8219/45) diff 19661 "Invalid job id" (42 ms)
[2021-12-13 02:16:13.593]  cpu      rejected (8331/46) diff 14681 "Invalid job id" (41 ms)
[2021-12-13 08:46:37.621]  cpu      rejected (9116/47) diff 9831 "Invalid job id" (41 ms)
[2021-12-13 09:20:53.253]  cpu      rejected (9197/48) diff 14681 "Invalid job id" (48 ms)
[2021-12-13 13:33:19.636]  cpu      rejected (9718/49) diff 14681 "Invalid job id" (41 ms)
[2021-12-13 15:50:17.624]  cpu      rejected (9943/50) diff 19661 "Invalid job id" (44 ms)
[2021-12-13 16:05:07.817]  cpu      rejected (9967/51) diff 19661 "Invalid job id" (42 ms)
[2021-12-13 16:34:06.734]  cpu      rejected (10013/52) diff 9831 "Invalid job id" (47 ms)
[2021-12-13 17:45:18.003]  cpu      rejected (10189/53) diff 9831 "Invalid job id" (81 ms)
[2021-12-13 18:36:40.531]  cpu      rejected (10320/54) diff 9831 "Invalid job id" (74 ms)
[2021-12-13 20:39:23.026]  cpu      rejected (10565/55) diff 29361 "Invalid job id" (41 ms)
[2021-12-13 21:10:26.742]  cpu      rejected (10606/56) diff 14681 "Invalid job id" (59 ms)
[2021-12-13 21:48:36.683]  cpu      rejected (10680/56) diff 22952 "stale-job" (161 ms)
[2021-12-13 22:04:23.682]  cpu      rejected (10716/57) diff 19661 "Invalid job id" (41 ms)
[2021-12-13 23:07:12.781]  cpu      rejected (10864/58) diff 19661 "Invalid job id" (46 ms)
[2021-12-13 23:42:54.571]  cpu      rejected (10945/59) diff 19661 "Invalid job id" (41 ms)
[2021-12-14 01:26:43.648]  cpu      rejected (11102/60) diff 19661 "Invalid job id" (98 ms)
[2021-12-14 04:50:42.759]  cpu      rejected (11421/61) diff 19661 "Invalid job id" (42 ms)
```

lshw:
*-cpu
          product: AMD Ryzen Threadripper 3960X 24-Core Processor
          vendor: Advanced Micro Devices [AMD]
          physical id: 1
          bus info: cpu@0
          size: 3834MHz
          width: 64 bits
          capabilities: fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp x86-64 constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate sme ssbd mba sev ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca cpufreq

```
[2021-12-12 08:02:11.413]  cpu      rejected (2372/6) diff 39322 "Invalid job id" (47 ms)
[2021-12-12 08:27:33.954]  cpu      rejected (2580/7) diff 39322 "Invalid job id" (46 ms)
[2021-12-12 10:00:09.072]  cpu      rejected (3267/8) diff 58852 "Invalid job id" (42 ms)
[2021-12-12 10:35:29.035]  cpu      rejected (3485/9) diff 58852 "Invalid job id" (71 ms)
[2021-12-12 10:38:39.451]  cpu      rejected (3501/10) diff 58852 "Invalid job id" (46 ms)
[2021-12-12 11:15:24.351]  cpu      rejected (3738/11) diff 58852 "Invalid job id" (50 ms)
[2021-12-12 11:16:06.745]  cpu      rejected (3739/12) diff 58852 "Invalid job id" (46 ms)
[2021-12-12 12:08:02.885]  cpu      rejected (4064/13) diff 131072 "Invalid job id" (41 ms)
[2021-12-12 12:11:13.731]  cpu      rejected (4074/14) diff 131072 "Invalid job id" (88 ms)
[2021-12-12 12:45:56.067]  cpu      rejected (4176/15) diff 131072 "Invalid job id" (45 ms)
[2021-12-12 14:01:12.714]  cpu      rejected (4682/16) diff 58852 "Invalid job id" (44 ms)
[2021-12-12 15:15:27.443]  cpu      rejected (5085/17) diff 58852 "Invalid job id" (42 ms)
[2021-12-12 15:30:38.349]  cpu      rejected (5211/18) diff 58852 "Invalid job id" (46 ms)
[2021-12-12 15:47:56.299]  cpu      rejected (5351/19) diff 58852 "Invalid job id" (45 ms)
[2021-12-12 15:58:36.987]  cpu      rejected (5459/20) diff 39322 "Invalid job id" (88 ms)
[2021-12-12 16:19:04.716]  cpu      rejected (5598/21) diff 58852 "Invalid job id" (44 ms)
[2021-12-12 17:55:54.710]  cpu      rejected (6208/22) diff 58852 "Invalid job id" (42 ms)
[2021-12-12 20:33:48.676]  cpu      rejected (7309/23) diff 19661 "Invalid job id" (73 ms)
[2021-12-12 21:26:21.355]  cpu      rejected (7599/24) diff 58852 "Invalid job id" (45 ms)
[2021-12-12 23:35:12.829]  cpu      rejected (8439/25) diff 58852 "Invalid job id" (41 ms)
[2021-12-13 00:08:34.179]  cpu      rejected (8697/25) diff 22952 "high-hash" (169 ms)
[2021-12-13 00:08:34.701]  cpu      rejected (8697/25) diff 22952 "high-hash" (131 ms)
[2021-12-13 00:08:35.271]  cpu      rejected (8697/25) diff 22952 "high-hash" (135 ms)
[2021-12-13 00:09:20.424]  cpu      rejected (8697/25) diff 102945 "high-hash" (137 ms)
[2021-12-13 00:09:22.066]  cpu      rejected (8697/25) diff 102945 "high-hash" (137 ms)
[2021-12-13 00:19:24.151]  cpu      rejected (8746/26) diff 58852 "Invalid job id" (119 ms)
[2021-12-13 00:37:43.503]  cpu      rejected (8827/27) diff 58852 "Invalid job id" (44 ms)
[2021-12-13 01:29:40.564]  cpu      rejected (9225/28) diff 58852 "Invalid job id" (42 ms)
[2021-12-13 02:21:33.270]  cpu      rejected (9556/29) diff 58852 "Invalid job id" (46 ms)
[2021-12-13 02:45:55.208]  cpu      rejected (9680/30) diff 58852 "Invalid job id" (80 ms)
[2021-12-13 03:11:00.192]  cpu      rejected (9850/31) diff 58852 "Invalid job id" (88 ms)
[2021-12-13 03:17:42.697]  cpu      rejected (9914/32) diff 58852 "Invalid job id" (41 ms)
[2021-12-13 04:59:01.660]  cpu      rejected (10712/33) diff 39322 "Invalid job id" (42 ms)
[2021-12-13 06:44:12.869]  cpu      rejected (11467/34) diff 58852 "Invalid job id" (53 ms)
[2021-12-13 07:05:28.076]  cpu      rejected (11603/35) diff 58852 "Invalid job id" (59 ms)
[2021-12-13 07:17:28.573]  cpu      rejected (11678/36) diff 58852 "Invalid job id" (42 ms)
[2021-12-13 08:02:44.952]  cpu      rejected (11976/37) diff 58852 "Invalid job id" (64 ms)
[2021-12-13 08:21:50.350]  cpu      rejected (12102/38) diff 58852 "Invalid job id" (63 ms)
[2021-12-13 08:42:41.127]  cpu      rejected (12233/39) diff 58852 "Invalid job id" (50 ms)
[2021-12-13 09:01:04.261]  cpu      rejected (12374/40) diff 58852 "Invalid job id" (41 ms)
[2021-12-13 12:29:58.365]  cpu      rejected (10/1) diff 19661 "Invalid job id" (56 ms)
[2021-12-13 12:32:05.339]  cpu      rejected (42/2) diff 39322 "Invalid job id" (41 ms)
[2021-12-13 18:10:16.817]  cpu      rejected (263/1) diff 58852 "Invalid job id" (64 ms)
[2021-12-13 19:13:27.079]  cpu      rejected (683/2) diff 58852 "Invalid job id" (46 ms)
[2021-12-13 19:49:35.339]  cpu      rejected (939/3) diff 58852 "Invalid job id" (41 ms)
[2021-12-13 19:53:47.973]  cpu      rejected (980/4) diff 58852 "Invalid job id" (41 ms)
[2021-12-13 20:43:16.110]  cpu      rejected (5/1) diff 19661 "Invalid job id" (41 ms)
[2021-12-13 20:47:07.718]  cpu      rejected (36/1) diff 39322 "Invalid job id" (41 ms)
[2021-12-13 22:35:53.542]  cpu      rejected (249/1) diff 131072 "Invalid job id" (64 ms)
[2021-12-13 22:44:40.571]  cpu      rejected (309/2) diff 131072 "Invalid job id" (46 ms)
[2021-12-13 23:38:24.354]  cpu      rejected (81/1) diff 44041 "Invalid job id" (40 ms)
[2021-12-13 23:41:33.940]  cpu      rejected (102/2) diff 44041 "Invalid job id" (47 ms)
```

![xmrig-invalid from 2021-12-13 23-40-04](https://user-images.githubusercontent.com/95162025/145943196-d96645d0-d7b8-4f1f-bc45-b962bbe8a988.png)


 - Config file or command line (without wallets)
cat config.json


```
{
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
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
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
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 24, 1, 25, 2, 26, 3, 27, 4, 28, 5, 29, 6, 30, 7, 31, 8, 32, 9, 33, 10, 34, 11, 35, 12, 36, 13, 37, 14, 38, 15, 39, 16, 40, 17, 41, 18, 42, 19, 43, 20, 44, 21, 45, 22, 46, 23, 47],
        "astrobwt": [0, 24, 1, 25, 2, 26, 3, 27, 4, 28, 5, 29, 6, 30, 7, 31, 8, 32, 9, 33, 10, 34, 11, 35, 12, 36, 13, 37, 14, 38, 15, 39, 16, 40, 17, 41, 18, 42, 19, 43, 20, 44, 21, 45, 22, 46, 23, 47],
        "cn": [
            [1, 0],
            [1, 24],
            [1, 1],
            [1, 25],
            [1, 2],
            [1, 26],
            [1, 3],
            [1, 27],
            [1, 4],
            [1, 28],
            [1, 5],
            [1, 29],
            [1, 6],
            [1, 30],
            [1, 7],
            [1, 31],
            [1, 8],
            [1, 32],
            [1, 9],
            [1, 33],
            [1, 10],
            [1, 34],
            [1, 11],
            [1, 35],
            [1, 12],
            [1, 36],
            [1, 13],
            [1, 37],
            [1, 14],
            [1, 38],
            [1, 15],
            [1, 39],
            [1, 16],
            [1, 40],
            [1, 17],
            [1, 41],
            [1, 18],
            [1, 42],
            [1, 19],
            [1, 43],
            [1, 20],
            [1, 44],
            [1, 21],
            [1, 45],
            [1, 22],
            [1, 46],
            [1, 23],
            [1, 47]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 26],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 29],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 32],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 35],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 38],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 41],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 44],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 47]
        ],
        "cn-lite": [
            [1, 0],
            [1, 24],
            [1, 1],
            [1, 25],
            [1, 2],
            [1, 26],
            [1, 3],
            [1, 27],
            [1, 4],
            [1, 28],
            [1, 5],
            [1, 29],
            [1, 6],
            [1, 30],
            [1, 7],
            [1, 31],
            [1, 8],
            [1, 32],
            [1, 9],
            [1, 33],
            [1, 10],
            [1, 34],
            [1, 11],
            [1, 35],
            [1, 12],
            [1, 36],
            [1, 13],
            [1, 37],
            [1, 14],
            [1, 38],
            [1, 15],
            [1, 39],
            [1, 16],
            [1, 40],
            [1, 17],
            [1, 41],
            [1, 18],
            [1, 42],
            [1, 19],
            [1, 43],
            [1, 20],
            [1, 44],
            [1, 21],
            [1, 45],
            [1, 22],
            [1, 46],
            [1, 23],
            [1, 47]
        ],
        "cn-pico": [
            [2, 0],
            [2, 24],
            [2, 1],
            [2, 25],
            [2, 2],
            [2, 26],
            [2, 3],
            [2, 27],
            [2, 4],
            [2, 28],
            [2, 5],
            [2, 29],
            [2, 6],
            [2, 30],
            [2, 7],
            [2, 31],
            [2, 8],
            [2, 32],
            [2, 9],
            [2, 33],
            [2, 10],
            [2, 34],
            [2, 11],
            [2, 35],
            [2, 12],
            [2, 36],
            [2, 13],
            [2, 37],
            [2, 14],
            [2, 38],
            [2, 15],
            [2, 39],
            [2, 16],
            [2, 40],
            [2, 17],
            [2, 41],
            [2, 18],
            [2, 42],
            [2, 19],
            [2, 43],
            [2, 20],
            [2, 44],
            [2, 21],
            [2, 45],
            [2, 22],
            [2, 46],
            [2, 23],
            [2, 47]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 24],
            [2, 1],
            [2, 25],
            [2, 2],
            [2, 26],
            [2, 3],
            [2, 27],
            [2, 4],
            [2, 28],
            [2, 5],
            [2, 29],
            [2, 6],
            [2, 30],
            [2, 7],
            [2, 31],
            [2, 8],
            [2, 32],
            [2, 9],
            [2, 33],
            [2, 10],
            [2, 34],
            [2, 11],
            [2, 35],
            [2, 12],
            [2, 36],
            [2, 13],
            [2, 37],
            [2, 14],
            [2, 38],
            [2, 15],
            [2, 39],
            [2, 16],
            [2, 40],
            [2, 17],
            [2, 41],
            [2, 18],
            [2, 42],
            [2, 19],
            [2, 43],
            [2, 20],
            [2, 44],
            [2, 21],
            [2, 45],
            [2, 22],
            [2, 46],
            [2, 23],
            [2, 47]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3],
            [8, 4],
            [8, 5],
            [8, 6],
            [8, 7],
            [8, 8],
            [8, 9],
            [8, 10],
            [8, 11],
            [8, 12],
            [8, 13],
            [8, 14],
            [8, 15],
            [8, 16],
            [8, 17],
            [8, 18],
            [8, 19],
            [8, 20],
            [8, 21],
            [8, 22],
            [8, 23]
        ],
        "rx": [0, 24, 1, 25, 2, 26, 3, 27, 4, 28, 5, 29, 6, 30, 7, 31, 8, 32, 9, 33, 10, 34, 11, 35, 12, 36, 13, 37, 14, 38, 15, 39, 16, 40, 17, 41, 18, 42, 19, 43, 20, 44, 21, 45, 22, 46, 23, 47],
        "rx/wow": [0, 24, 1, 25, 2, 26, 3, 27, 4, 28, 5, 29, 6, 30, 7, 31, 8, 32, 9, 33, 10, 34, 11, 35, 12, 36, 13, 37, 14, 38, 15, 39, 16, 40, 17, 41, 18, 42, 19, 43, 20, 44, 21, 45, 22, 46, 23, 47],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "log-file": "xmrighash.log",
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "ghostrider",
            "coin": null,
            "url": "stratum+tcp://pool.minafacil.com:4001",
            "user": "wallet.worker",
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
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
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
    "pause-on-battery": false,
    "pause-on-active": false

```





**Additional context**
- Tell me what else you need to supply to help triage this incident.




# Discussion History
# Action History
- Created by: mynerzulu | 2021-12-14T06:25:03+00:00
- Closed at: 2025-06-20T11:07:09+00:00
