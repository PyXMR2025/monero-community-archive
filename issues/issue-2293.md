---
title: mining with amd card result 0 hashrate
source_url: https://github.com/xmrig/xmrig/issues/2293
author: ilovefood2
assignees: []
labels: []
created_at: '2021-04-21T05:34:01+00:00'
updated_at: '2021-05-05T23:48:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
I'm trying to use amd card to mine, all settings are default, but result seems to be 0 hashrate for some reason( see attached picture

here is command i use
```
@echo off
"%~dp0xmrig.exe" -o pool.minexmr.com:4444 -u xxxxx --opencl --no-cpu 
pause
```

any idea? or did i miss anything ? 

![image](https://user-images.githubusercontent.com/4293869/115501434-3757b180-a241-11eb-9a12-6b963b176536.png)


# Discussion History
## Lonnegan | 2021-04-21T14:21:47+00:00
I have no idea, but since not even temperature and consumption is reported correctly, xmrig may not get along with Navi 14, yet?

Apart from that, you should not mine XMR with graphics cards. XMR uses RandomX as algo and that is a pure CPU algo running very very inefficiently on GPUs. Mine something else with your graphics cards, TRTL or XHV for example. This still works well with 4GB cards.

## ilovefood2 | 2021-04-21T14:35:52+00:00
Thanks, I was just testing it

## SChernykh | 2021-04-21T14:38:35+00:00
XMRig recognizes Navi 14 and uses an appropriate code for it, I tested it on Radeon RX 5500 XT which is also `gfx1012` and it worked. I don't know what exactly is the issue here. What OS is this? Windows or Linux?

## G2G2G2G | 2021-04-23T06:21:58+00:00
@SChernykh I doubt he's running a .exe on linux

## ilovefood2 | 2021-05-05T23:48:35+00:00
> XMRig recognizes Navi 14 and uses an appropriate code for it, I tested it on Radeon RX 5500 XT which is also `gfx1012` and it worked. I don't know what exactly is the issue here. What OS is this? Windows or Linux?

it's windows

# Action History
- Created by: ilovefood2 | 2021-04-21T05:34:01+00:00
