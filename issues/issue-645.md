---
title: Config Help for VM
source_url: https://github.com/xmrig/xmrig/issues/645
author: hierdem
assignees: []
labels: []
created_at: '2018-05-22T12:10:35+00:00'
updated_at: '2018-06-17T18:01:56+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:01:56+00:00'
---

# Original Description
For various reasons I'm forced to run xmrig on a Hyper-V VM with x2 E5-2660 v2 CPU.

Any recommendations about what should be ideal CPU config for the VM? Right now, I'm running 30 (15x2) cores for VM, since each CPU comes with 25 MB cache, it seems sufficient.

What should be the affinity configuration? From what I could test best performance comes when first 12 cores of both of the CPUs are used. It tested using cores 0-11 and 15-26 on xmr-stak, how should it be set on xmrig? Of course I'm open for suggestions for different configs.

I can get around 1 KH/s while using xmr-stak but really wish to try xmrig with optimal configuration. Not sure if this is a good score for this kind of CPU combination or not, so I would appreciate all the input.

# Discussion History
## QwertyJack | 2018-05-29T23:44:28+00:00
1 KH/s is the limit of this kind of cpu. Any optimization would not increase the hashrate from my point of view.

# Action History
- Created by: hierdem | 2018-05-22T12:10:35+00:00
- Closed at: 2018-06-17T18:01:56+00:00
