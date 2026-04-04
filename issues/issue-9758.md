---
title: v0.18.4.0 release to-do list
source_url: https://github.com/monero-project/monero/issues/9758
author: selsta
assignees: []
labels: []
created_at: '2025-01-31T17:14:22+00:00'
updated_at: '2025-04-05T21:28:00+00:00'
type: issue
status: closed
closed_at: '2025-04-05T21:27:59+00:00'
---

# Original Description
The following pull requests have to be merged, tests have to be done and issues have to be resolved.

- [x] #9722
- [x] #9823
- [x] #9687
- [x] #9807
- [x] #9740 
- [x] #9759
- [x] #8617
- [x] #9775 
- [x] #9793
- [x] #9805
- [x] #9755
- [x] https://github.com/monero-project/monero/pull/9844
- [x] https://github.com/monero-project/monero/pull/9459#issuecomment-2677282415
- [x] #9862
- [X] #9864
- [X] Test a full chain sync
- [x] Investigate the issue reported by woodser about transactions not propagating in his test suite
- [x] Tag v0.18.4.0
- [x] Release on website

Any other PRs that I'm missing?

# Discussion History
## jeffro256 | 2025-02-17T18:19:07+00:00
We should add #9805 

## jeffro256 | 2025-02-24T07:44:18+00:00
https://github.com/monero-project/monero/pull/9459#issuecomment-2677282415

## MaxXor | 2025-03-11T18:46:34+00:00
So only the dependency bump to boost 1.69.0  is pending until we can see a release?

## selsta | 2025-03-11T18:50:16+00:00
@MaxXor it will need good testing before we put out the release

## MaxXor | 2025-03-11T18:54:52+00:00
That's definitely right. I'll happily help testing and spin up a 2nd monero node once all necessary PRs are merged.

## fxrstor | 2025-03-14T14:47:40+00:00
> That's definitely right. I'll happily help testing and spin up a 2nd monero node once all necessary PRs are merged.

@MaxXor All PRs are merged.

## SyntheticBird45 | 2025-03-14T20:25:40+00:00
@selsta https://libera.monerologs.net/monero-dev/20250314#c509956

Please check `Investigate the issue reported by woodser about transactions not propagating in his test suite` as completed.

