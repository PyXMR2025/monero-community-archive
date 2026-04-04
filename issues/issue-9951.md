---
title: UnstoppableSwap instantly closes on launch
source_url: https://github.com/monero-project/monero/issues/9951
author: dkhughesme
assignees: []
labels: []
created_at: '2025-06-08T18:06:03+00:00'
updated_at: '2025-06-09T17:10:13+00:00'
type: issue
status: closed
closed_at: '2025-06-09T17:10:13+00:00'
---

# Original Description
Hello,

I am trying to run the latest version of on a custom Windows 10 build (Superlite SE), but the application immediately opens and then closes without any error messages or logs. I have only the single executable file — no additional DLLs or config files in the folder.unstoppableswap-gui-rs.exe

Details:

Windows version: 10.0.26100.4061 (Superlite SE custom build)
.NET Framework 4.8.1 and latest Visual C++ Redistributables are installed
Tried launching from command line, PowerShell, and with admin rights — no difference
No output or error logs generated
Older version 0.6.4 runs fine on the same system
The process sometimes remains in background after closing, blocking relaunch until manual kill
No antivirus or firewall is blocking it

Is this expected behavior? Is there any missing dependency or environment setting required? Could you please advise how to troubleshoot this or provide a build compatible with minimal Windows versions?

Thank you!

# Discussion History
## nahuhh | 2025-06-08T18:23:10+00:00
thanks for reporting! this repo is for monero though. Please open your unstoppableswap issue here:

https://github.com/UnstoppableSwap/core

# Action History
- Created by: dkhughesme | 2025-06-08T18:06:03+00:00
- Closed at: 2025-06-09T17:10:13+00:00
