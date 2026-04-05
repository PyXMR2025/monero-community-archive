---
title: Feature request - Exit xmrig on connection errors.
source_url: https://github.com/xmrig/xmrig/issues/391
author: Yorper
assignees: []
labels:
- wontfix
created_at: '2018-02-07T20:47:48+00:00'
updated_at: '2018-11-05T12:49:01+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:49:01+00:00'
---

# Original Description
Would it please be possible to add a switch that would cause the application to exit after "X" failed reconnection attempts?

The reason i ask for this is that i have a mining setup that switches based on profit, but it does this by closing ports and opening others for the next coin.

I want to use this miner for the XMR portion of the script as in my testing it appears to be the most superior. Right now i'm using ccminer as xmrig doesnt have, to my knowledge the ability to do this.

This would be done by passing a switch something like this "-exit 3" for 3 failed connections then exiting.

So just to be clear, this is the type of thing i mean.

   IF 
       primary stratum server does not respond/connection refused/bad log in credentials.
   THEN
       exit xmrig
   END 

Thanks.

# Discussion History
# Action History
- Created by: Yorper | 2018-02-07T20:47:48+00:00
- Closed at: 2018-11-05T12:49:01+00:00
