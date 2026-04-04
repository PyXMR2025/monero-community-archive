---
title: no mention of gitian reproducible builds in verification guides
source_url: https://github.com/monero-project/monero-site/issues/2278
author: plowsof
assignees: []
labels: []
created_at: '2024-03-15T17:24:27+00:00'
updated_at: '2025-08-06T01:17:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
e.g. in these guides
https://www.getmonero.org/resources/user-guides/verification-windows-beginner.html
https://www.getmonero.org/resources/user-guides/verification-allos-advanced.html

there is no mention of gitian reproducible hashes. and may seem that we 'trust' solely the signed hashes.txt list of hashes. when in reality it is the reproducible hashes of gitian that we trust (which bF signs after several other contributors have confirmed them)

here are the submissions for 0.18.3.3 linux binaries https://github.com/monero-project/gitian.sigs/tree/master/v0.18.3.3-linux 

a short sentence or 2 describing gitian (soon to be guix) build process would suffice i think

# Discussion History
## jermanuts | 2025-08-06T01:14:57+00:00
it is now [Guix](https://github.com/monero-project/monero?tab=readme-ov-file#guix-builds)

## nahuhh | 2025-08-06T01:16:23+00:00
It's not guix yet

## nahuhh | 2025-08-06T01:17:53+00:00
Current releases (v0.18.x.x) are gitian.

when we branch off of master, we'll start using guix. For now, there are no guix attestations 

# Action History
- Created by: plowsof | 2024-03-15T17:24:27+00:00
