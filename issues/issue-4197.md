---
title: Build arm64 binaries for Windows
source_url: https://github.com/monero-project/monero-gui/issues/4197
author: AArnott
assignees: []
labels: []
created_at: '2023-07-16T20:28:21+00:00'
updated_at: '2023-10-14T13:33:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Please build arm64 installer and binaries for Windows. Windows x64 binaries require emulation on arm64 hardware and burn laptop batteries more than necessary.

# Discussion History
## selsta | 2023-08-01T21:29:55+00:00
We are currently focused on adding macOS ARM binaries, but the end goal is to support all 3 operating systems (macOS, Linux, Windows) natively on ARM.

## karelbilek | 2023-08-30T09:10:12+00:00
Is there a ticket/issue tracking the progress of macos ARM binaries?

edit: ah it's hidden here

https://github.com/monero-project/monero-gui/issues/3495

## Mike-Bou | 2023-10-13T23:47:31+00:00
> We are currently focused on adding macOS ARM binaries, but the end goal is to support all 3 operating systems (macOS, Linux, Windows) natively on ARM.

Good. I have been building MacOS ARM variants, since 18.1.1 Now i cannot build 18.3.1 due to problems with Qt 5.15.2 from Qt or qt@5 5.15.10_1 from homebrew. 

For 18.2.2 I was able to make deploy and codesign, but not Notarize.

https://github.com/Mike-Bou/monero-wallet-gui-aarch64-AppleSilicon 

There seemed to be some problems, not having full Frameworks and Resouces, but did work ok 

https://mikebouckley.net/download/error.html

has details of failed build. index.html has screenshots of it working.

Now running monerod on a linux server (before on x86 Mac with big SSD's) Using Mac ARM GUI to view wallet, and or a VM Linux with ssh -X  window from the server.

## selsta | 2023-10-14T13:33:07+00:00
@Mike-Bou please follow #4228 for your build issue

# Action History
- Created by: AArnott | 2023-07-16T20:28:21+00:00
