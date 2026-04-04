---
title: Can't transfer or sweep_all via my own remote node "Failed to invoke http request
  to  /json_rpc"
source_url: https://github.com/monero-project/monero/issues/3806
author: mariodian
assignees: []
labels: []
created_at: '2018-05-15T15:41:29+00:00'
updated_at: '2018-06-05T11:25:00+00:00'
type: issue
status: closed
closed_at: '2018-06-05T11:24:59+00:00'
---

# Original Description
Hi, 

since the latest fork, I'm not able to `transfer` or `sweep_all` my funds. 

After I `sweep_all <address>` and type in the wallet password, monero-wallet-cli freezes, then outputs the following message after around 3 minutes and stays frozen: "_Error: no connection to daemon. Please make sure daemon is running._"

While the wallet is frozen, the node's IO is mostly at 99.99%.

I'm on the latest commit 4b728d7dd48584987f53995a141baac4f886f017, monero-wallet-cli runs on the latest Mac OS, and my remote node on the latest Ubuntu.

The node doesn't output anything useful even on log level 1, however, the wallet outputs the following:

```
2018-05-15 15:01:55.454	  0x7000022c0000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2036	asking for 1 transactions
2018-05-15 15:01:55.539	  0x7000022c0000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2042	Got 1 and OK
2018-05-15 15:01:55.540	  0x7000022c0000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2101	update_pool_state end
2018-05-15 15:01:58.998	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8086	Using v4 rules
2018-05-15 15:01:58.999	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7869	Spending from subaddress index 0
2018-05-15 15:01:59.054	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8086	Using v5 rules
2018-05-15 15:01:59.054	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8086	Using v4 rules
2018-05-15 15:01:59.104	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8088	Not using v8 rules
2018-05-15 15:01:59.104	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8086	Using v4 rules
2018-05-15 15:01:59.155	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8086	Using v5 rules
2018-05-15 15:01:59.155	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7931	Starting with X non-dust outputs and X dust outputs
2018-05-15 15:01:59.155	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7954	Picking output X, amount XX.XXXXXXXXXXXX
2018-05-15 15:01:59.155	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7966	Considering whether to create a tx now, X inputs, tx limit XXXXXX
2018-05-15 15:01:59.155	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for X with ring size X and X: XXXXX (XXX saved)
2018-05-15 15:01:59.155	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for X with ring size X and X: XXXX (XXX saved)
2018-05-15 15:01:59.156	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7980	Trying to create a tx now, with X destinations and X outputs
2018-05-15 15:01:59.156	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8086	Using v5 rules
2018-05-15 15:01:59.156	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6480	transfer_selected_rct: starting with fee XX.XXXXXXXXXXXX
2018-05-15 15:01:59.156	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6481	selected transfers: X
2018-05-15 15:01:59.156	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6489	transfer: adding XX.XXXXXXXXXXXX, for a total of XX.XXXXXXXXXXXX
2018-05-15 15:01:59.156	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6529	wanted XX.XXXXXXXXXXXX, found XX.XXXXXXXXXXXX, fee XX.XXXXXXXXXXXX
2018-05-15 15:01:59.156	  0x7fff90ba4380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:5863	fake_outputs_count: X
2018-05-15 15:02:00.017	  0x7fff90ba4380	DEBUG	net.dns	src/common/dns_utils.cpp:481	DNSSEC not available for checkpoint update at URL: segheights.moneropulse.co, skipping.
2018-05-15 15:02:00.017	  0x7fff90ba4380	DEBUG	net.dns	src/common/dns_utils.cpp:486	DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.co, skipping.
2018-05-15 15:02:00.017	  0x7fff90ba4380	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:10482	Found segregation height via DNS: asicflood fork height at 1564000
```

and

