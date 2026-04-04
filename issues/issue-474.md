---
title: convert_blockchain fails MDM_MAP_FULL
source_url: https://github.com/monero-project/monero/issues/474
author: ByronAP
assignees: []
labels: []
created_at: '2015-11-01T11:49:11+00:00'
updated_at: '2015-11-01T13:47:21+00:00'
type: issue
status: closed
closed_at: '2015-11-01T13:47:21+00:00'
---

# Original Description
[- batch commit at height 278000 -]

height 278970/803743 (34%)2015-Nov-01 06:47:02.790016 Failed to add <tx hash, gl
obal output index> to db transaction: MDB_MAP_FULL: Environment mapsize limit re
ached

Error adding block 278975 to new blockchain: Failed to add <tx hash, global outp
ut index> to db transaction: MDB_MAP_FULL: Environment mapsize limit reached


# Discussion History
## fluffypony | 2015-11-01T11:50:12+00:00
Do you have enough free disk space? Also, what version are you using? There's a bug we fixed with the map resize, but as I recall that was some time ago, so this may be unrelated.


## ByronAP | 2015-11-01T11:51:25+00:00
Plenty of space and i am trying out the 0.9 beta build since I could not get the src to build properly (win64)


## ByronAP | 2015-11-01T12:25:13+00:00
I must say with this much data it would be nice to have support for external databases such as MSSQL and MYSQL


## fluffypony | 2015-11-01T12:58:59+00:00
Ok I've built a new beta, try this: https://downloads.getmonero.org/monero.win.x64.v0-9-beta.zip


## ByronAP | 2015-11-01T13:24:57+00:00
Thank you. Is there anyway we can get the build instructions updated so i can keep evaluating off of the current src?


## fluffypony | 2015-11-01T13:25:31+00:00
The build instructions work, I just followed them to build the beta:)


## ByronAP | 2015-11-01T13:25:40+00:00
hmm oddd


## ByronAP | 2015-11-01T13:29:55+00:00
first error right off the bat installing packages "target not found: mingw-w64-x86_64-unbound"

info@Byron-PC MINGW64 /f/bitmonero
$ pacman -S mingw-w64-x86_64-gcc make mingw-w64-x86_64-cmake mingw-w64-x86_64-unbound mingw-w64-x86_64-boost
warning: mingw-w64-x86_64-gcc-5.2.0-4 is up to date -- reinstalling
warning: make-4.1-4 is up to date -- reinstalling
warning: mingw-w64-x86_64-cmake-3.3.2-2 is up to date -- reinstalling
error: target not found: mingw-w64-x86_64-unbound
warning: mingw-w64-x86_64-boost-1.59.0-2 is up to date -- reinstalling


## fluffypony | 2015-11-01T13:31:54+00:00
Ah, looks like msys2 has lost its unbound package temporarily. Skip it, you don't need it to build, we include unbound in the source tree for static builds (which is the default way its built on Windows anyway)


## ByronAP | 2015-11-01T13:47:21+00:00
I must have had a bad git clone because I just re-cloned it and now it built... Thank You for all of the help BTW very good to know people are around.


# Action History
- Created by: ByronAP | 2015-11-01T11:49:11+00:00
- Closed at: 2015-11-01T13:47:21+00:00
