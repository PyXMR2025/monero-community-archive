---
title: trouble starting monerod.exe from windows 10 64-bit cmd window
source_url: https://github.com/monero-project/monero-site/issues/289
author: DavidJNowak
assignees: []
labels: []
created_at: '2017-06-30T04:39:12+00:00'
updated_at: '2017-10-20T22:13:25+00:00'
type: issue
status: closed
closed_at: '2017-08-31T09:25:11+00:00'
---

# Original Description

![monero daemon start message](https://user-images.githubusercontent.com/13257104/27721145-53c7cb1a-5d13-11e7-9948-cf42d0a92ba0.PNG)
![mymonerowallet not connect window](https://user-images.githubusercontent.com/13257104/27721147-53cc0c7a-5d13-11e7-9099-32bbf1f25c12.PNG)
![windows 10 gui mymonerowallet address book window](https://user-images.githubusercontent.com/13257104/27721146-53c9a412-5d13-11e7-8d15-0012aa26e7db.PNG)
![windows 10 gui mymonerowallet daemon failed to start message](https://user-images.githubusercontent.com/13257104/27721150-53d0d264-5d13-11e7-9498-2c05d21f366b.PNG)
![windows 10 gui mymonerowallet history window](https://user-images.githubusercontent.com/13257104/27721149-53cf4390-5d13-11e7-8720-5c952316058c.PNG)
![windows 10 gui mymonerowallet receive window](https://user-images.githubusercontent.com/13257104/27721148-53ccf1da-5d13-11e7-9293-4b592db65bc7.PNG)
![windows 10 gui mymonerowallet send window](https://user-images.githubusercontent.com/13257104/27721152-53e1c100-5d13-11e7-9bfe-85b5655e82cf.PNG)
![windows 10 gui mymonerowallet settings window](https://user-images.githubusercontent.com/13257104/27721151-53df974a-5d13-11e7-934f-afafd9453237.PNG)







I am trying to get monerod started as a node from either the GUI or CLI in Windows, but monerod code is failing.  I have been trying to run it as installed in the Downloads\monero-win-x64-v0.10.3.1\ folder or the Program Files\monero-gui-0.10.3.1-beta2\ folder.

Both fail.

The CLI interface gives me these messages:

C:\Users\Owner\Downloads\monero-win-x64-v0.10.3.1\monero-v0.10.3.1>monerod
2017-06-29 21:12:03.612 14104   INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-06-29 21:12:03.612 14104   INFO    global  src/daemon/main.cpp:282 Monero 'Wolfram Warptangent' (v0.10.3.1-release)
2017-06-29 21:12:03.612 14104   INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-06-29 21:12:03.612 14104   INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-06-29 21:12:03.612 14104   INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-06-29 21:12:11.345 14104   INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-06-29 21:12:11.345 14104   INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-06-29 21:12:11.345 14104   INFO    global  contrib/epee/include/net/http_server_impl_base.h:70  Binding on 127.0.0.1:18081
2017-06-29 21:12:11.345 14104   INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-06-29 21:12:11.345 14104   INFO    global  src/daemon/core.h:73    Initializing core...
2017-06-29 21:12:11.345 14104   INFO    global  src/cryptonote_core/cryptonote_core.cpp:326     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-06-29 21:12:11.361 14104   WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:71   Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2017-06-29 21:12:11.361 14104   ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:395     Error opening database: Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2017-06-29 21:12:11.361 14104   INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-06-29 21:12:11.361 14104   INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-06-29 21:12:11.377 14104   INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-06-29 21:12:11.377 14104   ERROR   daemon  src/daemon/core.h:94    Failed to deinitialize core...
2017-06-29 21:12:11.377 14104   INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-06-29 21:12:11.377 14104   INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully

C:\Users\Owner\Downloads\monero-win-x64-v0.10.3.1\monero-v0.10.3.1>

The GUI gives me this messsage:

[Use Monero.pdf](https://github.com/monero-project/monero-site/files/1114104/Use.Monero.pdf)
![monerd windows startup failure](https://user-images.githubusercontent.com/13257104/27720814-e8bee648-5d10-11e7-9ea6-45cabc16a8a1.PNG)


# Discussion History
## mattcode55 | 2017-07-13T12:29:33+00:00
I think you want to report that issue [here (https://github.com/monero-project/monero)](https://github.com/monero-project/monero) instead, this is the issue tracker for the getmonero.org website.

## rehrar | 2017-07-13T23:38:02+00:00
@DavidJNowak can we close this issue seeing as how this isn't the place for this type of support? Thanks.

# Action History
- Created by: DavidJNowak | 2017-06-30T04:39:12+00:00
- Closed at: 2017-08-31T09:25:11+00:00
