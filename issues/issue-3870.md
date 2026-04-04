---
title: monero-wallet-rpc sometimes freezes.
source_url: https://github.com/monero-project/monero/issues/3870
author: CamilleScholtz
assignees: []
labels: []
created_at: '2018-05-27T13:49:05+00:00'
updated_at: '2018-09-05T07:40:45+00:00'
type: issue
status: closed
closed_at: '2018-09-05T07:40:45+00:00'
---

# Original Description
See title. I can no longer quit it using either `ctrl+c` or `pkill monero-wallet-rpc`. `pkill -9 monero-wallet-rpc` however works.

This started happening since 0.12.1.0.

# Discussion History
## moneromooo-monero | 2018-05-27T15:00:44+00:00
When it does this:
gdb /path/to/monero-wallet-rpc \`pidof monero-wallet-rpc\`
thread apply all bt


## CamilleScholtz | 2018-05-27T15:34:54+00:00
I want to provide more info, but it seems to happen at random. Ill try doing this.

## moneromooo-monero | 2018-09-04T23:49:50+00:00
Any luck ?

## CamilleScholtz | 2018-09-05T07:40:45+00:00
I haven't run into this issue anymore, I'll  close it and re-open if it happens again.

# Action History
- Created by: CamilleScholtz | 2018-05-27T13:49:05+00:00
- Closed at: 2018-09-05T07:40:45+00:00
