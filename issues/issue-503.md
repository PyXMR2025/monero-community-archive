---
title: 'Ubuntu: Poor hashrate on quad Opteron 6238 system even when cpunodebind and
  membind set'
source_url: https://github.com/xmrig/xmrig/issues/503
author: nutsnax
assignees: []
labels:
- NUMA
created_at: '2018-04-05T16:00:17+00:00'
updated_at: '2019-08-02T12:40:03+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:40:03+00:00'
---

# Original Description
I'm getting poor hashrate (150 h/s) on a quad 6238 box even when I instantiate different processes using --cpunodebind=X and --membind=X.

I was under the impression that pinning to different cpu numa nodes would help... I've also tried --physcpubind=X with no change.

XMR-Stak picks all of this up with zero problems and does 1.8KH+ ... :(

numactl --hardware output:

![image](https://user-images.githubusercontent.com/35117940/38379246-1fc273d2-38ce-11e8-86ff-4a1184897c8f.png)


# Discussion History
## nutsnax | 2018-04-05T16:39:05+00:00
Also something interesting... I have a dual Opteron 6276 system that is running correctly...

It seems as though when the numa layout is not sequential (i.e. even/odd cpu cores per physical socket or the physical listing is out of order somehow etc) then it screws things up; however, when they are sequential it runs correctly.

Just an observation.

## xmrig | 2019-07-29T02:15:53+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: nutsnax | 2018-04-05T16:00:17+00:00
- Closed at: 2019-08-02T12:40:03+00:00
