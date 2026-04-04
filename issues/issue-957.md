---
title: Boost issue when trying to make
source_url: https://github.com/monero-project/monero/issues/957
author: kirkins
assignees: []
labels: []
created_at: '2016-08-12T05:46:26+00:00'
updated_at: '2016-08-20T03:40:02+00:00'
type: issue
status: closed
closed_at: '2016-08-20T03:40:01+00:00'
---

# Original Description
I'm trying to make monero on centos 7.2. I have boost installed but I get back this:

```

[red@datasci bitmonero]$ sudo make release-static-64
mkdir -p build/release
cd build/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Could not find libunwind (missing:  LIBUNWIND_INCLUDE_DIR LIBUNWIND_LIBRARIES) 
-- Stack trace on exception disabled
-- Could not find miniupnp
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
-- Using 64-bit LMDB from source tree
-- AES support enabled
CMake Error at /usr/share/cmake/Modules/FindBoost.cmake:1096 (message):
  Unable to find the requested Boost libraries.

  Unable to find the Boost header files.  Please set BOOST_ROOT to the root
  directory containing Boost or BOOST_INCLUDEDIR to the directory containing
  Boost's headers.
Call Stack (most recent call first):
  CMakeLists.txt:451 (find_package)


CMake Error at CMakeLists.txt:45 (message):
  Could not find Boost libraries, please make sure you have installed
  Boost or libboost-all-dev (1.53 or 1.55+) or the equivalent
Call Stack (most recent call first):
  CMakeLists.txt:455 (die)


-- Configuring incomplete, errors occurred!

```


# Discussion History
## anonimal | 2016-08-12T11:03:55+00:00
> Unable to find the Boost header files.  Please set BOOST_ROOT to the root
> directory containing Boost or BOOST_INCLUDEDIR to the directory containing
> Boost's headers.

So, you can try something like this:

``` bash
$ BOOST_ROOT=/usr/local/
$ export BOOST_ROOT
```

Replacing your `BOOST_ROOT` as appropriate, then running make again.

Does that work?


## kirkins | 2016-08-12T18:30:00+00:00
I'm trying this based on what you said (/usr/include/boost seems to be where boost is located):

`BOOST_ROOT=/usr/include/boost
export BOOST_ROOT`

Getting the same results.


## guzzijones | 2016-08-12T22:53:33+00:00
is /user/include part of your path?

On 8/12/2016 1:46 AM, kirkins wrote:

> I'm trying to make monero on cent 7.2. I have boost installed but I get
> back this:
> 
> |[red@datasci bitmonero]$ sudo make release-static-64 mkdir -p
> build/release cd build/release && cmake -D STATIC=ON -D ARCH="x86-64" -D
> BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. && make -- Could not find
> DEVELOPER_LOCAL_TOOLS in env (not required) -- BOOST_IGNORE_SYSTEM_PATHS
> defaults to OFF -- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not
> required) -- Building for a 64-bit system -- Could not find DATABASE in
> env (not required unless you want to change database type from default:
> lmdb) -- Using LMDB as default DB type -- Could not find libunwind
> (missing: LIBUNWIND_INCLUDE_DIR LIBUNWIND_LIBRARIES) -- Stack trace on
> exception disabled -- Could not find miniupnp -- Using miniupnpc from
> local source tree for static build -- Looking for libunbound -- Using
> 64-bit LMDB from source tree -- AES support enabled CMake Error at
> /usr/share/cmake/Modules/FindBoost.cmake:1096 (message): Unable to find
> the requested Boost libraries. Unable to find the Boost header files.
> Please set BOOST_ROOT to the root directory containing Boost or
> BOOST_INCLUDEDIR to the directory containing Boost's headers. Call Stack
> (most recent call first): CMakeLists.txt:451 (find_package) CMake Error
> at CMakeLists.txt:45 (message): Could not find Boost libraries, please
> make sure you have installed Boost or libboost-all-dev (1.53 or 1.55+)
> or the equivalent Call Stack (most recent call first):
> CMakeLists.txt:455 (die) -- Configuring incomplete, errors occurred! |
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> https://github.com/monero-project/bitmonero/issues/957, or mute the
> thread
> https://github.com/notifications/unsubscribe-auth/ALPZoUc5NDZ1uRyWNgZ5qwK5mp6Q5sL_ks5qfAi1gaJpZM4Jiyv1.


## kirkins | 2016-08-13T20:33:30+00:00
I think you mean '/user/include'. It wasn't in my path. I've since tried adding it and rebooted the server.

Still the same error.


## guzzijones | 2016-08-13T21:05:22+00:00
If you are on linux it is /usr

Enviado con Aquamail para Android
http://www.aqua-mail.com

El 13 de agosto de 2016 4:33:36 PM kirkins notifications@github.com escribio:

> I think you mean '/user/include'. It wasn't in my path. I've since tried 
> adding it and rebooted the server.
> 
> Still the same error.
> 
> ## 
> 
> You are receiving this because you commented.
> Reply to this email directly or view it on GitHub:
> https://github.com/monero-project/bitmonero/issues/957#issuecomment-239640195


## guzzijones | 2016-08-14T01:32:25+00:00
I just had the same issue after installing a self compiled verison of boost.

I had to do:
export BOOST_ROOT=[path to boost root];   mine was /usr/local
make clean
make

for some reason cmake was remembering i previously had built with the 
system version of boost.

good luck

On 8/13/2016 4:33 PM, kirkins wrote:

> I think you mean '/user/include'. It wasn't in my path. I've since tried
> adding it and rebooted the server.
> 
> Still the same error.
> 
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> https://github.com/monero-project/bitmonero/issues/957#issuecomment-239640195,
> or mute the thread
> https://github.com/notifications/unsubscribe-auth/ALPZoecBOVWwt_TTziscgZfiNQYTo4XMks5qfiodgaJpZM4Jiyv1.


## guzzijones | 2016-08-20T03:35:49+00:00
Is this issue closed?  
Did you try  

```
$ export BOOST_ROOT=/usr/local
$ make clean
$ make
```


## kirkins | 2016-08-20T03:40:01+00:00
I gave up and switched back to debian so I'll close this.


# Action History
- Created by: kirkins | 2016-08-12T05:46:26+00:00
- Closed at: 2016-08-20T03:40:01+00:00
