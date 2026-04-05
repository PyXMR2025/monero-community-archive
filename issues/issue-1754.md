---
title: AMD GPU not reporting possible health stats
source_url: https://github.com/xmrig/xmrig/issues/1754
author: pjbollinger
assignees: []
labels:
- bug
created_at: '2020-06-28T17:45:48+00:00'
updated_at: '2020-07-09T16:24:40+00:00'
type: issue
status: closed
closed_at: '2020-07-09T16:24:39+00:00'
---

# Original Description
**Describe the bug**
There is no report for temperatures/wattage/fan speeds when data is accessible.

**To Reproduce**
Have an amdgpu hwmon folder like I have below? Not sure if there is better steps to reproduce, I feel it is highly dependent on the system.

**Expected behavior**
When data is available, all temperatures/wattage/fan speeds/frequencies should be reported.

**Required data**
 - Miner log as text or screenshot: See below
 - Config file or command line (without wallets): I can provide if necessary, but don't think it is based on code.
 - OS: Ubuntu 18.04.4 LTS
 - For GPU related issues: amdgpu 18.50-725072

**Additional context**

I will start to look at writing a PR for this but I feel the `sysfs_read` in this conditional statement is a bit too restrictive: https://github.com/xmrig/xmrig/blob/16863763d3d3796cfef5ac06013e26244627145b/src/backend/opencl/wrappers/AdlLib_linux.cpp#L85

If we remove that and generalize the following code to search for reported information, this would probably behave as intended: https://github.com/xmrig/xmrig/blob/16863763d3d3796cfef5ac06013e26244627145b/src/backend/opencl/wrappers/AdlLib_linux.cpp#L131-L135

Based on the sysfs "standard", properties could be numbered 1-*. I feel a for loops, similar to checking `hwmon` folders would be a benefit, and just return the first folder found. I feel the structure of the `AdlHealth` could be more supportive of multiple measurements of the same type, but adding the loop and returning the first result is probably a good first step.

`xmrig` log:
```
[2020-06-28 13:26:36.215]  opencl   #0 06:00.0   0W  0C    0RPM 0/0MHz
[2020-06-28 13:26:36.215]  opencl   #1 07:00.0   0W  0C    0RPM 0/0MHz
[2020-06-28 13:26:36.215]  opencl   #2 08:00.0   0W  0C    0RPM 0/0MHz
[2020-06-28 13:26:36.216]  opencl   #3 09:00.0   0W  0C    0RPM 0/0MHz
[2020-06-28 13:26:36.216]  opencl   #4 0a:00.0   0W  0C    0RPM 0/0MHz
[2020-06-28 13:26:36.216]  opencl   #5 0b:00.0   0W  0C    0RPM 0/0MHz
```

