---
title: Nothing print on console
source_url: https://github.com/xmrig/xmrig/issues/68
author: calvintam236
assignees: []
labels: []
created_at: '2017-08-21T18:47:00+00:00'
updated_at: '2017-08-27T04:48:44+00:00'
type: issue
status: closed
closed_at: '2017-08-27T04:48:44+00:00'
---

# Original Description
I made your binary into a [docker image](https://hub.docker.com/r/calvintam236/xmrig/). It has no problem printing logs on console on v2.2.1.

sample command: ```docker run -d --name cpu0_xmr calvintam236/xmrig -a cryptonight -o POOL_URL -u USERNAME --donate-level=1 --print-time=2 --max-cpu-usage=100 --cpu-affinity=0xAAAA```

I tried with and without ```--no-huge-pages```, same result.

Docker host is Ubuntu 16.04.3 with kernel 4.10.0-32-generic.

# Discussion History
## xmrig | 2017-08-21T19:21:41+00:00
Please checkout to **bug-68** branch, probably it helps. I add some debug printf in code, it little spam output, will looks like `uv_is_writable: 1, uv_guess_handle: 14` I need this line from your logs.
Im not familiar with docker containers, so can't do it by myself.
Thank you.

## calvintam236 | 2017-08-22T05:42:50+00:00
Thanks for getting back so fast. I used the binary in the release in the docker image. Tested on my macOS docker host as well, with same problem.
By building `bug-68` branch in the docker image and run it in my macOS docker host, it do have some console output (probably debug).

![screen shot 2017-08-21 at 10 41 08 pm](https://user-images.githubusercontent.com/6436149/29550299-eacec8e2-86c1-11e7-9fa3-6b9eeda1e050.png)



## xmrig | 2017-08-22T08:18:35+00:00
I fixed it in master branch.
Surprising console in docker not a true console it named pipe.
Thank you.

## calvintam236 | 2017-08-25T02:20:05+00:00
Thanks for fixing that. Are you planned to have a new release anytime soon?

## xmrig | 2017-08-25T11:24:59+00:00
It already in master branch or for docker need tagged release? I can create bugfix release later today.

## calvintam236 | 2017-08-25T19:00:13+00:00
it requires me to trigger the image build. Currently, I am using your binary release in the `Dockerfile` instead of compiling.

## xmrig | 2017-08-25T19:41:10+00:00
https://github.com/xmrig/xmrig/releases/tag/v2.3.1

## calvintam236 | 2017-08-27T04:48:44+00:00
Fix confirmed on v2.3.1. Thanks! :D

# Action History
- Created by: calvintam236 | 2017-08-21T18:47:00+00:00
- Closed at: 2017-08-27T04:48:44+00:00
