---
title: The latest xmrig version produces duplicate shares
source_url: https://github.com/xmrig/xmrig/issues/3404
author: MoneroOcean
assignees: []
labels:
- bug
- randomx
created_at: '2024-01-21T16:51:43+00:00'
updated_at: '2025-06-17T05:59:02+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:58:37+00:00'
---

# Original Description
**Describe the bug**
The latest xmrig version v6.21.0 (built from this repo) produces duplicate shares.

**To Reproduce**
Build https://github.com/xmrig/xmrig sources (I used ```cmake -DWITH_DEBUG_LOG=ON``` to show deblicate nonces more clearly) and run the following way as usual:

```sudo ~/xmrig/xmrig -o gulf.moneroocean.stream:20016 --tls -u ...```

MoneroOcean pool may be essential to reproduce since it more often changes seed between ZEPH and XMR rx/0 algos. I noticed seed change often preceeds duplicate shares errors. Error happens once per 3 days on average.

**Expected behavior**
No duplicate share errors.

**Required data**
 - Miner log as text or screenshot
As you can see job with ```b0da0400``` nonce is really submitted twice by the miner without any reconnects to the pool and job changes. 

```
[2024-01-21 03:54:08.146] [gulf.moneroocean.stream:20016] received (370 bytes): "{"method":"job","params":{"blob":"1010e08bb4ad062f90cad883cb95fbb48b2c7f78722ef6e5390a2346bef03de4bd6886318daf1a0000000038eef0dba57a4598ea97ff98d5bd7df0d8384b321f7b5eb01e1d57a2c300850729","algo":"rx/0","
height":3066758,"seed_hash":"c7c40a37e46754b82f67b9a9b5edf03c5af1303221b729ceb2604eb32eeb9ccc","job_id":"10387278","target":"68360000","id":"9698647"},"jsonrpc":"2.0"}"
[2024-01-21 03:54:08.146]  net      new job from gulf.moneroocean.stream:20016 diff 308369 algo rx/0 height 3066758 (41 tx)
[2024-01-21 03:54:13.011] [gulf.moneroocean.stream:20016] TLS received (632 bytes)
[2024-01-21 03:54:13.011] [gulf.moneroocean.stream:20016] received (609 bytes): "{"method":"job","params":{"blob":"0303dd8bb4ad06d8906bc8e00540ce03b207b9d74a3548f06319f17adc497142f7a6e0a5128ca100000000102f7f920b0d0000c065377bfc0c0000e0ef8e3b10000000d0e26b4e10000000a01318a605010000c00
c3d7c05010000dd05ad65000000002736b6c3b41351a2fd2addd6d3cb7b913178b96688f8bb03baae24523def3ac3fe6e5eba1f632570cd4d23ea23a552c2fe2b0e36233d8bf007fd25f27358cec98c9198caf0f2e0682fa3972f2fc50f99e155cbf787788123103a62c0ff7b3ff101","algo":"rx/0","height":168811,"seed_hash":"222f067bd4d8c074
a776ca6c14831caa1e5884b225f7a74eecbde2369d58bba1","job_id":"10389009","target":"c5690000","id":"9698647"},"jsonrpc":"2.0"}"
[2024-01-21 03:54:13.011]  net      new job from gulf.moneroocean.stream:20016 diff 158620 algo rx/0 height 168811
[2024-01-21 03:54:13.011]  randomx  init dataset algo rx/0 (16 threads) seed 222f067bd4d8c074...
[2024-01-21 03:54:14.666]  randomx  dataset ready (1655 ms)
[2024-01-21 03:54:30.975] [gulf.moneroocean.stream:20016] send (186 bytes): "{"id":517,"jsonrpc":"2.0","method":"submit","params":{"id":"9698647","job_id":"10389009","nonce":"722f0500","result":"6c6d191dda79a247637af31cea3b24be4131d6f6e8c934ba0686618a304a0000"}}"
[2024-01-21 03:54:30.975] [gulf.moneroocean.stream:20016] TLS send     (208 bytes)
[2024-01-21 03:54:31.488] [gulf.moneroocean.stream:20016] TLS received (87 bytes)
[2024-01-21 03:54:31.489] [gulf.moneroocean.stream:20016] received (64 bytes): "{"jsonrpc":"2.0","id":517,"error":null,"result":{"status":"OK"}}"
[2024-01-21 03:54:31.489]  cpu      accepted (469/0) diff 158620 (514 ms)
[2024-01-21 03:54:40.140]  miner    speed 10s/60s/15m 5929.3 5758.7 5842.3 H/s max 6041.2 H/s
[2024-01-21 03:54:45.893] [gulf.moneroocean.stream:20016] send (186 bytes): "{"id":518,"jsonrpc":"2.0","method":"submit","params":{"id":"9698647","job_id":"10389009","nonce":"b0da0400","result":"65e06cf5dca6fa3c6accf5284c0cb92c0dff298949e13163b7752854411d0000"}}"
[2024-01-21 03:54:45.893] [gulf.moneroocean.stream:20016] TLS send     (208 bytes)
[2024-01-21 03:54:46.409] [gulf.moneroocean.stream:20016] TLS received (87 bytes)
[2024-01-21 03:54:46.409] [gulf.moneroocean.stream:20016] received (64 bytes): "{"jsonrpc":"2.0","id":518,"error":null,"result":{"status":"OK"}}"
[2024-01-21 03:54:46.409]  cpu      accepted (470/0) diff 158620 (515 ms)
[2024-01-21 03:54:54.712] [gulf.moneroocean.stream:20016] send (186 bytes): "{"id":519,"jsonrpc":"2.0","method":"submit","params":{"id":"9698647","job_id":"10389009","nonce":"5ef40400","result":"f04fab5d5b3c57f5cde4ebe13ba8ad995bd06e6dbf0c7f0e320c468fe45a0000"}}"
[2024-01-21 03:54:54.712] [gulf.moneroocean.stream:20016] TLS send     (208 bytes)
[2024-01-21 03:54:55.287] [gulf.moneroocean.stream:20016] TLS received (87 bytes)
[2024-01-21 03:54:55.287] [gulf.moneroocean.stream:20016] received (64 bytes): "{"jsonrpc":"2.0","id":519,"error":null,"result":{"status":"OK"}}"
[2024-01-21 03:54:55.287]  cpu      accepted (471/0) diff 158620 (576 ms)
[2024-01-21 03:54:57.455] [gulf.moneroocean.stream:20016] send (186 bytes): "{"id":520,"jsonrpc":"2.0","method":"submit","params":{"id":"9698647","job_id":"10389009","nonce":"c87b0400","result":"13ce1246d2570bbfc617f28009838acec4d1e6298c12cf64c8a54393bd3d0000"}}"
[2024-01-21 03:54:57.455] [gulf.moneroocean.stream:20016] TLS send     (208 bytes)
[2024-01-21 03:54:58.052] [gulf.moneroocean.stream:20016] TLS received (87 bytes)
[2024-01-21 03:54:58.052] [gulf.moneroocean.stream:20016] received (64 bytes): "{"jsonrpc":"2.0","id":520,"error":null,"result":{"status":"OK"}}"
[2024-01-21 03:54:58.052]  cpu      accepted (472/0) diff 158620 (597 ms)
[2024-01-21 03:55:21.571] [gulf.moneroocean.stream:20016] send (186 bytes): "{"id":521,"jsonrpc":"2.0","method":"submit","params":{"id":"9698647","job_id":"10389009","nonce":"f0410000","result":"331b11fad4ef7e688ffb57ab45283595a4a80dff60100b5a43b7e022af490000"}}"
[2024-01-21 03:55:21.571] [gulf.moneroocean.stream:20016] TLS send     (208 bytes)
[2024-01-21 03:55:22.089] [gulf.moneroocean.stream:20016] TLS received (87 bytes)
[2024-01-21 03:55:22.089] [gulf.moneroocean.stream:20016] received (64 bytes): "{"jsonrpc":"2.0","id":521,"error":null,"result":{"status":"OK"}}"
[2024-01-21 03:55:22.089]  cpu      accepted (473/0) diff 158620 (519 ms)
[2024-01-21 03:55:40.276]  miner    speed 10s/60s/15m 5907.6 5898.3 5845.6 H/s max 6041.2 H/s
[2024-01-21 03:55:59.405] [gulf.moneroocean.stream:20016] send (186 bytes): "{"id":522,"jsonrpc":"2.0","method":"submit","params":{"id":"9698647","job_id":"10389009","nonce":"722f0500","result":"6c6d191dda79a247637af31cea3b24be4131d6f6e8c934ba0686618a304a0000"}}"
[2024-01-21 03:55:59.405] [gulf.moneroocean.stream:20016] TLS send     (208 bytes)
[2024-01-21 03:55:59.454] [gulf.moneroocean.stream:20016] TLS received (97 bytes)
[2024-01-21 03:55:59.454] [gulf.moneroocean.stream:20016] received (74 bytes): "{"jsonrpc":"2.0","id":522,"error":{"code":-1,"message":"Duplicate share"}}"
[2024-01-21 03:55:59.454]  cpu      rejected (473/1) diff 158620 "Duplicate share" (50 ms)
[2024-01-21 03:56:14.487] [gulf.moneroocean.stream:20016] send (186 bytes): "{"id":523,"jsonrpc":"2.0","method":"submit","params":{"id":"9698647","job_id":"10389009","nonce":"b0da0400","result":"65e06cf5dca6fa3c6accf5284c0cb92c0dff298949e13163b7752854411d0000"}}"
[2024-01-21 03:56:14.487] [gulf.moneroocean.stream:20016] TLS send     (208 bytes)
[2024-01-21 03:56:14.534] [gulf.moneroocean.stream:20016] TLS received (97 bytes)
[2024-01-21 03:56:14.534] [gulf.moneroocean.stream:20016] received (74 bytes): "{"jsonrpc":"2.0","id":523,"error":{"code":-1,"message":"Duplicate share"}}"
[2024-01-21 03:56:14.534]  cpu      rejected (473/2) diff 158620 "Duplicate share" (48 ms)
[2024-01-21 03:56:23.353] [gulf.moneroocean.stream:20016] send (186 bytes): "{"id":524,"jsonrpc":"2.0","method":"submit","params":{"id":"9698647","job_id":"10389009","nonce":"5ef40400","result":"f04fab5d5b3c57f5cde4ebe13ba8ad995bd06e6dbf0c7f0e320c468fe45a0000"}}"
[2024-01-21 03:56:23.354] [gulf.moneroocean.stream:20016] TLS send     (208 bytes)
[2024-01-21 03:56:23.472] [gulf.moneroocean.stream:20016] TLS received (97 bytes)
[2024-01-21 03:56:23.472] [gulf.moneroocean.stream:20016] received (74 bytes): "{"jsonrpc":"2.0","id":524,"error":{"code":-1,"message":"Duplicate share"}}"
[2024-01-21 03:56:23.472]  cpu      rejected (473/3) diff 158620 "Duplicate share" (118 ms)
[2024-01-21 03:56:25.991] [gulf.moneroocean.stream:20016] send (186 bytes): "{"id":525,"jsonrpc":"2.0","method":"submit","params":{"id":"9698647","job_id":"10389009","nonce":"c87b0400","result":"13ce1246d2570bbfc617f28009838acec4d1e6298c12cf64c8a54393bd3d0000"}}"
[2024-01-21 03:56:25.991] [gulf.moneroocean.stream:20016] TLS send     (208 bytes)
[2024-01-21 03:56:26.040] [gulf.moneroocean.stream:20016] TLS received (97 bytes)
[2024-01-21 03:56:26.040] [gulf.moneroocean.stream:20016] received (74 bytes): "{"jsonrpc":"2.0","id":525,"error":{"code":-1,"message":"Duplicate share"}}"
[2024-01-21 03:56:26.040]  cpu      rejected (473/4) diff 158620 "Duplicate share" (48 ms)
```
 - Config file or command line (without wallets)
