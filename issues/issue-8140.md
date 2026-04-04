---
title: monero-wallet-rpc get_transfers(..., pending=True) does not work
source_url: https://github.com/monero-project/monero/issues/8140
author: elibroftw
assignees: []
labels: []
created_at: '2022-01-14T00:20:00+00:00'
updated_at: '2025-12-22T03:35:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
1. Startup an RPC in stagenet (bind to port 38088)
2. Open Stagenet wallet and send to address in RPC
3. This issue occurs regardless if the daemon is marked as trusted or not
4. Also the seed for the wallets is the same but the accounts are different. The Monero GUI can detect that the transaction is received pending but the RPC cant.
```py
from dotenv import load_dotenv
import os
from pathlib import Path
import requests
from requests.auth import HTTPDigestAuth

load_dotenv('.env')

import requests
# monero_rpc_session.auth = HTTPDigestAuth('monero', os.environ['SIMPLE_PWD'])
XMR_RPC_ENDPOINT = 'http://127.0.0.1:38088/json_rpc'
XMR_RPC_AUTH = HTTPDigestAuth('monero', os.environ['XMR_RPC_PW'])

def xmr_rpc_api(method_name, **params):
    rpc_defaults = {'jsonrpc': '2.0', 'id': '0'}
    if '_in' in params:
        params['in'] = params.pop('_in')
    return requests.post(XMR_RPC_ENDPOINT, json={**rpc_defaults, 'method': method_name, 'params': params}, auth=XMR_RPC_AUTH)


r = xmr_rpc_api('get_transfers', _in=True, out=False, pending=True,
                account_index=1, subaddr_indices=[]).json()
print(r['result'].keys())

```
Expected:
```py
dict_keys(['in', 'pending']
```
Got:
```py
dict_keys(['in']
```

# Discussion History
## selsta | 2022-02-18T23:02:51+00:00
> Also the seed for the wallets is the same but the accounts are different.

Can you explain this in more detail?

## elibroftw | 2022-02-18T23:08:05+00:00
I'm using the same wallet for RPC and GUI, but sending and receiving from two different accounts.

## elibroftw | 2022-02-21T00:51:03+00:00
https://github.com/comit-network/xmr-btc-swap/issues/523#issuecomment-846487263
I'm not the only one experiencing this bug

## rbrunner7 | 2022-04-01T13:20:01+00:00
I built a [web wallet](https://monerotech.info/Wallet) that is using the RPC interface and the `monero-wallet-rpc` binary, and it does not show the slightest problem of picking up pending transactions. (Pending transactions are displayed with a red "Pending" in the *Type* column.) Of course it uses the call you mention, `get_transfers`, because it's the only one and thus no way around it, as far as I remember.

So no idea what's the reason for your problems, but I highly doubt it can be a general problem in the RPC daemon or even in the wallet.

## elibroftw | 2022-04-01T14:01:14+00:00
@rbrunner7 did you see the comment I linked to Comit's swap tool? They also experience the same problem.

Is there a specific way to call get transfers then? 

## rbrunner7 | 2022-04-01T14:10:45+00:00
Yes, I checked the link. It may well possible that there are special circumstances that prevent pending transfers getting reported, and if yes, it's the big question how to sensibly narrow down here. Their comment is without any details thus unfortunately it's not helpful in this regard.

As I had a dedicated goal of always showing all transactions in all states in my web wallet, I think any error there would have jumped at me. So I can confirm that the call at least works pretty reliably under some circumstances; it's certainly not completely broken.

## rbrunner7 | 2022-04-01T14:12:31+00:00
> Is there a specific way to call get transfers then?

Not that I know of. You set, like you did, the `pending` boolean, and call `get_transfers`.


## elibroftw | 2022-04-01T14:12:40+00:00
Okay but am I calling get transfers incorrectly then? Or is it a bug if the incoming transfer for one account is the outgoing of another account? 

## rbrunner7 | 2022-04-01T14:15:40+00:00
Maybe only some such combinations are problematic, yeah. Maybe if you send to yourself, from one account to another, you only get a `pool` transfer reported, but not a `pending` one? I myself don't know, never tried that, and my web wallet does not support accounts.

## rbrunner7 | 2022-04-01T14:17:22+00:00
Quite in general, the RPC daemon pretty much uses the same calls into `wallet2` as the CLI wallet does. If there is a problem you should have a good chance to catch it with the CLI wallet as well, which would be much easier to reproduce for people and then investigate.

## elibroftw | 2022-05-10T21:28:22+00:00
The issue isn't just from me. I linked a comment which shows the commit people have also faced this issue. 

## elibroftw | 2022-05-10T21:35:16+00:00
The bug is not present in the wallet-cli

## elibroftw | 2022-06-06T03:07:21+00:00
@rbrunner7 , do I need to use `"pool": True`? https://monerodocs.org/interacting/monero-wallet-rpc-reference/#get_transfers

## elibroftw | 2022-06-06T03:08:30+00:00
If this works, then it's a bug if `pending: true` also requires `pool: true`. 

## rbrunner7 | 2022-06-17T08:33:23+00:00
I had a look at the code of `wallet_rpc_server::on_get_transfers`: It's simple enough, and all I saw is a clean separation between the `pending` and the `pool` boolean in the processing. No surprising dependence between those two in sight anywhere so that it would only work with both set.

The code also looks unchanged sine aeons, written and last modified by @moneromooo-monero 5 years ago.

I would say the riddle is still unsolved.

## elibroftw | 2022-06-17T13:17:00+00:00
I'll just run experiments again when I get the time. 

## plowsof | 2025-12-20T08:10:40+00:00
"_in" should be "in" in the OP but it defaults to `FALSE`

The xmr-comit comment mentions rpc not picking up a tx until 1 conf

`get_transfers` has `pool` which is 'false` by default https://docs.getmonero.org/rpc-library/wallet-rpc/#get_transfers this caught me out too 

Question: what does pending mean? Do not show tx's under 10 confs?

I think this issue can be closed. I experienced major headaches when my test et wallets restore height was higher than tip (i guess from an incorrect estimate) - when in this state , your wallet will see pool tx's, and then, when they are in a block - your wallet see's nothing - however you can still use `scan_txid` .. i think it should throw an error if our wallet heigh is ahead of nodes tip.

I will try to confirm what exactly this`pending` means 

## plowsof | 2025-12-22T03:33:31+00:00
https://github.com/monero-project/monero/blob/48ad374b0d6d6e045128729534dc2508e6999afe/src/wallet/wallet_rpc_server.cpp#L2954

```c++
    if (req.pending || req.failed) {
      std::list<std::pair<crypto::hash, tools::wallet2::unconfirmed_transfer_details>> upayments;
      m_wallet->get_unconfirmed_payments_out(upayments, account_index, subaddr_indices);
      for (std::list<std::pair<crypto::hash, tools::wallet2::unconfirmed_transfer_details>>::const_iterator i = upayments.begin(); i != upayments.end(); ++i) {
        const tools::wallet2::unconfirmed_transfer_details &pd = i->second;
        bool is_failed = pd.m_state == tools::wallet2::unconfirmed_transfer_details::failed;
        if (!((req.failed && is_failed) || (!is_failed && req.pending)))
          continue;
        std::list<wallet_rpc::transfer_entry> &entries = is_failed ? res.failed : res.pending;
        entries.push_back(wallet_rpc::transfer_entry());
        fill_transfer_entry(entries.back(), i->first, i->second);
      }
    }
```
pending seems to be for `out` transactions. (get_unconfirmed_payments_out)

# Action History
- Created by: elibroftw | 2022-01-14T00:20:00+00:00
