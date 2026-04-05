---
title: API not reporting errors
source_url: https://github.com/xmrig/xmrig/issues/589
author: donovansolms
assignees: []
labels:
- wontfix
created_at: '2018-04-27T08:16:29+00:00'
updated_at: '2018-11-05T13:32:07+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:32:07+00:00'
---

# Original Description
In version v2.5.3 and v2.6.0-beta3 the API doesn't seem to report errors.

## Connection errors

**To replicate**

1. Run xmrig against a pool that supports validation of the address for Stellite
`./xmrig -o pool.xtl.fairhash.org:3333 -u ThisIsAnInvalidAddress -p apitest --api-port 16000 `

2. You'll see an error printed in the terminal 
`[2018-04-27 10:04:16] [pool.xtl.fairhash.org:3333] error: "invalid address used for login", code: -1`

3. Open the API at http://localhost:16000, you'll see no errors are reported

**Expected behaviour**
I'd expect the error to be listed under connection's error_log.

## Result/share errors

**To replicate**
1. Run xmrig against the Stellite community pool using the incorrect variant
`./xmrig -o communitypool.stellite.cash:6677 -u Se3sNoW8R9S7mF72SeUHrudscxVvvdCJ3Vh3jzZGykJwYB9mFjcWfAhBzi4Pr9vxbRHP7jb75odgoYGyzeiNzEwQ26xJTwTKp -p apitest --api-port 16000 --variant -1`

2. You'll see an error printed in the terminal 
`[2018-04-27 10:09:14] rejected (0/1) diff 1000 "Low difficulty share" (411 ms)`

3. Open the API at http://localhost:16000, you'll see no errors are reported

**Expected behaviour**
I'd expect the error to be listed under results' error_log.

I've scanned the code and it looks like the errors are not added to the API in `ApiState.cpp`. It would be great to have this fixed with #581 for the Stellite GUI miner.

Any thoughts?

# Discussion History
## xmrig | 2018-04-27T09:01:17+00:00
Errors in API was never implemented, it just for compatibility with xmr-stak api.json
Thank you.

# Action History
- Created by: donovansolms | 2018-04-27T08:16:29+00:00
- Closed at: 2018-11-05T13:32:07+00:00
