---
title: CLI Wallet can't load filenames with spaces in them
source_url: https://github.com/monero-project/monero/issues/9230
author: tidux
assignees: []
labels:
- question
- more info needed
created_at: '2024-03-10T08:01:08+00:00'
updated_at: '2024-03-23T20:50:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Several wallets including Cake and Feather allow loading of filenames with spaces in them, and Cake names wallets with multiple spaced words by default.  Entering the spaced name when prompted by the CLI resulted in it not finding the wallet, but renaming the wallet and wallet.keys files to remove spaces allowed the CLI Wallet to load them.  I'm not sure if this is a deliberate limitation in the CLI wallet or a parser bug.

# Discussion History
## plowsof | 2024-03-10T10:54:34+00:00
Spaces in filenames have to be escaped when typing in the terminal. That is out of scope for the Monero CLI and more an issue with your operating system or whichever terminal you are using 

## tidux | 2024-03-11T15:08:44+00:00
This isn't from the shell though, this is the interactive prompt within the wallet program when started without a `--wallet` or `--restore-from-foo` option.

## moneromooo-monero | 2024-03-23T20:50:45+00:00
Works fine here. Double check ?

# Action History
- Created by: tidux | 2024-03-10T08:01:08+00:00
