---
title: Fails with <randomx_prepare>:39 "out of memory"
source_url: https://github.com/xmrig/xmrig/issues/1355
author: Yaaman42
assignees: []
labels:
- CUDA
- randomx
created_at: '2019-12-01T13:20:41+00:00'
updated_at: '2022-04-04T12:56:27+00:00'
type: issue
status: closed
closed_at: '2019-12-04T00:31:33+00:00'
---

# Original Description
Ive got XMRig running on my single GPU system, just fine. But when trying on my 4 GPU rig, it fails as below. Any ideas?

 * CPU          Intel(R) Pentium(R) CPU G4400 @ 3.30GHz (1) x64 AES
                L2:0.5 MB L3:3.0 MB 2C/2T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.crypto-pool.fr:9999 coin monero
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         10.1/10.2/2.0.1-beta
 * NVML         10.441.41/441.41 press e for health report
 * CUDA GPU     #0 02:00.0 GeForce GTX 1070 Ti 1683/4004 MHz smx:19 arch:61 mem:6767/8192 MB
 * CUDA GPU     #1 03:00.0 GeForce GTX 1070 Ti 1683/4004 MHz smx:19 arch:61 mem:6767/8192 MB
 * CUDA GPU     #2 01:00.0 GeForce GTX 1070 1683/4004 MHz smx:15 arch:61 mem:6792/8192 MB
 * CUDA GPU     #3 04:00.0 GeForce GTX 1070 1835/4004 MHz smx:15 arch:61 mem:6792/8192 MB
[2019-12-01 14:08:39.316]  net  use pool xmr.crypto-pool.fr:9999  163.172.226.137
[2019-12-01 14:08:39.321]  net  new job from xmr.crypto-pool.fr:9999 diff 50000 algo rx/0 height 1979246
[2019-12-01 14:08:39.322]  rx   init dataset algo rx/0 (2 threads) seed 993ba25f61d47e1e...
[2019-12-01 14:08:39.382]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (59 ms)
[2019-12-01 14:08:50.647]  rx   dataset ready (11264 ms)
[2019-12-01 14:08:50.648]  nv   use profile  rx  (4 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |   T |   B | BF |  BS |  MEM | NAME
|  0 |   0 | 02:00.0 | 1216 |  32 |  38 |  6 |  25 | 2432 | GeForce GTX 1070 Ti
|  1 |   1 | 03:00.0 | 1216 |  32 |  38 |  6 |  25 | 2432 | GeForce GTX 1070 Ti
|  2 |   2 | 01:00.0 |  960 |  32 |  30 |  6 |  25 | 1920 | GeForce GTX 1070
|  3 |   3 | 04:00.0 |  960 |  32 |  30 |  6 |  25 | 1920 | GeForce GTX 1070
[2019-12-01 14:08:51.486]  nv   READY threads 4/4 (836 ms)
[2019-12-01 14:08:51.638]  nv   thread #1 failed with error <randomx_prepare>:39 "out of memory"
[2019-12-01 14:08:51.673]  nv   thread #3 failed with error <randomx_prepare>:39 "out of memory"
[2019-12-01 14:08:54.822]  nv   thread #2 failed with error <randomx_prepare>:43 "out of memory"
[2019-12-01 14:08:57.129]  nv   thread #0 failed with error <randomx_prepare>:43 "out of memory"


# Discussion History
## awakened888 | 2019-12-01T14:59:47+00:00
Same here with GTX 1060 6GB and 1050 Ti. One GPU runs fine. Been trying different things but can't get all of the cards to work. Only 3 of 6 or 2 of 4 work.

## Yaaman42 | 2019-12-01T15:17:36+00:00
Yeah, I can sometimes, at random it seems, get one of the four cards running. I wonder if it's system RAM or the memory on the gpus that's referred to in the error message. 

## awakened888 | 2019-12-01T15:48:54+00:00
I was wondering the same. But I have 8GB system on one of the machines, still same error. So, I'm starting to think it's not system memory. Or maybe it's the allocation of it somehow.

## Yaaman42 | 2019-12-01T15:57:00+00:00
Yeah, got 8 Gb in my rig too. And watching the resource monitor, there's still plenty of RAM when the errors pops up. 

## hawk-eye77 | 2019-12-01T18:29:55+00:00
 * CUDA         10.1/10.2/2.0.1-beta
 * NVML         10.441.28/441.28 press e for health report
 * CUDA GPU     #0 01:00.0 GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61 mem:2482/3072 MB
 * CUDA GPU     #1 04:00.0 GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61 mem:2482/3072 MB
[2019-12-01 21:13:44.508]  net  use pool xmr-eu1.nanopool.org:14433 TLSv1.2 79.137.82.5
[2019-12-01 21:13:44.511]  net  fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2019-12-01 21:13:44.511]  net  new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 1979413
[2019-12-01 21:13:44.512]  rx   init dataset algo rx/0 (2 threads) seed 993ba25f61d47e1e...
[2019-12-01 21:13:44.546]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (34 ms)
[2019-12-01 21:13:54.463]  net  new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 1979413
[2019-12-01 21:14:24.669]  rx   dataset ready (40113 ms)
[2019-12-01 21:14:24.670]  cpu  use profile  rx  (2 threads) scratchpad 2048 KB
[2019-12-01 21:14:24.758]  nv   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |   T |   B | BF |  BS |  MEM | NAME
|  0 |   0 | 01:00.0 |  576 |  32 |  18 |  6 |  25 | 1152 | GeForce GTX 1060 3GB
|  1 |   1 | 04:00.0 |  576 |  32 |  18 |  6 |  25 | 1152 | GeForce GTX 1060 3GB
[2019-12-01 21:14:24.846]  cpu  READY threads 2/2 (2) huge pages 0% 0/2 memory 4096 KB (176 ms)
[2019-12-01 21:14:38.963]  nv   READY threads 2/2 (14201 ms)
[2019-12-01 21:14:39.252]  nv   thread #1 failed with error <DatasetHost::reg>:50 "out of memory"
[2019-12-01 21:14:39.271]  nv   thread #0 failed with error <randomx_prepare>:36 "invalid argument" "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 18,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": true
            },
            {
                "index": 1,
                "threads": 32,
                "blocks": 18,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": true
            }


