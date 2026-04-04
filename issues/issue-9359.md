---
title: Compilation errors on gcc 14.1.1
source_url: https://github.com/monero-project/monero/issues/9359
author: moneroexamples
assignees:
- '0xFFFC0000'
labels:
- bug
created_at: '2024-06-11T06:40:22+00:00'
updated_at: '2025-12-29T01:27:28+00:00'
type: issue
status: closed
closed_at: '2025-12-29T01:27:28+00:00'
---

# Original Description
Regarding:

> error: implicit declaration of function ‘strdup’; did you mean ‘strcmp’? [-Wimplicit-function-declaration]

and

> error: assignment to ‘char *’ from ‘int’ makes pointer from integer without a cast [-Wint-conversion]

```
/home/mwo/monero/external/miniupnp/miniupnpc/listdevices.c: In function ‘add_device’:
/home/mwo/monero/external/miniupnp/miniupnpc/listdevices.c:60:24: error: implicit declaration of function ‘strdup’; did you mean ‘strcmp’? [-Wimplicit-function-declaration]
   60 |         elt->descURL = strdup(dev->descURL);
      |                        ^~~~~~
      |                        strcmp
/home/mwo/monero/external/miniupnp/miniupnpc/listdevices.c:60:22: error: assignment to ‘char *’ from ‘int’ makes pointer from integer without a cast [-Wint-conversion]
   60 |         elt->descURL = strdup(dev->descURL);
      |                      ^
make[3]: *** [external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/build.make:76: external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/listdevices.c.o] Error 1
make[2]: *** [CMakeFiles/Makefile2:1307: external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/all] Error 2
make[1]: *** [Makefile:146: all] Error 2
make[1]: Leaving directory '/home/mwo/monero/build/release'
make: *** [Makefile:103: release-all] Error 2
```

# Discussion History
## SyntheticBird45 | 2024-06-11T14:04:05+00:00
Confirm, same issue on updated Arch Linux

## SyntheticBird45 | 2024-06-11T14:25:36+00:00
@selsta Applied pastebin modifications.
Failed at 24%:
```
[scrubbed]/monero/external/miniupnp/miniupnpc/src/minihttptestserver.c:299:25: error: implicit declaration of function 'usleep'; did you mean 'sleep'? [-Wimplicit-function-declaration]
  299 |                         usleep(10000); /* 10ms */
      |                         ^~~~~~
      |                         sleep
make[2]: *** [external/miniupnp/miniupnpc/CMakeFiles/minihttptestserver.dir/build.make:76: external/miniupnp/miniupnpc/CMakeFiles/minihttptestserver.dir/src/minihttptestserver.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:1341: external/miniupnp/miniupnpc/CMakeFiles/minihttptestserver.dir/all] Error 2
```

## SyntheticBird45 | 2024-06-11T15:36:25+00:00
Compiled successfully from https://github.com/selsta/monero/tree/miniupnpc-2.2.8

## 0xFFFC0000 | 2024-06-11T22:32:25+00:00
After adding a small print to  `src/p2p/CMakeLists.txt` :
```
get_cmake_property(_variableNames VARIABLES)
list (SORT _variableNames)
foreach (_variableName ${_variableNames})
    message(STATUS "${_variableName}=${${_variableName}}")
endforeach()

get_target_property(dirs miniupnpc::miniupnpc INCLUDE_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "miniupnpc::miniupnpc INCLUDE_DIRECTORIES='${dir}'")
endforeach()

get_target_property(dirs miniupnpc::miniupnpc INTERFACE_INCLUDE_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "miniupnpc::miniupnpc INTERFACE_INCLUDE_DIRECTORIES='${dir}'")
endforeach()

message(WARNING "p2p:")
get_target_property(dirs p2p INCLUDE_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "p2p INCLUDE_DIRECTORIES='${dir}'")
endforeach()
get_target_property(dirs p2p INTERFACE_INCLUDE_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "p2p INTERFACE_INCLUDE_DIRECTORIES='${dir}'")
endforeach()
```
you can see this output (even if you add `miniupnpc::miniupnpc` to `p2p` as dependency): 

