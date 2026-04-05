---
title: DNS error unknown node or service
source_url: https://github.com/xmrig/xmrig/issues/2631
author: Hussainm39
assignees: []
labels: []
created_at: '2021-10-15T08:02:09+00:00'
updated_at: '2021-10-16T01:21:25+00:00'
type: issue
status: closed
closed_at: '2021-10-15T08:55:48+00:00'
---

# Original Description
Hello every one can some one help me out I am mining on unmineable app and from yesterday when I want to do mining on cpu it’s say DNS error unknown node or service ,  also before this it’s say Opencl Disabled. But gpu mining working but the app giving me to low MH 
Thanks in advance

# Discussion History
## Spudz76 | 2021-10-15T08:48:08+00:00
If you have nvidia GPU then OpenCL disabled / CUDA enabled is normal?

It might just be mining on the CPU?  Unclear without screenshots of xmrig.  Any other unmineable specific issues should be directed to unmineable support (the unmineable-app github has no "Issues" section, so I guess their main support site is the way).

Some ISPs and/or Internet Security Apps are filtering DNS for known mining pools.

## Hussainm39 | 2021-10-15T08:52:53+00:00
![7F250E41-B3E7-4635-AF07-068EA93D0EAA](https://user-images.githubusercontent.com/92572107/137460492-5525fb0a-650b-41c1-9143-804868a0ec9b.jpeg)
![Uploading AFE7FB2B-7018-43F3-A0E4-A0D67B4486B3.jpeg…]()


## Hussainm39 | 2021-10-15T08:53:43+00:00
![A9253C91-D7CB-4B28-AAA0-604EA4E7849B](https://user-images.githubusercontent.com/92572107/137460636-97be223d-a7bd-4a7c-a3b2-8a1bcdf23bb0.jpeg)


## Hussainm39 | 2021-10-15T08:55:48+00:00
![7F250E41-B3E7-4635-AF07-068EA93D0EAA](https://user-images.githubusercontent.com/92572107/137460492-5525fb0a-650b-41c1-9143-804868a0ec9b.jpeg)
![Uploading AFE7FB2B-7018-43F3-A0E4-A0D67B4486B3.jpeg…]()


## Hussainm39 | 2021-10-15T08:56:33+00:00
I tried every think also xmrig website has some issues because it’s not opening 

## Spudz76 | 2021-10-16T01:21:25+00:00
Then something or ISP is filtering DNS for known mining sites.

Switch DNS servers to a public one (not the one your ISP gives you) or investigate new/updated security software and add exceptions/whitelist.

# Action History
- Created by: Hussainm39 | 2021-10-15T08:02:09+00:00
- Closed at: 2021-10-15T08:55:48+00:00
