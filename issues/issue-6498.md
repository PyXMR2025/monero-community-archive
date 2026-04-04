---
title: get_pruned_transaction_weight errors flooding the log
source_url: https://github.com/monero-project/monero/issues/6498
author: Forage
assignees: []
labels: []
created_at: '2020-05-03T17:13:10+00:00'
updated_at: '2020-05-09T01:51:33+00:00'
type: issue
status: closed
closed_at: '2020-05-09T01:51:33+00:00'
---

# Original Description
Hi,

I've build 0.15.0.5 for running it on Debian 10.
Still in the process (66% at the moment) of the initial pruned sync the log is getting flooded with the following error:

```
...

2020-05-03 17:10:30.152 [P2P2]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:426    get_pruned_transaction_weight does not support older range proof types
2020-05-03 17:10:30.152 [P2P2]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:426    get_pruned_transaction_weight does not support older range proof types
2020-05-03 17:10:30.152 [P2P2]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:426    get_pruned_transaction_weight does not support older range proof types
2020-05-03 17:10:30.167 [P2P2]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:426    get_pruned_transaction_weight does not support older range proof types
2020-05-03 17:10:30.167 [P2P2]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:426    get_pruned_transaction_weight does not support older range proof types

...
```
This while the syncing appear to be continuing.

For the moment I'm running `monerod` as a service with the original config and service files, with the exception of the following two additional parameters:

```
prune-blockchain=1
sync-pruned-blocks=1
```
What can be the problem here?
Let me know if you need any more info to correct this issue.

# Discussion History
## Forage | 2020-05-04T10:48:24+00:00
Not using the option `sync-pruned-blocks=1` fixes the flood of identical errors.

## moneromooo-monero | 2020-05-04T15:12:58+00:00
https://github.com/monero-project/monero/pull/6503 ought to fix it. Can you confirm ?

## Forage | 2020-05-05T08:18:00+00:00
Thanks. Testing it now but it takes a bit of time. It only appears to happing during syncing and not before having synced about 60% already. Since my blockchain was already complete I have to start from scratch again.

## Forage | 2020-05-05T09:50:18+00:00
Oddly enough there's no change. The same error occurs.
I double checked and the patch has been applied correctly before doing a completely clean build.

## moneromooo-monero | 2020-05-05T14:02:06+00:00
Annoying. I'll have to get a chain synced to that part of the chain to test. Thanks.

## moneromooo-monero | 2020-05-05T17:31:12+00:00
I could test, and I pushed a fixed version. Works for me.

## Forage | 2020-05-05T19:32:11+00:00
That did the trick. Thank you for fixing it.

## moneromooo-monero | 2020-05-09T01:51:33+00:00
Fixed

# Action History
- Created by: Forage | 2020-05-03T17:13:10+00:00
- Closed at: 2020-05-09T01:51:33+00:00
