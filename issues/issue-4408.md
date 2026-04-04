---
title: 'Couldn''t open wallet: invalid password.'
source_url: https://github.com/monero-project/monero-gui/issues/4408
author: dchmelik
assignees: []
labels: []
created_at: '2025-02-05T10:32:44+00:00'
updated_at: '2025-02-19T18:08:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Every time it says "Couldn't open wallet: invalid password" I enter my password, and it's valid.  When such fields say something (password, personal/contact information, username, etc.) is 'invalid' before even started/finished entering, it's possibly nasty; alarms/confuses some/lesser users: best wait until entered it and only give any error message afterwards.  Apparently there's a trend (all over World Wide Web) to analyse text boxes before anything is started/finished entering, and only disappear to tell user when they get it right, which is a bad (and lazy) practice, rather than not saying anything unless they get it wrong.

# Discussion History
## dchmelik | 2025-02-05T10:36:02+00:00
It's not an inquiry rather than comment on apparent new poor (but increasingly common) computer programming practice.

## selsta | 2025-02-05T10:37:11+00:00
This sounds like a bug, we do not "analyze" the entry before pressing enter and it should not say "invalid" beforehand.

## dchmelik | 2025-02-05T10:37:40+00:00
> This sounds like a bug, we do not "analyze" the entry before pressing enter and it should not say "invalid" beforehand.

Good.  Is there a way I should get a log?

## selsta | 2025-02-05T10:38:25+00:00
Which operating system are you using? How did you install monero-gui? Are you using a hardware wallet?

## dchmelik | 2025-02-05T10:43:48+00:00
Slackware 15 GNU/Linux (current 64-bit n86) always from official monero-gui GitHub's stable tag which currently points to [monero-gui-linux-x64-v0.18.3.4.tar.bz2](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.3.4.tar.bz2).  I decompress it into a directory/folder and run (the following way with my wrapper script).  I have no hardware wallet.  First time monero-gui maybe installed in KDE & XFCE 'other' menu (which that XFCE menu disappeared or I'd use that entry sometimes).
```
#!/bin/sh
cd /usr/local/lib64/monero-gui
exec /usr/local/lib64/monero-gui/monero-wallet-gui "$@"
```


## selsta | 2025-02-19T18:08:52+00:00
Can you try to start monero-wallet-gui from the command line and say how often it says 

```
2025-02-19 18:05:20.153	E !r. THROW EXCEPTION: error::invalid_password
2025-02-19 18:05:20.154	E Error opening wallet: invalid password
2025-02-19 18:05:20.157	E Error opening wallet with password:  invalid password
```

in the logs? Does it match with the amount of characters your password has?

# Action History
- Created by: dchmelik | 2025-02-05T10:32:44+00:00