```sudo ~/xmrig/xmrig -o gulf.moneroocean.stream:20016 --tls -u ...```

 - OS: [e.g. Windows]
Linux (not checked Windows)

**Additional context**

Miner rx/0 setup on affected system:
```
 * ABOUT        XMRig/6.21.0 gcc/11.4.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.43.0 OpenSSL/3.0.2 hwloc/2.7.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          11th Gen Intel(R) Core(TM) i7-11700K @ 3.60GHz (1) 64-bit AES
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       12.7/31.2 GB (41%)
                Controller0-ChannelA-DIMM0: 16 GB DDR4 @ 3200 MHz SP016GXLZU320FSA
                Controller0-ChannelA-DIMM1: <empty>
                Controller0-ChannelB-DIMM0: 16 GB DDR4 @ 3200 MHz SP016GXLZU320FSA
                Controller0-ChannelB-DIMM1: <empty>
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - PRIME H570M-PLUS
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      gulf.moneroocean.stream:20016 algo auto
[2024-01-21 08:48:57.864] POOLS --------------------------------------------------------------------
[2024-01-21 08:48:57.864] url:       gulf.moneroocean.stream:20016
[2024-01-21 08:48:57.864] host:      gulf.moneroocean.stream
[2024-01-21 08:48:57.864] port:      20016
[2024-01-21 08:48:57.864] user:      ...
[2024-01-21 08:48:57.864] pass:      (null)
[2024-01-21 08:48:57.864] rig-id     (null)
[2024-01-21 08:48:57.864] algo:      invalid
[2024-01-21 08:48:57.864] nicehash:  0
[2024-01-21 08:48:57.864] keepAlive: 0
[2024-01-21 08:48:57.864] --------------------------------------------------------------------------
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-01-21 08:48:57.866] [gulf.moneroocean.stream:20016] state: "unconnected" -> "host-lookup"
[2024-01-21 08:48:57.892] [gulf.moneroocean.stream:20016] state: "host-lookup" -> "connecting"
[2024-01-21 08:48:57.941] [gulf.moneroocean.stream:20016] state: "connecting" -> "connected"
[2024-01-21 08:48:57.942] [gulf.moneroocean.stream:20016] TLS send     (293 bytes)
[2024-01-21 08:48:57.996] [gulf.moneroocean.stream:20016] TLS received (1465 bytes)
[2024-01-21 08:48:58.000] [gulf.moneroocean.stream:20016] send (546 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"...","pass":"x","agent":"XMRig/6.21.0 (Linux x86_64) libuv/1.43.0 gcc/11.4.0","algo":["cn/1","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn/ccx","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/upx2","rx/0","rx/wow","rx/arq","rx/graft","rx/sfx","rx/keva","argon2/chukwa","argon2/chukwav2","argon2/ninja","ghostrider"]}}"
[2024-01-21 08:48:58.000] [gulf.moneroocean.stream:20016] TLS send     (648 bytes)
[2024-01-21 08:48:58.051] [gulf.moneroocean.stream:20016] TLS received (1218 bytes)
[2024-01-21 08:48:58.051] [gulf.moneroocean.stream:20016] received (653 bytes): "{"jsonrpc":"2.0","id":1,"error":null,"result":{"id":"11285391","job":{"blob":"0303f695b5ad06c2dc5f4b8a724d032dc76978ea94e74456326ffd2b9c4032e470ca673c21174900000000a0634db8340d0000a0df80af0b0d000050c9fa081000000010c66a3b10000000103ac43a06010000a041d9ca05010000f74aad650000000073d1f011c33509e8ecacf1bedb78301d4ebc649c6fde95ee045bfeee72a8d48ea913b1de146cb4835a660312266e3157a3fa1d5a6198a017b4172952f0740f27c13d547c1066374e6a7b0a0531503cc382352f04934421031f65d58366e10c3301","algo":"rx/0","height":168960,"seed_hash":"222f067bd4d8c074a776ca6c14831caa1e5884b225f7a74eecbde2369d58bba1","job_id":"11285392","target":"89b90000","id":"11285391"},"status":"OK"}}"
[2024-01-21 08:48:58.051]  net      use pool gulf.moneroocean.stream:20016 TLSv1.3 44.224.209.130
[2024-01-21 08:48:58.051]  net      fingerprint (SHA-256): "239daadd5c7d0ac097376c7871f787738826eef1c024729eff870e473b970855"
[2024-01-21 08:48:58.051]  net      new job from gulf.moneroocean.stream:20016 diff 90426 algo rx/0 height 168960
[2024-01-21 08:48:58.051]  cpu      use argon2 implementation AVX-512F
[2024-01-21 08:48:58.052]  msr      register values for "intel" preset have been set successfully (1 ms)
[2024-01-21 08:48:58.052]  randomx  init dataset algo rx/0 (16 threads) seed 222f067bd4d8c074...
[2024-01-21 08:48:58.141]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (89 ms)
[2024-01-21 08:48:59.763]  randomx  dataset ready (1622 ms)
[2024-01-21 08:48:59.763]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2024-01-21 08:48:59.767]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (4 ms)
```


