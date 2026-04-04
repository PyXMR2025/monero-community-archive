---
title: Hide mnemonic and add unhide button
source_url: https://github.com/monero-project/monero-gui/issues/2823
author: brandsimon
assignees: []
labels:
- enhancement
created_at: '2020-04-07T13:08:56+00:00'
updated_at: '2020-04-22T20:48:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When creating a new wallet, the mnemonic is shown by default in plaintext.
I dont think this is a secure practice.
I'd like to create a new wallet while somebody (cameras) can look at my screen without being able to access my wallet.
Probably a copy to clipboard button is also a nice feature.

# Discussion History
## selsta | 2020-04-07T13:17:24+00:00
Even with the large seed and warnings we still have users who don’t write down the seed. I don’t think hiding it is a good idea.

We also want to encourage writing down the seed physically, not copying it to the clipboard and saving it to a textfile.

I wonder how to implement your feature request whiteout encouraging bad practices to new users.

## brandsimon | 2020-04-07T23:20:00+00:00
@selsta 
Thank you for the answer, I totally understand your concern.
Is there a checkbox on the mnemonic view that users have to check to continue like `I have written down the mnemonic or I am totally aware what will happen if I loose the secret (money loss)`?

For my use case a commandine option to create a wallet file would be enough, as long as when importing it to the gui the secret is never shown on the screen.

## garlicgambit | 2020-04-08T18:02:30+00:00
You could make it an advanced feature. Put it under advanced options with a checkbox to hide the seed by default.

# Action History
- Created by: brandsimon | 2020-04-07T13:08:56+00:00
