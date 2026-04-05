---
title: Socket Connection Error
source_url: https://github.com/xmrig/xmrig/issues/2381
author: Sammed98
assignees: []
labels: []
created_at: '2021-05-16T02:12:16+00:00'
updated_at: '2021-12-08T15:59:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Getting the error 'read error: "socket is not connected"' when executing XMRIG with unmineable mining pool rx.unmineable.com:3333 . It was working well for many days and the coins I was mining was appearing on the unmineable dashboard too. 

What could be possible error? I am running this on my Mac Book pro. Is the error on the pooling side or XMRIG's side?
Mining Coin: DOGE, Mining Pool: rx.unmineable.com:3333, CPU Mining with algo rx/0 (RandomX)

**To Reproduce**
Execute XMRIG on Mac, with unmineable mining pool for RandomX algo. 

**Expected behavior**
Clear exeuction of XMRIG and mining of DOGE coin



**Required data**
<img width="972" alt="Screenshot 2021-05-16 at 7 41 17 AM" src="https://user-images.githubusercontent.com/25957319/118383285-1bfe7d00-b61a-11eb-9427-e9aa56ca17e0.png">
 - Config file or command line (without wallets) - generic config. No major modifications
 - OS: Mac
 - 

**Additional context**
Add any other context about the problem here.


# Discussion History
## Sammed98 | 2021-05-17T08:35:23+00:00
@xmrig Any comments?

## Spudz76 | 2021-05-17T20:30:17+00:00
Firewall or security software is aborting the connection.  Or the pool is having issues on their end, abandoning active connections.

## monkeyfisherman | 2021-12-08T12:55:10+00:00
@xmrig y'all fix this?

## Spudz76 | 2021-12-08T15:59:40+00:00
Nothing to fix... fix your own networking.

# Action History
- Created by: Sammed98 | 2021-05-16T02:12:16+00:00
