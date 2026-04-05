---
title: Support nicehash
source_url: https://github.com/xmrig/xmrig/issues/144
author: Jh0nW1cK
assignees: []
labels:
- question
created_at: '2017-10-09T02:44:19+00:00'
updated_at: '2017-10-09T16:12:33+00:00'
type: issue
status: closed
closed_at: '2017-10-09T16:12:33+00:00'
---

# Original Description
Good morning, 
What is the function of --nicehash?
Thank you

# Discussion History
## xmrig | 2017-10-09T10:27:46+00:00
This option explicitly enables [nicehash.com](https://www.nicehash.com) and [xmrig-proxy](https://github.com/xmrig/xmrig-proxy) support. Nicehash has small difference in protocol, just one byte, but it required special handle of it.
Thank you.

https://github.com/nicehash/Specifications/blob/master/NiceHash_CryptoNight_modification_v1.0.txt

## Jh0nW1cK | 2017-10-09T16:00:54+00:00
This is hard to understand for me. I use xmrig.exe with config.json by default on several computers located in different locations. 
Would it be nice to use the --nicehash function for me? 
Thank you

## xmrig | 2017-10-09T16:08:19+00:00
If you use the miner with nicehash.com or xmrig-proxy you must add this option. In all other cases it not need.

## Jh0nW1cK | 2017-10-09T16:12:25+00:00
Thank you very much.

# Action History
- Created by: Jh0nW1cK | 2017-10-09T02:44:19+00:00
- Closed at: 2017-10-09T16:12:33+00:00
