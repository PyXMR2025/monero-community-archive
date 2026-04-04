---
title: Errors in monero-wallet-rpc console output
source_url: https://github.com/monero-project/monero/issues/6229
author: nikitasius
assignees: []
labels: []
created_at: '2019-12-12T19:04:51+00:00'
updated_at: '2020-04-28T17:58:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
- I run `monerod` and `monero-wallet-rpc`.
- Version is `Monero 'Carbon Chamaeleon' (v0.15.0.1-release)`
- main network

actual log output from wallet-rpc:
```
2019-11-30 08:25:34.376 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3509     Detaching blockchain on height 1978107
2019-11-30 08:25:34.377 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3579     Detached blockchain on height 1978107, transfers detached 0, blocks detached 1
2019-11-30 20:27:08.978 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3509     Detaching blockchain on height 1978491
2019-11-30 20:27:08.978 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3579     Detached blockchain on height 1978491, transfers detached 0, blocks detached 1
2019-12-01 06:07:30.999 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3509     Detaching blockchain on height 1978956
2019-12-01 06:07:30.999 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3579     Detached blockchain on height 1978956, transfers detached 0, blocks detached 1
2019-12-01 21:54:06.718 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3509     Detaching blockchain on height 1979516
2019-12-01 21:54:06.719 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3579     Detached blockchain on height 1979516, transfers detached 0, blocks detached 1
2019-12-01 21:58:26.861 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3509     Detaching blockchain on height 1979518
2019-12-01 21:58:26.861 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3579     Detached blockchain on height 1979518, transfers detached 0, blocks detached 1
2019-12-04 10:20:01.385 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3509     Detaching blockchain on height 1981383
2019-12-04 10:20:01.385 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3579     Detached blockchain on height 1981383, transfers detached 0, blocks detached 1
2019-12-04 20:59:44.768 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:911    wrong number of additional derivations
2019-12-04 21:02:24.960     {HAD 12 symbols hash, i removed}        ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:911    wrong number of additional derivations
2019-12-04 21:06:25.221     {HAD 12 symbols hash, i removed}        ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:911    wrong number of additional derivations
2019-12-05 11:35:30.849 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3509     Detaching blockchain on height 1982145
2019-12-05 11:35:30.877 [RPC0]  WARNING wallet.wallet2  src/wallet/wallet2.cpp:3579     Detached blockchain on height 1982145, transfers detached 0, blocks detached 1
2019-12-08 19:59:03.424 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1122   Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:03.425 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1122   Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:03.425 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1031   Failed to calculate transaction hash
2019-12-08 19:59:23.444 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1122   Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:23.444 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1122   Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:23.444 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1031   Failed to calculate transaction hash
2019-12-08 19:59:43.461 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1122   Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:43.461 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1122   Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:43.461 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1031   Failed to calculate transaction hash
2019-12-08 20:00:03.477 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1122   Cannot calculate the hash of a pruned transaction
2019-12-08 20:00:03.478 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1122   Cannot calculate the hash of a pruned transaction
2019-12-08 20:00:03.478 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1031   Failed to calculate transaction hash
```

Server config is (just removed p2p bind addr and rpc bind addresses and credentials):
```
confirm-external-bind=0
restricted-rpc=1
no-igd=1

db-sync-mode=safe

enforce-dns-checkpointing=1

out-peers=64
in-peers=1024

limit-rate-up=1048576
limit-rate-down=1048576
```

Wallet config (RPC) contains credentials and wallet.

All this run in Debian 9x64, have 10Gbit network, 2x NVMe in raid and 2x Gold xeons with 96Gb Ram.

Loooks similar to #5739 but:
* nothing hangs, all continue work
* daemon continue be up to date (compared with xmrchain data)\
* sometimes daemon losing connections or have:
  * `2019-12-09 21:39:13.986 I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1985327`
  * `2019-12-10 01:43:53.764 W ge_frombytes_vartime failed at 445` -- what does this mean btw?

# Discussion History
## moneromooo-monero | 2019-12-14T16:49:54+00:00
Is your node pruned ?

## moneromooo-monero | 2019-12-14T17:59:23+00:00
The "wrong number of additional derivations" message is fine. I found a tx in your log's range which has one additional pubkey and two outputs, which triggers this. The tx is technically correct, but likely created by wonky software. This is one thing to add constraints on if we end up parsing extra in consensus, which we're currently not.

The tx hash messages seem wrong. Something somewhere wants to calc a txid, possibly a log. It's not clear what.


## normoes | 2020-01-08T16:32:29+00:00
@moneromooo-monero 

We also see those errors.

