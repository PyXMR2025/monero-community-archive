---
title: WinRing0 errorcode 183
source_url: https://github.com/xmrig/xmrig/issues/2475
author: blade198222
assignees: []
labels: []
created_at: '2021-07-06T08:08:04+00:00'
updated_at: '2025-06-20T11:11:45+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:11:44+00:00'
---

# Original Description
Possible bug:
Error Output on CMD
"failed to start WinRing0 driver, error 183"
"FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW"

To Reproduce:
Using Windows 10 x64 21H1 and XMRig 6.13.1 with admin rights

Expected behavior:
- A few days ago this error did not exist. Reduction of the hash performance from 9200 to 7600
- In the meantime, no further software has been changed, installed or uninstalled
- The error does not occur under Ubuntu 20.04.2 on the same hardware with the same BIOS settings.
Here the hash performance is pinned at 9,200
- Error code for WinRing0 driver 183 seems rare or new. Couldn't find any more information on this.

Required data
<img width="673" alt="XMrig Error" src="https://user-images.githubusercontent.com/43348259/124564127-07cc4480-de41-11eb-9466-d8acd18eeea8.png">

config.json
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
        "enabled": true,
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn": [
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
            [1, 15]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14]
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
            [1, 15]
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
            [2, 15]
        ],
        "cn/upx2": [
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
            [2, 15]
        ],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 5,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.minexmr.com:443",
            "user": "shortened",
            "pass": null,
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
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}

Hopefully someone can do something with the error, doesn't want to rule out that I am responsible for the problem myself ;)

Thx Blade



# Discussion History
## SChernykh | 2021-07-06T09:00:49+00:00
Do you have Open Hardware Monitor installed? If so, try to reinstall it and reboot.

## blade198222 | 2021-07-06T09:09:43+00:00
Thanks for the answer.
I've heard of the software, but I've never installed it.
Monitor tools that were installed long before the problem occurred are:
- HWMonitor
- MSI Afterburner

## SChernykh | 2021-07-06T09:15:25+00:00
Try to reinstall HWMonitor then.

## blade198222 | 2021-07-06T09:31:06+00:00
Thank you for your prompt reply.

Found the problem. It was the program "Aquasuite" from Aquacomputer. A software to configure the monitoring of water cooling. The software has been installed for a long time, the latest version may have caused a problem.

## SkyportDEV | 2021-07-14T16:27:48+00:00
Disable the Aqua Computer Service will solve this issue. You do not need this service. After disabling it, you will not be able to switch the cooling profile if the software is closed

