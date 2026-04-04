---
title: Couldn’t sync correctly blockchain
source_url: https://github.com/monero-project/monero-gui/issues/3184
author: svpi11
assignees: []
labels: []
created_at: '2020-10-21T07:13:38+00:00'
updated_at: '2020-10-22T06:57:12+00:00'
type: issue
status: closed
closed_at: '2020-10-22T06:57:12+00:00'
---

# Original Description
I had a problem sync correctly to the Monero blockchain. I try for days to do it on a hard drive disk (so slower), so I have to shutdown and start again quite often, and today I had some issue to restart the sync of the daemon.

Here are the logs:





2020-10-21 07:01:13.406 I Monero 'Oxygen Orion' (v0.17.1.0-release) 2020-10-21 07:01:13.406 I Initializing cryptonote protocol... 2020-10-21 07:01:13.406 I Cryptonote protocol initialized OK 2020-10-21 07:01:13.407 I Initializing core...
2020-10-21 07:01:13.407 I Loading blockchain from folder /home/MYNAME/.bitmonero/lmdb ... 2020-10-21 07:01:13.407 W The blockchain is on a rotating drive: this will be very slow, use an
SSD if possible
2020-10-21 07:01:13.544 I
2020-10-21 07:01:13.544 I
2020-10-21 07:01:13.544 I
2020-10-21 07:01:13.550 I
2020-10-21 07:01:13.550 I
2020-10-21 07:01:13.550 I
2020-10-21 07:01:13.931 I
2020-10-21 07:01:13.931 I
2020-10-21 07:01:13.931 I
2020-10-21 07:01:13.932 I
2020-10-21 07:01:14.933 I
2020-10-21 07:01:14.933 I
2020-10-21 07:01:14.933 I
long time to complete.
2020-10-21 07:01:14.934 I
2020-10-21 07:01:14.934 I
categories>" command,
2020-10-21 07:01:14.934 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-10-21 07:01:14.934 I
2020-10-21 07:01:14.934 I Use the "help" command to see the list of available commands. 2020-10-21 07:01:14.934 I Use "help <command>" to see a command's documentation. 2020-10-21 07:01:14.934 I **********************************************************************
2020-10-21 07:01:17.518 I [213.106.30.43:18080 OUT] Sync data returned a new top block candidate: 2081151 -> 2210720 [Your node is 129569 blocks (5.9 months) behind]
2020-10-21 07:01:17.518 I SYNCHRONIZATION started
2020-10-21 07:01:21.679 W Failed to get top block hash to check for new block's parent: MDB_NOTFOUND: No matching key/data pair found
2020-10-21 07:01:21.679 E Error adding block with hash: <68b837f89e8e80a33a5b4aec495133b22c581becad154b2861ce484f584b0d62> to blockchain, what = Failed to get top block hash to check for new block's parent: MDB_NOTFOUND: No matching key/data pair found
2020-10-21 07:01:21.681 W monerod is now disconnected from the network
2020-10-21 07:01:23.641 I [85.215.86.29:18080 OUT] Sync data returned a new top block candidate: 2081151 -> 2213093 [Your node is 131942 blocks (6.0 months) behind]
2020-10-21 07:01:23.641 I SYNCHRONIZATION started
2020-10-21 07:01:25.048 E Failed to get tx meta from txpool
2020-10-21 07:01:25.049 E Failed to get tx meta from txpool
2020-10-21 07:01:25.049 E Failed to get tx meta from txpool
2020-10-21 07:01:25.049 E Failed to get tx meta from txpool
2020-10-21 07:01:25.049 E Failed to get tx meta from txpool
2020-10-21 07:01:25.049 E Failed to get tx meta from txpool
2020-10-21 07:01:25.049 E Failed to get tx meta from txpool
2020-10-21 07:01:25.049 E Failed to get tx meta from txpool
2020-10-21 07:01:25.049 E Failed to get tx meta from txpool
2020-10-21 07:01:25.049 E Failed to get tx meta from txpool
2020-10-21 07:01:25.049 E Failed to get tx meta from txpool
2020-10-21 07:01:25.050 E Failed to get tx meta from txpool
2020-10-21 07:01:25.050 E Failed to get tx meta from txpool
2020-10-21 07:01:25.050 E Failed to get tx meta from txpool
2020-10-21 07:01:25.050 E Failed to get tx meta from txpool
2020-10-21 07:01:25.050 E Failed to get tx meta from txpool
2020-10-21 07:01:25.050 E Failed to get tx meta from txpool
Loading checkpoints
Core initialized OK
Initializing p2p server...
p2p server initialized OK
Initializing core RPC server...
Binding on 127.0.0.1 (IPv4):18081
core RPC server initialized OK on port: 18081 Starting core RPC server...
core RPC server started ok Starting p2p net loop...
You can set the level of process detailization through "set_log <level|
**********************************************************************
The daemon will start synchronizing with the network. This may take a

 2020-10-21 07:01:25.050 E Failed to get tx meta from txpool
