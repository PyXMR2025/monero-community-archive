---
title: Settings for bytecoin
source_url: https://github.com/xmrig/xmrig/issues/723
author: Sveeeeeen
assignees: []
labels:
- question
created_at: '2018-07-24T16:45:25+00:00'
updated_at: '2018-10-10T22:20:21+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:20:21+00:00'
---

# Original Description
Since I upgraded to the very current version I just receive only "Low difficulty share" errors.
Whats the problem with it? 

# Discussion History
## Sveeeeeen | 2018-08-05T14:13:32+00:00
Push

## xmrig | 2018-08-05T14:33:07+00:00
As I know Bytecoin still use original cryptonight, so key options:
```json
{
  "algo": "cryptonight",
  ...
  "pools": [
    {
      "url": "...",
      "variant": 0,
      ...
    }
 ],
 ...
}
```

## Sveeeeeen | 2018-08-05T15:24:28+00:00
I receive only "Low difficulty share" after upgrading to the current version. Older version "XMRig/2.6.0-beta2" in my case is working fine with the same config.

## xmrig | 2018-08-05T15:56:29+00:00
You must set `"variant": 0` for newer versions, default variant changed from `0` to `1`.
Thank you.

# Action History
- Created by: Sveeeeeen | 2018-07-24T16:45:25+00:00
- Closed at: 2018-10-10T22:20:21+00:00
