---
title: Libuv library dependency
source_url: https://github.com/xmrig/xmrig/issues/117
author: erotavlasme
assignees: []
labels: []
created_at: '2017-09-19T07:43:31+00:00'
updated_at: '2017-10-02T11:52:23+00:00'
type: issue
status: closed
closed_at: '2017-10-02T11:52:23+00:00'
---

# Original Description
Hi,
I know that xmrig requires libuv library in order to be built. I successfully compiled libuv with msys2 and autotools and with standard method with MSVC compiler as suggested by the maintainers [here](https://github.com/libuv/libuv).
However, in both cases I get some errors during the make check/test phase as I reported [here](https://github.com/libuv/libuv/issues/1549). 
I do not know if I have to care about such errors. What method do you use?
Thank you

# Discussion History
## NmxMilk | 2017-09-23T19:38:33+00:00
Well, if you run xmrig and get good results you can !
It is though good reflex to have signaled your problems to the libuv dev team.


# Action History
- Created by: erotavlasme | 2017-09-19T07:43:31+00:00
- Closed at: 2017-10-02T11:52:23+00:00
