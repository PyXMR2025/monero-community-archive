---
title: Cannot Restore Deterministic Wallet from Seed Using latest build
source_url: https://github.com/monero-project/monero/issues/3025
author: phloatingman
assignees: []
labels: []
created_at: '2017-12-29T03:52:08+00:00'
updated_at: '2018-01-03T00:50:38+00:00'
type: issue
status: closed
closed_at: '2018-01-03T00:50:38+00:00'
---

# Original Description
I'm running Ubuntu Mate 16.04.3 64-bit

After I build, this is the version of the CLI wallet
Monero 'Helium Hydra' (v0.11.1.0-master-a0a8706)

After I run, this command.. I am able to input the seed, but it just hangs forever and I have to Ctrl+c to quit

./monero-wallet-cli --log-level 4 --restore-deterministic-wallet

Here is the log file...
https://gist.github.com/phloatingman/376a3edb2c3ad8e2499d00bce80f47cc

Here is a screenshot of my terminal session...
https://i.imgur.com/PdLDCXd.png

# Discussion History
## stoffu | 2017-12-29T07:20:08+00:00
I can't reproduce this on Mac. Restoring wallet from seed is such a frequently used tool that this bug is likely specific to Ubuntu Mate (or possibly also to a few other platforms).

## phloatingman | 2017-12-29T09:20:30+00:00
Thanks for looking into it...

Hmmmm..  I just tried on Antergos an Arch based OS and it still would hang on restoring from seed and I needed to ctrl+c out of it.. screenshot..

https://i.imgur.com/U1Vjsmk.png

## moneromooo-monero | 2017-12-29T10:53:22+00:00
Possibly it's prompting for a password and the prompt is getting buffered. Try pressing enter when it looks blocked.

## phloatingman | 2017-12-29T11:08:17+00:00
You're right!  I just had to press enter a second time, then it asks for a password and continues as expected...

screenshot...
https://i.imgur.com/rSpIrXz.png

Thanks for checking it out!  A bit confusing for an end user having to press enter twice though...


## moneromooo-monero | 2017-12-29T14:23:25+00:00
<s>Does https://github.com/monero-project/monero/pull/2960/files help ?
(and I hope it's a test seed since it's public now)</s>

<s>Nevermind, probably doesn't.</s>

Actually, it should :)

## phloatingman | 2017-12-30T02:56:42+00:00
Sorry, I'm a bit new to git.. do I build after running this command to see if 2960 works?

git clone -b ms-next https://github.com/moneromooo-monero/bitmonero



## moneromooo-monero | 2017-12-30T10:53:55+00:00
Yes, you could do that.

## phloatingman | 2018-01-03T00:50:38+00:00
Restoring from seed seems to work correctly using that branch. Thanks!

# Action History
- Created by: phloatingman | 2017-12-29T03:52:08+00:00
- Closed at: 2018-01-03T00:50:38+00:00
