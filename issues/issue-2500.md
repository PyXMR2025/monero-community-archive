---
title: READY threads 4/4 (4) huge pages 0% 0/8 memory 8192 KB (3 ms)
source_url: https://github.com/xmrig/xmrig/issues/2500
author: ipinyulun
assignees: []
labels: []
created_at: '2021-07-30T06:56:51+00:00'
updated_at: '2023-12-18T13:01:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Dear all

`
sudo ./xmrig --donate-level 2 -o rx.unmineable.com:3333 -u RVNxxxxxxxxxxxxxxxxxx.ipinrigrx -k --cpu-max-threads-hint=50 --cpu-priority=5 --cpu-no-yield --hugepage-size=1280 -cpu-memory-pool=-1 --randomx-no-numa --randomx-1gb-pages`

thats my command above
 and below is what i get
![image](https://user-images.githubusercontent.com/44455228/127613391-cc947ebc-098e-48e9-b34d-91097f681029.png)
![image](https://user-images.githubusercontent.com/44455228/127613448-5242f1f7-fd70-4f2a-a933-aba99e6e45bb.png)



i wonder why the huge pages show 0 %.. can somebody enlighten me?
and also the hash rate was quite low






# Discussion History
## SChernykh | 2021-07-30T13:48:08+00:00
You have 1 GB pages working there, but no regular huge pages. Probably you need to enable them on the OS level manually.

## Spudz76 | 2021-07-31T21:22:35+00:00
You also missed the double `--` on the `cpu-memory-pool` arg and used a single `-` which it took as `--config "pu-memory-pool=1"` (top line says it can't open that file...)

Your system provided hwloc is ancient, compile the included deps with `./scripts/build_deps.sh` and don't turn it off since it's fairly important for binding memory to the right places for max performance (~2.3KH/s).  Which is still below optimal for that fixed-diff pool port (which is for 3.33KH/s).  Your accepts will just be farther between than 30s optimal target, such as an autodiff pool would do.

Also you need the `3` 1GB hugepages that you have, but then also at least `8` 2MB hugepages at the same time.  Only the main RandomX dataset uses 1GB pages, the regular miner threads use 2MB always, so it needs both.  Kernel args to force reservations at boot: `hugepagesz=1GB hugepages=3 hugepagesz=2MB hugepages=8` or wrangle with your own `/etc/sysfs.d` file to set them (sometimes 1GB pages don't reserve without the kernel doing it before userspace fires up).

## ipinyulun | 2021-08-03T09:55:37+00:00
> You have 1 GB pages working there, but no regular huge pages. Probably you need to enable them on the OS level manually.

alright.. will try

## ipinyulun | 2021-08-03T09:58:54+00:00
> You also missed the double `--` on the `cpu-memory-pool` arg and used a single `-` which it took as `--config "pu-memory-pool=1"` (top line says it can't open that file...)
> 
> Your system provided hwloc is ancient, compile the included deps with `./scripts/build_deps.sh` and don't turn it off since it's fairly important for binding memory to the right places for max performance (~2.3KH/s). Which is still below optimal for that fixed-diff pool port (which is for 3.33KH/s). Your accepts will just be farther between than 30s optimal target, such as an autodiff pool would do.
> 
> Also you need the `3` 1GB hugepages that you have, but then also at least `8` 2MB hugepages at the same time. Only the main RandomX dataset uses 1GB pages, the regular miner threads use 2MB always, so it needs both. Kernel args to force reservations at boot: `hugepagesz=1GB hugepages=3 hugepagesz=2MB hugepages=8` or wrangle with your own `/etc/sysfs.d` file to set them (sometimes 1GB pages don't reserve without the kernel doing it before userspace fires up).

sorry, new bie here. btw what do you mean by 3 1GB hugepage... 
should i set the huges to 3 or 8
what i read from xmrig hugepage was this(set to 1280) which left me confuse
`sudo sysctl -w vm.nr_hugepages=1280`

also i cant find /etc/sysfs.d
what in my etc was

![image](https://user-images.githubusercontent.com/44455228/127997097-e7787e21-dced-45ee-abcf-69294391faad.png)


## ipinyulun | 2021-08-03T09:59:23+00:00
 thank you both for your input


## Spudz76 | 2021-08-03T10:33:29+00:00
If Ubuntu/Debian for `/etc/sysfs.d/` you need to install `sysfsutils` package.  Kernel args (into `/etc/default/grub`) is the easiest way.

In the kernel args, where `hugepagesz` is set to 1GB then `hugepages=3` is set that means how many 1GB pages... then `hugepagesz=2MB` switches context for the next `hugepages=8` and sets 8*2MB hugepages in addition to the 1GB ones.  They are parsed in the order they are on the line.  `hugepagesz` defines what the next `hugepages` it finds means.  Therefore the order is very important, as I pasted.

If everything worked out right, then `grep . /sys/devices/system/node/node*/hugepages/hugepages-*/nr*` should be like:

```
/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages:3
/sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages:8
```

Rather than showing `0`.

The documentation for hugepages which uses `vm.nr_hugepages` only controls 2MB hugepages and there is no 1GB hugepage access via sysctl, only sysfs.  xmrig has had 2MB hugepage support for a long time, 1GB was added after RandomX became a thing, therefore anywhere it says just hugepages means 2MB unless it specifically says 1GB hugepages.

## ipinyulun | 2021-08-04T06:16:23+00:00
Thanks...

> If Ubuntu/Debian for `/etc/sysfs.d/` you need to install `sysfsutils` package. Kernel args (into `/etc/default/grub`) is the easiest way.
> 
> In the kernel args, where `hugepagesz` is set to 1GB then `hugepages=3` is set that means how many 1GB pages... then `hugepagesz=2MB` switches context for the next `hugepages=8` and sets 8*2MB hugepages in addition to the 1GB ones. They are parsed in the order they are on the line. `hugepagesz` defines what the next `hugepages` it finds means. Therefore the order is very important, as I pasted.
> 
> If everything worked out right, then `grep . /sys/devices/system/node/node*/hugepages/hugepages-*/nr*` should be like:
> 
> ```
> /sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages:3
> /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages:8
> ```
> 
> Rather than showing `0`.
> 
> The documentation for hugepages which uses `vm.nr_hugepages` only controls 2MB hugepages and there is no 1GB hugepage access via sysctl, only sysfs. xmrig has had 2MB hugepage support for a long time, 1GB was added after RandomX became a thing, therefore anywhere it says just hugepages means 2MB unless it specifically says 1GB hugepages.

![image](https://user-images.githubusercontent.com/44455228/128130857-698f22ad-5395-47bf-92af-a50d5f1bd267.png)



all i did was change the param 
`--hugepage-size=2048`
and set 
`sudo sysctl -w vm.nr_hugepages=2048`
and i was able to turn on the huge page above...
current setup is with 
`--cpu-max-threads-hint=70`
i wonder if this is  the MAX?

and also
![image](https://user-images.githubusercontent.com/44455228/128131157-4e6f9149-a66e-4334-81a2-2367b364803c.png)

somehow if i set the hugepages below 2048,.. the hugepages wont fill and will be like this
![image](https://user-images.githubusercontent.com/44455228/128131264-75593508-57bb-44ed-875c-ab1ce9c0a3d4.png)






## ipinyulun | 2021-08-04T07:23:18+00:00


> Your system provided hwloc is ancient, compile the included deps with `./scripts/build_deps.sh` and don't turn it off since it's fairly important for binding memory to the right places for max performance (~2.3KH/s)

anyway,  i saw hwloc is TLS openSSL thing... does is have to do with the command 
`--tls | enable SSL/TLS support (needs pool support`)


how to know and turn if on or off ? since i didnt include `--tls` in my command.. i guess its off by default?





## Spudz76 | 2021-08-04T19:27:48+00:00
hwloc is how the miner navigates the hardware (hw) location (loc) of various components, like CPU cores, cache, memory slots, etc and also how the miner binds memory and cache allocations properly stacked to CPU cores in a fully cross-platform way. 
 Turning it off falls back to the old code which may not work properly.  But old versions especially less than 2.x might not work well either.
 
Zero to do with SSL/TLS which is all in OpenSSL.  That is less touchy about version drift since billions of things use it and would all whine loudly if they change the API without bumping to a new major-ver.  But for tested deps it's best to still use the bundled ones.

Then libuv is what provides asynchronous threading so that the miner can do 80 things at once (well, 5 or 6 things plus however many mining threads...) and have an event-based main loop more easily than inventing from scratch.  This may or may not be subject to API changes but it makes sense to use the latest possible (which won't be what comes with the distro `*-dev` packages).  Or if you're on Debian Sid (unstable) maybe the things would be far too new...

Regardless just build the deps and tell cmake `-DXMRIG_DEPS=../scripts/deps` since that's where `scripts/build_deps.sh` puts them when it's complete.  Then ensure the lib versions line at launch shows the right stuff:

` * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1`

## ipinyulun | 2021-08-25T07:11:40+00:00
> hwloc is how the miner navigates the hardware (hw) location (loc) of various components, like CPU cores, cache, memory slots, etc and also how the miner binds memory and cache allocations properly stacked to CPU cores in a fully cross-platform way.
> Turning it off falls back to the old code which may not work properly. But old versions especially less than 2.x might not work well either.
> 
> Zero to do with SSL/TLS which is all in OpenSSL. That is less touchy about version drift since billions of things use it and would all whine loudly if they change the API without bumping to a new major-ver. But for tested deps it's best to still use the bundled ones.
> 
> Then libuv is what provides asynchronous threading so that the miner can do 80 things at once (well, 5 or 6 things plus however many mining threads...) and have an event-based main loop more easily than inventing from scratch. This may or may not be subject to API changes but it makes sense to use the latest possible (which won't be what comes with the distro `*-dev` packages). Or if you're on Debian Sid (unstable) maybe the things would be far too new...
> 
> Regardless just build the deps and tell cmake `-DXMRIG_DEPS=../scripts/deps` since that's where `scripts/build_deps.sh` puts them when it's complete. Then ensure the lib versions line at launch shows the right stuff:
> 
> ` * LIBS libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1`

Thanks you bro.
sorry for the late... i been busy with my works recently


i installed it, and its works... next would be monitoring its hashrate.. currently i only get like 1400 h/s
maybe becoz i was using my laptop simultaneously 

## Royal-Techno | 2023-12-18T13:00:37+00:00

![Screenshot 2023-12-18 183113](https://github.com/xmrig/xmrig/assets/65861003/5a6ab03f-f6b8-4bde-9ba7-0e5022132f33)
@echo off
xmrig.exe --donate-level 1 -o pool.hashvault.pro:3333 -u xxxxxxxx-p SnoXEco2 -a rx/0 --huge-pages-jit --cpu-no-yield -k 
pause

Am I doing something wrong in this bat file as when I ran this in administration privilege I still not getting huge pages. 

I am running it on win 11. 

# Action History
- Created by: ipinyulun | 2021-07-30T06:56:51+00:00