## danielsouza | 2021-11-04T23:48:04+00:00
I had this problem too, I fixed applying the following instructions [here](https://gitmemory.com/issue/nicehash/NiceHashMiner/2537/960303419)

**_When ENABLED under Advanced -> Disable Device Status Monitoring and restarting NiceHashMiner fixes it (running as admin) but of course no temperatures are shown._**

## Spudz76 | 2021-11-05T01:03:10+00:00
If the NiceHashMiner people used OpenHardwareMonitor for its status monitoring, it would still work.

## MrStark21 | 2021-11-05T11:43:32+00:00
I have the same issue
I have tried everything I could
Still nothing changed
I have VM(Virtual Machine) installed
Does it has anything to do with it
pls help


## mikemcv879nz | 2021-11-08T08:25:10+00:00
> I had this problem too, I fixed applying the following instructions [here](https://gitmemory.com/issue/nicehash/NiceHashMiner/2537/960303419)
> 
> **_When ENABLED under Advanced -> Disable Device Status Monitoring and restarting NiceHashMiner fixes it (running as admin) but of course no temperatures are shown._**

this worked for me its in settings-advanced nicehash not sure about xmrig itself, thanks bro

## aalencia | 2021-11-18T10:08:55+00:00
> > I had this problem too, I fixed applying the following instructions [here](https://gitmemory.com/issue/nicehash/NiceHashMiner/2537/960303419)
> > **_When ENABLED under Advanced -> Disable Device Status Monitoring and restarting NiceHashMiner fixes it (running as admin) but of course no temperatures are shown._**
> 
> this worked for me its in settings-advanced nicehash not sure about xmrig itself, thanks bro

While this also worked for me, now I cannot see my temps etc in the dashboard..  this is not a fix.

## mikemcv879nz | 2021-11-18T10:48:50+00:00
> > > I had this problem too, I fixed applying the following instructions [here](https://gitmemory.com/issue/nicehash/NiceHashMiner/2537/960303419)
> > > **_When ENABLED under Advanced -> Disable Device Status Monitoring and restarting NiceHashMiner fixes it (running as admin) but of course no temperatures are shown._**
> > 
> > 
> > this worked for me its in settings-advanced nicehash not sure about xmrig itself, thanks bro
> 
> While this also worked for me, now I cannot see my temps etc in the dashboard.. this is not a fix.

yes temps aren't visable but after starting xmrig you can enable again and temps become visable again make sure to start xmrig first annoying to have to do this every restart so i downloaded it separately and used nicehash stratum sever and xmrig wizard to do a work around everything still shows up in nicehash website except mbtc but a dollar amout per day i think you may earn a few cents more ive also switch my gpus but still use nicehash also desktop app you can still use to monitor temps 

## mikemcv879nz | 2021-12-01T11:14:34+00:00
> > > > I had this problem too, I fixed applying the following instructions [here](https://gitmemory.com/issue/nicehash/NiceHashMiner/2537/960303419)
> > > > **_When ENABLED under Advanced -> Disable Device Status Monitoring and restarting NiceHashMiner fixes it (running as admin) but of course no temperatures are shown._**
> > > 
> > > 
> > > this worked for me its in settings-advanced nicehash not sure about xmrig itself, thanks bro
> > 
> > 
> > While this also worked for me, now I cannot see my temps etc in the dashboard.. this is not a fix.
> 
> yes temps aren't visable but after starting xmrig you can enable again and temps become visable again make sure to start xmrig first annoying to have to do this every restart so i downloaded it separately and used nicehash stratum sever and xmrig wizard to do a work around everything still shows up in nicehash website except mbtc but a dollar amout per day i think you may earn a few cents more ive also switch my gpus but still use nicehash also desktop app you can still use to monitor temps

just as a sidenote i found argus monitor free version for monitoring temps and it has fan control and other features including a widget very nice software has alarms etc for overheat  link:https://www.softlay.com/downloads/argus-monitor

## GOLDDUBBY | 2021-12-03T11:35:08+00:00
Bug has returned. 

Got the error after enabling (not disable) the Power setting under advance settings. 

Tried turning it off, but the bug is stuck.

## mikemcv879nz | 2021-12-03T11:43:38+00:00
> Bug has returned.
> 
> Got the error after enabling (not disable) the Power setting under advance settings.
> 
> Tried turning it off, but the bug is stuck.

so i think you would have to undo that option and restart nicehash cos they still havent fixed the winring error its just as easy to move (once set up for nicehash) over to xmrig itself and use argus monitor for temps etc

## GOLDDUBBY | 2021-12-03T12:06:27+00:00
> > Bug has returned.
> > Got the error after enabling (not disable) the Power setting under advance settings.
> > Tried turning it off, but the bug is stuck.
> 
> so i think you would have to undo that option and restart nicehash cos they still havent fixed the winring error its just as easy to move (once set up for nicehash) over to xmrig itself and use argus monitor for temps etc

I restarted it all, incl full system reboot. Still present I'm afraid. Had the issue once before and had hell fixing it. I believe it was caused by using kernel mode in AB at that time. Swishing to user-mode fixed it. This time, all I did was turning on the option for NH power-control. 😑 ..I mean, it's not a big deal it's only one xeon 20 core. Not exactly farming millions, right? Still buggs me when things don't work as they are supposed to. I'm a bit anal like that 🤓

## SChernykh | 2021-12-03T12:08:31+00:00
What xmrig version do you use? Error 183 was supposed to be fixed in v6.16.0 and newer versions.

## GOLDDUBBY | 2021-12-03T12:10:43+00:00
> What xmrig version do you use? Error 183 was supposed to be fixed in v6.16.0 and newer versions.

I'm just running what NH provides me, atm it says..

XMRig/6.8.1 MSVC/2019


Should I do a complete re-install of NH ? 

The price of electricity in Sweden is completely bonkus atm anyways (from the usual €0,04.. to €0,5 /Kwh) , I've already turned off 2 rigs. 

## SChernykh | 2021-12-03T12:14:02+00:00
I'm sure you can set up Nicehash with newer xmrig versions. You can just straight copy xmrig.exe from the latest v6.16.2 into your xmrig folder and it should work.

## mikemcv879nz | 2021-12-03T12:15:21+00:00
> > What xmrig version do you use? Error 183 was supposed to be fixed in v6.16.0 and newer versions.
> 
> I'm just running what NH provides me, atm it says..
> 
> XMRig/6.8.1 MSVC/2019

6.16.0 from xmrig directly as i was annoyed by nicehash so i dont really use it except for wallet and trading aswell as the pools

## GOLDDUBBY | 2021-12-03T12:21:03+00:00
> I'm sure you can set up Nicehash with newer xmrig versions. You can just straight copy xmrig.exe from the latest v6.16.2 into your xmrig folder and it should work.

I've done similar to that in the past, but it didn't get detected properly. It was when they removed the other cpu-miner that I forgot the name of. Had to copy a folder from another rig that hadn't updated yet. That worked tho. 

I'll try getting it from XMRig directly as you suggest. Worth a shot!

## PwFake | 2021-12-03T13:42:12+00:00
> I'm sure you can set up Nicehash with newer xmrig versions. You can just straight copy xmrig.exe from the latest v6.16.2 into your xmrig folder and it should work.

I tried that method but it still didnt work and the error will still show up

## PwFake | 2021-12-03T13:43:41+00:00
I have tried all the methods but they all dont fix my problem

## jeytee84 | 2021-12-04T01:01:53+00:00
Turns out turning off [Rem0o'S FanControl](https://github.com/Rem0o/FanControl.Releases) solves the issue. 

## PwFake | 2021-12-04T01:29:25+00:00
I still have the error coming up but i have my normal hashrate that im supposed to get from disabling my fan control. Weird fix and now my pc is very very very loud

## mikemcv879nz | 2021-12-04T03:07:58+00:00
> > I'm sure you can set up Nicehash with newer xmrig versions. You can just straight copy xmrig.exe from the latest v6.16.2 into your xmrig folder and it should work.
> 
> I tried that method but it still didnt work and the error will still show up

if you have nicehash open with temps visable (disable in advanced settings) restart nicehash start xmrig then enable device status monitoring has worked for me multiple times but if you restart nicehash with temps still visable winring0 will show up

## PainkillerXX | 2021-12-08T02:01:41+00:00
> > > I'm sure you can set up Nicehash with newer xmrig versions. You can just straight copy xmrig.exe from the latest v6.16.2 into your xmrig folder and it should work.
> > 
> > 
> > I tried that method but it still didnt work and the error will still show up
> 
> if you have nicehash open with temps visable (disable in advanced settings) restart nicehash start xmrig then enable device status monitoring has worked for me multiple times but if you restart nicehash with temps still visable winring0 will show up

dude you'r a genius, i literally downgraded from windows 11 back to windows 10 thinking that would solve it. thanks it worked for me hope it works for everyone else

## finndo77 | 2021-12-11T11:32:40+00:00
> > > What xmrig version do you use? Error 183 was supposed to be fixed in v6.16.0 and newer versions.
> > 
> > 
> > I'm just running what NH provides me, atm it says..
> > XMRig/6.8.1 MSVC/2019
> 
> 6.16.0 from xmrig directly as i was annoyed by nicehash so i dont really use it except for wallet and trading aswell as the pools

This worked for me, current version is 6.16.2
1. download the package direct
2. stop mining (can leave nicehash running)
3. make a backup up xmrig.exe from nicehash
4. replace the exe ONLY
5. Start mining again
6. all good.

it did give a yellow INFO notice that winring0 already exists, but with a different service name, but it activated msr and ran anyway.

## RiotRecoil | 2021-12-31T00:10:02+00:00
> > > I'm sure you can set up Nicehash with newer xmrig versions. You can just straight copy xmrig.exe from the latest v6.16.2 into your xmrig folder and it should work.
> > 
> > 
> > I tried that method but it still didnt work and the error will still show up
> 
> if you have nicehash open with temps visable (disable in advanced settings) restart nicehash start xmrig then enable device status monitoring has worked for me multiple times but if you restart nicehash with temps still visable winring0 will show up

This worked for me as well. Downloaded xmrig 6.16.2 and replaced the xmrig.exe and Disabled Device Status Monitoring, thanks man!

## N1h1l1sT | 2022-01-04T05:44:00+00:00
What worked for me, weirdly, was to stop the Razer Game Manager service (which also stops the Razer Synapse service), run it, and then restart the services.

## jbminecraft2000 | 2022-09-11T20:25:12+00:00
nzxt cam also causes it

## Ricky9111 | 2023-05-26T08:21:40+00:00
Just delete recent downloads, and check 1 by 1.

# Action History
- Created by: blade198222 | 2021-07-06T08:08:04+00:00
- Closed at: 2025-06-20T11:11:44+00:00
