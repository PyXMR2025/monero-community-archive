---
title: Could not compile on clang due to atomic library not present (on Raspberry
  Pi)
source_url: https://github.com/monero-project/monero/issues/4677
author: TheQuantumPhysicist
assignees: []
labels: []
created_at: '2018-10-20T20:20:12+00:00'
updated_at: '2018-10-26T21:09:00+00:00'
type: issue
status: closed
closed_at: '2018-10-26T21:09:00+00:00'
---

# Original Description
So I tried to compile Monero on Raspberry Pi 2 (Raspbian Stretch) in debug mode. On `g++`, this definitely didn't work, and the virtual memory of g++ was exhausted (yes, whole 4 GB were out during compilation). Now since I know that clang consumes less memory, I decided to try it. So I forced Monero to use clang 6.0, and... it compiles!

But...

At first it didn't work. I got an error that some "Atomic" library was "NOTFOUND". Then I investigated the cmake file and found that there's a condition to add some atomic library for clang:

```
if(CMAKE_C_COMPILER_ID STREQUAL "Clang" AND ARCH_WIDTH EQUAL "32" AND NOT IOS AND NOT FREEBSD)
  find_library(ATOMIC atomic)
  list(APPEND EXTRA_LIBRARIES ${ATOMIC})
endif()
```

I don't know what these lines are for, but since clang++ 6 definitely supports C++11 (which already natively contain the atomic stuff that are used in Monero), and since cmake already forces C++11 to be supported, I decided to remove these lines. So I removed them, and it compiles with no problem.

Is this a bug? Should these lines be removed?

# Discussion History
## moneromooo-monero | 2018-10-20T20:31:33+00:00
It should presumably only append the lib if it's found, like:

<pre>
if(CMAKE_C_COMPILER_ID STREQUAL "Clang" AND ARCH_WIDTH EQUAL "32" AND NOT IOS AND NOT FREEBSD)
  find_library(ATOMIC atomic)
  if (ATOMIC_FOUND)
    list(APPEND EXTRA_LIBRARIES ${ATOMIC})
  endif()
endif()
</pre>

Does this work ?


## TheQuantumPhysicist | 2018-10-20T21:33:30+00:00
Yes. These changes make it work.

Feel free to close this issue. I don't know if you want postpone this until the change is is committed (or if you want me to make a pull-request).

Best.

## moneromooo-monero | 2018-10-20T21:35:35+00:00
Please leave this open, I'll close when the fix is merged.

## moneromooo-monero | 2018-10-26T20:52:57+00:00
+resolved

# Action History
- Created by: TheQuantumPhysicist | 2018-10-20T20:20:12+00:00
- Closed at: 2018-10-26T21:09:00+00:00
