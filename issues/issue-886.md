---
title: Two Linux files in the .zip file for Windows
source_url: https://github.com/monero-project/monero-gui/issues/886
author: rbrunner7
assignees: []
labels:
- bug
- resolved
created_at: '2017-09-19T18:12:08+00:00'
updated_at: '2017-10-27T14:00:15+00:00'
type: issue
status: closed
closed_at: '2017-10-27T14:00:15+00:00'
---

# Original Description
The .zip file *monero-gui-win-x64-v0.11.0.0.zip* for Windows contains the following 2 files that are Linux files almost for sure, with no use and no role on Windows: *libcrypto.a* and *libssl.a*

(I noticed this while updating the Windows installer for the new release. I did not add the files to the install script, and the GUI wallet seems to perfectly run without those two files.)

# Discussion History
## MaxXor | 2017-09-19T18:50:30+00:00
Yes, they should get removed.

## dEBRUYNE-1 | 2017-09-23T20:09:13+00:00
+bug

## dEBRUYNE-1 | 2017-10-27T13:46:45+00:00
+resolved

# Action History
- Created by: rbrunner7 | 2017-09-19T18:12:08+00:00
- Closed at: 2017-10-27T14:00:15+00:00
