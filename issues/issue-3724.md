---
title: Monero Wallet GUI fails to detect already running monerod
source_url: https://github.com/monero-project/monero-gui/issues/3724
author: adrelanos
assignees: []
labels: []
created_at: '2021-11-02T13:08:29+00:00'
updated_at: '2021-12-24T10:46:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If monerod is already running or better said if port 18081 on localhost is already open, Monero Wallet CLI auto detects that, uses that port to connect to to that monerod.

Monero Wallet GUI however ignores existing localhost port 18081 and starts its own monerod.

Could you please autodetect if monerod is running on the default port on localhost and in that case avoid Monero Wallet GUI from starting its own monerod?

# Discussion History
## selsta | 2021-11-02T14:02:19+00:00
That must be some configuration issue. The GUI does auto detect if a daemon is running on port 18081 and uses it. Is anything special with your setup?

## adrelanos | 2021-11-02T14:08:33+00:00
This is the full setup:
https://www.whonix.org/wiki/Monero_Wallet_Isolation

Special because socat opens the listening port and forwards it. Monero Wallet CLI can deal with it. Monero Wallet GUI seems to do something else. Does it attempt to detect the process instead of the listening port?

## rbrunner7 | 2021-12-24T10:46:11+00:00
For what it's worth, for me (on bog-standard Linux) sometimes it does not detect an already-running daemon **fast enough**, the GUI wallet kind of gives up and starts to show its "countdown to daemon start" dialog box. If I click the "special settings" button there to prevent any daemon start attempt it takes only a few seconds more until it finally connects to the daemon. No idea why detecting the daemon should take so long ...

# Action History
- Created by: adrelanos | 2021-11-02T13:08:29+00:00