## MaxXor | 2025-03-16T08:16:36+00:00
> [@MaxXor](https://github.com/MaxXor) it will need good testing before we put out the release

I can not complete a full chain sync with v0.18.4.0-88a5d0768. Worked fine till fork version v11. Then it's stuck with "Failed to parse transaction from blob" at Height: 1788724/3368917 (53.1%) on mainnet,

See here: https://github.com/monero-project/monero/issues/4833#issuecomment-2727256300

## selsta | 2025-03-16T11:32:32+00:00
@MaxXor how did you compile it? Which OS are you using?

## MaxXor | 2025-03-16T13:42:06+00:00
I simply followed the [build instructions](https://github.com/monero-project/monero?tab=readme-ov-file#on-linux-and-macos) on a ubuntu 22.04 x64 vm. I've built a debug and release build using `make -j8 debug` and `make -j8 release`. Both builds can not continue to sync the chain anymore.

I've adjusted the log level and got a more detailed error, it's always the same transaction:

```
2025-03-16 13:39:06.908	E Failed to parse transaction from blob
2025-03-16 13:39:06.908	E failed to parse and/or validate unpruned transaction as inside block: 02000202000bdbc3bd02bddd2cc8ed58ce9824fdcf38f261f5e703ce9a0372f902f404a984c981b93bbb9d12ed04a1142b7d50d7753e8b695c55c3111f6373526b25ac02000b83cf8b04e69104b9f705e2c30ba2ad02b389029da301a505c83c8c0be21d38d6473dab3bf768878357f9146ffb1c52170053b3a17b30ebeb4b73c5b283710300024a84dbc4cd899233eb0eacd59cf83028087039b3c4c15305cf18f4c0ddda7871000252780fccaea64837153ec335e88163b3f487ea8b13565d825470f904849b253e0002fd190824adbaf60911943c368c8fa82d1d9d98954045c6cf150fecf66e16dcdf2101f7740c382c979fd5de1d25703d9f6fb057642ff0734945c6794e04a5c699901204f0f1dd1fa023e9fbe701818859a6d18ba6dc732b0bfa8d295c8d6e5428621bd49666c0c5e42903b620fd6ae5409200ed08e786abb7e3a6c986f85a03f29729a1e007df5ceb6e41861ea42dfe9ccef52c2ce5dc66b92ba382a4717ef6c7231a452eca74eeefde6d09b53effafddf6909360ae022be2decb63a2ffe644
```

## selsta | 2025-03-16T13:43:50+00:00
Did you set the prune-blockchain flag?

## MaxXor | 2025-03-16T13:46:45+00:00
Yes correct, I'm using the following config:

```
data-dir=/mnt/data/monero-data
log-file=/tmp/monerod.log

log-level=1

p2p-bind-ip=0.0.0.0
p2p-bind-port=18080
public-node=false

rpc-restricted-bind-ip=0.0.0.0
rpc-restricted-bind-port=18089

prune-blockchain=true
sync-pruned-blocks=true
enable-dns-blocklist=true
no-igd=true
no-zmq=true
```

## selsta | 2025-03-16T13:48:08+00:00
Just to confirm, /mnt/ is not a network share?

## MaxXor | 2025-03-16T13:49:42+00:00
Yes, it's a local partition on a NVMe SSD.

## MaxXor | 2025-03-16T15:34:45+00:00
Just a follow-up. I've tried to sync another machine using the same config, in the hope that it was a simple db corruption. This time using debian 12 x64. It's stuck at a different height. Height: 1789952/3369125 (53.1%) on mainnet

```
2025-03-16 15:32:03.421	E Failed to parse transaction from blob
2025-03-16 15:32:03.421	E failed to parse and/or validate unpruned transaction as inside block: 02000102000bf0adf703fdda19c677ebc109dfda06979f04d3228a8c018b34b82fed092b92e0eba22e32a54bd9018620d1d4ae69ea825b4db7ceb2385c17a5fb31070b020002940528d70a2fc98b6153b79565088a8b2deeb1593129fed23a917a324f38a7f4000215fcb861ebd300c3974b01ca5d56df4b20d6e47bc4adc15918eca5ac7bbefb8844022100eac8d74212d16694be4565b003d4fa406b41a2577e6f5fca0dd679d263133fdd01b2c7fc14c2a4c3fea28d64ecf7cb5cb78b3ce564272d22822daaf6c78890af6b04a0cca01afbc2bbf9dd3cb80082964cbfae182d7842ab685c0981888cb4ae08be461e88c4daf76f3710f761fced214b83584aee8612f3bee8930c49e211482d5355871193b9d2545f1cfcab7d160b57f2e319cec6
```

## selsta | 2025-03-16T16:34:01+00:00
@MaxXor one last test, can you try to build v0.18.3.4 in the same environment and sync? Just to make sure it is something introduced recently.

## MaxXor | 2025-03-16T16:53:03+00:00
@selsta Sure, no worries. Two things:

1) Sync works fine using v0.18.3.4 built @ b089f9ee69924882c5d14dd1a6991deb05d9d1cd on both ubuntu 22.04 and debian 12. I just continued at the old block height where the nodes where previously stuck and didn't sync from scratch. Then switched back to the "broken" build and sync is stuck again. So it looks like a regression in v0.18.4.0 starting at fork version 11.

2) I encountered an error when trying to compile the v0.18.3.4 debug build, similar to #9486 but that's fixed already in 0.18.4.0, so the issue can be closed I think.
```
/usr/bin/ld: CMakeFiles/obj_epee_readline.dir/readline_buffer.cpp.o: in function `handle_line(char*)':
/repos/monero/contrib/epee/src/readline_buffer.cpp:177: undefined reference to `epee::string_tools::trim_right(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&)'
collect2: error: ld returned 1 exit status
```

## MaxXor | 2025-03-16T17:47:08+00:00
@selsta I bisected the regression down to this commit: https://github.com/monero-project/monero/commit/3da68db9789697d30dc309df2f1da5d348bc4ce2

