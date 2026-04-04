---
title: '[FEATURE REQUEST] Cold Spending Improvements'
source_url: https://github.com/monero-project/monero-gui/issues/822
author: JollyMort
assignees: []
labels:
- feature
created_at: '2017-08-16T21:25:58+00:00'
updated_at: '2017-08-18T13:00:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
With regards to cold spending functionality introduced in [#398](https://github.com/monero-project/monero-core/pull/398) I believe it would be useful to add GUI functions for import/export outputs and import/export key images, to match the functions of the CLI wallet. Those are essential if you want to do cold spending, and to fix any problems if users do unexpected things. Right now, you still have to fire up the CLI for many cases.

Let's walk through the possiblities:

## 1 Creating the wallet pairs

### 1.1: Import from keys

This means there's no way the watch wallet can know the key images at creation. It can sync with the blockchain, find the outputs, and that's it. It can't know the status of them without importing key images.

On the cold side, if the cold counterpart is imported from keys and without the blockchain copy, it will not have the outputs so it can not generate the key images. The user must somehow transfer the knowledge of outputs from the watch wallet to the cold wallet. There are 2 ways to address this: either use the import/export outputs, or copy the entire blockchain database from the online machine. The latter can be cumbersome considering the size, so import/export outputs would be the preferred method.

Either way, the cold wallet must export the key images, and the watch wallet must import them as to have the correct state.

### 1.2: Create from full wallet

This way, the watch wallet can inherit whatever the full wallet is aware of. Thing is, if you want to keep the full wallet cold, then by definition you can't sync it online.

There's only 1 way to address this: sync a node on the online machine, copy the blockchain database to the cold machine, refresh the full wallet, and then make the watch wallet with key images bundled. When the wallet files are copied to the online PC, the watch wallet will see the correct balance as it will have a corresponding key image for each output (unless something new is received).

It's my understanding that this is how both CLI / GUI do it. However, I noticed inaccurate balance with the GUI, so maybe there's a bug somewhere. It's fixed when doing import/export key images from the CLI, so maybe some key image is missing for whatever reason.

## 2 Spending

### 2.1 Watch wallet with knowledge of all the key images

This is easy. It creates a 100% valid TX which has to be signed by the cold wallet. Since it's creating the change output, it will be part of the TX so it will be piggy-backed to the cold wallet.

The cold wallet signs the TX. Since the change output was delivered as part of TX destinations, cold wallet must recognize it and can automatically create the matching key image which can get a piggy-back ride with the signed TX. In fact, any output destined to the same wallet, must also be recognized and key image created for that output as well.

It's my understanding this is done with both CLI/GUI.

### 2.2 Watch wallet with partial knowledge of key images

The wallet has key images for some outputs. From there it can establish some 100% spendable balance if it ignores the outputs without a missing key image. Then, the process would be the same as in 2.1 but all outputs could be piggy-backed to cold wallet, and all key images back from it to fill the gaps.

Also, even for the outputs with no key images, the wallet could establish that some are 100% not spent (if they never appear on the blockchain*). If they do appear, it can't know whether it's spent or not and it should not be used as the user would risk creating a non-valid TX (double-spend).

### 2.3 Watch wallet with no knowledge of key images

We can also establish some 100% not spent outputs and use only those (if outputs never appear on the blockchain*). Use the opportunity to piggy-back outputs and key images in the TX.

*requires looking up whether the output appears in any ring signature on the blockchain, if not - it's 100% not spent. I assume this would take a while unless we're indexing outputs in the db. If we make some changes to increase the ring size dramatically, or a kind of "wear-levelling" so least-picked outputs are given priority, then this method would become invalid but privacy improved since every output would eventually get picked at least once.

### 2.4 Blind attempt / best effort

Use all outputs as if they're all not spent, prioritizing those 100% not spent. All outputs with missing key images should be piggy-backed with the TX. The cold wallet will produce all key images and they'll be piggy-backed to with the signed TX.

The watch wallet can now check whether any outputs in the signed TX are already spent and reject to broadcast it. User is asked to do another TX, and this time it will be the case of 2.1 since we just imported the key images.

## To summarize:

- 1.1 with import/export outputs and key images is 100% fail-safe way to have the correct balance, CLI allows this, GUI does not
- 1.2 may or may not give the correct balance, depending on the state of full wallet when it created the watch wallet. The user could be requested to perform import/export stuffs if it's detected some outputs are missing their key images.

- 2.1 is a fail-safe way to spend, CLI / GUI allow this
- 2.2 with allowing to spend only 100% not spent outputs is also fail-safe but may have bad user experience as the displayed/spendable balance will be inaccurate. 2.1 could become 2.2 if something new is received in the meantime. It would be auto-magically fixed from 2.2 to 2.1 when doing a TX, or the user could be alerted that some outputs are missing key images and requested to do imports/exports if he only wants to monitor. (not sure if implemented)
- 2.3 can't make the double-spend if guards are in place, but it not sure if it could easily be implemented. Converted to 2.1 with the first cold TX done. (not sure if implemented)
- 2.4 anything can happen. converted to 2.1 with the first cold TX (either rejected or performed) (not sure if implemented)

In any case, any weird state can always be fixed by manual import/export, and that's why it would be useful to have in the GUI.

# Discussion History
## JollyMort | 2017-08-16T21:28:46+00:00
@NanoAkron I think it was you who told me about the piggy-back so fyi; @moneromooo-monero fyi as well

## dEBRUYNE-1 | 2017-08-18T12:55:13+00:00
+feature

## Jaqueeee | 2017-08-18T12:56:04+00:00
the bug mentioned in 1.2 is fixed in https://github.com/monero-project/monero/pull/2309
When creating a view only wallet, all cached data is copied from the full wallet. 

# Action History
- Created by: JollyMort | 2017-08-16T21:25:58+00:00
