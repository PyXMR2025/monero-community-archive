---
title: 'read error:  "end of file"  (v6.16.1 - RTM)'
source_url: https://github.com/xmrig/xmrig/issues/2753
author: mynerzulu
assignees: []
labels: []
created_at: '2021-11-29T18:32:58+00:00'
updated_at: '2021-12-14T20:14:10+00:00'
type: issue
status: closed
closed_at: '2021-12-14T20:14:10+00:00'
---

# Original Description
**Describe the bug**
During active mining run, from time to time this error shows.

`stratum+tcp://raptorna.011data.com:3032 read error: "end of file"`

Will need to check if this happens on other pools. ( will test )


**To Reproduce**
normal execution of xmrig

**Expected behavior**
No error.    This seems to be happening on some of my computers that also see the "no active pools, stop mining" error.

**Required data**
```
[2021-11-29 18:11:47.623]  net      new job from raptorna.011data.com:3032 diff 1092K algo ghostrider height 195035
[2021-11-29 18:12:25.334]  net      stratum+tcp://raptorna.011data.com:3032 read error: "end of file"
[2021-11-29 18:12:25.334]  net      no active pools, stop mining
[2021-11-29 18:12:30.695]  net      use pool raptorna.011data.com:3032  66.228.57.126
[2021-11-29 18:12:30.695]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 195036
```
 - Config file or command line (without wallets)
sudo `screen -dmS RTM011data ./xmrig -a gr -o stratum+tcp://raptorna.011data.com:3032 -u <wallet.workername> -p x --cpu-max-threads-hint=80 --log-file=xmrig-log-txt`

miner startup:
```
 * ABOUT        XMRig/6.16.1 gcc/9.3.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU E5-1650 v2 @ 3.50GHz (1) 64-bit AES
                L2:1.5 MB L3:12.0 MB 6C/12T NUMA:1
 * MEMORY       0.6/15.6 GB (4%)
                DIMM1: 4 GB DDR3 @ 1866 MHz 0x45424A3430454738424657422D4A532D4620
                DIMM2: 4 GB DDR3 @ 1866 MHz 0x45424A3430454738424657422D4A532D4620
                DIMM3: 4 GB DDR3 @ 1866 MHz 0x45424A3430454738424657422D4A532D4620
                DIMM4: 4 GB DDR3 @ 1866 MHz 0x45424A3430454738424657422D4A532D4620
 * MOTHERBOARD  Apple Inc. - Mac-F60DEB81FF30ACF6
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+tcp://raptorna.011data.com:3032 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
```





 - OS: [e.g. Windows]
