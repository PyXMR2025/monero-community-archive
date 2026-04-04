---
title: Problem in call COMMAND_RPC_GET_HASHES_FAST as used by wallet2 for refresh
source_url: https://github.com/monero-project/monero/issues/2558
author: rbrunner7
assignees: []
labels: []
created_at: '2017-10-01T12:41:48+00:00'
updated_at: '2017-10-02T19:42:25+00:00'
type: issue
status: closed
closed_at: '2017-10-02T19:42:25+00:00'
---

# Original Description
With the code at 5f7cdde, on my Linux OS, the CLI wallet is not able to refresh anymore.

It uses the RPC `COMMAND_RPC_GET_HASHES_FAST` for the refresh. The daemon rejects the call, returning *false*. I traced the ultimate rejection to the following lines in *blockchain.cpp*: `qblock_ids` is empty:

```
bool Blockchain::find_blockchain_supplement(const std::list<crypto::hash>& qblock_ids, uint64_t& starter_offset) const
{
  LOG_PRINT_L3("Blockchain::" << __func__);
  CRITICAL_REGION_LOCAL(m_blockchain_lock);

  // make sure the request includes at least the genesis block, otherwise
  // how can we expect to sync from the client that the block list came from?
  if(!qblock_ids.size() /*|| !req.m_total_height*/)
  {
    MCERROR("net.p2p", "Client sent wrong NOTIFY_REQUEST_CHAIN: m_block_ids.size()=" << qblock_ids.size() << /*", m_height=" << req.m_total_height <<*/ ", dropping connection");
    return false;
  }
```
The wallet prepares that empty list as `short_chain_history` in method `wallet2::refresh`. The following method returns very early because `sz` evaluates as 0:

```
void wallet2::get_short_chain_history(std::list<crypto::hash>& ids) const
{
  size_t i = 0;
  size_t current_multiplier = 1;
  size_t sz = m_blockchain.size() - m_blockchain.offset();
  if(!sz)
    return;
```
... and here was end of the line for me, no idea how to get nearer to the real problem.

But a shot into the dark: Is this new optimized refresh method in any way connected with the Moneropulse "checkpoints" that are queried over DNSSEC? And if those queries do not work because a resolver does not properly support DNSSEC the whole thing fails (or does not properly proceed to a second attempt with a more primitive method)?

Because DNSSEC somehow does not work on my system...

# Discussion History
## moneromooo-monero | 2017-10-01T14:11:50+00:00
It's unrelated to DNSSEC, it's overeager trimming, which will be fixed in the next few hours.

## moneromooo-monero | 2017-10-02T14:26:14+00:00
See https://github.com/monero-project/monero/pull/2561

## rbrunner7 | 2017-10-02T18:52:47+00:00
Thanks, it refreshes again.

But now I have the new problem that the wallet looses the connection to the daemon, e.g. can refresh without problem after opening a wallet but as reaction to a manual refresh after that already changes the prompt to *wallet xyz (no daemon)*.

No idea yet about the reason. I will try to investigate and maybe open a new issue.

## rbrunner7 | 2017-10-02T18:57:40+00:00
The last lines of my CLI wallet log, produced when this error happened:

````
2017-10-02 18:46:41.729	    7f1b23f74780	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Starting refresh...
2017-10-02 18:46:42.213	    7f1b23f74780	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1558	Error calling gettransactions daemon RPC: r 0, status 
2017-10-02 18:46:42.213	    7f1b23f74780	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Refresh done, blocks received: 0
2017-10-02 18:46:42.213	    7f1b23f74780	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Balance: 0.000000000000, unlocked balance: 0.000000000000
2017-10-02 18:46:42.213	    7f1b23f74780	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Background refresh thread started
2017-10-02 18:46:42.213	    7f1b17d16700	ERROR	net.http	contrib/epee/include/net/http_client.h:393	HTTP_CLIENT: Failed to SEND
2017-10-02 18:48:12.755	    7f1b17d16700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1558	Error calling gettransactions daemon RPC: r 0, status 
2017-10-02 18:49:42.759	    7f1b17d16700	ERROR	net.http	contrib/epee/include/net/http_client.h:393	HTTP_CLIENT: Failed to SEND
2017-10-02 18:51:13.207	    7f1b17d16700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1558	Error calling gettransactions daemon RPC: r 0, status 
2017-10-02 18:52:43.208	    7f1b17d16700	ERROR	net.http	contrib/epee/include/net/http_client.h:393	HTTP_CLIENT: Failed to SEND
````

Maybe also a subtle incompatibility now between daemon and wallet because I just cherry-picked your single commit in the indicated PR, but nothing else?

## moneromooo-monero | 2017-10-02T19:17:32+00:00
Try https://github.com/monero-project/monero/pull/2548 on top

## moneromooo-monero | 2017-10-02T19:34:35+00:00
And if that doesn't fix it, please open a new bug for it.

+resolved

# Action History
- Created by: rbrunner7 | 2017-10-01T12:41:48+00:00
- Closed at: 2017-10-02T19:42:25+00:00
