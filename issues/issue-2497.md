---
title: OS X build error
source_url: https://github.com/monero-project/monero/issues/2497
author: jtgrassie
assignees: []
labels: []
created_at: '2017-09-20T19:24:25+00:00'
updated_at: '2018-03-31T07:11:41+00:00'
type: issue
status: closed
closed_at: '2017-09-21T12:26:53+00:00'
---

# Original Description
```
CMake Error at CMakeLists.txt:696 (message):
  Could not find required header zmq.hpp
```

# Discussion History
## moneromooo-monero | 2017-09-20T19:29:02+00:00
Do you have libzmq installed ?

## jtgrassie | 2017-09-20T19:31:05+00:00
Yes.
Should there be a cmake file to find it though (none in the cmake dir)?

## moneromooo-monero | 2017-09-20T19:35:07+00:00
I've no idea. I'll ping tewinget. 

## jtgrassie | 2017-09-20T19:38:21+00:00
My research suggests there should be: https://stackoverflow.com/questions/41251474/how-to-import-zeromq-libraries-in-cmake

## jtgrassie | 2017-09-20T19:42:47+00:00
And: http://zeromq.org/bindings:c

```
CMake: If you have installed libzmq to the standard library path (/usr/lib/) then in your CMakeLists.txt use the following

FIND_LIBRARY(ZMQ_LIB libzmq)
TARGET_LINK_LIBRARIES(myExecOrLib ${ZMQ_LIB})
```

Problem is, on Mac, it would most likely be installed to /opt/local/lib (MacPorts) or /usr/local/lib (homebrew).


## hyc | 2017-09-20T19:44:16+00:00
Well, CMakeLists.txt currently has `find_library(ZMQ_LIB zmq)`. I suppose you just need to set some env vars for CPPFLAGS and LDFLAGS if you want to search other paths.

## jtgrassie | 2017-09-20T19:47:14+00:00
My point is that a default build should work 'best effort' on supported platforms. That means expecting dependencies to be installed by systems common package manager. On OS X that is either MacPorts or Homebrew. Every other dependency (installed via MacPorts or Homebrew) is correctly being found. Not ZMQ.

## hyc | 2017-09-20T19:56:53+00:00
IMO it's the platform's responsibility to configure its tools with sane defaults. All the tools should check in /usr/local by default. If /opt is commonly used on a platform, then the platform tools should check that by default too. And then, if your particular system is ultra-customized, it's on you to -D overrides as needed.

## jtgrassie | 2017-09-20T20:03:51+00:00
camke and zmq fails with even /usr/local, only /usr works with no cmake helper file.

@hyc agreed. OS X common paths are certainly /opt/local and /usr/local. I've been away a couple of weeks so missed these ZMQ PRs.

## jtgrassie | 2017-09-20T20:08:57+00:00
Another observation: `find_path(ZMQ_INCLUDE_PATH zmq.hpp)`. This can be `zmq.h` not `.hpp`. So even when setting CMAKE_PREFIX_PATH to /opt/local, it's still not found and fails to build.

## hyc | 2017-09-20T20:09:54+00:00
Try this:
````
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 971c097..f0c12cf 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -689,8 +689,13 @@ endif()
 
 include(version.cmake)
 
-find_path(ZMQ_INCLUDE_PATH zmq.hpp)
-find_library(ZMQ_LIB zmq)
+if(APPLE)
+  find_path(ZMQ_INCLUDE_PATH zmq.hpp HINTS /usr/local /opt/local)
+  find_library(ZMQ_LIB zmq HINTS /usr/local /opt/local)
+else()
+  find_path(ZMQ_INCLUDE_PATH zmq.hpp)
+  find_library(ZMQ_LIB zmq)
+endif()
 
 if(NOT ZMQ_INCLUDE_PATH)
   message(FATAL_ERROR "Could not find required header zmq.hpp")
````

## jtgrassie | 2017-09-20T20:11:37+00:00
Still fails as zmq header is zmq.h not .hpp

## moneromooo-monero | 2017-09-20T20:12:38+00:00
Is it the right flie though ? It it's a different name, it's probably not it. Or someone's playing silly buggers.

## hyc | 2017-09-20T20:12:39+00:00
zmq.h is only the C header file. If you don't have zmq.hpp then you're still missing a dependency.

## iDunk5400 | 2017-09-20T20:13:38+00:00
Maybe you need the OSX equivalent of cppzmq. I think that is what provides zmq.hpp (the C++ header needed).

## jtgrassie | 2017-09-20T20:18:42+00:00
@iDunk5400 That was it. I tried zmq, then zmq-devel then your suggestion of cppzmq which worked (but only with env variable  CMAKE_PREFIX_PATH=/opt/local). So the path is still an issue. @hyc's patch above would fix.

## danrmiller | 2017-09-20T20:25:50+00:00
@iDunk5400 commented:
> Maybe you need the OSX equivalent of cppzmq. I think that is what provides zmq.hpp (the C++ header needed).

