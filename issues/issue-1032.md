---
title: '32 bit linux mint '
source_url: https://github.com/xmrig/xmrig/issues/1032
author: SilentSeir
assignees: []
labels:
- libuv
created_at: '2019-06-11T19:10:42+00:00'
updated_at: '2019-08-02T11:48:21+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:48:21+00:00'
---

# Original Description
libuv1-dev

 $ sudo apt-get install libuv1-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package libuv1-dev

Also : 

xmrig-2.15.4-beta $ ./xmrig
bash: ./xmrig: cannot execute binary file: Exec format error

#NIM


# Discussion History
## Spudz76 | 2019-06-15T17:05:00+00:00
How old is this Mint, that it doesn't have libuv1?
Tessa works fine, Tara should also work, although not sure about 32-bit I would never personally bother trying that.  Is your CPU 64-bit capable?

Probably older you'll end up building your own libuv1 (older came with libuv0.10 or worse)
Same sort of issues as you'd hit with old Ubuntu before 16.
It does work on Ubuntu 14 but only if the newer dependencies are manually compiled from source.

As Mint is a modification of Ubuntu, you should also search for solutions that apply to the Ubuntu version (check sources.list for which Ubuntu codename the Mint is based from)

# Action History
- Created by: SilentSeir | 2019-06-11T19:10:42+00:00
- Closed at: 2019-08-02T11:48:21+00:00
