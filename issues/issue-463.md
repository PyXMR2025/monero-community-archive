---
title: Issue with 32bit build.
source_url: https://github.com/xmrig/xmrig/issues/463
author: Gill1000
assignees: []
labels: []
created_at: '2018-03-20T05:51:03+00:00'
updated_at: '2018-11-05T13:00:03+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:00:03+00:00'
---

# Original Description
I m using mingw 32 bit version with both xmrig-deps2.1and 3 result is same.. and building 32bit xmrig successfully...actually my 32bit xmrig automatically closed after few seconds  (and i m mining with minergate )without any showing error...i m using 64bit 8.1window and i have also tested this in 32bit win7 in virtualbox.....any idea what the heck Is this...?

# Discussion History
## xmrig | 2018-03-20T06:25:54+00:00
Please provide all possible information:

1. What do you use for compile MSYS2 or MSVC and versions.
2. Official 32 bit build is crashed too or not.
3. What CPU used.
4. All command line parameters or config file (without your email of course)

Thank you.

## Gill1000 | 2018-03-20T14:56:10+00:00
I m using msys2
official 32 bit not crashing working normally
cpu i3 4130
and here comes tricky part it does not exiting when i m mining with nicehash ......exiting when mining with minergate....i guess there is something with minergate..
my command line 
m_background(false),
    m_colors(true),
    m_doubleHash(false),
    m_dryRun(false),
    m_hugePages(true),
    m_ready(false),
    m_safe(true),
    m_syslog(false),
    m_apiToken(nullptr),
    m_apiWorkerId(nullptr),
    m_logFile(nullptr),
    m_userAgent(nullptr),
    m_algo(0),
    m_algoVariant(0),
    m_apiPort(0),
    m_donateLevel(kDonateLevel),
    m_maxCpuUsage(35),
    m_printTime(1),
    m_priority(-1),
    m_retries(99),
    m_retryPause(10),
    m_threads(1),
    m_affinity(-1L)

   // m_pools.push_back(new Url("xmr.pool.minergate.com", 45560, "lxxx@xxx.com", "x"));
    
  m_pools.push_back(new Url("cryptonight.in.nicehash.com", 3355, 
  "1d6h34xh743x4h38rtjwkKpBbD", "x"));


and another thing is that 64 bit xmrig running normal with minergate ...only  32bit xmrig.exe give problem with minergate


## Gill1000 | 2018-03-20T14:58:44+00:00
how to enable keepalive option in source code only..??

## xmrig | 2018-03-21T00:50:15+00:00
Check constructor of Url https://github.com/xmrig/xmrig/blob/master/src/net/Url.cpp#L79 keepalive can simple enabled, but both minergate.com and nicehash.com not support it.

## Gill1000 | 2018-03-21T07:45:40+00:00
Then still i dont understand why is this with minergate..........anyone other facing this issue..??

## Gill1000 | 2018-03-24T15:36:29+00:00
few days of testing..now 32bit build automatically exited after 20-30 sec...now with everypool it exited...earlier i was wrong about only minergate!! 

## Marcus-Vittek-Haakan | 2018-03-31T16:37:28+00:00
@Gill1000 I'm looking forward to do the same thing as you do. Any way you can contact me?

## Gill1000 | 2018-04-01T03:19:41+00:00
How..?? And
I have solved this issue by re-installing window and re-install msys2 too.. hope this will work for those who are looking..
I will close this issue in a day.!!

# Action History
- Created by: Gill1000 | 2018-03-20T05:51:03+00:00
- Closed at: 2018-11-05T13:00:03+00:00
