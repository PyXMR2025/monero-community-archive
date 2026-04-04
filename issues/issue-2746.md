---
title: problem with display coin at new wallet
source_url: https://github.com/monero-project/monero/issues/2746
author: mraksoll4
assignees: []
labels: []
created_at: '2017-11-02T16:39:01+00:00'
updated_at: '2017-11-04T00:19:08+00:00'
type: issue
status: closed
closed_at: '2017-11-04T00:19:08+00:00'
---

# Original Description
When i create new wallet and mine , or send to them money it's not display balance and tx.

Only if i restore it from seed/key's or use  set refresh-from-block-height 0

it's start display tx balance , i use latest release. 

I compile it from sources.

# Discussion History
## moneromooo-monero | 2017-11-02T18:36:50+00:00
Did you create the wallet with a previous release ?

## mraksoll4 | 2017-11-02T20:52:57+00:00
i create it at new release .  I think problem is at refresh fuction when create new wallet. For some reason it's not download tx data from daemon before use "set refresh-from-block-height 0"
simple refresh not work.

## moneromooo-monero | 2017-11-02T23:47:55+00:00
What is the value of refresh-from-block-height before you set it to 0 ?

## mraksoll4 | 2017-11-03T16:15:46+00:00
how i can see it  , i dont see this info at log's?

## moneromooo-monero | 2017-11-03T16:25:27+00:00
If you type "set", it will display it.

## ghost | 2017-11-03T17:51:14+00:00
refresh-from-block-height = 1413083

## moneromooo-monero | 2017-11-03T18:53:12+00:00
That looks right. You'll have to supply a log (run the wallet with --log-level 2, and paste on fpaste.org or pastebin.mozilla.org) showing the bug happening.


# Action History
- Created by: mraksoll4 | 2017-11-02T16:39:01+00:00
- Closed at: 2017-11-04T00:19:08+00:00
