---
title: Checkpoint failure on height 1288616
source_url: https://github.com/monero-project/monero/issues/2025
author: clefru
assignees: []
labels: []
created_at: '2017-05-10T13:52:46+00:00'
updated_at: '2017-05-15T22:52:08+00:00'
type: issue
status: closed
closed_at: '2017-05-15T16:34:38+00:00'
---

# Original Description
On my initial sync, my local copy of the blockchain got corrupted and can't seem to unstick itself.  

2017-05-10 14:22:25.245 [P2P2]  WARN    checkpoints     src/cryptonote_basic/checkpoints.cpp:85 CHECKPOINT FAILED FOR HEIGHT 1288616. EXPECTED HASH: <875ac1bc7aa6c5eedc5410abb9c694034f9e7f79dce4c60698baf37009cb6365>, FETCHED HASH: <1e6b1019968d4a33b281ab70d83947bc051ac952f26dd2693c427b04d82151fe>

My copy doesn't seem to be unique: https://bitcointalk.org/index.php?topic=1875775.0

I would assume that the corrupted chain is of interest for investigation. Please let me know if I should serve a copy somewhere. 

# Discussion History
## moneromooo-monero | 2017-05-13T18:43:24+00:00
Exit monerod, restart it with --log-level 2, post the relevant part of the log till the error on fpaste.org.

## binhminhcc1990 | 2017-05-13T19:07:29+00:00
i'am sorry, but what is this (monero-v0.10.3.1), i do not understand how to
dig monero. tôi đã làm theo chỉ đẫn nhưng toi van ko hiểu file đó dùng để
làm gì, có phải để đào monero không, nếu vậy thì làm sao biết được mình đào
được bao nhiêu

2017-05-14 2:43 GMT+08:00 moneromooo-monero <notifications@github.com>:

> Exit monerod, restart it with --log-level 2, post the relevant part of the
> log till the error on fpaste.org.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2025#issuecomment-301266968>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AaZ_f9E3jdDyOTC6GhJg09dElwRSsuz4ks5r5fnOgaJpZM4NWsnr>
> .
>


## moneromooo-monero | 2017-05-13T20:11:13+00:00
Run monerod the same way you normally do, but add " --log-level 2" to the command line. This will make monerod print more logs.

## clefru | 2017-05-14T13:23:23+00:00
@moneromooo-monero: That's the best I could find:

