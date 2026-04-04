---
title: '[Feature Request] Start Daemon automatically if no .bitmonero dir found in
  $HOME.'
source_url: https://github.com/monero-project/monero-gui/issues/39
author: dternyak
assignees: []
labels: []
created_at: '2016-10-06T03:36:28+00:00'
updated_at: '2016-12-21T01:35:52+00:00'
type: issue
status: closed
closed_at: '2016-12-21T01:35:52+00:00'
---

# Original Description
Messing with CLI commands for most users is not user friendly.
Can we allow the daemon to be shipped with the GUI and optionally auto-started?


# Discussion History
## dternyak | 2016-10-06T07:29:25+00:00
Moving to mbg033, seems to be more active. 


## Jaqueeee | 2016-10-06T07:43:06+00:00
imo it makes sense to keep feature requests in main repo. 
To the issue. An option to start/stop daemon from GUI would definitely be good. Not sure if auto-start is a good option though. Also, daemon could be configured to use other dir than .bitmonero in $HOME. 

I'm suggesting the following scenario instead.
- Check if daemon is running with RPC call to configured daemon address.
- if not found, present option to start daemon from GUI or alternatively option to change daemon address. 

What's your thoughts on this?


## dternyak | 2016-10-06T08:18:58+00:00
Okay, I'll reopen it!

I think your suggested scenario solves the use case and adds a lot of value. Do you think this falls within scope of the initial release? 


## dternyak | 2016-10-07T06:16:29+00:00
@Jaqueeee I'm willing to put on a small bounty (lets say 15 XMR) on this feature if you feel its out of scope. Ideally, the GUI shouldn't have any requirement for running CLI commands, and I think this is a great step towards that. 


## Jaqueeee | 2016-10-10T14:06:53+00:00
@dternyak sorry, I missed your last comment. I agree that the GUI should be able to run by itself in the future. It will take some effort to make this work cross platform so on the initial beta release the user will have to start the daemon separately most likely. CLI skills isn't really needed. A click on the monerod binary will be enough afaik. 


## dternyak | 2016-10-10T20:25:49+00:00
@Jaqueeee Thanks for the discussion. I see your point about the cross-platform GUI adding some complexity to the build (I assume the daemon binary must be built for each platform as well).

I think this should be a high-priority feature after the beta.


## medusadigital | 2016-10-10T21:45:50+00:00
i agree with your view @dternyak about the priorization of that feature. once we have a stable GUI and some community feedback regarding performance, this should be addressed. nevertheless, for the first public beta, its unfortunately out of scope. 

how does big brother bitcoin do it? they also have a daemon i assume.


## Jaqueeee | 2016-12-19T19:20:32+00:00
Added in #217
Please close. 

## dternyak | 2016-12-21T01:35:52+00:00
nice work @Jaqueeee  :)

# Action History
- Created by: dternyak | 2016-10-06T03:36:28+00:00
- Closed at: 2016-12-21T01:35:52+00:00
