---
title: Miningcore stratum pool - RandomX - Floating point exception
source_url: https://github.com/xmrig/xmrig/issues/3156
author: blackmennewstyle
assignees: []
labels: []
created_at: '2022-11-06T01:08:12+00:00'
updated_at: '2022-11-16T02:35:22+00:00'
type: issue
status: closed
closed_at: '2022-11-16T02:35:22+00:00'
---

# Original Description
So i'm trying to mine XMR on `Miningcore` stratum pool.

`Miningcore` is on a laptop running an `AMD Ryzen 7 5800H`:
```
[2022-11-06 01:05:19.1438] [I] [Core] Version 73.0.1.0-master [2311784f0eb5e5f6180a5ac12eec2c9a270f9ca5] 
[2022-11-06 01:05:19.1616] [I] [Core] Runtime .NET 6.0.10 on Linux 5.18.0-0.deb11.4-amd64 #1 SMP PREEMPT_DYNAMIC Debian 5.18.16-1~bpo11+1 (2022-08-12) [X64] 
[2022-11-06 01:05:19.1708] [I] [Core] Prometheus Metrics API listening on http://0.0.0.0:4000/metrics 
[2022-11-06 01:05:19.1708] [I] [Core] WebSocket Events streaming on ws://0.0.0.0:4000/notifications 
[2022-11-06 01:05:19.8553] [I] [XmlKeyManager] User profile is available. Using '/home/ceedii/.aspnet/DataProtection-Keys' as key repository; keys will not be encrypted at rest. 
[2022-11-06 01:05:19.9051] [I] [ShareRecorder] Online 
[2022-11-06 01:05:19.9160] [I] [PayoutManager] Online 
[2022-11-06 01:05:19.9170] [I] [StatsRecorder] Online 
[2022-11-06 01:05:19.9861] [I] [Core] 131 coins loaded from '/home/ceedii/miningcore/build/coins.json' 
[2022-11-06 01:05:19.9985] [I] [xmr1] Starting Pool ... 
[2022-11-06 01:05:20.0032] [I] [xmr1] Starting Job Manager ... 
[2022-11-06 01:05:20.0458] [I] [Core] API Access to /api/admin restricted to 127.0.0.1,::1,::ffff:127.0.0.1 
[2022-11-06 01:05:20.0458] [I] [Core] API Access to /metrics restricted to 127.0.0.1,::1,::ffff:127.0.0.1 
[2022-11-06 01:05:20.0540] [I] [xmr1] All daemons online 
[2022-11-06 01:05:20.1042] [I] [Core] API access limited to 30 requests per 1s, except from 192.168.1.4 
[2022-11-06 01:05:20.1109] [I] [Lifetime] Now listening on: http://0.0.0.0:4000 
[2022-11-06 01:05:20.1109] [I] [Lifetime] Application started. Press Ctrl+C to shut down. 
[2022-11-06 01:05:20.1109] [I] [Lifetime] Hosting environment: Production 
[2022-11-06 01:05:20.1109] [I] [Lifetime] Content root path: /home/ceedii/miningcore/build/ 
[2022-11-06 01:05:20.1212] [I] [xmr1] All daemons synched with blockchain 
[2022-11-06 01:05:20.1434] [I] [xmr1] Job Manager Online 
[2022-11-06 01:05:20.5735] [I] [xmr1] Detected new block 2749504 [POLL] 
[2022-11-06 01:05:20.5735] [I] [xmr1] Detected new seed hash 758c3c212274e654f41abe93a7909eb0b48fddbc2a0af8f5d620c02477d581bb starting @ height 2749504 
[2022-11-06 01:05:20.5779] [I] [RandomX] Creating VM xmr1@1 [RANDOMX_FLAG_HARD_AES, RANDOMX_FLAG_FULL_MEM, RANDOMX_FLAG_JIT, RANDOMX_FLAG_ARGON2], hash 758c3c212274e654f41abe93a7909eb0b48fddbc2a0af8f5d620c02477d581bb ... 
[2022-11-06 01:05:34.9280] [I] [StatsRecorder] Performing Stats GC 
[2022-11-06 01:05:34.9458] [I] [StatsRecorder] Stats GC complete 
[2022-11-06 01:05:43.8137] [I] [RandomX] Created VM xmr1@1 in 00:00:23.2333895 
[2022-11-06 01:05:43.8285] [I] [xmr1] Broadcasting jobs 
[2022-11-06 01:05:43.8984] [I] [xmr1] Pool Online 
[2022-11-06 01:05:43.8984] [I] [xmr1] 

Mining Pool:            xmr1
Coin Type:              XMR [XMR]
Network Connected:      Main
Detected Reward Type:   POW
Current Block Height:   2749504
Current Connect Peers:  26
Network Difficulty:     357.97G
Network Hash Rate:      2.78 GH/s
Stratum Port(s):        3344, 3345
Pool Fee:               0.1%
 
[2022-11-06 01:05:43.9080] [I] [xmr1] Stratum ports 0.0.0.0:3344, 0.0.0.0:3345 online 
[2022-11-06 01:05:53.1626] [I] [xmr1] Detected new block 2749505 [POLL] 
[2022-11-06 01:05:53.1626] [I] [xmr1] Broadcasting jobs 
[2022-11-06 01:06:19.9326] [I] [PayoutManager] Processing payments for pool xmr1 
[2022-11-06 01:06:19.9657] [I] [PayoutManager] No updated blocks for pool xmr1 
[2022-11-06 01:06:19.9734] [I] [PayoutManager] No balances over configured minimum payout for pool xmr1 
[2022-11-06 01:06:21.8838] [I] [xmr1] [0HMLVICF7L732] Accepting connection from ::ffff:192.168.1.5:50468 ... 
[2022-11-06 01:06:22.0057] [I] [xmr1] [0HMLVICF7L732] TLS13-AES256 Connection from ::ffff:192.168.1.5:50468 accepted on port 3345 
[2022-11-06 01:06:22.0057] [D] [xmr1] [0HMLVHPDTJJ8B] [NET] Waiting for data ... 
[2022-11-06 01:06:22.0057] [D] [xmr1] [0HMLVHPDTJJ8B] [NET] Received data: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"48W8eVd8EikDRWMgg7qePZgyrCu5hBhobNGkgor38vjxDC21ed7DuUQcDjwJurFWQeA722XTnfhv76Cpr4ECqHaFRoi7A9Q","pass":"ganymede","agent":"XMRig/6.18.1 (Linux x86_64) libuv/1.44.1 gcc/5.4.0","algo":["rx/0","cn/1","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/0","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","cn/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/keva","argon2/chukwa","argon2/chukwav2","argon2/ninja","ghostrider"]}}
 
[2022-11-06 01:06:22.0057] [D] [xmr1] [0HMLVHPDTJJ8B] [NET] Waiting for data ... 
[2022-11-06 01:06:22.0057] [D] [xmr1] [0HMLVHPDTJJ8B] [PIPE] Waiting for data ... 
[2022-11-06 01:06:22.0057] [D] [xmr1] [0HMLVHPDTJJ8B] [PIPE] Received data: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"48W8eVd8EikDRWMgg7qePZgyrCu5hBhobNGkgor38vjxDC21ed7DuUQcDjwJurFWQeA722XTnfhv76Cpr4ECqHaFRoi7A9Q","pass":"ganymede","agent":"XMRig/6.18.1 (Linux x86_64) libuv/1.44.1 gcc/5.4.0","algo":["rx/0","cn/1","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/0","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","cn/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/keva","argon2/chukwa","argon2/chukwav2","argon2/ninja","ghostrider"]}}
 
[2022-11-06 01:06:22.0057] [D] [xmr1] [0HMLVHPDTJJ8B] Dispatching request 'login' [1] 
[2022-11-06 01:06:22.0057] [I] [xmr1] [0HMLVHPDTJJ8B] Authorized miner 48W8eVd8EikDRWMgg7qePZgyrCu5hBhobNGkgor38vjxDC21ed7DuUQcDjwJurFWQeA722XTnfhv76Cpr4ECqHaFRoi7A9Q 
[2022-11-06 01:06:22.0057] [D] [xmr1] [0HMLVHPDTJJ8B] [PIPE] Waiting for data ... 
[2022-11-06 01:06:22.0057] [D] [xmr1] [0HMLVHPDTJJ8B] Sending: {"result":{"id":"0HMLVHPDTJJ8B","job":{"job_id":"1","blob":"1010c3809c9b06fe2b6cbe95e529ec14c449f0c488b134c5e3a94ce4aa28b41fdb43b88a6756f60000000020523fc271efde5a7f402c6c823e90a20149a1da25a432daa528afdb4b48e56a36","target":"00000000","seed_hash":"758c3c212274e654f41abe93a7909eb0b48fddbc2a0af8f5d620c02477d581bb","algo":"rx/0","height":2749492},"status":"OK"},"id":1} 
[2022-11-06 01:06:22.0057] [D] [xmr1] Template update 2749492 [POLL] 
[2022-11-06 01:06:22.0057] [D] [xmr1] [0HMLVHPDTJJ8B] Received EOF 
[2022-11-06 01:06:22.1037] [I] [xmr1] [0HMLVICF7L732] Connection closed 
```