## prapor102 | 2019-12-03T06:53:13+00:00
could you solve the problem??

## awakened888 | 2019-12-03T07:28:48+00:00
I haven't yet. Still only one GPU works. Others get the 39 "out of memory" message.

## awakened888 | 2019-12-03T10:55:52+00:00
Solved it! Increase Windows virtual memory size. It uses a huge chunk of it. After that, all GPU-s mine properly!

## prapor102 | 2019-12-03T13:56:00+00:00
thnk...i have 8k-20k virtual memory size, no work....
[2019-12-01 21:14:39.252] nv thread #1 failed with error DatasetHost::reg:50 "out of memory"
[2019-12-01 21:14:39.271] nv thread #0 failed with error <randomx_prepare>:36 "invalid argument" 
and how to win? pool xmr-eu1.nanopool.org...

## awakened888 | 2019-12-03T16:40:48+00:00
I increased it even more. The rig with 4 GPU-s, virtual memory 50000-60000. The rig with 6 GPU-s needed even more. 70000-80000. Both still mining with all GPU-s without interruptions.

## Yaaman42 | 2019-12-04T00:03:18+00:00
Are you talking about windows page file, or is there a parameter in xmrig for virtual memory?

## Yaaman42 | 2019-12-04T00:31:33+00:00
Went from 8Gb of page file to 25Gb page file. Seems to have solved the problem, however it seems a bit excessive with that amount of swap space. 

