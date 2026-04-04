---
title: Support specifying another asset for amount in URI
source_url: https://github.com/monero-project/monero/issues/8064
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2021-11-15T18:48:15+00:00'
updated_at: '2021-11-15T22:47:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Related:
* https://github.com/monero-project/monero/wiki/URI-Formatting
* https://github.com/monero-project/monero/issues/7731
* https://github.com/monero-project/monero/pull/7737
* https://github.com/monero-project/monero/issues/8063

Suppose someone wants to print a QR code that says "pay me the equivalent in 10 USD." Or 0.1 BTC. Or any other asset.

The URI scheme should have a method for passing through an asset.

Ideally, we could add another parameter such as `amount_asset`. If only 1 asset is given and there are several recipients, then it will apply that asset conversion to all specified amounts. Else, one could optionally provide 1 `amount_asset` per `tx_amount` for versatility.

While this is flexible, this has the downside of existing wallets potentially interpreting a message of "pay 10 USD equivalent" as "pay 10 XMR." Maybe we can kill 2 birds with 1 stone by changing `tx_amount` to `amount` (to be consistent with [BIP21](https://en.bitcoin.it/wiki/BIP_0021)) and to break previous implementations that rely on `tx_amount`.

If no `amount_asset` is specified, wallets should assume XMR. If a wallet doesn't support paying in other assets, it should cancel and display an error message.

Obviously it's on the wallet side to pick the conversion rate. If merchants want to specify exact XMR amounts for the conversion rate, they will need to use something more sophisticated than a printed QR code.

# Discussion History
## hyc | 2021-11-15T20:39:58+00:00
Sounds like an easily abusable feature, if the sender's wallet sets the conversion rate. Vendors should just set their price as a fixed amount in XMR and customers can deal with it or not.

## SamsungGalaxyPlayer | 2021-11-15T22:47:00+00:00
@hyc it definitely does not prevent a wallet from abusing the exchange rate; today people can of course scan a QR code for a specific amount of XMR and change it manually. In all cases, merchants actually need to confirm an expected amount of XMR is received.

# Action History
- Created by: SamsungGalaxyPlayer | 2021-11-15T18:48:15+00:00