Coincidentally, whenever they happen, our clients (that connect to the wallet RPC) die.

Could you maybe have another look at this, please?

The node is not pruned.

## moneromooo-monero | 2020-01-09T11:25:52+00:00
What is "our clients" ?

## normoes | 2020-01-09T12:22:37+00:00
By "our clients" I just mean tools and applications that access the Monero RPC.

## moneromooo-monero | 2020-01-09T17:09:16+00:00
You're not asking me to fix them, right ? :)

## moneromooo-monero | 2020-01-09T17:11:15+00:00
Oh, the "Cannot calculate the hash of a pruned transaction" ones are likely fixed in #6268.

## normoes | 2020-01-09T19:43:49+00:00
> You're not asking me to fix them, right ? :)

No, I'm not:) That's something I have to figure out.

But thanks :)

I will test the patch/fix and report back here.


## gituser | 2020-04-27T20:37:21+00:00
* I have this issue as well on the latest monero release `v0.15.0.5-17ec003c0`:

Monerod suddenly stops receiving incoming connections and there are some entires in the log like:
```
2020-04-26 08:44:08.537	[P2P2]	INFO	global	src/p2p/net_node.inl:1808	Incoming connections disabled, enable them for full connectivity
2020-04-26 08:59:52.686	[P2P0]	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:239	Failed to parse transaction from blob
2020-04-26 09:00:01.606	[P2P7]	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:239	Failed to parse transaction from blob
2020-04-26 09:24:17.681	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-26 09:24:39.330	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2163	SYNCHRONIZED OK
2020-04-26 09:44:12.668	[P2P2]	INFO	global	src/p2p/net_node.inl:1808	Incoming connections disabled, enable them for full connectivity
2020-04-26 10:44:31.540	[P2P4]	INFO	global	src/p2p/net_node.inl:1808	Incoming connections disabled, enable them for full connectivity
2020-04-26 11:24:18.587	[P2P8]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-26 11:44:31.759	[P2P1]	INFO	global	src/p2p/net_node.inl:1808	Incoming connections disabled, enable them for full connectivity
2020-04-26 12:44:32.550	[P2P1]	INFO	global	src/p2p/net_node.inl:1808	Incoming connections disabled, enable them for full connectivity
2020-04-26 13:24:19.024	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-26 13:44:33.269	[P2P0]	INFO	global	src/p2p/net_node.inl:1808	Incoming connections disabled, enable them for full connectivity
2020-04-26 14:44:33.939	[P2P4]	INFO	global	src/p2p/net_node.inl:1808	Incoming connections disabled, enable them for full connectivity
2020-04-26 15:24:19.896	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-26 15:42:10.368	[P2P7]	WARNING	ringct	src/ringct/rctOps.cpp:442	ge_frombytes_vartime failed at 442
2020-04-26 15:44:34.773	[P2P3]	INFO	global	src/p2p/net_node.inl:1808	Incoming connections disabled, enable them for full connectivity
2020-04-26 16:23:53.667	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2085280
2020-04-26 16:23:53.667	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	id:	<4cb86826755a05d96529e5815a2ab5b5b64ca913889d84b3a976c5f090c59ed0>
2020-04-26 16:23:53.667	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	PoW:	<180d4c30243bdb14a57b0b6eded47c84b90d04bc8924c9b11272df0600000000>
2020-04-26 16:23:53.667	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	difficulty:	147135777144
2020-04-26 16:23:57.583	[P2P2]	INFO	global	src/cryptonote_core/blockchain.cpp:1828	###### REORGANIZE on height: 2085280 of 2085280 with cum_difficulty 49835415021875191
2020-04-26 16:23:57.583	[P2P2]	INFO	global	src/cryptonote_core/blockchain.cpp:1828	 alternative blockchain size: 2 with cum_difficulty 49835562105876934
2020-04-26 16:23:57.831	[P2P2]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2085280
2020-04-26 16:23:57.831	[P2P2]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	id:	<5e8c280c14741008cf0ea6401b5fce35cd4ec47065f6566a8abad610f27f4539>
2020-04-26 16:23:57.831	[P2P2]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	PoW:	<8efc78709e3cc53fe9db9728560db3911329395714efbd34fae8710200000000>
2020-04-26 16:23:57.831	[P2P2]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	difficulty:	147135777144
2020-04-26 16:23:58.069	[P2P2]	INFO	global	src/cryptonote_core/blockchain.cpp:1047	REORGANIZE SUCCESS! on height: 2085280, new blockchain size: 2085282
2020-04-26 16:43:32.708	[P2P0]	WARNING	ringct	src/ringct/rctOps.cpp:445	ge_frombytes_vartime failed at 445
2020-04-26 16:45:15.844	[P2P7]	INFO	global	src/p2p/net_node.inl:1808	Incoming connections disabled, enable them for full connectivity
2020-04-26 17:24:20.795	[P2P0]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-26 17:45:27.068	[P2P9]	INFO	global	src/p2p/net_node.inl:1808	Incoming connections disabled, enable them for full connectivity
2020-04-26 18:20:59.994	[P2P4]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2085343
2020-04-26 18:20:59.995	[P2P4]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	id:	<be17ec6f7b0f878ec7707e8fe439c7b0d18a11fd87a5380d8fd44d29b7a966f0>
2020-04-26 18:20:59.995	[P2P4]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	PoW:	<aa45763011cc1e2797f3f0df3161eb4cdf19895deadfb19edad1830200000000>
2020-04-26 18:20:59.995	[P2P4]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	difficulty:	146710814266
2020-04-26 19:24:21.020	[P2P0]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-26 21:24:21.298	[P2P1]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-26 23:24:22.293	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-27 01:24:22.651	[P2P0]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-27 03:24:23.583	[P2P9]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-27 05:24:24.466	[P2P1]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-27 07:24:25.452	[P2P1]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-27 09:24:26.414	[P2P9]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-27 11:24:26.890	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-27 12:48:02.445	[P2P4]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2085900
2020-04-27 12:48:02.445	[P2P4]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	id:	<aa01a1c2d231f80c17c0b0d72c4b9ad5dea9a06565a90534c39d37dba9e3913c>
2020-04-27 12:48:02.445	[P2P4]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	PoW:	<8e5c068a0a921fd83eb987540a5d1f28e945c1e7ba6a0c06b880dd0300000000>
2020-04-27 12:48:02.445	[P2P4]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	difficulty:	145281407309
2020-04-27 12:49:36.770	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1828	###### REORGANIZE on height: 2085900 of 2085900 with cum_difficulty 49925756901473448
2020-04-27 12:49:36.770	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1828	 alternative blockchain size: 2 with cum_difficulty 49925902396558006
2020-04-27 12:49:37.696	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2085900
2020-04-27 12:49:37.696	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	id:	<93c3a21eaef930bd341668daa722f19208cab88fbdb5cd115b4920b53083f22a>
2020-04-27 12:49:37.696	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	PoW:	<ec31760077c881a0187ad123b49c23a6a3efd69b4f8550ee7f3f430300000000>
2020-04-27 12:49:37.696	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1839	difficulty:	145281407309
2020-04-27 12:49:37.942	[P2P0]	INFO	global	src/cryptonote_core/blockchain.cpp:1047	REORGANIZE SUCCESS! on height: 2085900, new blockchain size: 2085902
2020-04-27 13:24:26.931	[P2P4]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-27 15:24:27.755	[P2P6]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-27 17:24:28.453	[P2P9]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
2020-04-27 17:43:10.491	[P2P3]	WARNING	ringct	src/ringct/rctOps.cpp:442	ge_frombytes_vartime failed at 442
2020-04-27 19:24:28.921	[P2P9]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1676	Last scheduled hard fork time suggests a daemon update will be released within the next couple months.
```

