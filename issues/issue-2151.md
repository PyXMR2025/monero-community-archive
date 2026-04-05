---
title: Hashrate loss
source_url: https://github.com/xmrig/xmrig/issues/2151
author: saloniamatteo
assignees: []
labels:
- bug
created_at: '2021-03-02T12:27:45+00:00'
updated_at: '2025-06-16T20:00:45+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:00:45+00:00'
---

# Original Description
**Describe the bug**
Before the latest commit[s], XMRig would show totals when pressing <kbd>h</kbd> when mining. Now, I only see my CPU's hashrate per core, without the total hashrate.

**To Reproduce**
1. Start mining
2. Press <kbd>h</kbd> after miner is ready

**Expected behavior**
XMRig should show the totals, below the individual core stats. Example:

| CPU # 	| AFFINITY 	| 10s H/s 	| 60s H/s 	| 15m H/s 	|
|-------	|----------	|---------	|---------	|---------	|
| 0     	| 0        	| 500     	| 500     	| 500     	|
| 1     	| 2        	| 500     	| 500     	| 500     	|
| -     	| -        	| 1000     | 1000     |  1000    |

**Required data**
 - Miner log as text or screenshot:
![IMG_20210302_131329](https://user-images.githubusercontent.com/28765699/109648413-e093fc80-7b5a-11eb-9c79-3fd320c258c3.png)
 - Command line:
```bash
xmrig -o stratum+tcp://[url]:[port] -u [wallet id] -k --rig-id [rig id] \
--randomx-1gb-pages --cpu-no-yield --cpu-priority 5 \
--randomx-mode fast --asm intel --randomx-no-numa \
--no-color --print-time 120 \
--cpu-affinity=0x255 -a rx/0 -t 2
```
 - OS: Artix Linux, Linux-ck 5.11.2

# Discussion History
## andress134 | 2021-03-03T02:45:48+00:00
Yes some wrong here
the new version of xmrig does not work well at all
I don't know what's going on but I'm using the same servers I've used before, my servers have 5-6 kH / s and now just 1k why?
Im using linux, os: ubuntu 18 / debian 9

## saloniamatteo | 2021-03-05T08:02:34+00:00
More details:
- xmrig version:
```bash
XMRig 6.9.1-dev
 built on Mar  4 2021 with GCC 10.2.0
 features: 64-bit AES

libuv/1.41.0
OpenSSL/1.1.1j
hwloc/2.4.0
```

I can confirm @andress134's issue: hashrate dropped significantly (about 100/200H/s lost)

## saloniamatteo | 2021-04-13T11:38:09+00:00
@xmrig, Even if you close this issue, #2151, the problems still persist in the latest version, 6.11.3-dev, noticeably the hashrate drop & missing hashrate total tab, as written above.

## xmrig | 2021-04-13T11:57:44+00:00
I unable to reproduce this bug, did you know the version when or better the commit when did this bug appear.
Thank you.

## saloniamatteo | 2021-04-13T11:59:49+00:00
I'm sure these two issues appeared before release 6.9.1, as I had written in the original post.

## xmrig | 2021-04-13T12:02:09+00:00
Ok I will try to reproduce this again later.
Thank you.


## xmrig | 2021-04-13T12:09:42+00:00
Total hashrate is not really required if you build CPU only miner, next line will print total hashrate anyway, #2261 makes it less confusing.
Thank you.


## saloniamatteo | 2021-04-13T12:15:00+00:00
Good! Now the only issue left is the hashrate loss.

To give you more details, I had bought a new CPU, an Intel Core i7-4700MQ. When I first started the miner with the new CPU, it had reached 1648H/s, but it has never come back up like that. Now it fluctuates between 1404H/s and 1500H/s.

I have checked multiple times if my setup is somewhat wrong, I have repasted the CPU, I have cleaned the fans, but nothing has changed.

## saloniamatteo | 2021-04-13T12:15:44+00:00
I had noticed this with my older CPU as well, Intel Core i5-4340M, where the Hashes per second dropped from ~1030H/s to ~900H/s

## SChernykh | 2021-04-13T12:21:31+00:00
These are mobile CPUs, they never give stable hashrate. Check that huge pages and MSR mod are working, clean up Windows: https://xmrig.com/docs/miner/randomx-optimization-guide
You probably installed some programs that are running in the background and slowing down xmrig.

## saloniamatteo | 2021-04-13T12:28:27+00:00
Yes, they indeed are mobile CPUs. However, I'm not running Windows: I'm running Artix Linux, and I'm mining with as less processes running as possible.

To reduce overhead, I kill X.org, and I interact directly with the TTY.

I've even set every process' niceness to 19, and XMRig's niceness to -20, so that the scheduler focuses on mining. I've also set CPUs 0-2-4-6 as the CPUs used for mining, and no other processes can use them.

I'm using the MSR mod already, as well as hugepages, so I can't apply any more optimizations.

## SChernykh | 2021-04-13T12:33:01+00:00
It must be because of power settings for your CPUs, they're just running at lower speed. You can just test some old XMRig version to see if you get the same lower hashrate.

## saloniamatteo | 2021-04-13T12:35:42+00:00
Again, no power settings are influencing mining. Since I have a Thinkpad T440p, I have removed the battery, and only use the charger to power my laptop, as I have suspected intense and repeated battery usage might damage it, and lower its life.

## Spudz76 | 2021-04-15T23:43:36+00:00
I mine on same CPU and it does this.  Lenovo W540 in particular has garbage cooling no matter what paste or how clean the insufficient fan is.  Perhaps T440p similar once heat-soaked.  Add external blow-through fan and see if rate rises and stabilizes, and then there's the answer, it's heat management in a laptop not being designed for 101%/24/27 duty cycles.

I can't even mine the GPU without thermal overload and shutdown, and all my screws are worn to nubs from how much I've repasted...

Anyway it should still hit that nice max when fired up from cold, for 5 minutes or less.

## saloniamatteo | 2021-04-16T04:36:15+00:00
@Spudz76, I've set my laptop's fan speed to 7 (one step away from maximum), and the CPU temperature does not get above 60°C.

Even after cold starting it, it does not get above 1500H/s.

## Spudz76 | 2021-04-17T11:26:26+00:00
Here's how hot mine runs, and it downclocks from 3.4 because of it.  Fan on max.
Since the GPU shares the same radiator/heatpipe setup, running any mining on that raises total temps to 90C+ and then it shuts off.

```
 * ABOUT        XMRig/6.11.3-dev-mo3 gcc/9.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Core(TM) i7-4700MQ CPU @ 2.40GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       13.4/15.5 GB (86%)
                DIMM_A0: 4 GB DDR3 @ 1600 MHz M471B5173QH0-YK0  
                DIMM_A1: 4 GB DDR3 @ 1600 MHz M471B5173QH0-YK0  
                DIMM_B0: 4 GB DDR3 @ 1600 MHz M471B5173QH0-YK0  
                DIMM_B1: 4 GB DDR3 @ 1600 MHz M471B5173QH0-YK0  

  miner    speed 10s/60s/15m 1432.4 1444.4 n/a H/s max 1462.3 H/s

root@tpad:~# grep -r . /sys/devices/system/cpu/cpu*/cpufreq/*cur*
/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq:3192727
/sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq:3192732
/sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq:3192727
/sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq:3192725
/sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq:3192732
/sys/devices/system/cpu/cpu5/cpufreq/scaling_cur_freq:3192726
/sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq:3192802
/sys/devices/system/cpu/cpu7/cpufreq/scaling_cur_freq:3192804

root@tpad:~# sensors
thinkpad-isa-0000
Adapter: ISA adapter
fan1:        4464 RPM
temp1:        +83.0°C  
temp2:         +0.0°C  
temp3:         +0.0°C  
temp4:         +0.0°C  
temp5:         +0.0°C  
temp6:         +0.0°C  
temp7:         +0.0°C  
temp8:         +0.0°C  

BAT0-acpi-0
Adapter: ACPI interface
in0:          12.22 V  

coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +84.0°C  (high = +84.0°C, crit = +100.0°C)
Core 0:        +83.0°C  (high = +84.0°C, crit = +100.0°C)
Core 1:        +82.0°C  (high = +84.0°C, crit = +100.0°C)
Core 2:        +84.0°C  (high = +84.0°C, crit = +100.0°C)
Core 3:        +74.0°C  (high = +84.0°C, crit = +100.0°C)

acpitz-acpi-0
Adapter: ACPI interface
temp1:        +83.0°C  (crit = +200.0°C)
```

## saloniamatteo | 2021-04-17T11:42:40+00:00
Here are my current stats (I'm still getting 1500H/s, by the way):

```bash
[root@artix ~] # grep -r . /sys/devices/system/cpu/cpu*/cpufreq/*cur*
/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq:2993235
/sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq:2993506
3/sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq:2993235
/sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq:2993329
/sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq:2993235
/sys/devices/system/cpu/cpu5/cpufreq/scaling_cur_freq:2993415
/sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq:2993235
/sys/devices/system/cpu/cpu7/cpufreq/scaling_cur_freq:2993946

[root@artix ~] # sensors
thinkpad-isa-0000
Adapter: ISA adapter
fan1:        4778 RPM
temp1:        +64.0°C
temp2:        +0.0°C
temp3:        +0.0°C
temp4:        +0.0°C
temp5:        +0.0°C
temp6:        +0.0°C
temp7:        +0.0°C
temp8:        +0.0°C

coretemp-isa-0000
Adapter: ISA adapter
Package id 0:       +65.0°C    (high = +84.0°C, crit = +100.0°C)
Core 0:             +64.0°C    (high = +84.0°C, crit = +100.0°C)
Core 1:             +65.0°C    (high = +84.0°C, crit = +100.0°C)
Core 2:             +62.0°C    (high = +84.0°C, crit = +100.0°C)
Core 3:             +62.0°C    (high = +84.0°C, crit = +100.0°C)

acpitz-acpi-0
Adapter: ACPI interface
temp1:             +64.0°C    (crit = +200.0°C)
```
I do not have a GPU (except for my CPU's iGPU); how are you getting higher clock speeds?

By the way, I suggest undervolting (for me at least, that keeps the CPU cool and efficient)

Also note that I only have 8GB of RAM.

## Spudz76 | 2021-04-18T23:04:32+00:00
No idea how to undervolt, I'll see if I can figure it out.
First file blasts fan at 100% always, Second file may be how my clocks are higher - i think the default max are 3100000...  Confirmed powersave is no different than performance as long as xmrig is running (same cur_freqs)
```
root@tpad:~# cat /etc/sysfs.d/01-thinkpad_acpi.conf 
#devices/platform/thinkpad_hwmon/hwmon/hwmon4/pwm1_enable = 2
devices/platform/thinkpad_hwmon/hwmon/hwmon4/pwm1_enable = 0
devices/platform/thinkpad_hwmon/hwmon/hwmon4/pwm1 = 255
root@tpad:~# cat /etc/sysfs.d/02-cpufreq.conf 
devices/system/cpu/cpufreq/policy0/scaling_governor = powersave
devices/system/cpu/cpufreq/policy1/scaling_governor = powersave
devices/system/cpu/cpufreq/policy2/scaling_governor = powersave
devices/system/cpu/cpufreq/policy3/scaling_governor = powersave
devices/system/cpu/cpufreq/policy4/scaling_governor = powersave
devices/system/cpu/cpufreq/policy5/scaling_governor = powersave
devices/system/cpu/cpufreq/policy6/scaling_governor = powersave
devices/system/cpu/cpufreq/policy7/scaling_governor = powersave
devices/system/cpu/cpufreq/policy0/scaling_max_freq = 3400000
devices/system/cpu/cpufreq/policy0/scaling_min_freq = 800000
devices/system/cpu/cpufreq/policy1/scaling_max_freq = 3400000
devices/system/cpu/cpufreq/policy1/scaling_min_freq = 800000
devices/system/cpu/cpufreq/policy2/scaling_max_freq = 3400000
devices/system/cpu/cpufreq/policy2/scaling_min_freq = 800000
devices/system/cpu/cpufreq/policy3/scaling_max_freq = 3400000
devices/system/cpu/cpufreq/policy3/scaling_min_freq = 800000
devices/system/cpu/cpufreq/policy4/scaling_max_freq = 3400000
devices/system/cpu/cpufreq/policy4/scaling_min_freq = 800000
devices/system/cpu/cpufreq/policy5/scaling_max_freq = 3400000
devices/system/cpu/cpufreq/policy5/scaling_min_freq = 800000
devices/system/cpu/cpufreq/policy6/scaling_max_freq = 3400000
devices/system/cpu/cpufreq/policy6/scaling_min_freq = 800000
devices/system/cpu/cpufreq/policy7/scaling_max_freq = 3400000
devices/system/cpu/cpufreq/policy7/scaling_min_freq = 800000
```

## saloniamatteo | 2021-04-19T05:04:07+00:00
/g/ memes aside, I have to add that installing Gentoo increased my hashrate instantly (got to 1550H/s).

I haven't tested this further because I'm compiling other packages, but later I'll let everyone know if the hashrate increase is significant enough to make a change and try it out.

@Spudz76, undervolt with `intel-undervolt`.

## Spudz76 | 2021-04-19T09:15:34+00:00
Yes, thanks, I tried some undervolting but had barely any result from `-100` and it was already unstable there.  `-125` locks up instantly.

Seems like the Core and Cache undervolt are tied together on this CPU model.

Trying this setup right now, seems okay:
```
root@tpad:~# intel-undervolt measure
dram:             4.228 W
package-0:        1.052 W

Package id 0:    90.000°C
Core 0:          87.000°C
Core 1:          88.000°C
Core 2:          90.000°C
Core 3:          88.000°C

Core 0:        3192.443 MHz
Core 1:        3192.423 MHz
Core 2:        3192.445 MHz
Core 3:        3192.425 MHz
Core 4:        3192.443 MHz
Core 5:        3192.444 MHz
Core 6:        3192.445 MHz
Core 7:        3192.445 MHz
root@tpad:~# intel-undervolt read
CPU (0): -47.85 mV
GPU (1): -0.00 mV
CPU Cache (2): -47.85 mV
System Agent (3): -0.00 mV
Analog I/O (4): -0.00 mV

Short term package power: 59 W, 0.002 s, disabled
Long term package power: 47 W, 28.000 s, enabled
```

## saloniamatteo | 2021-04-19T09:51:02+00:00
@Spudz76, I have the following configuration:

```bash
[matteo@gentoo ~] $ doas intel-undervolt read
CPU (0): -80.08 mV
GPU (1): -75.20 mV
CPU Cache (2): -80.08 mV
System Agent (3): -75.20 mV
Analog I/O (4): -70.31 mV
```

`/etc/intel-undervolt.conf`:

```
# Enable or Disable Triggers (elogind)
# Usage: enable [yes/no]

enable yes

# CPU Undervolting
# Usage: undervolt ${index} ${display_name} ${undervolt_value}
# Example: undervolt 2 'CPU Cache' -25.84

undervolt 0 'CPU' -80.00
undervolt 1 'GPU' -75.00
undervolt 2 'CPU Cache' -80.00
undervolt 3 'System Agent' -75.00
# Limiting I/O can affect USB charging
# and other stuff as well
undervolt 4 'Analog I/O' -70.00

# Power Limits Alteration
# Usage: power ${domain} ${short_power_value} ${long_power_value}
# Power value: ${power}[/${time_window}][:enabled][:disabled]
# Domains: package
# Example: power package 45 35
# Example: power package 45/0.002 35/28
# Example: power package 45/0.002:disabled 35/28:enabled

# Critical Temperature Offset Alteration
# Usage: tjoffset ${temperature_offset}
# Example: tjoffset -20
#tjoffset -15

# Energy Versus Performance Preference Switch
# Usage: hwphint ${mode} ${algorithm} ${load_hint} ${normal_hint}
# Hints: see energy_performance_available_preferences
# Modes: switch, force
# Load algorithm: load:${capture}:${threshold}
# Power algorithm: power[:${domain}:[gt/lt]:${value}[:[and/or]]...]
# Capture: single, multi
# Threshold: CPU usage threshold
# Domain: RAPL power domain, check with `intel-undervolt measure`
# Example: hwphint force load:single:0.8 performance balance_performance
# Example: hwphint switch power:core:gt:8 performance balance_performance
# Best performance on AC
hwphint switch power:core:gt:8:and:uncore:lt:3 performance balance_performance
# Best performance on Battery
hwphint switch load:single:0.90 balance_power power

# Daemon Update Interval
# Usage: interval ${interval_in_milliseconds}

interval 5000

# Daemon Actions
# Usage: daemon action[:option...]
# Actions: undervolt, power, tjoffset
# Options: once

daemon undervolt:once
daemon power
daemon tjoffset
```

It works fine for me, even with normal use.

# Action History
- Created by: saloniamatteo | 2021-03-02T12:27:45+00:00
- Closed at: 2025-06-16T20:00:45+00:00