## Saikatsaha1996 | 2020-10-11T13:48:15+00:00
> * CUDA         10.1/10.2/2.0.1-beta
> * NVML         10.441.28/441.28 press e for health report
> * CUDA GPU     #0 01:00.0 GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61 mem:2482/3072 MB
> * CUDA GPU     #1 04:00.0 GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61 mem:2482/3072 MB
>   [2019-12-01 21:13:44.508]  net  use pool xmr-eu1.nanopool.org:14433 TLSv1.2 79.137.82.5
>   [2019-12-01 21:13:44.511]  net  fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
>   [2019-12-01 21:13:44.511]  net  new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 1979413
>   [2019-12-01 21:13:44.512]  rx   init dataset algo rx/0 (2 threads) seed 993ba25f61d47e1e...
>   [2019-12-01 21:13:44.546]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (34 ms)
>   [2019-12-01 21:13:54.463]  net  new job from xmr-eu1.nanopool.org:14433 diff 480045 algo rx/0 height 1979413
>   [2019-12-01 21:14:24.669]  rx   dataset ready (40113 ms)
>   [2019-12-01 21:14:24.670]  cpu  use profile  rx  (2 threads) scratchpad 2048 KB
>   [2019-12-01 21:14:24.758]  nv   use profile  rx  (2 threads) scratchpad 2048 KB
>   |  # | GPU |  BUS ID |    I |   T |   B | BF |  BS |  MEM | NAME
>   |  0 |   0 | 01:00.0 |  576 |  32 |  18 |  6 |  25 | 1152 | GeForce GTX 1060 3GB
>   |  1 |   1 | 04:00.0 |  576 |  32 |  18 |  6 |  25 | 1152 | GeForce GTX 1060 3GB
>   [2019-12-01 21:14:24.846]  cpu  READY threads 2/2 (2) huge pages 0% 0/2 memory 4096 KB (176 ms)
>   [2019-12-01 21:14:38.963]  nv   READY threads 2/2 (14201 ms)
>   [2019-12-01 21:14:39.252]  nv   thread #1 failed with error DatasetHost::reg:50 "out of memory"
>   [2019-12-01 21:14:39.271]  nv   thread #0 failed with error <randomx_prepare>:36 "invalid argument" "rx": [
>   {
>   "index": 0,
>   "threads": 32,
>   "blocks": 18,
>   "bfactor": 6,
>   "bsleep": 25,
>   "affinity": -1,
>   "dataset_host": true
>   },
>   {
>   "index": 1,
>   "threads": 32,
>   "blocks": 18,
>   "bfactor": 6,
>   "bsleep": 25,
>   "affinity": -1,
>   "dataset_host": true
>   }

Your problem now solved ? Or not ? Because i got same problem..can you help me ?

## Yaaman42 | 2020-10-11T15:44:30+00:00
I got it working using a ridiculous amount of swap space.

On Sun, Oct 11, 2020, 15:48 Saikatsaha1996 <notifications@github.com> wrote:

