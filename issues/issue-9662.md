---
title: auto miner do nothing on Alpine Linux - "couldn't query power status from /sys/class/power_supply"
source_url: https://github.com/monero-project/monero/issues/9662
author: tankf33der
assignees: []
labels: []
created_at: '2024-12-29T19:50:36+00:00'
updated_at: '2025-01-01T22:32:53+00:00'
type: issue
status: closed
closed_at: '2025-01-01T19:04:48+00:00'
---

# Original Description
Alpine Linux 3.20 + 0.18.3.3

empty config file, `monerod --detach`, wait  ~10mins

Log line:
```
$ cat bitmonero.log | grep miner
...
2024-12-29 19:18:16.233     14847f8bcb38        ERROR   miner   src/cryptonote_basic/miner.cpp:1073     couldn't query power status from /sys/class/power_supply
...
````

```
$ monerod mining_status
Mining at 0 H/s with 1 threads
PoW algorithm: RandomX
Mining address: 42rQUMr79zn2DT7VXBfLYYPcRMNqtS7QQNbMabMBVV6PLiRHrpUztVpPZXCsE9KX1g3ro5CRaqRXsNLSH6aJD67YG8SB7Fh
Smart mining enabled:
  Target: 40% CPU
  Idle threshold: 90% CPU
  Min idle time: 10 seconds
  Ignore battery: no
