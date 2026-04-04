---
title: CLI prompt showing password in clear
source_url: https://github.com/monero-project/monero/issues/6292
author: dalecooper
assignees: []
labels: []
created_at: '2020-01-12T19:10:22+00:00'
updated_at: '2022-04-08T16:39:20+00:00'
type: issue
status: closed
closed_at: '2022-04-08T16:39:20+00:00'
---

# Original Description
Using latest version 0.15.0.1. (Edit : on Ubuntu 18.04)
After the CLI wallet was locked, the prompt showed the password in clear while typing.
I'm not a big CLI user so this happened only twice so far, but I thought it's worth reporting this issue.
Not sure if a screenshot is useful, but here's one below anyway.

![image](https://user-images.githubusercontent.com/16813929/72224145-2e286100-3577-11ea-9f1c-2ad5f143a2c6.png)


# Discussion History
## moneromooo-monero | 2020-01-13T03:24:31+00:00
What version of readline is that using ?

## dalecooper | 2020-01-13T05:56:46+00:00
Apparently readline 7.0

```
$ dpkg -l | grep readline
ii  libreadline5:amd64                            5.2+dfsg-3build1                                amd64        GNU readline and history libraries, run-time libraries
ii  libreadline7:amd64                            7.0-3                                           amd64        GNU readline and history libraries, run-time libraries
ii  readline-common
```
A few more details just in case : this happened randomly, so after the next lock (same session) all went well, then it happened again later. It was always at the unlock prompt. Also, as you can see in the screenshot the next immediate prompt (output received) showed nothing, just as expected.

## selsta | 2022-04-08T16:39:20+00:00
No other reports about this, could be an issue with your readline version. Try `8.0` or newer and comment if you can reproduce, then I can reopen.

# Action History
- Created by: dalecooper | 2020-01-12T19:10:22+00:00
- Closed at: 2022-04-08T16:39:20+00:00
