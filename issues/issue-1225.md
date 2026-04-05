---
title: Add option to disable old CryptoNight variation
source_url: https://github.com/xmrig/xmrig/issues/1225
author: ghost
assignees: []
labels:
- question
created_at: '2019-10-07T17:30:24+00:00'
updated_at: '2019-10-10T13:16:17+00:00'
type: issue
status: closed
closed_at: '2019-10-10T13:16:16+00:00'
---

# Original Description
Could you consider add this option in futre release ?

# Discussion History
## xmrig | 2019-10-08T03:04:21+00:00
Isn't that what you are looking for? https://github.com/xmrig/xmrig/blob/master/src/config.json#L28
Thank you.

## ghost | 2019-10-09T14:28:30+00:00
thank for your reply but i mean the Cmake flag , like -DWITH_CRYPTONIGHT=OFF

## xmrig | 2019-10-09T14:35:56+00:00
https://github.com/xmrig/xmrig/blob/master/doc/build/CMAKE_OPTIONS.md#algorithms but currently not possible complete disable all cryptonight algorithms.

## ghost | 2019-10-10T13:16:16+00:00
Thanks for your answer

# Action History
- Created by: ghost | 2019-10-07T17:30:24+00:00
- Closed at: 2019-10-10T13:16:16+00:00
