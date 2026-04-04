---
title: '[Bug] The GUI wallet doesn''t scan enough forward subaddresses so can sometimes
  lead to missing currency.'
source_url: https://github.com/monero-project/monero-gui/issues/4198
author: chizutan5
assignees: []
labels: []
created_at: '2023-07-16T22:22:56+00:00'
updated_at: '2023-07-16T22:22:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When using a view wallet/spend wallet combination (for Bitcart or to have spend keys kept away from a Till POS in a shop) and creating fresh subaddresses in the view wallet for each transaction, the spend wallet doesn't seem to keep up to date with all the created addresses, this means the view wallet can see recieved currency but the spend wallet cannot and this can lead to "missing" coins until enough addresses are manually created within the spend wallet.

The solution to this for now is to use `address mnew <number of addresses>` within the CLI wallet to create enough addresses up to the point that the view wallet is at, perhaps this functionality needs to be added into the GUI wallet, alongside `--subaddress-lookahead`, or perhaps there is a way to solve this in a way that has the spend wallet keep track of the addresses properly.

This probably isn't a critical bug but is worth fixing since address reuse is suboptimal, and obviously "missing" coins are also not ideal.

I have also not seen this documented elsewhere on the internet, so this may be another solution to the "I can't see my coins" problem.

# Discussion History
# Action History
- Created by: chizutan5 | 2023-07-16T22:22:56+00:00