# Discussion History
## SChernykh | 2024-01-21T21:54:28+00:00
Does it happen after every dataset change (when switching xmr <-> zeph), or only after some of them, randomly?

> Error happens once per 3 days on average.

Dataset update period is 2048 blocks, or ~2.84 days. So does it happen with this periodicity? Although, neither zeph nor xmr were at the end of their respective periods in your log, they were in the middle.

## MoneroOcean | 2024-01-21T21:59:53+00:00
I think this is related to dataset change required between ZEPH and XMR. 3 days is very approximate estimate. Do not have enough history data to say this for sure. Just a crude estimation.

## MoneroOcean | 2024-02-01T23:35:22+00:00
Here is update with more logs with nonces. I believe the reason is due to delayed to seed change nonce reset do not really resets it to zero in step 2 (or do it too late in step 4).


I use the following patch:

```
diff --git a/src/core/Miner.cpp b/src/core/Miner.cpp
index 9cc9092b..6ead5f6a 100644
--- a/src/core/Miner.cpp
+++ b/src/core/Miner.cpp
@@ -122,6 +122,7 @@ public:

         if (reset) {
             Nonce::reset(job.index());
+            LOG_INFO("NONCE RESET REAL");
         }

         for (IBackend *backend : backends) {
@@ -566,6 +567,10 @@ void xmrig::Miner::setJob(const Job &job, bool donate)
     if (d_ptr->job.isEqualBlob(job)) {
         d_ptr->reset = false;
     }
+    if (d_ptr->reset)
+      LOG_INFO("NONCE PLANNED RESET");
+    else
+      LOG_INFO("NONCE NO PLANNED RESET");

     d_ptr->job   = job;
     d_ptr->job.setIndex(index);
```
```
diff --git a/src/backend/common/WorkerJob.h b/src/backend/common/WorkerJob.h
index b579a116..f151d92d 100644
--- a/src/backend/common/WorkerJob.h
+++ b/src/backend/common/WorkerJob.h
@@ -32,6 +32,7 @@
 #include "base/net/stratum/Job.h"
 #include "base/tools/Alignment.h"
 #include "crypto/common/Nonce.h"
+#include "base/io/log/Log.h"


 namespace xmrig {
@@ -141,6 +142,7 @@ inline bool xmrig::WorkerJob<1>::nextRound(uint32_t rounds, uint32_t roundSize)
         }
     }
     else {
+        if ((m_rounds[index()] & 4095) == 0) LOG_INFO("r %08x %08x\n", n, *n);
         writeUnaligned(n, readUnaligned(n) + roundSize);
     }
```
```
diff --git a/src/crypto/common/Nonce.cpp b/src/crypto/common/Nonce.cpp
index feb48786..6fc95ebb 100644
--- a/src/crypto/common/Nonce.cpp
+++ b/src/crypto/common/Nonce.cpp
@@ -18,6 +18,8 @@

 #include "base/tools/Alignment.h"
 #include "crypto/common/Nonce.h"
+#include <cstdio>
+#include "base/io/log/Log.h"


 namespace xmrig {
@@ -33,12 +35,14 @@ std::atomic<uint64_t> Nonce::m_nonces[2] = { {0}, {0} };
 bool xmrig::Nonce::next(uint8_t index, uint32_t *nonce, uint32_t reserveCount, uint64_t mask)
 {
     mask &= 0x7FFFFFFFFFFFFFFFULL;
+    //printf("%08x\n", *nonce);
     if (reserveCount == 0 || mask < reserveCount - 1) {
         return false;
     }

     uint64_t counter = m_nonces[index].fetch_add(reserveCount, std::memory_order_relaxed);
     while (true) {
+        //printf("? %08x\n", *nonce);
         if (mask < counter) {
             return false;
         }
@@ -55,9 +59,11 @@ bool xmrig::Nonce::next(uint8_t index, uint32_t *nonce, uint32_t reserveCount, u
         }

         writeUnaligned(nonce, static_cast<uint32_t>((readUnaligned(nonce) & ~mask) | counter));
+        LOG_INFO("+++ %08x %08x\n", nonce, *nonce);

         if (mask > 0xFFFFFFFFULL) {
             writeUnaligned(nonce + 1, static_cast<uint32_t>((readUnaligned(nonce + 1) & (~mask >> 32)) | (counter >> 32)));
+            LOG_INFO("*** %08x %08x\n", nonce, *nonce);
         }

         return true;
```


