---
title: master fails to compile
source_url: https://github.com/monero-project/monero/issues/901
author: schnerchi
assignees: []
labels: []
created_at: '2016-07-10T14:47:16+00:00'
updated_at: '2016-07-12T08:29:34+00:00'
type: issue
status: closed
closed_at: '2016-07-12T08:29:34+00:00'
---

# Original Description
Am I the only one that can not compile git master? compiling tag v0.9.4 works.....


# Discussion History
## schnerchi | 2016-07-10T14:47:46+00:00
system : ubuntu 16.04 and mac osx 10.11.5


## moneromooo-monero | 2016-07-10T15:52:53+00:00
At the risk of sounding obvious, a mention of the error would help.


## moneromooo-monero | 2016-07-10T15:53:49+00:00
If it's something to do with an operator /= in boost, this got fixed yesterday.


## schnerchi | 2016-07-10T17:18:58+00:00
sure, I was just wondering. Last time master would not compile it was "well" known...

info : http://pastebin.com/JiHc2V1E
error : http://pastebin.com/wW91MsC1


## radfish | 2016-07-10T17:32:14+00:00
Duplicate of #871. There is a patch described there, you can try applying it.


## schnerchi | 2016-07-12T08:29:34+00:00
pull #904 solves this issue. thanks!


# Action History
- Created by: schnerchi | 2016-07-10T14:47:16+00:00
- Closed at: 2016-07-12T08:29:34+00:00
