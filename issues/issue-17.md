---
title: New hasharate logging creates extra line after getting 15m avg value
source_url: https://github.com/xmrig/xmrig/issues/17
author: YetAnotherRussian
assignees: []
labels: []
created_at: '2017-06-19T11:19:33+00:00'
updated_at: '2017-06-29T22:42:05+00:00'
type: issue
status: closed
closed_at: '2017-06-29T22:42:05+00:00'
---

# Original Description
![xmrig1](https://user-images.githubusercontent.com/4670472/27282777-1cfe3162-54fa-11e7-9beb-c75753dcee87.png)

When 15m avg speed is calculated, console output creates extra line with 1 symbol. Write new line or reduce string length for output. Win7 x64.


# Discussion History
## xmrig | 2017-06-19T11:38:26+00:00
Ok thanks, on Windows 10 default size of console bigger and I forgot about older systems.

## xmrig | 2017-06-19T21:58:09+00:00
I just simple rename `highest` to `max`.

# Action History
- Created by: YetAnotherRussian | 2017-06-19T11:19:33+00:00
- Closed at: 2017-06-29T22:42:05+00:00
