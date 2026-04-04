---
title: Crash after long inactivity and then unable to start
source_url: https://github.com/monero-project/monero-gui/issues/92
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-10-30T00:06:05+00:00'
updated_at: '2016-11-05T09:43:34+00:00'
type: issue
status: closed
closed_at: '2016-10-30T13:50:48+00:00'
---

# Original Description
Recently compiled on Ubuntu 16. Set things up for a remote node, and then created a new wallet. Let it sit there open for ... maybe an hour? Came back to the Ubuntu application-greyed-out effect, which means that the program has crashed (or becomes unresponsive). Oddly enough, it still seemed to be in `top` but then disappeared without me killing it. 

Tried to reload - entered my password, (in a box which is totally not scaled right - I have to use my mouse to make the box bigger) but got this: 

`Couldn't open wallet: Genesis block missmatch. You probably use wallet without testnet flag with blockchain from test network or vice versa`

I assume this has something to do with using a remote node.

And even if I cancel to try and get out of this dialogue, nothing in the program is responsive - so I can't "recover" the program by putting in a local node or something. 

Also, I loathe disappearing top menu bars. But thats just me I think. 


# Discussion History
## dEBRUYNE-1 | 2016-10-30T09:37:42+00:00
> (in a box which is totally not scaled right - I have to use my mouse to make the box bigger) but got this:

This is issue #86. Only happens on Linux somehow. 

> `Couldn't open wallet: Genesis block missmatch. You probably use wallet without testnet flag with blockchain from test network or vice versa`

This is fixed by @hyc [here](https://github.com/monero-project/monero/pull/1266). 


## Gingeropolous | 2016-10-30T13:50:48+00:00
Then I will close my issue. I am an issue closing wizard. 


## Jaqueeee | 2016-11-05T09:32:44+00:00
@Gingeropolous 
https://github.com/monero-project/monero/pull/1266 didn't get merged.
But this issue was hopefully fixed in https://github.com/monero-project/monero-core/pull/90 instead.
Can you still reproduce this error on monero-core master? Please delete the old wallet and create/restore a new one before you test. 


# Action History
- Created by: Gingeropolous | 2016-10-30T00:06:05+00:00
- Closed at: 2016-10-30T13:50:48+00:00
