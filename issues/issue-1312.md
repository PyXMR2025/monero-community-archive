---
title: Converting DLL
source_url: https://github.com/xmrig/xmrig/issues/1312
author: yesilcimenahmet
assignees: []
labels: []
created_at: '2019-11-25T08:24:52+00:00'
updated_at: '2021-04-12T15:28:40+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:28:40+00:00'
---

# Original Description
Hi. I compiled the XMRig project as a DLL to directly control it. Before this, I removed some parts by making some changes related to background, color support and signal, and developed a few exported DLL functions (start, stop, pause, resume, setarguments, callback, etc.). The application works fine.
The App.exec () function creates a loop with the UV library and blocks the Main Thread. This is necessary for Miner to work. I could not find the main loop function to remove it. I think there are some cyclic operations with the Timer, which organizes other Thread operations. Correct me if I'm wrong. Therefore, after loading the DLL and starting the miner, I cannot perform a process on the main form because the Main Thread is blocked. In order to solve this problem, I create a new thread from the external application that I developed and run the miner through this thread. This way the Main Thread is not blocked.
Since I don't have any experience or knowledge about the UV library, I'm concerned about whether the UV library is thread-safe outside the Main Thread. For example: In Windows, this can be a problem if Timer creates a ghost Windows to manage its operations with Windows messages. I did tests for about 1 day and I didn't have any problems. What's your opinion on this?

Thanks.

Image: [https://prnt.sc/q1mw85](url)

# Discussion History
# Action History
- Created by: yesilcimenahmet | 2019-11-25T08:24:52+00:00
- Closed at: 2021-04-12T15:28:40+00:00
