---
title: --threads=20 initialy honoured, but reverts to lower threads after about 1
  minute
source_url: https://github.com/xmrig/xmrig/issues/3251
author: LexxM3
assignees: []
labels: []
created_at: '2023-04-17T00:10:14+00:00'
updated_at: '2025-06-18T22:42:13+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:42:13+00:00'
---

# Original Description
**Describe the bug**
--threads=20 initially utilizes all cores (14) and all threads (20) as specified, but after about 1 minute, reverts to only running on the 8 high efficiency cores.

**To Reproduce**
Behaviour exhibits both during normal mining and benchmarking.

**Expected behavior**
With only 8 cores running, hash rate is about 3kH/s.  With all 14 cores running, hash rate is about 5kH/s.  One would like the maximum possible hash rate, hence the issue.

**Required data**
 - Miner start status: see attached, xmrig-6.19.2
 - command line: xmrig.exe -o xmr.2miners.com:2222 -u wallet.rig_id -p x
 - config file: default as downloaded
 - OS: Windows 11 Pro, Version: 22H2, OS Build: 22621.1555, Experience: Windows Feature Experience Pack 1000.22640.1000.0
 - CPU: Intel i9-12900HK

**Additional context**
See attached Task Manager screen cap demonstrating this behaviour.  When --threads=20 is omitted, miner defaults to just the 8 efficiency cores right from the start and hash rate is 3kH/s.

