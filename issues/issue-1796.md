---
title: Update build instructions for Fedora 32
source_url: https://github.com/xmrig/xmrig/issues/1796
author: agentpatience
assignees: []
labels: []
created_at: '2020-08-02T14:56:45+00:00'
updated_at: '2020-08-02T18:28:52+00:00'
type: issue
status: closed
closed_at: '2020-08-02T18:28:52+00:00'
---

# Original Description
Hi,

I am trying to get XMRIG installed on Fedora 32.

The build instructions for Fedora are for older versions and don't completely work properly:

https://github.com/xmrig/xmrig/wiki/Fedora-Build

If I follow those directions the user will get this error:

[root@bigdaddy build]# cmake ..
CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
See also "/root/xmrig/build/CMakeFiles/CMakeOutput.log".

The system is: Linux - 5.7.11-200.fc32.x86_64 - x86_64

It complains because there is an issue the script is having trying to find compiler paths.

GCC on Fedora 32 resides in  /usr/bin/gcc
 
Additional packages needed: hwloc-devel and openssl-devel


What is the proper way to solve this?








# Discussion History
## agentpatience | 2020-08-02T16:39:20+00:00
Seems that installing make on Fedora allows it to configure.





# Action History
- Created by: agentpatience | 2020-08-02T14:56:45+00:00
- Closed at: 2020-08-02T18:28:52+00:00
