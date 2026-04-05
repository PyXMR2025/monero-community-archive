---
title: Silent crash with OpenCL backend when running MoneroOcean metaminer's benchmark
source_url: https://github.com/xmrig/xmrig/issues/3644
author: boogieman58
assignees: []
labels: []
created_at: '2025-03-10T09:22:15+00:00'
updated_at: '2025-06-18T22:38:38+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:38:38+00:00'
---

# Original Description
**Describe the bug**
I'm using xmrig with MoneroOcean's metaminer. Unless I disable the `cn/r` algorithm in the config (`opencl.cn/r: false`), when metaminer tries to benchmark this algorithm xmrig will start, compile the OpenCL code, and crash right after printing "opencl   READY threads 2/2".

When this happens, metaminer logs that the miner socket closed, and xmrig exited with 0 exit code:
```
>>> Miner socket was closed
>>> Miner './xmrig_local --config config_gpu.json' exited with zero code
!!! Can't find performance data in './xmrig_local --config config_gpu.json' miner output
```

**To Reproduce**
I'm running metaminer with this command:
```
./mm.js -p=gulf.moneroocean.stream:ssl20128 -m="./xmrig_local --config config_gpu.json" --debug --verbose
```

**Expected behavior**

I have expected that the benchmark process runs for 2 minutes (+ init), and prints hashrates.

**Required data**
 - XMRig version: local build
Commands used to build xmrig:
1. git clone https://github.com/xmrig/xmrig
2. git checkout v6.22.2
3. mkdir xmrig/build && cd xmrig/scripts
4. ./build_deps.sh && cd ../build
5. cmake .. -DXMRIG_DEPS=scripts/deps
6. make -j16

 - Miner log as text or screenshot (including metaminer log)
 
```
>>> Checking miner performance for cn/r algo
>>> Starting miner: ./xmrig_local --config config_gpu.json
 * ABOUT        XMRig/6.22.2 gcc/7.5.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 7 2700X Eight-Core Processor (1) 64-bit AES
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       9.2/31.3 GB (29%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      localhost:3333 algo auto
 * POOL #2      redacted
 * POOL #3      redacted
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3635.0)
 * OPENCL GPU   #0 0a:00.0 AMD Radeon RX 6600 XT (gfx1032) 2900 MHz cu:16 mem:6949/8176 MB
 * CUDA         disabled
>>> Miner server on 127.0.0.1:3333 port connected from 127.0.0.1
>>> Miner message: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"redacted","pass":"x","agent":"XMRig/6.22.2 (Linux x86_64) libuv/1.49.2 gcc/7.5.0","algo":["cn/1","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/yada","kawpow"]}}
>>> Meta-Miner message to miner: {"jsonrpc":"2.0","id":1,"error":null,"result":{"id":"benchmark","status":"OK","job":{"target":"01000000","blob":"7f7ffeeaa0db054f15eca39c843cb82c15e5c5a7743e06536cb541d4e96e90ffd31120b7703aa90000000076a6f6e34a9977c982629d8fe6c8b45024cafca109eef92198784891e0df41bc03","seed_hash":"0000000000000000000000000000000000000000000000000000000000000001","algo":"cn/r","height":0,"job_id":"benchmark1","id":"benchmark"}}}

[2025-03-10 09:43:15.578]  net      use pool localhost:3333  127.0.0.1
[2025-03-10 09:43:15.578]  net      new job from localhost:3333 diff 4294M algo cn/r (3 tx)
[2025-03-10 09:43:15.578]  opencl   use profile  cn/2  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 0a:00.0 |       448 |     8 |    896 | AMD Radeon RX 6600 XT (gfx1032)
|  1 |   0 | 0a:00.0 |       448 |     8 |    896 | AMD Radeon RX 6600 XT (gfx1032)
[2025-03-10 09:43:17.962]  opencl   GPU #0 compiling...
[2025-03-10 09:43:26.968]  opencl   GPU #0 compilation completed (9006 ms)
[2025-03-10 09:43:26.968]  opencl   GPU #0 compiling...
[2025-03-10 09:43:35.773]  opencl   GPU #0 compilation completed (8805 ms)
[2025-03-10 09:43:35.774]  opencl   READY threads 2/2 (20196 ms)
>>> Miner socket was closed
>>> Miner './xmrig_local --config config_gpu.json' exited with zero code
!!! Can't find performance data in './xmrig_local --config config_gpu.json' miner output
```

 - Config file or command line (without wallets)
 
