---
title: Make archived /bitmonero Available on getmonero.org for Download
source_url: https://github.com/monero-project/monero-site/issues/2027
author: Cactii1
assignees: []
labels:
- downloads
- enhancement
created_at: '2022-08-16T23:00:10+00:00'
updated_at: '2022-10-07T16:42:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently there's a blockchain.raw file available on getmonero.org that allows people to download the blockchain and import it using the blockchain import tool. This is still very resource intensive so it's not suitable for a lot of people.

An alternative might be to archive a known good /bitmonero directory and make it available for download. Doing this would allow some users an option that is almost plug and play. A user would only have to download, and unarchive the directory into the correct location and then sync some of the last blocks since the archive was made. This could be done with a pruned chain as well, making two archive downloads available.

Of course the archive should have the verification hashes included (why doesn't the blockchain.raw feature have that anyways?) like the other Monero downloads.

I know that this is a shortcut and that everybody should verify their own blockchain on the network but maybe we could have options for the people that don't have the resources to or for those who just don't want to.

# Discussion History
## HardenedSteel | 2022-10-07T09:53:17+00:00
Instead hosting ./bitmonero files on getmonero.org can we implement skip verifying blockchain as a feature? Like user can able skip 80-90% of the old blockchain.

## Cactii1 | 2022-10-07T16:42:58+00:00
I would think that there would be a way to programmatically derive a hash at certain points in the blockchain and have nodes store the hash so that newer nodes that are syncing could just ask other nodes for the hash to be able to compare to its own. This way there's still some sort of verification going on.

# Action History
- Created by: Cactii1 | 2022-08-16T23:00:10+00:00
