---
title: Bus Error after  'use profile  rx  (4 threads) scratchpad 2048 KB'
source_url: https://github.com/xmrig/xmrig/issues/3009
author: Zigler21
assignees: []
labels: []
created_at: '2022-04-07T04:27:05+00:00'
updated_at: '2022-04-07T05:00:24+00:00'
type: issue
status: closed
closed_at: '2022-04-07T05:00:24+00:00'
---

# Original Description
**Describe the bug**
A Bus error occurs when trying to start mining on Raspberry pi 4. 

**To Reproduce**
clone repo and build with Debian instructions.

**Expected behavior**
I'm assuming that the miner usually just start mining without any big issues.

**Required data**
 
![error](https://user-images.githubusercontent.com/44149710/162119513-d7c7ed31-858f-4f2c-b9fe-b8b20b419c41.PNG)

{
    "autosave": true,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "url": "us-west.minexmr.com:443",
            "user": "[hidden]",
            "keepalive": true,
            "tls": true
        }
    ]
}

 - OS: GNU/Linux: Raspbian
 

**Additional context**
This is my first time doing crypto mining, thus I am a newb, but I do know how use Linux fairly well, so following instruction isn't hard for me. 


# Discussion History
## Zigler21 | 2022-04-07T05:00:24+00:00
UPDATE: 
All I had to do was install Raspbian 64bit, no errors so far...
Unfortunate to lose all of the progress I had with the initial setup, but it works!

If this is happening to you, try to see if this will help.

# Action History
- Created by: Zigler21 | 2022-04-07T04:27:05+00:00
- Closed at: 2022-04-07T05:00:24+00:00
