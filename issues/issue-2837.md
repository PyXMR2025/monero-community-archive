---
title: Cannot configure build without libreadline
source_url: https://github.com/monero-project/monero/issues/2837
author: danrmiller
assignees: []
labels:
- cmake
created_at: '2017-11-17T16:35:00+00:00'
updated_at: '2017-11-27T22:40:28+00:00'
type: issue
status: closed
closed_at: '2017-11-27T22:40:28+00:00'
---

# Original Description
If libreadline isn't present, cmake does not complete configuring the build.

```
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Readline_LIBRARY (ADVANCED)
    linked by target "simplewallet" in directory /mnt/buildbot/buildbot/slave/monero-static-debian-armv8/build/src/simplewallet
    linked by target "daemon" in directory /mnt/buildbot/buildbot/slave/monero-static-debian-armv8/build/src/daemon
-- Configuring incomplete, errors occurred!
See also "/mnt/buildbot/buildbot/slave/monero-static-debian-armv8/build/build/release/CMakeFiles/CMakeOutput.log".
See also "/mnt/buildbot/buildbot/slave/monero-static-debian-armv8/build/build/release/CMakeFiles/CMakeError.log".
Makefile:88: recipe for target 'release-static-linux-armv8' failed
make: *** [release-static-linux-armv8] Error 1
```
For example: https://build.getmonero.org/builders/monero-static-debian-armv8/builds/2449/steps/compile/logs/stdio

# Discussion History
## danrmiller | 2017-11-17T16:35:11+00:00
+cmake

## jtgrassie | 2017-11-18T11:08:11+00:00
Can you try running cmake with `-DUSE_READLINE=OFF`

## moneromooo-monero | 2017-11-19T09:28:48+00:00
https://github.com/monero-project/monero/pull/2841

## danrmiller | 2017-11-19T17:32:36+00:00
2841 works for me thanks.

## moneromooo-monero | 2017-11-27T22:33:20+00:00
+resolved

# Action History
- Created by: danrmiller | 2017-11-17T16:35:00+00:00
- Closed at: 2017-11-27T22:40:28+00:00
