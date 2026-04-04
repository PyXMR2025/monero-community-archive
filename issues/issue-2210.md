---
title: Very small wording change on 'Send' page.
source_url: https://github.com/monero-project/monero-gui/issues/2210
author: ghost
assignees: []
labels: []
created_at: '2019-06-11T09:20:49+00:00'
updated_at: '2019-11-12T10:41:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![image](https://user-images.githubusercontent.com/46682965/59259348-f13f6900-8c39-11e9-82b7-43b3a7c191a8.png)
Rephrase to **"Sending not possible while daemon is synchronizing."** so that it doesn't look like a general status message. Because general status messages shouldn't be shown on the `Send` page only.


# Discussion History
## ghost | 2019-08-30T19:10:37+00:00
Updated.

## rating89us | 2019-11-12T09:38:10+00:00
Why not use "wallet" instead of "daemon"?

## ghost | 2019-11-12T09:55:34+00:00
> Why not use "wallet" instead of "daemon"?

That would be super super nice. The word "daemon" needs to die in the GUI. It just needs wording changes on so many other pages, too, in order to be coherent. 

I mean the daemon is something nobody ever sees! Just no point to bother the user with some a technical details. It's more than enough to tell him something like "blockchain is syncing in the background" or not. But the user just doesn't have to be bothered with a technical term like "daemon".

## rating89us | 2019-11-12T10:41:07+00:00
- Simple mode: "wallet"
- Advanced mode: "daemon"

# Action History
- Created by: ghost | 2019-06-11T09:20:49+00:00