Full log is here - https://pastebin.com/qgAK0AaC

Strangely enough incoming deposits are being processed without an issue, but outgoing withdrawals are all stuck with `withdrawal pending`.

And if I issue `./monerod status` I can see that the daemon is fully synced with the blockchain and latest block matches the one at https://xmrchain.net

* The only way to "cure" this is to restart stuck monerod daemon by killing it and starting again and then also use:

`./monerod relay_tx <txhash>` for each stuck transaction, list of transactions can be obtained by grepping monero-wallet-rpc logs.

* My monerod runs behind NAT and there is no port available outside (for security reasons).

Here is how I run it:
`/home/monero/monerod --out-peers 200 --data-dir /home/monero/.monero --log-file /home/monero/.monero/monero.log --log-level 0 --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18081 --no-igd --hide-my-port --detach`

monerod is not running pruned, it contains full blockchain.

I'm pretty sure this is a bug and it's been here in monero since at least v0.14.0.

Could it be because of `--hide-my-port` or `--no-igd` options?

Ping @moneromooo-monero 

## moneromooo-monero | 2020-04-28T17:58:16+00:00
When this happens, run "sync_info" to see your current peer list. I doubt the two options you mention have anything to do with it.

# Action History
- Created by: nikitasius | 2019-12-12T19:04:51+00:00
