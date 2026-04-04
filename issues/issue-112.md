---
title: 'Buildbot: OpenBSD static build failing for Kovri'
source_url: https://github.com/monero-project/meta/issues/112
author: anonimal
assignees: []
labels: []
created_at: '2017-08-25T00:46:12+00:00'
updated_at: '2018-07-15T22:51:18+00:00'
type: issue
status: closed
closed_at: '2018-07-15T22:51:18+00:00'
---

# Original Description
A long-standing issue, ticketing for housekeeping.

Details on how the boost libs were built are needed.

https://build.getmonero.org/builders/kovri-static-openbsd-amd64.

This hack fixes the build but it shouldn't be necessary (even if refactored for openbsd-only):

```diff
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 1ae0f16..b2ec78f 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -200,7 +200,7 @@ if(NOT Boost_FOUND)
   message(FATAL_ERROR "Boost not found or requirement not satisfied. See building instructions.")
 else()
   message(STATUS "Found Boost: ${Boost_INCLUDE_DIR}, ${Boost_LIBRARIES}")
-  if(NOT WITH_STATIC)
+  if(WITH_STATIC)
     add_definitions(-DBOOST_ALL_DYN_LINK)
   endif()
   include_directories(${Boost_INCLUDE_DIRS})
```

# Discussion History
## danrmiller | 2017-10-11T00:52:15+00:00
Boost 1.63.0 from: https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.tar.bz2/download

Patches:

https://svn.boost.org/trac10/attachment/ticket/12575/boost-1.62-asio-libressl.patch

https://gist.githubusercontent.com/laanwj/bf359281dc319b8ff2e1/raw/92250de8404b97bb99d72ab898f4a8cb35ae1ea3/patch-boost_test_impl_execution_monitor_ipp.patch

```echo 'using gcc : : eg++ : "-fvisibility=hidden -fPIC" "" "ar" "strip"  "ranlib" "" : ;' > user-config.jam```

```./bootstrap.sh --without-icu --with-libraries=serialization,chrono,log,program_options,date_time,thread,system,filesystem,regex,test```   
(serialization, date_time, and regex modules are needed by monero)

```./b2 -d2 -d1 runtime-link=shared threadapi=pthread threading=multi link=shared,static variant=release  --layout=tagged --build-type=complete --user-config=user-config.jam -sNO_BZIP2=1 stage```

```sudo ./b2 -d0 runtime-link=shared threadapi=pthread threading=multi link=shared,static variant=release --layout=tagged --build-type=complete --user-config=user-config.jam -sNO_BZIP2=1 install```

Latest attempt: https://build.getmonero.org/builders/kovri-static-openbsd-amd64/builds/230/steps/compile/logs/stdio2 

(Maybe something with the b2 link settings?)


## danrmiller | 2017-10-11T16:11:37+00:00
Also verified that if only the static boost libs are present and the shared ones are not, the static build works fine.

## anonimal | 2018-04-24T03:34:43+00:00
Should be resolved once https://github.com/monero-project/kovri/pull/842 is merged (includes in-tree updated findboost which should be formally resolved with #201).

## anonimal | 2018-06-28T23:24:06+00:00
Was resolved by the in-tree FindBoost.cmake but now the build machine itself needs more memory. https://build.getmonero.org/builders/kovri-static-openbsd-amd64/builds/473/steps/compile/logs/stdio

## danrmiller | 2018-07-14T16:33:58+00:00
@anonimal I gave that machine 6 Gigs of RAM and it still runs out compiling kovri. I'll add a larger swap disk.

## danrmiller | 2018-07-14T17:03:11+00:00
@anonimal Same issue, made sure the user was in staff group to have less restrictions such as datasize in login.conf, etc. Will move on to the next issue for you and come back to this later in several hours.

## danrmiller | 2018-07-14T23:59:01+00:00
Switched the compiler to the same one the dynamic lib build was using.

https://build.getmonero.org/builders/kovri-static-openbsd-amd64/builds/493


## anonimal | 2018-07-15T22:51:18+00:00
>Switched the compiler to the same one the dynamic lib build was using.

Awesome, thanks.

# Action History
- Created by: anonimal | 2017-08-25T00:46:12+00:00
- Closed at: 2018-07-15T22:51:18+00:00
