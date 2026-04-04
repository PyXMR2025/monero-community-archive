---
title: Monero Wallet RPC stops responding to Monero Python module after some time
source_url: https://github.com/monero-project/monero/issues/5612
author: hacheigriega
assignees: []
labels: []
created_at: '2019-06-08T02:18:09+00:00'
updated_at: '2019-06-21T17:42:06+00:00'
type: issue
status: closed
closed_at: '2019-06-21T17:42:06+00:00'
---

# Original Description
I wrote a program that repeatedly requests for JSON responses from Monero Wallet RPCs at time intervals ranging from 10 seconds to a minute. Everything is running on a testnet in my local network.

Strangely, the RPC often stops responding after a while, causing a time out error. I cannot even reconnect to the wallet once the error occurs.

I observed that the problem only occurs when I run multiple instances of the program at the same time. So perhaps there is some kind of collision happening. Each instance of the program is connected to a different wallet on a different port, though. Also, the problem persists when I run a single Python module connected to multiple wallets.

The following is the traceback output:
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py", line 387, in _make_request
    six.raise_from(e, None)
  File "<string>", line 2, in raise_from
  File "/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py", line 383, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.6/http/client.py", line 1331, in getresponse
    response.begin()
  File "/usr/lib/python3.6/http/client.py", line 297, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.6/http/client.py", line 258, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/usr/lib/python3.6/socket.py", line 586, in readinto
    return self._sock.recv_into(b)
socket.timeout: timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/requests/adapters.py", line 449, in send
    timeout=timeout
  File "/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py", line 641, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/usr/local/lib/python3.6/dist-packages/urllib3/util/retry.py", line 368, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/usr/local/lib/python3.6/dist-packages/urllib3/packages/six.py", line 686, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py", line 603, in urlopen
    chunked=chunked)
  File "/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py", line 389, in _make_request
    self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
  File "/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py", line 307, in _raise_timeout
    raise ReadTimeoutError(self, url, "Read timed out. (read timeout=%s)" % timeout_value)
urllib3.exceptions.ReadTimeoutError: HTTPConnectionPool(host='127.0.0.1', port=28023): Read timed out. (read timeout=30)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/econ_reader.py", line 31, in <module>
    tx = w.transfer(D[row['dest_addr']], Decimal(row['xmr_amount']))
  File "/usr/local/lib/python3.6/dist-packages/monero/wallet.py", line 259, in transfer
    relay=relay)
  File "/usr/local/lib/python3.6/dist-packages/monero/account.py", line 97, in transfer
    relay=relay)
  File "/usr/local/lib/python3.6/dist-packages/monero/backends/jsonrpc.py", line 307, in transfer
    _transfers = self.raw_request('transfer_split', data)
  File "/usr/local/lib/python3.6/dist-packages/monero/backends/jsonrpc.py", line 324, in raw_request
    self.url, headers=hdr, data=json.dumps(data), auth=auth, timeout=self.timeout)
  File "/usr/local/lib/python3.6/dist-packages/requests/api.py", line 116, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/lib/python3.6/dist-packages/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/requests/adapters.py", line 529, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPConnectionPool(host='127.0.0.1', port=28023): Read timed out. (read timeout=30)
