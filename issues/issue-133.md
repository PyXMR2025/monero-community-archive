---
title: Failing to compile
source_url: https://github.com/xmrig/xmrig/issues/133
author: SecretMNC
assignees: []
labels:
- question
created_at: '2017-10-02T06:51:39+00:00'
updated_at: '2018-03-14T22:53:55+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:53:55+00:00'
---

# Original Description
On Xubuntu, trying to compile the source code.  I attempt to cmake on the top level folder with this command:

`miningrig@miningrig-MS-7640:~/Desktop/Crypto/xmrig-2.3.1/cmake/build$ cmake ../..`

And the following occurs:

```
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is unknown
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
See also "/home/miningrig/Desktop/Crypto/xmrig-2.3.1/cmake/build/CMakeFiles/CMakeOutput.log".
See also "/home/miningrig/Desktop/Crypto/xmrig-2.3.1/cmake/build/CMakeFiles/CMakeError.log".
```



# Discussion History
## xmrig | 2017-10-02T07:02:44+00:00
Looks like you only have C compiler (gcc), but no C++ compiler (g++).
Thank you.

# Action History
- Created by: SecretMNC | 2017-10-02T06:51:39+00:00
- Closed at: 2018-03-14T22:53:55+00:00
