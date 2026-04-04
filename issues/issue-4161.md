---
title: 'ux: restore wallet and cancel password dialogue '
source_url: https://github.com/monero-project/monero-gui/issues/4161
author: plowsof
assignees: []
labels: []
created_at: '2023-04-25T02:22:46+00:00'
updated_at: '2023-04-25T02:24:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
when restoring a wallet from seed/keys - clicking create wallet on the final screen opens the password dialogue - if you cancel this , you are returned back. however, the restart() function in wizardcontroller was called, and everything has been reset / you are trapped seeing electrum seed empty. it should check if the current state is wizard (wizardCreateWallet5) then return users to the WizardOpenWallet1 page (as the wallet has been created already)

# Discussion History
# Action History
- Created by: plowsof | 2023-04-25T02:22:46+00:00
