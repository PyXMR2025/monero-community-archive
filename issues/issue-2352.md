---
title: how to configure mining only use cpu 2
source_url: https://github.com/xmrig/xmrig/issues/2352
author: zhlzjz
assignees: []
labels: []
created_at: '2021-05-07T03:24:31+00:00'
updated_at: '2021-05-11T19:48:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have a dual E5-2680 v2 system. Just want to configure only cpu2 to mining. need cpu1 work for other task.

But not sure how to edit the config file.

# Discussion History
## RCTORONTO | 2021-05-07T13:34:00+00:00
you need to look at defining the cpu affinity, google "cpu affinity calculator", mark the threads you want active, and copy the value into your config file (I think it's a mask that tells xmrig where to put your x # of threads)

## Spudz76 | 2021-05-09T00:31:02+00:00
Clarifying, the `--affinity` command line option is a mask (all allowed CPUs, 64-bit binary each bit-position is a CPU core) and only applies to runs where autoconfig is triggered (will be ignored if your config.json already has algo/threads defined).  Delete the whole section of algo/thread defs for any of the autoconfig hint command-line options to work.  Or rename the entire file so it does complete first-run cycle again.

All affinity in the config.json are not masks, but core ID number which can be different depending on Linux or Windows (they count cores, HT/Fakecores, and multiple cpus differently).  If you put "3" it runs on core "3" not any of core "0" or "1" (which is "3" in binary mask, 0 and 1 positions are "on").  If you wanted "ID 3" in a mask it would be "4" because the third bit position on, rest are off.  And everything is zero-based so core "3" is the fourth core (first core is "0", but with bitmask value "1")

## coolhaircut | 2021-05-10T19:10:06+00:00
See this config in my comment for https://github.com/xmrig/xmrig/issues/1193#issuecomment-837168279

The E5 Xeons have weird affinities like this to try to make sure the workload is split evenly in dual sockets if you just specify the first half of the cores. So for a 2x 20 core CPUs, specifying 0-19 would recruit 0-9 from cpu1 and 10-19 from cpu2.

**Affinity for your E5s:**
`CPU1: 0-9, 20-29`
`CPU2: 10-19,30-39`

To override this, just manually declare the cores in the `cpu` part of the config for your algo. So to use 100% cpu1 and 0% cpu2 on Randomx, set the config to this:

`"cpu":{"rx/0":[0,1,2,3,4,5,6,7,8,9,20,21,22,23,24,25,26,27,28,29]}`

## Spudz76 | 2021-05-11T19:48:34+00:00
Correct however the ordering/grouping changes depending if Linux or Windows.

# Action History
- Created by: zhlzjz | 2021-05-07T03:24:31+00:00
