---
title: no share accepting after build from source
source_url: https://github.com/xmrig/xmrig/issues/162
author: serkanyalcin21
assignees: []
labels:
- libuv
created_at: '2017-10-20T22:40:03+00:00'
updated_at: '2018-03-14T23:20:11+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:20:11+00:00'
---

# Original Description
Hi, i installed msys2 and all other dependencies. 
The original xmrig application works well with nanopool but after building from source outputs couldn"t send shares. 
Also when i run the output file it gives dll missing errors so i copied dll files to main folder to work. 

Running about 2 hours but no share accept
![no share accept](https://user-images.githubusercontent.com/32970179/31844305-7e107764-b600-11e7-957b-9efea034da2a.jpg)

It doesent work if i remove dll files 
![folder](https://user-images.githubusercontent.com/32970179/31844304-7dfb7d6e-b600-11e7-8aee-2d589a97e8fd.jpg)


# Discussion History
## xmrig | 2017-10-22T05:02:36+00:00
Probably libuv related issue, don't place libuv.a in msys2 dir, no `make install` or use pacman to install it.
Nanopool use very high diff, with 15 H/s 2 hours without shares it ok.
Thank you.

# Action History
- Created by: serkanyalcin21 | 2017-10-20T22:40:03+00:00
- Closed at: 2018-03-14T23:20:11+00:00
