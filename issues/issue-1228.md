---
title: (Error) Unable to set affinity. Windows supports only affinity up to 63
source_url: https://github.com/xmrig/xmrig/issues/1228
author: ghost
assignees: []
labels: []
created_at: '2019-10-09T04:02:41+00:00'
updated_at: '2019-12-22T19:35:22+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:35:22+00:00'
---

# Original Description
I have 72 CPUs how to use them all.

Image
<img src="https://i.imgur.com/mStXohD.jpg" />

# Discussion History
## Spudz76 | 2019-11-03T21:28:21+00:00
Windows decided to be dumb and requires a large pile of additional code to support more than 64 cores.  There are no miners I know of that bothered to support the silly ProcessorGroup stuff.  Most of those people just install Linux which handles hundreds of cores properly without any additional system calls or tracking which process is in which virtual group.

[https://docs.microsoft.com/en-us/windows/win32/procthread/processor-groups](https://docs.microsoft.com/en-us/windows/win32/procthread/processor-groups)

Sometimes Windows will force Processor Groups even with less than 64 cores, depending on the layout of the motherboard (dual CPU etc), which is even more annoying.

## xmrig | 2019-12-22T19:35:22+00:00
Recent versions correctly supports affinity above 63.
Thank you.

# Action History
- Created by: ghost | 2019-10-09T04:02:41+00:00
- Closed at: 2019-12-22T19:35:22+00:00
