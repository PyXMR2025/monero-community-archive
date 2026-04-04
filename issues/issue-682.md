---
title: blockchain_import.exe crashes when importing blockchain.raw
source_url: https://github.com/monero-project/monero/issues/682
author: rariro
assignees: []
labels: []
created_at: '2016-02-21T08:46:30+00:00'
updated_at: '2016-02-22T21:29:10+00:00'
type: issue
status: closed
closed_at: '2016-02-22T21:29:10+00:00'
---

# Original Description
Command: blockchain_import.exe --log-level 1 > log.txt
Last entry in log.txt before crash: "[- batch commit at height 1000 -]"
System: Windows 7 Ultimate x64, Lenovo G500 i3 3110M
Version: monero windows x64 v0.9.1

Let me know if you need more info and I can reproduce the crash.


# Discussion History
## rariro | 2016-02-21T08:48:33+00:00
From Windows crash window:

Problem signature:
  Problem Event Name:   APPCRASH
  Application Name: blockchain_import.exe
  Application Version:  0.0.0.0
  Application Timestamp:    569932ce
  Fault Module Name:    blockchain_import.exe
  Fault Module Version: 0.0.0.0
  Fault Module Timestamp:   569932ce
  Exception Code:   c0000005
  Exception Offset: 000000000014a432
  OS Version:   6.1.7601.2.1.0.256.1
  Locale ID:    1033
  Additional Information 1: 7068
  Additional Information 2: 706855bd6cead96492663940e72a4bdb
  Additional Information 3: 238f
  Additional Information 4: 238fd18da58aef11f116a8da025a92c1

Read our privacy statement online:
  http://go.microsoft.com/fwlink/?linkid=104288&clcid=0x0409

If the online privacy statement is not available, please read our privacy statement offline:
  C:\Windows\system32\en-US\erofflps.txt


## hyc | 2016-02-22T03:05:23+00:00
Current master 3860feecb8374ba3b49c30503def22260c32304e works fine for me.


## rariro | 2016-02-22T14:59:36+00:00
if you have a win64 binary with that commit, I can test it out. In the meantime I'll try to play around with compiling myself, but I can't promise anything :)


## hyc | 2016-02-22T17:41:00+00:00
http://highlandsun.com/hyc/monero.w64-3860fee.7z sha1sum 749564cb3fad38f67a70996a3c174bf8c3208e13


## rariro | 2016-02-22T21:29:10+00:00
yup, looks like that commit fixed it, thanx! I'll let it run overnight just to confirm.


# Action History
- Created by: rariro | 2016-02-21T08:46:30+00:00
- Closed at: 2016-02-22T21:29:10+00:00
