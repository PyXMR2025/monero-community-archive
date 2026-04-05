---
title: old glibc compatibility
source_url: https://github.com/xmrig/xmrig/issues/70
author: ghost
assignees: []
labels: []
created_at: '2017-08-22T21:40:26+00:00'
updated_at: '2017-09-07T01:15:46+00:00'
type: issue
status: closed
closed_at: '2017-09-04T00:36:43+00:00'
---

# Original Description
Can it be compiled for old glibc 2.5 ?

I download compiled file from releases and got this error:

```
./xmrig: /lib64/libc.so.6: version `GLIBC_2.6' not found (required by ./xmrig)
./xmrig: /lib64/libc.so.6: version `GLIBC_2.14' not found (required by ./xmrig)
./xmrig: /lib64/libc.so.6: version `GLIBC_2.7' not found (required by ./xmrig)
./xmrig: /lib64/libc.so.6: version `GLIBC_2.17' not found (required by ./xmrig)
```

# Discussion History
## xmrig | 2017-08-23T08:48:32+00:00
Probable yes, until you can install gcc 4.9+ and libuv1 on this system, if that requirements satificated, you can build binary.
Thank you.

## ghost | 2017-08-23T19:11:22+00:00
Thanks for your answer. I try to do this...

## ghost | 2017-08-27T09:28:25+00:00
@xc85  just wondering if you've succeeded to compile for old glibc? 

# Action History
- Created by: ghost | 2017-08-22T21:40:26+00:00
- Closed at: 2017-09-04T00:36:43+00:00
