---
title: GetLargePageMinimum is not supported by Windows XP
source_url: https://github.com/xmrig/xmrig/issues/1314
author: peredozo
assignees: []
labels: []
created_at: '2019-11-25T22:14:00+00:00'
updated_at: '2021-04-12T19:24:15+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:28:31+00:00'
---

# Original Description
Fast slove

src\crypto\common\VirtualMemory_win.cpp (167):

`#if defined(_WIN64)`
`    const size_t min = GetLargePageMinimum();`
`#else`
`    const size_t min = 0;`
`#endif`

Maybe it have a more correct way?

# Discussion History
## lilyanatia | 2019-12-02T21:26:08+00:00
> Maybe it have a more correct way?

there is no more correct way. Windows XP has been EOL for more than half a decade.

## peredozo | 2019-12-03T10:47:22+00:00
> Windows XP has been EOL for more than half a decade.

Like a 32-bit apps. But they still exist.

## lilyanatia | 2019-12-03T14:22:33+00:00
most 32-bit apps don't have severe security vulnerabilities that have been known and not fixed for 5 years.

# Action History
- Created by: peredozo | 2019-11-25T22:14:00+00:00
- Closed at: 2021-04-12T15:28:31+00:00