```
[0m[32m2017-05-14 11:41:33.026	[P2P1]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:900	[1;33mGot NEW BLOCKS inside of handle_response_get_objects: size: 200[0m
[0m[36m2017-05-14 11:41:33.026	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:547	[check_and_resize_for_batch] checking DB size
[0m[36m2017-05-14 11:41:33.026	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:601	[get_estimated_batch_size] m_height: 1288639  block_start: 1288139  block_stop: 1288638
[0m[36m2017-05-14 11:41:33.027	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:629	average block size across recent 500 blocks: 57418
[0m[36m2017-05-14 11:41:33.027	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:633	estimated average block size for batch: 57418
[0m[36m2017-05-14 11:41:33.027	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:554	calculated batch size: 1291905024
[0m[36m2017-05-14 11:41:33.027	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:563	increase size: 1291905024
[0m[36m2017-05-14 11:41:33.027	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:511	DB map size:     20174168064
[0m[36m2017-05-14 11:41:33.027	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:512	Space used:      14243409920
[0m[36m2017-05-14 11:41:33.027	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:513	Space remaining: 5930758144
[0m[36m2017-05-14 11:41:33.027	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:514	Size threshold:  1291905024
[0m[36m2017-05-14 11:41:33.027	[P2P1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:516	Percent used: 0.7060  Percent threshold: 0.8000
[0m[32m2017-05-14 11:41:33.027	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3641	block_batches: 50
[0m[32m2017-05-14 11:41:33.027	[P2P1]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3664	Skipping prepare blocks. New blocks don't belong to chain.
[0m[32m2017-05-14 11:41:33.027	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <fc3ff84c4dd7930a5bb6c3d5e12ffb1eb599a7894c98764f2de60836958bb72a> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.028	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <92e35209af82107fcbe0b85cd637f823c5f54046a732634c9a0d461a52f7895f> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.028	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <664fe1ca1e29b8d939ab6caa849cb212715d715504e32c1c2bdb1e1f6e71824c> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.029	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <d88db941f551110f862e6a780f0fc437403aedde4d048643aaa813ed7936b314> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.029	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <ca2b650c14191de73378e5ae2d4d73f2ea743e447aaf45173b370d4b46398973> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.030	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <98efa2b1fb46a631059832d2585d344710733324594913d8bb5fe2c737a1b92f> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.030	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <486095b55b3319306a3c8e4a5a72e715ae0062704bfc5c62b6b932f90f6b52f4> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.030	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <a1c8cf89150cbd34ca29a815736b43efd8132b71b660c0ef602c968fa3bd66d2> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.031	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <a35dcdfa3977abbe13783cd503e14a2f592dc886cbfe1bca9ccdd7e22928a473> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.031	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <795a4939b6def5c6dceb42732c6b452039beca014a9fad2b6c46537e554cbfee> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.032	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <999d7a8f1558e3ee05f20a83dd93e1e9ede98e414087d235d685a06b1c8eef65> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.032	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <33e0ea4de9f66c5455695f4f676d5ec5abe1ecaae1988fc4a9e3600537bf518f> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.032	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <ae2dfc8521a25403795f5949df06243e2608431cd67aef612cc91ef1b5152f50> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.033	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <c2e481a71a1ca88199275ee1a8d5a81eb978ef596d4cdac6a67736dbbdeb993e> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.033	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <d4f76e0e152b60174dd6d4cfb2e1c7307bca963643e5c54077bfbab2c4625048> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.034	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <6a584fa26827e80a380ed391f9f2bbd2276e021f57124e633027c5403791d408> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.034	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <14857013b6539c9d04cb5abe4ea1770656e0d47b87351a3d4e05ea32f8c0b995> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.034	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <1871a872865dcf7e399d03363ef753286e0b69d79561752662716b0bbf184d17> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.035	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <4dade576d19f72469e189837f4d21bc0295bcde4cead4b6f8b368a4254ade643> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.035	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <665d45bef422994f0a0daf120ab11f3c8205ba128277a15af192e5bd84237e1d> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.036	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <9741bb92b171b29ec064ca77619bbbd3130d305e46fa70832bd463ccb885f2ce> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.036	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <45ec3741d71b10116595e5c104513e36d30fcea5d88de97bf9c44fa96fa97575> already have transaction in blockchain
[0m[32m2017-05-14 11:41:33.037	[P2P1]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:528	tx <9c65d8870fda987f7e3b1b8b999eb5d45a364f9b6101b3f84474672c5b4a4eac> already have transaction in blockchain
[0m[36m2017-05-14 11:41:33.037	[P2P1]	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:1276	Block with id: <875ac1bc7aa6c5eedc5410abb9c694034f9e7f79dce4c60698baf37009cb6365>
has old version for height 1288616
[0m[36m2017-05-14 11:41:33.037	[P2P1]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:972	[70.59.202.16:18080 OUT] Block verification failed, dropping connection
```

## moneromooo-monero | 2017-05-14T13:33:03+00:00
Your blockchain might be corrupt. But just in case you're only hitting bad peers, do this:
Exit monerod, rm ~/.bitmonero/p2pstate.bin, restart monerod.
If that still doesn't work, resync from scratch.



## clefru | 2017-05-14T14:36:33+00:00
@moneromooo-monero: rm-oing p2pstate didn't affect the behavior.

What's interesting is that my monerod doesn't think about the block as orphaned.

