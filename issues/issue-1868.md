---
title: How to use "max-cpu-usage" without thread pinning for RandomX in the embedded
  config ?
source_url: https://github.com/xmrig/xmrig/issues/1868
author: fahoc22128
assignees: []
labels: []
created_at: '2020-10-06T09:56:24+00:00'
updated_at: '2020-10-07T07:43:10+00:00'
type: issue
status: closed
closed_at: '2020-10-07T07:43:10+00:00'
---

# Original Description
I use "max-cpu-usage" in the embedded config but would like to avoid problem with newer Windows scheduler and make sure threads are unpinned like in manual setting: "rx": [-1,-1, ...],

How to do this in the embedded config while using "max-cpu-usage" setting ?

Thank you in advance!

# Discussion History
## SChernykh | 2020-10-07T05:53:35+00:00
Note that there's another solution for Windows scheduler problem: https://www.reddit.com/r/MoneroMining/comments/iq9kl9/windows_10_sudden_low_hashrate_mystery_solved/
Default config generators always pin threads to cores.

# Action History
- Created by: fahoc22128 | 2020-10-06T09:56:24+00:00
- Closed at: 2020-10-07T07:43:10+00:00
