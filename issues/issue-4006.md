---
title: 'Docker build broken. Makefile:76: recipe for target ''release-static'' failed'
source_url: https://github.com/monero-project/monero/issues/4006
author: j4ys0n
assignees: []
labels:
- duplicate
created_at: '2018-06-15T21:58:17+00:00'
updated_at: '2018-06-16T10:00:53+00:00'
type: issue
status: closed
closed_at: '2018-06-16T10:00:53+00:00'
---

# Original Description
Steps to reproduce:

Pull repo. `docker build -t xmr .`

Error:
```
-- Found Boost Version: 106600
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.11") 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring incomplete, errors occurred!
See also "/src/build/release/CMakeFiles/CMakeOutput.log".
See also "/src/build/release/CMakeFiles/CMakeError.log".
Makefile:76: recipe for target 'release-static' failed
make: *** [release-static] Error 1
```

# Discussion History
## moneromooo-monero | 2018-06-16T09:56:13+00:00
#3563
+duplicate


# Action History
- Created by: j4ys0n | 2018-06-15T21:58:17+00:00
- Closed at: 2018-06-16T10:00:53+00:00