I also thought this was the case but @tewinget says here https://github.com/monero-project/monero/pull/2044#issuecomment-330445641 that "iirc the c++ bindings I chose to use come with libzmq (use newest) not cppzmq" when I mention using zmq.hpp from cppzmq.



## hyc | 2017-09-20T20:26:38+00:00
cmake --system-information on my box tells me
````
CMAKE_SYSTEM "Linux-4.4.0-62-generic"
CMAKE_SYSTEM_INCLUDE_PATH "/usr/include/w32api;/usr/X11R6/include;/usr/include/X11;/usr/pkg/include;/opt/csw/include;/opt/include;/usr/openwin/include"
CMAKE_SYSTEM_INFO_FILE "Platform/Linux"
CMAKE_SYSTEM_LIBRARY_PATH "/usr/lib/w32api;/usr/X11R6/lib;/usr/lib/X11;/usr/pkg/lib;/opt/csw/lib;/opt/lib;/usr/openwin/lib"
CMAKE_SYSTEM_LOADED "1"
CMAKE_SYSTEM_NAME "Linux"
CMAKE_SYSTEM_PREFIX_PATH "/usr/local;/usr;/;/usr;/usr/local"
````
If you've got /usr/local in your `CMAKE_SYSTEM_PREFIX_PATH` already then the hint should only need /opt/local. @jtgrassie perhaps you can PR the appropriate patch.

## jtgrassie | 2017-09-20T20:38:40+00:00
@hyc yes, good spot. I tried a fresh shell and it's in there. So it's just the dependency on cppzmq needed. Simple readme update of required dependencies. I've commented on #2044 as @danrmiller pointed out the specific PR with the incorrect assumption that latest libzmq includes the cpp bindings.

## jtgrassie | 2017-09-20T20:46:06+00:00
@iDunk5400 could you add the cppzmq to your readme PR with the zmq dependency?

## iDunk5400 | 2017-09-20T21:16:12+00:00
Added a note for OS X builds.

## danielbjornadal | 2017-09-23T20:59:46+00:00
This fixed it for me on ubuntu:xenial
`apt-get install -y libzmq-dev`

## bitkevin | 2017-09-25T09:54:14+00:00
After `apt-get install -y libzmq-dev`, I got error:

```
/usr/local/src/monero/src/rpc/zmq_server.cpp: In member function 'bool cryptonote::rpc::ZmqServer::addTCPSocket(std::__cxx11::string, std::__cxx11::string)':
/usr/local/src/monero/src/rpc/zmq_server.cpp:105:69: error: no matching function for call to 'zmq::socket_t::setsockopt(int, const int&)'
     rep_socket->setsockopt(ZMQ_RCVTIMEO, DEFAULT_RPC_RECV_TIMEOUT_MS);
                                                                     ^
In file included from /usr/local/src/monero/src/rpc/zmq_server.h:32:0,
                 from /usr/local/src/monero/src/rpc/zmq_server.cpp:29:
/usr/include/zmq.hpp:289:21: note: candidate: void zmq::socket_t::setsockopt(int, const void*, size_t)
         inline void setsockopt (int option_, const void *optval_,
                     ^
/usr/include/zmq.hpp:289:21: note:   candidate expects 3 arguments, 2 provided
```

## bitkevin | 2017-09-25T10:38:01+00:00
Finally, I use `apt-get install libzmq3-dev` to fix the issue on Ubuntu 16.04.

## Ulmo | 2017-11-11T18:51:08+00:00
For others like me who came here trying to figure out how to build in Homebrew in OS X:

The note of which @iDunk5400 speaks is in the file "README.md":

    *Note*: If cmake can not find zmq.hpp file on OS X, installing `zmq.hpp` from
    https://github.com/zeromq/cppzmq to `/usr/local/include` should fix that error.

I didn't figure out that that text would be away from the Homebrew text above it in the README.md file, so I found another solution first.  Here's another way to do it in Homebrew:

    https://github.com/Homebrew/homebrew-core/pull/4052

which says to:

    brew tap jmuncaster/homebrew-header-only

which of course means you then:

    brew install jmuncaster/header-only/cppzmq

I wonder why that isn't included in the original ZMQ, but since I only know C and that header file is a bunch of C++ code, I could see myself as a package maintainer not including code I don't understand, so I can see why this sort of thing sometimes happens.  I briefly read 0mq's purpose, and apparently, it's one of the first ideas I ever had when I was learning C, so that makes sense someone finally did it.  I could definitely see myself in the shoes of the person releasing 0mq without any darn messy C++ headers.

## dimalinux | 2017-11-13T06:49:23+00:00
If you are using MacPorts, this is the package you need.  There are 14 different zmq packages in MacPorts, so it's easy to pick the wrong one.
```
sudo port install cppzmq
```

## sammy007 | 2018-03-31T07:11:41+00:00
Why not just include this shit into repository? The brew maintainers recently added "official" monero formula and indeed it can't depend on other tap AFAIK. Simple file will fix everything.

# Action History
- Created by: jtgrassie | 2017-09-20T19:24:25+00:00
- Closed at: 2017-09-21T12:26:53+00:00
