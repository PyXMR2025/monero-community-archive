---
title: RandomX init setting being overwritten by max-threads-hint
source_url: https://github.com/xmrig/xmrig/issues/1689
author: Miner9009
assignees: []
labels: []
created_at: '2020-05-24T09:41:33+00:00'
updated_at: '2020-08-19T01:19:19+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:19:19+00:00'
---

# Original Description
Applies to embedded config and outside config.

When using setting:
`  "max-threads-hint": 25, `

The initialization setting to use all threads is not working and is overwritten by 25% setting:
```
 "randomx": {
        "init": -1,  
```

Expecting initialization data to run on all available threads and then use 25% to mine.

OS: Windows 10

# Discussion History
## downystreet | 2020-06-01T13:10:33+00:00
I'm not quite understanding your question here. If what you're trying to say is that you want xmrig to initialize with all threads and then only mine at 25%, I don't think that's possible. You can either mine with all threads or a lesser percentage of threads depending on your CPU. What you can do is go to the config.json file which is usually located in the xmrig/src directory when you compile and should be moved to the build directory and go down below the "cpu" option and where you see "rx": [ ], you can put in this box the number of threads you want to use. When you start mining this box usually gets prefilled with what xmrig thinks is the optimal configuration. This option varies depending on your available L3 and L2 Cache. For example if you have a 4 core CPU with 8MB of L3 cache then rx will probably look something like this "rx": [0, 1, 2, 3]. It creates 4 threads for each 2mb of L3 cache. A 4 core cpu with 6mb L3 cache might only use [0, 1, 2]. So lets say you have a 4 core CPU with 8mb L3 cache and your config looks like "rx": [0, 1, 2, 3], you can basically set it to only use 3 cores or 75% by using [0, 1, 2] or you can set it to 50% using [0, 1] or 25% using [0]. This is basically what the "max-threads-hint" option is doing for you. I think you can also configure it to use the cores at a certain affinity but I'm not 100% sure how this works and I haven't done much testing with it, except I have used the setting "rx": [-1, -1, -1, -1]. Where each number represents the core affinity. I'm not totally sure how this works but I didn't notice much difference when using this setting as compared to the other way.

## Miner9009 | 2020-06-03T18:34:30+00:00
> I'm not quite understanding your question here. If what you're trying to say is that you want xmrig to initialize with all threads and then only mine at 25%, I don't think that's possible. 

It's not possible due to bug, otherwise why there would be separate option for it... 
It is possible when you're not using percentage (max-threads-hint) and instead use constant to set threads to how u want for example use all threads to init and then two cores on a four core processor (50%) to mine.

# Action History
- Created by: Miner9009 | 2020-05-24T09:41:33+00:00
- Closed at: 2020-08-19T01:19:19+00:00