2020-10-21 07:01:25.050 E Failed to get tx meta from txpool
2020-10-21 07:01:25.050 E Failed to get tx meta from txpool
2020-10-21 07:01:25.050 E Failed to get tx meta from txpool
2020-10-21 07:01:25.068 W Failed to get top block hash to check for new block's parent: MDB_NOTFOUND: No matching key/data pair found
2020-10-21 07:01:25.068 E Error adding block with hash: <68b837f89e8e80a33a5b4aec495133b22c581becad154b2861ce484f584b0d62> to blockchain, what = Failed to get top block hash to check for new block's parent: MDB_NOTFOUND: No matching key/data pair found
2020-10-21 07:01:25.069 W monerod is now disconnected from the network
2020-10-21 07:01:29.898 I [85.215.86.29:18080 OUT] Sync data returned a new top block candidate: 2081151 -> 2213093 [Your node is 131942 blocks (6.0 months) behind]
2020-10-21 07:01:29.899 I SYNCHRONIZATION started
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.441 E Failed to get tx meta from txpool
2020-10-21 07:01:30.442 E Failed to get tx meta from txpool
2020-10-21 07:01:30.442 E Failed to get tx meta from txpool
2020-10-21 07:01:30.442 E Failed to get tx meta from txpool
2020-10-21 07:01:30.442 E Failed to get tx meta from txpool
2020-10-21 07:01:30.446 E Failed to get tx meta from txpool
2020-10-21 07:01:30.446 E Failed to get tx meta from txpool
2020-10-21 07:01:30.447 E Failed to get tx meta from txpool
2020-10-21 07:01:30.448 E Failed to get tx meta from txpool
2020-10-21 07:01:30.448 E Failed to get tx meta from txpool
2020-10-21 07:01:30.450 W Failed to get top block hash to check for new block's parent: MDB_NOTFOUND: No matching key/data pair found
2020-10-21 07:01:30.450 E Error adding block with hash: <68b837f89e8e80a33a5b4aec495133b22c581becad154b2861ce484f584b0d62> to blockchain, what = Failed to get top block hash to check for new block's parent: MDB_NOTFOUND: No matching key/data pair found
2020-10-21 07:01:30.451 W monerod is now disconnected from the network






Is there any way to not have to resync all the blockchain ? Because apparently seeing the log something is corrupted right ?

Thank you all !!!

# Discussion History
## selsta | 2020-10-21T07:15:35+00:00
First make sure to upgrade to v0.17.1.1 and then wait a bit for it. If it still does not sync then it most likely is corrupted :/

## svpi11 | 2020-10-21T08:08:58+00:00
Ok thank you !
I will update latest release v0.17.1.1, wait a bit for the deamon to try to resync and see how does it go. 

## svpi11 | 2020-10-21T12:12:38+00:00
I upgraded to last version, let it search to resync but still the issue... :(


Is there is any other solution than just resync all monero blockchain from the beginning ? Maybe delete just some last blocks ? 
Thanks,

## selsta | 2020-10-21T12:16:00+00:00
> Is there is any other solution that just resync all monero blockchain from the beginning ? Maybe delete just some last blocks ?
Thanks,

Delete ~/.bitmonero/lmdb/data.mdb

## svpi11 | 2020-10-22T06:28:38+00:00
The problem is also I didn't want to delete data.mdb because it would take weeks again to download the entire blockchain.

But finally good news ! I achieve to make resync to the blockchain again this morning. :)

So to help if someone may have the same problem:

I did first delete the last corrupted blocks (around 500) with command line "monero-blockchain-import --pop-blocks n" where n is the number of blocks you want to delete.

Then I deleted also the file "lock.mdb" and "p2pstate.bin" file, and after this I ran again monerod, with the flag --block-sync-size 10, and let it run for a all night.

This morning, I exit and started again the daemon monerod normally, and it started again and followed the blockchain ! :)


Thanks !

# Action History
- Created by: svpi11 | 2020-10-21T07:13:38+00:00
- Closed at: 2020-10-22T06:57:12+00:00
