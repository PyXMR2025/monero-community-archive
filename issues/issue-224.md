---
title: 'Daemon-rpc doc: Add correct output description for /sendrawtransaction'
source_url: https://github.com/monero-project/monero-site/issues/224
author: cryptoshrimpi
assignees: []
labels: []
created_at: '2017-02-17T20:57:32+00:00'
updated_at: '2017-12-07T07:53:27+00:00'
type: issue
status: closed
closed_at: '2017-12-07T07:53:27+00:00'
---

# Original Description
URL: https://getmonero.org/knowledge-base/developer-guides/daemon-rpc#sendrawtransaction

The output of ```/sendrawtransaction``` is described as:

> Outputs:
> - status - string; General RPC error code. "OK" means everything looks good.
> 

In Monero v0.10.1.0 the actual output for an invalid ```tx_as_hex``` input value such as ```'abc'``` is

```
{ double_spend: false,
  fee_too_low: false,
  invalid_input: false,
  invalid_output: false,
  low_mixin: false,
  not_rct: false,
  not_relayed: false,
  overspend: false,
  reason: '',
  status: 'Failed',
  too_big: false }
```
This leads to the following type pattern:

    double_spend: boolean;
    fee_too_low: boolean;
    invalid_input: boolean;
    invalid_output: boolean;
    low_mixin: boolean;
    not_rct: boolean;
    not_relayed: boolean;
    overspend: boolean;
    reason: string;
    status: string;
    too_big: boolean;


# Discussion History
## QuickBASIC | 2017-08-31T13:29:08+00:00
@cryptoshrimpi Do you feel comfortable editing the [daemon-rpc.md](https://github.com/monero-project/monero-site/blob/master/resources/developer-guides/daemon-rpc.md) and adding the correct information? (Make sure you add `closes #224` in the commit description.) 

Or could someone more familiar with daemon rpc update the doc so we can close this issue, please? (I'd do it but I don't know enough about it to know what I'm adding.)

## QuickBASIC | 2017-10-23T11:14:25+00:00
+guide

## cryptoshrimpi | 2017-11-04T12:20:43+00:00
I'll try to add the correct information to the doc when I find time the next days. 

Can someone confirm that all of the mentioned attributes are not optional in the result set? I was only able to submit an invalid tx so I couldn't see the response for a valid tx. 

## cryptoshrimpi | 2017-11-04T12:35:58+00:00
I  noticed that the method can return the status "OK" even if the transaction was not relayed. One would expect that it returns "OK" only if everything went fine. Especially when the methods name is "**send**rawtransaction" and the transaction is not relayed automatically on a later time.

# Action History
- Created by: cryptoshrimpi | 2017-02-17T20:57:32+00:00
- Closed at: 2017-12-07T07:53:27+00:00
