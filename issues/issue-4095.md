---
title: Parsing signed tx using wallet -RPC fails with "bad magic from signed transaction"
source_url: https://github.com/monero-project/monero/issues/4095
author: MatteBru
assignees: []
labels:
- invalid
created_at: '2018-07-03T18:36:15+00:00'
updated_at: '2018-07-12T22:32:59+00:00'
type: issue
status: closed
closed_at: '2018-07-12T22:32:59+00:00'
---

# Original Description
I have created two wallets on a remote machine running Monero on stagenet compiled from source (7/3/2018), one is a view only wallet, and is connected to monerod/synced, the other is a full wallet not connected to the daemon (to simulate an airgapped situation).

I am sending my RPC requests from a node.js app, and for each of the import/export steps I am logging the response and passing it to the next step. I have toyed around with adding additional parameters/renaming parameters in the response before passing them on to the next step, but generally I am just passing the full JSON response from each step as the params for the next request.

I have a wallet RPC class (based on https://github.com/PsychicCat/monero-nodejs) that handles the requests, and instantiate one for the view wallet and one for the full wallet:

```
let view = new RPC(hostname, 38067);
let full = new RPC(hostname, 38066)


view.open_wallet('hdview', '123').then(console.log)
full.open_wallet('hdfull', '123').then(console.log)
```

then the responses kind of just ping-pong back and forth:

```
view._request('export_outputs')
.then(res => {
    console.log(res);
    return full._request('import_outputs', res)
})
.then(res => {
    console.log(res);
    return full._request('export_key_images')
})
.then(res => {
    console.log(res);
    return view._request('import_key_images', res)
})
.then(res => {
    console.log(res);
    let options = {
        get_tx_hex: true,
        get_tx_metadata: true,
        export_raw: true
    };
    let destinations = {address: '59SoMJPAsX1QQXsRjj1Kx4H9QmRY6VXLp4vqswuvFMC1YwVAywNpgewAe2VUoQcemtAirvwAusESc6VuiBMbLmvM22H6fPC', amount: 200};
    return view.transfer(destinations, options)
})
.then(res => {
    console.log(res);
    return full._request('sign_transfer', res)
})
.then(res => {
    console.log(res);
    return view._request('submit_transfer', res)
})
.then(console.log)
```

The General format of the responses logged from this chain look like this:

export_outputs from view:
```
{ outputs_data_hex:
   '4d6f6e6572... really long hex ...f6dea100' }
```

import_outputs from full:
```
{ num_imported: 1 }
```

export_key_images from full:
```
{ signed_key_images:
   [ { key_image:
        '662e136607f52c537f30e280f017474137d6eb2254200cfe708f47696e198618',
       signature:   '12a7fdee1d3a73bfdecc8d4fe3af03bcd4bd6e0c8f37c34ccc3bb71b16d4c2099ec04cc9dfa9d8c586655bd6df3933eb88cf7b8f996a68956978d575d8ba100f' } ] }
```

import_key_images from view:
```
{ height: 106641, spent: 0, unspent: 616000000000000 }
```

transfer from view:
```
{ amount: 200000000000000,
  fee: 15273180000,
  multisig_txset: '',
  tx_blob: '',
  tx_hash:
   '880ddd5ed9f73e5fb34da1c0b6193ad4c2124f9069840e868c79069e2e56075b',
  tx_key: '',
  tx_metadata: '',
  unsigned_txset:
   '4d6f6e6... really long hex ...ec0156920b' }
```

sign_transfer from full:
```
{ signed_txset:
   '4d6f6e65... really long hex ...0325c4786f0e',
  tx_hash_list:
   [ 'f2d5bc4867de3751360b8c079f19523f0c43db10a7b7c374b8005948e8e195fe' ] }
```

submit_transfer from view:
```
{ error: { code: -40, message: 'Failed to parse signed tx data.' },
  id: '0',
  jsonrpc: '2.0' }

```

On the RPC server for the view wallet I get this error for the last step:
```
2018-07-03 17:39:44.168 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:5143     Bad magic from signed transaction
```

Again, I have tried playing around with including other params/renaming some things in the responses before passing them along, but I am kind of just taking shots in the dark, so I could be missing something quite fundamental.

# Discussion History
## moneromooo-monero | 2018-07-03T21:46:50+00:00
Worked for me (manually setting up all those RPCs).
Maybe the last call's parameters got corrupted ?


## stoffu | 2018-07-03T23:24:03+00:00
There was a bugfix regarding the magic for signed txes that was recently merged: #4028 
Please try the latest master.

## moneromooo-monero | 2018-07-04T08:19:18+00:00
That's on the unsigned tx file though, not the signed one.

## stoffu | 2018-07-04T09:22:15+00:00
I believe that one is needed for the cold signing to work. On the other hand, the double header issue should cause an error after checking the file magic, so I'm confused, too.

## stoffu | 2018-07-04T13:46:13+00:00
@MatteBru 
Can you apply this patch and see what the log says?
```diff
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index d99371673..ce824a83e 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -5140,7 +5140,7 @@ bool wallet2::parse_tx_from_str(const std::string &signed_tx_st, std::vector<too
   const size_t magiclen = strlen(SIGNED_TX_PREFIX) - 1;
   if (strncmp(s.c_str(), SIGNED_TX_PREFIX, magiclen))
   {
-    LOG_PRINT_L0("Bad magic from signed transaction");
+    LOG_PRINT_L0("Bad magic from signed transaction: " << s.substr(0, magiclen));
     return false;
   }
   s = s.substr(magiclen);
```


## MatteBru | 2018-07-05T14:46:18+00:00
Hi @stoffu and @moneromooo-monero,

Sorry for the delay in testing. I just changed the source and recompiled as you advised in your patch, and now see that there is nothing being logged where the magic should be:

```
2018-07-05 14:36:34.307 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:5143     Bad magic from signed transaction:
```

I am assuming this means that a parameter being passed in has been improperly named somewhere along the way? I can try tinkering around with logging stuff, to see if 's' itself is even being set and let you know. Thanks for your help!

UPDATE: 
after adding another logging line just under the location of your patch to log the entire string 's', it seems that it has never been set to anything. @moneromooo-monero, when you set your RPCs up manually, what was the structure of the JSON you passed into submit_transfer?

## moneromooo-monero | 2018-07-05T15:30:51+00:00
curl -k -X POST http://127.0.0.1:9001/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"submit_transfer","params":{"tx_data_hex":"4d6f6e65726f207369676e65642074782073657404371592370e36...b11c58aa02"}}' -H 'Content-Type: application/json'

## MatteBru | 2018-07-05T16:08:03+00:00
After restructuring the parameters being passed in to submit_transfer, I was just able to send a cold-signed tx through RPC!

The response from sign_transfer looked like this:
```
{ signed_txset:
   '4d6f6e65... really long hex ...0325c4786f0e',
  tx_hash_list:
   [ 'f2d5bc4867de3751360b8c079f19523f0c43db10a7b7c374b8005948e8e195fe' ] }
```
which did not go over well with wallet RPC when passed into submit_transfer. However after renaming signed_txset, and removing tx_hash_list like so:
```
{ "tx_data_hex": '4d6f6e65... really long hex ...0325c4786f0e'}
```
it goes through. Thank you both!

## moneromooo-monero | 2018-07-12T22:10:52+00:00
+invalid

# Action History
- Created by: MatteBru | 2018-07-03T18:36:15+00:00
- Closed at: 2018-07-12T22:32:59+00:00
