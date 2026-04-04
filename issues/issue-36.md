---
title: simplewallet refresh should include optional height param
source_url: https://github.com/monero-project/monero/issues/36
author: monero-project
assignees: []
labels:
- enhancement
created_at: '2014-06-13T00:49:14+00:00'
updated_at: '2014-08-02T09:22:17+00:00'
type: issue
status: closed
closed_at: '2014-08-02T09:22:17+00:00'
---

# Original Description
Simplewallet currently refreshes from height 0. However, if you are making a new wallet and have not used that wallet address before, it seems unnecessary to sync from block 0 as there can not possibly be utxos belonging to you from blocks before the current height.

I would propose that refresh should have an optional height argument, eg
refresh [height]
where height allows you to indicate when you'd like to start looking for utxos (which must be higher than the last block which the wallet was synced to).

This should also be the default behaviour when generating a new wallet.


# Discussion History
## fluffypony | 2014-07-31T08:22:29+00:00
simplewallet (by default) syncs up from the "creation date" that is serialised and stored in the .keys file

This option should disregard the date and sync from the block height


## jakoblind | 2014-08-01T08:33:41+00:00
My solution sends start_height parameter in the RPC call and only receives blocks newer than that block. 
https://github.com/jakoblind/bitmonero/commit/e4273f24153ca5222ab0af6ea6d84b7761e31f05


## fluffypony | 2014-08-01T08:36:13+00:00
Awesome - up for testing:) When you get a moment, can you add the start_height optional parameter to the simplewallet "refresh" CLI command as well? Good job!!


## jakoblind | 2014-08-01T08:38:10+00:00
i already added it to the refresh command. just try:
 refresh 153000

if the number cant be parsed it just treats it as 0.


## fluffypony | 2014-08-01T08:39:21+00:00
Oh brilliant, I don't know how I missed that in glossing through the code!


## jakoblind | 2014-08-01T08:48:14+00:00
Right now I'm thinking about this: "This should also be the default behaviour when generating a new wallet."

After a new wallet is generated, it is not automatically synced but the user have to write "refresh" command manually. Should we instead do autosync after wallet creation? 


## fluffypony | 2014-08-01T08:54:27+00:00
@jakoblind I'd say no - reason being that simplewallet is also used for offline wallet creation, so you don't want it trying to sync when the daemon may not even be accessible. Those who will use simplewallet in the long run and not touch any of the forthcoming GUI tools will be intelligent enough to refresh after create (one hopes;)


## fluffypony | 2014-08-01T22:17:05+00:00
Tested and working - can you wrap this into a PR so we can merge? Thank you!


## fluffypony | 2014-08-02T09:22:17+00:00
Merged, thank you @jakoblind!


# Action History
- Created by: monero-project | 2014-06-13T00:49:14+00:00
- Closed at: 2014-08-02T09:22:17+00:00
