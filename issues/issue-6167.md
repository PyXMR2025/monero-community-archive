---
title: '[RELEASE] Wallet API accepts only long payment id format'
source_url: https://github.com/monero-project/monero/issues/6167
author: naughtyfox
assignees: []
labels: []
created_at: '2019-11-21T11:30:47+00:00'
updated_at: '2019-11-21T13:36:15+00:00'
type: issue
status: closed
closed_at: '2019-11-21T13:36:15+00:00'
---

# Original Description
When we try to set short payment id to a transaction we get the following error: 
```
payment id has invalid format, expected 64 character hex string
```

Despite support of long payment ids is deprecated it appears to be the only acceptable format if you use `wallet2_api.h` interface. It was deleted in this commit - https://github.com/monero-project/monero/commit/def703abecbd55fdb358b31250bd722766aa24d1. 


# Discussion History
## selsta | 2019-11-21T11:32:22+00:00
Can you use integrated addresses?

## naughtyfox | 2019-11-21T11:52:23+00:00
Yes, we can use integrated addresses. But I think this is a bug nevertheless.

## selsta | 2019-11-21T11:53:37+00:00
AFAIK support for separate short payment IDs has been removed everywhere in the codebase.

## naughtyfox | 2019-11-21T12:04:26+00:00
IIRC integrated address is just an address + payment id. As long as integrated addresses are supported the payment ids should also be. I know for sure that long payment id format is deprecated, but not short one.

## selsta | 2019-11-21T12:52:36+00:00
I did only support 64 character payment IDs intentionally in def703a. Maybe someone else can comment if this is wrong, but I thought that short payment IDs should **always** use the integrated format.

## hyc | 2019-11-21T12:58:13+00:00
That was my understanding as well, always integrated format.

## naughtyfox | 2019-11-21T13:36:15+00:00
Ok, sorry then.

# Action History
- Created by: naughtyfox | 2019-11-21T11:30:47+00:00
- Closed at: 2019-11-21T13:36:15+00:00
