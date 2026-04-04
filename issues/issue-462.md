---
title: '"Unlocked balance ~20 minutes" message even though there is no incoming tx'
source_url: https://github.com/monero-project/monero-gui/issues/462
author: ghost
assignees: []
labels: []
created_at: '2017-02-05T17:46:31+00:00'
updated_at: '2017-02-28T04:52:57+00:00'
type: issue
status: closed
closed_at: '2017-02-28T04:52:57+00:00'
---

# Original Description
Shouldn't the "unlocked balance" timer only be working if there are incoming/outgoing tx that haven't confirmed? Right now I have a testwallet that has no incoming/outgoing tx and yet it still shows this message.

![tx](https://cloud.githubusercontent.com/assets/21302237/22628385/1c60c8ae-eba1-11e6-8f22-f3837ffd667b.png)


# Discussion History
## ghost | 2017-02-05T18:54:28+00:00
This message went away. I think I figured out where it came from.

Before I opened the GUI, I had just sent a transaction from the CLI. Like, I closed the CLI about 2 seconds after the payment ID appeared on my screen, and immediately opened the GUI. So for some reason the GUI had picked up the CLI transaction that had just been sent?

## Jaqueeee | 2017-02-05T18:56:45+00:00
Yes, that would make sense if you opened the same wallet with GUI. GUI scans mempool continuously.  

## ghost | 2017-02-05T19:43:42+00:00
There's what's weird. I didn't open the same wallet. It was a GUI test wallet unrelated to the CLI tx I had just sent

## Jaqueeee | 2017-02-05T19:45:59+00:00
That's really weird. Let me know if you can reproduce it. 

## ghost | 2017-02-28T04:52:57+00:00
I'm just going to close this. I'll reopen it if the issue pops up again.

# Action History
- Created by: ghost | 2017-02-05T17:46:31+00:00
- Closed at: 2017-02-28T04:52:57+00:00
