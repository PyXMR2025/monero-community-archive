---
title: Provide SHA3 hashes on downloads page of getmonero.org
source_url: https://github.com/monero-project/monero/issues/3041
author: b-g-goodell
assignees: []
labels:
- invalid
created_at: '2017-12-31T18:47:54+00:00'
updated_at: '2018-01-08T13:24:30+00:00'
type: issue
status: closed
closed_at: '2018-01-08T13:24:30+00:00'
---

# Original Description
Since SHA256 is vulnerable to length extension attacks, the downloads page of getmonero.org should include at least the SHA3 hash for each file.

# Discussion History
## b-g-goodell | 2017-12-31T19:06:12+00:00
I'm aware that a more complete "canonical" list is available, but I don't think the sha256 hash should be the one on getmonero.org

## mberry | 2018-01-01T22:09:20+00:00
The hashing is to check for file integrity, not security. If getmonero/repo is compromised changing the hash is trivial. Verifying the signature determines authenticity and ensures security, the particular hash function used doesn't really matter, though it's always good to have more.
  
  

## ghost | 2018-01-03T19:11:43+00:00
Whichever the outcome is, this issue is more related to the [monero-site repository](https://github.com/monero-project/monero-site/issues).

## dEBRUYNE-1 | 2018-01-08T13:20:09+00:00
@b-g-goodell Please reopen this issue on the monero-site repository.

+invalid 

# Action History
- Created by: b-g-goodell | 2017-12-31T18:47:54+00:00
- Closed at: 2018-01-08T13:24:30+00:00