Here is log output that leads to duplicate share:

1) Nonce counters became high:

```
[2024-02-01 03:02:31.053] r 14000c0f 00042fff
[2024-02-01 03:02:31.063] r 2c000c0f 0004afff
[2024-02-01 03:02:31.110] r 0c000c0f 00052fff
[2024-02-01 03:02:31.201] r 24000c0f 00062fff
[2024-02-01 03:02:31.231] r 1c000c0f 0005afff
[2024-02-01 03:02:31.820] r 34000c0f 0006afff
[2024-02-01 03:02:32.203] r fc000c0f 00072fff
[2024-02-01 03:02:32.316] r 04000c0f 0007afff
[2024-02-01 03:02:36.645] r 2c000c0f 0004bfff
[2024-02-01 03:02:36.647] r 14000c0f 00043fff
[2024-02-01 03:02:36.690] r 0c000c0f 00053fff
[2024-02-01 03:02:36.778] r 24000c0f 00063fff
[2024-02-01 03:02:36.941] r 1c000c0f 0005bfff
[2024-02-01 03:02:37.434] r 34000c0f 0006bfff
[2024-02-01 03:02:37.930] r fc000c0f 00073fff
[2024-02-01 03:02:37.983] r 04000c0f 0007bfff
```

2) We got job with seed change that not really resets nonces to 0 (00000000, 00008000, ..., 00038000). That seems to be an issue here:

