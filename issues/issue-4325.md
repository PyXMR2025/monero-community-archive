---
title: warning net fatal
source_url: https://github.com/monero-project/monero-gui/issues/4325
author: Bigalsr
assignees: []
labels: []
created_at: '2024-06-22T15:44:46+00:00'
updated_at: '2024-06-24T18:12:19+00:00'
type: issue
status: closed
closed_at: '2024-06-24T12:40:03+00:00'
---

# Original Description
hey developers. im having an issue with running node solo on win10
Intel(R) Xeon(R) CPU E5-2698 v3 @ 2.30GHz   2.30 GHz 16 core 32 thread
32 gb ram
monerorod ran fine the first few times i ran it but then started to say failed to bind ip4 after this started. ive never been able to run solo but i have been able to run pool. but nothing now


2024-06-22 14:39:22.250	4024	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-06-22 14:39:22.252	4024	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.3-release)
2024-06-22 14:39:24.196	9980	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-06-22 14:39:24.196	9980	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.3-release)
2024-06-22 14:39:25.078	4024	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2024-06-22 14:39:26.945	9980	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2024-06-22 14:39:27.252	684	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-06-22 14:39:27.253	684	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.3-release)
2024-06-22 14:39:32.321	684	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2024-06-22 14:40:37.032	5848	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2024-06-22 14:40:37.033	5848	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.3-release)

# Discussion History
## selsta | 2024-06-22T15:47:17+00:00
Can you explain with more detail what the exact issue is? The log does not show anything interesting.

## Bigalsr | 2024-06-22T16:08:13+00:00
These are the errors i get in the bitmonero file when i try to run solo. it starts to mine in solo mode and then goes into a short loop of disconnected and connected and then the synchronizing bars come back up and start downloading the blockchain all over again like they just disappeared. so i went into that file and scrolled down and these are constantly repeating, then downloading more blockchain then the messages over and over

## selsta | 2024-06-22T17:31:42+00:00
Without mining, can you go to Settings -> Log, type "status" into it and share the output?

## Bigalsr | 2024-06-23T20:49:08+00:00
I appreciate your response. I am away from my computer today, can I get that info for you when I get back around to it please?

## selsta | 2024-06-24T11:40:28+00:00
Yes, you can reply once you have time

## Bigalsr | 2024-06-24T12:40:03+00:00
im not sure if this was the problem but i found i had to have java installed and i reset gui twice and downloaded the previous version of the monerod file and it seems to have fixed everything including my mining from my other pc to the main node. i read another post that you had said to download that previous version and it fixed it. at least for now. sorry for no caps but typing from mini handheld keyboard. thank you for your time.

## selsta | 2024-06-24T18:12:18+00:00
Java should not be needed, monero doesn't use Java.

# Action History
- Created by: Bigalsr | 2024-06-22T15:44:46+00:00
- Closed at: 2024-06-24T12:40:03+00:00
