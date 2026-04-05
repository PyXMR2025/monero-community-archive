---
title: How to set that the command window is not displayed at all,“Background” has
  been set to true
source_url: https://github.com/xmrig/xmrig/issues/2504
author: JeffreyRoberts2
assignees: []
labels: []
created_at: '2021-08-01T10:52:57+00:00'
updated_at: '2021-08-20T09:48:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
When using GPU to mine kawpow, the background is set to true, and the command window will be displayed for 2 seconds. How to set it so that the command window is not displayed at all, config is as follows

config.json

{
    "autosave": true,
    "background": true,
    "cpu": false,
    "opencl": true,
    "cuda": true,
    "pools": [
        {
            "algo": "kawpow",
            "url": "stratum.ravenminer.com:3838",
            "user": "RVN_WALLET",
            "pass": "x",
            "tls": false
        }
    ]
}

File:
config.json
nvrtc64_112_0.dll
nvrtc-builtins64_113.dll
xmrig.exe
xmrig-cuda.dll
WinRing0x64.sys
SHA256SUMS




# Discussion History
## Spudz76 | 2021-08-01T18:56:36+00:00
If you're launching via BAT file then that must flash a command window (for the moment it runs the BAT file).  Use a shortcut instead?

## JeffreyRoberts2 | 2021-08-02T04:21:46+00:00
> If you're launching via BAT file then that must flash a command window (for the moment it runs the BAT file).  Use a shortcut instead?

Run xmrig.exe directly, and not run through start.bat

## freakovision | 2021-08-07T20:04:51+00:00
Console apps will always flash the console window. You should change the entry point from `main` to `WinMain` and compile it with Windows Subsystem to fix this. 

## DeeDeeRanged | 2021-08-20T09:48:58+00:00
When you are using xmrig with a GPU it needs to have background set to false. At least thats what I have to do on Linux and it with nohup don't know how it works on windows.

# Action History
- Created by: JeffreyRoberts2 | 2021-08-01T10:52:57+00:00
