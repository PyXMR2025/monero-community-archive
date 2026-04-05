---
title: How to end uv_run() once and for all?
source_url: https://github.com/xmrig/xmrig/issues/754
author: sentinel-dll
assignees: []
labels:
- invalid
created_at: '2018-09-16T23:52:26+00:00'
updated_at: '2018-09-22T06:07:30+00:00'
type: issue
status: closed
closed_at: '2018-09-22T06:07:30+00:00'
---

# Original Description
![xmrig_exit](https://user-images.githubusercontent.com/43325629/45602225-b5e87480-b9f0-11e8-9b22-150d15c18ef8.PNG)

I have a code in which I use xmrig as .dll.
One problem I have is not being able to get the 'uv_run' return from this using the stop code, how much I use 'uv_loop_close (uv_default_loop ())' it kills my executable is this is a problem.

Please, how can I finalize 'uv_run' to get its feedback and continue the execution flow?


# Discussion History
# Action History
- Created by: sentinel-dll | 2018-09-16T23:52:26+00:00
- Closed at: 2018-09-22T06:07:30+00:00
