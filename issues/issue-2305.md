---
title: failed to start WinRing0 driver, error 395
source_url: https://github.com/xmrig/xmrig/issues/2305
author: Dark-Hunter540
assignees: []
labels: []
created_at: '2021-04-23T22:44:40+00:00'
updated_at: '2023-01-16T22:15:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Here are my logs:
![image](https://user-images.githubusercontent.com/10456133/115936646-ba6d4780-a48d-11eb-9b23-4dca0c0d044d.png)

I cannot manage to get MSR mod to work. Are these related?


# Discussion History
## Spudz76 | 2021-04-24T06:42:58+00:00
Yes, on Windows it must load the Ring0 driver in order to access CPU MSRs.  Unable to load driver leads directly to not being able to change MSRs.  You must have Secure Boot disabled or MSRs are forever locked.  Could also be something with virus protection not allowing "unknown" vxd's to load.  The VXD file should be in the same folder as the `xmrig.exe` and is called `WinRing0x64.sys`.

Another method is to load Open Hardware Monitor which installs its own MSR driver, but if that works then xmrig will use it (with a complaint there is already some other Ring0 driver, but it uses it fine).  Perhaps OHM installer is smarter about whitelisting its VXD.  Or, if it also doesn't work then it's Secure Boot or some other security junk blocking it.

## Dark-Hunter540 | 2021-04-24T13:53:26+00:00
> Yes, on Windows it must load the Ring0 driver in order to access CPU MSRs. Unable to load driver leads directly to not being able to change MSRs. You must have Secure Boot disabled or MSRs are forever locked. Could also be something with virus protection not allowing "unknown" vxd's to load. The VXD file should be in the same folder as the `xmrig.exe` and is called `WinRing0x64.sys`.
> 
> Another method is to load Open Hardware Monitor which installs its own MSR driver, but if that works then xmrig will use it (with a complaint there is already some other Ring0 driver, but it uses it fine). Perhaps OHM installer is smarter about whitelisting its VXD. Or, if it also doesn't work then it's Secure Boot or some other security junk blocking it.

Thank you, it works now. However I am still getting around 4950H/s. Here is what it says now. 
![image](https://user-images.githubusercontent.com/10456133/115961014-6eadb300-a50c-11eb-979b-d042553c3217.png)
Looking at RandomX benchmarks it says I should expect around 12000H/s+. Anything you guys can think of that would be stopping this?


## clflush | 2021-04-24T14:01:05+00:00
what the benchmark didnt capture is the overclocking part. In your case, likely need to overclock and undervolt the CPU, and adjust the DRAM timing. 

## Dark-Hunter540 | 2021-04-24T14:03:30+00:00
> what the benchmark didnt capture is the overclocking part. In your case, likely need to overclock and undervolt the CPU, and adjust the DRAM timing.

Hi, I have overclocked and undervolted my cpu using PBO2. It regularly boosts over 5GHz. I will overclock my RAM too and get back to you.

## SChernykh | 2021-04-24T14:08:39+00:00
You're still running only 6 threads on 5800X, it should be 16 threads on this CPU. Use xmrig.com/wizard to create new config.

## Dark-Hunter540 | 2021-04-24T15:24:24+00:00
> You're still running only 6 threads on 5800X, it should be 16 threads on this CPU. Use xmrig.com/wizard to create new config.

That helped thanks. Creating a new config file has boosted my hashrate to about 8300H/s. I also overclocked my RAM to 3800Mhz. Any ideas on what is preventing it from reaching 12kH/s+? Many thanks so far.
![image](https://user-images.githubusercontent.com/10456133/115963896-85a6d200-a519-11eb-8c97-53491492c890.png)


## SChernykh | 2021-04-24T15:29:18+00:00
> Any ideas on what is preventing it from reaching 12kH/s+?

Maybe other programs running and using CPU. Try setting high performance mode in power options, also go through https://xmrig.com/docs/miner/randomx-optimization-guide/ (Windows 10 tuning guide there).

## Dark-Hunter540 | 2021-04-24T16:27:24+00:00
> > Any ideas on what is preventing it from reaching 12kH/s+?
> 
> Maybe other programs running and using CPU. Try setting high performance mode in power options, also go through https://xmrig.com/docs/miner/randomx-optimization-guide/ (Windows 10 tuning guide there).

Hi again,

I carried out the optimisations mentioned. I then proceeded to run the benchmark.
My results are:
https://xmrig.com/benchmark/j2E3s
https://xmrig.com/benchmark/6yGPi
Any tips to improve this?
Thanks

## RaptorBlue428 | 2023-01-16T22:10:38+00:00
i have a cannot set msr error and service msr already exists error i have load hardware moniotr

## RaptorBlue428 | 2023-01-16T22:15:34+00:00
so help me god

# Action History
- Created by: Dark-Hunter540 | 2021-04-23T22:44:40+00:00
