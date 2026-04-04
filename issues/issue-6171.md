---
title: rpc_payments not working via bootstrapped daemon
source_url: https://github.com/monero-project/monero/issues/6171
author: sebseb7
assignees: []
labels: []
created_at: '2019-11-22T14:01:05+00:00'
updated_at: '2019-11-22T21:53:39+00:00'
type: issue
status: closed
closed_at: '2019-11-22T21:53:39+00:00'
---

# Original Description
does not seem to work via bootstrapped daemon


# Discussion History
## moneromooo-monero | 2019-11-22T14:20:57+00:00
Not enough details to know what you're reporting.

## sebseb7 | 2019-11-22T14:22:48+00:00
I have a cli wallet connected to a daemon which is connected to another daemon (with rpc payments enabled) via --bootstrap-daemon-address, branch release-v0.15 ,

## sebseb7 | 2019-11-22T14:23:51+00:00
a direct connection to the payments-enabled daemon works

## moneromooo-monero | 2019-11-22T17:26:13+00:00
I can repro, will fix.

## moneromooo-monero | 2019-11-22T18:19:33+00:00
https://github.com/monero-project/monero/pull/6173

## sebseb7 | 2019-11-22T21:53:39+00:00
works for me, 

# Action History
- Created by: sebseb7 | 2019-11-22T14:01:05+00:00
- Closed at: 2019-11-22T21:53:39+00:00
