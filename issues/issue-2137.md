---
title: I want to use my raspberry pi but can not build success
source_url: https://github.com/xmrig/xmrig/issues/2137
author: GouMingAnKang
assignees: []
labels: []
created_at: '2021-02-27T05:12:18+00:00'
updated_at: '2021-04-12T14:09:17+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:09:17+00:00'
---

# Original Description
## Device
Raspberry Pi 4B
## OS
Cent OS 8 stream
## Matters
Some packages cant be found before i build
Do you consider publish a linux-arm64 version?


# Discussion History
## ghost | 2021-03-01T11:22:58+00:00
follow this guide [https://blog.ijasoneverett.com/2020/08/cpu-mining-on-a-raspberry-pi/](url) that is what i did to get it on my pi

## grahamreeds | 2021-03-22T13:06:34+00:00
I had it working a while back with just raspberry os, no dspawn needed.

However something has changed and the latest version no longer compiles on Pi4.

I suspect the sse2neon update Tobe the culprit.

# Action History
- Created by: GouMingAnKang | 2021-02-27T05:12:18+00:00
- Closed at: 2021-04-12T14:09:17+00:00
