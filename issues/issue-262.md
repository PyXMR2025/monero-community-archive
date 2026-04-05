---
title: Unnecessary CMake Version Requirement
source_url: https://github.com/xmrig/xmrig/issues/262
author: gordan-bobic
assignees: []
labels: []
created_at: '2017-12-13T20:06:42+00:00'
updated_at: '2017-12-16T12:27:55+00:00'
type: issue
status: closed
closed_at: '2017-12-16T12:27:55+00:00'
---

# Original Description
CMakeLists.txt header contains requirement for CMake 3.0 or later. This is unnecessary as no features exceeding what is provided by CMake 2.8 are used. Changing the first line accordingly allows xmrig to be build on EL7, which only ships with CMake 2.8.

# Discussion History
## xmrig | 2017-12-16T12:27:55+00:00
Fixed.

# Action History
- Created by: gordan-bobic | 2017-12-13T20:06:42+00:00
- Closed at: 2017-12-16T12:27:55+00:00
