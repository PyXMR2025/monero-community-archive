---
title: '[Windows] Constant high CPU usage'
source_url: https://github.com/monero-project/monero-gui/issues/757
author: romenoo
assignees: []
labels:
- bug
- resolved
created_at: '2017-06-01T17:12:58+00:00'
updated_at: '2017-08-28T20:25:30+00:00'
type: issue
status: closed
closed_at: '2017-08-28T20:25:08+00:00'
---

# Original Description
The monero-wallet-gui.exe process is constanly using high CPU without any reason, even when not connected to the network. Could somebody please help? Is this a bug? I'm not mining or anything

# Discussion History
## Jaqueeee | 2017-06-02T22:50:48+00:00
Sounds like a bug yes. Are you connected to a local or remote node? What's your computer and os specs? 

## romenoo | 2017-06-03T12:00:34+00:00
No remote node, and no connection necessary for this bug, the moment the GUI shows up, high CPU usage starts with no end. Windows 7 x64, plenty of RAM and CPU

## romenoo | 2017-06-03T13:34:24+00:00
I found a way to stop this, after I start monero-wallet-gui.exe If I block all connections to monerod.exe, when it says "Daemon failed to start" after the failed connection attempts the CPU usage stops. Otherwise when there are connection attempts or a successful connection to monerod.exe, there is constant CPU usage.

Using Process Hacker I found that there is also constant GPU usage along with CPU usage and that stops too after blocking monerod.exe connections.

In case it's related, these lines show up in monero-wallet-gui.log when I start monero-wallet-gui.exe

WARN 	net.dns	src/common/dns_utils.cpp:531	WARNING: no two valid MoneroPulse DNS checkpoint records were received
ERROR	WalletAPI	src/wallet/api/wallet.cpp:551	Status_Critical - not storing wallet

## medusadigital | 2017-08-07T17:26:38+00:00
one of my win 7 machines has similar behaviour. Beta 2.

+Bug 

## medusadigital | 2017-08-28T20:24:56+00:00
fixed in current master.

closing here. will be in next release

+resolved

# Action History
- Created by: romenoo | 2017-06-01T17:12:58+00:00
- Closed at: 2017-08-28T20:25:08+00:00
