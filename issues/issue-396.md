---
title: Severe Linux 4.15 Slowdowns
source_url: https://github.com/xmrig/xmrig/issues/396
author: XRiga
assignees: []
labels: []
created_at: '2018-02-09T23:29:12+00:00'
updated_at: '2018-11-05T12:50:26+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:50:26+00:00'
---

# Original Description
I have for the last few months been hashing at 520H/s on a Ryzen 1700X, but as of this morning after upgrading to Linux 4.15, I can't break 380H/s.

I believe this is to do with the Meltdown/Spectre patches included in the latest kernel, however I'm seeing this with a Ryzen CPU. My understanding is that the latest Kernel introduces a couple of things that might cause this. One is retpoline in the kernel, and the other is PTI. If I reboot with kernel arguments `spectre_v2=off` and `pti=off`, I regain performance of 430H/s. Still around 100H/s short of Linux 4.14.

Would this be fixable in software in xmrig, such as by reducing the amount of syscalls made?

# Discussion History
## erotavlasme | 2018-03-30T12:53:43+00:00
I have an i7-3537u that is involved in all bugs Meltdown, Spectre v1 and v2 with respect to Ryzen that is only involved in Spectre v1 and v2. I'm using kernel v.4.13.0-37 and I did not notice any reduction on the hash rate even if the kernel is already patched.

# Action History
- Created by: XRiga | 2018-02-09T23:29:12+00:00
- Closed at: 2018-11-05T12:50:26+00:00
