---
title: Allow running a node without creating/opening a wallet
source_url: https://github.com/monero-project/monero-gui/issues/1170
author: leafcutterant
assignees: []
labels:
- wontfix
created_at: '2018-03-06T16:39:38+00:00'
updated_at: '2018-03-29T23:09:16+00:00'
type: issue
status: closed
closed_at: '2018-03-29T23:09:16+00:00'
---

# Original Description
After opening and choosing a language, there should be a fourth option to just sync the blocks and act as a full node without having any wallets open.

What do you think?

# Discussion History
## sanderfoobar | 2018-03-28T23:45:48+00:00
Perhaps 2 seperate launch icons could do the trick as well (one for `monerod`, one for `monero-wallet-gui`)

## leafcutterant | 2018-03-29T00:16:36+00:00
Not sure what you mean.

If you mean that those who only want to run a full node, without a wallet open, should simply run `monerod`, then I oppose as I think there is value in enabling a "no-wallet" mode for users who are deterred by the sight of command line windows.

Speaking of that, it could be like Bitcoin Core started with the  `--no-wallet` parameter, where wallet-related content is simply not displayed on the UI.

## sanderfoobar | 2018-03-29T22:57:46+00:00
I hear what you're saying. However, I believe that users will not be deterred by a command prompt, as those that have a full-node requirement (and ofc, everyone should) will either:

- Take peace with leaving the GUI on
- Will find out how to run the daemon without using the GUI

Wont implement for now, as the development time needed to implement these changes don't compare up to the value such a feature will bring to the table.

## sanderfoobar | 2018-03-29T23:01:56+00:00
+wontfix

# Action History
- Created by: leafcutterant | 2018-03-06T16:39:38+00:00
- Closed at: 2018-03-29T23:09:16+00:00
