---
title: 'fatal error: uv.h: No such file or directory'
source_url: https://github.com/xmrig/xmrig/issues/571
author: LinProg
assignees: []
labels:
- question
created_at: '2018-04-21T22:22:46+00:00'
updated_at: '2018-10-10T22:18:26+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:18:26+00:00'
---

# Original Description
Ok, lets start off with BE CLEAR AND SPECIFIC because multiple people have this problem and nobody is giving a COMPLETE answer. Just "you need libuv and we have prebuilt version". Ok, well I've tried the following and still same problem so how about a step by step on how to install libuv.

Installed via these command lines:
`sudo apt-get install libuv1`
`sudo apt-get install libuv-dev`

Both say installed, so then I try:
`x86_64-w64-mingw32-g++ xmrig.cpp -o xmrig.exe`

Which still gives me the error:

`In file included from xmrig.cpp:24:0:
App.h:28:16: fatal error: uv.h: No such file or directory
compilation terminated.`

So I tried copying the uv.h file from xmrig-debs-3.0/x64/include/ and pasting it in my xmrig-master/src/ directory and the problem still persists. What am I supposed to do with the files in xmrig-debs-3.0 that will make it work? Because you dont give any instruction whatsoever beyond downloading the files making it impossible for people trying to compile on their own. And instead of telling me vaguely "install libuv" give STEP-BY-STEP instructions cause as I've described I tried doing that in multiple ways and nothing worked. I am using Ubuntu 16.04 and I'm trying to compile for Windows. I've only written programs in Java and other web based languages like PHP so if theres something else I gotta configure for the C++ compiler that'd be pretty useful information.

# Discussion History
## xmrig | 2018-04-22T04:23:25+00:00
How to build native Ubuntu version https://github.com/xmrig/xmrig/wiki/Ubuntu-Build
Native Windows version https://github.com/xmrig/xmrig/wiki/Windows-Build

If you try make cross-compilation, eg build Windows version on Linux, it should be possible, but it not supported way, I can't help you with it.

Anyway you should use `cmake` to create `Makefile` and then use `make` to build whole project, you never need run C++ compiler byself.
Thank you. 

## LinProg | 2018-04-22T06:40:29+00:00
So how am I supposed to build it straight from the source? I've added command line arguments so when I double click the executable I dont have to enter my address or the mining pool as I hard coded them in xmrig.cpp

The following command appears to only build from the original source and from the default program download location. I have a xmrig-master directory in my home folder. How would I compile by opening this directory in the terminal? I want to be able to have it where just clicking the executable will set everything up via hard code (what I'm trying to do now) and/or a custom settings file I plan on creating that contains all the args.

```
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake ..
make
```

## xmrig | 2018-04-22T06:44:18+00:00
change `cd xmrig` to `cd ~/xmrig-master`.

## ghost | 2018-09-23T00:19:30+00:00
what ? isn't the .exe loading the .json file to get args from there straight while executing "if the file exists"?

# Action History
- Created by: LinProg | 2018-04-21T22:22:46+00:00
- Closed at: 2018-10-10T22:18:26+00:00
