---
title: '[FR] Don''t ask for a wallet password until a wallet password is actually
  needed.'
source_url: https://github.com/monero-project/monero-gui/issues/3834
author: ITwrx
assignees: []
labels: []
created_at: '2022-02-05T17:18:00+00:00'
updated_at: '2022-05-26T15:46:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Most of the time when i open the GUI wallet i'm just wanting to let the blockchain sync, not needing to send or even view a wallet's balance. 

I think it would be better UX for the GUI to just open up and start syncing and only ask for a password once a password is required for the action the user has initiated. I'm assuming the wallet doesn't have to be unlocked for the blockchain to be synced.

thanks

# Discussion History
## selsta | 2022-04-27T04:26:36+00:00
Starting the daemon manually would be possible workaround, assuming that you don't use a custom blockchain location.

## stefan-reich | 2022-05-26T15:46:05+00:00
Also, how about not asking for the password when the password is the empty string :)

# Action History
- Created by: ITwrx | 2022-02-05T17:18:00+00:00
