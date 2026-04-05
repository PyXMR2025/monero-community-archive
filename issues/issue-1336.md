---
title: RandomX on 4GB cards - workaround
source_url: https://github.com/xmrig/xmrig/issues/1336
author: komatom
assignees: []
labels:
- randomx
created_at: '2019-11-30T11:49:16+00:00'
updated_at: '2021-04-12T15:17:57+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:17:57+00:00'
---

# Original Description
@xmrig @SChernykh 
After endless hours of making calculations with memory buffers and intensity to make 4GB cards work with randomx out of the box and set dataset_host when needed, I was forced to do the following in ocl_generic_rx_generator.cpp

```
constexpr const size_t OneMB = 1024u * 1024u;

const size_t mem = device.globalMemSize();
const size_t freeMem = device.freeMemSize();

bool datasetHost = false;

if (freeMem / OneMB < 4096) {
	datasetHost = true;
}

```

I guess we need more complex checks than original

`bool datasetHost = (mem < dataset_mem);`

what happens is even before starting the actual work threads xmrig allocates 2099MB of VRAM(on GPU-Z).. even though intensity is calculated something like 448 (448 * 2 *2 ) it's still doesn't fit in there rest of 4GB of ram with the above dataset. For example rig is with 8 cards and windows has taken just from the first GPU around 300MB, the other GPUs are with free memory. So the issue with this is only the calculations of buffers so it can set datasethost or keep it false.

If I don't set datasetHost = true, most of the GPUs just sit there with allocated 2099 of VRAM and does nothing - doesn't start the work threads.

That is a fix for me so I don't have to set different config files on every rig and allow the program when to enable or disable dataset_host.

So I would like us to discuss how to exactly calculate buffers for datasetHost to be accurate, so it works for other smaller VRAM cards as well in general.

Thanks

# Discussion History
## hawk-eye77 | 2019-12-01T18:19:09+00:00
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
[2019-12-01 21:14:39.271]  nv   thread #0 failed with error <randomx_prepare>:36 "invalid argument"

config.json:
        "rx": [
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

All my 1060 3gb rigs doesn't work...
1060 6 gb - one of four with small hashrate...

## sakorc | 2019-12-01T23:26:50+00:00
xmrig-5.0.0
Miner working with CPU and GPU , but 1 of 2 GPU card not working. Why ?

 * CUDA GPU     #0 01:00.0 GeForce GTX 1050 Ti 1417/3504 MHz smx:6 arch:61 mem:3
924/4096 MB
 * CUDA GPU     #1 02:00.0 GeForce GTX 1050 Ti 1417/3504 MHz smx:6 arch:61 mem:3
947/4096 MB

  nv   thread #1 failed with error <randomx_prepare>:39
 "out of memory"

 In config file 2 cards is same parameters

## SChernykh | 2019-12-01T23:38:09+00:00
One card is used by Windows for display output, so it has less available memory. Reduce "blocks" parameter for this card.

## sakorc | 2019-12-01T23:57:22+00:00
I removed from 18 to 2 blocks , both cards. The problem is the same.

EDIT:  reduced by 1 "bfactor"  now both cards work.

## komatom | 2019-12-02T15:38:24+00:00
About AMD RX580 cards with 4GB, even though I have enabled dataset_host in the code, all GPUs start mining however 90% of the time I get COMPUTE ERROR, so there is realy something messy with 2 threads on AMD cards. I just switched to 1 thread and  everything works like a charm, with the same performance - 8x RX580 4gb cards mine at ~ 3600h/s

```
uint32_t rxThreads = 1;
threads.add(OclThread(device.index(), intensity, 8, rxThreads, gcnAsm, datasetHost, 6));
```
before it was like this

`uint32_t rxThreads = (device.vendorId() == OCL_VENDOR_AMD)? 2 : 1;`

I have tried 2 threads with super small intensity.. so it is not only the limit of RAM, I think after all the looking, that there is a bug with 2 threads on GPUs:

1. On dataset_host = true, 2 threads, result: COMPUTE ERRORS, it was showing hashrate, but it never showed this on the pool, because no shares were accepted
2. On dataset_host = false, 2 threads, result: 1 or 2 of the cards mine. Others just allocate 2099MB of VRAM.
3. On dataset_host = false, 1 thread, result: Everything works


## SChernykh | 2019-12-02T15:53:46+00:00
Are your cards on risers? If you're getting compute errors with dataset on host it means your risers are not very reliable. RandomX pumps a lot of data through PCIe when dataset is on host.

## komatom | 2019-12-02T22:15:58+00:00
They are on risers yes, which might be true, however the actual issue is that we shouldn't set dataset_host = true at all and it still should work for 2 threads and intensity calculated.

I started digging into this when xmrig couln't start the work threads on several of the gpus(same model and batch), 1 or 2 cards start working, while other 6 cards just sitting there with N/A for hashrate and 2099MB allocated in VRAM. But they have all the necessary RAM for that.

So recently I see there is a problem with 2 work threads on these, since 1 thread no matter what the intensity, works perfectly fine.

## Zeushn | 2019-12-11T12:16:54+00:00
I had the same problem, increased the virtual memory in windows and problem solved. 

## Moschus88 | 2020-01-02T21:41:54+00:00
> I removed from 18 to 2 blocks , both cards. The problem is the same.
> 
> EDIT: reduced by 1 "bfactor" now both cards work.

Can you please show me your json config file ?
I have many troubles with all my 1060s cards.

## sakorc | 2020-01-03T06:09:51+00:00
 > Can you please show me your json config file ?
> I have many troubles with all my 1060s cards.

"out of memory" problem was with my pc RAM - was 4G. I upgraded my pc, now it is 16G and the problem is gone.

I am using a CPU i5 3.7 GHz 6 threads
Works 3 threads   "rx": [0, 1, 2]
2 GPU cards GeForce GTX 1050 Ti  4G
GPU you need to look at yourself better and play with "threads"and "blocks"
In my config 
"rx" -> "index": 0 -> "threads": 70 , "blocks": 12    
            "index": 1 -> "threads": 70 , "blocks": 12
I get about ~1900 h/s



# Action History
- Created by: komatom | 2019-11-30T11:49:16+00:00
- Closed at: 2021-04-12T15:17:57+00:00
