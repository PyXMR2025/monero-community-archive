---
title: Low hash rate?
source_url: https://github.com/xmrig/xmrig/issues/84
author: lolcocks123
assignees: []
labels: []
created_at: '2017-09-02T18:05:25+00:00'
updated_at: '2017-09-08T13:48:21+00:00'
type: issue
status: closed
closed_at: '2017-09-08T13:48:21+00:00'
---

# Original Description
Hello,

I am using XMRig with AMD FX-8350.

Sadly I am getting a hash rate of only 90 H/s on the 64 bit variant and 40 H/s on the 32 bit variant.
Using 6 out 8 threads.

Anyone has any idea why?

# Discussion History
## frotunato | 2017-09-02T18:17:57+00:00
That CPU appears to have 8MB of L3 cache, and the algorithm to mine requires 2MB of L3 cache per thread. 

<strike>You should be using 4 threads, otherwise you will encounter poor performance.</strike>

## xmrig | 2017-09-03T02:09:50+00:00
1. What operation system? Windows/Linux, 32 bit version always slower.
2. Is hugepages enabled?
3. On same PC works other cache intensive tasks like video playback?
4. Try set proper cpu affinity, 95 for 6 threads or 255 for 8

@frotunato It's ok, this CPU can run 8 threads, for AMD FX works rule L2 + L3, so it has 16 MB cache, but affinity is very important.

## lolcocks123 | 2017-09-03T05:55:26+00:00
Okay, this has become an different issue altogether.

I was trying it with my build of xmrig, build with Visual Studio 2017.
If I use your build from the releases, xmrig gives me 150 hash rate with 32 bit version and 250 using 64 bit version.

So the problem is probably on my side.
But I don't get what is wrong exactly. I didn't change your code one bit and directly built it.

Strange.

## xmrig | 2017-09-03T05:59:28+00:00
Probably you don't change Debug build to Release.

## lolcocks123 | 2017-09-03T07:58:36+00:00
![release 1](https://user-images.githubusercontent.com/16006564/30001429-adc60264-90ab-11e7-9fe6-0cd01328d8eb.png)

![release 2](https://user-images.githubusercontent.com/16006564/30001430-b7b40244-90ab-11e7-94e4-cf7668530d57.png)

Build fails if I switch to Release.


EDIT:
https://github.com/xmrig/xmrig-deps/releases
Using these by the way.

## xmrig | 2017-09-08T13:48:21+00:00
You need update dependencies, related issue with more details #101 

# Action History
- Created by: lolcocks123 | 2017-09-02T18:05:25+00:00
- Closed at: 2017-09-08T13:48:21+00:00