```$ curl -X POST http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getblock","params":{"hash":"1e6b1019968d4a33b281ab70d83947bc051ac952f26dd2693c427b04d82151fe"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "blob": "0405f498c4c705bc704ee138fdb7b12148bca85cc25a42ec8df0bf085523f544a2ff63e258812ccc65000002e4d34e01ffa8d34e01affb93d9a4e9010245a6d6295c00d6778d049b790d9e0514f9545af3714548be377ae86cfbcc7edf2b01a3d1dac6c32c4a9db217d5484597065b8710cc611fd621b395531f547a94fa3b0208000000472f30e1d20005d94d91eddd6e9955ff69caf9323ad846c4584bd6f0b0e932ab4287c0a3a03b9b53307fdf8f8fc62864b37752f5893a9722f060bb7d0ab8f565caed27bccd56465ca03ee4724e881dc5a5eddf5da007c6256959b9ffb7acb13d5f79b7726a0563c6e07a6852387334dbdc34295892dff9a54a4867dbea45f867d6f44dffba6c21f25fcd33b949da79c7fafab46270c3dfcc20031c148284bc3cd5b9375597f06b",
    "block_header": {
      "block_size": 66414,
      "depth": 22,
      "difficulty": 9718310133,
      "hash": "1e6b1019968d4a33b281ab70d83947bc051ac952f26dd2693c427b04d82151fe",
      "height": 1288616,
      "major_version": 4,
      "minor_version": 5,
      "nonce": 26060,
      "num_txes": 5,
      "orphan_status": false,
      "prev_hash": "bc704ee138fdb7b12148bca85cc25a42ec8df0bf085523f544a2ff63e258812c",
      "reward": 8015669689775,
      "timestamp": 1492192372
    },
    "json": "{\n  \"major_version\": 4, \n  \"minor_version\": 5, \n  \"timestamp\": 1492192372, \n  \"prev_id\": \"bc704ee138fdb7b12148bca85cc25a42ec8df0bf085523f544a2ff63e258812c\", \n  \"nonce\": 26060, \n  \"miner_tx\": {\n    \"version\": 2, \n    \"unlock_time\": 1288676, \n    \"vin\": [ {\n        \"gen\": {\n          \"height\": 1288616\n        }\n      }\n    ], \n    \"vout\": [ {\n        \"amount\": 8015669689775, \n        \"target\": {\n          \"key\": \"45a6d6295c00d6778d049b790d9e0514f9545af3714548be377ae86cfbcc7edf\"\n        }\n      }\n    ], \n    \"extra\": [ 1, 163, 209, 218, 198, 195, 44, 74, 157, 178, 23, 213, 72, 69, 151, 6, 91, 135, 16, 204, 97, 31, 214, 33, 179, 149, 83, 31, 84, 122, 148, 250, 59, 2, 8, 0, 0, 0, 71, 47, 48, 225, 210\n    ], \n    \"rct_signatures\": {\n      \"type\": 0\n    }\n  }, \n  \"tx_hashes\": [ \"d94d91eddd6e9955ff69caf9323ad846c4584bd6f0b0e932ab4287c0a3a03b9b\", \"53307fdf8f8fc62864b37752f5893a9722f060bb7d0ab8f565caed27bccd5646\", \"5ca03ee4724e881dc5a5eddf5da007c6256959b9ffb7acb13d5f79b7726a0563\", \"c6e07a6852387334dbdc34295892dff9a54a4867dbea45f867d6f44dffba6c21\", \"f25fcd33b949da79c7fafab46270c3dfcc20031c148284bc3cd5b9375597f06b\"\n  ]\n}",
    "status": "OK",
    "tx_hashes": ["d94d91eddd6e9955ff69caf9323ad846c4584bd6f0b0e932ab4287c0a3a03b9b","53307fdf8f8fc62864b37752f5893a9722f060bb7d0ab8f565caed27bccd5646","5ca03ee4724e881dc5a5eddf5da007c6256959b9ffb7acb13d5f79b7726a0563","c6e07a6852387334dbdc34295892dff9a54a4867dbea45f867d6f44dffba6c21","f25fcd33b949da79c7fafab46270c3dfcc20031c148284bc3cd5b9375597f06b"]
  }
}
```
Probably that is because my node has about 22 blocks on-top of that block:

```
$ curl -X POST http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"on_getblockhash","params":[1288638]}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": "6787eef14f031f4da3e4e41431a251824e2f091eecaeb8486f3b83257abf5670"
}
curl -X POST http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"on_getblockhash","params":[1288639]}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": "0000000000000000000000000000000000000000000000000000000000000000"
}
```

Also just as a remark: I was not asking for support. I know how to wipe and resync. I was filing this issue because I expected the project to have an interest in nodes self-healing from bad state, and an example for bad state is what I could provide. Please close, if that's not interesting to you || no time for this.


## moneromooo-monero | 2017-05-14T16:50:28+00:00
It is interesting, and it should work. But the logs provided seem to show corruption, rather than the original issue (failed checkpoint).

## perl5577 | 2017-05-14T18:15:31+00:00
monerod is just not updated to 0.10.3.1.
run command : "monerod --version"


## moneromooo-monero | 2017-05-14T18:19:51+00:00
A comment above does say it's 0.10.3.1.

## clefru | 2017-05-14T18:25:45+00:00
$ monerod --version                                                                                                                          Monero 'Wolfram Warptangent' (v0.10.2.1-release)

Indeed, I am running an outdated version. Sorry for the noise. (Picked my distro's packaging without looking)

## clefru | 2017-05-15T16:34:37+00:00
Monero 0.10.3.1 syncs for me.

Maybe provide a github issue template text that requests people to state their version number. Sorry again for the waste of time.


## danrmiller | 2017-05-15T16:46:19+00:00
@clefru What distribution? We should contact the maintainer if they need to update.

## clefru | 2017-05-15T22:52:08+00:00
@danmiller: NixOS. I already sent a PR :) https://github.com/NixOS/nixpkgs/issues/25806

# Action History
- Created by: clefru | 2017-05-10T13:52:46+00:00
- Closed at: 2017-05-15T16:34:38+00:00
