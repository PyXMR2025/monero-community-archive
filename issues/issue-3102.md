---
title: Xmrig does not detect if the computer is charging (specific hardware and linux
  kernel)
source_url: https://github.com/xmrig/xmrig/issues/3102
author: JacksonChen666
assignees: []
labels:
- review later
created_at: '2022-08-01T17:34:34+00:00'
updated_at: '2025-06-18T23:00:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
- hardware: M1 MacBook Pro (2020)
- software: gentoo linux on ARM64/AARCH64, runs [this kernel](https://github.com/AsahiLinux/linux/tree/asahi-5.19-rc7-1) (for hardware support reasons), [manually configured](https://wiki.gentoo.org/wiki/Kernel/Configuration)
- xmrig: emerged from the [`gentoo` repository](https://packages.gentoo.org/packages/net-misc/xmrig)
part of `emerge --info`:
```
=================================================================
                        Package Settings
=================================================================

net-misc/xmrig-6.18.0::gentoo was built with the following:
USE="hwloc ssl -donate (-opencl)"
```

to summarize the problem, here's just a single screenshot with most of the details:
![](https://user-images.githubusercontent.com/50755746/182206130-594c7b57-c05c-4f49-85e9-b45402f67c4f.png)

- pause on battery is enabled
- xmrig does not detect if the charger is plugged in or not, or does not respond to the charger state. (`/sys/class/power_supply/macsmc-ac/online`)
- plasma battery status in the taskbar is able to detect if the computer is charging

# Discussion History
## Spudz76 | 2022-08-01T19:21:13+00:00
Relevant function being used when in "unix" mode (it does not use Platform_mac unless it's OSX...) is [here](https://github.com/xmrig/xmrig/blob/master/src/base/kernel/Platform_unix.cpp#L148)

Only checks `/sys/class/power_supply/BAT0/status` and `/sys/class/power_supply/BAT1/status` which are the standard places for it to be, with literal content `Discharging` (not `0` or `1`).

Would require modification to look anywhere else, such as `/sys/class/power_supply/macsmc-ac/online` and only when the standard location(s) are not supported.  Or, macsmc-ac driver should be reporting via the standard location, really, but I suppose kernel source mods are more difficult to get accepted (would take many, many kernel revisions before it was there on the mainstream source).  They should have done it correctly in the first place IMHO.  Although some thinkpad-acpi type drivers also do stuff like that, it's easier/quicker to have code accepted underneath "your driver" versus more global changes (to the `BAT*` sysfs nodes in the `sysfs` driver).

## Spudz76 | 2022-08-01T19:31:53+00:00
If you have relevant C++ skills you could make and test the mod yourself just insert it before the `return false` exit, mostly a clone of the `BAT*` code just using the macsmc-ac path and then comparing to 0 (online=0 means on-battery...?) rather than the string.  Since the `BAT*` code would exit early with true if those nodes existed, it should automatically never look for macsmc-ac on anything where the proper `BAT*` nodes exist (although it would still try it on things where there is no battery, like desktop and server).

Or wait some days and I'll have a chance to formulate an acceptable Pull Request with patch as described, for you to test and confirm.

## JacksonChen666 | 2022-08-01T19:41:07+00:00
i'm debating on if i should close this issue as wont fix because of the following:
- one of the features in xmrig is not working in my case
- the linux kernel is a fork and the asahi linux project *is* trying to upstream the drivers and stuff ([battery is not upstreamed](https://github.com/AsahiLinux/docs/wiki/Feature-Support))
- plasma has a battery indicator already working when the battery driver was made, although that might be linux specific stuff (or it could be posix/unix whatever, idk)
- the fix adds additional checks for a single status (bikeshedding?)

also, there are multiple files for the battery stuff. i just used one of them because i assumed that's what xmrig could be looking for (or just to show that it is charging).

i think i might be able to deal with C++, just maybe very poorly. also, i might not work on a patch for this issue, but i also could if i wanted to (i might either have to wait for a release or use the git version).

## Spudz76 | 2022-08-05T04:06:18+00:00
You could build with the above mentioned PR and it should (might?) work.

## Spudz76 | 2022-08-05T04:09:45+00:00
Does the system have `/sys/class/power_supply/AC/online`?

## JacksonChen666 | 2022-08-05T07:29:48+00:00
@Spudz76 the system does not have the mentioned path.

the system does have the following path: `/sys/class/power_supply/macsmc-battery/status` which tells the battery status like "Discharging", "Full" (my battery was full), and "Charging".

## JacksonChen666 | 2022-08-05T07:56:42+00:00
Just made a patch [here](https://github.com/JacksonChen666/xmrig/tree/dev-M1LinuxBattery) to use `/sys/class/power_supply/macsmc-battery/status` and it does work. Note that it might be possible I made rookie errors.

# Action History
- Created by: JacksonChen666 | 2022-08-01T17:34:34+00:00
