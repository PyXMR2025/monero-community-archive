---
title: '''<'' and ''>'' characters should be removed from TX IDs in RPC mode'
source_url: https://github.com/monero-project/monero/issues/57
author: Jojatekok
assignees: []
labels: []
created_at: '2014-07-04T09:43:33+00:00'
updated_at: '2014-08-21T09:19:51+00:00'
type: issue
status: closed
closed_at: '2014-08-21T09:19:51+00:00'
---

# Original Description
No description

# Discussion History
## Neozaru | 2014-07-04T10:11:53+00:00
This has been discussed on IRC networks when developing new RPC calls.
The fact is that "old" RPC calls responses always included "<" and ">" in TX IDs, so we followed this syntax.
Additionally, changing interfaces after releases is generally a bad practice, because services/exchanges could use these interfaces (ie: Maybe they manually remove  first and last char)

A solution could be to ADD new return parameters : For example "tx_hash_proper" would be the same value as "tx_hash" without "<", ">". Changing interfaces in this way ensures retro-compatibility.


## Jojatekok | 2014-07-04T10:16:03+00:00
Yes, I remember discussing about the new rpcwallet's commands, and Fluffypony told me that first we need backend changes, and then we will deprecate old methods and introduce new ones.


## fluffypony | 2014-08-21T09:19:51+00:00
Closing this, as we'll fix it in the new RPC API when we get there.

Reference: http://monero.wikia.com/wiki/RPC_API


# Action History
- Created by: Jojatekok | 2014-07-04T09:43:33+00:00
- Closed at: 2014-08-21T09:19:51+00:00