```
{
    "autosave": false,
    "cpu": false,
    "cuda": false,
    "opencl": {
        "enabled": true,
        "loader": "/usr/lib64/libOpenCL.so.1",
        "platform": "AMD",
        "cache": false,
        "adl": true,
        "cn/r": true,
        "kawpow": false
    },  
    "log-file": null,
    "donate-level": 1,
    "pools": [
        {
            "enabled": true,
            "url": "localhost:3333",
            "user": "redacted",
            "pass": null,
            "rig-id": null,
            "algo": null,
            "coin": null
        }
    ]   
}
```

Note: removed the disabled pools.

 - OS: Linux, openSUSE Leap 15.6
 - For GPU related issues:
   - GPU: AMD RX 6600 XT
   - Driver: amdgpu in kernel, 23.3.4
   - ROCm 6.3.3

**Additional context**

Setting the `algo_perf` for this algorithm manually in metaminer config skips the benchmark and then xmig seems to work fine, it prints the hashrate every minute and metaminer logs the miner communication.

The metaminer I am using is unmodified v4.5.

When OpenCL is disabled and CPU is enabled in xmrig config, benchmark completes as expected.

# Discussion History
## stephenmontgomery | 2025-04-09T01:40:13+00:00
I confirm the same behaviour. After (finally) getting opencl working on Linux, backing up original generated ~/moneroocean directory (cpu enabled only), rerunning bash install script, enabling opencl with loader option, the benchmarking never finishes on job startup. Waiting for 40 mins before killing it. Doing an sdiff between the original cpu-only and the new config.json gives a missing algo-perf block: 

```
stephen@stephen-MS-7C37:~/moneroocean$ sdiff -s ./config.json ../moneroocean_old/config.json 
    "algo-perf": {},					      |	    "algo-perf": {
							      >	        "cn/0": 2055.7836017261343,
							      >	        "cn/1": 2068.624355331018,
							      >	        "cn/2": 2068.624355331018,
							      >	        "cn/r": 2068.624355331018,
							      >	        "cn/fast": 4137.248710662036,
							      >	        "cn/half": 4137.248710662036,
							      >	        "cn/xao": 2068.624355331018,
							      >	        "cn/rto": 2068.624355331018,
							      >	        "cn/rwz": 2758.1658071080237,
							      >	        "cn/zls": 2758.1658071080237,
							      >	        "cn/double": 1034.312177665509,
							      >	        "cn/ccx": 4111.567203452269,
							      >	        "cn-lite/0": 5533.726191728928,
							      >	        "cn-lite/1": 5533.726191728928,
							      >	        "cn-heavy/xhv": 1550.6788759077992,
							      >	        "cn-pico": 33365.26315789474,
							      >	        "cn-pico/tlo": 33365.26315789474,
							      >	        "cn/gpu": 362.38290706241446,
							      >	        "rx/0": 16806.21052631579,
							      >	        "rx/arq": 72192.31578947368,
							      >	        "rx/xeq": 72192.31578947368,
							      >	        "rx/graft": 16373.78947368421,
							      >	        "rx/sfx": 16806.21052631579,
							      >	        "panthera": 14037.368421052632,
							      >	        "argon2/chukwav2": 31774.63157894737,
							      >	        "kawpow": -1.0,
							      >	        "ghostrider": 4148.085822465292,
							      >	        "flex": 3406.706612004625
							      >	    },

```

which probably is set when benchmark finishes?

Just adding this block (or replacing config file) means benchmark is skipped and starts processing pool work.

# Action History
- Created by: boogieman58 | 2025-03-10T09:22:15+00:00
- Closed at: 2025-06-18T22:38:38+00:00
