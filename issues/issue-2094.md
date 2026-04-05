---
title: xmrig in datacenter
source_url: https://github.com/xmrig/xmrig/issues/2094
author: tbizarre
assignees: []
labels:
- question
created_at: '2021-02-11T08:11:18+00:00'
updated_at: '2021-04-12T14:16:10+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:16:10+00:00'
---

# Original Description
Hello,
I am using xmrig on a server with 8 xeons of 20 cores each.

On the server I installed vmware and I created 2 VMs with Ubuntu 18, 80 cores and 16Gb of ram.

Each Vm manages to keep an average of 20Kh / s.

Is it fair as a result or can I achieve more?

Thank you

# Discussion History
## ghost | 2021-02-11T18:48:09+00:00
Running directly on OS can make a lot more as it can enable things like msr mods

## xmrig | 2021-02-12T09:57:13+00:00
Correct autoconfiguration is not guaranteed in virtual machines, it highly depends how precise CPU topology represented to the guests and vmware usually create pretty bad CPU topology and the miner will use all cores because it reports much more CPU cache than you actually have. For optimal performance you should run miner without virtualization especially if you use a multi-CPU server.
Thank you.

# Action History
- Created by: tbizarre | 2021-02-11T08:11:18+00:00
- Closed at: 2021-04-12T14:16:10+00:00
