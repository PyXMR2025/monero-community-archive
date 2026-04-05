---
title: Cannot build - MHD_LIBRARY (ADVANCED) NOTFOUND
source_url: https://github.com/xmrig/xmrig/issues/349
author: robme
assignees: []
labels:
- bug
created_at: '2018-01-18T10:34:49+00:00'
updated_at: '2018-01-19T18:38:54+00:00'
type: issue
status: closed
closed_at: '2018-01-19T18:38:54+00:00'
---

# Original Description
I cannot build the newer versions. I tried with

`cmake .. -DWITH_HTTPD=OFF`

I get the error:

> CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
> Please set them or make sure they are set and tested correctly in the CMake files:
> MHD_LIBRARY (ADVANCED)
>     linked by target "xmrig" in directory xmrig-2.4.4
>
> -- Configuring incomplete, errors occurred!

This is on Ubuntu. I have installed all the packages as well, including libmicrohttpd-dev.

# Discussion History
## robme | 2018-01-18T10:38:56+00:00
I managed to build it by modifying the last line of CMakeLists.txt and removing ${MHD_LIBRARY}:

`target_link_libraries(xmrig ${UV_LIBRARIES} ${EXTRA_LIBS} ${CPUID_LIB})`


## xmrig | 2018-01-19T18:38:31+00:00
Fixed now https://github.com/xmrig/xmrig/pull/324
This issue caused because cmake cache, fresh cmake run (without exists files/previous runs) with `-DWITH_HTTPD=OFF` should work ok anyway.
Thank you.

# Action History
- Created by: robme | 2018-01-18T10:34:49+00:00
- Closed at: 2018-01-19T18:38:54+00:00
