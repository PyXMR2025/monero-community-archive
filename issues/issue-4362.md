---
title: Wallet-RPC 'export_outputs' method is returning 'Method not found'
source_url: https://github.com/monero-project/monero/issues/4362
author: TorreJohnson
assignees: []
labels: []
created_at: '2018-09-10T20:08:36+00:00'
updated_at: '2018-09-11T14:57:33+00:00'
type: issue
status: closed
closed_at: '2018-09-11T14:57:33+00:00'
---

# Original Description
I'm currently using monero v0.12.3.0-c7bca47, although I've tried this rpc call with no success in a few different versions as well. When making an rpc call using the method `export_outputs`, I receive the following response:

    { error: { code: -32601, message: 'Method not found' },
        id: '0',
        jsonrpc: '2.0' }

I have been able to use this method in a previous version, so I'm wondering if it has maybe been renamed? Or is there another way to obtain the outputs data hex? Ultimately I am attempting to export all outputs from a view only wallet so that I can import them into an offline wallet. I've also noticed that the `import_outputs` method is returning the same error, so I'm looking for a solution to that as well. Thanks for the help.

# Discussion History
## moneromooo-monero | 2018-09-11T13:13:20+00:00
Those two are still here. Please post the JSON you're sending. Also double check you're actually asking the wallet and not some other server.

## TorreJohnson | 2018-09-11T13:59:07+00:00
I'm currently sending:

    { "jsonrpc": "2.0", "id": "0", "method": "export_outputs", "params": "" }

I'm able to make successful rpc calls using other methods (`getbalance`, `getheight`, `create_address`, `stop_wallet`, etc.). Using the curl command below also returns that the `export_outputs` method is not found, but does work for the additional methods mentioned.

`curl -u user:pass --digest -X POST http://127.0.0.1:3001/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"export_outputs"}' -H 'Content-Type: application/json'`

Let me know if you need anything else.

## moneromooo-monero | 2018-09-11T14:04:50+00:00
Did you mean json_rpc instead of jsn_rpc in the URI ?

## TorreJohnson | 2018-09-11T14:10:07+00:00
Sorry, that was a typo in my post, but yes, I am sending json_rpc in the URI.

## moneromooo-monero | 2018-09-11T14:43:44+00:00
Works for me.

## TorreJohnson | 2018-09-11T14:57:33+00:00
Ok, I just pulled down from the master branch and after commenting out some code as per #4340 I was able to get it to build and make the export_outputs rpc call, so it is now working.

I wasn't able to locate the call in the v0.12.3.0 release, so that may have been where my mistake was as it looks like it hadn't been added at that point. Thanks again for all of your help.

# Action History
- Created by: TorreJohnson | 2018-09-10T20:08:36+00:00
- Closed at: 2018-09-11T14:57:33+00:00
