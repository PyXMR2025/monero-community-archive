---
title: Unable to start monero-wallet-gui Qt version incompatible
source_url: https://github.com/monero-project/monero-gui/issues/2820
author: ghost
assignees: []
labels:
- invalid
created_at: '2020-04-05T02:54:53+00:00'
updated_at: '2020-04-22T20:48:16+00:00'
type: issue
status: closed
closed_at: '2020-04-22T20:48:15+00:00'
---

# Original Description
In the last 2 days when I attempt to start monero-wallet-gui, I get this error:
`2020-04-05 02:46:01.021 W app startd (log: /home/anon/.bitmonero/monero-wallet-gui.log)
2020-04-05 02:46:01.022 W Qt:5.14.1 GUI:- | screen: 1600x900 - dpi: 96.063 - ratio:1.02695
2020-04-05 02:46:01.107 W QQmlApplicationEngine failed to load component
2020-04-05 02:46:01.107 W qrc:/main.qml: File was compiled ahead of time with an incompatible version of Qt and the original file cannot be found. Please recompile
2020-04-05 02:46:01.107 E Error: no root objects
`
I am using Arch linux and I am using the latest version from the repos. I have tried re-installing monero-gui and all components of qt installed on my system. 

# Discussion History
## selsta | 2020-04-05T02:56:29+00:00
Appears to be some caching issue on your system.

## ghost | 2020-04-05T02:57:30+00:00
> Appears to be some caching issue on your system.

Would you recommend clearing my cache?
 

## selsta | 2020-04-05T02:58:29+00:00
I’m not familiar with arch. Delete monero and caches and reinstall.

## selsta | 2020-04-05T02:59:55+00:00
If this does not work please report to the maintainer of the arch package. This is not a monero-gui bug.

## selsta | 2020-04-22T20:48:15+00:00
Not a monero-gui bug.

# Action History
- Created by: ghost | 2020-04-05T02:54:53+00:00
- Closed at: 2020-04-22T20:48:15+00:00