`XMRig`
```
 * ABOUT        XMRig/6.18.1 gcc/9.3.0
 * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       3.0/15.5 GB (19%)
                DIMM_A0: 16 GB DDR4 @ 2400 MHz M471A2K43CB1-CRC    
                DIMM_B0: <empty>
 * MOTHERBOARD  Micro-Star International Co., Ltd. - MS-16JB
 * DONATE       1%
 * ASSEMBLY     intel
 * POOL #1      monero.cedric-crispin.local:3345 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     192.168.1.5:3333 
Floating point exception
```

# Discussion History
## SChernykh | 2022-11-15T06:25:50+00:00
@blackmennewstyle what's your XMRig config.json? And full command line you use to start XMRig.

## blackmennewstyle | 2022-11-15T06:31:14+00:00
> @blackmennewstyle what's your XMRig config.json? And full command line you use to start XMRig.

Hello,

I'm not using `config.json`, but here the full command-line:
```
/home/ceedii/xmrig-6.18.1/xmrig --donate-level=1 --api-id=ganymede --api-worker-id=ganymede --http-host=192.168.1.5 --http-port=4442 --http-access-token=ganymede --http-no-restricted -a rx/0 -o monero.cedric-crispin.com:3345 -u 48W8eVd8EikDRWMgg7qePZgyrCu5hBhobNGkgor38vjxDC21ed7DuUQcDjwJurFWQeA722XTnfhv76Cpr4ECqHaFRoi7A9Q.ganymede -k --tls -p ganymede --coin=monero --asm=ryzen --threads=8 --randomx-1gb-page
```

## SChernykh | 2022-11-15T06:42:16+00:00
In the screenshot, it crashes when it tries to initialize OpenCL and CUDA, so try to add `--disable-opencl --disable-cuda` to the command line.

Also, remove these two:

`--asm=ryzen` you have Intel CPU
`--threads=8` it can run only 3 threads on RandomX, everything more than that will reduce your hashrate. Automatic thread configuration works fine in XMRig.

## blackmennewstyle | 2022-11-16T02:35:22+00:00
> In the screenshot, it crashes when it tries to initialize OpenCL and CUDA, so try to add `--disable-opencl --disable-cuda` to the command line.
> 
> Also, remove these two:
> 
> `--asm=ryzen` you have Intel CPU `--threads=8` it can run only 3 threads on RandomX, everything more than that will reduce your hashrate. Automatic thread configuration works fine in XMRig.

Thanks for the inputs, especially the threads one about INTEL. There was also an issue with my `miningcore` setup. Now, everything works great.

# Action History
- Created by: blackmennewstyle | 2022-11-06T01:08:12+00:00
- Closed at: 2022-11-16T02:35:22+00:00
