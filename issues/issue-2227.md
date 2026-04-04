---
title: 'Error: failed to load wallet: basic_string::resize in monero-gui-win-x64-v0.10.3.1'
source_url: https://github.com/monero-project/monero/issues/2227
author: godamos
assignees: []
labels:
- invalid
created_at: '2017-07-30T13:25:25+00:00'
updated_at: '2018-01-08T13:56:33+00:00'
type: issue
status: closed
closed_at: '2018-01-08T13:56:33+00:00'
---

# Original Description
i had read https://monero.stackexchange.com/questions/1380/wallet-initialization-failed-basic-stringresize but some issue is diffent 
my version is monero-gui-win-x64-v0.10.3.1 and monero-win-x86-v0.10.3.1 (the lasted version download on https://getmonero.org/downloads/)

its good somedays ago but get issue in today . I haven't modified any files. i dont knnow why.and test on three computer All these problems arise



 2017-07-30 21:14:01.238	720	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-07-30 21:14:03.035	720	INFO 	global	src/simplewallet/simplewallet.cpp:179	Wallet and key files found, loading...
2017-07-30 21:14:05.035	720	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2413	Loaded wallet keys file, with public address: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
2017-07-30 21:14:05.473	720	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2450	Failed to open portable binary, trying unportable
2017-07-30 21:14:05.488	720	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2469	Failed to open portable binary, trying unportable
2017-07-30 21:14:05.488	720	ERROR	global	src/simplewallet/simplewallet.cpp:179	Error: failed to load wallet: basic_string::resize
2017-07-30 21:14:05.488	720	ERROR	wallet.simplewallet	src/simplewallet/simplewallet.cpp:1295	failed to open account
2017-07-30 21:14:05.488	720	ERROR	wallet.simplewallet	src/simplewallet/simplewallet.cpp:4468	Failed to initialize wallet


# Discussion History
## dEBRUYNE-1 | 2017-08-02T22:34:48+00:00
If I recall correctly, this means that your wallet cache is incompatible. To solve it, rename the walletcache to <wallet_old> such that you don't lose any data. Subsequently, you can open the .keys file and the GUI will automatically rebuild the wallet cache. 

## Jaqueeee | 2017-08-07T21:33:02+00:00
@godamos have you tried what @dEBRUYNE-1 suggested above? 



## dEBRUYNE-1 | 2018-01-08T13:01:03+00:00
+invalid

# Action History
- Created by: godamos | 2017-07-30T13:25:25+00:00
- Closed at: 2018-01-08T13:56:33+00:00
