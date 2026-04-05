---
title: .
source_url: https://github.com/xmrig/xmrig/issues/3029
author: openwrtfirmwarecostum
assignees: []
labels: []
created_at: '2022-04-17T14:39:40+00:00'
updated_at: '2022-09-24T15:48:58+00:00'
type: issue
status: closed
closed_at: '2022-04-18T13:16:42+00:00'
---

# Original Description
No description

# Discussion History
## Spudz76 | 2022-04-17T14:55:48+00:00
That is just how CMake works.  When you run `cmake` the present working directory should be the build directory, and the argument `..` is the source directory.

If you must launch from the source directory then you could use `cmake --build ./build .` but I think that still requires preparatory `mkdir build`  Notice how since the argument is the source path, and in this example we're in the source directory as present working directory, we gave single `.` rather than `..` and instead specified the build-dir since we're not presently working inside it as normally expected.

## Spudz76 | 2022-04-17T15:01:15+00:00
What sort of recipe are you using for OpenWRT.  Did you make a whole proper package?

## Spudz76 | 2022-04-18T12:44:40+00:00
[CMakeLists.txt line 240](https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L240)

```
target_link_libraries(${CMAKE_PROJECT_NAME} ${XMRIG_ASM_LIBRARY} ${OPENSSL_LIBRARIES} ${UV_LIBRARIES} ${EXTRA_LIBS} ${CPUID_LIB} ${ARGON2_LIBRARY} ${ETHASH_LIBRARY} ${GHOSTRIDER_LIBRARY} gcc_eh)
```

Should do it.

# Action History
- Created by: openwrtfirmwarecostum | 2022-04-17T14:39:40+00:00
- Closed at: 2022-04-18T13:16:42+00:00
