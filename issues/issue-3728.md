---
title: Wallet could not connect to deamon
source_url: https://github.com/monero-project/monero-gui/issues/3728
author: SorenJorgensen-crypto
assignees: []
labels: []
created_at: '2021-11-05T14:38:23+00:00'
updated_at: '2023-03-12T16:43:46+00:00'
type: issue
status: closed
closed_at: '2023-01-17T05:13:42+00:00'
---

# Original Description
My Monero-wallet will not connect to deamon. It did synchronize/update this blocks but did not connect. I get this error message in login: 127.0.01:18081. I cannot find monerod (which is suggested I use to open manually) in applications and my funds are not shown in the balance anymore which worries me. Is it possible to get some assistance with this issue?

# Discussion History
## chesc-I0 | 2022-01-21T02:49:24+00:00
I thought that I would give Monero a try and that is all I can get out of it.

[21/01/2022 02:46] 2022-01-21 02:46:27.409 I Monero 'Oxygen Orion' (v0.17.3.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081



## selsta | 2022-01-21T03:50:00+00:00
@chesc-I0 you have to be more precise at describing what your problem is, that message can be normal and doesn't mean much, it just means it couldn't connect during the first try

## ghost | 2022-01-21T10:34:49+00:00
Hi All!

I'm having the same problem on Manjaro Linux( 5.14.21-2-MANJARO), this is what I'm getting while running monerod in console:

```
2022-01-21 10:22:47.220	I [136.24.42.205:18080 OUT] Sync data returned a new top block candidate: 2295984 -> 2541963 [Your node is 245979 blocks (11.2 months) behind] 
2022-01-21 10:22:47.220	I SYNCHRONIZATION started
monerod: malloc.c:2539: sysmalloc: Assertion `(old_top == initial_top (av) && old_size == 0) || ((unsigned long) (old_size) >= MINSIZE && prev_inuse (old_top) && ((unsigned long) old_end & (pagesize - 1)) == 0)' failed.
```
I have installed monero-gui through package manager and it's this version: Monero 'Oxygen Orion' (v0.17.3.0-release)

## chesc-I0 | 2022-01-21T14:22:28+00:00
@selsta Thanks.

I am using Ubuntu 21.10. This problem affects:
-Appimage 0.17.3.1-release (Qt 5.15.2) 
-Flatpak 0.17.3.1 for me. 

When I launch the Monero GUI and look at the log, this message:

[21/01/2022 14:07] 2022-01-21 14:07:38.483 I Monero 'Oxygen Orion' (v0.17.3.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081

Is repeated over an over. Eventually I get a pop up that says that it is unable to connect to the Daemon. It seems to never finish setting up a wallet since every time I close and relaunch the GUI it asks me to set up a new wallet.

## selsta | 2022-01-26T00:59:57+00:00
@cptBartsky It likely means that your blockchain is corrupted. This can happen if you force shutdown your computer during initial sync. You have to delete the blockchain and resync.

@chesc-I0 Could this be a permission issue? Do the wallets get saved to disk? Default location is `~/Monero/wallets`

## ghost | 2022-01-28T15:10:26+00:00
> @cptBartsky It likely means that your blockchain is corrupted. This can happen if you force shutdown your computer during initial sync. You have to delete the blockchain and resync.
> 
> @chesc-I0 Could this be a permission issue? Do the wallets get saved to disk? Default location is `~/Monero/wallets`

Thank You very much @selsta worked like a charm :)

## chesc-I0 | 2022-01-28T15:22:22+00:00
@selsta If I change the wallet location to default the daemon can connect - I agree that this probably a permissions issue. 

## selsta | 2023-01-17T05:13:42+00:00
Closing this support issue due to inactivity.

## tsilvs | 2023-03-12T11:14:36+00:00
Having this issue with flatpak wallet and blockchain in external drive.

## selsta | 2023-03-12T15:18:19+00:00
@BigmenPixel0 is this sandboxing related?

## tsilvs | 2023-03-12T16:43:13+00:00
@selsta Don't know yet. The permission is given (via Flatseal), the path to `bch` directory is visible by the file manager window used by the wallet GUI to specify the path to it.

# Action History
- Created by: SorenJorgensen-crypto | 2021-11-05T14:38:23+00:00
- Closed at: 2023-01-17T05:13:42+00:00
