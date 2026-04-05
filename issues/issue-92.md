---
title: Is there any way to write my mine address to the source code?
source_url: https://github.com/xmrig/xmrig/issues/92
author: Likelym
assignees: []
labels:
- question
created_at: '2017-09-06T04:56:25+00:00'
updated_at: '2018-01-19T05:05:00+00:00'
type: issue
status: closed
closed_at: '2017-09-19T08:08:27+00:00'
---

# Original Description
Is there any way to write my mine address in the source code? Build, which does not require additional instructions, open xmrig.exe can start working?

# Discussion History
## lolcocks123 | 2017-09-06T05:58:11+00:00
Hmmmm, interesting.
I too am interested in this.

## xmrig | 2017-09-06T13:23:48+00:00
https://github.com/xmrig/xmrig/blob/master/src/Options.cpp#L204 can override default (empty) pool url.

## Valke88 | 2017-09-08T20:56:33+00:00
I also would like to know how to integrate my pool and wallet address into xmrig.exe

> https://github.com/xmrig/xmrig/blob/master/src/Options.cpp#L204 can override default (empty) pool url.

For me it is not clear where to put my pool and wallet address in options.ccp



## lolcocks123 | 2017-09-11T14:18:34+00:00
Edit: Thank you @xmrig for the response, I integrated the pool url and wallet address into my miner.

I was wondering if it is also possible to include a fail over address into the same?

## Valke88 | 2017-09-11T19:22:54+00:00
@lolcocks123 how do you integrate wallet and pool url? Can you post it here?

Thanks

## xmrig | 2017-09-11T19:37:08+00:00
The line need changed to something like that:
```cpp
m_pools.push_back(new Url("pool.example.com", 3333, "WALLET", "PASSWORD"));
```

@lolcocks123 yep just add more lines, it supports multiple failover pools. 

## Valke88 | 2017-09-11T19:40:00+00:00
It's working thx

## lolcocks123 | 2017-09-12T02:10:26+00:00
Thank you again @xmrig.

I will surely give you a nice donation once I have enough. :)

## hi0x0 | 2018-01-19T05:05:00+00:00
chinaes:
请问：是把m_pools.push_back(new Url("pool.example.com", 3333, "WALLET", "PASSWORD")); 替换到 https://github.com/xmrig/xmrig/blob/master/src/Options.cpp#L204 吗？

就像是这样：

    return algo_names[m_algo];
}

m_pools.push_back(new Url("pool.example.com", 3333, "WALLET", "PASSWORD"));
Options::Options(int argc, char **argv) :
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

但是无法编译，请问具体应该如何修改？

# Action History
- Created by: Likelym | 2017-09-06T04:56:25+00:00
- Closed at: 2017-09-19T08:08:27+00:00
