---
title: Cant read stdout
source_url: https://github.com/xmrig/xmrig/issues/200
author: OpNop
assignees: []
labels:
- bug
created_at: '2017-11-15T09:17:35+00:00'
updated_at: '2017-11-27T00:20:15+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:20:15+00:00'
---

# Original Description
Im trying to wrap your miner into an easy frontend but when trying to read the stdout I get nothing, I tried a a few things but I have never used libuv and could not figure out how to output to a standard stdout. I would also like to send commands via stdin but have not be able to test that yet but I assume the same issue will happen and I wont have access to it.

Thanks 

# Discussion History
## xmrig | 2017-11-17T09:43:12+00:00
If you can compile from source try change this function https://github.com/xmrig/xmrig/blob/master/src/log/ConsoleLog.cpp#L134 to always return `true`.

If it helps I need to know what value returning `uv_guess_handle(1)`.
Thank you.

## OpNop | 2017-11-18T03:40:34+00:00
Did your change, but it did not work. When I would redirect stdout using xmrig.exe > test.txt or using process.StartInfo.RedirectStandardOutput = true; in C# the application would instant exit without any message. However with that set to true and also changing https://github.com/xmrig/xmrig/blob/master/src/log/ConsoleLog.cpp#L152 to 

```
fprintf(stdout, m_buf);
fflush(stdout);
```
does work both in standard and piped stdout modes. This works for my application but would assume not a good solution to push back into the repo but might give you some insight as to where to properly fix it.

Thanks

## xmrig | 2017-11-18T11:10:37+00:00
I added fprintf failback mode.
`uv_tty_init` return error, so`m_stream` never assigned, so simple override `isWritable` was cause crash.

# Action History
- Created by: OpNop | 2017-11-15T09:17:35+00:00
- Closed at: 2017-11-27T00:20:15+00:00
