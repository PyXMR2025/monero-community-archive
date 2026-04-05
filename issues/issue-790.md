---
title: cmake Construction problem
source_url: https://github.com/xmrig/xmrig/issues/790
author: oneoy
assignees: []
labels:
- invalid
- question
created_at: '2018-10-11T09:03:03+00:00'
updated_at: '2018-11-05T14:23:59+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:23:59+00:00'
---

# Original Description
![360 1624122199128132](https://user-images.githubusercontent.com/38435398/46793087-730f8780-cd77-11e8-9eb2-7f0a6dbbb6c0.png)
I don't know what's wrong. Please help me.

# Discussion History
## xmrig | 2018-10-11T09:10:15+00:00
Follow documentation, use xmrig-deps https://github.com/xmrig/xmrig/wiki/Windows-Build

## oneoy | 2018-10-11T09:13:40+00:00
"D:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\Tools\VsMSBuildCmd.bat"

set CMAKE_PREFIX_PATH=C:\xmr-stak-dep\hwloc;C:\xmr-stak-dep\libmicrohttpd;C:\xmr-stak-dep\openssl

cd c:\xmrig

mkdir build

cd build

cmake -G "Visual Studio 15 2017 Win64" -T v141,host=x64 .. -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF



There's a problem here.   》》》》》》》》cmake -G "Visual Studio 15 2017 Win64" -T v141,host=x64 .. -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF





cmake --build . --config Release --target install

cd bin\Release

copy C:\xmr-stak-dep\openssl\bin\* .

## xmrig | 2018-10-11T09:15:51+00:00
You use instructions from another miner and another deps.

## oneoy | 2018-10-11T09:17:19+00:00
Which one? I'm not going to use GPU.

## oneoy | 2018-10-11T09:19:57+00:00
use >>cmake -G "Visual Studio 15 2017 Win64" -T v141,host=x64 ..
Or a mistake

## oneoy | 2018-10-11T09:20:28+00:00
![360 16751028122118107](https://user-images.githubusercontent.com/38435398/46794195-ef0acf00-cd79-11e8-85fb-629cba82a209.png)


## DeadManWalkingTO | 2018-10-11T20:07:02+00:00
Please follow the [instructions](https://github.com/xmrig/xmrig/wiki/Build).
Thank you!

# Action History
- Created by: oneoy | 2018-10-11T09:03:03+00:00
- Closed at: 2018-11-05T14:23:59+00:00