`hwmon` folder contents:
```
miner@miner-001:~$ ls /sys/bus/pci/drivers/amdgpu/0000\:06\:00.0/hwmon/hwmon2/
device/          fan1_input       fan1_min         in0_input        name             power1_average   power1_cap_max   pwm1             pwm1_max         subsystem/       temp1_crit_hyst  uevent           
fan1_enable      fan1_max         fan1_target      in0_label        power/           power1_cap       power1_cap_min   pwm1_enable      pwm1_min         temp1_crit       temp1_input 
miner@miner-001:~$ ls /sys/bus/pci/drivers/amdgpu/0000\:07\:00.0/hwmon/hwmon3/
device/          fan1_input       fan1_min         in0_input        name             power1_average   power1_cap_max   pwm1             pwm1_max         subsystem/       temp1_crit_hyst  uevent           
fan1_enable      fan1_max         fan1_target      in0_label        power/           power1_cap       power1_cap_min   pwm1_enable      pwm1_min         temp1_crit       temp1_input      
miner@miner-001:~$ ls /sys/bus/pci/drivers/amdgpu/0000\:08\:00.0/hwmon/hwmon4/
device/          fan1_input       fan1_min         in0_input        name             power1_average   power1_cap_max   pwm1             pwm1_max         subsystem/       temp1_crit_hyst  uevent           
fan1_enable      fan1_max         fan1_target      in0_label        power/           power1_cap       power1_cap_min   pwm1_enable      pwm1_min         temp1_crit       temp1_input      
miner@miner-001:~$ ls /sys/bus/pci/drivers/amdgpu/0000\:09\:00.0/hwmon/hwmon5/
device/          fan1_input       fan1_min         in0_input        name             power1_average   power1_cap_max   pwm1             pwm1_max         subsystem/       temp1_crit_hyst  uevent           
fan1_enable      fan1_max         fan1_target      in0_label        power/           power1_cap       power1_cap_min   pwm1_enable      pwm1_min         temp1_crit       temp1_input      
miner@miner-001:~$ ls /sys/bus/pci/drivers/amdgpu/0000\:0a\:00.0/hwmon/hwmon6/
device/          fan1_input       fan1_min         in0_input        name             power1_average   power1_cap_max   pwm1             pwm1_max         subsystem/       temp1_crit_hyst  uevent           
fan1_enable      fan1_max         fan1_target      in0_label        power/           power1_cap       power1_cap_min   pwm1_enable      pwm1_min         temp1_crit       temp1_input      
miner@miner-001:~$ ls /sys/bus/pci/drivers/amdgpu/0000\:0b\:00.0/hwmon/hwmon7/
device/          fan1_input       fan1_min         in0_input        name             power1_average   power1_cap_max   pwm1             pwm1_max         subsystem/       temp1_crit_hyst  uevent           
fan1_enable      fan1_max         fan1_target      in0_label        power/           power1_cap       power1_cap_min   pwm1_enable      pwm1_min         temp1_crit       temp1_input  
```

# Discussion History
## xmrig | 2020-06-29T06:12:17+00:00
Please upload content of hwmon folders it required to test changes and your PR against your data and what GPUs do you use?

I added restrictive check for `freq1_input` for case if files in hwmon* directory available, but not readable, I wrongly guessed this file is always available.

`temp2_input` should be preferable and `temp1_input` should used only as failback, because temp2 is junction temperature, but seems it not reported in your case, same for `freq*_input` it reports different clocks.

Thank you.



## pjbollinger | 2020-06-29T16:02:16+00:00
Since it doesn't cause errors if the file doesn't exist, I think it should be OK to remove the check for `freq1_input`. 

Also, for temperature, do you think it makes sense to return the max value out of all temperatures found? So if junction temp is available, that would be the hottest. Same question for fans and power, should we return the max for each category?

Contents of my hwmon folders for `AMD Radeon (TM) RX 470 Graphics`:

```
device/
fan1_input
fan1_min
in0_input
name
power1_average
power1_cap_max
pwm1
pwm1_max
subsystem/
temp1_crit_hyst
uevent           
fan1_enable
fan1_max
fan1_target
in0_label
power/
power1_cap
power1_cap_min
pwm1_enable
pwm1_min
temp1_crit
temp1_input
```

## xmrig | 2020-07-03T14:24:28+00:00
Fixed in the dev branch, I replaced `freq1_input` check to `temp1_input` or `power1_average` check, if use a mix of different generations of GPUs files can exist, but not readable, so read check required.

According the docs https://dri.freedesktop.org/docs/drm/gpu/amdgpu.html?highlight=fan1_input#gpu-power-thermal-controls-and-monitoring `freq1_input` and `freq2_input` is fixed, same as `power1_average` and `fan1_input` no need to search other values.

`temp1_input` is used as a fallback if reading of `temp2_input` fails as it is not supported for all GPUs.


## xmrig | 2020-07-09T16:24:39+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.2.3

# Action History
- Created by: pjbollinger | 2020-06-28T17:45:48+00:00
- Closed at: 2020-07-09T16:24:39+00:00
