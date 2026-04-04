---
title: Starting monerod with block-sync-size >~ 100 prevents daemon to sync
source_url: https://github.com/monero-project/monero/issues/9897
author: kuchta
assignees: []
labels: []
created_at: '2025-04-07T11:31:24+00:00'
updated_at: '2025-08-27T18:27:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Starting monerod with larger block-sync-size than ~100 (tested 200, 500, 1000, 10000) prevents unsynced daemon from synchronizing by going into some strange loop that only prints over and over again:

```
SYNCHRONIZATION started
91.218.20.4:18080 OUT Sync data returned a new top block candidate: 2552513 -> 3384786 [Your node is 832273 blocks (3.2 years) behind] 
SYNCHRONIZATION started
52.143.116.21:18080 OUT Sync data returned a new top block candidate: 2552513 -> 3384786 [Your node is 832273 blocks (3.2 years) behind] 
SYNCHRONIZATION started
4.227.140.143:18080 OUT Sync data returned a new top block candidate: 2552513 -> 3384786 [Your node is 832273 blocks (3.2 years) behind] 
SYNCHRONIZATION started
```

.bitmonero/bitmonero.conf:
```
prune-blockchain=1
sync-pruned-blocks=1
db-sync-mode=fast:async
block-sync-size=100
enable-dns-blocklist=1
bootstrap-daemon-address=auto
```

# Discussion History
## nahuhh | 2025-04-07T12:09:43+00:00
its a bug that requires either a network upgrade to change, or relaying info to peers about whether they can send > 100. 

The max is supposed to be 2048

## kuchta | 2025-04-07T12:52:39+00:00
Thank you for clarification, @nahuhh. After some time synchronizing with block-sync-size=100 it also went into that loop so I had to restart the process with default (0 == adaptive) which at the moment fetchces just 20 blocks at the time. Is there something else one can to do to speed up the sync?

## nahuhh | 2025-04-07T13:03:53+00:00
There are serialization limits that effectively add size restrictions to the batches being pulled in. 100 will hit those limits at some point after ringct. Once blocks grow in the future, 20 will also fail.


pr #9494 introduces a dynamic block sync size that will auto-adjust, and #8867 fixes the serialization limits 

edit: also re `default (0 == adaptive)`. 0 = 100 pre-V4 and 20 post-V4 (fixed valued based on block heights). Its not truly adaptive until 9494 is approved

## noelportillo | 2025-04-08T01:58:44+00:00
very good

## jeffro256 | 2025-08-27T14:48:27+00:00
I don't think the serialization limit is what @kuchta is hitting. It is more likely the `CURRENCY_PROTOCOL_MAX_OBJECT_REQUEST_COUNT` limit enforced at: https://github.com/monero-project/monero/blob/09bb3705e01e0f9fd62eaaad7607e7f1877a0098/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L991-L999
This causes the connection to be dropped. IMO, we should output an error message when the user tries to set the `block-sync-size` setting higher than `CURRENCY_PROTOCOL_MAX_OBJECT_REQUEST_COUNT`.

## nahuhh | 2025-08-27T15:39:03+00:00
> I don't think the serialization limit is what @kuchta is hitting. It is more likely the `CURRENCY_PROTOCOL_MAX_OBJECT_REQUEST_COUNT` limit enforced at: https://github.com/monero-project/monero/blob/09bb3705e01e0f9fd62eaaad7607e7f1877a0098/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L991-L999
> This causes the connection to be dropped. IMO, we should output an error message when the user tries to set the `block-sync-size` setting higher than `CURRENCY_PROTOCOL_MAX_OBJECT_REQUEST_COUNT`.


right. When >100 its not serialization, but the config posted shows 100

```
prune-blockchain=1
sync-pruned-blocks=1
db-sync-mode=fast:async
block-sync-size=100
enable-dns-blocklist=1
bootstrap-daemon-address=auto
```


I agree that setting a higher bss than `CURRENCY_PROTOCOL_MAX_OBJECT_REQUEST_COUNT` should warn user that it cant be set above that.

but still, at this point in time, manually setting at ~50 or above will eventually (during IBD) hit the serialization limits

## jeffro256 | 2025-08-27T16:47:52+00:00
This is also true. @kuchta is that config the one used while hitting the loop? Or was it higher before?

## kuchta | 2025-08-27T18:27:44+00:00
It's a long time ago, but I **believe** both is true, so it was the one used while hitting the loop, but it was also higher before, as I gradually lowered the value...

# Action History
- Created by: kuchta | 2025-04-07T11:31:24+00:00
