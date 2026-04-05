---
title: 'rejected: "Low difficulty share" issue'
source_url: https://github.com/xmrig/xmrig/issues/123
author: maverickl-0813
assignees: []
labels: []
created_at: '2017-09-27T14:34:01+00:00'
updated_at: '2018-03-08T17:34:59+00:00'
type: issue
status: closed
closed_at: '2017-09-30T11:46:38+00:00'
---

# Original Description
Hi,
I encountered a problem while tuning the configuration with trying cryptonight-lite as the working algorithm. 
While the hash rate goes really sky high in a sudden, the pool returns "Low difficulty share" and reject all my results.
Can't be sure what caused the problem, and here's the details I can provide here:

**CPU: Intel i5-4460 (6MB L3 cache), not overclocked.**
Configuration:
{
    **"algo": "cryptonight-lite",
    "av": 2,**
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 1,
    "log-file": null,
    "max-cpu-usage": 50,
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "syslog": false,
    **"threads": 2,**
...
}

Before this configuration, I use Cryptonight / av:0 as the values and everything else is the same (using 2 threads for power saving), and it gives me about **130 hash/s**.
Using this configuration my hashrate rocks to **480 hash/s** and above, but the results are failing.

Would anyone please explain what is going on? I think the cache usage is alright according to the document. 
And what exactly does the "Low difficulty share" means? Is there any materials I can read and dig into?

Thanks, and this mining tool is great :)

# Discussion History
## xmrig | 2017-09-27T17:41:39+00:00
cryptonight-lite it special variation of cryptonight algorithm, theoretically it can be up to 4x faster, memory requirements and loop count reduced twice. Currently only one coin use this algo http://www.aeon.cash/ so you also need change your pool for use it. It not comparable with Monero.

"Low difficulty share" it pool error message means something wrong with your share, without specify what exactly wrong.
Thank you.

## maverickl-0813 | 2017-09-28T04:52:35+00:00
Thanks for the response and the info @xmrig, I realized the Cryptonight-lite is not used for mining Monero now.


## nwsm | 2017-12-16T16:41:16+00:00
Tip for anyone else getting this: be sure to change "algo" in config.json to "cryptonight-lite" for mining Aeon

This was my problem.

## Schepses | 2018-03-08T17:34:59+00:00
"cpu-priority": 2,  //0, 2, 5,
"max-cpu-usage": 75,
"threads": 4, // 0, 2, 4, 8........

# Action History
- Created by: maverickl-0813 | 2017-09-27T14:34:01+00:00
- Closed at: 2017-09-30T11:46:38+00:00
