---
title: 'Hardware wallet: request to plug in the device only when sending transaction'
source_url: https://github.com/monero-project/monero-gui/issues/2952
author: rating89us
assignees: []
labels: []
created_at: '2020-06-13T20:57:21+00:00'
updated_at: '2020-06-19T11:16:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently it's not possible to open a wallet file from a hardware wallet without plugging in the device. 

It would be better if it were possible to open the wallet as a view-only wallet, allowing the user to check the balance and incoming transactions.

This way the user would only be requested to plug in the device when a transaction is being sent or when a transaction key is being requested in transactions page.

# Discussion History
## selsta | 2020-06-13T21:01:51+00:00
Do you know if the view key gets saved locally? I don’t think this is the case.

## rating89us | 2020-06-14T10:45:19+00:00
As I understand, the Monero GUI wallet file of a hardware wallet is a normal (spend) wallet that only holds the view key, and not the private key. Probably the view key is exported from the device when the wallet file is created. 

For the user experience, it seems to work like a normal (spend) wallet, because you send transactions normally using the usual fields of the send tab (the user doesn't have to use the offline transaction signing feature). However, in the background, it works like a view-only wallet that holds the private view key and does offline transaction signing in the device.

Currently, if you create a view-only wallet of a Trezor wallet, the user will not be asked to plug in the device when opening this wallet. I'm not sure, but I guess the balance of this view-only wallet is not updated correctly now, because the hardware wallet firmware is not designed to send key images and outputs to a view-only wallet.

@ph4r05

## dEBRUYNE-1 | 2020-06-14T17:53:20+00:00
In case of Ledger, the private view key is stored in RAM and not in the `.keys` file. The private view key is thus exported to the host per session basically. As a result, I think this feature will be quite difficult to implement for Ledger Monero wallets, as the architecture essentially needs an overhaul. 

## ph4r05 | 2020-06-14T18:30:23+00:00
Hi @rating89us! The hardware wallet is required for opening the wallet due to the architecture design. Moreover, the key-image refresh is being done on the fly (HW wallet required). 

As a workaround, you can export the view key and create a pure software view-only wallet that does not require a connected hardware wallet to operate (however, your balance will be shown incorrectly and the key image sync would require some manual work).

I think I am not going to refactor this as it could bring just more issues and I don't see a benefit in this overhaul (which is rather costly, I am doing this in my free time). But I can review pull requests.

## selsta | 2020-06-14T18:32:28+00:00
Yep, IMO does not sound worth it for the amount of work required.

## rating89us | 2020-06-14T18:49:21+00:00
@dEBRUYNE-1 Do you know if it is possible to create a Ledger view-only wallet file (that holds the private view key permanently)?

@ph4r05 And what do you think of redesigning this "manual work" that is required in the Trezor view-only wallet to keep the balance updated? So that when a user click a "refresh balance" button in the view-only wallet, it would be required to plug in the device, and then the view-only wallet would automatically manage the exporting of outputs and the importing of key images?

## ph4r05 | 2020-06-15T13:05:39+00:00
@rating89us - my opinion on the redesigning is basically the same, not worth the effort for the amount of work needed. I don't have free time for such feature requests (as I am doing it as a hobby, opensource devel for free). I currently don't see an easy way to do it and I have to prioritize. 

But as I said, if somebody comes with the proposal and the PR I can consult and do the review.

## dEBRUYNE-1 | 2020-06-19T11:01:46+00:00
@rating89us - In theory that should be possible I guess. However, this feature does currently not exist. 

# Action History
- Created by: rating89us | 2020-06-13T20:57:21+00:00
