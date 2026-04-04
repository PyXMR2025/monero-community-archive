---
title: All monero-wallet-rpc methods error with "wrong number of additional derivations"
  on first use with new wallet
source_url: https://github.com/monero-project/monero/issues/4127
author: MatteBru
assignees: []
labels:
- invalid
created_at: '2018-07-10T20:56:02+00:00'
updated_at: '2018-09-16T21:24:21+00:00'
type: issue
status: closed
closed_at: '2018-08-17T23:00:53+00:00'
---

# Original Description
UPDATE: I have also tested this with get_balance, and this pattern of warnings/errors appears the same way.

*this all happens on stagenet on code compiled from master on July 5*

Upon creating a new view-only wallet, starting monero-wallet-rpc, and running export_outputs, I am getting an error ```wrong number of additional derivations``` both in the response to my rpc request, and in the logfile. It is also surrounded by many ```The same transaction pubkey is present more than once, ignoring extra instance``` messages. If I change nothing, and send the same request, it seems to work just fine. This happens both when the wallet has been funded after creation, and when it has no tx history.

Example section from log file:

```
2018-07-10 20:17:53.055     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:3965     Loaded wallet keys file, with public address: 52e3kyPej6a6dPTu2fGpB38NGykxdSzuy7RtWivLgnsw3n3LZPXGmDXGdLHAEvCrqNHoWGbMkTZvjZYGMvzkj1q$
2018-07-10 20:18:02.086     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:02.086     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:04.089     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:07.501     7f8f8efc4780        WARN    10mwallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:07.503     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:07.503     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:07.670     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:08.059     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:08.267     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:08.484     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:08.650     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:08.651     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:08.850     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:13.046     7f8f8efc4780        ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:666    wrong number of additional derivations
2018-07-10 20:18:13.048     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:13.048     7f8f8efc4780        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1199     The same transaction pubkey is present more than once, ignoring extra instance
2018-07-10 20:18:13.576     7f8f8efc4780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 0.0.0.0:38033
allet/wallet2.c8:13.576     7f8f8efc4780        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3250   Starting wallet RPC server
```

It is not really clear to me why either of the above messages are being displayed, or what they even mean?

Sorry if there is not enough info here, if more is required, I'll be happy to oblige.

I also am wondering if at least the "same transaction pubkey" message has to do with PR https://github.com/monero-project/monero/pull/4117?

# Discussion History
## phire | 2018-07-10T23:08:35+00:00
There is a malformed transaction on the stagenet blockchain.

As your wallet scans over it, it throws a few warnings/errors but nothing bad happens. It's safe to ignore them.

## MatteBru | 2018-07-11T11:50:50+00:00
And this error is caused by the same thing?

```
2018-07-10 20:18:13.046     7f8f8efc4780        ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:666    wrong number of additional derivations
```

Also, if I can pester for more detail:

- Why does this not happen during the initial blockchain scan that occurs when the wallet is created?

## moneromooo-monero | 2018-08-17T15:11:29+00:00
Yes, and did you try to actually scan the whole blockchain (ie, from seed, and don't give a refresh height/date) ?

## MatteBru | 2018-08-17T20:52:19+00:00
You'll have to forgive me as the situation is not so fresh in my mind anymore, but I am almost positive that I did not provide a height to begin scanning. If I remember correctly it defaults to height 0, so I would have been scanning the whole blockchain. I followed phire's advice, and did not seem to suffer any consequences so I kind of just let it go.

## moneromooo-monero | 2018-08-17T22:56:49+00:00
Yes, it's ignorable and not a bug, I'll close this then.

+invalid

## phire | 2018-08-18T07:24:12+00:00
If you want, I can narrow it down to a date.

I'm pretty sure It was my test transaction that's causing this error message.

## bityogi | 2018-09-16T21:24:21+00:00
I get this error even if I am running the `./monerod --stagenet` in `--offline` mode.

Note: That I did sync the monerod and only did I start getting this error. But even if I run the monerod in offline mode to generate a new wallet from json, I get this error. 

Like @phire mentioned, `nothing bad happens`, but it does take a few seconds more now to actually generate the wallet.


# Action History
- Created by: MatteBru | 2018-07-10T20:56:02+00:00
- Closed at: 2018-08-17T23:00:53+00:00