![Screenshot 2023-04-16 19 58 10](https://user-images.githubusercontent.com/55937877/232351208-dba333c4-f9d6-4dd6-8976-9c10365c6bbb.png)

![Screenshot 2023-04-16 19 37 01](https://user-images.githubusercontent.com/55937877/232351211-7a5d4f65-95e4-43b7-bf4a-ecf97c9092a7.png)


# Discussion History
## xmrig | 2023-04-17T05:51:40+00:00
Please share `topology.xml` obtained by command `xmrig.exe --export-topology`. It will allow me to simulate auto config on your CPU without physical access to it.


`--threads` option not supposed to work well on any complex CPU, because OS can migrate threads by any way including aggressive power optimizations.
Thank you.

## SChernykh | 2023-04-17T07:42:57+00:00
> but after about 1 minute, reverts to only running on the 8 high efficiency cores.

This is Windows doing "optimizations". `--threads` doesn't set affinity, so Windows can move threads to other cores, in this case it decided to move "long running task" (XMRig) to efficiency cores.

The proper way is to set threads in config.json - then XMRig will set affinity, and Windows shouldn't be able to move them.

## LexxM3 | 2023-04-17T18:54:02+00:00
> Please share `topology.xml` obtained by command `xmrig.exe --export-topology`. It will allow me to simulate auto config on your CPU without physical access to it.

Attached is the requested topology.xml file (rename .TXT to .XML as Github doesn't allow .XML attachments, duh).  Only change in the file is redacted machine name.  One other change in the setup is that I've since restored Win11 WIndows Security Memory Integrity protection and, thus, prevented the ability of the miner to apply the MSR MOD -- I feel more comfortable with that protection on and MSR MOD appears to make no difference in this setup, at least not at the current configuration state (interestingly, Win10 does not require similar modification to enable MSR MOD, only Win11).

One other new observation: I also have a nearly identical machine to this one with ONLY difference is that it's an i7-12700H -- it does NOT have this problem and seems to make good use of the processors (identical assortment of cores as i9-12900HK) and, in fact, mines above 5kH/s without any finagling in spite of being a slightly lower end processor.  Identical Win11 Pro versions on that one as well and identical mobo and memory config.

[topology.txt](https://github.com/xmrig/xmrig/files/11254805/topology.txt)


## LexxM3 | 2023-04-17T18:58:46+00:00
> > but after about 1 minute, reverts to only running on the 8 high efficiency cores.
> 
> This is Windows doing "optimizations". `--threads` doesn't set affinity, so Windows can move threads to other cores, in this case it decided to move "long running task" (XMRig) to efficiency cores.
> 
> The proper way is to set threads in config.json - then XMRig will set affinity, and Windows shouldn't be able to move them.

Interesting observation that rings as likely valid.  Per above follow-up, interestingly an otherwise-completely-identical i7-12700H machine does NOT have the same problem under Win11 Pro.

Can you suggest a snippet of config.json change that would potentially accomplish better control per your note?

## xmrig | 2023-04-18T14:10:58+00:00
Currently auto config generates 14 threads and looks like `"rx": [0, 2, 4, 6, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19],` this is not optimal as it uses only physical cores.

Correct configuration should be like `"rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16],` which fully uses all performance cores and optimally uses 2 efficient cores since they do not have enough cache. This config is also 14 threads.

If you like try use all 20 threads, it will be like: `"rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],`

## LexxM3 | 2023-04-18T14:47:59+00:00
> Currently auto config generates 14 threads and looks like `"rx": [0, 2, 4, 6, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19],` this is not optimal as it uses only physical cores.
> 
> Correct configuration should be like `"rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16],` which fully uses all performance cores and optimally uses 2 efficient cores since they do not have enough cache. This config is also 14 threads.
> 
> If you like try use all 20 threads, it will be like: `"rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],`

Thanks.  I figured you would recommend an "rx" section.  There is currently no "rx" keyword or section anywhere in config.json and the Wizard doesn't generate one either.  Do I just add the "rx" config above at the bottom of the cpu section?

## SChernykh | 2023-04-18T15:01:56+00:00
Just run XMRig with config.json generated by the Wizard, and XMRig will create this section. Then you can edit it.

## LexxM3 | 2023-04-18T15:08:54+00:00
> Just run XMRig with config.json generated by the Wizard, and XMRig will create this section. Then you can edit it.

I've run xmrig many times now, it has never generated that keyword anywhere in config.json (I've been researching "rx" before your note as well). When I manually add that keyword and configure array to cpu section, I can see it is being interpreted as the initial status changes, but neither the "right 14 thread" nor the "20 thread" config has made any hash rate difference after a minute of running -- still running about 3kH/S on the 12900HK.

## SChernykh | 2023-04-18T16:02:24+00:00
> I've run xmrig many times now

You have to run it without command line parameters, or it will ignore config.json

## LexxM3 | 2023-04-19T05:58:50+00:00
> You have to run it without command line parameters, or it will ignore config.json

Ok, thanks!!! config.json now makes sense!  Here is what I observe now, running xmrig fully off the config.json file with no command line parameters:

`"rx": [0, 2, 4, 6, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19]`: this is the default, runs 100% of all 8 efficiency cores, 20% of 6 performance core threads, and idle on the remaining 6 performance core threads (so while it's supposed to be a 14 thread config, it is actually only 8ish). Hash rate about 3kH/s

`"rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16]`: suggested better 14 thread config, it utilizes as states: 50% of each of the 12 performance cores threads and 100% of 2 efficiency cores, leaving remaining 6 efficiency cores at idle.  Hash rate drops to about 2.3kH/s (!!!)

`"rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]`: suggested all 20 thread config, it utilizes 100% of 8 efficiency cores and interestingly exactly 20% of each of the 12 performance cores threads.  Hash rate around 2.8kH/s

So clearly the config has impact, but not entirely as expected and have yet succeeding utilizing all 20 threads.

P.S. Also tried `"rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]` with command line solely `--threads=20` -- exactly the same CPU utility as without `--threads=20` (20% on each of 12 performance cores threads, 100% on each of 8 efficiency cores, 2.8kH/s).

Edit: slightly more precise description of observed utilization, but unlikely to be material relative to pre-edit.

## SChernykh | 2023-04-19T06:03:02+00:00
Something is wrong with your setup. Suggested 20 thread config should utilize 100% of all cores, and you're not getting it for some reason. Suggested 14 thread config should utilize 100% of all P-cores, and you're not getting it as well.

## LexxM3 | 2023-04-19T06:22:06+00:00
Hm.  Win11 might be "too smart" for xmrig.  I'll try same machine under Win10 Pro and then under Linux as I get a chance to set it up.  In the meantime, all further ideas welcome.

## SChernykh | 2023-04-19T07:28:54+00:00
You can try to turn off virtualization and memory integrity first: https://www.tomshardware.com/how-to/disable-vbs-windows-11

## LexxM3 | 2023-07-16T00:12:01+00:00
It's been a little while, but I finally got a chance to test the same machine in this discussion but now under Windows 10.  The behaviour where performance cores turn off after a minute of XMrig run time and half the hashrate that happens under Windows 11, DOES NOT occur under Windows 10.  I can also add that, so far, neither XMRig version nor cores configuration nor threads configuration of XMrig makes any difference to this behaviour under Win 11.  Now that the difference has been narrowed down to Win 11 vs Win 10, I can try a few more things under Win 11 to help narrow down further.

## Spudz76 | 2023-07-16T19:17:01+00:00
`--threads` creates a `"*"` profile which will override the `"rx"` section if any because it's a wildcard.  If you want the `"rx"` profile to work you must manually remove the `"*"` profile and stop using `--threads`

## trabanom | 2024-02-24T12:21:38+00:00
I get more hashes after stop using --threads=21 and started to use --cpu-max-threads-hint=89 (89% of my CPU) on my ryzen 9 5900x. 

# Action History
- Created by: LexxM3 | 2023-04-17T00:10:14+00:00
- Closed at: 2025-06-18T22:42:13+00:00
