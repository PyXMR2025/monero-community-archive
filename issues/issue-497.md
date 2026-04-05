---
title: Remote control issue
source_url: https://github.com/xmrig/xmrig/issues/497
author: ghost
assignees: []
labels: []
created_at: '2018-04-04T09:37:29+00:00'
updated_at: '2018-11-05T13:18:52+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:18:52+00:00'
---

# Original Description
I write a script to remote control my Linux machines like this
```
function start(){
    for i in hosts;do
        ssh $i "/root/xmrig/xmrig"
    done
}
```
I've done ssh-key import and it needs no password to use SSH

BUT the xmrig won't run in the background even if I use '&'.

I had to quit with 'ctrl + c' for every machine manually.

Hope this issue could be solved.

Thanks a lot.


# Discussion History
## d3c0d3d | 2018-04-04T12:06:24+00:00
I believe you should run it in the background and monitor its functioning via api.

> -B, --background          run the miner in the background

## ghost | 2018-04-04T13:19:17+00:00
Actually, I've set the 'background' option in the config file. Seems that the shell did not receive a correct signal or the miner did not run in daemon mode.

# Action History
- Created by: ghost | 2018-04-04T09:37:29+00:00
- Closed at: 2018-11-05T13:18:52+00:00
