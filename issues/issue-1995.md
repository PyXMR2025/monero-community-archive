---
title: 'Is this a bug or a feature? '
source_url: https://github.com/xmrig/xmrig/issues/1995
author: Maz4id
assignees: []
labels:
- bug
created_at: '2020-12-22T09:00:45+00:00'
updated_at: '2020-12-22T21:31:10+00:00'
type: issue
status: closed
closed_at: '2020-12-22T21:31:10+00:00'
---

# Original Description
Today I wanted to compile Xmrig again because I had an old version of it v6.4.0. 
I always use at cmake `-DWITH_EMBEDDED_CONFIG=ON ` and background true inside the config. 
After I finished and tried to start it, I saw that there is no error message and it goes right into background.
It used to say: unable to open config.json or something like that.
So that message is removed now if ur using embedded config option?
Personally, I love it because you can run xmrig again with 'systemd'. It used to fail the service because of that error message. 

# Discussion History
## xmrig | 2020-12-22T09:05:44+00:00
Seems related #1930
Can you show your service file? Thank you.

## Maz4id | 2020-12-22T09:22:58+00:00
It works If the executable path is prefixed with "-"so I don't have any problems running it.
But again, the error message is removed now on embedded config option or is a bug? 

## xmrig | 2020-12-22T09:32:28+00:00
Message not removed, but since v6.5.0 with #1925 there should be 3 messages instead of 1, not sure how it breaks systemd compatibility, but you are the second who reported it. I asked about the service file to try reproduce the issue.
Thank you.


## Maz4id | 2020-12-22T10:36:37+00:00
Here is a video of how I compiled xmrig on centos 7 and you can clearly see at the end that there's no message about config or anything. It goes to background instantly. 
Maybe it helps if ur saying that the message is not removed.
https://youtu.be/Xw-_3Je5Ln0

## xmrig | 2020-12-22T14:47:48+00:00
Fixed in dev branch, this was regression with v6.7.0, log was not initialized on such an early phase.

P.S. Please don't use `-DBUILD_STATIC=ON` option, it only work as expected with musl libc for example on [Alpine](https://xmrig.com/docs/miner/build/alpine) your executable will crash on other OS because not all functions was added https://i.imgur.com/6qu6jch.png

# Action History
- Created by: Maz4id | 2020-12-22T09:00:45+00:00
- Closed at: 2020-12-22T21:31:10+00:00
