---
title: ' Transaction broadcast failed when  the input number is larger than 10'
source_url: https://github.com/monero-project/monero/issues/3651
author: bitcodernull
assignees: []
labels: []
created_at: '2018-04-16T23:28:39+00:00'
updated_at: '2018-04-19T07:52:33+00:00'
type: issue
status: closed
closed_at: '2018-04-18T03:58:29+00:00'
---

# Original Description
I generate transactions  (not use wallet software) and broadcast it to network 
I found it will be failed where the input number is larger than 10

the fail info  is :
{ double_spend: false,
  fee_too_low: false,
  invalid_input: true,
  invalid_output: false,
  low_mixin: false,
  not_rct: false,
  not_relayed: false,
  overspend: false,
  reason: 'invalid input',
  status: 'Failed',
  too_big: false,
  untrusted: false,
  error: null }

# Discussion History
## moneromooo-monero | 2018-04-16T23:32:20+00:00
set_log 1 in monerod to see what the reason is.

## bitcodernull | 2018-04-17T04:52:37+00:00
I have set log 1, and i have got the following errors:

2018-04-17 04:51:42.715	    7f0fcff6e700	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:154	Failed to parse transaction from blob
2018-04-17 04:51:42.715	    7f0fcff6e700	INFO 	cn	src/cryptonote_core/cryptonote_core.cpp:613	WRONG TRANSACTION BLOB, Failed to parse, rejected
2018-04-17 04:51:42.715	[RPC0]	WARN 	daemon.rpc	src/rpc/core_rpc_server.cpp:797	[on_send_raw_tx]: tx verification failed

## moneromooo-monero | 2018-04-17T09:02:47+00:00
 What exact versions of monerod and monero-wallet-* are you running ?

## bitcodernull | 2018-04-17T10:32:07+00:00
Monerod 'Lithium Luna' (v0.12.0.0-master-release)

I have not use monero-wallet, I create transaction offline and send it to monerd

it is strange , when the number of input is smaller than 10, everything is ok, the number of inputs is larger than 10, the broadcast return error

i hava not found the reason , maybe my program have a bug where the size of inputs is larger than 10

## stoffu | 2018-04-17T10:52:48+00:00
The error says that the tx blob couldn’t be parsed. Isn’t there perhaps any obstacle on your console etc that prevents you from sending data whose size is above certain limit or something?

You could test if this hypothesis is true by trying with bigger ring sizes and fewer inputs.

## bitcodernull | 2018-04-17T11:04:28+00:00
thanks
i will test it

Do the monerod have limit  about it? 

## moneromooo-monero | 2018-04-17T17:04:39+00:00
No arbitrary limit.

## bitcodernull | 2018-04-19T07:52:33+00:00
I found the reason
input sorts has bugs.

https://github.com/mymonero/mymonero-core-js/issues/9

# Action History
- Created by: bitcodernull | 2018-04-16T23:28:39+00:00
- Closed at: 2018-04-18T03:58:29+00:00