```




# Discussion History
## moneromooo-monero | 2019-06-08T08:37:54+00:00
Please send a wallet stack trace when this occurs:

gdb /path/to/monero-wallet-rpc PID
thread apply all bt

Replace PID by the pid of the wallet that is unresponsive, and the path with the actual path.

## hacheigriega | 2019-06-08T22:53:03+00:00
The wallet-rpc continues to run in a separate tmux window. Does this suggest that it is probably an issue with the Monero Python module?

## moneromooo-monero | 2019-06-08T23:39:57+00:00
Maybe. We will know once we work out what's going on :)


## hacheigriega | 2019-06-10T01:13:24+00:00
I have found that the last two lines of the log file of the wallet RPC that becomes unresponsive don't appear in working ones. The last lines of the log file look as follows:

```
2019-06-10 00:52:09.960 T update_pool_state start
2019-06-10 00:52:09.960 T READ ENDS: Success. bytes_tr: 159
2019-06-10 00:52:09.960 T http_stream_filter::parse_cached_header(*)
2019-06-10 00:52:09.960 T READ ENDS: Success. bytes_tr: 98
2019-06-10 00:52:09.960 T update_pool_state got pool
2019-06-10 00:52:09.960 T update_pool_state done first loop
2019-06-10 00:52:09.960 T update_pool_state done second loop
2019-06-10 00:52:09.960 I Found new pool tx: <da02b0e4319bde737abc7eea3d921109c68f80e59a302b185b96e337470fdb1d>
2019-06-10 00:52:09.960 D asking for 1 transactions
```

## moneromooo-monero | 2019-06-10T08:52:51+00:00
That means it might be the daemon that wedges in a RPC. Send a stack trace for the daemon too.

## hacheigriega | 2019-06-10T17:12:41+00:00
Thanks for your help. I have been looking into the issue to understand it better. Do you think the following log of the daemon may be relevant to the problem? 
```
2019-06-10 17:02:47.629 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1014   Failed to calculate tx prunable hash
```

I am also not sure why I get the following error when I connected the three nodes to each other using the "--add-exclusive-node" option.
```
2019-06-10 17:45:18.084 [P2P6]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2256    Transaction not relayed - no peers available
```

## moneromooo-monero | 2019-06-10T18:03:52+00:00
Yes. It should not happen. Give all relevant information for the case where it happens. Same for the second thing.

## hacheigriega | 2019-06-10T19:28:54+00:00
I find it strange that "no peers are available." When I use "print_pl" in the daemon, no peers appear. I am not sure if this issue is relevant to the original problem, but how can I add the other two nodes in my test network? I tried -add-exclusive-node and --add-peer, but neither of them seems to work. 

## moneromooo-monero | 2019-06-10T19:43:18+00:00
I use --add-exclusive-node myself, it works fine. print_pl shows known peers. print_cn shows current connections.

## moneromooo-monero | 2019-06-10T19:44:25+00:00
One of my commands:
```
./build/$type/bin/monerod \
  --no-igd --regtest --fixed-difficulty 1 \
  --add-exclusive-node 127.0.0.1:28090 --add-exclusive-node 127.0.0.1:28070 \
  --p2p-bind-port 28080 --rpc-bind-port 28081 \
  --zmq-rpc-bind-port 28082 \
  --allow-local-ip --log-level 2 #1,net.p2p.msg:INFO
