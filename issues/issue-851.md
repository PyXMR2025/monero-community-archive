---
title: 'hardcode '
source_url: https://github.com/xmrig/xmrig/issues/851
author: M0x65
assignees: []
labels:
- question
created_at: '2018-10-26T23:59:50+00:00'
updated_at: '2018-11-05T06:55:26+00:00'
type: issue
status: closed
closed_at: '2018-11-05T06:55:26+00:00'
---

# Original Description
Hello is it possible to hardcode and pool / xmr address in xmrig ? 

# Discussion History
## snipeTR | 2018-10-27T10:38:44+00:00
src/common/config/CommonConfig.cpp

    m_pools.push_back(Pool());
"Poolurl.com",12345,"username","pw"

## M0x65 | 2018-10-27T14:45:21+00:00
in that format?

## mrleduck | 2018-10-27T19:55:47+00:00
Yes i would also like to know how to hardcode my pool and addres into the code. just nobody can mess with it even if they mean it as a joke.
i just want it so it only runs to the pool i put in the src any help?

## snipeTR | 2018-10-27T22:16:11+00:00
m_pools.push_back(Pool("Poolurl.com", 12345, "username", "pw"));
tip: you are noob

## mrleduck | 2018-10-27T22:19:08+00:00
So its fixed? And even if someone runs a command line with different config would it still be the same?

## snipeTR | 2018-10-27T22:28:40+00:00
no first json


## mrleduck | 2018-10-27T22:34:42+00:00
i have never messed or even close looked into the source. could you please explain this noob what u mean and what to change to get a fixed pool?

# Action History
- Created by: M0x65 | 2018-10-26T23:59:50+00:00
- Closed at: 2018-11-05T06:55:26+00:00
