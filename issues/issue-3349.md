---
title: Docker build crash
source_url: https://github.com/monero-project/monero/issues/3349
author: alextaaa
assignees: []
labels: []
created_at: '2018-03-05T07:55:37+00:00'
updated_at: '2018-09-12T08:40:58+00:00'
type: issue
status: closed
closed_at: '2018-09-12T08:40:58+00:00'
---

# Original Description
I try to use `docker build -t monero .` in stable branch `release-v0.11.0.0`

But I get the error:

```
-- Could not find GNU readline library so building without readline support
CMake Error at CMakeLists.txt:847 (message):
  Could not find required header zmq.hpp


-- Configuring incomplete, errors occurred!
See also "/usr/local/src/monero/build/release/CMakeFiles/CMakeOutput.log".
See also "/usr/local/src/monero/build/release/CMakeFiles/CMakeError.log".
Makefile:68: recipe for target 'release-static' failed
make: *** [release-static] Error 1
The command '/bin/sh -c make -j$(nproc) release-static' returned a non-zero code: 2
```

# Discussion History
## moneromooo-monero | 2018-03-05T11:50:53+00:00
I see no crash here.

As for your build error, install zmq.hpp.


## alextaaa | 2018-03-05T12:13:26+00:00
But I use the Dockerfile `https://github.com/monero-project/monero/blob/release-v0.11.0.0/Dockerfile`

Could you plz include all required command (like this `install zmq.hpp`) for successfully build?

## MoroccanMalinois | 2018-03-05T16:51:29+00:00
@alextaaa The Dockerfile you are using is pulling code from branch master (even if you cloned from another branch), and zmq has been added since v0.11.0.0. 

So easiest solution is to just add ` -b release-v0.11.0.0` to https://github.com/monero-project/monero/blob/release-v0.11.0.0/Dockerfile#L19.

Or you could use branch `master` with #3316 (whose Dockerfile include commands to rebuild all dependencies, but it will probably not work with branch v0.11 because of the `-fPIC` build).


## homdx | 2018-06-11T21:28:41+00:00
My commit is fix you issue?
https://github.com/monero-project/monero/pull/3879

## moneromooo-monero | 2018-09-12T08:35:26+00:00
I'll call that fixed since several people built this since the fix.

+resolved


# Action History
- Created by: alextaaa | 2018-03-05T07:55:37+00:00
- Closed at: 2018-09-12T08:40:58+00:00
