---
title: XmRig don't open
source_url: https://github.com/xmrig/xmrig/issues/2336
author: samjviana
assignees: []
labels: []
created_at: '2021-05-01T17:48:00+00:00'
updated_at: '2021-05-03T19:01:42+00:00'
type: issue
status: closed
closed_at: '2021-05-03T12:41:45+00:00'
---

# Original Description
I'm trying to configure two low end processor to mine with XmRig, one is intel core i3-4170 and an i7-4770k. The thing is that xmrig start and closes and don't even show any error messages. Even using "xmrig.exe --help" the help message don't show up. Funny thing, I have another machine with an i3-4170 that is working fine. 
How can I see the cause of the error.

# Discussion History
## Spudz76 | 2021-05-02T05:09:35+00:00
Likely some antivirus garbage, set your miner folder to whitelisted in everything.

## samjviana | 2021-05-03T12:41:45+00:00
After some testing i found out that the it was the firewall that was blocking the miner, silly me lol.
thanks anyway.

## Spudz76 | 2021-05-03T19:01:42+00:00
Also running a command prompt and running xmrig (or your launcher bat file) from there will avoid the window just closing...

# Action History
- Created by: samjviana | 2021-05-01T17:48:00+00:00
- Closed at: 2021-05-03T12:41:45+00:00
