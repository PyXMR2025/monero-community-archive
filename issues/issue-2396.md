---
title: Is this made to be imported as a library to be integrated into code?
source_url: https://github.com/xmrig/xmrig/issues/2396
author: Joe23232
assignees: []
labels: []
created_at: '2021-05-20T13:03:04+00:00'
updated_at: '2021-05-24T10:27:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, I am considering to use xmrig's libraries into my own code.

I wanted to ask is xmrig designed to be imported into anyone's elses code?

I know that it is open source so it is 100% possible, however how "user friendly" is it to import it as a library into my own code?

# Discussion History
## Spudz76 | 2021-05-20T20:41:39+00:00
Wrap all input and output and configuration with DLL exports.  Or run it as child process and use existing API bound to strange localnet IP (127.6.9.69 or such).

## Joe23232 | 2021-05-24T10:27:35+00:00
I wanted to put it into my own software all into a single executable without needing dlls.

So how user friendly is it to import the code as a library into my own code? Is it made for such purposes?

# Action History
- Created by: Joe23232 | 2021-05-20T13:03:04+00:00
