---
title: CN-Heavy-Italo
source_url: https://github.com/xmrig/xmrig/issues/714
author: swa74
assignees: []
labels:
- wontfix
created_at: '2018-07-06T09:11:16+00:00'
updated_at: '2018-07-11T19:17:58+00:00'
type: issue
status: closed
closed_at: '2018-07-11T19:17:58+00:00'
---

# Original Description
There will be a new CN-Heavy-Italo ?

# Discussion History
## xmrig | 2018-07-06T10:12:17+00:00
Any information about this algorithm?
Thank you.

## swa74 | 2018-07-06T10:13:13+00:00
https://github.com/italocoin-project/xmrig

## xmrig | 2018-07-06T10:49:15+00:00
Looks like It should work already as `cn-heavy/xhv`.
```json
{
  "algo": "cryptonight-heavy",
  ...
  "pools": [
        {
            "url": "...",
            ...
            "variant": "xhv"
        }
  ]
}
```

## swa74 | 2018-07-06T10:59:21+00:00
![default](https://user-images.githubusercontent.com/34404806/42375628-c5c3166c-8124-11e8-8eae-c492f491b93b.JPG)
![1](https://user-images.githubusercontent.com/34404806/42375629-c5decf10-8124-11e8-888a-bd20ae1b6025.JPG)


## xmrig | 2018-07-06T11:03:20+00:00
nvidia miner not support variant `xhv` yet.

## swa74 | 2018-07-06T11:11:46+00:00
![2](https://user-images.githubusercontent.com/34404806/42376073-8335e8ea-8126-11e8-9135-a541adf32caf.JPG)


## xmrig | 2018-07-06T11:19:49+00:00
You should use v2.6.3 also is they already forked?

## swa74 | 2018-07-06T11:25:28+00:00
![3](https://user-images.githubusercontent.com/34404806/42376612-6c9b11bc-8128-11e8-99d9-ea05d4be4220.JPG)


## swa74 | 2018-07-06T11:26:33+00:00
Thank you when will work nVidia

## italocoin-project | 2018-07-06T13:46:54+00:00
Hello,

the difference between italo and xhv is this

XHV has `idx0 = (~d) ^ q` and italo has `idx0 = ~(d ^ q)` could you please add it?

Regards.

## xmrig | 2018-07-06T13:57:25+00:00
Okay, look at this line https://github.com/italocoin-project/xmrig/commit/c2c0c7c5ba2bff012c981c5b78cf89ec25ed61ee#diff-b279619f2bf01fd93a78050a584f96eeL177 in your fork, reference hashes are equal to `cn-heavy/xhv`.
Thank you.

## italocoin-project | 2018-07-06T14:01:55+00:00
Those must be remade, i haven't touched them, you think you can add heavy/ITA?

## xmrig | 2018-07-06T14:14:33+00:00
`idx0 = (~d) ^ q` equal to `idx0 = ~(d ^ q)`, so `cn-heavy/ita` not exists, self test additionally confirm it.

## italocoin-project | 2018-07-06T14:22:42+00:00
U sure bro? "self test" i didn't changed the self test, try to make a self test

## xmrig | 2018-07-06T14:33:09+00:00
Yep, if algorithm really changed miner threads won't start and you will see red error messages like
`thread 0 error: "hash self-test failed".`

## italocoin-project | 2018-07-06T15:17:35+00:00
Thank you for letting me know :) Really apreciate it

# Action History
- Created by: swa74 | 2018-07-06T09:11:16+00:00
- Closed at: 2018-07-11T19:17:58+00:00
