---
title: Help need with xmrig and minemonero.pro
source_url: https://github.com/xmrig/xmrig/issues/140
author: petervalencic
assignees: []
labels: []
created_at: '2017-10-06T14:48:45+00:00'
updated_at: '2017-10-22T05:24:00+00:00'
type: issue
status: closed
closed_at: '2017-10-22T05:24:00+00:00'
---

# Original Description
Hi,
have setup monero wallet and modified xmrig config.json file..

have setup like this:
 "url": "pool.minemonero.pro:5555",
            "user": "43kwC3YXzj42qdT1uoGbS97TUqbNE43r5jnPFnJ4cwGjZa4U9G5mCL2VEbJywoSw62RFqbt9hiAwLQsGzAFAvQkcSykCn6N",
            "pass": "xxxx",

When I like to sign into minemonero.pro with user and pass I get error: please check your login..

Can someone tell me what I'am doing wrong? 

# Discussion History
## MineMoneroPRO | 2017-10-06T14:52:34+00:00
Hi!
You should set your password in xmrig like "worker_id:password".
In this case the password from web interface would be just "password".
Please note that you can set the password as an email (eg. "worker_id:email@email.com") and you will be receiving email notifications in this case.

# Action History
- Created by: petervalencic | 2017-10-06T14:48:45+00:00
- Closed at: 2017-10-22T05:24:00+00:00
