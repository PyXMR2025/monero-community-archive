---
title: 'Wallet RPC (transfer): Transaction Key (tx_key) returns empty value'
source_url: https://github.com/monero-project/monero/issues/3623
author: cookiedumper
assignees: []
labels:
- invalid
created_at: '2018-04-12T19:00:40+00:00'
updated_at: '2019-04-16T23:09:31+00:00'
type: issue
status: closed
closed_at: '2019-04-16T23:09:31+00:00'
---

# Original Description
I run into an issue where when submitting an RPC request to the `transfer` method,
the `tx_key` (that helps prove a tx was made) is not being returned.

Sample request:

    array (
      'destinations' => 
      stdClass::__set_state(array(
         'amount' => '0.01314010',
         'address' => '44P8rkTRW5u1i...cEePYi4J5Vr3QLimydCX',
      )),
      'mixin' => 4,
      'get_tx_hex' => true,
      'get_tx_key' => true,
      'payment_id' => 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    )


What is being returned is:

    stdClass::__set_state(array(
       'amount' => 1140160000,
       'fee' => 10785600000,
       'multisig_txset' => '',
       'tx_blob' => '',
       'tx_hash' => 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
       'tx_key' => '',
       'tx_metadata' => '',
    ))

As you can see the `tx_key` property was returned empty. This isnt' the desired nor correct behavior.
Any ideas?

# Discussion History
## stoffu | 2018-04-13T04:26:46+00:00
I can't reproduce this behavior. Could be a bug.

## moneromooo-monero | 2018-04-13T10:32:15+00:00
<s>This data is (1) not saved unless store-tx-info is true in the settings, and (2) not restorable if you delete the cache, or restore from seed, rescan_bc, etc.</s>
Re-reading the report, this reply does not apply.

## moneromooo-monero | 2018-09-26T09:19:01+00:00
Re-reading this, I see:

> 'amount' => '0.01314010',

Maybe the software you're feeding this to convert, but monero expects a canonical number of atomic units, not a floating point value.

## moneromooo-monero | 2018-10-12T20:29:20+00:00
Is it till happening with current master or 0.13.x.y ?

## moneromooo-monero | 2018-12-18T12:48:33+00:00
ping

## moneromooo-monero | 2019-04-16T23:04:47+00:00
Works here. Reopen if it still happens with master, and without the extra layer you're using.

+invalid

# Action History
- Created by: cookiedumper | 2018-04-12T19:00:40+00:00
- Closed at: 2019-04-16T23:09:31+00:00
