---
title: monero-wallet-rpc freezes during getting height and synchronization
source_url: https://github.com/monero-project/monero/issues/8561
author: gst2233
assignees: []
labels: []
created_at: '2022-09-11T01:23:39+00:00'
updated_at: '2022-09-11T23:30:56+00:00'
type: issue
status: closed
closed_at: '2022-09-11T23:30:56+00:00'
---

# Original Description
Hello, I'm trying to use monero-wallet-rpc for automation of creation and sync monero wallets and something went wrong:

1) I'm starting rpc server

`$ monero-wallet-rpc --proxy 127.0.0.1:9050 --daemon-address http://6dsdenp6vjkvqzy4wzsnzn6wixkdzihx3khiumyzieauxuxslmcaeiad.onion:18081 --rpc-bind-port 9999 --disable-rpc-login`

2) generating a new wallet, it works and opens wallet automatically. 

`$ curl -X POST http://127.0.0.1:9999/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"generate_from_keys", "params"={"restore_height":0,"filename":"wallet_name","address":"42gt8cXJSHAL4up8XoZh7fikVuswDU7itAoaCjSQyo6fFoeTQpAcAwrQ1cs8KvFynLFSBdabhmk7HEe3HS7UsAz4LYnVPYM","spendkey":"11d3fd247672c4cb29b6e38791dcf07629cd2d68d868f0b78811ce584a6b0d01","viewkey":"97cf64f2cd6c930242e9bed5f14f8f16a33047229aca3eababf4af7e8d113209","password":"pass","autosave_current":true}},' -H 'Content-Type: application/json'`

3) trying to get height

`$ curl http://127.0.0.1:9999/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_height"}' -H 'Content-Type: application/json'`

and sometimes it responds "1", sometimes rpc server is freezing. 
Finally, single way to kill rcp server and starting all from scratch.

Please help to resolve the issue.
I tested it on 2 devices (debian 11 in virtualbox and debian 10 on the remote VPS ) and had the same freezing.
Monero vestion is 'Fluorine Fermi' (v0.18.0.0-release).

Also I tried to wait 24 hours when it unfreezes but it didn't help.
Also tried to change daemons - the same issue (sometimes works, sometimes doesn't).
I need a stable working for my app, hope it's my mistake in settings and not a bug of rpc server.







# Discussion History
## gst2233 | 2022-09-11T22:26:10+00:00
I found the reason why it's unresponsive  https://github.com/monero-project/monero/issues/7431
But I still can't understand how to set stable connection to daemons .

## selsta | 2022-09-11T22:29:27+00:00
Did you try running your own daemon, or connect to a clearnet one?

## gst2233 | 2022-09-11T23:03:35+00:00
Thanks. I'm trying to use remote daemons from this list https://monero.fail/
Also I found that log-level 2 shows that daemons works, but synchronization is long.
Why is it such a long in compare with https://featherwallet.org/ (for example)?

## selsta | 2022-09-11T23:05:18+00:00
Restoring a wallet from height 0 will takes a while with a remote node.

## gst2233 | 2022-09-11T23:22:39+00:00
Got it. Is there some approach to increase speed of synchronization? Maybe multichannel connection to different daemons or something like this?

## selsta | 2022-09-11T23:23:27+00:00
Run a local node :)

## gst2233 | 2022-09-11T23:30:50+00:00
Thanks :)

# Action History
- Created by: gst2233 | 2022-09-11T01:23:39+00:00
- Closed at: 2022-09-11T23:30:56+00:00
