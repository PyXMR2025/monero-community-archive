---
title: 'Build failed - ''Makefile:284: recipe for target ''release/bin/monero-wallet-gui''
  failed'''
source_url: https://github.com/monero-project/monero-gui/issues/1186
author: 1337tester
assignees: []
labels:
- resolved
created_at: '2018-03-17T23:09:48+00:00'
updated_at: '2018-03-29T21:54:19+00:00'
type: issue
status: closed
closed_at: '2018-03-29T21:54:19+00:00'
---

# Original Description
The recent build is not building on my Ubuntu Linux - [log_build.txt](https://github.com/monero-project/monero-gui/files/1822181/log_build.txt)

OS - Ubuntu 17.10, GNOME
commit -  da0155e

# Discussion History
## 1337tester | 2018-03-17T23:49:38+00:00
Just to spare some time here, I have all the dependencies (made double-sure) and I did builds of course with previous versions successfully 

## radfish | 2018-03-18T21:20:00+00:00
`src/wallet/api/CMakeFiles/obj_wallet_api.dir/build.make:62: recipe for target 'src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet.cpp.o' failed`

so this might be an issue for monero not monero-gui but I don't see the error in the log. Does monero build for you?

## 1337tester | 2018-03-18T22:46:55+00:00
yes, the newest build (yesterday from master) of monero cli builds quite smoothly

## qubenix | 2018-03-24T14:32:24+00:00
Seems that I have the same issue on Debian 9: [build.log](http://termbin.com/f04m). Monero builds no problem from current master.

## qubenix | 2018-03-24T15:34:56+00:00
Some strangeness, on build attempts 2 and 3 I get a new error, different error than the first attempt. This is the log from subsequent build attempts: http://termbin.com/b7ms.

## qubenix | 2018-03-26T19:19:35+00:00
#1172 fixes this for me.

## 1337tester | 2018-03-26T22:13:35+00:00
Is this already in the master? I tried the newest master (merge of PR #1144) just now - still the same error

## 1337tester | 2018-03-28T08:15:07+00:00
@qubenix  - yes, tried yesterday as #1172 was merged and it can be built

-> can be closed

## sanderfoobar | 2018-03-29T21:48:13+00:00
+resolved

# Action History
- Created by: 1337tester | 2018-03-17T23:09:48+00:00
- Closed at: 2018-03-29T21:54:19+00:00
