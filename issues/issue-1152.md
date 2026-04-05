---
title: Embedded config unable to open "/xmrig/build/config.json"
source_url: https://github.com/xmrig/xmrig/issues/1152
author: stinkefisch
assignees: []
labels:
- question
created_at: '2019-08-30T10:42:55+00:00'
updated_at: '2019-08-30T22:31:34+00:00'
type: issue
status: closed
closed_at: '2019-08-30T22:31:34+00:00'
---

# Original Description
Hi,
I have updated /xmrig/src/core/config/Config_default.h with my config and compile via 
cmake .. -DWITH_HTTPD=OFF -DWITH_EMBEDDED_CONFIG=ON

However when I start xmrig it gives me
unable to open "/xmrig/build/config.json"

# Discussion History
## xmrig | 2019-08-30T10:47:26+00:00
Miner first try load external config if it fails, used embedded config.
Thank you.

## stinkefisch | 2019-08-30T10:51:29+00:00
Thanks for the reply,

I haven't got external config why is it still failing and not using the embedded one ?

## xmrig | 2019-08-30T11:10:03+00:00
If you like disable external config and remove warning, you should remove this line https://github.com/xmrig/xmrig/blob/master/src/base/kernel/Base.cpp#L109 but why embedded one not used I can't say, are you sure config valid?
Thank you.

## stinkefisch | 2019-08-30T12:46:29+00:00
No problems, just me.
Config was wrong
Thanks

# Action History
- Created by: stinkefisch | 2019-08-30T10:42:55+00:00
- Closed at: 2019-08-30T22:31:34+00:00
