---
title: transaction build cannot add output
source_url: https://github.com/monero-project/monero/issues/9806
author: x64x2
assignees: []
labels:
- invalid
created_at: '2025-02-18T03:16:26+00:00'
updated_at: '2025-02-18T13:04:34+00:00'
type: issue
status: closed
closed_at: '2025-02-18T13:04:34+00:00'
---

# Original Description
Describe the issue
I am using monero compiled from sources on gentoo.
I want to use  monero to send funds from one in-wallet address to multiple users at once 
I receive error message which prevent me from transferring the funds:
transaction cannot add output

This is possibly a bug report, it looks to me I am unable to continue using this monero node at all while all funds are locked 

Can you reliably reproduce the issue?
Yes, it is still the same, regardless of the value I send.

Expected behaviour
I expect monero to send the funds to many people at once

Actual behaviour
Funds not sent

The version of monero you were using:
monero version v5

Machine specs:
Gentoo, AMD Ryzen 5 3600 6-Core Processor, 64 GB RAM, 500GB disk, kernel 6.1.0-26-amd64, gcc 12.2.0, ld 2.40, as 2.40

Any extra information that might be useful in the debugging process.
I tried -rescan, didn't work. I can send you my wallet.dat, there is just remaining 0.19 XMR in it.
I started using this node like a month ago.

debug log is here:

`2025-02-17T17:21:52.451097Z DEBUG http: Received a POST request for / from 127.0.0.1:60054
2025-02-17T17:21:52.451194Z DEBUG rpc: ThreadRPCServer method=monero
2025-02-17T17:21:52.455701Z DEBUG zrpc: opid-99c48829-108e-429f-a22b-e9967464610c: monero initialized
2025-02-17T17:21:52.462079Z DEBUG http: Received a POST request for / from 127.0.0.1:60058
2025-02-17T17:21:52.462112Z DEBUG rpc: ThreadRPCServer 
2025-02-17T17:21:52.463571Z DEBUG xmrrpcunsafe: opid-99c48829-108e-429f-a22b-e9967464610c: found unspent XMR  (txid=bb18613774, amount=0.19005, memo=f600000000)
2025-02-17T17:21:52.463580Z DEBUG xmrrpcunsafe:  opid-99c48829-108e-429f-a22b-e9967464610c: total transparent input: 0.00 (to choose from) opid-99c48829-108e-429f-a22b-e9967464610c: total transparent output: 0.00
2025-02-17T17:21:52.463589Z DEBUG xmrrpcunsafe: opid-99c48829-108e-429f-a22b-e9967464610c: total shielded output:0.00
2025-02-17T17:21:52.463591Z DEBUG zrpcunsafe: opid-99c48829-108e-429f-a22b-e9967464610c: total shielded output:0.18995
2025-02-17T17:21:52.463593Z DEBUG xmrrpcunsafe: opid-99c48829-108e-429f-a22b-e9967464610c: requested fee: default
2025-02-17T17:21:52.463595Z DEBUG xmrrpc: opid-99c48829-108e-429f-a22b-e9967464610c: fee: 0.0001
2025-02-17T17:21:52.463651Z  INFO main: opid-99c48829-108e-429f-a22b-e9967464610c: finished (status=failed, error=runtime error: `

# Discussion History
# Action History
- Created by: x64x2 | 2025-02-18T03:16:26+00:00
- Closed at: 2025-02-18T13:04:34+00:00
