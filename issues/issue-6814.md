---
title: how to debug monero on Win7?
source_url: https://github.com/monero-project/monero/issues/6814
author: jiebanghan
assignees: []
labels: []
created_at: '2020-09-10T00:58:45+00:00'
updated_at: '2020-10-15T22:36:49+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:36:49+00:00'
---

# Original Description
My aim is to learn the codes of monero so I build monero in MSYS2 on Win7. And my aim is also debug it and set some breakpoints and so on in order to trace the codes of monero.But I am not ready to use gdb because I like GUI mode to debug. So how to meet my conditions with some GUI IDE? Thank you very much with all my heart.
By the way , why compile monero in msys2 so slowly? It almost consume 1 hours  or more to make.

# Discussion History
## selsta | 2020-09-10T01:08:22+00:00
Look into CLion

## jiebanghan | 2020-09-10T07:19:18+00:00
thank you @selsta 

## sanderfoobar | 2020-09-14T12:20:27+00:00
`-DCMAKE_RELEASE_TYPE=Debug` will include debugging symbols and whatnot, so you can use a debugger and step through the code.

CLion is nice because it picks up on your `CMakeLists.txt` contents and parses the various targets - which you can compile in debug mode and debug with the integrated debugger.

Lastly, I recommend ditching Windows for this type of task. The process outlined above is easier on Linux.

## jiebanghan | 2020-09-15T09:42:44+00:00
OK,  thank you @xmrdsc 

# Action History
- Created by: jiebanghan | 2020-09-10T00:58:45+00:00
- Closed at: 2020-10-15T22:36:49+00:00