```
inxi -Ff
System:    Host: myner1 Kernel: 5.4.0-90-generic x86_64 bits: 64 Console: tty 0 
           Distro: Ubuntu 20.04.3 LTS (Focal Fossa) 
Machine:   Type: Unknown System: Apple product: MacPro6,1 v: 1.0 serial: <superuser/root required> 
           Mobo: Apple model: Mac-F60DEB81FF30ACF6 v: MacPro6,1 serial: <superuser/root required> UEFI: Apple 
           v: 429.40.7.0.1 date: 09/16/2021 
CPU:       Topology: 6-Core model: Intel Xeon E5-1650 v2 bits: 64 type: MT MCP L2 cache: 12.0 MiB 
           Speed: 3600 MHz min/max: 1200/3900 MHz Core speeds (MHz): 1: 3600 2: 3600 3: 3600 4: 3600 5: 3600 6: 3600 
           7: 3600 8: 3600 9: 3600 10: 3600 11: 3600 12: 3600 
           Flags: acpi aes aperfmperf apic arat arch_perfmon avx bts clflush cmov constant_tsc cpuid cpuid_fault 
           cx16 cx8 dca de ds_cpl dtes64 dtherm dts epb ept erms est f16c flexpriority flush_l1d fpu fsgsbase fxsr 
           ht ibpb ibrs ida lahf_lm lm mca mce md_clear mmx monitor msr mtrr nonstop_tsc nopl nx pae pat pbe pcid 
           pclmulqdq pdcm pdpe1gb pebs pge pln pni popcnt pse pse36 pti pts rdrand rdtscp rep_good sep smep smx ss 
           ssbd sse sse2 sse4_1 sse4_2 ssse3 stibp syscall tm tm2 tpr_shadow tsc tsc_deadline_timer vme vmx vnmi 
           vpid x2apic xsave xsaveopt xtopology xtpr 
Graphics:  Device-1: Advanced Micro Devices [AMD/ATI] Tahiti LE [Radeon HD 7870 XT] driver: radeon v: kernel 
           Device-2: Advanced Micro Devices [AMD/ATI] Tahiti LE [Radeon HD 7870 XT] driver: radeon v: kernel 
           Display: server: No display server data found. Headless machine? tty: 120x42 
           Message: Advanced graphics data unavailable in console. Try -G --display 
Audio:     Device-1: Intel C600/X79 series High Definition Audio driver: snd_hda_intel 
           Device-2: Advanced Micro Devices [AMD/ATI] Tahiti HDMI Audio [Radeon HD 7870 XT / 7950/7970] 
           driver: snd_hda_intel 
           Device-3: Advanced Micro Devices [AMD/ATI] Tahiti HDMI Audio [Radeon HD 7870 XT / 7950/7970] 
           driver: snd_hda_intel 
           Sound Server: ALSA v: k5.4.0-90-generic 
Network:   Device-1: Broadcom and subsidiaries NetXtreme BCM57762 Gigabit Ethernet PCIe driver: tg3 
Drives:    Local Storage: total: 466.65 GiB used: 7.79 GiB (1.7%) 
           ID-1: /dev/sda type: USB model: 1JMicron Generic size: 232.89 GiB 
           ID-2: /dev/sdb vendor: Apple model: SSD SM0256F size: 233.76 GiB 
Partition: ID-1: / size: 113.37 GiB used: 7.68 GiB (6.8%) fs: ext4 dev: /dev/dm-0 
           ID-2: /boot size: 975.9 MiB used: 107.0 MiB (11.0%) fs: ext4 dev: /dev/sda2 
Sensors:   System Temperatures: cpu: 65.0 C mobo: N/A 
           Fan Speeds (RPM): N/A 
           GPU: device: radeon temp: 55 C device: radeon temp: 56 C 
Info:      Processes: 212 Uptime: 33m Memory: 15.61 GiB used: 452.4 MiB (2.8%) Init: systemd runlevel: 5 Shell: bash 
           inxi: 3.0.38 

 
```





**Additional context**
Add any other context about the problem here.


# Discussion History
## Lonnegan | 2021-11-29T18:35:40+00:00
Just
-o raptorna.011data.com:3032

not

-o stratum+tcp://raptorna.011data.com:3032

## SChernykh | 2021-11-29T18:36:27+00:00
`diff 1092K`
You have very high difficulty and don't send shares for a while, this is why pool disconnects.

## mynerzulu | 2021-11-29T18:44:25+00:00
@Lonnegan
Trying your recommendation...

(FYI - I have 4 four computers running for a few days now with this.  submitting and payout are happening.  
Changing one to without 'stratum+tcp'  ( this was needed in the config file.))

## mynerzulu | 2021-11-29T19:20:01+00:00
Update: 

