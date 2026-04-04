---
title: 'Synced from scratch 12.0.0 node on some strange chain '
source_url: https://github.com/monero-project/monero/issues/3743
author: kaykurokawa
assignees: []
labels: []
created_at: '2018-05-01T20:04:54+00:00'
updated_at: '2018-05-18T08:49:00+00:00'
type: issue
status: closed
closed_at: '2018-05-18T08:49:00+00:00'
---

# Original Description
Starting at block height 1546000  , my v 12.0.0 Monero (linux x64 version downloaded from https://github.com/monero-project/monero/releases ) that I synced from scratch (databae directory was cleared out before starting)  is on some strange chain that does not match with what I checked on explorer (both https://moneroblocks.info/ https://moneroexplorer.com). 

Here is what getblock for 1546000 looks like (respective explorer entry https://moneroexplorer.com/search?value=1546000) : 

{u'blob': u'0606abdd9cd60586d1d20a40cefcf3dd410ff6967e0491613b77bf73ea8f1bf2e335cf9cf7d57a6715002202ccae5e01ff90ae5e018e88f1cfca8d01023c306e3000c8dc568513d39127a4b6e2fa5e52b7bdcf4fabcef8b82e6e66aa7a2b01f9bce1e268114010f68d00e753f7cc0ad191cde7bd462290ae87996899e9a0b4020800021e01281c000000031028edfd8c5f7e80db749882b1f3b2cf310a106bdf4f914b45355dcb6ab21829860aab7963e314c44dc3aaa734eb120144869b6ac24cf54ee9d4be6bae7cc4af3f5721757df6d970829663f7089389d1d7605a799a20c9fcefb8e54ed949f6b1',
  u'block_header': {u'block_size': 40235,
                    u'depth': 12071,
                    u'difficulty': 134716086238,
                    u'hash': u'bb14a40058675e31a940b4fd685d46f245386ccc56e10f2e6951e2ba07f5a0f3',
                    u'height': 1546000,
                    u'major_version': 6,
                    u'minor_version': 6,
                    u'nonce': 570430823,
                    u'num_txes': 3,
                    u'orphan_status': False,
                    u'prev_hash': u'86d1d20a40cefcf3dd410ff6967e0491613b77bf73ea8f1bf2e335cf9cf7d57a',
                    u'reward': 4864754861070,
                    u'timestamp': 1523003051},
  u'json': u'{\n  "major_version": 6, \n  "minor_version": 6, \n  "timestamp": 1523003051, \n  "prev_id": "86d1d20a40cefcf3dd410ff6967e0491613b77bf73ea8f1bf2e335cf9cf7d57a", \n  "nonce": 570430823, \n  "miner_tx": {\n    "version": 2, \n    "unlock_time": 1546060, \n    "vin": [ {\n        "gen": {\n          "height": 1546000\n        }\n      }\n    ], \n    "vout": [ {\n        "amount": 4864754861070, \n        "target": {\n          "key": "3c306e3000c8dc568513d39127a4b6e2fa5e52b7bdcf4fabcef8b82e6e66aa7a"\n        }\n      }\n    ], \n    "extra": [ 1, 249, 188, 225, 226, 104, 17, 64, 16, 246, 141, 0, 231, 83, 247, 204, 10, 209, 145, 205, 231, 189, 70, 34, 144, 174, 135, 153, 104, 153, 233, 160, 180, 2, 8, 0, 2, 30, 1, 40, 28, 0, 0\n    ], \n    "rct_signatures": {\n      "type": 0\n    }\n  }, \n  "tx_hashes": [ "1028edfd8c5f7e80db749882b1f3b2cf310a106bdf4f914b45355dcb6ab21829", "860aab7963e314c44dc3aaa734eb120144869b6ac24cf54ee9d4be6bae7cc4af", "3f5721757df6d970829663f7089389d1d7605a799a20c9fcefb8e54ed949f6b1"\n  ]\n}',
  u'miner_tx_hash': u'ac847c89223482d9f19bb40ffe178c5c3d6330e0c5be8e33c0f1bd2adc782ac6',
  u'status': u'OK',
  u'tx_hashes': [u'1028edfd8c5f7e80db749882b1f3b2cf310a106bdf4f914b45355dcb6ab21829',
                 u'860aab7963e314c44dc3aaa734eb120144869b6ac24cf54ee9d4be6bae7cc4af',
                 u'3f5721757df6d970829663f7089389d1d7605a799a20c9fcefb8e54ed949f6b1'],
  u'untrusted': False},

Coincidentally, I'm also running a 11.1.0 node and I see the exact same block, so it looks like somehow the hard fork did not activate on my node? 


# Discussion History
## kaykurokawa | 2018-05-01T20:23:11+00:00
Here is output of RPC command hard_fork_info 

{u'earliest_height': 1546000,
  u'enabled': True,
  u'state': 2,
  u'status': u'OK',
  u'threshold': 0,
  u'untrusted': False,
  u'version': 7,
  u'votes': 0,
  u'voting': 7,
  u'window': 10080}



## moneromooo-monero | 2018-05-01T22:59:29+00:00
Did you sync 1546000 with 0.12.0.0, or 0.11.1.0 ? If 0.11.1.0, you need to pop blocks using 0.11.1.0 first (monero-blockchain-import --pop-blocks N, with N enough to go back to 1546000 or below). Then sync the rest with 0.12.0.0.

## kaykurokawa | 2018-05-02T01:01:05+00:00
Looking at the logs, it looks like I synced up to block 76412 with 0.11.1.0 

2018-04-20 18:52:02.816 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[155.33.87.231:58426 INC]  Synced 76312/1556038

And then, I updated it to 0.12.0  and finished syncing. Is it expected behavior that if I update in the middle of syncing that it goes to the wrong chain, and cannot recover? 



## moneromooo-monero | 2018-05-02T09:45:53+00:00
No, you should be good as long as you switched to 0.12.0.0 before 1546000, which you seem to have done, but getting a v6 block there implies you synced it with 0.11.1.0, so that's odd. Are you sure you did not restart 0.11.1.0 after installing 0.12.0.0 ?

## moneromooo-monero | 2018-05-18T08:34:31+00:00
Some sync bugs were fixed, release-0.12 is now up to date with all fixes.

+resolved

# Action History
- Created by: kaykurokawa | 2018-05-01T20:04:54+00:00
- Closed at: 2018-05-18T08:49:00+00:00
