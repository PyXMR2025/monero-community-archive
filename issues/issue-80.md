---
title: Rename legacy bits to Monero
source_url: https://github.com/monero-project/monero/issues/80
author: fluffypony
assignees: []
labels: []
created_at: '2014-08-02T20:44:03+00:00'
updated_at: '2018-06-22T18:01:06+00:00'
type: issue
status: closed
closed_at: '2016-09-03T17:28:04+00:00'
---

# Original Description
Per https://help.github.com/articles/renaming-a-repository - renaming a project will forward everything from the old name to the new with no major consequences. Forks would do well to change their upstream URL, or just re-clone their fork to a working copy, but it'll forward a 'git fetch upstream' to the new URL.

The binary should also be renamed 'monerod' from 'bitmonerod'.


# Discussion History
## fluffypony | 2014-08-02T20:55:45+00:00
I'd also like to change the CRYPTONOTE_NAME to monero. The knock-on effect is it will change the bitmonero bit in the data directory (which was formerly ~/.bitmonero / AppData\Roaming\bitmonero).

I'm of the opinion that the best to deal with this is to add a small stub of code to the daemon that will rename an "old" data directory it encounters to the new one. This check should be hard-coded (ie. don't introduce extra unnecessary constants like OLD_CRYPTONOTE_NAME).

As an aside: transitionary stubs such as this one should always be introduced with a deprecation date. For this change, I suggest 12 months, after which this code is completely removed. If anyone runs into a problem thereafter, they can always grab an older tagged release before switching up to a new one (or in this case just rename the folder). It's not feasible to have Monero littered with code to ensure compatibility with ancient and deprecated versions.


## Jojatekok | 2014-08-03T15:55:31+00:00
May I propose to change the exe file names like the following:
- bitmonerod.exe -> monero_daemon.exe
- simplewallet.exe -> monero_wallet_simple.exe
- rpcwallet.exe -> monero_wallet_rpc.exe

Just for consistency :)


## fluffypony | 2014-08-10T10:11:28+00:00
Marked for inclusion in the next tagged release


## fluffypony | 2016-06-03T14:38:21+00:00
This slipped away due to all the other bits, but I'd like to revisit it.

The recommendations above all still stand, except I'm leaning more towards a dash instead of an underscore, to follow `git` convention. Thus the following changes would occur:
- `bitmonerod` -> `monero-daemon` (or `monero-node` ?)
- `simplewallet` -> `monero-wallet-cli`
- `blockchain_dump` -> `monero-blockchain-dump`
- `blockchain_import` -> `monero-blockchain-import`
- `blockchain_export` -> `monero-blockchain-export`
- utility bits (eg. pop-blocks) from blockchain_import -> `monero-utils-blockchain`
- `cn_deserialize` -> dropped, or renamed to `monero-utils-deserialize`
- `blockchain_converter` -> dropped, no longer necessary
- `simpleminer` -> dropped due to disuse

And later on:
- `monero-wallet-rpc` once we've pulled through the old rpcwallet work
- `monero-deprecated-rpc` for the RPC stub for daemon RPC calls, once the 0MQ work is done

Suggestions welcome.


## moneromooo-monero | 2016-08-28T16:57:18+00:00
How about s/monero-blockchain/monero-utils/ ?
Or s/monero-blockchain/monero-utils-blockchain/ too.


## hyc | 2016-08-28T16:58:07+00:00
Naming of resulting binaries with '-' is ok. Naming of individual source files should use underscores. Debuggers don't like filenames/symbols with dashes in them.


## radfish | 2016-08-28T23:59:40+00:00
Please accept vote for: `monerod` -- it is short and follows the convention.

I would combine all those separate blockchain manipulation binaries into either one binary with subcommands (`monero-blockchain import|export|dump|convert`) or even roll it into monerod (after all, the daemon "owns" the blockchain). Not sure what cm_serialize does, but hopefully it can also be rolled into. With all respect to unix principle, I think grouping these is better for the end user than having them as separate binaries.

One vote for `monero-wallet` instead of `monero-wallet-cli` for sake of shortness, although I don't know what the *-rpc binaries are intended to be and how they relate to *-cli?


## hyc | 2016-08-29T00:15:14+00:00
Yes, I had proposed rolling import/export into the daemon earlier as well. It would have made the migration code much easier to write.


## fluffypony | 2016-08-29T00:23:43+00:00
@radfish it's silly to have monero-wallet offer both CLI and RPC modes, since they're super distinct and will need to be able to be developed independently of each other without affecting each other's moving parts. so having one that is CLI, and pulling out the RPC stuff into its own binary (as we did with rpcwallet on the now-defunct development branch) is the way to allow that to happen.


## fluffypony | 2016-09-03T17:28:04+00:00
Mostly closed by #1039, will have to consider the CRYPTONOTE_NAME stuff later on.


## jetwhiz | 2016-09-03T19:16:02+00:00
It looks like Travis-CI is broken -- possibly related to the rename? 

https://travis-ci.org/monero-project/bitmonero


## fluffypony | 2016-09-03T19:30:23+00:00
@jetwhiz the Travis stuff moved as well, check https://travis-ci.org/monero-project/monero


## jetwhiz | 2016-09-03T19:36:50+00:00
@fluffypony  -- I think the [README.md](https://github.com/monero-project/monero/blob/master/README.md) is still pointing to https://travis-ci.org/monero-project/bitmonero 


## fluffypony | 2016-09-03T19:38:01+00:00
@jetwhiz tks - busy fixing that now :)


## sysfu | 2018-06-22T17:59:01+00:00
Blockchain is still being written to legacy folder name C:\ProgramData\bitmonero\lmdb as of version 0.12.2.0

# Action History
- Created by: fluffypony | 2014-08-02T20:44:03+00:00
- Closed at: 2016-09-03T17:28:04+00:00
