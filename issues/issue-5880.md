---
title: deamon synced OK, no blocks warning persists
source_url: https://github.com/monero-project/monero/issues/5880
author: DanielBullimore
assignees: []
labels: []
created_at: '2019-09-04T02:26:58+00:00'
updated_at: '2019-09-05T02:24:03+00:00'
type: issue
status: closed
closed_at: '2019-09-05T02:24:03+00:00'
---

# Original Description
So I have read through all bug label issues. This one isn't there. (some other label?)

Running release 14.1.0 monerod.exe... windows 10

Looks like daemon is sending warning message every two minutes when it should send new top block message. See attached image.
Has been doing this for days. Recently removed --public_node as a result daemon has stopped claiming to be off-line.  Yet still sends 'no blocks in 90' error. 

no probs getting in and out peers
rpc works fine have sent and received funds

![Untitled](https://user-images.githubusercontent.com/50190195/64220585-00267680-cf1e-11e9-98aa-b8b41eec108a.png)

Is this a known/patched bug? I don't want to waste time debugging for a pull request that has been resolved.

# Discussion History
## moneromooo-monero | 2019-09-04T10:56:47+00:00
It is not a known bug. Is your computer time off ?

## DanielBullimore | 2019-09-05T02:24:03+00:00
Oh my you were not even kidding. monerod.exe uses system clock. My servers clock had inverse am/pm. Fresh install on a built for purpose machine and not setting the clock messed me up.
Hopefully the next person can read this and _quickly_ solve.
Thanks moneromooo-monero your a total asset to this project.



# Action History
- Created by: DanielBullimore | 2019-09-04T02:26:58+00:00
- Closed at: 2019-09-05T02:24:03+00:00
