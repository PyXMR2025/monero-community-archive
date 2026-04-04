---
title: 'Replacing boost serialization with something else (eg cereal) offering compatibility '
source_url: https://github.com/monero-project/monero/issues/1430
author: kenshi84
assignees: []
labels: []
created_at: '2016-12-11T04:52:48+00:00'
updated_at: '2016-12-14T09:28:52+00:00'
type: issue
status: closed
closed_at: '2016-12-14T09:28:52+00:00'
---

# Original Description
PR #1435 

As mentioned in previous issues #1106 #1341, it seems useful to be able to read wallet cache file from different platforms independent of the boost version used for building the wallet software.

@hyc mentioned on IRC that in the future, boost serialization may be replaced by LMDB which eliminates the boost serialization compatibility issue. Is anyone working on actually implementing this?

Have people considered another library called [cereal](https://github.com/USCiLab/cereal)? It's a header-only library and I found it quite easy to use in my past projects. If no one is working on it, I'd be up for contributing a patch.

# Discussion History
## ghost | 2016-12-11T09:55:28+00:00
Is cereal being maintained? There are PRs hanging around from 2-3 years ago. 

## kenshi84 | 2016-12-11T11:41:21+00:00
As I skimmed through some of those 2-3 year old PRs, they're mostly a bit controversial requiring discussion which seems to be continuing (albeit not too actively), so the project seems overall reasonably actively maintained.

## moneromooo-monero | 2016-12-11T14:06:04+00:00
hyc has been thinking about this for a while.
There are other constraints behind "must be compatible between architectures", though:
- data must be encrypted
- would be nice to not have it all in memory (for large wallets, it can be significant)


## kenshi84 | 2016-12-11T14:41:13+00:00
@moneromooo-monero: I suppose the first constraint is satisfied currently by doing encryption  before serialization / decryption after de-serialization?
Is the second constraint satisfied currently?

## moneromooo-monero | 2016-12-11T21:38:17+00:00
Yes, and no.

## kenshi84 | 2016-12-12T01:13:17+00:00
@moneromooo-monero thanks! Looks like I need to study a bit more how serialization is implemented currently, it's more complicated than I initially thought :)

# Action History
- Created by: kenshi84 | 2016-12-11T04:52:48+00:00
- Closed at: 2016-12-14T09:28:52+00:00
