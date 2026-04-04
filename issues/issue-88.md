---
title: 'Win32/64: Install Inno Setup and modify buildbot''s kovri nightly-build command'
source_url: https://github.com/monero-project/meta/issues/88
author: anonimal
assignees: []
labels:
- resolved
created_at: '2017-07-14T04:08:10+00:00'
updated_at: '2017-07-22T15:45:04+00:00'
type: issue
status: closed
closed_at: '2017-07-22T15:45:04+00:00'
---

# Original Description
```
@anonimal       pigeons: I'll open a meta issue re: ^. All we need to do now is install Inno Setup on both win machines and have buildbot output an .exe instead of .zip when passing the `-f` switch in the bash script :)
```

- Inno Setup download [here](http://www.jrsoftware.org/isdl.php#stable)
- By default, our Inno Setup scripts will currently produce the filenames `KovriSetup32.exe` or `KovriSetup64.exe` but our bash installer will rename them to commit hash + platform + arch + date if filename is unspecified. This may or may not be desirable so we may want to keep what we're doing now with buildbot (`kovri-latest-win64.exe`, etc.)
- Referencing https://github.com/monero-project/kovri/pull/673

# Discussion History
## danrmiller | 2017-07-22T15:34:53+00:00
+resolved

# Action History
- Created by: anonimal | 2017-07-14T04:08:10+00:00
- Closed at: 2017-07-22T15:45:04+00:00