```
[2021-11-29 19:02:37.532]  miner    speed 10s/60s/15m 193.5 197.2 197.5 H/s max 738.7 H/s avg 202.6 H/s
[2021-11-29 19:03:24.112]  net      new job from raptorna.011data.com:3032 diff 280422 algo ghostrider height 195057
[2021-11-29 19:03:37.589]  miner    speed 10s/60s/15m 194.3 197.5 197.7 H/s max 738.7 H/s avg 202.4 H/s
[2021-11-29 19:04:19.299]  net      new job from raptorna.011data.com:3032 diff 280422 algo ghostrider height 195057
[2021-11-29 19:04:37.647]  miner    speed 10s/60s/15m 194.3 197.9 197.5 H/s max 738.7 H/s avg 202.2 H/s
[2021-11-29 19:05:14.416]  net      new job from raptorna.011data.com:3032 diff 280422 algo ghostrider height 195057
[2021-11-29 19:05:37.708]  miner    speed 10s/60s/15m 194.3 194.6 197.3 H/s max 738.7 H/s avg 201.8 H/s
[2021-11-29 19:06:09.539]  net      new job from raptorna.011data.com:3032 diff 280422 algo ghostrider height 195057
[2021-11-29 19:06:37.769]  miner    speed 10s/60s/15m 197.7 197.3 197.3 H/s max 738.7 H/s avg 201.7 H/s
[2021-11-29 19:07:04.614]  net      new job from raptorna.011data.com:3032 diff 280422 algo ghostrider height 195057
[2021-11-29 19:07:37.808]  miner    speed 10s/60s/15m 205.4 199.5 197.3 H/s max 738.7 H/s avg 201.6 H/s
[2021-11-29 19:07:59.732]  net      new job from raptorna.011data.com:3032 diff 280422 algo ghostrider height 195057
[2021-11-29 19:08:37.845]  miner    speed 10s/60s/15m 196.9 196.5 197.4 H/s max 738.7 H/s avg 201.4 H/s
[2021-11-29 19:08:54.856]  net      new job from raptorna.011data.com:3032 diff 280422 algo ghostrider height 195057
[2021-11-29 19:09:37.882]  miner    speed 10s/60s/15m 196.9 198.9 197.5 H/s max 738.7 H/s avg 201.3 H/s
[2021-11-29 19:09:50.011]  net      new job from raptorna.011data.com:3032 diff 280422 algo ghostrider height 195057
[2021-11-29 19:10:37.918]  miner    speed 10s/60s/15m 196.9 197.7 197.6 H/s max 738.7 H/s avg 201.2 H/s
[2021-11-29 19:10:45.128]  net      new job from raptorna.011data.com:3032 diff 280422 algo ghostrider height 195057
[2021-11-29 19:11:37.958]  miner    speed 10s/60s/15m 195.2 197.4 197.6 H/s max 738.7 H/s avg 201.0 H/s
[2021-11-29 19:11:40.208]  net      new job from raptorna.011data.com:3032 diff 280422 algo ghostrider height 195057

[2021-11-29 19:12:35.373]  net      raptorna.011data.com:3032 read error: "end of file"
[2021-11-29 19:12:35.373]  net      no active pools, stop mining

[2021-11-29 19:12:37.992]  miner    speed 10s/60s/15m 145.6 188.9 197.0 H/s max 738.7 H/s avg 200.7 H/s
[2021-11-29 19:12:41.063]  net      use pool raptorna.011data.com:3032  66.228.57.126
[2021-11-29 19:12:41.063]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 195057
[2021-11-29 19:12:58.083]  cpu      accepted (10/0) diff 16384 (81 ms)
[2021-11-29 19:13:06.460]  net      new job from raptorna.011data.com:3032 diff 16384 algo ghostrider height 195058
[2021-11-29 19:13:06.485]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2021-11-29 19:13:06.485]  cpu      GhostRider algo 2: cn/turtle-lite (128 KB)
[2021-11-29 19:13:06.485]  cpu      GhostRider algo 3: cn/dark-lite (256 KB)
[2021-11-29 19:13:14.590]  cpu      accepted (11/0) diff 16384 (95 ms)
[2021-11-29 19:13:15.520]  net      new job from raptorna.011data.com:3032 diff 307200 algo ghostrider height 195059
[2021-11-29 19:13:15.525]  cpu      GhostRider algo 1: cn/dark-lite (256 KB)
[2021-11-29 19:13:15.525]  cpu      GhostRider algo 2: cn/dark (512 KB)
[2021-11-29 19:13:15.525]  cpu      GhostRider algo 3: cn/turtle-lite (128 KB)
[2021-11-29 19:13:38.041]  miner    speed 10s/60s/15m 1904.7 943.2 246.3 H/s max 1908.1 H/s avg 223.6 H/s
```

