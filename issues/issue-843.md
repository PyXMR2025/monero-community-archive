---
title: Need review of restricted/nonrestricted apis
source_url: https://github.com/monero-project/monero/issues/843
author: iamsmooth
assignees: []
labels:
- enhancement
created_at: '2016-05-16T03:07:23+00:00'
updated_at: '2018-01-08T12:48:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
#840 restricts setbans and flush_txpool which is good but I would also restrict getbans and get_connections since these allow mapping the network which facilitates isolation attacks.

Some of the information in getinfo is clearly useful (top block hash, etc.) but other information similar to the above such as the peer connection counts should probably not be public. This would require breaking up getinfo into public and private info, or allowing the restricted flag to change the behavior of a single request (currently I believe it only allows/denies entire requests).


# Discussion History
## osensei | 2016-05-16T15:44:54+00:00
I also think getbans and get_connections should be restricted, I didn't block them in #840 because I wasn't sure if they had been left unrestricted for some reason. I only restricted setbans and flush_txpool because it was pretty clear to me that those had to be restricted as they were allowing anyone to affect the behavior of your node.


## osensei | 2016-05-16T16:01:29+00:00
I just pushed a commit to my branch where I'm also restricting getbans and get_connections. 
I didn't know that it was automatically added to the same pull request, I'm new to github.


## osensei | 2016-05-16T21:23:50+00:00
What about getblocktemplate and submitblock? Should they be allowed?


## iamsmooth | 2016-05-17T20:18:05+00:00
Reasonable to introduce a new run time flag whether a node operator wants to allow mining or not. I'd suggest on by default. There's nothing dangerous about it, but it may introduce unwanted load.


## iamsmooth | 2016-05-17T20:18:40+00:00
Partially addressed by #840 


## dEBRUYNE-1 | 2018-01-08T12:43:18+00:00
+enhancement

# Action History
- Created by: iamsmooth | 2016-05-16T03:07:23+00:00
