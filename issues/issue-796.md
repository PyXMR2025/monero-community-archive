---
title: Password on Send
source_url: https://github.com/monero-project/monero-gui/issues/796
author: tschauner-s
assignees: []
labels:
- feature
- resolved
created_at: '2017-07-16T19:03:12+00:00'
updated_at: '2017-12-13T11:18:15+00:00'
type: issue
status: closed
closed_at: '2017-12-13T11:18:15+00:00'
---

# Original Description
I think an important security feature is missing in Monero GUI currently:

- There is no password required for sending funds, even if a password is set for opening the GUI.

I think this feature should be available and set default in the Monero GUI, with options to disable them. If I accidentally forget to shutdown the GUI on my computer, my funds may be moved by someone else...

This feature request was split from issue #814.

# Discussion History
## Jaqueeee | 2017-08-07T21:04:55+00:00
great idea @wostl. Technically these are two separate requests. Please move one of them to a separate issue. 
+feature

## Timo614 | 2017-12-12T15:17:59+00:00
I spent a little time looking into this. It looks like we currently do ask for password at the time of this comment so some subsequent PR must have added this functionality.

These actions all ask for a password:

1. Sending money directly from a hot wallet
2. Sweeping from a hot wallet
3. Creating a tx file from a hot wallet

The following do not require passwords:

1. Signing a tx from a cold wallet
2. Submitting a signed tx from a hot wallet

Any thoughts on whether it's worth password protecting the latter two items? 

I guess the only benefit of password protecting the former would be for cases where the hot wallet is compromised and someone manages then to go to an open cold wallet GUI to sign the transaction (a very unlikely scenario as if you're using a cold wallet you likely have it offline so keeping the GUI open somewhere accessible seems unlikely / not sure if that risk is worth adding barriers to the flow). 

The latter seems unneeded though as you've already then presented the hot wallet's password in the generation of the tx and have had to sign it via the cold wallet at this point. I guess it couldn't hurt to add it though.

Guess if these two cases don't matter though we should be able to close this out. I just did some searching and it looks like #884 is the PR that added this functionality before.

## dEBRUYNE-1 | 2017-12-13T11:13:24+00:00
See #884.

+resolved

# Action History
- Created by: tschauner-s | 2017-07-16T19:03:12+00:00
- Closed at: 2017-12-13T11:18:15+00:00