Running with:
`sudo screen -dmS RTM011data ./xmrig -a gr -o raptorna.011data.com:3032 -u <wallet.worker> -p x --cpu-max-threads-hint=80 --log-file=xmrig-log-txt`














## Lonnegan | 2021-11-29T21:42:09+00:00
As @SChernykh has said already: that pool give you jobs with much too high difficulty. Look at the log! You get new jobs, and new jobs, and new jobs.... but your system doesn't manage to send a result back. So the pool disconnects you after a while. Either choose a port with lower difficulty, configure a fixed difficulty as long as the pool supports it or choose an other pool with better difficulty calculation.

## mynerzulu | 2021-11-30T00:17:28+00:00
Thanks @Lonnegan 
 Since I am new to this arena (mining), I am not aware yet of what is acceptable or possible. 
- What is acceptable ranges for difficulty ?  ( will try some other pools )
- Why would pools issue high difficulty jobs ?  ( I have not been happy with 011data performance )
- I will do some research to see if the pool accepts defined difficulty numbers.  How does this affect, impact hash rate or coin generation velocity ?

regards,


## Spudz76 | 2021-11-30T00:49:56+00:00
Difficulty always 30 times your average hashrate.  This should result in one accept every ~30 seconds.

The most recent paste, it had given you a nice low 16K diff which is also when you show accepts.  But then it changed it up to 307200 which is too high again.  Their autodiff technique is pretty broken.  If they do have a way to set a diff, that would work best.

Note once the miner saves a config.json the command line is mostly ignored.

## NVMDSTEVil | 2021-11-30T04:18:51+00:00
You are connecting to the wrong port, that is why you are getting such difficult jobs.  3008 is usually the port most people are supposed to use for mining.  3004 is for very weak devices such as Intel cpu's and 3032/3256 are for large miners.

## mynerzulu | 2021-11-30T04:32:56+00:00

Good info, thanks @NVMDSTEVil.   I saw the ports listed on 011data, they did not specify why which port needs to be used and determination of choice.  I will adjust and see outcome.

@Spudz76 - I did notice that since this 6.16.x version, the config.json does not get generated anymore.   With the new version I did generate a config file with the web wizzard.   ( you cannot choose 'gr' / RTM ) so I updated that manually after downloading it.   This produced an error, that is why I started using full command line. 
== I will try it again tonight.
 thanks!

## mynerzulu | 2021-11-30T07:13:32+00:00

Tried minafacil pool with d=0.8

![xmrig-6 16 1-minafacil-pool_2021-11-29_23-21-26](https://user-images.githubusercontent.com/95162025/144001247-c3c881a7-e73c-4e67-8a95-41e6e704d6e1.png)


Went back to 011data pool with port 3008.  over time the diff creeps up to 500k region.

![xmrig6 16 1-011data-diff_2021-11-30_01-07-10](https://user-images.githubusercontent.com/95162025/144001582-2d5da8fa-b612-44d2-88b0-c276ece3bc3d.png)

![xmrig6 16 1-011data_2021-11-30_00-04-11](https://user-images.githubusercontent.com/95162025/144001904-309bb9a5-043f-47d8-9b6a-b3b3ad324cf7.png)

If this is normal - no issues then.  Wanted to report the behavior.

This is not the original issue "end of file" and I have not seen that again.  ( can open new threads for other observations )

regards,





## NVMDSTEVil | 2021-11-30T07:43:06+00:00
Most pools auto-balance you somewhat which is why you see the rise in difficulty over time.

There have been a few users mentioning issues with 011 pool in the RTM discord over the last 6 hours so i'm wondering if they're getting a bit overloaded with users or something as well.

# Action History
- Created by: mynerzulu | 2021-11-29T18:32:58+00:00
- Closed at: 2021-12-14T20:14:10+00:00