```

## hacheigriega | 2019-06-10T20:05:42+00:00
My command looks very similar to yours, except that I am not using --regtest. 

The following is where the programs starts to go wrong. The line "n_indices is only 0" is the first error log. Perhaps the transaction being sent to the daemon is defective?

```
block reward: 17.590021915642(17.590021915642 + 0.000000000000), coinbase_weight: 237, cumulative weight: 237, 35(0/35)ms
2019-06-10 19:58:40.096 I Received NOTIFY_NEW_FLUFFY_BLOCK <4d3247298c319e710716537886b6a86b7ac8e6dbc3c8a87f0801e2e39f24f646> (height 130, 0 txes)
2019-06-10 19:58:40.996 I HTTP [127.0.0.1] GET /json_rpc
2019-06-10 19:58:40.996 I [127.0.0.1:39806 INC] Calling RPC method get_info
2019-06-10 19:58:40.997 I HTTP [127.0.0.1] GET /json_rpc
2019-06-10 19:58:40.997 I [127.0.0.1:39806 INC] Calling RPC method hard_fork_info
2019-06-10 19:58:40.998 I HTTP [127.0.0.1] GET /json_rpc
2019-06-10 19:58:40.998 I [127.0.0.1:39806 INC] Calling RPC method hard_fork_info
2019-06-10 19:58:40.998 I HTTP [127.0.0.1] GET /json_rpc
2019-06-10 19:58:40.998 I [127.0.0.1:39806 INC] Calling RPC method hard_fork_info
2019-06-10 19:58:40.999 I HTTP [127.0.0.1] GET /json_rpc
2019-06-10 19:58:40.999 I [127.0.0.1:39806 INC] Calling RPC method hard_fork_info
2019-06-10 19:58:41.000 I HTTP [127.0.0.1] GET /json_rpc
2019-06-10 19:58:41.000 I [127.0.0.1:39806 INC] Calling RPC method hard_fork_info
2019-06-10 19:58:41.001 I HTTP [127.0.0.1] GET /json_rpc
2019-06-10 19:58:41.001 I [127.0.0.1:39806 INC] Calling RPC method hard_fork_info
2019-06-10 19:58:41.002 I HTTP [127.0.0.1] GET /json_rpc
2019-06-10 19:58:41.002 I [127.0.0.1:39806 INC] Calling RPC method hard_fork_info
2019-06-10 19:58:41.041 I HTTP [127.0.0.1] POST /sendrawtransaction
2019-06-10 19:58:41.041 I [127.0.0.1:46596 INC] calling /sendrawtransaction
2019-06-10 19:58:41.042 E n_indices is only 0
2019-06-10 19:58:41.042 I transaction with hash 0a724a73a04e73b21e2b09476c5559ff663a6d7882b3f174cdbb8d346f91568f not found in db
2019-06-10 19:58:41.044 I transaction with hash 0a724a73a04e73b21e2b09476c5559ff663a6d7882b3f174cdbb8d346f91568f not found in db
2019-06-10 19:58:41.045 I Transaction added to pool: txid <0a724a73a04e73b21e2b09476c5559ff663a6d7882b3f174cdbb8d346f91568f> weight: 827 fee/byte: 4.83676e+06
2019-06-10 19:58:41.051 I [127.0.0.1:40944 INC] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2019-06-10 19:58:41.051 I Including transaction <0a724a73a04e73b21e2b09476c5559ff663a6d7882b3f174cdbb8d346f91568f>
2019-06-10 19:58:42.116 I HTTP [127.0.0.1] GET /getblocks.bin
2019-06-10 19:58:42.116 I [127.0.0.1:39806 INC] calling /getblocks.bin
2019-06-10 19:58:42.118 I HTTP [127.0.0.1] GET /getblocks.bin
2019-06-10 19:58:42.118 I [127.0.0.1:39806 INC] calling /getblocks.bin
2019-06-10 19:58:42.141 I HTTP [127.0.0.1] GET /getblocks.bin
2019-06-10 19:58:42.141 I [127.0.0.1:39806 INC] calling /getblocks.bin
2019-06-10 19:58:42.143 I HTTP [127.0.0.1] GET /get_transaction_pool_hashes.bin
2019-06-10 19:58:42.143 I [127.0.0.1:39806 INC] calling /get_transaction_pool_hashes.bin
2019-06-10 19:58:42.144 I HTTP [127.0.0.1] GET /gettransactions
2019-06-10 19:58:42.144 I [127.0.0.1:39806 INC] calling /gettransactions
2019-06-10 19:58:42.144 E Failed to calculate tx prunable hash
2019-06-10 19:58:42.149 E Exception at [connection<t_protocol_handler>::handle_read], what=Failed to calculate tx prunable hash
```


## moneromooo-monero | 2019-06-10T20:12:20+00:00
Can you please post the results of:

mdb_dump -s tpxool_blob ~/.bitmonero/lmdb

To paste.debian.net or similar site ?

## hacheigriega | 2019-06-11T03:53:01+00:00
I put the result here because it was short. Please let me know if you prefer paste.debian.net. All three nodes' blockchains had the following result:
```
root@24da3b95bf71:/monero/external/db_drivers/liblmdb# ./mdb_dump -s txpool_blob /root/testnet/node_1/testnet/lmdb/
VERSION=3
format=bytevalue
database=txpool_blob
type=btree
mapsize=1073741824
maxreaders=126
db_pagesize=4096
HEADER=END
DATA=END
```

## moneromooo-monero | 2019-06-11T09:12:18+00:00
This is puzzling.
What are the versions of monero you are using for each monerod and wallets, and what is the command you're using to create that tx ? Also describe anything else you're doing to get this.

## hacheigriega | 2019-06-11T13:26:49+00:00
Everything is running on 'Boron Butterfly' (v0.14.1.0-51766d02). 

I am using tmux to create windows for three daemons and three corresponding wallets. Using python module, I load wallets and daemons and create transactions as follows:

```
w1 = Wallet(JSONRPCWallet(port=28013))
daemon1 = Daemon(JSONRPCDaemon(port=28011))
tx = w1.transfer(dest_addr, amount, relay=False)
result = daemon1.send_transaction(tx[0])
```

It seems that around 5-10 transactions go through successfully. But eventually the program comes to a halt with the traceback output in the original question. I have noticed that I sometimes get the following traceback output:
```
Traceback (most recent call last):
  File "/tmp/econ_runner.py", line 70, in <module>
    result = daemon1.send_transaction(txs[0])
  File "/usr/local/lib/python3.6/dist-packages/monero/daemon.py", line 35, in send_transaction
    return self._backend.send_transaction(tx.blob, relay=relay)
  File "/usr/local/lib/python3.6/dist-packages/monero/backends/jsonrpc.py", line 50, in send_transaction
    details=res)
