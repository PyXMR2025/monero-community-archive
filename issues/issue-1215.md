---
title: 'dataset.hpp(61): error C2338: randomx_cache must be a standard-layout struct'
source_url: https://github.com/xmrig/xmrig/issues/1215
author: xmska
assignees: []
labels:
- question
created_at: '2019-10-02T20:08:51+00:00'
updated_at: '2020-04-06T15:17:08+00:00'
type: issue
status: closed
closed_at: '2019-10-08T03:15:25+00:00'
---

# Original Description
I am unable to compile in visual studio 2017

> dataset.hpp(61): error C2338: randomx_cache must be a standard-layout struct

But it will compile in MSYS2 MinGW.
How can I compile this corectly in visual studio?

# Discussion History
## xmrig | 2019-10-02T20:46:54+00:00
Use release build or remove this check.
Thank you.

## xmska | 2019-10-02T21:05:35+00:00
Could you explain what that is and why it does not work in debugging mode? Is it gonna work properly in debug mode with this check removed?

## SChernykh | 2019-10-03T14:55:03+00:00
It doesn't work in debug in Visual Studio. Removing the check will make it compile, but it will crash when trying to mine RandomX.

## xmska | 2019-10-06T21:51:28+00:00
Under what circumstances does it crash? I let it mine LOKI in debug and it worked without crashing.

## xmrig | 2019-10-08T03:15:24+00:00
This check should be unnecessary since RandomX code embedded into miner and don't need to be strictly compatible with C (unlike official library), but if you need debug build it means you known what you do and all possible crashes is your responsibility.
Thank you.


# Action History
- Created by: xmska | 2019-10-02T20:08:51+00:00
- Closed at: 2019-10-08T03:15:25+00:00
