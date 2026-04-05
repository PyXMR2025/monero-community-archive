---
title: 'Error: please uppgrade amd'
source_url: https://github.com/xmrig/xmrig/issues/3064
author: G4rmSec
assignees: []
labels: []
created_at: '2022-06-07T13:13:58+00:00'
updated_at: '2025-06-18T23:01:24+00:00'
type: issue
status: closed
closed_at: '2025-06-18T23:01:24+00:00'
---

# Original Description
Iv started to get 
error: "please uppgrade 'XMRig-amd/2.14.6 (Windows NT 10.0; win64; x64) libuv/1.31.0 msvc/2017' to be.2.0+ to support Rx/0 Montero algo", code:1

Running XMRig 6.17.0
Can't get my rx5600xt to mine. 


# Discussion History
## SChernykh | 2022-06-07T13:20:09+00:00
Are you sure that you downloaded XMRig 6.17.0 and not XMRig-amd 2.14.6? So you see both "XMRig 6.17.0" and then this error message in the console window? Which pool do you use?

## G4rmSec | 2022-06-07T13:23:17+00:00
Wanted to run CPU and GPU to mine Montero
So I'm using XMRig-amd 2.14.6
And XMRig 6.17.0 

Have the AMD files in a folder in XMRig

## G4rmSec | 2022-06-07T13:30:30+00:00
![Monero](https://user-images.githubusercontent.com/107049624/172392691-bf951fd1-b70d-4d8a-a0e2-f8555ef87e23.jpg)


## SChernykh | 2022-06-07T13:33:26+00:00
XMRig-amd 2.14.6 is deprecated, use XMRig 6.17.0 for both CPU and GPU. Find "opencl" section in config.json and set "enabled" to true.

## G4rmSec | 2022-06-07T13:37:17+00:00
Thank you
How can I see if it worked? 
opencl in the program still says disabled

## suoutriV | 2024-04-05T23:50:05+00:00
after setting it to true, you'll see opencl and cpu saying accepted etc.. and that means both are working at the same time. and check your temps for both and your gpu fans should be moving now

# Action History
- Created by: G4rmSec | 2022-06-07T13:13:58+00:00
- Closed at: 2025-06-18T23:01:24+00:00
