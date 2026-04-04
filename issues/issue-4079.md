---
title: Genesis block hash mismatch on stagenet if --data-dir option is not set
source_url: https://github.com/monero-project/monero/issues/4079
author: naughtyfox
assignees: []
labels:
- invalid
created_at: '2018-06-29T14:33:56+00:00'
updated_at: '2018-07-12T22:41:01+00:00'
type: issue
status: closed
closed_at: '2018-07-12T22:41:01+00:00'
---

# Original Description
Reproduced with both `0.12.0` and `0.12.2.0` versions.

I'm trying to sync stagenet blockchain from scratch. At first, I have the following bitmonero-home directory structure:
```
/home/user/.bitmonero/
├── bitmonero.log
├── lmdb
│   ├── data.mdb
│   └── lock.mdb
├── monero-blockchain-import.log
├── monerod.conf
├── monero-wallet-cli.log
├── p2pstate.bin
└── testnet
    ├── 38080
    │   └── p2pstate.bin
    ├── 48080
    │   └── p2pstate.bin
    ├── 88080
    │   └── p2pstate.bin
    ├── bitmonero.log
    ├── lmdb
    │   ├── data.mdb
    │   └── lock.mdb
    └── p2pstate.bin
```
then i start my `monerod` as follows:
```
$ ./bitmonerod --stagenet --log-level=2
```
and a lot of errors like (full log is here - https://www.dropbox.com/s/jyte292csmvxj9c/bitmonero.log?dl=0):
```
2018-06-29 13:58:52.300	[P2P5]	ERROR	net.p2p	src/cryptonote_core/blockchain.cpp:2011	Client sent wrong NOTIFY_REQUEST_CHAIN: genesis block mismatch: 
id: <96375dc8a8dd960c33f59190edf51a3f458d6e8d8a2c7bc7517c5dee26955174>, 
expected: <76ee3cc98646292206cd3e86f74d88b4dcc1d937088645e9b0cbca84b7ce74eb>,
 dropping connection
```
after deleting `~/.bitmonero/stagenet` directory and restarting daemon with `--data-dir` option being set to default value it works just fine:
```
$ rm -rf ~/.bitmonero/stagenet && ./monerod --stagenet --log-level=2 --data-dir=/home/user/.bitmonero/stagenet
````
log:
```
2018-06-29 14:33:17.373	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[18.191.223.168:38080 OUT]  Synced 11600/107757
2018-06-29 14:33:18.110	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[18.191.223.168:38080 OUT]  Synced 11620/107757
2018-06-29 14:33:18.798	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[18.191.223.168:38080 OUT]  Synced 11640/107757
2018-06-29 14:33:19.607	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[92.35.34.106:38080 OUT]  Synced 11660/107757

```

# Discussion History
## moneromooo-monero | 2018-06-29T16:01:49+00:00
I'd want to see a level 2 log of the other nodes, the ones sending the apparently wrong block. AFAICT this is a problem on the other side, which is odd since there are many having it...



## stoffu | 2018-06-30T01:27:29+00:00
FWIW a web search with that block ID led me to these scamcoins:

- https://explorer.getlotto.io/block/c23f87a0cec573c043ce9b255a4693a2369cc4376ea62c87156b53ff8d80fc4e

- https://explorer.goprivatepay.com/block/46ef0cca046bc20581bbd5af8ab2ced70d3f1afec36340bad9d54623150bec3d


## naughtyfox | 2018-07-02T10:33:28+00:00
I accidentally noticed that if start daemon with option `--data-dir=~/.bitmonero/stagenet` it create directory `~` in cwd.

## moneromooo-monero | 2018-07-02T13:22:19+00:00
~ is a bash thing. If you use another shell, it won't replace it. Use $HOME instead.

## naughtyfox | 2018-07-02T13:30:21+00:00
but i use bash and apparently it doesn't expand the wildcard

## hyc | 2018-07-02T13:56:46+00:00
This isn't the place to discuss how Bash works.

## moneromooo-monero | 2018-07-02T15:04:31+00:00
But drop the = if you want bash to see it.

## moneromooo-monero | 2018-07-12T22:11:19+00:00
+invalid

# Action History
- Created by: naughtyfox | 2018-06-29T14:33:56+00:00
- Closed at: 2018-07-12T22:41:01+00:00
