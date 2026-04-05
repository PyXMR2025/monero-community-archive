---
title: Nvidia GPU under utilized
source_url: https://github.com/xmrig/xmrig/issues/2242
author: davidshen84
assignees: []
labels: []
created_at: '2021-04-07T11:33:35+00:00'
updated_at: '2021-04-12T13:31:01+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:31:01+00:00'
---

# Original Description
**Describe the bug**
xmrig with cuda module cannot fully utilized Nvidia GPU power.

**To Reproduce**
1. Enable cuda module
2. Mine with GPU efficient algorithm, like *kawpow*

**Expected behavior**
GPU clock work at close to 100%

**Required data**
 - Miner log as text or screenshot

```
[2021-04-07 11:26:20.404]  net      new job from kawpow.usa-east.nicehash.com:3385 diff 80000K algo kawpow height 1700664
[2021-04-07 11:26:27.657]  net      new job from kawpow.usa-east.nicehash.com:3385 diff 80000K algo kawpow height 1700665
[2021-04-07 11:26:42.521]  nvidia   accepted (155/0) diff 80000K (243 ms)                                                
[2021-04-07 11:27:06.276]  nvidia   #0 01:00.0   0W 63C 999/3504 MHz                                                     
[2021-04-07 11:27:06.276]  miner    speed 10s/60s/15m 3.48 3.49 n/a MH/s max 5.25 MH/s                                   
[2021-04-07 11:27:08.013]  net      new job from kawpow.usa-east.nicehash.com:3385 diff 80000K algo kawpow height 1700666
[2021-04-07 11:27:34.541]  nvidia   accepted (156/0) diff 80000K (318 ms)                                                
[2021-04-07 11:27:58.708]  net      new job from kawpow.usa-east.nicehash.com:3385 diff 80000K algo kawpow height 1700666
[2021-04-07 11:28:00.494]  nvidia   accepted (157/0) diff 80000K (298 ms)                                                
[2021-04-07 11:28:03.214]  net      new job from kawpow.usa-east.nicehash.com:3385 diff 80000K algo kawpow height 1700666
```

 - Config file or command line (without wallets)

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
    "enabled": false,
    "huge-pages": false,
    "huge-pages-jit": false,
    "hw-aes": null,
    "priority": null,
    "memory-pool": false,
    "yield": true,
    "max-threads-hint": 100,
    "asm": true,
    "argon2-impl": null,
    "astrobwt-max-size": 550,
    "astrobwt-avx2": false,
    "kawpow": []
  },
  "opencl": {
    "enabled": false,
    "cache": true,
    "loader": null,
    "platform": "AMD",
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
        "blocks": 13,
        "bfactor": 0,
        "bsleep": 0,
        "affinity": -1,
        "dataset_host": false
      }
    ],
    "cn": [
      {
        "index": 0,
        "threads": 66,
        "blocks": 15,
        "bfactor": 0,
        "bsleep": 0,
        "affinity": -1,
        "dataset_host": false
      }
    ],
    "cn-heavy": [
      {
        "index": 0,
        "threads": 32,
        "blocks": 15,
        "bfactor": 0,
        "bsleep": 0,
        "affinity": -1,
        "dataset_host": false
      }
    ],
    "cn-lite": [
      {
        "index": 0,
        "threads": 128,
        "blocks": 15,
        "bfactor": 0,
        "bsleep": 0,
        "affinity": -1,
        "dataset_host": false
      }
    ],
    "cn-pico": [
      {
        "index": 0,
        "threads": 128,
        "blocks": 15,
        "bfactor": 0,
        "bsleep": 0,
        "affinity": -1,
        "dataset_host": false
      }
    ],
    "cn/2": [
      {
        "index": 0,
        "threads": 66,
        "blocks": 15,
        "bfactor": 0,
        "bsleep": 0,
        "affinity": -1,
        "dataset_host": false
      }
    ],
    "kawpow": [
      {
        "index": 0,
        "threads": 256,
        "blocks": 10240,
        "bfactor": 0,
        "bsleep": 0,
        "affinity": -1,
        "dataset_host": false
      }
    ],
    "rx": [
      {
        "index": 0,
        "threads": 32,
        "blocks": 10,
        "bfactor": 0,
        "bsleep": 0,
        "affinity": -1,
        "dataset_host": false
      }
    ],
    "cn/0": true,
    "cn-lite/0": []
  },
  "log-file": null,
  "donate-level": 1,
  "donate-over-proxy": 1,
  "pools": [
    {
      "algo": "kawpow",
      "coin": null,
      "url": "stratum+tcp://kawpow.usa-east.nicehash.com:3385",
      "user": "xmrig user",
      "pass": "x",
      "rig-id": null,
      "nicehash": true,
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
  "user-agent": null,
  "verbose": 9,
  "watch": true,
  "pause-on-battery": false,
  "pause-on-active": false
}
```

 - OS: Linux 5.10.27
 - For GPU related issues: information about GPUs and driver version.
   - Nvidia 460.39-r1
   - xmrig-cuda 6.5.0

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2021-04-07T11:37:16+00:00
XMRig doesn't set GPU core clock, you need to use 3rd-party software to change it. For example MSI Afterburner on Windows, not sure about Linux.

## Spudz76 | 2021-04-09T05:43:51+00:00
`nvidia-smi` will show current utilization and "P" mode

Anything Pascal or newer will force "P2" which usually is not the highest clocks ("P0").  Nvidia says this is so that when you're doing CUDA you don't get any erroneous calculation (slow and safe).  But mining doesn't care, we know if it's wrong - unlike image processing or other AI stuff where the correct answer isn't known / can't be rechecked.  So we want P0 or equivalent clocks at least, and probably can add a bit to that even.

With miner already running you can use `nvidia-settings` and crank up the clocks.  However since clocking works based on offsets, when you exit the miner the card briefly exits P2 and visits P0 (highest/gaming mode) on the way to P8 (sleep mode) and then it will probably crash hard / lockup.  Depends on what your card particular BIOS has for clocking, I have a few PNY which have P0+P2 on the same clocking so they have no problems (offset hits same clock either way).  Other MSI ones I have base clock very low in P2 so the offset is huge and P0 adds way too much clock.  There is a utility I built based on some sample code that didn't work without most of it updated, to open a CUDA session on the GPU and do a zero-work no-op loop to keep the card forced into P2 even if you start and stop other CUDA apps, which avoids the P0 blip and any crashing (but also the card will never P8 either while the forcer is running).  I may clean this code up and submit it as a utility in `xmrig/scripts/` with some sort of readme about all this

On windows there is a tool NvidiaProfileInspectorDmW which can flip a hidden setting in the Windows driver that disables the P2-lock feature, and then they run P0 just fine and you can set clock offsets and it doesn't crash.  Linux driver is internally completely missing this knob.  To clock in windows there is NvidiaInspector and it usually works better than Afterburner.

Also to use `nvidia-settings` you have to have Xorg installed, configured, and running (google: linux nvidia driver Xorg setup howto).  And to clock the card at all or set manual fans or etc you have to use `nvidia-settings` since `nvidia-smi` doesn't usually allow it except on actual compute series cards or GTX970 (application clocks, see `nvidia-smi --help`)

## Spudz76 | 2021-04-09T05:53:20+00:00
Also what model card is it, odd it doesn't show watts (some older ones don't).  Also curious if it does show watts in `nvidia-smi` output, maybe xmrig NVML code could be repaired.  Would be helpful to see the startup section output where it lists GPU detect info...

## davidshen84 | 2021-04-09T09:22:57+00:00
I am playing *xmrig* on my Dell XPS 15 2017 version...very old. It has a GTX 1050 mobile GPU. I build *xmrig* and *xmrig-cuda* myself using docker, then I use *nvidia-docker* to launch *xmrig* and mine with *kawpow*.

I cannot get the power usage even with `nvidia-smi`. Some people suggest it is because Nvidia does not support power management with this model.

From the `nvidia-smi` table, I can see the GPU is running in **P0** state.

What confuses me is this line.

> #0 01:00.0   0W 77C 1657/3504 MHz

It seems *xmrig* knows my GPU can work at *3504* MHz, but it is not able to utilize all the power. Maybe because there's not enough jobs or not enough memory?

# xmrig header
```
 * ABOUT        XMRig/6.11.1 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   disabled
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       1.1/31.1 GB (3%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+tcp://kawpow.usa-east.nicehash.com:3385 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * CUDA         11.2/11.2/6.5.0
 * NVML         11.460.39/460.39 press e for health report
 * CUDA GPU     #0 01:00.0 GeForce GTX 1050 1493/3504 MHz smx:5 arch:61 mem:3995/4042 MB
[2021-04-09 09:08:07.352]  net      use pool kawpow.usa-east.nicehash.com:3385  172.65.202.202
[2021-04-09 09:08:07.354]  net      new job from kawpow.usa-east.nicehash.com:3385 diff 363M algo kawpow height 1703404
[2021-04-09 09:08:07.354]  nvidia   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 01:00.0 |   2621440 |     256 |  10240 |  0 |   0 |   2840 | GeForce GTX 1050
[2021-04-09 09:08:07.509]  nvidia   READY threads 1/1 (155 ms)
[2021-04-09 09:08:12.009]  miner    KawPow light cache for epoch 227 calculated (4499ms)
```

# nvidia-smi
```
Fri Apr  9 19:10:55 2021
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.39       Driver Version: 460.39       CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 1050    Off  | 00000000:01:00.0 Off |                  N/A |
| N/A   61C    P0    N/A /  N/A |   2887MiB /  4042MiB |    100%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1834      C   ./xmrig                          2885MiB |
+-----------------------------------------------------------------------------+
```


## Spudz76 | 2021-04-10T01:31:21+00:00
That's `Coreclock/Memclock` not `current/max`

The one at the beginning in the detection line are the max `core/mem` clocks.

Fairly common for laptop models to be missing watts and fan.  Most share the main cooling fan so they don't have their own.

## davidshen84 | 2021-04-10T03:01:53+00:00
Ok... that sounds good.

On Sat, Apr 10, 2021, 11:31 Tony Butler ***@***.***> wrote:

> That's Coreclock/Memclock not current/max
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2242#issuecomment-817049552>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAAQBTMANUOHGLNGFCD2QRTTH6S7TANCNFSM42QTPJVQ>
> .
>


# Action History
- Created by: davidshen84 | 2021-04-07T11:33:35+00:00
- Closed at: 2021-04-12T13:31:01+00:00
