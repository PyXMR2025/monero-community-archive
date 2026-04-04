---
title: Monero GUI (0.17.1.4 / 5 ) Crash on MAC OS after entering password
source_url: https://github.com/monero-project/monero-gui/issues/3250
author: TCardinal
assignees: []
labels: []
created_at: '2020-11-30T14:51:31+00:00'
updated_at: '2021-04-21T01:36:37+00:00'
type: issue
status: closed
closed_at: '2021-04-21T01:36:37+00:00'
---

# Original Description
This happens every time on both these versions. 

Run Monero GUI
Enter Password
Crash

Process:               monero-wallet-gui [44598]
Path:                  /private/var/folders/*/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
Identifier:            org.monero-project.monero-wallet-gui
Version:               0.17.1.5 (???)
Code Type:             X86-64 (Native)
Parent Process:        ??? [1]
Responsible:           monero-wallet-gui [44598]
User ID:               501

Date/Time:             2020-11-30 14:41:52.117 +0000
OS Version:            Mac OS X 10.15.5 (19F96)
Report Version:        12
Anonymous UUID:        6324FB06-154E-9F73-6CB0-1229E0949959


Time Awake Since Boot: 600000 seconds

System Integrity Protection: disabled

Notes:                 Translocated Process

Crashed Thread:        12  QSGRenderThread

Exception Type:        EXC_CRASH (SIGABRT)
Exception Codes:       0x0000000000000000, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Application Specific Information:
abort() called

Application Specific Signatures:
Graphics kernel error: 0x00000003

Thread 12 crashed with X86 Thread State (64-bit):
  rax: 0x0000000000000000  rbx: 0x00007000061cf000  rcx: 0x00007000061cea78  rdx: 0x0000000000000000
  rdi: 0x0000000000014603  rsi: 0x0000000000000006  rbp: 0x00007000061ceaa0  rsp: 0x00007000061cea78
   r8: 0x00007000061ce880   r9: 0x00007000061ceac0  r10: 0x00007000061cf000  r11: 0x0000000000000246
  r12: 0x0000000000014603  r13: 0x0000000000000000  r14: 0x0000000000000006  r15: 0x0000000000000016
  rip: 0x00007fff7168033a  rfl: 0x0000000000000246  cr2: 0x00007fc37d978000
  
Logical CPU:     0
Error Code:      0x02000148
Trap Number:     133


# Discussion History
## selsta | 2020-11-30T14:53:10+00:00
Is this the full crash log output? Anything specific about your setup?

## TCardinal | 2020-12-01T10:44:33+00:00
The full crash report attached. There was nothing special in the installation, just opened the install and moved the files to Applications
[Monero GUI Crash Report.txt](https://github.com/monero-project/monero-gui/files/5621944/Monero.GUI.Crash.Report.txt)


## selsta | 2020-12-01T10:45:59+00:00
What kind of Mac is this?

## xiphon | 2020-12-01T11:39:19+00:00
Something is wrong with the GPU driver, it causes the crash. You could try to either fix the driver issue or run Monero GUI in software rendering mode (set `QMLSCENE_DEVICE=softwarecontext` environment variable).

## selsta | 2021-04-21T01:36:37+00:00
Closing as there are no further information and the crash does not seem monero related.

# Action History
- Created by: TCardinal | 2020-11-30T14:51:31+00:00
- Closed at: 2021-04-21T01:36:37+00:00