```
2018-05-15 15:05:30.022	  0x7fff90ba4380	DEBUG	net	contrib/epee/include/net/net_helper.h:398	Problems at read: Operation canceled
2018-05-15 15:05:30.023	  0x7fff90ba4380	ERROR	net.http	contrib/epee/include/net/http_client.h:456	Unexpected recv fail
2018-05-15 15:05:30.023	  0x7fff90ba4380	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /json_rpc
2018-05-15 15:05:30.023	  0x7fff90ba4380	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:5897	!r. THROW EXCEPTION: error::no_connection_to_daemon
2018-05-15 15:05:30.023	  0x7fff90ba4380	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/mariodian/source/Monero/monero/src/wallet/wallet2.cpp:5897:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = transfer_selected
2018-05-15 15:05:30.025	  0x7fff90ba4380	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: no connection to daemon. Please make sure daemon is running.
2018-05-15 15:05:30.226	  0x7000022c0000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1670	Daemon is recent enough, asking for pruned blocks
2018-05-15 15:06:36.738	  0x7000022c0000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1774	Block is already in blockchain: 95cac3b00973ad513cc723050ee345499aae566425cd695c07908dd1ee75ab65
2018-05-15 15:06:36.742	  0x70000223d000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1670	Daemon is recent enough, asking for pruned blocks
2018-05-15 15:06:36.746	  0x7000022c0000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1594	Processed block: <19c88928f435003d9889c44dfc964543ca9f7a941b78129c833fd5ba1a768624>, height 1573381, 5(1/4)ms
2018-05-15 15:06:36.747	  0x7000022c0000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1594	Processed block: <18b46d566d5de1373ee5838e51696291a3aa073f872675be1c60773c73b576c3>, height 1573382, 0(0/0)ms
```

GUI wallet also prints out a similar message:

```
2018-05-15 15:33:33.474	  0x70000c6c7000	ERROR	net.http	contrib/epee/include/net/http_client.h:456	Unexpected recv fail
2018-05-15 15:33:33.476	  0x70000c6c7000	ERROR	net.http	src/wallet/node_rpc_proxy.cpp:78	Failed to connect to daemon
2018-05-15 15:33:33.477	  0x70000c6c7000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1633	result->empty(). THROW EXCEPTION: tools::error::no_connection_to_daemon
2018-05-15 15:33:33.477	  0x70000c6c7000	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/buildbot/slave/monero-gui-osx-10_11/build/monero/src/wallet/wallet2.cpp:1633:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getversion
2018-05-15 15:33:48.623	  0x70000c74a000	ERROR	net.http	contrib/epee/include/net/http_client.h:456	Unexpected recv fail
2018-05-15 15:34:43.531	  0x70000c6c7000	ERROR	net.http	contrib/epee/include/net/http_client.h:456	Unexpected recv fail
2018-05-15 15:34:43.533	  0x70000c6c7000	ERROR	WalletAPI	src/wallet/api/wallet.cpp:893	daemonBlockChainTargetHeight: possibly lost connection to daemon
```

# Discussion History
## moneromooo-monero | 2018-05-15T16:26:59+00:00
Try with current release-0.12, (some) timeouts have been fixed.

## mariodian | 2018-05-15T18:38:41+00:00
I'm using the latest code already. 

