---
title: Could you please make offline GnuPG signatures for GUI/CLI packages?
source_url: https://github.com/monero-project/monero-gui/issues/2495
author: hiviah
assignees: []
labels: []
created_at: '2019-11-26T00:39:57+00:00'
updated_at: '2019-11-26T23:31:25+00:00'
type: issue
status: closed
closed_at: '2019-11-26T23:31:25+00:00'
---

# Original Description
Following up on the latest web hack on package distribution, could you please make offline GnuPG signatures before publishing the packages and upload them on the getmonero page?

It is almost weird that someone could have changed the packages, but not the hashes (that were not signed, I'm guessing some kind of CDN hack).

So could you please publish GnuPG signatures of the packages on the web, while publishing the keys elsewhere? Key distribution is hard, but Keybase.io offers proofs via various ways (twitter, github, web, ...). It's hard to attack all of those. Another possibility is Key Transparency from Google (it has the same principial issue that you can't prove who was the first to register key). PGP keyservers could be an additional way. The more ways to check the key, the better.

# Discussion History
## dEBRUYNE-1 | 2019-11-26T08:35:16+00:00
I might be missing something here, but there are GPG signed hashes (from Fluffypony) available here.

https://web.getmonero.org/downloads/hashes.txt

His key is hosted on Github as well as in some other places.

https://github.com/monero-project/monero/blob/master/utils/gpg_keys/fluffypony.asc

## hiviah | 2019-11-26T23:31:25+00:00
OK I see it now. Though never noticed there were any signatures before. It's PEBKAC, but the "canonical way" is to have signature for each package (like basically other software has).

# Action History
- Created by: hiviah | 2019-11-26T00:39:57+00:00
- Closed at: 2019-11-26T23:31:25+00:00
