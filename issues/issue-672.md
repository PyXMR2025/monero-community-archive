---
title: 'algo: cryptonight-lite ignored when variant:1 specified.'
source_url: https://github.com/xmrig/xmrig/issues/672
author: cryptonote-social
assignees: []
labels:
- bug
created_at: '2018-06-03T16:48:18+00:00'
updated_at: '2018-06-17T17:57:48+00:00'
type: issue
status: closed
closed_at: '2018-06-17T17:57:48+00:00'
---

# Original Description
In my v.2.5 config files for Aeon and TRTL I had specified "algo: cryptonight-lite" at the top, and "variant: 1" in the pools section.   When I ran it with v2.6.2, it defaulted to cryptonight algorithm instead of cryptonight lite.  The fix was to change algo to "cn-lite/1",  but ideally it would be backwards compatible.  Perhaps "variant: 1" in the pools section is overriding the algo: field inappropriately?

# Discussion History
## cryptonote-social | 2018-06-03T16:57:49+00:00
After a bit more debugging it appears a combination of user error and software change.

I had actually specified "algo: cryptonight-light" (light vs lite) and that *used* to work but no longer does.  Perhaps xmrig can be made to complain when an invalid algo is specified instead of fall back silently to regular cryptonight?

## xmrig | 2018-06-03T19:15:54+00:00
`cryptonight-light` is invalid algorithm name, but for some reason it used too, better use `cryptonight-lite` or `cn-lite`.

Anyway I fixed it, name `cryptonight-light` now supported again, it was a bug, and miner show error message and exit if invalid algorithm specified.
Thank you.

## xmrig | 2018-06-17T17:57:48+00:00
Fixed in v2.6.3.

# Action History
- Created by: cryptonote-social | 2018-06-03T16:48:18+00:00
- Closed at: 2018-06-17T17:57:48+00:00
