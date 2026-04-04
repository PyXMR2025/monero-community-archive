---
title: cant find coins on trezor after monero gui update
source_url: https://github.com/monero-project/monero/issues/9276
author: ofiryy
assignees: []
labels: []
created_at: '2024-04-03T22:59:59+00:00'
updated_at: '2024-04-05T10:21:27+00:00'
type: issue
status: closed
closed_at: '2024-04-04T21:01:38+00:00'
---

# Original Description
i had monero gui from 2 years ago, so i uninstalled it,
and installed the lated version  0.18.3.3,
i accessed the gui and restored from trezor device,
now i see all the coins are gone, the balance is 0.
could i have created by aacident a new monero wallet from trezor?
what can i do to access the old coins?

# Discussion History
## selsta | 2024-04-03T23:01:25+00:00
Do you still have the old wallet file?

What does it say inside Settings -> Info -> Wallet restore height?

## ofiryy | 2024-04-03T23:04:04+00:00
i dont think i have any old file, i uninstalled the old gui, and also manually deleted its directory,
i wanted to start fresh with the latest monero gui.
the wallet restore hight is 1.  i use remote node

## selsta | 2024-04-03T23:05:40+00:00
What does it say in Settings -> Info -> Wallet mode?

What does it say in the bottom left corner? Wallet is synchronized or is it still syncing?

## ofiryy | 2024-04-03T23:06:58+00:00
wallet mode is advanced mode (remote node)
wallet still syncing

## selsta | 2024-04-03T23:07:54+00:00
You have to let the wallet finish syncing first before the funds show up.

## ofiryy | 2024-04-03T23:17:42+00:00
i use node.moneroworld.com:18089 
is it ok?
how much time should it take ?

## selsta | 2024-04-03T23:19:42+00:00
If it syncs blocks then the node is ok. I don't know how long it will take, it depends on your internet speed, your CPU, the speed of the node, etc.

In the future it would be better to set a restore height that is higher than 1 but still lower than your first received transactions to speed up the process.

## ofiryy | 2024-04-03T23:26:21+00:00
can i change the restore height while it is syncronizing ?

## selsta | 2024-04-03T23:32:02+00:00
In theory yes, but it would be best to just let it sync now before you enter a wrong restore height.

## ofiryy | 2024-04-04T00:21:28+00:00
the remote node has finished syncronizing and still i see 0 in balance,
so i switched to local node, network status is connected, ans still 0 balance.
i had changed the resore hight to a date 2021-04-04, could it be the problem ?


## selsta | 2024-04-04T03:53:42+00:00
Please stay on remote node, you don't have a synced local node so use remote node instead.

>i had changed the resore hight to a date 2021-04-04, could it be the problem ?

What does it say under Settings -> Info -> Restore height? Share the exact value.

## ofiryy | 2024-04-04T09:09:55+00:00
Wallet restore height: 2311108

## selsta | 2024-04-04T15:38:50+00:00
Did you setup a passphrase on your Trezor that you previously did not have?

Did you let it sync on a remote node until 0 blocks were remaining before you switched to local node?

## ofiryy | 2024-04-04T15:50:25+00:00
i did not setup any passphrase. not before and not now.
with the remote node - it finished syncronizing, i mean, the "Syncronizing" was replaced with "Remote node",
so i understood from this that it finished syncronizing (btw at that point the Wallet restore height was: 2311108) 
and i still had only 0 funds.
but after  the "Syncronizing" was replaced with "Remote node", i dont know to say how many blocks were remaining.






## ofiryy | 2024-04-04T18:39:23+00:00
@selsta 
now, with local node, after hours of syncronizing, i have the "Connected" status,
Wallet restore height: 2311108 
and still 0 funds.
what can i do to access my funds ?

## selsta | 2024-04-04T20:16:05+00:00
@ofiryy  go to Settings -> Log, type "status" into the textbox and post the output here.

## ofiryy | 2024-04-04T20:20:59+00:00
i found the funds! 
i just needed to "open wallet from file" and then go the first wallet. i had like 3 wallets there, the 3rd one i created yesterday, 
i didnt know it actually kept some files from the old wallet, i didnt know it works like that.
so i send some funds to another address- and complete the approvel process on trezor - it went well,
but it seems stuck on "Sending transaction..."
what do you think is the issue ?
thanks

## selsta | 2024-04-04T20:22:16+00:00
Please do what I suggested in my last comment. I need to know the status of the daemon.

## ofiryy | 2024-04-04T20:26:04+00:00
i had to restart the gui because it was stuck, 
here is the output:

[4/4/2024 11:23 PM] 2024-04-04 20:23:45.145 I Monero 'Fluorine Fermi' (v0.18.3.3-release) 
Height: 3120194, target: 3120202 (99.9997%) 
Downloading at 3 kB/s 
4 peers 
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB 
24.90.16.82:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued 
135.181.86.255:18080 1cee5a28ef1d2f26 normal 180 3120202 1 kB/s, 0 blocks / 0 MB queued 
76.237.91.67:18089 a2134f97838eea72 normal 0 3120202 1 kB/s, 0 blocks / 0 MB queued 
185.165.170.162:18080 bed0e8f96e1b2b8b normal 0 3120202 1 kB/s, 0 blocks / 0 MB queued 
0 spans, 0 MB 
[]
>>> status
[4/4/2024 11:25 PM] 2024-04-04 20:24:26.904 I Monero 'Fluorine Fermi' (v0.18.3.3-release) 
Height: 3120202/3120202 (100.0%) on mainnet, bootstrapping from 5.78.103.116:18089, local height: 3120194 (99.9%), not mining, net hash 2.04 GH/s, v16, 0(out)+0(in) connections
[4/4/2024 11:25 PM] 2024-04-04 20:24:41.039 I Monero 'Fluorine Fermi' (v0.18.3.3-release) 
Height: 3120202/3120202 (100.0%) on mainnet, bootstrapping from 5.78.103.116:18089, local height: 3120194 (99.9%), not mining, net hash 2.04 GH/s, v16, 0(out)+0(in) connections

## selsta | 2024-04-04T20:28:09+00:00
> Height: 3120194, target: 3120202 (99.9997%)

It has to be at 100% for everything to work correctly.

## ofiryy | 2024-04-04T20:49:04+00:00
now i confirmd that it was 100%, and the transaction still get stuck...how long can it take ?

## selsta | 2024-04-04T20:51:54+00:00
I'm confused how you were even able to create that transaction because as long as your node isn't at 100% you can't create one. Did you switch to a remote node for it?

> now i confirmd that it was 100%

Get the transaction ID, go to Settings -> Log and enter

relay_tx txid

with txid being your transaction id.

## ofiryy | 2024-04-04T21:01:38+00:00
its so weird,  i let the trasaction be stuck for like 15 min, and now i see that it succeeded, i see the funds in the target adress, but the gui is still stuck.

i would send you the log you asked, but i dont have the transaction id.
this wallet need some work to be more stable - but your support is fantastic,
thank you very much


## johnr365 | 2024-04-05T10:21:26+00:00
@ofiryy - maybe try out the (Monero only) wallet called [Feather Wallet](https://featherwallet.org/) in the future. It supports Trezor hardware wallets, and some people prefer it to the GUI wallet.

# Action History
- Created by: ofiryy | 2024-04-03T22:59:59+00:00
- Closed at: 2024-04-04T21:01:38+00:00
