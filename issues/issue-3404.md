---
title: Warn about tracing attack when untrusted remote node tx fails
source_url: https://github.com/monero-project/monero/issues/3404
author: monero-hax123
assignees: []
labels: []
created_at: '2018-03-14T15:15:35+00:00'
updated_at: '2018-11-07T15:09:25+00:00'
type: issue
status: closed
closed_at: '2018-11-07T15:09:25+00:00'
---

# Original Description
When using an untrusted / public remote node, if the remote node sends invalid data and the client retries the transaction, it could let the remote node trace the real transaction input. https://www.reddit.com/r/Monero/comments/84810s/psa_tracing_attacks_could_be_possible_when_using/

A mitigation for this would be to provide a stronger warning message to the client if the transaction creation fails. Something along the lines of `You are using an untrusted remote node (--untrusted) and transaction creation failed. This could potentially be because of a tracing attack. To ensure your privacy, DISCONNECT from the remote node and DO NOT try your transaction again right away.`

Other more comprehensive mitigations are possible but this seems like a simple and reasonable way.

Here are a list of lines of code that could throw exceptions *after* sending a list of outputs to `get_outs.bin`, but before the transaction is successfully constructed.
 
https://github.com/monero-project/monero/blob/a69c713f8e7717bc29c8a02d9d32a580f880562f/src/wallet/wallet2.cpp#L5609
https://github.com/monero-project/monero/blob/a69c713f8e7717bc29c8a02d9d32a580f880562f/src/wallet/wallet2.cpp#L5610
https://github.com/monero-project/monero/blob/a69c713f8e7717bc29c8a02d9d32a580f880562f/src/wallet/wallet2.cpp#L5611
https://github.com/monero-project/monero/blob/a69c713f8e7717bc29c8a02d9d32a580f880562f/src/wallet/wallet2.cpp#L5612

https://github.com/monero-project/monero/blob/a69c713f8e7717bc29c8a02d9d32a580f880562f/src/wallet/wallet2.cpp#L5641

https://github.com/monero-project/monero/blob/a69c713f8e7717bc29c8a02d9d32a580f880562f/src/wallet/wallet2.cpp#L5759

https://github.com/monero-project/monero/blob/a69c713f8e7717bc29c8a02d9d32a580f880562f/src/wallet/wallet2.cpp#L5803
https://github.com/monero-project/monero/blob/a69c713f8e7717bc29c8a02d9d32a580f880562f/src/wallet/wallet2.cpp#L5804
https://github.com/monero-project/monero/blob/a69c713f8e7717bc29c8a02d9d32a580f880562f/src/wallet/wallet2.cpp#L5813

Questions to discuss: 
- what should the exact error message be?
- are there other exceptions missing?


# Discussion History
## moneromooo-monero | 2018-03-15T09:49:30+00:00
Fair. I'll point out that if a node has multiple IPs, you can't tell whether a node you're connecting to is the same as a previous one so you can't reliably blackball nodes that try to not be.

> are there other exceptions missing?

Luckily, there's a handle_transfer_exception in simplewallet where we can add this to any relevant exception. I suppose the GUI ought to have the same kind of message too if you want to file a bug on 
https://github.com/monero-project/monero-gui/issues too.


## iamsmooth | 2018-03-15T10:52:04+00:00
@moneromooo-monero Agree you can't tell and even if it is a completely different node, you still can't tell that they might share data or both share with a third party (both get subpoenas for example).

Some better mitigations: 

1. Freeze (and store) the fake outs once a output is used for a real out (even if the transaction fails) and always use that same set of outs again if trying to spend that same output again.
2. Store the output keys in the wallet (or some random sample) and stop asking the server for them. The wallet receives them for scanning anyway, at least above the restore height. 

## moneromooo-monero | 2018-03-15T11:36:15+00:00
Could do. That is one good reason to have a deterministic fake out selection too.

## moneromooo-monero | 2018-03-15T12:04:57+00:00
https://github.com/monero-project/monero/pull/3410 for now. Anything more can be added after the fork, though I think those things above aren't all that a malicious daemon can do so it's a neverending thing.

## hyc | 2018-03-15T15:23:46+00:00
> Store the output keys in the wallet (or some random sample) and stop asking the server for them. The wallet receives them for scanning anyway, at least above the restore height.

Makes the most sense. There's no reason for the wallet to ask for the real gidx again after the first attempt.

## moneromooo-monero | 2018-03-17T14:09:44+00:00
Storing the keys for all outs requires ~1.5 GB (32 bit key and a mask for each out - pre-rct don't have masks, but you also need to keep track of unlockedness for all outs). So not before LMDB wallets :)

## iamsmooth | 2018-03-17T17:19:36+00:00
@moneromooo-monero You don't need to store them all. If you stash 1%, that should be plenty available for outgoing transactions, although maybe you want more of the more recent ones (and could then drop them as they got older). Clearly this increases complexity significantly.


## hyc | 2018-03-17T17:38:33+00:00
I wasn't even talking about permanent storage. The wallet makes an initial request for all keys. It can temporarily remember the real output's key in case it needs to retry the request, and it can then omit the real output from any retries. Once the transaction succeeds the info can be discarded.

## iamsmooth | 2018-03-17T20:27:58+00:00
@hyc I don't see how that works. The reason the real output is included in the request in the first place is so the server can't tell which was the real one when the transaction is broadcast (tx will contain N-1 fake outputs requested from the server, plus another one, which would be the real one). 


## moneromooo-monero | 2018-11-04T12:53:19+00:00
The selecting ring is now reused (https://github.com/monero-project/monero/pull/4743).

## moneromooo-monero | 2018-11-07T14:28:59+00:00
+resolved

# Action History
- Created by: monero-hax123 | 2018-03-14T15:15:35+00:00
- Closed at: 2018-11-07T15:09:25+00:00
