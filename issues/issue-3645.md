---
title: Cannot mine kawpow on OpenCL
source_url: https://github.com/xmrig/xmrig/issues/3645
author: boogieman58
assignees: []
labels: []
created_at: '2025-03-10T09:53:03+00:00'
updated_at: '2025-06-18T22:38:29+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:38:29+00:00'
---

# Original Description
**Describe the bug**
I'm using xmrig with MoneroOcean's metaminer. xmrig produces errors both when metaminer tries to benchmark kawpow performance, and when it tries to mine it.

When running benchmarks, xmrig prints `login error code: -1`. As I have understood, this means an undefined error.
When attempting to mine, xmrig prints `login error code: 2`. As I have understood, this means that in the pool message, `result.job` was not an object. That is indeed true, because it is an array according to the logs below. After a quick look into metaminer code, it seems the MoneroOcean pool is the source of the JSON that has the array on that path, but I may be mistaken.

**To Reproduce**
 I'm running metaminer with this command:
```
./mm.js -p=gulf.moneroocean.stream:ssl20128 -m="./xmrig_local --config config_gpu.json" --debug --verbose
```

**Expected behavior**
I have expected that the benchmark process runs as unusual, and then xmrig can mine with the kawpow algorithm.

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
 
When metaminer attempts to benchmark kawpow performance:
```
>>> Checking miner performance for kawpow algo
>>> Starting miner: ./xmrig_local --config config_gpu.json
 * ABOUT        XMRig/6.22.2 gcc/7.5.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 7 2700X Eight-Core Processor (1) 64-bit AES
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       9.0/31.3 GB (29%)
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
>>> Miner message: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"redacted","pass":"x","agent":"XMRig/6.22.2 (Linux x86_64) libuv/1.49.2 gcc/7.5.0","algo":["cn/1","cn/2","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/yada","kawpow"]}}
>>> Meta-Miner message to miner: {"jsonrpc":"2.0","id":1,"error":null,"result":{"id":"benchmark","status":"OK","job":{"target":"01000000","blob":"7f7ffeeaa0db054f15eca39c843cb82c15e5c5a7743e06536cb541d4e96e90ffd31120b7703aa90000000076a6f6e34a9977c982629d8fe6c8b45024cafca109eef92198784891e0df41bc03","seed_hash":"0000000000000000000000000000000000000000000000000000000000000001","algo":"kawpow","height":0,"job_id":"benchmark1","id":"benchmark"}}}

[2025-03-10 10:34:27.625]  net      use pool localhost:3333  127.0.0.1
[2025-03-10 10:34:27.625]  net      new job from localhost:3333 diff 4294M algo kawpow
[2025-03-10 10:34:27.625]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 0a:00.0 |   4194304 |   256 |   1039 | AMD Radeon RX 6600 XT (gfx1032)
[2025-03-10 10:34:27.968]  opencl   GPU #0 compiling...
[2025-03-10 10:34:28.239]  opencl   GPU #0 compilation completed (270 ms)
[2025-03-10 10:34:28.240]  opencl   READY threads 1/1 (615 ms)
[2025-03-10 10:34:28.660]  opencl   KawPow program for period 0 compiled (419ms)
[2025-03-10 10:34:29.038]  opencl   KawPow program for period 1 compiled (377ms)
[2025-03-10 10:34:29.524]  miner    KawPow light cache for epoch 0 calculated (864ms)
[2025-03-10 10:34:31.460]  opencl   KawPow DAG for epoch 0 calculated (1926ms)
>>> Miner socket was closed
[2025-03-10 10:34:32.525]  net      no active pools, stop mining
>>> Miner server on 127.0.0.1:3333 port connected from 127.0.0.1
>>> Miner message: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"redacted","pass":"x","agent":"XMRig/6.22.2 (Linux x86_64) libuv/1.49.2 gcc/7.5.0","algo":["cn/1","cn/2","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/yada","kawpow"]}}
>>> Meta-Miner message to miner: {"jsonrpc":"2.0","id":1,"error":null,"result":{"id":"benchmark","status":"OK","job":{"target":"01000000","blob":"7f7ffeeaa0db054f15eca39c843cb82c15e5c5a7743e06536cb541d4e96e90ffd31120b7703aa90000000076a6f6e34a9977c982629d8fe6c8b45024cafca109eef92198784891e0df41bc03","seed_hash":"0000000000000000000000000000000000000000000000000000000000000001","algo":"kawpow","height":0,"job_id":"benchmark1","id":"benchmark"}}}

>>> Miner socket was closed
[2025-03-10 10:34:37.626]  net      localhost:3333 login error code: -1
>>> Miner server on 127.0.0.1:3333 port connected from 127.0.0.1
>>> Miner message: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"redacted","pass":"x","agent":"XMRig/6.22.2 (Linux x86_64) libuv/1.49.2 gcc/7.5.0","algo":["cn/1","cn/2","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/yada","kawpow"]}}
>>> Meta-Miner message to miner: {"jsonrpc":"2.0","id":1,"error":null,"result":{"id":"benchmark","status":"OK","job":{"target":"01000000","blob":"7f7ffeeaa0db054f15eca39c843cb82c15e5c5a7743e06536cb541d4e96e90ffd31120b7703aa90000000076a6f6e34a9977c982629d8fe6c8b45024cafca109eef92198784891e0df41bc03","seed_hash":"0000000000000000000000000000000000000000000000000000000000000001","algo":"kawpow","height":0,"job_id":"benchmark1","id":"benchmark"}}}

>>> Miner socket was closed
[2025-03-10 10:34:43.627]  net      localhost:3333 login error code: -1
>>> Miner server on 127.0.0.1:3333 port connected from 127.0.0.1
>>> Miner message: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"redacted","pass":"x","agent":"XMRig/6.22.2 (Linux x86_64) libuv/1.49.2 gcc/7.5.0","algo":["cn/1","cn/2","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/yada","kawpow"]}}
>>> Meta-Miner message to miner: {"jsonrpc":"2.0","id":1,"error":null,"result":{"id":"benchmark","status":"OK","job":{"target":"01000000","blob":"7f7ffeeaa0db054f15eca39c843cb82c15e5c5a7743e06536cb541d4e96e90ffd31120b7703aa90000000076a6f6e34a9977c982629d8fe6c8b45024cafca109eef92198784891e0df41bc03","seed_hash":"0000000000000000000000000000000000000000000000000000000000000001","algo":"kawpow","height":0,"job_id":"benchmark1","id":"benchmark"}}}

>>> Miner socket was closed
[2025-03-10 10:34:48.631]  net      localhost:3333 login error code: -1
^C
```

