---
title: xmrig.win32 produces start error on various x86 Windows 7 systems
source_url: https://github.com/xmrig/xmrig/issues/27
author: nightbowl
assignees: []
labels: []
created_at: '2017-07-04T18:22:42+00:00'
updated_at: '2017-07-06T07:10:54+00:00'
type: issue
status: closed
closed_at: '2017-07-06T07:10:54+00:00'
---

# Original Description
Hi!
I guess, it occurs while xmrig (2.0.0) parses command line switches. Some combinations of parameters produce error, some don't.

# Discussion History
## xmrig | 2017-07-05T01:13:28+00:00
Can you provide example command line that occurs error.
If you use option `--backup-url` it was removed in 2.0.0. Instead now accept multiple `--url` options.
Thank you.

## nightbowl | 2017-07-05T02:29:23+00:00
It's a kind of strange error. The similar results I've got on different hardware (Core i7, Core i5, etc). Previous version of xmrig was without such a flaw. Below I put series of screenshots.

1. Command line can be seen on image. There's a window in Russian saying that Xmrig has been terminated due to some error.
![01](https://user-images.githubusercontent.com/29701149/27846457-4a22eece-6159-11e7-922b-23317462dde7.jpg)

2. It's successful start just by removing --no-color option.
![02](https://user-images.githubusercontent.com/29701149/27846514-b336ab08-6159-11e7-8422-5baa597fb230.jpg)

3. Removing --cpu-affinity causes error again
![03](https://user-images.githubusercontent.com/29701149/27846547-06e05308-615a-11e7-8503-2aa451947dcc.jpg)

4. Changing --algo to -a returns working state
![04](https://user-images.githubusercontent.com/29701149/27846583-4f9b5bc4-615a-11e7-9e81-2e0878801aef.jpg)

5. Replacing -p with --pass= brings error
![05](https://user-images.githubusercontent.com/29701149/27846626-a52bf896-615a-11e7-9b18-3711db48655f.jpg)

6. The last command line iteration is to get rid of --keepalive option. Xmrig works.
![06](https://user-images.githubusercontent.com/29701149/27846728-4c331958-615b-11e7-9a4a-120a05b10ee3.jpg)


## xmrig | 2017-07-05T04:25:01+00:00
[xmrig-2.0.1-dev-gcc-win32.zip](https://github.com/xmrig/xmrig/files/1123510/xmrig-2.0.1-dev-gcc-win32.zip)
Please confirm if issue solved.
Thank you.

## xmrig | 2017-07-05T04:31:21+00:00
Also nicehash does not support keepalive. Specifying this option cause disconnects by timeout because nicehash not answer for keepalive pings (no error/no success).

## nightbowl | 2017-07-05T06:52:36+00:00
The test was successful so I confirm that your fix had solved the issue.
Thank you!

# Action History
- Created by: nightbowl | 2017-07-04T18:22:42+00:00
- Closed at: 2017-07-06T07:10:54+00:00
