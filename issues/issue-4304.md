---
title: '[suggestion/request] list existing wallet files on start of wallet-cli'
source_url: https://github.com/monero-project/monero/issues/4304
author: aeon1234
assignees: []
labels:
- invalid
created_at: '2018-08-26T10:20:02+00:00'
updated_at: '2018-10-01T18:57:00+00:00'
type: issue
status: closed
closed_at: '2018-10-01T18:57:00+00:00'
---

# Original Description
**either first suggestion:**

`This is the command line monero wallet. It needs to connect to a monero daemon to work correctly.`
`WARNING: Do not reuse your Monero keys on an another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.`
`Monero 'Lithium Luna' (v0.12.3.0-release)`
`Logging to ./monero-wallet-cli.log`
`Existing wallet files:`
`wallet_1` `wallet_2` `wallet_3` `wallet_4` `wallet_5`
`wallet_6` `wallet_7` `wallet_8` `wallet_9` `wallet_10`
`wallet_11` `wallet_12` `wallet_13` `wallet_14` `wallet_15`
`Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.`
`Wallet file name (or Ctrl-C to quit): `

it would also be possible to create a flag to start with/without this (depends on which one makes more sense):
`./monero-wallet-cli --show-existing-wallets`
`./monero-wallet-cli --hide-existing-wallets`



**or second suggestion:**

`This is the command line monero wallet. It needs to connect to a monero daemon to work correctly.`
`WARNING: Do not reuse your Monero keys on an another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.`
`Monero 'Lithium Luna' (v0.12.3.0-release)`
`Logging to ./monero-wallet-cli.log`
`Existing wallet files:`
`1) wallet_1` `2) wallet_2` `3) wallet_3` `4) wallet_4` `5) wallet_5`
`6) wallet_6` `7) wallet_7` `8) wallet_8` `9) wallet_9` `10) wallet_10`
`11) wallet_11` `12) wallet_12` `13) wallet_13` `14) wallet_14` `15) wallet_15`
`Use number in front of a file name to open it (or Q to create a new wallet).`
`Which file do you want to open (or Ctrl-C to quit): `

# Discussion History
## jtgrassie | 2018-08-26T12:42:09+00:00
I'm not a fan of this suggestion. It would require parsing files in the CWD just to check if each file was an actual wallet file. Unclear what problem this is trying to solve for.

## jonathancross | 2018-08-27T12:33:29+00:00
Please correct me if I am wrong, but I believe @aeon1234 is trying to make it easier for users to select from their existing wallet files to prevent typos, have a better overview of the options available, etc.  The idea is to present a better user interface for wallet selection.  I am assuming it would not parse the CWD but rather look in the _default_ wallet location (eg `~/.bitmonero/wallet/`)

Such an interface might help users to feel more confident in the use of the software as it suggests that the wallet is aware of its state (the wallets files that can be loaded).

I still don't know if I agree with the change, but thought I would add this clarification.

## jtgrassie | 2018-08-27T12:43:45+00:00
There is no _default_ wallet location IIRC. It simply gets created in your CWD. 

> select from their existing wallet files to prevent typos

You could have wallets in multiple places though (not in CWD). To effectively solve for this, there would need to be a file at a known location storing where wallets were created. Even then it's flimsy, as people might move wallets.

This suggestion is trying to solve a problem that doesn't exist, IMO. 

## aeon1234 | 2018-08-27T13:49:41+00:00
> Unclear what problem this is trying to solve for.

I always forget how I named my wallet files. 
e.g. is it `wallet_testnet_1` or `testnet_1` or `test1` or even `another_testnet`.

and I also create my wallet files in cwd only, otherwise I had not posted this suggestion.
I'm not sure how others handle this and if a lot of people really save their wallet files in other directories. 

## jtgrassie | 2018-08-27T14:08:10+00:00
But why not simply `ls` in the directory before launching the monero-wallet-cli? Adding file browser capability into the cli seems very odd to me and also, as stated, the cli would have to parse all the files to determine if they were actually wallet files vs other files. 

## jonathancross | 2018-08-27T16:58:51+00:00
>  I also create my wallet files in cwd only

Ah, okay, I did not understand it that way, I thought were talking about using the canonical wallet directory (`~/.bitmonero/wallet/`) and parsing what was in there for convenience.

I agree with @jtgrassie -- this feature offers little benefit above the `ls` command and would complicate the wallet by trying to make it "smart".  Once we set the user expectation that the wallet "knows" which wallets are available, it means all kinds of trouble unless we build a file browser as well.  Parsing everything in the CWD looking for possible wallets would slow down the wallet loading and I don't even think it would benefit most users.

## hyc | 2018-08-28T01:33:40+00:00
Also agree with @jtgrassie - just use `ls` before running the wallet. Write your own alias or shell script to do this automatically if you like, but the functionality doesn't belong in monero-wallet-cli itself.

## moneromooo-monero | 2018-08-28T11:23:55+00:00
I could see this being useful for the GUI though. File this in the monero-core repo.

## jonathancross | 2018-08-31T20:52:48+00:00
> I could see this being useful for the GUI though. File this in the monero-core repo.

A list of "recently opened wallets" would be sufficient and would require no directory parsing (this is how Electrum works).

## moneromooo-monero | 2018-10-01T18:51:40+00:00
Please reopen in the GUI repo instead.

+invalid

# Action History
- Created by: aeon1234 | 2018-08-26T10:20:02+00:00
- Closed at: 2018-10-01T18:57:00+00:00
