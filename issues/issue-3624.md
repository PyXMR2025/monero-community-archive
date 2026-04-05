---
title: cannot read MSR 0xc0011020
source_url: https://github.com/xmrig/xmrig/issues/3624
author: alpha754293
assignees: []
labels: []
created_at: '2025-01-27T20:16:25+00:00'
updated_at: '2025-06-28T10:25:25+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:25:25+00:00'
---

# Original Description
I am trying to run the xmrig benchmark on my Supermicro AMD Ryzen 9 7950X system (which has 128 GB of RAM installed, which as a result of all four DIMMs being populated, the RAM is stuck at DDR5-3600 speeds rather than either the 4800 or the 5600 speeds (I forget what the speed is actually supposed to be)).

It is running Debian 11 running 5.15.158 kernel.

I installed the `msr-tools` package and also ran the [randomx_boost.sh](https://raw.githubusercontent.com/xmrig/xmrig/refs/heads/master/scripts/randomx_boost.sh).

The error that I am getting now is: "cannot read MSR 0xc0011020"

[Here](https://i.postimg.cc/gjNK9sPH/Screenshot-2025-01-27-15-12-53.png) is the screenshot of it.

SVM has been disabled in the BIOS already.

I also tried to add the command line flag `--randomx-1gb-pages`, but that actually got a slightly lower hash rate than without it, so what you're seeing is the results without that command line flag.

When I ran the `randomx_boost.sh`, it said that it was able to set the MSR registers correctly for Zen4, so not really sure what's going on here.

If there are any suggestions of things that I can try -- your help is greatly appreciated.

# Discussion History
# Action History
- Created by: alpha754293 | 2025-01-27T20:16:25+00:00
- Closed at: 2025-06-28T10:25:25+00:00
