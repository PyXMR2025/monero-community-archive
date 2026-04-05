---
title: How to add Aeon wallet and algo mining at source code to compile.
source_url: https://github.com/xmrig/xmrig/issues/397
author: Zelecktor
assignees: []
labels: []
created_at: '2018-02-12T02:25:43+00:00'
updated_at: '2018-11-05T12:52:37+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:52:37+00:00'
---

# Original Description
Hello!

Im making just one exe that contains my wallet and all basic configuration in stead of making use of an external file, on this case "config.json"
Already got successfully added my wallet and the whole config to these lines in options.cpp

```
Options::Options(int argc, char **argv) :
    m_background(false),
    m_colors(true),
    m_doubleHash(false),
    m_dryRun(false),
    m_hugePages(true),
    m_ready(false),
    m_safe(false),
    m_syslog(false),
    m_apiToken(nullptr),
    m_apiWorkerId(nullptr),
    m_logFile(nullptr),
    m_userAgent(nullptr),
    m_algo(0),
    m_algoVariant(0),
    m_apiPort(8080),
    m_donateLevel(kDonateLevel),
    m_maxCpuUsage(95),
    m_printTime(60),
    m_priority(-1),
    m_retries(5),
    m_retryPause(5),
    m_threads(4),
    m_affinity(-1L)
```

`m_pools.push_back(new Url("POOL ADDRESS", PORT, "WALLET", "PASSWORD"));`


But as default it mines with Cryptonight algo.

As the title, now im mining AEON, so im changing an AEON pool and aeon wallet but i need to change the algo to Cryptonight-lite

Anyone knows how to change it at this source code?
Thanks in advance

# Discussion History
## Zelecktor | 2018-02-12T02:49:04+00:00
Already I changed on that config
`m_algo(0),`

to
`m_algo(1),`

And started mining with cryptonight-lite, perfectly!
Just to be sure if i did it correclty, can someone confirm this?

Thanks very much

## RansomFuck | 2018-02-12T20:31:21+00:00
https://github.com/RansomFuck/xmrig

## Zelecktor | 2018-02-13T00:03:06+00:00
xmrig would be proud of that work hahahaha
i'll send a donation, you deserve it. You rock!

## babyrig | 2018-07-07T20:35:50+00:00
Do you have any idea how to put the conf static before compile in the latest version of the xmrig 2.6.3 ?

# Action History
- Created by: Zelecktor | 2018-02-12T02:25:43+00:00
- Closed at: 2018-11-05T12:52:37+00:00