```
[2024-02-01 03:02:41.134] [gulf.moneroocean.stream:20016] received (608 bytes): "{"method":"job","params":{"blob":"0303caf4edad064b38a5235759a6f7007ce00d74db868a05947da7c6014b757bfd17ad4962add9000000006092c116d00a0000307355efd00a000090857d9513000000f05ef593130000007047837a080100004068db7c080100004b7abb65000000006c2f8325d870de1fbfaf687b9e9065807f45ff4b2aa760d4f370639727f9ae349afbd867b0a5aee7e5a0267b88590f3eed466f42456a4f991d669f3fb7e7142767f744ffcaa8052cc38e904761fedce160cd1f1b82e8c9484efe4a627330159001","algo":"rx/0","height":176703,"seed_hash":"17c904b484673b80c6b796fa1f81cf4cf45294b3e3db16143dc248e66be231e8","job_id":"4291851","target":"07500000","id":"3681101"},"jsonrpc":"2.0"}"
[2024-02-01 03:02:41.134]  net      new job from gulf.moneroocean.stream:20016 diff 209643 algo rx/0 height 176703
[2024-02-01 03:02:41.134] NONCE PLANNED RESET
[2024-02-01 03:02:41.134]  randomx  init dataset algo rx/0 (16 threads) seed 17c904b484673b80...
[2024-02-01 03:02:41.136] +++ 14000c0f 00080000
[2024-02-01 03:02:41.136] +++ 2c000c0f 00088000
[2024-02-01 03:02:41.136] +++ 1c000c0f 00090000
[2024-02-01 03:02:41.136] +++ 24000c0f 00098000
[2024-02-01 03:02:41.136] +++ 04000c0f 000a0000
[2024-02-01 03:02:41.136] +++ fc000c0f 000a8000
[2024-02-01 03:02:41.136] +++ 0c000c0f 000b0000
[2024-02-01 03:02:41.137] +++ 34000c0f 000b8000
[2024-02-01 03:02:42.990]  randomx  dataset ready (1856 ms)
[2024-02-01 03:02:42.990] NONCE RESET REAL
```

