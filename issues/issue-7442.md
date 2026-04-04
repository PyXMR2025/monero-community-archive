---
title: 'Tests: core_tests caching generation from the test perspective'
source_url: https://github.com/monero-project/monero/issues/7442
author: mj-xmr
assignees: []
labels: []
created_at: '2021-03-06T10:08:03+00:00'
updated_at: '2021-03-25T15:12:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I still want to speed up the `core_tests`, by addressing the generation bottleneck [mentioned here](https://github.com/monero-project/monero/pull/7300), but without affecting the implementation itself. 

For a recap, I discovered there, that 42% of the core_tests time is taken by the generation step, so I wanted to cache it by diving deep into the implementation and putting there a local static cache. The solution was not accepted for valid reasons. I would like to propose a different solution: give the `core_tests` a new parameter: `--generate-cache-and-play`, which would perform serialization on the first run, and deserialization on the second run. For safety, the cache would have an ID, based on the md5 sum of the `core_tests` binary.

Would such a solution be accepted? Any objections?

# Discussion History
## moneromooo-monero | 2021-03-06T10:20:18+00:00
Maybe you should consider using --generate_test_data and --play_test_data instead (and fix if broken).

## mj-xmr | 2021-03-06T16:03:33+00:00
Yes, it makes sense. It was somehow broken, although not beyond repair. I'm on it.

# Action History
- Created by: mj-xmr | 2021-03-06T10:08:03+00:00