When metaminer attempts to mine with kawpow:

```
>>> Starting miner watchdog timer (with 600 seconds max since last miner result)
>>> Meta-Miner message to pool: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"redacted","pass":"x","agent":"Meta Miner v4.5","algo":["cn/1","cn/2","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/yada","cn/r","kawpow"],"algo-perf":{"cn-lite/0":1420.5,"cn-lite/1":1420.5,"cn-heavy/xhv":811.4,"cn/ccx":1346.2,"cn/0":673.1,"rx/0":316.9,"rx/sfx":316.9,"rx/graft":287,"rx/arq":1266.7,"cn/r":1,"kawpow":2000},"algo-min-time":0}}

>>> Pool message: {"jsonrpc":"2.0","id":1,"error":null,"result":{"id":"5818463","algo":"kawpow","extra_nonce":"fe05"}}
>>> Connected to gulf.moneroocean.stream:ssl20128 pool
>>> Pool message: {"method":"mining.set_target","params":["000000010346a102ff34b0000000000000000000000000000000000000000000"],"id":null,"jsonrpc":"2.0"}
>>> Pool message: {"method":"mining.notify","params":["2abc","33c124061146f86aec6c96516359ef0ad9a3ec3d23a3e5ee3d7f58b0ce8eed9e","398c942492d1d1065c5accfa3ed3d5c541d9995437065daf8e7996bd1fa39ce3","000000010346a102ff34b0000000000000000000000000000000000000000000",true,3750905,"1b00d2b9"],"algo":"kawpow","id":null,"jsonrpc":"2.0"}
>>> Starting miner './xmrig_local --config config_gpu.json' to process new kawpow algo
>>> Starting miner: ./xmrig_local --config config_gpu.json
 * ABOUT        XMRig/6.22.2 gcc/7.5.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 7 2700X Eight-Core Processor (1) 64-bit AES
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       8.9/31.3 GB (29%)
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
>>> Miner message: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"redacted","pass":"x","agent":"XMRig/6.22.2 (Linux x86_64) libuv/1.49.2 gcc/7.5.0","algo":["cn/1","cn/2","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/yada","kawpow"]}}
>>> Pool (gulf.moneroocean.stream:ssl20128) <-> miner link was established due to new miner connection
>>> Meta-Miner message to miner: {"jsonrpc":"2.0","error":null,"result":{"id":"5818463","job":["2abc","33c124061146f86aec6c96516359ef0ad9a3ec3d23a3e5ee3d7f58b0ce8eed9e","398c942492d1d1065c5accfa3ed3d5c541d9995437065daf8e7996bd1fa39ce3","000000010346a102ff34b0000000000000000000000000000000000000000000",true,3750905,"1b00d2b9"],"status":"OK"},"id":1}

[2025-03-10 10:37:04.891]  net      localhost:3333 login error code: 2
>>> Miner socket was closed
!!! Pool (gulf.moneroocean.stream:ssl20128) <-> miner link was broken due to closed miner socket
>>> Miner server on 127.0.0.1:3333 port connected from 127.0.0.1
>>> Miner message: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"redacted","pass":"x","agent":"XMRig/6.22.2 (Linux x86_64) libuv/1.49.2 gcc/7.5.0","algo":["cn/1","cn/2","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/yada","kawpow"]}}
>>> Pool (gulf.moneroocean.stream:ssl20128) <-> miner link was established due to new miner connection
>>> Meta-Miner message to miner: {"jsonrpc":"2.0","error":null,"result":{"id":"5818463","job":["2abc","33c124061146f86aec6c96516359ef0ad9a3ec3d23a3e5ee3d7f58b0ce8eed9e","398c942492d1d1065c5accfa3ed3d5c541d9995437065daf8e7996bd1fa39ce3","000000010346a102ff34b0000000000000000000000000000000000000000000",true,3750905,"1b00d2b9"],"status":"OK"},"id":1}

>>> Miner socket was closed
!!! Pool (gulf.moneroocean.stream:ssl20128) <-> miner link was broken due to closed miner socket
[2025-03-10 10:37:09.894]  net      localhost:3333 login error code: 2
>>> Miner server on 127.0.0.1:3333 port connected from 127.0.0.1
>>> Miner message: {"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"redacted","pass":"x","agent":"XMRig/6.22.2 (Linux x86_64) libuv/1.49.2 gcc/7.5.0","algo":["cn/1","cn/2","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/yada","kawpow"]}}
>>> Pool (gulf.moneroocean.stream:ssl20128) <-> miner link was established due to new miner connection
>>> Meta-Miner message to miner: {"jsonrpc":"2.0","error":null,"result":{"id":"5818463","job":["2abc","33c124061146f86aec6c96516359ef0ad9a3ec3d23a3e5ee3d7f58b0ce8eed9e","398c942492d1d1065c5accfa3ed3d5c541d9995437065daf8e7996bd1fa39ce3","000000010346a102ff34b0000000000000000000000000000000000000000000",true,3750905,"1b00d2b9"],"status":"OK"},"id":1}

>>> Miner socket was closed
!!! Pool (gulf.moneroocean.stream:ssl20128) <-> miner link was broken due to closed miner socket
[2025-03-10 10:37:14.898]  net      localhost:3333 login error code: 2
^C
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
        "cn/r": false,
        "kawpow": true
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

 - OS: Linux, openSUSE Leap 15.6
 - For GPU related issues:
   - GPU: AMD RX 6600 XT
   - Driver: amdgpu in kernel, 23.3.4
   - ROCm 6.3.3

**Additional context**
The metaminer I am using is unmodified v4.5.

# Discussion History
## OsakaPhysics | 2025-03-18T15:06:30+00:00
Weird it works for me on ubuntu newest.

## co945 | 2025-03-18T17:04:34+00:00
Bonjour 

## OsakaPhysics | 2025-03-19T19:33:09+00:00
Sorry if my comment was useless, im just as useless as my comment.

# Action History
- Created by: boogieman58 | 2025-03-10T09:53:03+00:00
- Closed at: 2025-06-18T22:38:29+00:00
