---
title: Homebrew XMRig version is behind (2.6.4)
source_url: https://github.com/xmrig/xmrig/issues/850
author: eliasmath
assignees: []
labels: []
created_at: '2018-10-25T17:47:59+00:00'
updated_at: '2018-10-30T11:30:25+00:00'
type: issue
status: closed
closed_at: '2018-10-30T04:39:57+00:00'
---

# Original Description
Current Homebrew XMRig version is v2.6.4.

Latest released is v2.8.x that was released over 2 weeks ago.

# Discussion History
## snipeTR | 2018-10-25T18:59:00+00:00
So?

## eliasmath | 2018-10-26T14:37:15+00:00
XMRig will not mine on mac until Homebrew is at least 2.8.  There was a fork on Oct 18th...

## xmrig | 2018-10-26T14:55:15+00:00
Homebrew build supported by community, I not directly support it, some manual actions required on homebrew side, since version 2.8 required OpenSSL support.
Thank you.

## rtau | 2018-10-30T00:30:41+00:00
As per advised by xmrig, I've updated the xmrig formula in Homebrew in https://github.com/Homebrew/homebrew-core/commit/af299fcb804dbcde65434e8f7a7758149d530e33

## eliasmath | 2018-10-30T01:22:06+00:00
excellent thanks!

## xmrig | 2018-10-30T04:39:57+00:00
@rtau Thank you.

## rtau | 2018-10-30T11:22:49+00:00
From my experience, the Homebrew team will take care of version update unless something is broken with the build, then need someone to amend the homebrew formula.

@xmrig, do you prefer to take care of it or notify me, or someone else, in case help is needed again?

## xmrig | 2018-10-30T11:30:25+00:00
@rtau I'd like notify you, if something will need change again. Thank you.

# Action History
- Created by: eliasmath | 2018-10-25T17:47:59+00:00
- Closed at: 2018-10-30T04:39:57+00:00
