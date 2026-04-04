---
title: Please provide cli and gui binaries for armhf and aarch64
source_url: https://github.com/monero-project/monero-gui/issues/1441
author: baryluk
assignees: []
labels: []
created_at: '2018-06-02T06:40:44+00:00'
updated_at: '2020-01-16T02:23:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

just a tracking bug for a wishlist I have myself and have seen from others.

Please provide prebuilt binaries for cli-only and gui for armhf (or more armv7-a with tunning for Cortex-A15, and NEON+VFPv4 assumed to be available) and for aarch64 (aka ARMv8.1-A with tunning for Cortex-A75). (tunning means -mtune in gcc, aka code compatible with older models, but instruction selection and scheduling optimized more toward specific model, so it works on older/newer chips, but on common chips that it is tuned for it works even better).

This would be useful as building monero on arm is kind of bit a time consuming. Or if doing crosscompilation requires a lot of preparations (either using qemu, or crosscompiling toolchain with all dependencies installed too, but that does not allow to run tests for example). Also a lot of people with Raspberry Pi and other fruit boards would really want to use them. Not to mention it would help you keep monero better tested and more portable for the future. Once you have continues build and testing in place.

And please be sure to make builds reproducible, so one can compile monero and gui on personal machine with the same libraries and compilers, and verify that binaries are the same.

PS. ppc64el (tuned for power8/power9) would be useful too, but considering small number of people using it, and the fact that these machines are powerful and can compile monero in few minutes, it is smaller issue.


# Discussion History
## baryluk | 2018-06-02T06:51:49+00:00
PS. I found there is continues build already in place (as expected), https://build.getmonero.org/buildslaves  
both 32 and 64 bit arm.

But https://build.getmonero.org/buildslaves/armv8 shows last build was in Februrary. :/ And no gui builds attempted on arm7 or armv8 :/


## selsta | 2020-01-16T02:23:02+00:00
FWIW, CLI now supports reproducible builds and offers ARMv7 and ARMv8 downloads.

# Action History
- Created by: baryluk | 2018-06-02T06:40:44+00:00
