---
title: Monero v0.17.3.2 will NOT compile with msys2 for various reasons.
source_url: https://github.com/monero-project/monero/issues/8364
author: LordOfDisdain
assignees: []
labels: []
created_at: '2022-05-30T07:50:15+00:00'
updated_at: '2022-06-12T08:23:31+00:00'
type: issue
status: closed
closed_at: '2022-06-02T14:54:45+00:00'
---

# Original Description
Good afternoon. I am trying to build Monero using a windows 11 operating system. I have followed the steps and ran into some issues when it came to using the command: make release-static-win64. I have troubleshooted the the steps but there is one issue I cannot understand. I cannot edit the properties of Msys2 Shell to change msys2_shell.bat" to "msys2_shell.cmd -mingw64. I have looked up several forums on how to change the properties of MSYS2 and the properties option does not exist. That is the only thing so far stopping me from building Monero on my computer. I will also attach the output logs to see if there is anything I missed because so far I am stuck. Thank you for your time.
[CMakeOutput.log](https://github.com/monero-project/monero/files/8796518/CMakeOutput.log)
[CMakeError.log](https://github.com/monero-project/monero/files/8796520/CMakeError.log)
![Monero build fail](https://user-images.githubusercontent.com/42873006/170943708-cc42510e-3db8-46c7-9194-408b77ad86b9.png)
 

# Discussion History
## selsta | 2022-05-30T19:58:28+00:00
Does compiling master work?

## LordOfDisdain | 2022-06-02T14:54:45+00:00
> Does compiling master work?

It has worked! I also had to download the other binaries on my windows drive. Thank you again for your help and I look forward to building with Monero. 

# Action History
- Created by: LordOfDisdain | 2022-05-30T07:50:15+00:00
- Closed at: 2022-06-02T14:54:45+00:00
