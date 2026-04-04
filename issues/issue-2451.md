---
title: Error building Monero-Gui from source in Windows + Fix from Monero-Dev Community
source_url: https://github.com/monero-project/monero-gui/issues/2451
author: keatond
assignees: []
labels: []
created_at: '2019-11-22T18:03:44+00:00'
updated_at: '2021-04-21T02:32:25+00:00'
type: issue
status: closed
closed_at: '2021-04-21T02:32:25+00:00'
---

# Original Description
Hello All!

So I took the plunge to learn how to build software from source. I was following the instructions within the README.md.

Everything went smoothly until I got to the "make deploy" command. 
I received the error: 
```
Release` build
cp: cannot stat '/mingw64/bin/libdouble-conversion.dll': No such file or directory
make: *** [Makefile:471: deploy] Error 1
```
I reached out to the monero-dev community about the issue and iDUNK requested that I install:
`pacman -S mingw-w64-x86_64-double-conversion`

I then re-did the "make deploy" command and it built successfully and was able to open the GUI.


# Discussion History
## selsta | 2021-04-21T02:32:25+00:00
`mingw-w64-x86_64-double-conversion` is a required dependency by `mingw-w64-x86_64-qt5` which is included in the readme. Not clear why it was missing on your PC.

# Action History
- Created by: keatond | 2019-11-22T18:03:44+00:00
- Closed at: 2021-04-21T02:32:25+00:00
