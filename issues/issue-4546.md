---
title: 'Couldn''t open wallet: Invalid password, on fresh wallet created with `monero-wallet-cli`'
source_url: https://github.com/monero-project/monero-gui/issues/4546
author: DirtyGadget
assignees: []
labels: []
created_at: '2026-01-05T08:12:05+00:00'
updated_at: '2026-01-12T18:32:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi

when I create a wallet with `monero-wallet-cli`
```bash
monero-wallet-cli --offline --generate-new-wallet ~/Monero/wallets/waletname/waletname
```
it generate well the wallet.

but when I try to open it with monero-gui ( open a wallet from file) I get _Couldn't open wallet: Invalid password_ even with the right password...

# Discussion History
## selsta | 2026-01-05T17:00:40+00:00
can you reproduce this with a wallet that has no password set?

## DirtyGadget | 2026-01-08T06:14:16+00:00
@selsta

I've tried, but I don't see in the `monero-wallet-cli` [documentation](http://xmrdoc6phnvjbf5hmjbwdfu47zavzfngymlnwhs2gyxxpxmad4c65kyd.onion/interacting/monero-wallet-cli-reference/) 
how to create a wallet without  password....

## nahuhh | 2026-01-08T06:17:32+00:00
you press enter

## DirtyGadget | 2026-01-12T15:03:44+00:00
It should be write in the documentation ( I'll look how to make a Pull Request for that )

So I tried with no/empty password.

same error appear in `monero-wallet-gui` _Couldn't open wallet: Invalid password_

## selsta | 2026-01-12T18:32:55+00:00
Did you change the amount of kdf rounds in advanced settings?

# Action History
- Created by: DirtyGadget | 2026-01-05T08:12:05+00:00