## moneromooo-monero | 2018-05-15T18:45:43+00:00
Then, during those three minutes, gdb into monerod (gdb /path/to/monerod \`pidof monerod\`), then "thread apply all bt" in gdb.

## dEBRUYNE-1 | 2018-05-15T19:48:00+00:00
A bit pedantic, but 4b728d7 is a master commit and not a `release-v0.12` commit. 

## mariodian | 2018-05-16T11:23:25+00:00
@moneromooo-monero [gdb.txt](https://github.com/monero-project/monero/files/2008854/gdb.txt)

@dEBRUYNE-1 I just tried release-v0.12 and it's the same behavior.

## moneromooo-monero | 2018-05-16T18:21:20+00:00
OK, I see, fixing.
That call takes ~30 seconds here (to 1 minute if the db is not cached), so well within the 3 minute timeout, but if the server's busy it might hit it. And it's slow anyway.

## moneromooo-monero | 2018-05-16T22:27:54+00:00
Try with https://github.com/monero-project/monero/pull/3815



## mariodian | 2018-05-18T17:36:32+00:00
I tried. It's stuck but this time it didn't even timeout. 

Btw I'm trying to sweep funds from a different account within the wallet. Not sure if that makes a difference. 

## moneromooo-monero | 2018-05-18T17:58:13+00:00
Apply this, it will log the inputs to the RPC, so we know how much work it requests:

```
diff --git a/src/rpc/core_rpc_server.cpp b/src/rpc/core_rpc_server.cpp
index 7ce309c..9f97f23 100644
--- a/src/rpc/core_rpc_server.cpp
+++ b/src/rpc/core_rpc_server.cpp
@@ -2084,6 +2084,7 @@ namespace cryptonote
   {
     try
     {
+MGINFO("on_get_output_distribution: " <<req.amounts.size() << " amounts, from " << req.from_height << " to " << req.to_height);
       for (uint64_t amount: req.amounts)
       {
         std::vector<uint64_t> distribution;
```



## mariodian | 2018-05-18T19:15:39+00:00
I don't see such message in logs (set_log 1).

## mariodian | 2018-05-18T19:43:05+00:00
I shut down all my other nodes (bitcoind, lnd, electrumx) and now I see the first message after a minute or so since executing the `sweep_all` command:

`2018-05-18 19:32:06.142	[RPC1]	INFO 	global	src/rpc/core_rpc_server.cpp:2089	on_get_output_distribution: 1 amounts, from X to Y`

but it's been stuck since then (more than 10 minutes).

`sudo iotop` shows me monerod's IO (read) is almost 100% most of the time. I run on HDD. Could that be the issue? However, I had zero problems before the last fork. 

## moneromooo-monero | 2018-05-19T07:38:01+00:00
It should not print "from X to Y", they should be numbers.

## mariodian | 2018-05-19T10:32:03+00:00
The numbers were 1562704 and 1564001. 

## moneromooo-monero | 2018-05-19T12:17:48+00:00
Ah, I see the problem. Your numbers get pulled from the segheights TXT record, so don't hit my precalc. I'll add this one.

## moneromooo-monero | 2018-05-19T12:39:24+00:00
I updated the #3815 patch with a precalc for this case.

## mariodian | 2018-05-19T13:29:00+00:00
Thanks! It worked. I had to shut down all other nodes, though.

If I don't, monero-wallet-cli shows me the following:

```
2018-05-19 13:22:52.378	  0x7fff90ba4380	ERROR	net.http	contrib/epee/include/net/http_client.h:456	Unexpected recv fail
2018-05-19 13:22:52.395	  0x7fff90ba4380	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:5897	!r. THROW EXCEPTION: error::no_connection_to_daemon
2018-05-19 13:22:52.396	  0x7fff90ba4380	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/mariodian/Source/moneromooo/src/wallet/wallet2.cpp:5897:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = transfer_selected
2018-05-19 13:22:52.414	  0x7fff90ba4380	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: no connection to daemon. Please make sure daemon is running.
```

## moneromooo-monero | 2018-05-19T14:06:30+00:00
That's a timeout. Maybe it's timing out on another call now. If you have really bad I/O, maybe a lot will time out.

## mariodian | 2018-05-19T14:21:27+00:00
But how come I never had these issues before the fork yet I've been running all the other nodes with no problems? What has changed so drastically?

## moneromooo-monero | 2018-05-19T14:37:02+00:00
This call is new, and heavy.

## moneromooo-monero | 2018-06-05T11:01:26+00:00
+resolved

# Action History
- Created by: mariodian | 2018-05-15T15:41:29+00:00
- Closed at: 2018-06-05T11:24:59+00:00
