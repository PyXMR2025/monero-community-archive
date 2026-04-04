---
title: TROJAN after installing CLI Wallet windows 64
source_url: https://github.com/monero-project/monero/issues/6617
author: githubnesys
assignees: []
labels: []
created_at: '2020-06-01T20:36:20+00:00'
updated_at: '2020-07-08T22:57:48+00:00'
type: issue
status: closed
closed_at: '2020-07-08T22:57:48+00:00'
---

# Original Description
Hello,

I have just installed CLI WALLET for windows 64.

I have done all pgp verification which worked fine.

However, after unzipping the monero-win-x64-v0.16.0.0.zip

I have been warned by windows defender of those malicious programm appearence :

win32/wacatac.D!ml
win32/wacatac.B!ml
win32/Uwasson.A!ml

I am wondering if this is safe to use CLI WALLET and what is happening generally here?

# Discussion History
## selsta | 2020-06-01T21:50:03+00:00
Windows Defender flags the included miner. If you verified the hashes then you can safely ignore it.

## githubnesys | 2020-06-02T08:22:02+00:00
Hello,

can somebody else confirm this ?

This is weird that something is happening in win32 directory whereas all the files I have unzipped must remain in the unzipped folder.

Do you check that some malicious hackers are not participing to the project coding? 

## MaxXor | 2020-06-02T11:42:44+00:00
`win32/XXX` are only names for the type of threat. It doesn't mean they are in the win32 directory.

## githubnesys | 2020-06-02T16:22:33+00:00
But those are well-known trojan. how can you explain?

## erciccione | 2020-06-02T17:54:56+00:00
@githubnesys Monero binaries often get labelled as malware (see https://github.com/monero-project/monero-gui/issues/1747). It's a problem and we are currently discussing solutions.

## trasherdk | 2020-06-03T02:43:43+00:00
@githubnesys It would be more fair to ask anti-virus software providers, why they are flagging valid software as well-known trojan malware.

## githubnesys | 2020-06-05T13:01:08+00:00
I know people that have been scammed with https://www.xmrwallet.com which is not reliable. so It is better to be carefull with any software dealing by monero.

The best thing would be to develop a browser based tool like coinb.in for BTC which allow to build transaction offline then to broadcast it. As a result one is sure that private key is not interacting with the web. why this doesn't exist yet for monero??

## selsta | 2020-06-05T13:05:29+00:00
> The best thing would be to develop a browser based tool like coinb.in for BTC which allow to build transaction offline then to broadcast it. As a result one is sure that private key is not interacting with the web. why this doesn't exist yet for monero??

The private key is also not interacting with the web if you use one of the desktop wallets. Also see: https://xmrchain.net/rawtx

## githubnesys | 2020-06-05T16:30:51+00:00
Is NOT interacting with the web what is NOT connected to the web. so forget about desktop wallets. 

## Marticoin | 2020-06-07T10:57:15+00:00
monero wallets gui and cli are infected with trojans ~ the downloaded exe's are severe threats, windows defender says .  So how to I safely store xmr on nano s ? Will ledger live hold xmr soon ?

## erciccione | 2020-06-07T11:21:46+00:00
@Marticoin did you read the conversation above before commenting? The Monero binaries don't contain malware.

## githubnesys | 2020-06-13T15:44:43+00:00
can you sign transaction offline with CLI Wallet?

## moneromooo-monero | 2020-06-13T15:46:41+00:00
Yes. See monero.stackexchange.com, which has a list of steps for this.

## dEBRUYNE-1 | 2020-06-14T09:19:10+00:00
@githubnesys - See:

https://monero.stackexchange.com/questions/2868/is-there-any-way-to-construct-a-transaction-manually

# Action History
- Created by: githubnesys | 2020-06-01T20:36:20+00:00
- Closed at: 2020-07-08T22:57:48+00:00
