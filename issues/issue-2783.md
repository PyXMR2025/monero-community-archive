---
title: --cpu-max-threads-hint has no effect on Ghostrider
source_url: https://github.com/xmrig/xmrig/issues/2783
author: Phosphor2pt4
assignees: []
labels: []
created_at: '2021-12-03T16:52:54+00:00'
updated_at: '2021-12-03T19:47:42+00:00'
type: issue
status: closed
closed_at: '2021-12-03T18:42:52+00:00'
---

# Original Description
**Describe the bug**
I am attempting to use XMRig on only 10 of my 12 available threads. "--cpu-max-threads-hint" seems to have no effect on ghostrider specifically.

**To Reproduce**
Attempt to use "rtm_ghostrider_example.cmd" with command line option --cpu-max-threads-hint=83.

**Expected behavior**
I was expecting XMRig to mine on only 10 of my 12 available threads. 83 was the closest integer to 10/12.

**Required data**
![image](https://user-images.githubusercontent.com/43998628/144640188-03dc718c-a62a-4399-a499-7ad1ce9cf8c6.png)
![image](https://user-images.githubusercontent.com/43998628/144641083-5b6529fc-5066-4216-ab3d-8cc484c93f18.png)


**Additional context**
I have read that it would be better to use the config.json instead of command line options to achieve my desired result. That does not seem to work for ghostrider, either. I know that the command line option only works when there is not an already existing profile in the config.json. I did indeed ensure that there was no ghostrider profile in my config.json when I was initially trying to use the command line option. After discovering that my desired result did not occur, I tried to use config.json to define the threads, like this: 
![image](https://user-images.githubusercontent.com/43998628/144640617-a540885e-e79d-472c-8fff-b8ac880e3713.png)
This still has no effect. No matter what, XMRig always runs on all threads with cpu usage maxed out. Am I just fundamentally not understanding something here?

# Discussion History
## Spudz76 | 2021-12-03T17:52:00+00:00
Try putting it last on the cmdline instead of first.  Someone else said the `--cpu-priority` wasn't working unless it was after all the pool and algo stuff.

Also max-threads-hint doesn't do anything if there is already a thread definition in config.json.  It is a hint for the autoconfigurator which does not run at all if there is already a thread configuration.

## Phosphor2pt4 | 2021-12-03T18:03:42+00:00
I did ensure that there were no existing definitions when running the command line option initially. The above screenshots which show the config.json were taken after I tried using that when --cpu-max-threads-hint didn't work initially. I have now removed the definitions again, and also placed --cpu-max-threads-hint at the end of my command line. Unfortunately the result is the same, runs on all 12 threads.

## SChernykh | 2021-12-03T18:18:13+00:00
Can you try values below 50, for example 40?

## Phosphor2pt4 | 2021-12-03T18:42:33+00:00
> Can you try values below 50, for example 40?

Thank you so much, this worked! When I enter --max-cpu-threads-hint=40 it does indeed run on only 10 threads. 
![image](https://user-images.githubusercontent.com/43998628/144655615-8b68dad3-8610-47b3-a0ac-c7a40c7774e2.png)


## Spudz76 | 2021-12-03T19:47:04+00:00
That was my other suspicion but I forgot to mention it.  The percentage is in total threads available, not cores.  So half of 83 means "83% of all cores" when each core is two "processor units".

Same as how 100% load on all cores (not threads) leads to "50%" usage total.

# Action History
- Created by: Phosphor2pt4 | 2021-12-03T16:52:54+00:00
- Closed at: 2021-12-03T18:42:52+00:00
