---
title: 'tcsetattr: 无效的参数'
source_url: https://github.com/xmrig/xmrig/issues/372
author: blacksirt
assignees: []
labels:
- bug
- libuv
created_at: '2018-01-29T06:36:08+00:00'
updated_at: '2018-11-05T07:10:11+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:10:11+00:00'
---

# Original Description
hello,when i run xmrig in linux,the console echo "tcsetattr: 无效的参数",how to resolv it?

# Discussion History
## Gill1000 | 2018-01-30T12:14:19+00:00
Thats strange.....i never received that....which is your linux distro..??

## blacksirt | 2018-01-31T03:05:41+00:00
SUSE Linux Enterprise Server 11
linux-kajs 2.6.27.19-5-default

## xmrig | 2018-01-31T08:44:36+00:00
What libuv version did you use? Propably some terminal/ssh related issue. Try remove this line https://github.com/xmrig/xmrig/blob/master/src/Console.cpp#L39
Thank you.

## blacksirt | 2018-02-04T06:11:10+00:00
thank you.
i don't know.... when i remove this: https://github.com/xmrig/xmrig/blob/master/src/Console.cpp#L39,in the begin it's ok,few minutes later still the same problom..............is there other place to modify?

## Bravoyk | 2018-07-16T16:24:37+00:00
@blacksirt hey, Can u tell me how to install this program with “SUSE Linux Enterprise Server 11” .

# Action History
- Created by: blacksirt | 2018-01-29T06:36:08+00:00
- Closed at: 2018-11-05T07:10:11+00:00