```
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/external/rapidjson/include'
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/external/easylogging++'
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/src'
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/contrib/epee/include'
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/external'
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/external/supercop/include'
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='/opt/monero/build-release/x86_64-pc-linux-gnu/include'
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/build-release/generated_include'
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/build-release/translations'
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='$<BUILD_INTERFACE:/home/0xfffc/developments/monero/external/miniupnp/miniupnpc/include>'
-- miniupnpc::miniupnpc INCLUDE_DIRECTORIES='$<INSTALL_INTERFACE:include/miniupnpc>'
-- miniupnpc::miniupnpc INTERFACE_INCLUDE_DIRECTORIES='$<BUILD_INTERFACE:/home/0xfffc/developments/monero/external/miniupnp/miniupnpc/include>'
-- miniupnpc::miniupnpc INTERFACE_INCLUDE_DIRECTORIES='$<INSTALL_INTERFACE:include/miniupnpc>'
-- miniupnpc::miniupnpc INTERFACE_INCLUDE_DIRECTORIES='$<INSTALL_INTERFACE:include>'
CMake Warning at src/p2p/CMakeLists.txt:71 (message):
  p2p:
-- p2p INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/external/rapidjson/include'
-- p2p INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/external/easylogging++'
-- p2p INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/src'
-- p2p INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/contrib/epee/include'
-- p2p INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/external'
-- p2p INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/external/supercop/include'
-- p2p INCLUDE_DIRECTORIES='/opt/monero/build-release/x86_64-pc-linux-gnu/include'
-- p2p INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/build-release/generated_include'
-- p2p INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/build-release/translations'
-- p2p INCLUDE_DIRECTORIES='/opt/monero/build-release/x86_64-pc-linux-gnu/include'
-- p2p INCLUDE_DIRECTORIES='/home/0xfffc/developments/monero/external/db_drivers/liblmdb'
-- p2p INCLUDE_DIRECTORIES='/opt/monero/build-release/x86_64-pc-linux-gnu/include/hidapi'
-- p2p INCLUDE_DIRECTORIES='/opt/monero/build-release/x86_64-pc-linux-gnu/include'
-- p2p INCLUDE_DIRECTORIES='/opt/monero/build-release/x86_64-pc-linux-gnu/include/libusb-1.0'
-- p2p INCLUDE_DIRECTORIES='/opt/monero/build-release/x86_64-pc-linux-gnu/include'
-- p2p INTERFACE_INCLUDE_DIRECTORIES='dirs-NOTFOUND'
```


It is obvious for some reason the include path from `miniupnpc::miniupnpc` does not propagate to the `p2p` target. 

And this is the PR causing it: https://github.com/miniupnp/miniupnp/pull/559

## 0xFFFC0000 | 2024-06-13T10:44:08+00:00
In case you want to take a look at early PR, this one is a complete fix, other than a few minor issues I expect it to work without issue https://github.com/0xFFFC0000/monero/pull/23

Once it passed all the tests, I will submit a PR.

## SyntheticBird45 | 2024-06-13T10:48:09+00:00
@0xFFFC0000 testing

## SyntheticBird45 | 2024-06-13T10:53:32+00:00
@0xFFFC0000 unable to compile from your branch. Still have error: `external/miniupnp/miniupnpc/src/minihttptestserver.c:299:25: error: implicit declaration of function 'usleep'; did you mean 'sleep'? [-Wimplicit-function-declaration]`

What I did:
```
$ git clone https://github.com/0xFFFC0000/monero -b dev/0xfffc/new-miniupnpc && cd monero/
$ git submodule update --init --force
$ make -j 8
```

## 0xFFFC0000 | 2024-06-13T10:57:24+00:00
Yes. That is their error. Not ours. Even if you compile `miniupnpc` in separate environment with same compiler, you will hit it.  ( in your spare time please try it if possible and let me know )

Let me double check though, I will find a workaround. 

## 0xFFFC0000 | 2024-06-13T11:05:35+00:00
> @0xFFFC0000 unable to compile from your branch. Still have error: `external/miniupnp/miniupnpc/src/minihttptestserver.c:299:25: error: implicit declaration of function 'usleep'; did you mean 'sleep'? [-Wimplicit-function-declaration]`
> 
> What I did:
> 
> ```
> $ git clone https://github.com/0xFFFC0000/monero -b dev/0xfffc/new-miniupnpc && cd monero/
> $ git submodule update --init --force
> $ make -j 8
> ```

Do you use Element? or IRC? 

## 0xFFFC0000 | 2024-06-13T12:16:41+00:00
```
if(NOT MSVC)              
  add_compile_options(-D_GNU_SOURCE)
endif()
```

Fixed the issue. Now we have updated `miniupnpc` and fixed this compilation issue. 

## gus4rs | 2024-08-25T18:53:28+00:00
A workaround to compile Monero on Fedora 40 (that ships with gcc 14.x):

```
dnf install -y gcc13-c++
CC="gcc-13" CXX="g++-13" make -j8 release
 ```

## preland | 2024-11-16T00:31:15+00:00
An equivalent workaround to @gus4rs's for Debian/Ubuntu  (I think this is only an issue for Debian sid, though I'm not sure if trixie or newer ubuntu ships with gcc 14.x) : 

```
apt install -y gcc-13 g++-13
CC="gcc-13" CXX="g++-13" make -j8 release
```

# Action History
- Created by: moneroexamples | 2024-06-11T06:40:22+00:00
- Closed at: 2025-12-29T01:27:28+00:00
