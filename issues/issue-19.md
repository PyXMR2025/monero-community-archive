---
title: New version hashrate drop
source_url: https://github.com/xmrig/xmrig/issues/19
author: niko1094
assignees: []
labels: []
created_at: '2017-06-20T03:46:28+00:00'
updated_at: '2017-06-20T18:43:35+00:00'
type: issue
status: closed
closed_at: '2017-06-20T18:43:35+00:00'
---

# Original Description
Hi. 
In 0.8.2 version, I had an avg of 236 h/s. Now with 1.0.1-msvc-win64 version, I have an avg of 230 h/s and with 1.0.1-gcc-win64 version I have an avg of 234.4 h/s.

I have windows 10 x64 and i5-3570.

Anyway, thank you very much: D

# Discussion History
## xmrig | 2017-06-20T09:47:07+00:00
Old version calc 60 hashes at one single loop, this solution has old history, but not so good for slow hashes like cryptonight, because if new job received, miner not immediately stop previous job.

In new version this situation impossibility, outdated job newer be mined. But these checks can costs few H/s.

Of course I will try any way to increase hashrate in future.
Thank you.

## niko1094 | 2017-06-20T17:02:47+00:00
Ah, okay. No problem.
One more question, you recommend msvc version for win64. Do you know why I have less hashes than with the gcc version?

msvc  ->  230 h/s
gcc     ->  234.4 h/s


## xmrig | 2017-06-20T17:13:00+00:00
In my tests and user feedback msvc little bit faster. But difference is very small, so there 2 versions.
I remove this recommendation.

Maybe gcc version better for your CPU, maybe some background tasks reduce performance.

## niko1094 | 2017-06-20T17:18:53+00:00
Okay :D
Very thanks you for your work and your attention.

# Action History
- Created by: niko1094 | 2017-06-20T03:46:28+00:00
- Closed at: 2017-06-20T18:43:35+00:00
