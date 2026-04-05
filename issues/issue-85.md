---
title: Windows defender says xmrig.exe has a trojan
source_url: https://github.com/xmrig/xmrig/issues/85
author: trashhalo
assignees: []
labels:
- invalid
- av
created_at: '2017-09-02T23:04:39+00:00'
updated_at: '2021-09-22T17:09:53+00:00'
type: issue
status: closed
closed_at: '2017-09-06T13:54:07+00:00'
---

# Original Description
specifically Trojan:Win32/Tilken.B!cl

do you know whats up with that?

# Discussion History
## xmrig | 2017-09-03T02:00:34+00:00
What version? If you download it from github nothing worry about. It periodically happens to all miners without exception, some people put it to botnets, it makes AV companies angry.

Also Windows Defender very funny, some time ago it claims xmrig and xmr-stak-cpu as trojan with exactly same name. Also claim 32bit proxy (not a miner, but based on same codebase) version as a trojan only because it contains word Monero in description.

## theycallmepepper | 2017-10-07T04:23:06+00:00
Flagged as vigorf.a - xmrig-2.3.1-msvc-win64.zip

## versteckt | 2018-01-07T05:56:14+00:00
Flagged as "Trojan:Win32/Bluteal!rfn" for me.

And yes, this is because so many trojans use xmrig in their payload to stealth mine stuff like Monero. Just "allow" it in your AV so that it stop deleting your executable like it was for me, and you should be OK. :-)

## minorminer | 2021-09-22T17:09:52+00:00
Windows is blocking, and calling "Severe Threat" this script:  Trojan:Script/Wacatac.B!ml which came with the latest XMRig download (xmrig-6.15.1-gcc-win64) this morning. Any word on whether or not this is a concern or just Windows being over protective? Hesitant to make a move. 

# Action History
- Created by: trashhalo | 2017-09-02T23:04:39+00:00
- Closed at: 2017-09-06T13:54:07+00:00