```


so, miner CAN work only if i manually set `ignore_battery`:
```
$ monerod start_mining 42rQUMr79zn2DT7VXBfLYYPcRMNqtS7QQNbMabMBVV6PLiRHrpUztVpPZXCsE9KX1g3ro5CRaqRXsNLSH6aJD67YG8SB7Fh 1 yes yes
```


# Discussion History
## iamamyth | 2025-01-01T00:04:55+00:00
Can you post the result of `ls -l --file-type /sys/class/power_supply`?

## iamamyth | 2025-01-01T02:37:54+00:00
I dug around a bit and it seems /sys/class/power_supply tends to omit devices when there's either a driver or BIOS issue, such that the power supply doesn't register properly at boot. You can usually find additional information in /sys/bus/acpi. For example, I wonder what this shows:
```
for dev in $(find /sys/bus/acpi/devices/ -name 'ACPI*'); do echo "$dev"; ls "$dev/power_supply"; done 
```

## tankf33der | 2025-01-01T08:57:43+00:00
> Can you post the result of `ls -l --file-type /sys/class/power_supply`?

```
pulsar:~# ls -l --file-type /sys/class/power_supply
total 0
pulsar:~# 
```


## tankf33der | 2025-01-01T08:58:44+00:00
> ```
> for dev in $(find /sys/bus/acpi/devices/ -name 'ACPI*'); do echo "$dev"; ls "$dev/power_supply"; done 
> ```

```
pulsar:~# for dev in $(find /sys/bus/acpi/devices/ -name 'ACPI*'); do echo "$dev"; ls "$dev/power_supply"; done 
/sys/bus/acpi/devices/ACPI0007:15
ls: cannot access '/sys/bus/acpi/devices/ACPI0007:15/power_supply': No such file or directory
/sys/bus/acpi/devices/ACPI0007:1c
ls: cannot access '/sys/bus/acpi/devices/ACPI0007:1c/power_supply': No such file or directory
/sys/bus/acpi/devices/ACPI0007:05
ls: cannot access '/sys/bus/acpi/devices/ACPI0007:05/power_supply': No such file or directory
...
...
...
```


## tankf33der | 2025-01-01T09:00:43+00:00
This Alpine Linux machine is real hardware - Dedicated server from `hetzner`.

on VPS dir is also empty.
 

## tankf33der | 2025-01-01T09:02:14+00:00
This is output from real laptop. Latest `Manjaro`.
```
[mpech@lambda power_supply]$ ls -l
total 0
lrwxrwxrwx 1 root root 0 dec 31 18:03 AC -> ../../devices/platform/ACPI0003:00/power_supply/AC
lrwxrwxrwx 1 root root 0 dec 31 18:03 BAT0 -> ../../devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0A:00/power_supply/BAT0
[mpech@lambda power_supply]$ 
```


## tankf33der | 2025-01-01T09:32:21+00:00
Debian 11, dedicated hardware server - dir is empty too.


## iamamyth | 2025-01-01T18:09:57+00:00
The output from the `lambda` machine seems like it's configured properly (has two symlinks to the real devices, which provide the necessary status info); mining should work there. On the `pulsar` machine, the output strongly suggests a configuration problem: You have ACPI devices which do not expose power supply info. I suspect if you inspect dmesg (`dmesg | grep ACPI`) and other kernel info, you'll see some ACPI errors or warnings, though you may need to enable some extra logging in the kernel.

Without proper device configuration, there's no good way to fix this issue. The software could default to ignoring battery if the user executes the `start_mining` command and the battery status cannot be determined, but that's about all I can think of which preserves the battery saving feature.

## tankf33der | 2025-01-01T18:26:17+00:00
`lambda` is laptop as i wrote above.

This issue is only about the automatic launch of the miner after starting the daemon. 

IMHO, the daemon should ignore the battery if the directory is empty and successfully launch a single thread.



## iamamyth | 2025-01-01T18:45:28+00:00
> IMHO, the daemon should ignore the battery if the directory is empty and successfully launch a single thread.

I happen to agree with you, from a first principles design perspective, but modifying an existing default behavior opens up a huge can of worms, recasting the nature of the issue from design to social coordination. If you can convince enough people that it's a worthwhile change, or think of an option which doesn't alter the existing default, so be it; otherwise, I fear you will hit a dead end.

## iamamyth | 2025-01-01T18:51:33+00:00
One change that might be worth making: Alter the logging behavior. I consider an indeterminate state a warning, rather than an error, and it might help to tell users in an indeterminate state how to fix it (set the appropriate flag on startup or fix your drivers).

## iamamyth | 2025-01-01T20:28:27+00:00
@tankf33der One last question, which maybe would sidestep backwards-compat concerns: What does the following command yield on `pulsar`?
```
for dev in $(find /sys/bus/acpi/devices/ -name 'ACPI*'); do echo "$dev"; cat "$dev/status"; done
```

## tankf33der | 2025-01-01T21:51:50+00:00
> @tankf33der One last question, which maybe would sidestep backwards-compat concerns: What does the following command yield on `pulsar`?
> 
> ```
> for dev in $(find /sys/bus/acpi/devices/ -name 'ACPI*'); do echo "$dev"; cat "$dev/status"; done
> ```

```
pulsar:~# for dev in $(find /sys/bus/acpi/devices/ -name 'ACPI*'); do echo "$dev"; cat "$dev/status"; done
/sys/bus/acpi/devices/ACPI0007:15
cat: '/sys/bus/acpi/devices/ACPI0007:15/status': No such file or directory
/sys/bus/acpi/devices/ACPI0007:1c
cat: '/sys/bus/acpi/devices/ACPI0007:1c/status': No such file or directory
/sys/bus/acpi/devices/ACPI0007:05
cat: '/sys/bus/acpi/devices/ACPI0007:05/status': No such file or directory
/sys/bus/acpi/devices/ACPI0007:0c
cat: '/sys/bus/acpi/devices/ACPI0007:0c/status': No such file or directory
/sys/bus/acpi/devices/ACPI0007:33
cat: '/sys/bus/acpi/devices/ACPI0007:33/status': No such file or directory
...
...
...
```

## iamamyth | 2025-01-01T21:57:56+00:00
Thanks for the reply. Unfortunately, that output matches my suspicion: There's no good way to gather information on the power supply, as the system recognizes it exists but can't determine its status.

## iamamyth | 2025-01-01T22:32:53+00:00
Appending a couple of useful ACPI-related resources to this thread for posterity:
* https://bugzilla.kernel.org/show_bug.cgi?id=156171
* https://wiki.ubuntu.com/Kernel/Reference/ACPITricksAndTips


# Action History
- Created by: tankf33der | 2024-12-29T19:50:36+00:00
- Closed at: 2025-01-01T19:04:48+00:00