>
>    - CUDA 10.1/10.2/2.0.1-beta
>    - NVML 10.441.28/441.28 press e for health report
>    - CUDA GPU #0 01:00.0 GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61
>    mem:2482/3072 MB
>    - CUDA GPU #1 <https://github.com/xmrig/xmrig/issues/1> 04:00.0
>    GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61 mem:2482/3072 MB
>    [2019-12-01 21:13:44.508] net use pool xmr-eu1.nanopool.org:14433
>    TLSv1.2 79.137.82.5
>    [2019-12-01 21:13:44.511] net fingerprint (SHA-256):
>    "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
>    [2019-12-01 21:13:44.511] net new job from xmr-eu1.nanopool.org:14433
>    diff 480045 algo rx/0 height 1979413
>    [2019-12-01 21:13:44.512] rx init dataset algo rx/0 (2 threads) seed
>    993ba25f61d47e1e...
>    [2019-12-01 21:13:44.546] rx allocated 2336 MB (2080+256) huge pages
>    0% 0/1168 +JIT (34 ms)
>    [2019-12-01 21:13:54.463] net new job from xmr-eu1.nanopool.org:14433
>    diff 480045 algo rx/0 height 1979413
>    [2019-12-01 21:14:24.669] rx dataset ready (40113 ms)
>    [2019-12-01 21:14:24.670] cpu use profile rx (2 threads) scratchpad
>    2048 KB
>    [2019-12-01 21:14:24.758] nv use profile rx (2 threads) scratchpad
>    2048 KB
>    | # | GPU | BUS ID | I | T | B | BF | BS | MEM | NAME
>    | 0 | 0 | 01:00.0 | 576 | 32 | 18 | 6 | 25 | 1152 | GeForce GTX 1060
>    3GB
>    | 1 | 1 | 04:00.0 | 576 | 32 | 18 | 6 | 25 | 1152 | GeForce GTX 1060
>    3GB
>    [2019-12-01 21:14:24.846] cpu READY threads 2/2 (2) huge pages 0% 0/2
>    memory 4096 KB (176 ms)
>    [2019-12-01 21:14:38.963] nv READY threads 2/2 (14201 ms)
>    [2019-12-01 21:14:39.252] nv thread #1
>    <https://github.com/xmrig/xmrig/issues/1> failed with error
>    DatasetHost::reg:50 "out of memory"
>    [2019-12-01 21:14:39.271] nv thread #0 failed with error
>    <randomx_prepare>:36 "invalid argument" "rx": [
>    {
>    "index": 0,
>    "threads": 32,
>    "blocks": 18,
>    "bfactor": 6,
>    "bsleep": 25,
>    "affinity": -1,
>    "dataset_host": true
>    },
>    {
>    "index": 1,
>    "threads": 32,
>    "blocks": 18,
>    "bfactor": 6,
>    "bsleep": 25,
>    "affinity": -1,
>    "dataset_host": true
>    }
>
> Your problem now solved ? Or not ? Because i got same problem..can you
> help me ?
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1355#issuecomment-706707481>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AKV6LC4QEN5X5TNEVUBNE7DSKGZSXANCNFSM4JTLUX5Q>
> .
>


## Saikatsaha1996 | 2020-10-11T16:06:40+00:00
> I got it working using a ridiculous amount of swap space.
> 
> On Sun, Oct 11, 2020, 15:48 Saikatsaha1996 <notifications@github.com> wrote:
> 
> >
> >    - CUDA 10.1/10.2/2.0.1-beta
> >    - NVML 10.441.28/441.28 press e for health report
> >    - CUDA GPU #0 01:00.0 GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61
> >    mem:2482/3072 MB
> >    - CUDA GPU #1 <https://github.com/xmrig/xmrig/issues/1> 04:00.0
> >    GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61 mem:2482/3072 MB
> >    [2019-12-01 21:13:44.508] net use pool xmr-eu1.nanopool.org:14433
> >    TLSv1.2 79.137.82.5
> >    [2019-12-01 21:13:44.511] net fingerprint (SHA-256):
> >    "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
> >    [2019-12-01 21:13:44.511] net new job from xmr-eu1.nanopool.org:14433
> >    diff 480045 algo rx/0 height 1979413
> >    [2019-12-01 21:13:44.512] rx init dataset algo rx/0 (2 threads) seed
> >    993ba25f61d47e1e...
> >    [2019-12-01 21:13:44.546] rx allocated 2336 MB (2080+256) huge pages
> >    0% 0/1168 +JIT (34 ms)
> >    [2019-12-01 21:13:54.463] net new job from xmr-eu1.nanopool.org:14433
> >    diff 480045 algo rx/0 height 1979413
> >    [2019-12-01 21:14:24.669] rx dataset ready (40113 ms)
> >    [2019-12-01 21:14:24.670] cpu use profile rx (2 threads) scratchpad
> >    2048 KB
> >    [2019-12-01 21:14:24.758] nv use profile rx (2 threads) scratchpad
> >    2048 KB
> >    | # | GPU | BUS ID | I | T | B | BF | BS | MEM | NAME
> >    | 0 | 0 | 01:00.0 | 576 | 32 | 18 | 6 | 25 | 1152 | GeForce GTX 1060
> >    3GB
> >    | 1 | 1 | 04:00.0 | 576 | 32 | 18 | 6 | 25 | 1152 | GeForce GTX 1060
> >    3GB
> >    [2019-12-01 21:14:24.846] cpu READY threads 2/2 (2) huge pages 0% 0/2
> >    memory 4096 KB (176 ms)
> >    [2019-12-01 21:14:38.963] nv READY threads 2/2 (14201 ms)
> >    [2019-12-01 21:14:39.252] nv thread #1
> >    <https://github.com/xmrig/xmrig/issues/1> failed with error
> >    DatasetHost::reg:50 "out of memory"
> >    [2019-12-01 21:14:39.271] nv thread #0 failed with error
> >    <randomx_prepare>:36 "invalid argument" "rx": [
> >    {
> >    "index": 0,
> >    "threads": 32,
> >    "blocks": 18,
> >    "bfactor": 6,
> >    "bsleep": 25,
> >    "affinity": -1,
> >    "dataset_host": true
> >    },
> >    {
> >    "index": 1,
> >    "threads": 32,
> >    "blocks": 18,
> >    "bfactor": 6,
> >    "bsleep": 25,
> >    "affinity": -1,
> >    "dataset_host": true
> >    }
> >
> > Your problem now solved ? Or not ? Because i got same problem..can you
> > help me ?
> >
> > —
> > You are receiving this because you modified the open/close state.
> > Reply to this email directly, view it on GitHub
> > <https://github.com/xmrig/xmrig/issues/1355#issuecomment-706707481>, or
> > unsubscribe
> > <https://github.com/notifications/unsubscribe-auth/AKV6LC4QEN5X5TNEVUBNE7DSKGZSXANCNFSM4JTLUX5Q>
> > .
> >
> 

How can i swap space can you explain it?

## Yaaman42 | 2020-10-13T07:51:51+00:00
Windows system settings for virtual memory.

On Sun, Oct 11, 2020, 18:06 Saikatsaha1996 <notifications@github.com> wrote:

> I got it working using a ridiculous amount of swap space.
>
> On Sun, Oct 11, 2020, 15:48 Saikatsaha1996 notifications@github.com wrote:
>
>
>    - CUDA 10.1/10.2/2.0.1-beta
>    - NVML 10.441.28/441.28 press e for health report
>    - CUDA GPU #0 01:00.0 GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61
>    mem:2482/3072 MB
>    - CUDA GPU #1 <https://github.com/xmrig/xmrig/issues/1> #1
>    <https://github.com/xmrig/xmrig/issues/1> 04:00.0
>    GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61 mem:2482/3072 MB
>    [2019-12-01 21:13:44.508] net use pool xmr-eu1.nanopool.org:14433
>    TLSv1.2 79.137.82.5
>    [2019-12-01 21:13:44.511] net fingerprint (SHA-256):
>    "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
>    [2019-12-01 21:13:44.511] net new job from xmr-eu1.nanopool.org:14433
>    diff 480045 algo rx/0 height 1979413
>    [2019-12-01 21:13:44.512] rx init dataset algo rx/0 (2 threads) seed
>    993ba25f61d47e1e...
>    [2019-12-01 21:13:44.546] rx allocated 2336 MB (2080+256) huge pages
>    0% 0/1168 +JIT (34 ms)
>    [2019-12-01 21:13:54.463] net new job from xmr-eu1.nanopool.org:14433
>    diff 480045 algo rx/0 height 1979413
>    [2019-12-01 21:14:24.669] rx dataset ready (40113 ms)
>    [2019-12-01 21:14:24.670] cpu use profile rx (2 threads) scratchpad
>    2048 KB
>    [2019-12-01 21:14:24.758] nv use profile rx (2 threads) scratchpad
>    2048 KB
>    | # | GPU | BUS ID | I | T | B | BF | BS | MEM | NAME
>    | 0 | 0 | 01:00.0 | 576 | 32 | 18 | 6 | 25 | 1152 | GeForce GTX 1060
>    3GB
>    | 1 | 1 | 04:00.0 | 576 | 32 | 18 | 6 | 25 | 1152 | GeForce GTX 1060
>    3GB
>    [2019-12-01 21:14:24.846] cpu READY threads 2/2 (2) huge pages 0% 0/2
>    memory 4096 KB (176 ms)
>    [2019-12-01 21:14:38.963] nv READY threads 2/2 (14201 ms)
>    [2019-12-01 21:14:39.252] nv thread #1
>    <https://github.com/xmrig/xmrig/issues/1>
>    #1 <https://github.com/xmrig/xmrig/issues/1> failed with error
>    DatasetHost::reg:50 "out of memory"
>    [2019-12-01 21:14:39.271] nv thread #0 failed with error
>    <randomx_prepare>:36 "invalid argument" "rx": [
>    {
>    "index": 0,
>    "threads": 32,
>    "blocks": 18,
>    "bfactor": 6,
>    "bsleep": 25,
>    "affinity": -1,
>    "dataset_host": true
>    },
>    {
>    "index": 1,
>    "threads": 32,
>    "blocks": 18,
>    "bfactor": 6,
>    "bsleep": 25,
>    "affinity": -1,
>    "dataset_host": true
>    }
>
> Your problem now solved ? Or not ? Because i got same problem..can you
> help me ?
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> #1355 (comment)
> <https://github.com/xmrig/xmrig/issues/1355#issuecomment-706707481>, or
> unsubscribe
>
> https://github.com/notifications/unsubscribe-auth/AKV6LC4QEN5X5TNEVUBNE7DSKGZSXANCNFSM4JTLUX5Q
> .
>
> How can i swap space can you explain it?
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1355#issuecomment-706727157>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AKV6LCZHO3DDBTGG47FSWLTSKHJZ5ANCNFSM4JTLUX5Q>
> .
>


## Saikatsaha1996 | 2020-10-13T08:14:54+00:00
> Windows system settings for virtual memory.
> 
> On Sun, Oct 11, 2020, 18:06 Saikatsaha1996 <notifications@github.com> wrote:
> 
> > I got it working using a ridiculous amount of swap space.
> >
> > On Sun, Oct 11, 2020, 15:48 Saikatsaha1996 notifications@github.com wrote:
> >
> >
> >    - CUDA 10.1/10.2/2.0.1-beta
> >    - NVML 10.441.28/441.28 press e for health report
> >    - CUDA GPU #0 01:00.0 GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61
> >    mem:2482/3072 MB
> >    - CUDA GPU #1 <https://github.com/xmrig/xmrig/issues/1> #1
> >    <https://github.com/xmrig/xmrig/issues/1> 04:00.0
> >    GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61 mem:2482/3072 MB
> >    [2019-12-01 21:13:44.508] net use pool xmr-eu1.nanopool.org:14433
> >    TLSv1.2 79.137.82.5
> >    [2019-12-01 21:13:44.511] net fingerprint (SHA-256):
> >    "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
> >    [2019-12-01 21:13:44.511] net new job from xmr-eu1.nanopool.org:14433
> >    diff 480045 algo rx/0 height 1979413
> >    [2019-12-01 21:13:44.512] rx init dataset algo rx/0 (2 threads) seed
> >    993ba25f61d47e1e...
> >    [2019-12-01 21:13:44.546] rx allocated 2336 MB (2080+256) huge pages
> >    0% 0/1168 +JIT (34 ms)
> >    [2019-12-01 21:13:54.463] net new job from xmr-eu1.nanopool.org:14433
> >    diff 480045 algo rx/0 height 1979413
> >    [2019-12-01 21:14:24.669] rx dataset ready (40113 ms)
> >    [2019-12-01 21:14:24.670] cpu use profile rx (2 threads) scratchpad
> >    2048 KB
> >    [2019-12-01 21:14:24.758] nv use profile rx (2 threads) scratchpad
> >    2048 KB
> >    | # | GPU | BUS ID | I | T | B | BF | BS | MEM | NAME
> >    | 0 | 0 | 01:00.0 | 576 | 32 | 18 | 6 | 25 | 1152 | GeForce GTX 1060
> >    3GB
> >    | 1 | 1 | 04:00.0 | 576 | 32 | 18 | 6 | 25 | 1152 | GeForce GTX 1060
> >    3GB
> >    [2019-12-01 21:14:24.846] cpu READY threads 2/2 (2) huge pages 0% 0/2
> >    memory 4096 KB (176 ms)
> >    [2019-12-01 21:14:38.963] nv READY threads 2/2 (14201 ms)
> >    [2019-12-01 21:14:39.252] nv thread #1
> >    <https://github.com/xmrig/xmrig/issues/1>
> >    #1 <https://github.com/xmrig/xmrig/issues/1> failed with error
> >    DatasetHost::reg:50 "out of memory"
> >    [2019-12-01 21:14:39.271] nv thread #0 failed with error
> >    <randomx_prepare>:36 "invalid argument" "rx": [
> >    {
> >    "index": 0,
> >    "threads": 32,
> >    "blocks": 18,
> >    "bfactor": 6,
> >    "bsleep": 25,
> >    "affinity": -1,
> >    "dataset_host": true
> >    },
> >    {
> >    "index": 1,
> >    "threads": 32,
> >    "blocks": 18,
> >    "bfactor": 6,
> >    "bsleep": 25,
> >    "affinity": -1,
> >    "dataset_host": true
> >    }
> >
> > Your problem now solved ? Or not ? Because i got same problem..can you
> > help me ?
> >
> > —
> > You are receiving this because you modified the open/close state.
> > Reply to this email directly, view it on GitHub
> > #1355 (comment)
> > <https://github.com/xmrig/xmrig/issues/1355#issuecomment-706707481>, or
> > unsubscribe
> >
> > https://github.com/notifications/unsubscribe-auth/AKV6LC4QEN5X5TNEVUBNE7DSKGZSXANCNFSM4JTLUX5Q
> > .
> >
> > How can i swap space can you explain it?
> >
> > —
> > You are receiving this because you modified the open/close state.
> > Reply to this email directly, view it on GitHub
> > <https://github.com/xmrig/xmrig/issues/1355#issuecomment-706727157>, or
> > unsubscribe
> > <https://github.com/notifications/unsubscribe-auth/AKV6LCZHO3DDBTGG47FSWLTSKHJZ5ANCNFSM4JTLUX5Q>
> > .
> >
> 

Already done many times ...1410mb to 10000mb but same showing not working
Showing ...failed with error DatasetHost::reg:50 "out of memory"..
My system windows 10 64b
Ram 4 gb
Processor Intel I3  6th gen
Graphic nvidia GeForce GT 710 2 gb ddr5..
My cpu given me max 700 H/s ...
But cuda gpu not working... 
Please help me.

## Yaaman42 | 2020-10-13T08:29:48+00:00
Oh, you might be out of video ram then. But I don't know what you could do
about that, other than getting another gpu with more ram on it.

On Tue, Oct 13, 2020, 10:15 Saikatsaha1996 <notifications@github.com> wrote:

> Windows system settings for virtual memory.
>
> On Sun, Oct 11, 2020, 18:06 Saikatsaha1996 notifications@github.com wrote:
>
> I got it working using a ridiculous amount of swap space.
>
> On Sun, Oct 11, 2020, 15:48 Saikatsaha1996 notifications@github.com wrote:
>
>    - CUDA 10.1/10.2/2.0.1-beta
>    - NVML 10.441.28/441.28 press e for health report
>    - CUDA GPU #0 01:00.0 GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61
>    mem:2482/3072 MB
>    - CUDA GPU #1 <https://github.com/xmrig/xmrig/issues/1> #1
>    <https://github.com/xmrig/xmrig/issues/1> #1
>    <https://github.com/xmrig/xmrig/issues/1>
>    #1 <https://github.com/xmrig/xmrig/issues/1> 04:00.0
>    GeForce GTX 1060 3GB 1771/4004 MHz smx:9 arch:61 mem:2482/3072 MB
>    [2019-12-01 21:13:44.508] net use pool xmr-eu1.nanopool.org:14433
>    TLSv1.2 79.137.82.5
>    [2019-12-01 21:13:44.511] net fingerprint (SHA-256):
>    "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
>    [2019-12-01 21:13:44.511] net new job from xmr-eu1.nanopool.org:14433
>    diff 480045 algo rx/0 height 1979413
>    [2019-12-01 21:13:44.512] rx init dataset algo rx/0 (2 threads) seed
>    993ba25f61d47e1e...
>    [2019-12-01 21:13:44.546] rx allocated 2336 MB (2080+256) huge pages
>    0% 0/1168 +JIT (34 ms)
>    [2019-12-01 21:13:54.463] net new job from xmr-eu1.nanopool.org:14433
>    diff 480045 algo rx/0 height 1979413
>    [2019-12-01 21:14:24.669] rx dataset ready (40113 ms)
>    [2019-12-01 21:14:24.670] cpu use profile rx (2 threads) scratchpad
>    2048 KB
>    [2019-12-01 21:14:24.758] nv use profile rx (2 threads) scratchpad
>    2048 KB
>    | # | GPU | BUS ID | I | T | B | BF | BS | MEM | NAME
>    | 0 | 0 | 01:00.0 | 576 | 32 | 18 | 6 | 25 | 1152 | GeForce GTX 1060
>    3GB
>    | 1 | 1 | 04:00.0 | 576 | 32 | 18 | 6 | 25 | 1152 | GeForce GTX 1060
>    3GB
>    [2019-12-01 21:14:24.846] cpu READY threads 2/2 (2) huge pages 0% 0/2
>    memory 4096 KB (176 ms)
>    [2019-12-01 21:14:38.963] nv READY threads 2/2 (14201 ms)
>    [2019-12-01 21:14:39.252] nv thread #1
>    <https://github.com/xmrig/xmrig/issues/1>
>    #1 <https://github.com/xmrig/xmrig/issues/1>
>    #1 <https://github.com/xmrig/xmrig/issues/1> #1
>    <https://github.com/xmrig/xmrig/issues/1> failed with error
>    DatasetHost::reg:50 "out of memory"
>    [2019-12-01 21:14:39.271] nv thread #0 failed with error
>    <randomx_prepare>:36 "invalid argument" "rx": [
>    {
>    "index": 0,
>    "threads": 32,
>    "blocks": 18,
>    "bfactor": 6,
>    "bsleep": 25,
>    "affinity": -1,
>    "dataset_host": true
>    },
>    {
>    "index": 1,
>    "threads": 32,
>    "blocks": 18,
>    "bfactor": 6,
>    "bsleep": 25,
>    "affinity": -1,
>    "dataset_host": true
>    }
>
> Your problem now solved ? Or not ? Because i got same problem..can you
> help me ?
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> #1355 <https://github.com/xmrig/xmrig/issues/1355> (comment)
> #1355 (comment)
> <https://github.com/xmrig/xmrig/issues/1355#issuecomment-706707481>, or
> unsubscribe
>
>
> https://github.com/notifications/unsubscribe-auth/AKV6LC4QEN5X5TNEVUBNE7DSKGZSXANCNFSM4JTLUX5Q
> .
>
> How can i swap space can you explain it?
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> #1355 (comment)
> <https://github.com/xmrig/xmrig/issues/1355#issuecomment-706727157>, or
> unsubscribe
>
> https://github.com/notifications/unsubscribe-auth/AKV6LCZHO3DDBTGG47FSWLTSKHJZ5ANCNFSM4JTLUX5Q
> .
>
> Already done many times ...1410mb to 10000mb but same showing not working
> Showing ...failed with error DatasetHost::reg:50 "out of memory"..
> My system windows 10 64b
> Ram 4 gb
> Processor Intel I3 6th gen
> Graphic nvidia GeForce GT 710 2 gb ddr5..
> My cpu given me max 700 H/s ...
> But cuda gpu not working...
> Please help me.
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1355#issuecomment-707573805>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AKV6LC727B5ALAJDVPEJIUDSKQEA7ANCNFSM4JTLUX5Q>
> .
>


## bessgeor | 2021-01-26T21:29:28+00:00
Same issue. CPU mining off, CUDA only. 2070s 8GB, page file 25000mb, 25Gb free RAM

## coltmerg420 | 2021-04-02T06:35:33+00:00
  "rx/arq": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 96,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }     this will fix it i can mine with my 2080 super now   complete config is

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
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": false,
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19]
        ],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "NVIDA",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": true,
        "loader": null,
        "nvml": true,
        "astrobwt": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 23,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn": [
            {
                "index": 0,
                "threads": 24,
                "blocks": 144,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 12,
                "blocks": 144,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 46,
                "blocks": 144,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 144,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 24,
                "blocks": 144,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 98304,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "rx": [
            {
                "index": 0,
                "threads": 24,
                "blocks": 96,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 96,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx/keva": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 96,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 96,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "???",
            "user": "???",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
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
        "enabled": true,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}

befor it was set to            {
                "index": 0,
                "threads": 70,
                "blocks": 96,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }   that mad it get no memory thing .

## ParGellen | 2022-04-04T12:56:27+00:00
I had the same problem when using the config file. If I launched XMRig with --cuda in the command line in Start.cmd everything worked fine. I fixed it for config.json launches by deleting everything under the "cuda" section in the config file except "enabled": true (don't forget the comma at the end after the word "true").
I don't know enough about it to know why this works but it did for me.


# Action History
- Created by: Yaaman42 | 2019-12-01T13:20:41+00:00
- Closed at: 2019-12-04T00:31:33+00:00
