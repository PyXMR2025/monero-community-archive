---
title: '[idea] combine key image signing with cold transaction signing'
source_url: https://github.com/monero-project/monero/issues/4182
author: dnaleor
assignees: []
labels:
- invalid
created_at: '2018-07-27T12:51:21+00:00'
updated_at: '2018-08-09T02:18:56+00:00'
type: issue
status: closed
closed_at: '2018-07-27T16:16:59+00:00'
---

# Original Description
I'm writing this issue because me (and others) were under the impression that the balance in a view wallet will always be correct after a first transaction, as long as you keep using the same view wallet. So you could for example check if you're hacked by just refreshing the view wallet. Recently, I discovered this to be false. Users get a false sense of security when they assume that the balance in the view wallet is indeed what they expect it to be, but it seems that you can't trust this number.

It seems that "rescan_bc" resets some kind of flags in the view wallet which results in a wrong balance (usually too high as change is counted as incoming transaction). "rescan_spent" doesn't solve this because it seems that the view wallet doesn't contain the key images.

To make it a bit more intuitive, I think it would be a good idea to do the exporting of outputs and signing of key images "in the background" when you are doing a cold signing.

1) when creating an unsigned_monero_tx, additional data can be included:
the view wallet could check for which outputs the key image is not present. These outputs are added to the unsigned_monero_tx

2) when running "sign_transfer" in the cold wallet, these outputs are imported and the signed key images will be added to the file "signed_monero_tx". Also, the key image of the change output should be signed and added. 

3) when running "submit" in the view wallet, all signed key images will be imported.

This will greatly increase the usability of the cold signing procedure. At least users will know they are hacked before they attempt a cold signing transaction. Maybe some notification could be added to the "balance" command for newly received outputs (after the last cold signing) for which the key image is not present yet in the view wallet. Example: balance after cold signing was 1 XMR, 0.234 XMR was received after last outgoing transaction. This could look like this:

`Balance: 1.234, unlocked balance: 1.234,` 
`Checked balance: 1, unchecked balance: 1.234`



# Discussion History
## moneromooo-monero | 2018-07-27T16:10:18+00:00
It does that already.

+invalid


## dnaleor | 2018-07-28T02:10:24+00:00
I just checked... even though the wallet seems to import the key images as I described in this github issue, it still seems that rescan_bc does somehow makes the balance wrong again. It seems to forget the imported key images.

Is this expected behaviour? If not, there needs to be some changes. If it is, maybe some warning about forgetting imported key images should be displayed when running the command. 

cc @moneromooo-monero 

## stoffu | 2018-08-09T02:18:56+00:00
`rescan_bc` is the same as manually deleting the wallet cache file and opening the `.keys` file, so the imported key images being lost is an expected behavior.

# Action History
- Created by: dnaleor | 2018-07-27T12:51:21+00:00
- Closed at: 2018-07-27T16:16:59+00:00