3) We find the first share with 74c60b00 nonce:

```
[2024-02-01 03:03:07.742] [gulf.moneroocean.stream:20016] send (185 bytes): "{"id":392,"jsonrpc":"2.0","method":"submit","params":{"id":"3681101","job_id":"4291851","nonce":"74c60b00","result":"06cc92d52e12775807f04802cb14cdf364491845e4ae9beb45727cd1e33f0000"}}"
[2024-02-01 03:03:07.742] [gulf.moneroocean.stream:20016] TLS send     (207 bytes)
[2024-02-01 03:03:08.180] [gulf.moneroocean.stream:20016] TLS received (87 bytes)
[2024-02-01 03:03:08.180] [gulf.moneroocean.stream:20016] received (64 bytes): "{"jsonrpc":"2.0","id":392,"error":null,"result":{"status":"OK"}}"
[2024-02-01 03:03:08.180]  cpu      accepted (357/0) diff 209643 (439 ms)
```

4) We reset nonces after they reach maximums (or issue can be here and not in step 2 since we do real nonce reset to 0 this late):

```
[2024-02-01 03:03:22.522] r 34000c0f 000befff
[2024-02-01 03:03:22.524] r 0c000c0f 000b6fff
[2024-02-01 03:03:22.559] r 2c000c0f 0008efff
[2024-02-01 03:03:22.698] r 04000c0f 000a6fff
[2024-02-01 03:03:22.744] r 1c000c0f 00096fff
[2024-02-01 03:03:22.764] r 14000c0f 00086fff
[2024-02-01 03:03:22.978] r 24000c0f 0009efff
[2024-02-01 03:03:23.171] r fc000c0f 000aefff
```

