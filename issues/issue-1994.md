---
title: OpenCL 1.1 Support
source_url: https://github.com/xmrig/xmrig/issues/1994
author: Geo25rey
assignees: []
labels: []
created_at: '2020-12-22T04:41:22+00:00'
updated_at: '2021-04-12T14:27:05+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:27:05+00:00'
---

# Original Description
When I try to use OpenCL on Linux with my Radeon HD 7970 using the amdgpu driver, I get this kernel compilation error. "OpenCL C version 1.1 does not support the 'static' storage class specifier." I assume that means that global's can't be defined with the "static" modifier. 


# Discussion History
## Spudz76 | 2020-12-22T05:03:14+00:00
Should work with amdgpu-pro 19.50 pretty well.  At some point Tahiti support got worse, it was always incomplete (sysfs `pp_*` stuff does nothing or crashes, etc), and some of the newer changes seem to have broken it more.  Also needs module args to enable Sea Islands series support.  Normally for graphics, the driver for Tahiti is `radeon`, but that doesn't do OpenCL at all - so you also need to blacklist radeon.

Also what algo, some have need of features that aren't available on earlier chips.  For example there is no support for the rounding mode needed for CN-R in Evergreen series (HD5xxx) so that algo will never work.  May be some similar functions with Tahiti.  Really the Hawaii was the first fully modern chip.

I have a Tahiti-Pro 3GB here and it seems to work on amdgpu-pro 20.30, although it throws compute errors a small percentage of the time constantly, it supports OpenCL 1.2 which is the minimum for mining.

I also have a HD7870 but it doesn't work, although seems more like the hardware is goofy (need repaste, bad vrms, something).  No errors about OpenCL it just hangs upon trying, after the compile.

## Spudz76 | 2020-12-22T05:12:53+00:00
It is also possible to run the regular free amdgpu module from Ubuntu and only install the amdgpu-pro opencl pieces (not the dkms etc) and sometimes that works when either MesaCL+freedriver won't or full amdgpu-pro stack won't.  I use hybrid stack to run a couple of V64 cards that wouldn't work any other way.  I don't use any of these for graphic output and the hybrid stack may not work for that at all (due to mixing Xorg parts).

There is a [patch here](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=972794#10) to make amdgpu-pro actually compile with kernel 5.4.x, and hacking `/etc/os-release` is how you get the various AMD installations to stop complaining about the 18.04 packs on 20.04, or vice versa.  They all work on either one really but AMD had to put a test in some of their packages that refuses to continue (and there is no 19.50 for 20.04 etc).

## Geo25rey | 2020-12-22T16:32:42+00:00
After installing the amdgpu-pro driver, I now have access to OpenCL 2.1. Now there's a new issue tho. I get this error: "error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2181038080." Is there a way in the config to limit the memory usage of an opencl device?

## bcheeves | 2021-02-28T06:29:23+00:00
I was getting the same issue with my AMD on a Mac. Check the "index" value for the algorithm that you're mining and make sure it's set to the correct device "0, 1,2, etc".  You'll see in the output when you run xmrig which device it's accessing.  Also, checking the MEM column to see if it matches how much memory you have dedicated for the graphics card.  If not, you need to adjust the worksize and intensity values to something lower. Remember, intensity needs to be a multiple of worksize as well.

# Action History
- Created by: Geo25rey | 2020-12-22T04:41:22+00:00
- Closed at: 2021-04-12T14:27:05+00:00
