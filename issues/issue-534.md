---
title: PUT config
source_url: https://github.com/xmrig/xmrig/issues/534
author: cupertank
assignees: []
labels: []
created_at: '2018-04-10T13:57:34+00:00'
updated_at: '2018-07-02T05:42:22+00:00'
type: issue
status: closed
closed_at: '2018-04-15T06:52:49+00:00'
---

# Original Description
How does it work "PUT /1/config".
What you need to send in the request.

My Python code
>>> data = {'threads':4}
>>> put('http://127.0.0.1:3222/1/config', headers={'Authorization':'Bearer 123'}, data=data)
<Response [415]>

# Discussion History
## xmrig | 2018-04-10T14:43:04+00:00
Whole JSON config, for convenient, config can be obtained by `GET /1/config`. Please note this feature is not fully implemented and tested, only some base settings now can changed in runtime. This feature was first introduced in xmrig-proxy v2.5.
Thank you.

## cupertank | 2018-04-10T17:05:17+00:00
Does this function now work in 2.6.0?
"Added API endpoint PUT /1/config to update current config."
@xmrig 

## xmrig | 2018-04-10T17:07:35+00:00
It works, config can changed, but some major functions eg change pools or threads not work at this moment.
Thank you.

## cupertank | 2018-04-10T17:08:41+00:00
I wrote a bot to track the work of the miner and would like to add a functional change to the configuration of the miner using PUT /1/config, but I do not understand why I get the 415 error.
By the way, I wrote to you on the mail about the bot, but so I did not answer, maybe you'll fix it on your GitHub?
[Bot](https://t.me/Miner_checker_bot)


## cupertank | 2018-04-10T17:09:03+00:00
And what functions are available at the moment?
@xmrig 

# Action History
- Created by: cupertank | 2018-04-10T13:57:34+00:00
- Closed at: 2018-04-15T06:52:49+00:00
