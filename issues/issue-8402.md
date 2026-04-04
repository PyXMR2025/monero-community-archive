---
title: Monerod shuts down at random times
source_url: https://github.com/monero-project/monero/issues/8402
author: ksdhans
assignees: []
labels: []
created_at: '2022-06-23T07:31:39+00:00'
updated_at: '2024-07-31T23:19:45+00:00'
type: issue
status: closed
closed_at: '2024-07-31T23:19:44+00:00'
---

# Original Description
Monerod will periodically just quit. It happens every few hours or so, although it's rather unpredictable. 

Here's the final entries when I run it in a console window:
2022-06-23 06:44:18.667 W No incoming connections - check firewalls/routers allow port 18080
Assertion failed: Connection reset by peer [10054] (src/signaler.cpp:372)
Assertion failed: Connection reset by peer [10054] (src/signaler.cpp:372)

This is with Monero 'Oxygen Orion' (v0.17.3.2-release), on Windows 10.  The blockchain is fully synchronized.

NOTE: I've only managed to capture one failure so far, so I can't say if it's always the connection reset that triggers it.

# Discussion History
## selsta | 2022-06-23T20:09:18+00:00
Can you please post your config / which options you start monerod with?

## selsta | 2022-07-19T15:49:15+00:00
ping

## moneromooo-monero | 2022-07-21T12:25:02+00:00
From a web search, it looks like libzmq asserting on us.

## John4266 | 2022-08-30T19:32:05+00:00
I just had this problem as well

![](https://i.imgur.com/YTzISD3.png)
![](https://i.imgur.com/AMfwyJ1.png)

My arguments were: `.\monerod.exe --out-peers=50 --prep-blocks-threads=8 --block-sync-size=60 --data-dir G:\bitmonero --check-updates disabled --non-interactive --max-concurrency 12`

I am using a Windows 10 (64 bit) computer
Monero version: `Monero 'Fluorine Fermi' (v0.18.1.0-release)`
`monerod.exe` is whitelisted in firewall

EDIT: I ended up downloading the whole blockchain by using a while loop in powershell so even if it crashes it will restart:
```ps
PS E:\Program Files\Monero GUI Wallet> while ($true) {
>> ".\monerod.exe --out-peers=50 --prep-blocks-threads=8 --block-sync-size=60 --data-dir G:\bitmonero --check-updates download --non-interactive --max-concurrency 12" | Invoke-Expression
>> }
```

## selsta | 2024-07-31T23:19:44+00:00
Closing as the issue does not appear to be on monero's side.

# Action History
- Created by: ksdhans | 2022-06-23T07:31:39+00:00
- Closed at: 2024-07-31T23:19:44+00:00
