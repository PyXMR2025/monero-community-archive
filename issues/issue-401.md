---
title: Payment ID stuff
source_url: https://github.com/monero-project/monero-gui/issues/401
author: Gingeropolous
assignees: []
labels:
- wontfix
created_at: '2017-01-14T15:32:25+00:00'
updated_at: '2018-03-30T02:54:20+00:00'
type: issue
status: closed
closed_at: '2018-03-30T02:54:20+00:00'
---

# Original Description
copied from reddit:

https://www.reddit.com/r/Monero/comments/5n1d3e/help_safedicecom_gamble_site_does_not_let_me/dceyzhh/

there seems to be a mismatch between the official Monero walllet (at least the GUI one) and the Monero documentation (which the Monero eco-system builds on).

The GUI wallet produces an 8 byte (16 hex digits) PID that can be conveniently copied to clipboard with the corresponding button in the GUI (next to the "Generate" button), whereas parts of the Monero eco-system appear to expect 32 byte (64 hex digits) PIDs and don't accept shorter ones, see this thread!

What is your view?

    Should the GUI wallet (once it leaves the beta stage) produce 64-hex-digit PIDs (at least as an option next to the 16-digit version)?

    Or do you consider all fine on Monero's side and you consider the eco-system (web sites etc.) have to be able to accept 16-hex-digit PIDs?

At least, "https://getmonero.org/knowledge-base/moneropedia/paymentid" describes both PID formats and seems to describe the 64-digit PIDs as the default for non-integrated PIDs, so it is no surprise that the eco-system's implementations are built on top of this information. On the other hand, the Monero GUI only supports the 16-digit PIDs, so the normal user (like myself) naturally uses these 16-digit PIDs which then won't be accepted by the "eco-system" (=web-site(s)).

So I think part of the problem that has occurred here and is documented in this thread is due to this "inconsistency" on Monero's side.

I am highlighting this to you to avoid that more of these annoyances happen as Monero adoption grows, which can be expected especially with the GUI wallet, and so I want to give you this user feedback which you probably would not have noticed by yourself, because for you as "deep experts" many things are obvious that cannot be expected to be taken for granted by the "casual user".

(Please forward this to other devs whose user name I am not aware of)

# Discussion History
## ghost | 2017-02-01T23:54:08+00:00
I just want to add my vote that we focus on one standard and stick to it.

## doobilydo | 2017-08-22T20:46:54+00:00
One standard is obviously the better idea, but accepting (and generating) both 16 and 64 digit IDs is the best solution for now. Poloniex appears to not support 16 digit IDs (last I tried). That `openssl rand -hex 32` stuff is not going to fly for layman users.

Consistency definitely needs to happen.

## sanderfoobar | 2018-03-30T01:54:43+00:00
Payment ID's are currently being phased out - I think I'm going to close this one.

## sanderfoobar | 2018-03-30T01:55:09+00:00
+wontfix

# Action History
- Created by: Gingeropolous | 2017-01-14T15:32:25+00:00
- Closed at: 2018-03-30T02:54:20+00:00