monero.exceptions.TransactionBroadcastError: Failed:
```

## moneromooo-monero | 2019-06-11T14:24:19+00:00
What are the command lines you use for each ?

## hacheigriega | 2019-06-11T14:42:54+00:00
Starting a daemon:
```
monerod --testnet --p2p-bind-port 28010 --rpc-bind-port 28011 --zmq-rpc-bind-port 28012 --no-igd --hide-my-port --log-level 1 --data-dir /root/testnet/node_1 --add-exclusive-node 127.0.0.1:28020 --add-exclusive-node 127.0.0.1:28030 --fixed-difficulty 100
```

Starting wallet RPC:
```
monero-wallet-rpc --testnet --wallet-file ./wallet_1.bin --password '' --daemon-port 28011 --trusted-daemon --log-file ./wallet_1.log --rpc-bind-port 28013 --disable-rpc-login --log-level 1
```

I'm using 18.04.2 LTS (Bionic Beaver)



## emesik | 2019-06-11T15:10:18+00:00
You may also use the following Python snippet to enable full debug logging and learn what exact data is being passed in the RPC requests:

```
import logging
logging.basicConfig(level=logging.DEBUG)
```

BTW, are you using *testnet* as in public testnet, or you're creating your own local blockchain from scratch?

## hacheigriega | 2019-06-11T15:19:10+00:00
I am creating my own local blockchain. Built based on what is described here: https://github.com/moneroexamples/private-testnet 

I have noticed that the following is another very common error message from some of the daemons:
```
COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
```

## moneromooo-monero | 2019-06-11T15:46:45+00:00
You can ignore the timeouts.

## hacheigriega | 2019-06-11T15:56:56+00:00
To clarify my issue, my program connects to wallets and their daemons using the Python Monero module inside a docker container as follows:
```
w1 = Wallet(JSONRPCWallet(port=28013))
w2 = Wallet(JSONRPCWallet(port=28023))
w3 = Wallet(JSONRPCWallet(port=28033))

dm1 = Daemon(JSONRPCDaemon(port=28011))
dm2 = Daemon(JSONRPCDaemon(port=28021))
dm3 = Daemon(JSONRPCDaemon(port=28031))
```

In the beginning, my program makes some transactions between the wallets, but then abruptly an HTTP connection to one of the wallets fails to start. The wallet RPC window hangs on "asking for 1 transactions" indefinitely.

When I check the daemon log messages, the node that has failed usually outputs "Failed to calculate tx prunable hash," although I am not sure if this is always the case. The other nodes have a lot of the "(-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)" error in their daemon logs. 


## hacheigriega | 2019-06-11T21:22:24+00:00
@moneromooo-monero Sorry, I missed your last response. How can I just ignore the timeouts? I cannot reconnect to the wallets once the connections becomes faulty.

## moneromooo-monero | 2019-06-11T22:42:01+00:00
AFAICT, the exception kills the RPC thread, so the client never gets a reply. The timeouts are a consequence of that, not the actual problem. I'll debug that hopefully tomorrow.

## hacheigriega | 2019-06-12T00:12:11+00:00
@moneromooo-monero I see. But what problem is causing the exceptions? Also, is there a way to reopen the connection?

Thanks again for looking into this.

## moneromooo-monero | 2019-06-12T12:01:23+00:00
Fixed in https://github.com/monero-project/monero/pull/5634

The n_indices is only 0 should not be an error, it means "we don't have enough outs to check anything yet, so we don't check anything". I'll fix it to be a debug message,


## hacheigriega | 2019-06-13T14:11:26+00:00
Although the timeout error has disappeared, now I am getting a "block orphaned and rejected" error and the n_indices error appears again along with a "key image already spent" error later on.

```
2019-06-13 13:59:40.275 [P2P5]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1818 Block recognized as orphaned and rejected, id = <ddbd96d079d9f3f892b$
4e7ef15360315f6ccf505829f4480fe6054164942fd1>, height 61, parent in alt 0, parent in main 0 (parent <92a3866d797a9535cfd013adbe2988078bd354c9d0917cecd8eeb8f$
b3d87282>, current top <ad81caf719245cd10cab90dfd28179fb21c16d57af54278395520845c81f9476>, chain height 61)
```

## moneromooo-monero | 2019-06-13T14:17:45+00:00
If you're sure it should not be orphaned, file a bug.

## hacheigriega | 2019-06-13T14:24:48+00:00
Okay. I was wondering one thing: If I add nodes using "--add-exclusive-node," then the nodes should appear in "print_cn" list and transactions must be relayed to the peers, right?

## moneromooo-monero | 2019-06-13T14:51:52+00:00
Yes.

# Action History
- Created by: hacheigriega | 2019-06-08T02:18:09+00:00
- Closed at: 2019-06-21T17:42:06+00:00
