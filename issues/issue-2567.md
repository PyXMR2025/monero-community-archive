---
title: Writing to the stdin from another process to pause xmrig does not work
source_url: https://github.com/xmrig/xmrig/issues/2567
author: j-hc
assignees: []
labels: []
created_at: '2021-08-29T17:53:09+00:00'
updated_at: '2021-10-18T18:18:20+00:00'
type: issue
status: closed
closed_at: '2021-10-18T18:18:19+00:00'
---

# Original Description
As we are able press p to pause mining on the console i though i could simulate the same behaviour by writing "p" into the stdin of the process but it does not work. 
Here is my code (i am doing this in rust so..):

```
let p = Command::new("xmrig.exe")
            .args([***])
            .stdin(Stdio::piped())
            .spawn().unwrap()
    }
let mut pstdin = p.stdin.as_mut().unwrap();
    pstdin.write(b"p").unwrap();
    pstdin.flush();
```

I am not sure if this is a bug but still..
I can get the raw handle to the process in rust so if anyone have the working code in some other language like cpp i would like to see it.

# Discussion History
## Spudz76 | 2021-08-30T00:58:02+00:00
Input is handled by `libuv` as a `uv_tty` and is handled as a real console, which may be what breaks piping.

It's expecting actual keypresses, not a stream of input.

There may be some way to (ab)use libuv tty to be able to pipe into it (more like a dummy keyboard that accepts a pipe?).  But I couldn't find a workaround in several seconds of searching and gave up.  YMMV

## j-hc | 2021-08-30T10:54:44+00:00
Well thanks for the explanation. I will just use the local http api to pause/resume as a workaround for now unless there is away to accomplish that.

## j-hc | 2021-10-18T18:18:19+00:00
I worked-around this using `PostMessageW`  :)

# Action History
- Created by: j-hc | 2021-08-29T17:53:09+00:00
- Closed at: 2021-10-18T18:18:19+00:00
