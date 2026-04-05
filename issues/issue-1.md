---
title: 128tx exploit
source_url: https://github.com/xmrig/xmrig/issues/1
author: esfomeado
assignees: []
labels: []
created_at: '2017-04-19T13:37:51+00:00'
updated_at: '2018-11-05T06:58:18+00:00'
type: issue
status: closed
closed_at: '2018-11-05T06:58:17+00:00'
---

# Original Description
https://www.reddit.com/r/Monero/comments/5pun87/miner_exploit_this_is_why_we_need_a_bug_bounty/

https://github.com/genesismining/sgminer-gm/commit/608c9885cbaa89b5f2846e8d1661dda02d2ba8ae

# Discussion History
## xmrig | 2017-04-21T16:23:41+00:00
Ok the task looks easy, add variable length support for blob (76+). It's right?

One moment unclear, what is the upper limit? 128 or more? in xmr-stak-cpu code I see 112. It's little bit confusing. Thank you.

## fireice-uk | 2017-04-21T17:33:18+00:00
The maximum length is 75 fixed + 9 variable so 84. I have a habit of rounding the sizeof manually sometimes.

## xmrig | 2017-04-22T11:04:22+00:00
@fireice-uk 
```
piNonce = (uint32_t*)(oWork.bWorkBlob + 39);
```
It's ok? looks like another magic number.

## fireice-uk | 2017-04-23T13:37:13+00:00
This is the nonce position in the miner's blob. The variable length fields that are included there are major_version, minor_version and timestamp. None of them are under control of the end user enough to make stuff fall out of place (section 4.1 here https://cryptonote.org/cns/cns003.txt )

If you want to avoid magic numbers completely then you can parse the whole thing ( see section 1.2 here for a public domain parsing code https://tukaani.org/xz/xz-file-format.txt ). 



## smoresmores | 2017-08-31T08:34:04+00:00
Is this issue solved? @xmrig 

## xmrig | 2017-08-31T10:14:25+00:00
Probably yes, at least three no overflows now, but I not 100% sure it works as expected.

# Action History
- Created by: esfomeado | 2017-04-19T13:37:51+00:00
- Closed at: 2018-11-05T06:58:17+00:00