Syncing v11 blocks works fine without this commit in [v0.18-branch](https://github.com/monero-project/monero/tree/release-v0.18).

## selsta | 2025-03-16T17:48:45+00:00
thank you, I'll ask @jeffro256 to take a look

## nahuhh | 2025-03-16T18:06:14+00:00
@MaxXor  does the gitian build also choke for you?

https://github.com/nahuhh/monero/actions/runs/13813130711

## MaxXor | 2025-03-16T18:15:05+00:00
@nahuhh Yes, same error.
```
2025-03-16 18:13:10.049	I [137.220.65.28:18080 OUT] Sync data returned a new top block candidate: 1825840 -> 3369197 [Your node is 1543357 blocks (5.9 years) behind] 
2025-03-16 18:13:10.049	I SYNCHRONIZATION started
2025-03-16 18:13:10.874	E Failed to parse transaction from blob
2025-03-16 18:13:10.941	I [135.181.5.233:18080 OUT] Sync data returned a new top block candidate: 1825840 -> 3369197 [Your node is 1543357 blocks (5.9 years) behind] 
2025-03-16 18:13:10.941	I SYNCHRONIZATION started
2025-03-16 18:13:11.357	E Failed to parse transaction from blob
2025-03-16 18:13:16.054	I [51.195.199.246:28080 OUT] Sync data returned a new top block candidate: 1825840 -> 3369197 [Your node is 1543357 blocks (5.9 years) behind] 
2025-03-16 18:13:16.054	I SYNCHRONIZATION started
2025-03-16 18:13:16.391	E Failed to parse transaction from blob
2025-03-16 18:13:17.846	I [69.57.194.208:18080 OUT] Sync data returned a new top block candidate: 1825840 -> 3369197 [Your node is 1543357 blocks (5.9 years) behind] 
2025-03-16 18:13:17.846	I SYNCHRONIZATION started
2025-03-16 18:13:18.835	E Failed to parse transaction from blob
```

## Gingeropolous | 2025-03-16T21:27:23+00:00
reproduced:

2025-03-16 20:24:11.935 [P2P3]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:679  calculated batch size: 92160000
2025-03-16 20:24:11.935 [P2P3]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:688  increase size: 536870912
2025-03-16 20:24:11.935 [P2P7]  DEBUG   cn.block_queue  src/cryptonote_protocol/block_queue.cpp:236     reserve_span: first_block_height 1800012, last_block_height 1804799, max 20, pe>
2025-03-16 20:24:11.935 [P2P3]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:640  DB map size:     32560003072
2025-03-16 20:24:11.935 [P2P3]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:641  Space used:      21881933824
2025-03-16 20:24:11.935 [P2P3]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:642  Space remaining: 10678069248
2025-03-16 20:24:11.935 [P2P3]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:643  Size threshold:  92160000
2025-03-16 20:24:11.935 [P2P7]  DEBUG   cn.block_queue  src/cryptonote_protocol/block_queue.cpp:273     span_start_height: 1800012
2025-03-16 20:24:11.935 [P2P1]  INFO    net.p2p.traffic contrib/epee/include/net/levin_protocol_handler_async.h:56      [116.202.196.114:18080 OUT] 114792 bytes received for category >
2025-03-16 20:24:11.935 [P2P3]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:645  Percent used: 67.2050  Percent threshold: 90.0000
2025-03-16 20:24:11.935 [P2P7]  DEBUG   cn.block_queue  src/cryptonote_protocol/block_queue.cpp:308     Reserving span 1800012 - 1800031 for f32c341f-7a28-43bd-9176-76b0a5216c32
2025-03-16 20:24:11.935 [P2P1]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1003    [116.202.196.114:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECT>
**2025-03-16 20:24:11.935 [P2P3]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:257    Failed to parse transaction from blob**
2025-03-16 20:24:11.935 [P2P1]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1004    [116.202.196.114:18080 OUT] [0] state: received objects in state synchr>
2025-03-16 20:24:11.935 [P2P3]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:108     failed to parse and/or validate unpruned transaction as inside block: 0>
2025-03-16 20:24:11.935 [P2P7]  DEBUG   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2174    [23.122.200.162:18080 OUT]  span from 1800012: 1800012/20
2025-03-16 20:24:11.935 [P2P1]  DEBUG   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [116.202.196.114:18080 OUT]  downloaded 98084 bytes worth of blocks
2025-03-16 20:24:11.935 [P2P3]  WARNING net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2800    dropping connections to 168.119.166.230:18080
2025-03-16 20:24:11.935 [P2P3]  DEBUG   net.p2p src/p2p/net_node.inl:416        Host 168.119.166.230 fail score=5
2025-03-16 20:24:11.935 [P2P7]  DEBUG   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2211    [23.122.200.162:18080 OUT]  span: 1800012/20 (1800012 - 1800031)
2025-03-16 20:24:11.935 [P2P3]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1477    [74.214.239.120:18080 OUT] span connection id not found
2025-03-16 20:24:11.935 [P2P3]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2123 Pruning blockchain...
2025-03-16 20:24:11.936 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:2258    [23.122.200.162:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: bloc>
2025-03-16 20:24:11.936 [P2P7]  DEBUG   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2262    Asking for pruned data, start/end 8/8, ours 6, peer stripe 0


## nahuhh | 2025-03-16T23:49:10+00:00
Reproduced as well

note from @Boog900
> 9135 added a check that rejected any pruned downloaded txs: https://github.com/monero-project/monero/blob/f90a267fa34bad095d7e8ba72ee78f2a63f37df6/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L106
> V11 is just when we start asking for pruned blocks
> https://github.com/monero-project/monero/blob/f90a267fa34bad095d7e8ba72ee78f2a63f37df6/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1966

https://libera.monerologs.net/monero-dev/20250316#c511012

## fxrstor | 2025-03-17T13:55:14+00:00
@selsta 

## nahuhh | 2025-03-17T22:03:26+00:00
@U65535F jsyk, selsta is notified on every comment. You dont have to ping repeatedly

## MaxXor | 2025-03-24T19:41:53+00:00
Full sync successfully completed using release build @ 4b7263d5879c6f8da4f4466829cdf640e57de4c1 with `prune-blockchain=true` and `sync-pruned-blocks=true`.

## nahuhh | 2025-03-24T21:58:31+00:00
> Full sync successfully completed using release build @ 4b7263d5879c6f8da4f4466829cdf640e57de4c1 with `prune-blockchain=true` and `sync-pruned-blocks=true`.

What was your sync time from start til 1. checkpoint 2. finish?

thanks

## selsta | 2025-03-26T13:16:54+00:00
v0.18.4.0 tag is scheduled for Friday if no new bugs are found. In the meantime more chain testing would be great.

## selsta | 2025-04-05T21:27:59+00:00
https://www.getmonero.org/2025/04/05/monero-0.18.4.0-released.html

# Action History
- Created by: selsta | 2025-01-31T17:14:22+00:00
- Closed at: 2025-04-05T21:27:59+00:00
