---
title: FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
source_url: https://github.com/xmrig/xmrig/issues/1973
author: rubic0nexe
assignees: []
labels:
- question
created_at: '2020-12-09T15:59:06+00:00'
updated_at: '2025-05-05T14:03:56+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:32:48+00:00'
---

# Original Description
FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

What is this and how do i fix that?

# Discussion History
## SChernykh | 2020-12-10T08:44:47+00:00
You need to run as administrator/root to enable MSR. You can read more here: https://xmrig.com/docs/miner/randomx-optimization-guide/msr

## mascondante | 2020-12-24T08:40:41+00:00
I'm getting this error and I am running with administrative permissions. No events in my AV. 
![image](https://user-images.githubusercontent.com/2492044/103075512-c3124780-4599-11eb-83d7-ed95ccf0e252.png)


## theSchein | 2021-01-10T04:27:52+00:00
I too am having this issue. Running as root

## tom634 | 2021-01-12T01:30:43+00:00
I too am having this issue. Running as administrator. XMRig with Ryzen.

## SChernykh | 2021-01-12T08:39:18+00:00
Please provide the full console output of XMRig when it starts

## tom634 | 2021-01-12T13:51:15+00:00
![obraz](https://user-images.githubusercontent.com/24915307/104322753-980a7c00-54e5-11eb-85f0-80d52e121594.png)
My console output

## SChernykh | 2021-01-12T14:45:00+00:00
You are not running it as administrator.

## tom634 | 2021-01-12T21:48:55+00:00
I ran as administrator and it worked, thanks

## iZerox7 | 2021-01-23T15:24:27+00:00
When i open as Administrator (Intel, win 10), it no works 
Edit: It says "pause", press any key to continue and when i press any key it closes

## melkorex | 2021-01-28T15:36:11+00:00
Hi i have same issue runing admin mode.

` * ABOUT        XMRig/6.7.2 MSVC/2019
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (1) 64-bit AES VM
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       11.4/15.9 GB (71%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.minexmr.com:4444 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-01-28 12:33:40.199]  net      use pool pool.minexmr.com:4444  37.59.43.131
[2021-01-28 12:33:40.199]  net      new job from pool.minexmr.com:4444 diff 75000 algo rx/0 height 2284462
[2021-01-28 12:33:40.200]  cpu      use argon2 implementation AVX2
[2021-01-28 12:33:40.204]  msr      cannot set MSR 0x000001a4 to 0x0000000f
[2021-01-28 12:33:40.242]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-01-28 12:33:40.243]  randomx  init dataset algo rx/0 (8 threads) seed f1a94ed2953f45f4...
[2021-01-28 12:33:40.310]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (66 ms)
[2021-01-28 12:33:45.997]  randomx  dataset ready (5686 ms)
[2021-01-28 12:33:45.997]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2021-01-28 12:33:46.000]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (2 ms)`

## SChernykh | 2021-01-28T15:39:42+00:00
```CPU Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (1) 64-bit AES VM```
The `VM` part says that you're running it inside a virtual machine. MSR mod works only on the physical CPU.

## melkorex | 2021-01-28T15:43:09+00:00
> 
> 
> `CPU Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (1) 64-bit AES VM`
> The `VM` part says that you're running it inside a virtual machine. MSR mod works only on the physical CPU.

Nop, is directly from cmd of my physical computer but i have running 4 docker working, i think that is the problem.... but its a shame 

## iZerox7 | 2021-01-28T15:44:26+00:00
I fix it 
You will have to open it frim CMD
First, You have to open cmd as Administrator, then open the dkrectory in cmd (always with CD at begining) and finally open the file
It works for me 


## SChernykh | 2021-01-28T15:44:40+00:00
It will never say `VM` on physical computer, double check where you start it from.

## melkorex | 2021-01-28T15:52:01+00:00
Come on, @SChernykh  i know the first questions is your turn off and on your computer.... but its not my case pls.

![Captura de pantalla 2021-01-28 124901](https://user-images.githubusercontent.com/46333033/106163088-8bce2200-6167-11eb-94dc-9c2e34fc550d.jpg)

Its not running in docker is my windows CMD of physical pc.


## SChernykh | 2021-01-28T15:59:44+00:00
XMRig checks the hypervisor bit in CPUID and if it's set, it shows "VM". This bit is never set on a physical CPU which means your whole Windows is running inside a VM right now. Probably because of docker or some other software you installed. MSR mod won't work until you fix it.

## melkorex | 2021-01-28T16:13:38+00:00
@SChernykh ok its say it in my physical computer.... for what ? i dont know.... later i turno off all of docker services and docker containers and try again, if i don see VM i upload the image to check the code. Thanks

## melkorex | 2021-01-28T16:22:14+00:00
I dont know its usefull for you.

![Captura de pantalla 2021-01-28 124901](https://user-images.githubusercontent.com/46333033/106167199-bc17bf80-616b-11eb-8ad3-ea8babe21682.jpg)

`wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed, status`

inform no VM

but down exec start.cmd xmrig

VM.

......


## ShadyJay1979 | 2021-01-28T23:27:27+00:00
Shut down NiceHash Miner and right click it and run as Administrator 

## guru220011 | 2021-02-02T06:23:10+00:00
Hey guys, make sure you Right Click and Run as Administrator on the file itself in the folder and not on the shortcut that it creates.

## ghost | 2021-02-03T23:26:53+00:00
On latest build i have same problem (v6.8.1) while on 6.8.0 haven't any issue (windows 10 enterprise LTSC with amd ryzen). I have run as administrator, reboot and rerun as administrator but nothing.

EDIT

Works again on v6.8.2

## 1RedOne | 2021-02-09T14:58:53+00:00
If you've got Docker and clicked 'next, next, next, finish' through the wizard, you probably setup Hyper-V.  

Once you setup hyper-v your host partition is, in some ways, treated as a VM too.  This impacts how you interact with the physical hardware on the device.

Basically you're effectively running as a VM.

## Shahnewaz1996 | 2021-02-09T19:34:13+00:00
> I'm getting this error and I am running with administrative permissions. No events in my AV.
> ![image](https://user-images.githubusercontent.com/2492044/103075512-c3124780-4599-11eb-83d7-ed95ccf0e252.png)

I fixed this by finding it under Process Hacker's Services tab, and manually editing the service's path (WinRing0 Driver).
I pointed it to XMRig's driver location, and it deleted the service afterwards.
> Come on, @SChernykh i know the first questions is your turn off and on your computer.... but its not my case pls.
> 
> ![Captura de pantalla 2021-01-28 124901](https://user-images.githubusercontent.com/46333033/106163088-8bce2200-6167-11eb-94dc-9c2e34fc550d.jpg)
> 
> Its not running in docker is my windows CMD of physical pc.

See my comment here: https://github.com/xmrig/xmrig/issues/1891#issuecomment-776180629



## TowrArisu | 2021-02-17T06:23:04+00:00
My machine had the same problem with failing to apply the MSR Mod and also showed  "VM" although it was not a VM.
I found a setting in the Bios with regards to  Intel Virtualization Technology, I switched it off and now the problem is gone.
VM no longer shows and MSR is set successfully.

## MacZillions | 2021-02-21T20:31:21+00:00
> Hey guys, make sure you Right Click and Run as Administrator on the file itself in the folder and not on the shortcut that it creates.

It works. 🤜🤛

## june-lau | 2021-02-25T06:29:55+00:00
I'm getting this error and I am running with administrative permissions. (platform: laptop, win10)
I need your help.
![1](https://user-images.githubusercontent.com/79624967/109112494-be266b80-7775-11eb-8cf1-bbfbc5bbbcf6.jpg)


## SChernykh | 2021-02-25T07:24:45+00:00
Try to reboot and don't start that program before xmrig (`Program Files (x86)\kaying_tools\program\colligatetest\masterluo`).

## mightmay | 2021-02-26T05:42:20+00:00
Hi, how can I run as admin in linux ?
Is this the correct command ?   
sudo ./xmrig

## june-lau | 2021-02-26T05:46:30+00:00
> 尝试重新启动，不要在xmrig（`Program Files (x86)\kaying_tools\program\colligatetest\masterluo`）之前启动该程序。

Thank you, sir.

## esskayesss | 2021-03-01T17:21:31+00:00
> Hi, how can I run as admin in linux ?
> Is this the correct command ?
> sudo ./xmrig

yes that should work. If you're using a configuration file, you'll now have to pass it with the `-c /path/to/config` option. Coz otherwise xmrig will search `/root` and `etc` for the config files while they might be kept in your home user config directory.

## cuppajoeman | 2021-03-03T17:12:59+00:00
> > Hi, how can I run as admin in linux ?
> > Is this the correct command ?
> > sudo ./xmrig
> 
> yes that should work. If you're using a configuration file, you'll now have to pass it with the `-c /path/to/config` option

Verified, it works.

## mightmay | 2021-03-04T17:43:48+00:00
> > > Hi, how can I run as admin in linux ?
> > > Is this the correct command ?
> > > sudo ./xmrig
> > 
> > 
> > yes that should work. If you're using a configuration file, you'll now have to pass it with the `-c /path/to/config` option
> 
> Verified, it works.

Thank You, I was sure that is the correct command, however, I am still getting this error on my Ubuntu 20:
FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
I also tried running this command: sudo bash ./scripts/randomx_boost.sh
However, I am getting the error:
`line 26: wrmsr: command not found`



## esskayesss | 2021-03-04T17:53:19+00:00
> > > > Hi, how can I run as admin in linux ?
> > > > Is this the correct command ?
> > > > sudo ./xmrig
> > > 
> > > 
> > > yes that should work. If you're using a configuration file, you'll now have to pass it with the `-c /path/to/config` option
> > 
> > Verified, it works.
> 
> Thank You, I was sure that is the correct command, however, I am still getting this error on my Ubuntu 20:
> FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
> I also tried running this command: sudo bash ./scripts/randomx_boost.sh
> However, I am getting the error:
> `line 26: wrmsr: command not found`
> 
> 

You probably have to install `wrmsr`. On Ubuntu I think it's the `msr-tools` package. 

## freki785 | 2021-03-05T07:25:08+00:00
Personally I've had some issues getting windows to start xmrig in admin mode when starting from a .cmd or .bat so if you're using this method instead of config file try:
Right clicking -> Properties -> Compatibility tab -> Check Run in Administrator mode on xmrig.exe - solved all my issues.

## mightmay | 2021-03-05T08:43:22+00:00
> > > > > Hi, how can I run as admin in linux ?
> > > > > Is this the correct command ?
> > > > > sudo ./xmrig
> > > > 
> > > > 
> > > > yes that should work. If you're using a configuration file, you'll now have to pass it with the `-c /path/to/config` option
> > > 
> > > 
> > > Verified, it works.
> > 
> > 
> > Thank You, I was sure that is the correct command, however, I am still getting this error on my Ubuntu 20:
> > FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
> > I also tried running this command: sudo bash ./scripts/randomx_boost.sh
> > However, I am getting the error:
> > `line 26: wrmsr: command not found`
> 
> You probably have to install `wrmsr`. On Ubuntu I think it's the `msr-tools` package.

Thank You, you are correct.
I was able to fix this error by installing `wrmsr `with this command:
`apt-get install msr-tools`
However, now I am getting this error instead, when I tried to run: `sudo bash ./scripts/randomx_boost.sh`
I get this error:  `wrmsr: CPU 0 cannot set MSR 0x000001a4 to 0x000000000000000f`



## SChernykh | 2021-03-05T08:46:53+00:00
@mightmay Did you take the effort to read through all messages in this issue and try proposed solutions? Everything is already here.

## esskayesss | 2021-03-05T09:31:38+00:00

> However, now I am getting this error instead, when I tried to run: `sudo bash ./scripts/randomx_boost.sh`
> I get this error:  `wrmsr: CPU 0 cannot set MSR 0x000001a4 to 0x000000000000000f`
> 
Can you post the entire output? Does it detect a proper architecture cpu?



## ghost | 2021-03-08T23:34:10+00:00
For anyone saying their CPU is showing VM but they are not running in a VM:  The Windows security feature Core Isolation - Memory Integrity will cause this.  That is because the way it works is to essentially run the entire OS inside a VM.

## chrisdab | 2021-03-17T03:49:19+00:00
The Core Isolation security setting in windows 10 caused the same issue for me as not running in administrative mode, although when not running in admin mode the error message correctly told me I wasn't in admin mode. I turned on Core Isolation recently and had my hashrate dropped, with the error message that brought me to this thread.

## DeeDeeRanged | 2021-03-31T02:34:27+00:00
> > > > > > Hi, how can I run as admin in linux ?
> > > > > > Is this the correct command ?
> > > > > > sudo ./xmrig
> > > > > 
> > > > > 
> > > > > yes that should work. If you're using a configuration file, you'll now have to pass it with the `-c /path/to/config` option
> > > > 
> > > > 
> > > > Verified, it works.
> > > 
> > > 
> > > Thank You, I was sure that is the correct command, however, I am still getting this error on my Ubuntu 20:
> > > FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
> > > I also tried running this command: sudo bash ./scripts/randomx_boost.sh
> > > However, I am getting the error:
> > > `line 26: wrmsr: command not found`
> > 
> > 
> > You probably have to install `wrmsr`. On Ubuntu I think it's the `msr-tools` package.
> 
> Thank You, you are correct.
> I was able to fix this error by installing `wrmsr `with this command:
> `apt-get install msr-tools`
> However, now I am getting this error instead, when I tried to run: `sudo bash ./scripts/randomx_boost.sh`
> I get this error: `wrmsr: CPU 0 cannot set MSR 0x000001a4 to 0x000000000000000f`

Strange you had to install msr-tools. I am running Debian bullseye/testing,  Ryzen 7 5800x getting a nice 9270.9 H/s algo rx/0,  Only thing I had to do was was using sudo to get it working as required. 

## FSPinho | 2021-06-27T14:25:30+00:00
For anyone having it on Ubuntu, I fixed it by:
- Installing msr-tools with `apt-get install msr-tools`;
- Disabling secure boot;
- And then running as root `sudo xmrig ...`

## DeeDeeRanged | 2021-06-27T18:04:24+00:00
> For anyone having it on Ubuntu, I fixed it by:
> 
>     * Installing msr-tools with `apt-get install msr-tools`;
> 
>     * Disabling secure boot;
> 
>     * And then running as root `sudo xmrig ...`

You don't need to run xmrig as root.
Download or copy the script randomx_boost.sh from https://github.com/xmrig/xmrig/scripts run that with sudo/root change to lines in the config.json file "rdmsr": false and "wrmsr": false to stop it blabbering about msr start it as user xmrig. As this is much safer.

## Eduarrb | 2021-07-15T23:58:40+00:00
> I fix it
> You will have to open it frim CMD
> First, You have to open cmd as Administrator, then open the dkrectory in cmd (always with CD at begining) and finally open the file
> It works for me

I works!!! thanks

## bktcaery | 2021-09-06T04:56:24+00:00
> For anyone having it on Ubuntu, I fixed it by:
> 
>     * Installing msr-tools with `apt-get install msr-tools`;
> 
>     * Disabling secure boot;
> 
>     * And then running as root `sudo xmrig ...`

Thanks, works great.

## Hotrod369 | 2021-11-01T19:55:45+00:00
> The Core Isolation security setting in windows 10 caused the same issue for me as not running in administrative mode, although when not running in admin mode the error message correctly told me I wasn't in admin mode. I turned on Core Isolation recently and had my hashrate dropped, with the error message that brought me to this thread.

![image](https://user-images.githubusercontent.com/72291352/139732566-049b5401-0bbb-49d7-9e7c-9e7e99aed7f1.png)
chrisdab you're exactly right. I turned off core isolation and I still get VM instead of AES but the Failed to apply MSR mod error is gone. 



## NewSunSEO | 2021-11-14T09:24:13+00:00
> 
> 
> For anyone having it on Ubuntu, I fixed it by:
> 
>     * Installing msr-tools with `apt-get install msr-tools`;
> 
>     * Disabling secure boot;
> 
>     * And then running as root `sudo xmrig ...`

THANK YOU!!!  I am new to Linux & that fixed the MSR for me.  I was looking for HOURS!!!

## ksgnu | 2021-11-14T10:09:37+00:00
> > For anyone having it on Ubuntu, I fixed it by:
> > ```
> > * Installing msr-tools with `apt-get install msr-tools`;
> > 
> > * Disabling secure boot;
> > 
> > * And then running as root `sudo xmrig ...`
> > ```
> 
> THANK YOU!!! I am new to Linux & that fixed the MSR for me. I was looking for HOURS!!!

Worked for me too, thanks a lot!

## netcast22 | 2021-11-26T06:13:00+00:00
> > > For anyone having it on Ubuntu, I fixed it by:
> > > ```
> > > * Installing msr-tools with `apt-get install msr-tools`;
> > > 
> > > * Disabling secure boot;
> > > 
> > > * And then running as root `sudo xmrig ...`
> > > ```
> > 
> > 
> > THANK YOU!!! I am new to Linux & that fixed the MSR for me. I was looking for HOURS!!!
> 
> Worked for me too, thanks a lot!

> Works like a charm!

## Soggydan | 2022-01-05T09:00:52+00:00
If you are a windows user check here for 5 fixes to try
[https://www.home-mining.com/failed-to-apply-msr-mod-hashrate-will-be-low/](url)

## SteaceP | 2022-01-17T04:23:21+00:00
The only thing that worked for me was to disable SMT (virtualization) in bios... Was doing this on a clean Windows 11 install. No Hyper-V, no WSL, no shit!

## Rakshitha-M-Rodrigo | 2022-03-16T18:37:02+00:00
running with sudo or  the super user mode worked for me. Thanks.

## sapeg | 2022-04-11T06:16:03+00:00
   Hi. I have a ryzen 5 3600, Linux OS. There is virtualization support, but it is disabled in the bios. I go under the root in the console, run from the directory where the program is located: xmrig -t 6 -o pool.minexmr.com:4444... But I still get the message: msr kernel module is not available, FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW. 
   What other options are there?


## juroberttyb | 2022-08-23T08:40:34+00:00
These steps help me on ubuntu 22.04
1, Disable secure boot
2, Reboot
3, Run xmrig as root

## umeshadabala | 2022-10-23T03:12:27+00:00
> You need to run as administrator/root to enable MSR. You can read more here: https://xmrig.com/docs/miner/randomx-optimization-guide/msr


Thanks a lot it helped me.

## furic | 2022-11-16T04:05:09+00:00
Fixed by [disabling "Memory Integrity"](https://github.com/xmrig/xmrig/issues/1891#issuecomment-776180629) on Windows.

## Egemenbdk | 2023-05-31T01:49:09+00:00
I FOUND OUT HOW TO FIX IT COMPLETELY!

1. Go into BIOS mode. (search up on google how to go in BIOS mode on your motherboard/laptop)
2. Disable Intel VTD and Intel VTX. If you only have one, just disable that one.
3. Save and exit, start your computer.
4. Run cmd as admin
5. Type "cd C:\Users\YOUR_NAME_HERE\Downloads\xmrig-6.19.2-gcc-win64\xmrig-6.19.2" OR wherever your file is located.
6. Then type xmrig.exe into the cmd.

## ghost | 2023-11-06T05:03:14+00:00
Buy another motherboard.

## NorthScholar | 2024-02-15T16:55:44+00:00
Im having this issue too, i right click and select run as administrator..what to do excatly=?
PS. I have Memory Integrity turned off in Windows 11
![Uten navn](https://github.com/xmrig/xmrig/assets/160160271/8988bb1b-f6d1-4f51-a5b5-9c41bac5b2c4)
And what else can i do to improve my outcome? except for buying new hardware :-) i know, i know i need new


## SChernykh | 2024-02-15T17:11:06+00:00
Did you try other advices from this thread? Secure boot disabled?

## NorthScholar | 2024-02-15T17:18:38+00:00
I tried what i understand :)
I dont know how to: Installing msr-tools with `apt-get install msr-tools, i will keep reading a bit

## SChernykh | 2024-02-15T17:49:23+00:00
`apt-get install msr-tools`
This is not for Windows

## NorthScholar | 2024-02-15T20:27:10+00:00
Where or how do i use it? Do i write in the "extra parameters"?

## SChernykh | 2024-02-15T20:31:38+00:00
You just don't use it on Windows. You should try to disable any memory integrity, secure boot, virtualization options you can find in BIOS and in Windows.

## NorthScholar | 2024-02-15T20:42:08+00:00
Ok, thanks - i have not checked my BIOS yet. i will do that now next 

## jsalaz-Gramps | 2024-03-19T20:02:10+00:00
Turning off Memory integrity is worrisome, since shortly after I mpoved the switch to disabled, 64 detectio0ns from Malwarebytes had to be cleaned.  I will use it, to get the MSR tweak, but that's it.  I really does not improve performance on this computer of mine.  HP Pavillion CX with AMD Ryzen 7.

I will be getting the AISC USB sticks on Amazon, with an associated power strip soon.  It's all I can afford due to financial restraints.

## ghost | 2024-04-12T15:24:52+00:00
i've followed everything above and still nothing. 
disabled secure boot
disabled virtualization
after all that no MSR mod (it fails)

## jsalaz-Gramps | 2024-04-12T15:28:13+00:00
When you right click on the xmrig.exe file, does it say Unblock? If ti does, Unblock it. It's very picky.



## ghost | 2024-04-12T15:35:09+00:00
no unblock button, just properties settings, probably because i unzipped the file.
also running the benchmarks that came with it

upd: 23.19% in 10 minutes (1 mil test)

## jsalaz-Gramps | 2024-04-12T15:40:21+00:00
OK, the unblock is under properties. It should be in the lower half on the right. Unzipping doesn't cause the files to break, but it makes everything accessible. The same goes for benchmarking. No issues with that either.

On Apr 12 2024, at 9:35 am, nick name ***@***.***> wrote:
>
>
> no unblock button, just properties settings, probably because i unzipped the file.
> also running the benchmarks that came with it
>
>
> —
> Reply to this email directly, view it on GitHub (https://github.com/xmrig/xmrig/issues/1973#issuecomment-2051993115), or unsubscribe (https://github.com/notifications/unsubscribe-auth/BDU7FTAIV32PDNE4DWJVSNTY475MPAVCNFSM4UTWCS72U5DIOJSWCZC7NNSXTN2JONZXKZKDN5WW2ZLOOQ5TEMBVGE4TSMZRGE2Q).
> You are receiving this because you commented.
>



## jsalaz-Gramps | 2024-04-12T15:41:17+00:00
OH, I forgot to ask what version of Windows 11 do you have?

On Apr 12 2024, at 9:39 am, Jason Salaz ***@***.***> wrote:
> OK, the unblock is under properties. It should be in the lower half on the right. Unzipping doesn't cause the files to break, but it makes everything accessible. The same goes for benchmarking. No issues with that either.
>
> On Apr 12 2024, at 9:35 am, nick name ***@***.***> wrote:
> >
> >
> > no unblock button, just properties settings, probably because i unzipped the file.
> > also running the benchmarks that came with it
> >
> >
> > —
> > Reply to this email directly, view it on GitHub (https://github.com/xmrig/xmrig/issues/1973#issuecomment-2051993115), or unsubscribe (https://github.com/notifications/unsubscribe-auth/BDU7FTAIV32PDNE4DWJVSNTY475MPAVCNFSM4UTWCS72U5DIOJSWCZC7NNSXTN2JONZXKZKDN5WW2ZLOOQ5TEMBVGE4TSMZRGE2Q).
> > You are receiving this because you commented.
> >
>



## jsalaz-Gramps | 2024-04-12T15:47:53+00:00
Hoepfully my previous comment about the Unblock being under properties is going to work. I have a script that I can send, that will manually unlock the MSR addresses. It works, but will still show the MSR Mod not applying, but it will when you run the batch file.

On Apr 12 2024, at 9:40 am, Jason Salaz ***@***.***> wrote:
> OH, I forgot to ask what version of Windows 11 do you have?
>
> On Apr 12 2024, at 9:39 am, Jason Salaz ***@***.***> wrote:
> > OK, the unblock is under properties. It should be in the lower half on the right. Unzipping doesn't cause the files to break, but it makes everything accessible. The same goes for benchmarking. No issues with that either.
> >
> > On Apr 12 2024, at 9:35 am, nick name ***@***.***> wrote:
> > >
> > >
> > > no unblock button, just properties settings, probably because i unzipped the file.
> > > also running the benchmarks that came with it
> > >
> > >
> > > —
> > > Reply to this email directly, view it on GitHub (https://github.com/xmrig/xmrig/issues/1973#issuecomment-2051993115), or unsubscribe (https://github.com/notifications/unsubscribe-auth/BDU7FTAIV32PDNE4DWJVSNTY475MPAVCNFSM4UTWCS72U5DIOJSWCZC7NNSXTN2JONZXKZKDN5WW2ZLOOQ5TEMBVGE4TSMZRGE2Q).
> > > You are receiving this because you commented.
> > >
> >
>



## jsalaz-Gramps | 2024-04-12T16:26:37+00:00
Did it work?

On Apr 12 2024, at 9:47 am, Jason Salaz ***@***.***> wrote:
> Hoepfully my previous comment about the Unblock being under properties is going to work. I have a script that I can send, that will manually unlock the MSR addresses. It works, but will still show the MSR Mod not applying, but it will when you run the batch file.
>
> On Apr 12 2024, at 9:40 am, Jason Salaz ***@***.***> wrote:
> > OH, I forgot to ask what version of Windows 11 do you have?
> >
> > On Apr 12 2024, at 9:39 am, Jason Salaz ***@***.***> wrote:
> > > OK, the unblock is under properties. It should be in the lower half on the right. Unzipping doesn't cause the files to break, but it makes everything accessible. The same goes for benchmarking. No issues with that either.
> > >
> > > On Apr 12 2024, at 9:35 am, nick name ***@***.***> wrote:
> > > >
> > > >
> > > > no unblock button, just properties settings, probably because i unzipped the file.
> > > > also running the benchmarks that came with it
> > > >
> > > >
> > > > —
> > > > Reply to this email directly, view it on GitHub (https://github.com/xmrig/xmrig/issues/1973#issuecomment-2051993115), or unsubscribe (https://github.com/notifications/unsubscribe-auth/BDU7FTAIV32PDNE4DWJVSNTY475MPAVCNFSM4UTWCS72U5DIOJSWCZC7NNSXTN2JONZXKZKDN5WW2ZLOOQ5TEMBVGE4TSMZRGE2Q).
> > > > You are receiving this because you commented.
> > > >
> > >
> >
>



## Fgr-35 | 2024-06-08T22:45:06+00:00
Is there a way to apply msr mod on a .cmd file? I couldn't get xmrig to connect with the pool so i made a .cmd file provided by the pool to start but i cannot run it in admin mode so i won't get msr. How can i fix that?

## ImTand | 2024-11-09T14:21:08+00:00
Sorry, I know I'm about 4 years late lol. In your BIOS (if you're using an AMD CPU) there should be a setting called SVM. If not, search for virtualization. In my BIOS I found this setting under the "Advanced" tab, then CPU Configuration, and then SVM Mode. I believe that it has a different name if you're using an Intel CPU but the process should be mostly the same.

Make sure you have SVM or any CPU Virtualization **OFF.** Then, once it is off, you should be able to run the command prompt as an administrator and start your XMRig through there. This doubled to tripled my hashrates, so I hope this works for you all!

## jsalaz-Gramps | 2024-11-09T18:21:12+00:00
 Thank you!

On Sat, Nov 9, 2024 at 7:21 AM ImTand ***@***.***> wrote:

> Sorry, I know I'm about 4 years late lol. In your BIOS (if you're using an
> AMD CPU) there should be a setting called SVM. If not, search for
> virtualization. In my BIOS I found this setting under the "Advanced" tab,
> then CPU Configuration, and then SVM Mode. I believe that it has a
> different name if you're using an Intel CPU but the process should be
> mostly the same.
>
> Make sure you have SVM or any CPU Virtualization *OFF.* Then, once it is
> off, you should be able to run the command prompt as an administrator and
> start your XMRig through there. This doubled to tripled my hashrates, so I
> hope this works for you all!
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1973#issuecomment-2466236861>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/BDU7FTEUWXY7CWQXDAI6PLDZ7YK63AVCNFSM4UTWCS72U5DIOJSWCZC7NNSXTN2JONZXKZKDN5WW2ZLOOQ5TENBWGYZDGNRYGYYQ>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


## TheSeer507 | 2025-02-21T04:26:19+00:00
> I FOUND OUT HOW TO FIX IT COMPLETELY!
> 
> 
> 
> 1. Go into BIOS mode. (search up on google how to go in BIOS mode on your motherboard/laptop)
> 
> 2. Disable Intel VTD and Intel VTX. If you only have one, just disable that one.
> 
> 3. Save and exit, start your computer.
> 
> 4. Run cmd as admin
> 
> 5. Type "cd C:\Users\YOUR_NAME_HERE\Downloads\xmrig-6.19.2-gcc-win64\xmrig-6.19.2" OR wherever your file is located.
> 
> 6. Then type xmrig.exe into the cmd.

This work for me, Intel i7 processor on a HP ZBook laptop. Both options where present turned off both, hash rate when 3x.

## BeanieBoy95 | 2025-03-10T06:03:03+00:00
![Image](https://github.com/user-attachments/assets/0d30828a-4d89-4403-b047-175bea1c268c) currently running with admin priv, this happened after a bios update. any solutions?

## SChernykh | 2025-03-10T08:06:02+00:00
BIOS updates reset all settings. You need to disable virtualization in BIOS again.

## jsalaz-Gramps | 2025-03-10T16:30:19+00:00
I am in agreement. everything seems to get reset to defaults, and the VM for Windows is reenabled. check System Info, and see if Virtual Based Security is on. If it is, there is a massive tutorial that I had.. I'll have to still check if I have it. But it's extra complicated. Like crazy Complicated. Are you running Windows 11 24H2?

Sent from Mailspring (https://getmailspring.com/), the best free email app for work
On Mar 10 2025, at 2:06 am, SChernykh ***@***.***> wrote:
>
> SChernykh left a comment (xmrig/xmrig#1973) (https://github.com/xmrig/xmrig/issues/1973#issuecomment-2709731560)
>
> BIOS updates reset all settings. You need to disable virtualization in BIOS again.
>
> —
> Reply to this email directly, view it on GitHub (https://github.com/xmrig/xmrig/issues/1973#issuecomment-2709731560), or unsubscribe (https://github.com/notifications/unsubscribe-auth/BDU7FTGUKZF7HI6IHQUUWDL2TVBYHAVCNFSM4UTWCS72U5DIOJSWCZC7NNSXTN2JONZXKZKDN5WW2ZLOOQ5TENZQHE3TGMJVGYYA).
> You are receiving this because you commented.
>



## satyadvi | 2025-05-05T14:03:55+00:00
msr mod is not getting unabled , i did a bios update and not its not just working.  moreover i'm using OMEN GAMING LAPTOP , can't even access proper bios , what to do??


# Action History
- Created by: rubic0nexe | 2020-12-09T15:59:06+00:00
- Closed at: 2021-04-12T14:32:48+00:00
