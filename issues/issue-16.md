---
title: gcc-win64 compile gives hasrate drop
source_url: https://github.com/xmrig/xmrig/issues/16
author: YetAnotherRussian
assignees: []
labels: []
created_at: '2017-06-19T10:56:09+00:00'
updated_at: '2017-07-19T23:58:50+00:00'
type: issue
status: closed
closed_at: '2017-07-19T23:58:50+00:00'
---

# Original Description
Hi, just to inform that gcc-win64 compile gives hasrate drop when compared to msvc version.

As for numbers, it's 774H/s vs 749H/s on stock i5-4570 CPU for cryptonight-light (3 double threads). It's win7 x64 system.

So I guess it's no point to compile x64 binary using gcc, and maybe you should try msvc for x32 as well.

# Discussion History
## xmrig | 2017-06-19T11:09:07+00:00
You right, for x64 msvc version faster than gcc, according my tests too.

But for x32 situation is different, msvc version 10% slower than gcc.

## YetAnotherRussian | 2017-06-19T11:22:09+00:00
Hmm, OK then :) I guess I shouldn't test x32 version on x64 system.

# Action History
- Created by: YetAnotherRussian | 2017-06-19T10:56:09+00:00
- Closed at: 2017-07-19T23:58:50+00:00
