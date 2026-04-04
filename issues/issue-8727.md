---
title: Monero Wallet RPC sends all remaining balance of subaddress with transfer function.
source_url: https://github.com/monero-project/monero/issues/8727
author: rayorole
assignees: []
labels: []
created_at: '2023-02-01T19:49:32+00:00'
updated_at: '2023-02-02T12:23:56+00:00'
type: issue
status: closed
closed_at: '2023-02-02T12:22:34+00:00'
---

# Original Description
I have following PHP code that sends a request to the wallet rpc to transfer 0.003 XMR from a specific address index. (in this case index 2)

```php

/**
     *
     * Send monero
     * Parameters can be passed in individually (as listed below) or as an object/dictionary (as listed at bottom)
     * To send to multiple recipients, use the object/dictionary (bottom) format and pass an array of recipient addresses and amount arrays in the destinations field (as in "destinations = [['amount' => 1, 'address' => ...], ['amount' => 2, 'address' => ...]]")
     *
     * @param  string   $amount           Amount of monero to send
     * @param  string   $address          Address to receive funds
     * @param  string   $payment_id       Payment ID                                                (optional)
     * @param  number   $mixin            Mixin number (ringsize - 1)                               (optional)
     * @param  number   $account_index    Account to send from                                      (optional)
     * @param  string   $subaddr_indices  Comma-separated list of subaddress indices to spend from  (optional)
     * @param  number   $priority         Transaction priority                                      (optional)
     * @param  number   $unlock_time      UNIX time or block height to unlock output                (optional)
     * @param  boolean  $do_not_relay     Do not relay transaction                                  (optional)
     *
     *   OR
     *
     * @param  object  $params            Array containing any of the options listed above, where only amount and address or a destination's array are required
     *
     * @return object  Example: {
     *   "amount": "1000000000000",
     *   "fee": "1000020000",
     *   "tx_hash": "c60a64ddae46154a75af65544f73a7064911289a7760be8fb5390cb57c06f2db",
     *   "tx_key": "805abdb3882d9440b6c80490c2d6b95a79dbc6d1b05e514131a91768e8040b04"
     * }
     *
     */

transfer(0.003, '8BEbScBSZ18gAoJKA3XfvddvT1MUooRpm4ZQsDtko3jcXF7mfh5bSRKZNLyJFUG8ciCiGJmi4BDCz9ctskWnjTt8GxNrT4P', null, 15, 0, [2], 2, 0, false, 13);

```


When I call the function, the transfer is successful but all the remaining balance of the sub address is gone. (not only the 0.003 XMR but everything)

Is this a bug? How do I fix my code?

# Discussion History
## moneromooo-monero | 2023-02-02T12:22:34+00:00
You are sending a floating point value. Don't. The "human readable" amount is divided by 1e12. 0.003 monero is 3 millinero, which is 3000000000 units (I might be off by some zeroes). The smallest amount you can send is 1 (1e-12 in human readable amounts).

## moneromooo-monero | 2023-02-02T12:23:56+00:00
Also, the doc for amount says "string", it should be "number" (understood to be unsigned integer).

# Action History
- Created by: rayorole | 2023-02-01T19:49:32+00:00
- Closed at: 2023-02-02T12:22:34+00:00
