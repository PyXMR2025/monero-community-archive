---
title: 'Syntax error: "(" unexpected'
source_url: https://github.com/xmrig/xmrig/issues/2206
author: jonz113
assignees: []
labels:
- question
created_at: '2021-03-25T01:07:42+00:00'
updated_at: '2021-04-12T13:49:18+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:49:18+00:00'
---

# Original Description
Hi All, I'm a total novice and trying to learn so I can demonstrate in a college class.  I have Ubuntu 20.04 on a Odroid C4 and I downloaded xmrig-6.10.0-focal-x64.tar.gz.  I am recieving the below message in terminal

odroid@odroid:~/Desktop/xmrig-6.10.0$ sudo ./xmrig
[sudo] password for odroid: 
./xmrig: 1: Syntax error: "(" unexpected
odroid@odroid:~/Desktop/xmrig-6.10.0$

Any help is greatly appreciated.  Thanks!

# Discussion History
## SChernykh | 2021-03-25T07:44:18+00:00
> xmrig-6.10.0-focal-x64.tar.gz

This is for x86 CPUs, not for ARM. You have to download source code and compile it yourself: https://xmrig.com/docs/miner/build

# Action History
- Created by: jonz113 | 2021-03-25T01:07:42+00:00
- Closed at: 2021-04-12T13:49:18+00:00
