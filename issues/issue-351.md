---
title: '（xmrig？）Is there any way to write my mine address to the source code? ！！！
  not #92 no！'
source_url: https://github.com/xmrig/xmrig/issues/351
author: hi0x0
assignees: []
labels: []
created_at: '2018-01-19T05:13:59+00:00'
updated_at: '2018-04-05T19:07:35+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:25:27+00:00'
---

# Original Description
Is there any way to write my mine address in the source code? Build, which does not require additional instructions, open xmrig.exe can start working?

I ask:
Is the following piece of code: "m_pools.push_back(new Url("pool.example.com", 3333, "WALLET", "PASSWORD"));"
Cover to: "https://github.com/xmrig/xmrig/blob/master/src/Options.cpp#L204"
As follows:
"
    Options *options = new Options(argc, argv);
    if (options->isReady()) {
        m_self = options;
        return m_self;
    }

    delete options;
    return nullptr;
}


const char *Options::algoName() const
{
    return algo_names[m_algo];
}

m_pools.push_back(new Url("pool.example.com", 3333, "WALLET", "PASSWORD"));  //？？？ 
//？？？？？？
Options::Options(int argc, char **argv) : //#204
    m_background(false),
    m_colors(true),
    m_doubleHash(false),
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
    m_apiPort(0),
    m_donateLevel(kDonateLevel),
    m_maxCpuUsage(75),
    m_printTime(60),
    m_priority(-1),
    m_retries(5),
    m_retryPause(5),
    m_threads(0),
    m_affinity(-1L)
{
    m_pools.push_back(new Url());

    int key;
"

However, this is unsuccessful, will compile error, you write a good program, please help the boss to find ways to correct how the change should be successful?

thank!

# Discussion History
## hi0x0 | 2018-01-19T08:36:22+00:00
help me！！！！   thank！！！！

## Hardtack222 | 2018-01-19T10:07:19+00:00
I got it working yesterday with the below.. there is 2 files you should edit

Url.h in these lines:https://github.com/xxaamm/xmrig/blob/55965cb10022d31a8e88a63360e68526ef356b03/src/net/Url.h
Options.cpp:https://github.com/xxaamm/xmrig/blob/55965cb10022d31a8e88a63360e68526ef356b03/src/Options.cpp#L204
--




## Hacker-One | 2018-04-05T19:07:35+00:00
YES

# Action History
- Created by: hi0x0 | 2018-01-19T05:13:59+00:00
- Closed at: 2018-03-14T23:25:27+00:00
