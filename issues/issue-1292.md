---
title: 'Bug with CLI wallet: Amounts get contaminated after deleting long multi-row
  texts wrapping around'
source_url: https://github.com/monero-project/monero/issues/1292
author: kenshi84
assignees: []
labels: []
created_at: '2016-11-03T03:31:03+00:00'
updated_at: '2016-11-06T06:08:13+00:00'
type: issue
status: closed
closed_at: '2016-11-06T05:40:20+00:00'
---

# Original Description
Operating System: OS X El Capitan 10.11.6 (15G1108)

I found this bug when I intended to send to multiple addresses and forgot to insert a space between the amount and the next address, so I had to delete the long multi-row text and give the correct syntax again.

Generally, the CLI wallet (or the Terminal itself?) seems to get confused when a long string spanning multiple lines gets erased, apparently leaving some dust.

https://youtu.be/PA-UcIIUx_8

I figured out that if I pasted the address N times after the amount which are then removed, the first N characters of the address get appended to the amount:

https://youtu.be/xRY3mZ9_iqM

Just to be safe with this kind of potential unknown bugs, I'd like the transfer confirmation dialogue to also show the total output amount.

# Discussion History
## moneromooo-monero | 2016-11-03T19:21:33+00:00
Terminal bug, I think. You deleted one less character than you thought. Try counting the characters you delete by pressing the backspace key once at a time, with a monero key being 95 chars long, and we'll be sure which it is. In any case, monero just uses std::getline, it doesn't do anything with editing.


## kenshi84 | 2016-11-04T05:50:14+00:00
You're right, it's Terminal bug:

https://youtu.be/AfvTFABVs60

Can we (most likely, you :D) do something about it, to save Mac users from disaster?
(I guess confirming the total outgoing amount would be at least a nice & simple safeguard.)


## moneromooo-monero | 2016-11-04T09:31:32+00:00
That's easy to add, yes. Someone recently made the prompt to be default behavior, so the amount(s) can be added there. Can you open a new bug for this, for clarity ?


## kenshi84 | 2016-11-05T09:46:04+00:00
OK, I'll open it. Would it be still possible to deal with this Mac specific bug? Or should this issue ne closed?


## moneromooo-monero | 2016-11-05T15:33:42+00:00
You'd report the bug against the terminal you're using. Would be nice if you could repro with just a minimal program that uses std::getline.


## kenshi84 | 2016-11-06T05:40:20+00:00
OK, I'll try to report this bug to Apple.


## kenshi84 | 2016-11-06T06:08:13+00:00
FYI, I could reproduce the bug with this minimal code:
http://ideone.com/oojpE0

Apple's bug report system is down at the moment... maybe I should switch to Linux:)


# Action History
- Created by: kenshi84 | 2016-11-03T03:31:03+00:00
- Closed at: 2016-11-06T05:40:20+00:00
