---
title: Logfile being generated with wrong name
source_url: https://github.com/xmrig/xmrig/issues/3596
author: Dat-Pudding
assignees: []
labels: []
created_at: '2024-12-10T23:40:28+00:00'
updated_at: '2024-12-11T01:16:00+00:00'
type: issue
status: closed
closed_at: '2024-12-11T01:15:10+00:00'
---

# Original Description
**Describe the bug**
After inserting the log-file option into `config.json` the executable did not generate any log file and after applying the according parameters in the `start.cmd` it always get generated as plain text file named `"ogfile"` without any file extension despite `"miner.log"` being specified as name.
![ogfile](https://github.com/user-attachments/assets/bae5bc52-317e-4db8-af93-7de70309616e)

**To Reproduce**
See description.

**Expected behavior**
Proper generation of a plain text file in accordance to the given file name and extension.

**Required data**
 - Operating System: Windows 10 Home (22H2)
 - App Version: XMRig v6.22.2
    - *acquired at: https://xmrig.com/download*
    - *file name: xmrig-6.22.2-msvc-win64.zip*
 - will add screenshot of log file later
 - command line/`start.cmd`: 
   ```
   @echo off
   cd /d "%~dp0"
   xmrig.exe -o protocol://xmr.somePool:1234 -u someAddress/id -k --coin monero -logfile "${XMRIG_EXE_DIR}/miner.log"
   pause
   ```
 - `config.json`:
   ![screenshot_config](https://github.com/user-attachments/assets/b0cd5b4f-5485-40ff-849b-7fd878d4ddf4)

**Additional context**
Maybe I just unknowingly broke some syntax, could be as trivial as that.

Issue is **NOT** severe! From the looks of it, it's just cosmetic since the file content itself is still a perfectly readable and complete log in plain text.

# Discussion History
## Dat-Pudding | 2024-12-11T01:15:59+00:00
I'm just illiterate it seems, the start.cmd was giving the parameter incorrectly 

# Action History
- Created by: Dat-Pudding | 2024-12-10T23:40:28+00:00
- Closed at: 2024-12-11T01:15:10+00:00
