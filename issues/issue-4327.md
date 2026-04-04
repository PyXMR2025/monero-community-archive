---
title: sign_multisig error via JSON-RPC
source_url: https://github.com/monero-project/monero/issues/4327
author: sneurlax
assignees: []
labels: []
created_at: '2018-09-02T18:50:44+00:00'
updated_at: '2018-09-03T00:15:11+00:00'
type: issue
status: closed
closed_at: '2018-09-03T00:15:11+00:00'
---

# Original Description
When attempting to sign a multisig tx via JSON-RPC, the error

```bash
{ error:
   { code: -35,
     message:
      'Failed to sign multisig tx: This signature was made with stale data: export fresh multisig data, which other participants must then use' },
  id: '0',
  jsonrpc: '2.0' }
```

is given erroneously.  The same sequence used in `monero-wallet-cli` is successful.  I've using my library [monerojs](https://github.com/monerojs/monerojs) but have confirmed that using regular curl commands doesn't work, either, as shown in [this snippet](https://www.irccloud.com/pastebin/jeJoGND9/)

[monero-wallet-rpc log level 2](https://dpaste.de/t5Qn) (some erroneous `boost::filesystem::exists(m_wallet_file, ignored_ec). THROW EXCEPTION: error::file_exists`s because [my unit tests](https://github.com/sneurlax/monerojs/blob/feature/multisig-tests/test/index_test.js#L1651-L2000) attempt to `create_wallet` every time)

# Discussion History
## sneurlax | 2018-09-02T19:10:54+00:00
This error originates from [wallet_rpc_server.cpp#L3110](https://github.com/monero-project/monero/blob/2e7bfd0de545d3031deb6242a1d1b219066f9465/src/wallet/wallet_rpc_server.cpp#L3110) which calls [wallet2::sign_multisig_tx](https://github.com/monero-project/monero/blob/13a34faeb09814121140e14e0af442714fa985f9/src/wallet/wallet2.cpp#L5658-L5758).  The error looks to stem from [wallet2's line 5703](https://github.com/monero-project/monero/blob/13a34faeb09814121140e14e0af442714fa985f9/src/wallet/wallet2.cpp#L5703) call to [wallet2::get_multisig_k](https://github.com/monero-project/monero/blob/13a34faeb09814121140e14e0af442714fa985f9/src/wallet/wallet2.cpp#L10632-L10645), which actually throws the `multisig_export_needed` error (`Failed to sign multisig tx: This signature was made with stale data...`)

As for a patch, I'll have to attempt it when I get back.

## moneromooo-monero | 2018-09-02T21:40:43+00:00
Works for me (with two processes). You don't save your wallet after loading the multisig data, so when you reload it, you have stale data... Try again after saving the data where appropriate, and it should work.

## sneurlax | 2018-09-02T21:48:35+00:00
I'll try that when I get back to my desk, thanks (and sorry if this was
frivolous.)

On Sun, Sep 2, 2018, 16:40 moneromooo-monero <notifications@github.com>
wrote:

> Works for me (with two processes). You don't save your wallet after
> loading the multisig data, so when you reload it, you have stale data...
> Try again after saving the data where appropriate, and it should work.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/4327#issuecomment-417961717>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AD6u2RGxhXTj4qp2pSUQPL7s7nHNZANTks5uXFBjgaJpZM4WWuJ2>
> .
>


## sneurlax | 2018-09-03T00:15:11+00:00
I found that the wallet state should be stored after both export and import.  Apologies again for being a noob

# Action History
- Created by: sneurlax | 2018-09-02T18:50:44+00:00
- Closed at: 2018-09-03T00:15:11+00:00
