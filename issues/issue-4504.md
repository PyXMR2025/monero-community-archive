---
title: '[Feature Request] Wallet-RPC Call to Decode/Describe Unsigned Transaction'
source_url: https://github.com/monero-project/monero/issues/4504
author: MatteBru
assignees: []
labels: []
created_at: '2018-10-05T20:40:12+00:00'
updated_at: '2018-10-26T20:41:02+00:00'
type: issue
status: closed
closed_at: '2018-10-26T20:41:02+00:00'
---

# Original Description
I have been working on an XMR cold-storage solution that relies on use of `monero-wallet-rpc` running on both the hot and cold side of the operation. Obviously at this point there is a rather well defined process for cold-signing, but I feel that the security of the process could be improved with a method that decodes the `unsigned_txset`, and displays the tx construction data in a human readable format.

Such a call would be very useful when hosting the view wallet on a VPS (or really, any potentially vulnerable internet-connected machine). Currently if a malicious actor were to gain access to the server they could either alter the wallet-rpc source, or whatever external code formats the parameters for the creation of the unsigned TX to use their own destination address. If this compromised unsigned tx is introduced into the signing environment, there is not a clean way of verifying that the destination address is that of the intended recipient.

I think the addition of a decoding call that could be used on the `unsigned_txset` before signing it would be very beneficial to the security of the cold-signing process.

# Discussion History
## MatteBru | 2018-10-05T20:40:28+00:00
@moneromooo-monero 

Addendum/edit:

My original approach was to somehow expose the JSON result of the [`wallet2::parse_tx_from_str` method](https://github.com/monero-project/monero/blob/4a652d6b52c60d169a0ccdc537afa5353c206b7c/src/wallet/wallet2.cpp#L5436-L5523) that gets called/logged during the `submit_transfer` process, and compare the values in the `vout[i].target.key` field to a stealth address generated with the known/verified recipient public address and `tx_key` (from the unsigned transaction) using the method @dEBRUYNE-1 outlined [here](https://monero.stackexchange.com/questions/1409/constructing-a-stealth-monero-address).

In theory that should've worked, but my stealth addresses were not matching up with those that came out of the signing process. After tearing my hair out for a little while, I figured out that the `tx_key` returned from the creation of the unsigned transaction is thrown away/replaced during the signing/reconstruction process. As a result the final stealth addresses differ from those created with that `tx_key`.

Perhaps it would be worthwhile to document that fact or potentially disable the `get_tx_key` option when `transfer` is called on a viewOnly wallet (seeing as it will not be relevant to the final transaction at all). Also it might be good to add the option to get the new/real `tx_key` along with the `signed_txset` in the `sign_transfer` method like you can when transferring from a full wallet.


Possibly relevant:
monero-project/monero#4316
el00ruobuob/monero-site/pull/21

## moneromooo-monero | 2018-10-09T10:51:53+00:00
https://github.com/monero-project/monero/pull/4539

## moneromooo-monero | 2018-10-09T10:59:47+00:00
The tx keys are stored in the cold wallet's cache if you need them. They're not included in the out data since that goes back to the hot wallet. Maybe they can be included separately in the RPC though.

## moneromooo-monero | 2018-10-19T10:31:57+00:00
https://github.com/monero-project/monero/pull/4552

## moneromooo-monero | 2018-10-26T20:33:25+00:00
+resolved

# Action History
- Created by: MatteBru | 2018-10-05T20:40:12+00:00
- Closed at: 2018-10-26T20:41:02+00:00
