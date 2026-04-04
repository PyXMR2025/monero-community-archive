---
title: 'multiple wallets and wallet-rpc '
source_url: https://github.com/monero-project/monero/issues/3131
author: crazy-logic
assignees: []
labels:
- invalid
created_at: '2018-01-16T00:01:28+00:00'
updated_at: '2018-08-15T12:33:02+00:00'
type: issue
status: closed
closed_at: '2018-08-15T12:33:02+00:00'
---

# Original Description
When calling the wallet-RPC in the --wallet-dir mode, so that multiple wallets can be opened. 

1. Can I have more than one wallet open at a time?
2. Is there a way to ensure that one connection to the server doesn't get information from another wallet and vice versa? 

Basically I would like to have multiple wallets open and be abel to read from each of them, but only have one wallet-rpc running on the host. Is this possible? 


# Discussion History
## emesik | 2018-01-16T00:46:42+00:00
1. Apparently, you can't.
2. You have to take care on client side. After `open_wallet` succeeds you should be geting information from the new wallet. You may always verify where you are by calling `getaddress`.

Be aware that after opening a new wallet file, it needs to be synced. This can take a while and the RPC will not tell you in any way whether you are in sync or not. (As comparison, when you start `monero-wallet-rpc` in single-file mode, it won't start receiving commands until synced.)

These reasons were enough for me to drop work with `--wallet-dir`. On one hand, accounts and subaddresses would make it obsolete, on the other, *multisig* makes it perfectly reasonable to have multiple wallets again.

Definitely, RPC needs a lot of work.

## crazy-logic | 2018-01-16T01:19:38+00:00
It does seem a pretty big security flaw to me for the wallet and password not to be passed in each transaction. do you have any idea how online wallets are preforming this functions for their users? 

## moneromooo-monero | 2018-01-16T10:26:35+00:00
If you're reporting a security flaw, please be precise. I've no idea what you're trying to say here.

## crazy-logic | 2018-01-16T13:55:33+00:00
The flaw goes something like this. 

script A opens a wallet A using rpc then makes calls. 
script B opens a wallet B using rpc then makes calls. 
script C - which is actually the same end user as scrip A, makes further calls expecting wallet A to be open, but receives data for wallet B. 

The lack of defining which wallet is used on each RPC request along with some authentication means that if a wallet hosting server is compromised/badly coded and it is using the wallet-rpc to access wallet data, then potentially the wrong responses are being sent to the user/script. Which means that the waller-rpc isn't suitable for hosting multiple wallets with concurrent multiple users? I hope that I have missed something here. 

## moneromooo-monero | 2018-01-16T14:07:58+00:00
Well, that's a bug in whatever drives those scripts.

## crazy-logic | 2018-01-16T14:15:52+00:00
Well yes - it would be is there any other way I can access multiple wallets concurrently (with security) without having to spin up many instances of the wallet-rpc? 

## moneromooo-monero | 2018-01-16T14:19:41+00:00
No. It's not meant to do that.

## emesik | 2018-01-16T20:01:01+00:00
I think the fastest way to have it running would be to maintain a pool of `monero-wallet-rpc` processes in single-wallet mode. Writing a manager that spins up and shuts down instances for requested wallets would be the biggest challenge but far from rocket science. You'd probably like to resync unused wallets in idle time, so they go up faster when needed.

A single instance in wallet-dir mode is useless while resyncing a freshly opened wallet. With multiple instances you may use that time with order another one working on different wallet.

## moneromooo-monero | 2018-01-16T20:43:38+00:00
Why, though ? Is there an actual use for this (beyond guarding against some break in subadresses) ?

## crazy-logic | 2018-01-16T22:30:09+00:00
yeah @emesik that's my thoughts exactly. 

@moneromooo-monero well if you want to host people's wallets for them as a web service, you'ld need to be able to sync wallets and query them concurrently. 

## moneromooo-monero | 2018-01-17T01:03:06+00:00
Fair enough. Not meant for that then :)

## crazy-logic | 2018-01-17T10:59:57+00:00
it would appear that way - so far i cannot find anything that is suitable - which makes me wonder how others are actually doing it. 

## moneromooo-monero | 2018-01-17T11:30:03+00:00
I see three different ways:

- use integrated addresses, so it's a single account, and you have a DB keeping track of everyone's balance
- mymonero has custom scanning code, which only scans a view key when the user logs in
- things like freewallet just scam the user



## hyc | 2018-01-17T15:25:08+00:00
monero-wallet-rpc isn't meant for multiuser services. It's meant for a single user. The create_wallet/open_wallet functionality only exists to round out the feature set and facilitate GUI wrappers like the old java wallet from jwinterm. I.e. its only purpose is to allow someone to do everything monero-wallet-cli does, from a separate process.

If you want to host a multiuser service you need something like MyMonero or OpenMonero.

## moneromooo-monero | 2018-08-15T11:45:54+00:00
No monero bug here.

+invalid

# Action History
- Created by: crazy-logic | 2018-01-16T00:01:28+00:00
- Closed at: 2018-08-15T12:33:02+00:00