```
[2024-02-01 03:03:28.141] +++ 34000c0f 00000000
[2024-02-01 03:03:28.157] +++ 0c000c0f 00008000
[2024-02-01 03:03:28.252] +++ 2c000c0f 00010000
[2024-02-01 03:03:28.344] +++ 04000c0f 00018000
[2024-02-01 03:03:28.375] +++ 14000c0f 00020000
[2024-02-01 03:03:28.402] +++ 1c000c0f 00028000
[2024-02-01 03:03:28.593] +++ 24000c0f 00030000
[2024-02-01 03:03:29.040] +++ fc000c0f 00038000
```

5) We submit dulicate share with the same 74c60b00 nonce:

```
[2024-02-01 03:05:28.248] [gulf.moneroocean.stream:20016] send (185 bytes): "{"id":396,"jsonrpc":"2.0","method":"submit","params":{"id":"3681101","job_id":"4291851","nonce":"74c60b00","result":"06cc92d52e12775807f04802cb14cdf364491845e4ae9beb45727cd1e33f0000"}}"
[2024-02-01 03:05:28.248] [gulf.moneroocean.stream:20016] TLS send     (207 bytes)
[2024-02-01 03:05:28.280] [gulf.moneroocean.stream:20016] TLS received (97 bytes)
[2024-02-01 03:05:28.280] [gulf.moneroocean.stream:20016] received (74 bytes): "{"jsonrpc":"2.0","id":396,"error":{"code":-1,"message":"Duplicate share"}}"
[2024-02-01 03:05:28.280]  cpu      rejected (359/1) diff 209643 "Duplicate share" (32 ms)
[2024-02-01 03:05:29.522]  miner    speed 10s/60s/15m 5694.4 5762.7 5743.3 H/s max 6055.0 H/s

```

## SChernykh | 2024-02-02T07:23:08+00:00
I think what happens here is that nonce reset happens after dataset init, but mining threads already started working on the new job using old nonce values. Nonce reset sets nonce to 0, but it takes effect only when mining threads reach the end of their current interval, so if the old value was small enough (from the last reset before the new dataset), it can overlap a bit later. I'll think about how to fix it better.

## SChernykh | 2024-02-02T07:25:38+00:00
@MoneroOcean how often do you send new jobs to miners? Reset happens every 32768 nonce values (per thread), so if you send new jobs every 15 seconds, no CPU will be able to reach the end of their interval within that time - required per-thread hashrate must be > 2 kh/s. ~Or did you decrease 32768 to a smaller value in MO version?~

## SChernykh | 2024-02-02T13:48:50+00:00
After looking more into it, I think that nonce gets reset to 0 after dataset init, miner threads start mining, then nonce gets reset again somewhere (?), and when miner threads try 32768 nonce values, they ask for new nonce ranges and get the same ranges (starting from 0).

## SChernykh | 2024-02-02T13:53:43+00:00
As a temporary fix, you should send new jobs more often (every 15-20 seconds). I thought you already did it, hmm: https://www.reddit.com/r/Monero/comments/11nu4aj/monero_transaction_confirmations_are_now_60/

