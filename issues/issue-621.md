---
title: Show desired fiat's value near XMR balance [+1]
source_url: https://github.com/monero-project/monero-gui/issues/621
author: scottAnselmo
assignees: []
labels:
- wontfix
created_at: '2017-03-27T21:39:51+00:00'
updated_at: '2018-03-30T02:36:19+00:00'
type: issue
status: closed
closed_at: '2018-03-30T02:36:19+00:00'
---

# Original Description
It would be nice to see the fiscal value of my XMR holdings (e.g. if holding 100 XMR and <XMR, USD> pairing is $20, it shows USD balance of $2,000)

Monero isn't particularly volatile so a re-sync of fiscal value of every 60 seconds should suffice although in the future advanced settings might allow configuring this. At the very least, fiscal currencies supported should be the primary currencies used in countries where the ~11 translated languages thus far are the primary language (e.g. English is the primary language in the US, Canada, Great Britain, etc and thus USD, CAD, GBP, etc should be supported)

# Discussion History
## dternyak | 2017-03-27T21:54:03+00:00
AFAIK, this would require a centralized source (API), that would provide such data. I don't think we should bake in network calls to any centralized source, so I don't think this issue should be implemented, as much as I agree it would be nice to see the fiat value of your balance. 

## ghost | 2017-03-27T23:51:03+00:00
I'm more ok with centralization on this issue, since pulling in the XMR/USD conversion has no effect upon the security or functionality of Monero. We could API into Bitfinex. I remember my Ethereum wallet displaying my balance in USD in parentheses, and it was really helpful.

## SamsungGalaxyPlayer | 2017-03-28T13:42:23+00:00
This could be one of the optional extensions for the GUI that we keep talking about.

## scottAnselmo | 2017-09-04T08:15:00+00:00
Did the idea of extensions die out? I haven't seen much of it as late.

## rex4539 | 2017-12-23T06:04:32+00:00
+1

## sanderfoobar | 2018-03-30T02:22:19+00:00
Having the GUI poll a centralized API as default behavior sounds like a bad idea and I strongly reject it.

However, I do like the idea of showing fiat in the GUI. I can't find any proposal for extensions, feel free to make one and refer to this issue. Closing for now though.

## sanderfoobar | 2018-03-30T02:26:11+00:00
+wontfix

# Action History
- Created by: scottAnselmo | 2017-03-27T21:39:51+00:00
- Closed at: 2018-03-30T02:36:19+00:00
