---
title: '"FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW" on start.'
source_url: https://github.com/xmrig/xmrig/issues/1805
author: kyngs
assignees: []
labels: []
created_at: '2020-08-09T08:17:41+00:00'
updated_at: '2020-08-10T07:23:31+00:00'
type: issue
status: closed
closed_at: '2020-08-10T07:23:31+00:00'
---

# Original Description
For some reason on the start, the miner is unable to apply MSR mod.
![log](https://user-images.githubusercontent.com/38181667/89727887-f4460d00-da28-11ea-8bfc-138e6c3a53ba.png)
Config: https://drive.google.com/file/d/1kQAHj8xCeZ_rW7wSJ84_7BlQtWoMDFmZ/view?usp=sharing


# Discussion History
## SChernykh | 2020-08-09T19:18:50+00:00
Do you run xmrig as root?

## kyngs | 2020-08-09T20:37:22+00:00
> Do you run xmrig as root?

Of course I do.

## SChernykh | 2020-08-09T20:39:37+00:00
MSR mod doesn't work in a VM. I've just noticed that you have `4C/4T` at startup whereas EPYC 7282 is 16C/32T CPU.

## kyngs | 2020-08-10T07:19:11+00:00
> MSR mod doesn't work in a VM. I've just noticed that you have `4C/4T` at startup whereas EPYC 7282 is 16C/32T CPU.

So am I doomed?

## SChernykh | 2020-08-10T07:21:29+00:00
You can still mine, but not at max speed. VMs restrict access to MSR registers because they can be used for getting full access to the physical machine, so you can't do anything here.

## kyngs | 2020-08-10T07:23:31+00:00
I guess I will search for a new algorithm. Because those mining speeds are poor.

# Action History
- Created by: kyngs | 2020-08-09T08:17:41+00:00
- Closed at: 2020-08-10T07:23:31+00:00
