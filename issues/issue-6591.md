---
title: Monero daemon sending commands to itself over i2p
source_url: https://github.com/monero-project/monero/issues/6591
author: MoneroArbo
assignees: []
labels: []
created_at: '2020-05-26T12:54:49+00:00'
updated_at: '2021-08-16T03:55:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm seeing in [my bitmonero.log](https://github.com/monero-project/monero/files/4682277/bitmonero.log.txt) where the daemon is sending command 1001 to its own i2p address, which is nqussuztpeyrbtxz7j6fc32lugwm4ajincm5emqueihlbxq2rtza.b32.i2p.

Expected behavior is that the daemon would recognize and not attempt to connect to the inbound address that was passed to it when it was run.

# Discussion History
## xanoni | 2021-08-16T03:55:59+00:00
Also curious, seems weird.

Also weird: https://github.com/monero-project/monero/issues/6938#issuecomment-752290654

# Action History
- Created by: MoneroArbo | 2020-05-26T12:54:49+00:00
