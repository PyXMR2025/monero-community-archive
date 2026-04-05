---
title: incompatible/disabled algorithm "cn/0" detected
source_url: https://github.com/xmrig/xmrig/issues/1667
author: imrecsoka
assignees: []
labels: []
created_at: '2020-05-03T03:58:27+00:00'
updated_at: '2020-08-29T04:34:29+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:34:29+00:00'
---

# Original Description
I am trying to mine against a pool , the Algorithm Masari.
So i am using 
-a cn as the algo in the command line :

I keep getting this error:
incompatible/disabled algorithm "cn/0" detected

I have tried XM-Rig 5.5 and 5.11 i dont know what the hell i am doing wrong here.

I tried -a half-fast and i tried to use --variant msr

I can successfully mine Loki and Monero though as a test.
However i would like to test other algorithms to i can contribute to speed stats .

Thank you

# Discussion History
## SChernykh | 2020-05-03T17:32:25+00:00
The algorithm for Masari is called `cn/half`

# Action History
- Created by: imrecsoka | 2020-05-03T03:58:27+00:00
- Closed at: 2020-08-29T04:34:29+00:00