## MoneroOcean | 2024-02-02T15:51:06+00:00
It is only for XMR. For other coins I update job only with new height.

## SChernykh | 2024-08-14T12:48:48+00:00
I did a new test and this is what I found:
```
[2024-08-14 14:45:01.152]  net      use daemon 127.0.0.1:28081  127.0.0.1
[2024-08-14 14:45:01.153]  net      new job from 127.0.0.1:28081 diff 1000 algo rx/0 height 2560064 (1 tx)
[2024-08-14 14:45:01.153]  cpu      use argon2 implementation AVX2
[2024-08-14 14:45:01.153]  msr      to access MSR registers Administrator privileges required.
[2024-08-14 14:45:01.153]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2024-08-14 14:45:01.154] NONCE PENDING RESET
[2024-08-14 14:45:01.154]  randomx  init dataset algo rx/0 (8 threads) seed d08c64d1045a7572...
[2024-08-14 14:45:01.423]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (270 ms)
[2024-08-14 14:45:05.245]  randomx  dataset ready (3821 ms)
[2024-08-14 14:45:05.245] NONCE RESET
[2024-08-14 14:45:05.246]  cpu      use profile  *  (1 thread) scratchpad 2048 KB
[2024-08-14 14:45:05.252]  cpu      READY threads 1/1 (1) huge pages 100% 1/1 memory 2048 KB (5 ms)
[2024-08-14 14:45:05.252] consumeJob
[2024-08-14 14:45:05.260] Starting nonce = 0
[2024-08-14 14:45:07.488]  cpu      accepted (1/0) diff 1000 (128 ms)
[2024-08-14 14:45:07.490]  net      new job from 127.0.0.1:28081 diff 1000 algo rx/0 height 2560065 (1 tx)
[2024-08-14 14:45:07.490] NONCE PENDING RESET
[2024-08-14 14:45:07.490]  randomx  init dataset algo rx/0 (8 threads) seed a9af0b7124fe61a8...
[2024-08-14 14:45:07.490] consumeJob
[2024-08-14 14:45:11.263]  randomx  dataset ready (3774 ms)
[2024-08-14 14:45:11.264] NONCE RESET
[2024-08-14 14:45:11.293] consumeJob
[2024-08-14 14:45:11.294] Starting nonce = 960
[2024-08-14 14:45:11.774]  cpu      accepted (2/0) diff 1000 (70 ms)
[2024-08-14 14:45:11.777]  net      new job from 127.0.0.1:28081 diff 1000 algo rx/0 height 2560066 (1 tx)
```

Pay attention to the part
```
[2024-08-14 14:45:07.490] consumeJob
[2024-08-14 14:45:11.263]  randomx  dataset ready (3774 ms)
[2024-08-14 14:45:11.264] NONCE RESET
[2024-08-14 14:45:11.293] consumeJob
[2024-08-14 14:45:11.294] Starting nonce = 960
```

It resets the nonce between two consecutive `consumeJob` calls, and the second call exits early because the job didn't change, and the new nonce doesn't get applied from the start. It started from the nonce 960, then reset it to 0 later and went through 960 again.

## SChernykh | 2024-08-14T12:57:15+00:00
@MoneroOcean can you try #3531 ?

## MoneroOcean | 2024-08-14T14:42:31+00:00
I certanly can. Thank you! Will see if it helps in mo xmrig [v6.22.0-mo3](https://github.com/MoneroOcean/xmrig/tree/v6.22.0-mo3)

## SChernykh | 2025-06-08T16:12:55+00:00
@MoneroOcean any updates on this? Did the fix help?

We have a similar bug report in the current version: https://www.reddit.com/r/MoneroMining/comments/1l6enyj/xmrig_bug/

## MoneroOcean | 2025-06-08T20:40:09+00:00
Yes, I think it solved the problem for me as far as I remember.

## MoneroOcean | 2025-06-17T05:59:02+00:00
It looks like different issue not related to seed change fixed here: https://github.com/xmrig/xmrig/issues/3669

# Action History
- Created by: MoneroOcean | 2024-01-21T16:51:43+00:00
- Closed at: 2025-06-16T19:58:37+00:00
