---
title: sign_transfer method not found!
source_url: https://github.com/monero-project/monero/issues/4367
author: lhfly5201314
assignees: []
labels:
- invalid
created_at: '2018-09-12T12:39:41+00:00'
updated_at: '2018-10-06T18:56:49+00:00'
type: issue
status: closed
closed_at: '2018-10-06T18:56:49+00:00'
---

# Original Description
Hi,everyone!
I tried to use the sign_transfer function to sign my raw-transaction in javascript code,but it returned the below error:
{ error: { code: -32601, message: 'Method not found' }

I tried the sign_transfer command in monero-wallet-cli,it works.

Why does it show 'method found' when I used in my javascript??
I reviewed the source code.The sign_transfer exist in the wallet_rpc_server.cpp file.
https://github.com/monero-project/monero/blob/master/src/wallet/wallet_rpc_server.cpp
And Why the monero-wallet-rpc docs don't list the sign_transfer func???Only describe the sign() func...
https://getmonero.org/resources/developer-guides/wallet-rpc.html#sign
It's really strange!

One more question,if I wanna use the curl + sign_transfer to test,what param keys should I use??The docs really suck!

Thanks,guys!



# Discussion History
## moneromooo-monero | 2018-09-12T13:09:18+00:00
Since there's no information apart from a single sentence, I assume you're sending a JSON request to the wallet RPC server. Post the JSON query you're sending. Also double check you're actually asking the wallet RPC server (yes, some people do happen to ask the wrong server). Also state which version of monero you're running (commit hash if possible, human readable version otherwise).


## lhfly5201314 | 2018-09-14T07:11:31+00:00
@moneromooo-monero Hi,friend!Thanks for your advice!Yes,I am trying to send a JSON request to the monero-wallet-rpc server.My monerod and  monero-wallet-rpc both are version  v0.12.3.0.
I tried to curl some other rpc functions to the wallet-rpc server,such as getheight,getbalance ,sign and transfer.They work well.
But when I tried the sign_transfer,I don't know how to write the params,
curl -X POST http://127.0.0.1:15000/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"sign_transfer","params":{""}' -H 'Content-Type: application/json'
When I send empty "params",it returned "Parse error".

monero-wallet-rpc server runs on the 15000 port.Have u ever tried to use the sign_transfer method with curl or in javascript code,not in the monero-wallet-cli???
I tried to use the sign_transfer in js code.It returns "Method not found",not "parse error"
I couldn't get any info about the sign_transfer on the Wallet RPC doc:
https://getmonero.org/resources/developer-guides/wallet-rpc.html
only sign() exists!

## moneromooo-monero | 2018-09-14T07:16:41+00:00
For sign_transfer, there should be one parameter called unsigned_txset, containing the hexadecimal representation of the transaction data to be signed (which you get from the transfer calls when your wallet does not have a spend key).

Note that I think "params":{""} is invalid. If params are empty for a given call, use "params":{} instead.

I have tried sign_transfer with RPC before, yes.


## lhfly5201314 | 2018-09-18T12:05:32+00:00
@moneromooo-monero Hi,friend!.Why isn't  there  any info about the sign_transfer func on the official moneor-wallet-rpc doc??I tried it in the javscript code again,still "Method not found",and the sign() works well!

## moneromooo-monero | 2018-09-18T13:13:18+00:00
Too new I guess. Are you using a recent master ?

## lhfly5201314 | 2018-09-19T02:01:47+00:00
No,friend! I downloaded the monero-linux-x64-v0.12.3.0.tar.bz2 and tared it directly...the link is:
https://github.com/monero-project/monero/releases
I could find the code about the sign_transfer method in the soucecode file(wallet_rpc_server.cpp),the link is:
https://github.com/monero-project/monero/blob/master/src/wallet/wallet_rpc_server.cpp
Now,the sign_transfer only works in the wallet-cli command mode,"Method not found" if it's tried in the javascript code with wallet-rpc.
Maybe,the v0.12.3.0 wallet-rpc doesn't support the sign_transfer RPC???But why under wallet-cli mode the sign_transfer works??
Doesn't the wallet-cli have a dependency with the wallet-rpc??
Should I compile the source code with the latest master branch??
Thanks,friend!

## xiphon | 2018-09-19T06:51:33+00:00
> curl -X POST http://127.0.0.1:15000/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"sign_transfer","params":{""}' -H 'Content-Type: application/json'
> When I send empty "params",it returned "Parse error".

You have to pass `unsigned_txset` param.

```
curl -X POST http://127.0.0.1:15000/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"sign_transfer","params":{"unsigned_txset":"UNSIGNED_TX_HEX"}' -H 'Content-Type: application/json'
```

## el00ruobuob | 2018-09-19T07:32:21+00:00
@lhfly5201314 the doc is being refreshed. A pull request is pending reviews. You can find the up-to-date instructions there https://github.com/monero-project/monero-site/pull/854

## lhfly5201314 | 2018-09-19T07:38:24+00:00
> > curl -X POST http://127.0.0.1:15000/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"sign_transfer","params":{""}' -H 'Content-Type: application/json'
> > When I send empty "params",it returned "Parse error".
> 
> You have to pass `unsigned_txset` param.
> 
> ```
> curl -X POST http://127.0.0.1:15000/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"sign_transfer","params":{"unsigned_txset":"UNSIGNED_TX_HEX"}' -H 'Content-Type: application/json'
> ```

Thanks,friend!

## lhfly5201314 | 2018-09-19T07:38:55+00:00
> @lhfly5201314 the doc is being refreshed. A pull request is pending reviews. You can find the up-to-date instructions there [monero-project/monero-site#854](https://github.com/monero-project/monero-site/pull/854)

Thanks!Really good job!

## moneromooo-monero | 2018-10-01T11:26:21+00:00
sign_transfer was not in 0.12.3.0 yet.

Try with a recent version, it should then find it.


## moneromooo-monero | 2018-10-06T18:20:49+00:00
Was looking in an old version.

+invalid

# Action History
- Created by: lhfly5201314 | 2018-09-12T12:39:41+00:00
- Closed at: 2018-10-06T18:56:49+00:00
