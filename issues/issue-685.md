---
title: Wallet restore from view / spend keys
source_url: https://github.com/monero-project/monero/issues/685
author: fluffypony
assignees: []
labels:
- enhancement
created_at: '2016-02-21T22:16:08+00:00'
updated_at: '2016-04-22T04:03:03+00:00'
type: issue
status: closed
closed_at: '2016-03-03T23:46:21+00:00'
---

# Original Description
It's possible to create a non-deterministic wallet (`--non-deterministic`) that isn't created from a mnemonic seed. It's also possible to disregard a wallet's mnemonic seed and just note down the spend and view keys, visible within the wallet using the `spendkey` and `viewkey` commands respectively.

The problem is that restoring wallets, without a mnemonic, requires the seed. This addition in functionality would allow wallets to be restored from private keys. It should follow the current flag convention, and add a `--restore-from-keys` flag. During the restoration it should prompt for both view and spend keys, validate that the keys are valid, and then create the wallet from them.

@auswalk has expressed interest in tackling this task, so it is assigned to him at present.


# Discussion History
## allenwalker3 | 2016-02-27T21:44:53+00:00
I'm still running into issues compiling monero on linux (ubuntu). Is this a known issue? I will probably try again from scratch but I wanted to check.


## iamsmooth | 2016-03-03T22:52:24+00:00
Solved by #688, can be closed now


## allenwalker3 | 2016-04-22T04:03:03+00:00
Hi riccardo, we haven't talk in a while. Was curious if you have any kind
of ETA on a native gui of monero? Thanks and keep up the good work!

On Sun, Feb 21, 2016 at 3:16 PM, Riccardo Spagni notifications@github.com
wrote:

> It's possible to create a non-deterministic wallet (--non-deterministic)
> that isn't created from a mnemonic seed. It's also possible to disregard a
> wallet's mnemonic seed and just note down the spend and view keys, visible
> within the wallet using the spendkey and viewkey commands respectively.
> 
> The problem is that restoring wallets, without a mnemonic, requires the
> seed. This addition in functionality would allow wallets to be restored
> from private keys. It should follow the current flag convention, and add a
> --restore-from-keys flag. During the restoration it should prompt for
> both view and spend keys, validate that the keys are valid, and then create
> the wallet from them.
> 
> @auswalk https://github.com/auswalk has expressed interest in tackling
> this task, so it is assigned to him at present.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/685.

## 

View my Public Key
http://pgp.mit.edu/pks/lookup?op=get&search=0x0C2469FFCE5F3498 for secure
communication


# Action History
- Created by: fluffypony | 2016-02-21T22:16:08+00:00
- Closed at: 2016-03-03T23:46:21+00:00
