---
title: Support debug builds on Windows
source_url: https://github.com/monero-project/monero-gui/issues/4081
author: elibroftw
assignees: []
labels: []
created_at: '2022-12-03T19:55:19+00:00'
updated_at: '2022-12-04T05:48:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```sh
make -j9 debug-static-win64
```

Results in 

<details>
<summary>log</summary>

```sh
mkdir -p build/debug && cd build/debug && cmake -D STATIC=ON -G "MSYS Makefiles" -D DEV_MODE=ON -DMANUAL_SUBMODULES=OFF -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Debug -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=C:/msys64 -D MINGW=ON ../.. && make
-- Initiating compile using CMake 3.25.1
HEAD is now at 9367b432f Merge pull request #8635
Synchronizing submodule url for 'external/miniupnp'
Synchronizing submodule url for 'external/randomx'
Synchronizing submodule url for 'external/rapidjson'
Synchronizing submodule url for 'external/rapidjson/thirdparty/gtest'
Synchronizing submodule url for 'external/supercop'
Synchronizing submodule url for 'external/trezor-common'
Synchronizing submodule url for 'external/trezor-common/defs/ethereum/tokens'
Submodule path 'external/miniupnp': checked out '544e6fcc73c5ad9af48a8985c94f0f1d742ef2e0'
Submodule path 'external/randomx': checked out '261d58c77fc5547c0aa7fdfeb58421ba7e0e6e1c'
Submodule path 'external/rapidjson': checked out '129d19ba7f496df5e33658527a7158c79b99c21c'
Submodule path 'external/rapidjson/thirdparty/gtest': checked out '0a439623f75c029912728d80cb7f1b8b48739ca4'
Submodule path 'external/supercop': checked out '633500ad8c8759995049ccd022107d1fa8a1bbc9'
Submodule path 'external/trezor-common': checked out 'bff7fdfe436c727982cc553bdfb29a9021b423b0'
Submodule path 'external/trezor-common/defs/ethereum/tokens': checked out '88414ef852e21279f217d2f3f8fd439cd7c5fd9f'
-- CMake version 3.25.1
-- Found ccache C:/msys64/usr/bin/ccache.exe, but is UNUSABLE! Return code: FALSE
-- Building build tag win-x64
-- Checking submodules
-- Submodule 'external/miniupnp' is up-to-date
-- Submodule 'external/rapidjson' is up-to-date
-- Submodule 'external/trezor-common' is up-to-date
-- Submodule 'external/randomx' is up-to-date
-- Submodule 'external/supercop' is up-to-date
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Building for a 64-bit system
-- Building internal libraries as static
-- MSYS location: C:/msys64
-- Using LMDB as default DB type
-- looking for liblzma
-- liblzma found
-- Could not find libunwind (missing: LIBUNWIND_INCLUDE_DIR)
-- Stack trace on exception disabled
-- Using OpenSSL include dir at C:/msys64/mingw64/include
CMake Warning (dev) at C:/msys64/mingw64/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (MiniUPnPc)
  does not match the name of the calling package (Miniupnpc).  This can lead
  to problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  monero/cmake/FindMiniupnpc.cmake:39 (find_package_handle_standard_args)
  monero/external/CMakeLists.txt:38 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY)
-- Using in-tree miniupnpc
-- Looking for libunbound
CMake Error at monero/CMakeLists.txt:113 (message):
  Could not find libunbound
Call Stack (most recent call first):
  monero/external/CMakeLists.txt:59 (die)


-- Configuring incomplete, errors occurred!
See also "C:/Users/maste/Documents/GitHub/monero-gui/build/debug/CMakeFiles/CMakeOutput.log".
See also "C:/Users/maste/Documents/GitHub/monero-gui/build/debug/CMakeFiles/CMakeError.log".make: *** [Makefile:60: debug-static-win64] Error 1
```
</details>

by thoughts: `libunbound` is not installed via current instructions.

# Discussion History
## elibroftw | 2022-12-03T20:14:35+00:00
mingw-w64-x86_64-unbound

## elibroftw | 2022-12-03T20:26:06+00:00
I solved the previous error, but got
```
CMake Error at CMakeLists.txt:291 (find_library):
  Could not find qtquicktemplates2plugin_LIBRARY using the following names:
  qtquicktemplates2plugin
```

## selsta | 2022-12-03T21:17:20+00:00
And when you try `make -j9 release-static-win64` ?

## elibroftw | 2022-12-03T21:58:19+00:00
<details>
<summary>output</summary>

```
make release-static-win64
mkdir -p build/release && cd build/release && cmake -D STATIC=ON -G "MSYS Makefiles" -D DEV_MODE=OFF -DMANUAL_SUBMODULES=OFF -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=C:/msys64 -D MINGW=ON ../.. && make
-- The C compiler identification is GNU 12.2.0
-- The CXX compiler identification is GNU 12.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: C:/msys64/mingw64/bin/x86_64-w64-mingw32-gcc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: C:/msys64/mingw64/bin/x86_64-w64-mingw32-g++.exe - 
skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Initiating compile using CMake 3.25.1
-- Found Git: C:/msys64/usr/bin/git.exe (found version "2.38.1") 
-- Checking submodules
CMake Error at CMakeLists.txt:41 (message):
  Submodule 'monero' is not using the checked head.  Please update all
  submodules with

  git submodule update --init --force --recursive

  or run cmake with -DMANUAL_SUBMODULES=1,

   or if you want to build from latest master run cmake with -DDEV_MODE=ON,
   or run make devmode
Call Stack (most recent call first):
  CMakeLists.txt:45 (check_submodule)


-- Configuring incomplete, errors occurred!
See also "C:/Users/maste/Documents/GitHub/monero-gui/build/release/CMakeFiles/CMakeOutput.log".
make: *** [Makefile:67: release-static-win64] Error 1
```
</details>

## selsta | 2022-12-03T21:59:48+00:00
git submodule update --init --force --recursive

## elibroftw | 2022-12-03T22:04:44+00:00
Same error
<details>
<summary>Output</summary>

```bash
...OTHER STUFF HERE
-- Initiating static build
-- Found Git: C:/msys64/usr/bin/git.exe
-- You are currently on commit 74b151991
-- You are ahead of or behind a tagged release
-- C:/Users/maste/Documents/GitHub/monero-gui/cmake
-- libsodium: libraries at C:/msys64/mingw64/lib/libsodium.a
-- Checking for modules 'Qt5Core;Qt5Quick;Qt5Gui;Qt5Qml;Qt5Svg;Qt5Xml;Qt5QmlModels;Qt5XmlPatterns'
--   Found Qt5Core, version 5.15.7
--   Found Qt5Quick, version 5.15.7
--   Found Qt5Gui, version 5.15.7
--   Found Qt5Qml, version 5.15.7
--   Found Qt5Svg, version 5.15.7
--   Found Qt5Xml, version 5.15.7
--   Found Qt5QmlModels, version 5.15.7
--   Found Qt5XmlPatterns, version 5.15.7
CMake Error at CMakeLists.txt:291 (find_library):
  Could not find qtquicktemplates2plugin_LIBRARY using the following names:
  qtquicktemplates2plugin


-- Configuring incomplete, errors occurred!
See also "C:/Users/maste/Documents/GitHub/monero-gui/build/release/CMakeFiles/CMakeOutput.log".
See also "C:/Users/maste/Documents/GitHub/monero-gui/build/release/CMakeFiles/CMakeError.log".
make: *** [Makefile:67: release-static-win64] Error 1
```
</details>

## elibroftw | 2022-12-03T22:06:29+00:00
If its relevant, I cloned in Windows first and then used MSYS2 64Bit in the directory.

## selsta | 2022-12-03T22:07:29+00:00
https://github.com/monero-project/monero-gui#building-on-windows

The README says to build `release-win64` and not static. I don't use Windows myself but try if that works.

## elibroftw | 2022-12-03T22:08:15+00:00
You told me to build release-static-win64. very well I'll try release-win64.

> And when you try `make -j9 release-static-win64` ?



## selsta | 2022-12-03T22:12:44+00:00
I'm not a Windows user and I assumed you followed the README instructions?

## selsta | 2022-12-03T22:13:18+00:00
But if you are annoyed that I didn't solve your issue instantly maybe someone else can help instead.

## elibroftw | 2022-12-03T22:14:02+00:00
I'm not annoyed, I'm only asking because I already spent 2 hours debugging. I'm not building just for the sake of building, I'm trying to finish that PR.

## elibroftw | 2022-12-03T22:28:15+00:00
build failed first time I ran `make -j9 release-win64`, second time also failed but easier to read.
<details>
<summary>output</summary>

```
[ 89%] Automatic MOC and UIC for target monero-wallet-gui
[ [ 89%] B89u%i]l di[Bn ug9i 0lCd%Xi]Xn  gBo ubCijXleXdc iton bgmj oeCncXetXr  omo/obsnjreecrc/otd/ asmeromcno/endr/aoCe/Mmsaorknce//FCdiMalaeekmseo/Fndi/alCeemMosan/k.dedaiFerm/iodlnae.desimro//dcnao.emcmmpoapnn..dod_bisjre
/rmvaeirn..ccpppp..oobbjj

In file included from C:/msys64/mingw64/include/windows.h:70,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/external/easylogging++/easylogging++.h:394,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/misc_log_ex.h:35,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/include_base_utils.h:32,       
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/simplewallet/simplewallet.cpp:53:
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/console_handler.h: In member function 'bool epee::async_stdin_reader::wait_stdin_data()':
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/console_handler.h:202:16: error: narrowing conversion of '4294967295' from 'DWORD' {aka 'long unsigned int'} to 'int' [-Wnarrowing]
  202 |           case WAIT_FAILED:
      |                ^~~~~~~~~~~
In file included from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/storages/portable_storage.h:3, 
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/storages/portable_storage_template_helper.h:32,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/storages/levin_abstract_invoke2.h:29,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_protocol/cryptonote_protocol_handler.h:41,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/simplewallet/simplewallet.cpp:61:
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/misc_language.h: At global scope:
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/misc_language.h:84:31: warning: 'template<class _Arg1, class _Arg2, class _Result> struct std::binary_function' is deprecated [-Wdeprecated-declarations]
   84 |                 : public std::binary_function<_Ty, _Ty, bool>
      |                               ^~~~~~~~~~~~~~~
In file included from C:/msys64/mingw64/include/c++/12.2.0/bits/unique_ptr.h:37,
                 from C:/msys64/mingw64/include/c++/12.2.0/memory:76,
                 from C:/msys64/mingw64/include/boost/config/no_tr1/memory.hpp:21,
                 from C:/msys64/mingw64/include/boost/get_pointer.hpp:14,
                 from C:/msys64/mingw64/include/boost/bind/mem_fn.hpp:25,
                 from C:/msys64/mingw64/include/boost/mem_fn.hpp:22,
                 from C:/msys64/mingw64/include/boost/bind/bind.hpp:26,
                 from C:/msys64/mingw64/include/boost/bind.hpp:29,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/simplewallet/simplewallet.cpp:39:
C:/msys64/mingw64/include/c++/12.2.0/bits/stl_function.h:131:12: note: declared here
  131 |     struct binary_function
      |            ^~~~~~~~~~~~~~~
In file included from C:/msys64/mingw64/include/windows.h:70,
                 from C:/msys64/mingw64/include/winsock2.h:23,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/string_tools.h:34,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/command_server.cpp:32:
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/console_handler.h: In member function 'bool epee::async_stdin_reader::wait_stdin_data()':
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/console_handler.h:202:16: error: narrowing conversion of '4294967295' from 'DWORD' {aka 'long unsigned int'} to 'int' [-Wnarrowing]
  202 |           case WAIT_FAILED:
      |                ^~~~~~~~~~~
In file included from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/net/net_helper.h:50,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/net/http_client.h:41,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/common/http_connection.h:33,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/common/rpc_client.h:33,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/rpc_command_executor.h:44,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/command_parser_executor.h:41,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/command_server.h:45,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/command_server.cpp:33:
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/misc_language.h: At global scope:
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/misc_language.h:84:31: warning: 'template<class _Arg1, class _Arg2, class _Result> struct std::binary_function' is deprecated [-Wdeprecated-declarations]
   84 |                 : public std::binary_function<_Ty, _Ty, bool>
      |                               ^~~~~~~~~~~~~~~
In file included from C:/msys64/mingw64/include/c++/12.2.0/string:48,
                 from C:/msys64/mingw64/include/boost/algorithm/string/std/string_traits.hpp:15,
                 from C:/msys64/mingw64/include/boost/algorithm/string/std_containers_traits.hpp:19,
                 from C:/msys64/mingw64/include/boost/algorithm/string.hpp:18,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/command_server.cpp:29:
C:/msys64/mingw64/include/c++/12.2.0/bits/stl_function.h:131:12: note: declared here
  131 |     struct binary_function
      |            ^~~~~~~~~~~~~~~
In file included from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_basic/cryptonote_basic.h:49,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/rpc/message_data_structs.h:32,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/rpc/message.h:37,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/rpc/daemon_messages.h:36,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/rpc/daemon_handler.h:32,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/daemon.cpp:36:
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/misc_language.h:84:31: warning: 'template<class _Arg1, class _Arg2, class _Result> struct std::binary_function' is deprecated [-Wdeprecated-declarations]
   84 |                 : public std::binary_function<_Ty, _Ty, bool>
      |                               ^~~~~~~~~~~~~~~
In file included from C:/msys64/mingw64/include/c++/12.2.0/bits/unique_ptr.h:37,
                 from C:/msys64/mingw64/include/c++/12.2.0/memory:76,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/daemon.cpp:31:
C:/msys64/mingw64/include/c++/12.2.0/bits/stl_function.h:131:12: note: declared here
  131 |     struct binary_function
      |            ^~~~~~~~~~~~~~~
In file included from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/p2p/p2p_protocol_defs.h:39,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/p2p/net_node_common.h:41,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_protocol/cryptonote_protocol_handler_common.h:33,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_core/cryptonote_core.h:41,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/main.cpp:35:
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/misc_language.h:84:31: warning: 'template<class _Arg1, class _Arg2, class _Result> struct std::binary_function' is deprecated [-Wdeprecated-declarations]
   84 |                 : public std::binary_function<_Ty, _Ty, bool>
      |                               ^~~~~~~~~~~~~~~
In file included from C:/msys64/mingw64/include/c++/12.2.0/functional:49,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/common/command_line.h:33,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/main.cpp:31:
C:/msys64/mingw64/include/c++/12.2.0/bits/stl_function.h:131:12: note: declared here
  131 |     struct binary_function
      |            ^~~~~~~~~~~~~~~
In file included from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/simplewallet/simplewallet.h:44,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/simplewallet/simplewallet.cpp:62:
C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_basic/cryptonote_basic_impl.h:43:29: warning: 'template<class _Arg, class _Result> struct std::unary_function' is deprecated [-Wdeprecated-declarations]
   43 |   struct array_hasher: std::unary_function<t_array&, std::size_t>
      |                             ^~~~~~~~~~~~~~
C:/msys64/mingw64/include/c++/12.2.0/bits/stl_function.h:117:12: note: declared here
  117 |     struct unary_function
      |            ^~~~~~~~~~~~~~
[ 90%] Built target monero-wallet-gui_autogen
In file included from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_core/tx_pool.h:47,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_core/cryptonote_core.h:46:
C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_basic/cryptonote_basic_impl.h:43:29: warning: 'template<class _Arg, class _Result> struct std::unary_function' is deprecated [-Wdeprecated-declarations]
   43 |   struct array_hasher: std::unary_function<t_array&, std::size_t>
      |                             ^~~~~~~~~~~~~~
C:/msys64/mingw64/include/c++/12.2.0/bits/stl_function.h:117:12: note: declared here
  117 |     struct unary_function
      |            ^~~~~~~~~~~~~~
C:/Users/maste/Documents/GitHub/monero-gui/monero/src/simplewallet/simplewallet.cpp: In member function 'void cryptonote::simple_wallet::print_accounts()':
C:/Users/maste/Documents/GitHub/monero-gui/monero/src/simplewallet/simplewallet.cpp:9443:51: warning: loop variable 'p' of type 'const std::pair<std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >&' binds to a temporary constructed from type 'const std::pair<const std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >' [-Wrange-loop-construct]
 9443 |   for (const std::pair<std::string, std::string>& p : account_tags.first)
      |                                                   ^
C:/Users/maste/Documents/GitHub/monero-gui/monero/src/simplewallet/simplewallet.cpp:9443:51: note: use non-reference type 'const std::pair<std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >' to make the copy explicit or 'const std::pair<const std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >&' to prevent copying
In file included from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_core/tx_pool.h:47,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_core/cryptonote_core.h:46,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/rpc/core_rpc_server.h:42,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/rpc_command_executor.h:47:
C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_basic/cryptonote_basic_impl.h:43:29: warning: 'template<class _Arg, class _Result> struct std::unary_function' is deprecated [-Wdeprecated-declarations]
   43 |   struct array_hasher: std::unary_function<t_array&, std::size_t>
      |                             ^~~~~~~~~~~~~~
C:/msys64/mingw64/include/c++/12.2.0/bits/stl_function.h:117:12: note: declared here
  117 |     struct unary_function
      |            ^~~~~~~~~~~~~~
In file included from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_core/tx_pool.h:47,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_core/cryptonote_core.h:46,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/rpc/daemon_handler.h:35:
C:/Users/maste/Documents/GitHub/monero-gui/monero/src/cryptonote_basic/cryptonote_basic_impl.h:43:29: warning: 'template<class _Arg, class _Result> struct std::unary_function' is deprecated [-Wdeprecated-declarations]
   43 |   struct array_hasher: std::unary_function<t_array&, std::size_t>
      |                             ^~~~~~~~~~~~~~
C:/msys64/mingw64/include/c++/12.2.0/bits/stl_function.h:117:12: note: declared here
  117 |     struct unary_function
      |            ^~~~~~~~~~~~~~
In file included from C:/msys64/mingw64/include/windows.h:70,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/external/easylogging++/easylogging++.h:394,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/misc_log_ex.h:35,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/include_base_utils.h:32,       
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/common/command_line.h:42:
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/console_handler.h: In member function 'bool epee::async_stdin_reader::wait_stdin_data()':
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/console_handler.h:202:16: error: narrowing conversion of '4294967295' from 'DWORD' {aka 'long unsigned int'} to 'int' [-Wnarrowing]
  202 |           case WAIT_FAILED:
      |                ^~~~~~~~~~~
In file included from C:/msys64/mingw64/include/shlobj.h:124,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemonizer/windows_daemonizer.inl:36,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemonizer/daemonizer.h:63,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/command_line_args.h:34,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/core.h:35,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/daemon.cpp:43:
C:/msys64/mingw64/include/shobjidl.h: In function 'HRESULT SHLoadLibraryFromItem(IShellItem*, DWORD, const IID&, void**)':  
C:/msys64/mingw64/include/shobjidl.h:32969: note: '-Wmisleading-indentation' is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
32969 |       if (SUCCEEDED(hr))
      |
C:/msys64/mingw64/include/shobjidl.h:32969: note: adding '-flarge-source-files' will allow for more column-tracking support, at the expense of compilation time and memory
In file included from C:/msys64/mingw64/include/windows.h:70,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/external/easylogging++/easylogging++.h:394,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/misc_log_ex.h:35,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/daemon.cpp:34:
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/console_handler.h: In member function 'bool epee::async_stdin_reader::wait_stdin_data()':
C:/Users/maste/Documents/GitHub/monero-gui/monero/contrib/epee/include/console_handler.h:202: error: narrowing conversion of '4294967295' from 'DWORD' {aka 'long unsigned int'} to 'int' [-Wnarrowing]
  202 |           case WAIT_FAILED:
      |
In file included from C:/msys64/mingw64/include/shlobj.h:124,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemonizer/windows_daemonizer.inl:36,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemonizer/daemonizer.h:63,
                 from C:/Users/maste/Documents/GitHub/monero-gui/monero/src/daemon/main.cpp:40:
C:/msys64/mingw64/include/shobjidl.h: In function 'HRESULT SHLoadLibraryFromItem(IShellItem*, DWORD, const IID&, void**)':  
C:/msys64/mingw64/include/shobjidl.h:32969: note: '-Wmisleading-indentation' is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
32969 |       if (SUCCEEDED(hr))
      |
C:/msys64/mingw64/include/shobjidl.h:32969: note: adding '-flarge-source-files' will allow for more column-tracking support, at the expense of compilation time and memory
make[3]: *** [monero/src/simplewallet/CMakeFiles/simplewallet.dir/build.make:76: monero/src/simplewallet/CMakeFiles/simplewallet.dir/simplewallet.cpp.obj] Error 1
make[2]: *** [CMakeFiles/Makefile2:3509: monero/src/simplewallet/CMakeFiles/simplewallet.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
make[3]: *** [monero/src/daemon/CMakeFiles/daemon.dir/build.make:90: monero/src/daemon/CMakeFiles/daemon.dir/command_server.cpp.obj] Error 1
make[3]: *** Waiting for unfinished jobs....
make[3]: *** [monero/src/daemon/CMakeFiles/daemon.dir/build.make:132: monero/src/daemon/CMakeFiles/daemon.dir/main.cpp.obj] 
Error 1
make[3]: *** [monero/src/daemon/CMakeFiles/daemon.dir/build.make:104: monero/src/daemon/CMakeFiles/daemon.dir/daemon.cpp.obj] Error 1
make[2]: *** [CMakeFiles/Makefile2:3699: monero/src/daemon/CMakeFiles/daemon.dir/all] Error 2
make[1]: *** [Makefile:136: all] Error 2
make[1]: Leaving directory '/c/Users/maste/Documents/Github/monero-gui/build/release'
make: *** [Makefile:73: release-win64] Error 2
```
</details>

## elibroftw | 2022-12-03T23:33:39+00:00
I was able to bring the errors down to just zmq related. Not sure how to intrepret these though.

<details>
<summary>output 2</summary>

```bash
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x1a4e): undefined reference to `__imp_zmq_send_const'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x1a5c): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x53b9): undefined reference to `__imp_zmq_socket'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x53d0): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x53e5): undefined reference to `__imp_zmq_connect'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x53fa): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x5442): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x5502): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x558d): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x5a03): undefined reference to `__imp_zmq_msg_init'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x5a0f): undefined reference to `__imp_zmq_msg_recv'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x5ab5): undefined reference to `__imp_zmq_msg_data'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x5ac1): undefined reference to `__imp_zmq_msg_size'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x5af0): undefined reference to `__imp_zmq_msg_send'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x608a): undefined reference to `__imp_zmq_msg_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text+0x65b1): undefined reference to `__imp_zmq_msg_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_pub.cpp.obj):zmq_pub.cpp:(.text$_ZN3net3zmq8retry_opIPFiP9zmq_msg_tPviEJS3_RKS4_iEEE6expectIvET_DpOT0_[_ZN3net3zmq8retry_opIPFiP9zmq_msg_tPviEJS3_RKS4_iEEE6expectIvET_DpOT0_]+0x15): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x2da): undefined reference to `__imp_zmq_socket'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x2ed): undefined reference to `__imp_zmq_setsockopt'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x338): undefined reference to `__imp_zmq_bind'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x4e8): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x6e2): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x89c): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0xa2c): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0xba2): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x11c9): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x13b7): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x1608): undefined reference to `__imp_zmq_init'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x1642): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x169e): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x16ad): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x16bc): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x1752): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x1761): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x1770): more undefined references to `__imp_zmq_close' follow
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x1f71): undefined reference to `__imp_zmq_poll'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x1f78): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x320c): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x321a): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../rpc/libdaemon_rpc_server.a(zmq_server.cpp.obj):zmq_server.cpp:(.text+0x322a): undefined reference to `__imp_zmq_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x192): undefined reference to `__imp_zmq_strerror'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x25e): undefined reference to `__imp_zmq_term'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x265): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x2b1): undefined reference to `__imp_zmq_msg_recv'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x2b8): undefined reference to `__imp_zmq_msg_size'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x2bf): undefined reference to `__imp_zmq_msg_data'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x323): undefined reference to `__imp_zmq_msg_init'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x32a): undefined reference to `__imp_zmq_msg_more'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x390): undefined reference to `__imp_zmq_msg_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x396): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x43a): undefined reference to `__imp_zmq_msg_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x5a1): undefined reference to `__imp_zmq_msg_close'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x5e7): undefined reference to `__imp_zmq_send'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x5ee): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x72f): undefined reference to `__imp_zmq_msg_init_data'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x747): undefined reference to `__imp_zmq_msg_send'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x74e): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x7ca): undefined reference to `__imp_zmq_errno'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: ../net/libnet.a(zmq.cpp.obj):zmq.cpp:(.text+0x82b): undefined reference to `__imp_zmq_msg_close'
```
</details>

## elibroftw | 2022-12-04T01:32:49+00:00
I would prefer faster debug builds than having to rely on a release build but if the practice is to use release builds while developing then this issue can be closed.

## selsta | 2022-12-04T05:38:34+00:00
We build every single monero and monero-gui commit on Windows through CI. The code itself compiles fine on Windows. I feel something in your dev environment is setup incorrectly, can you explain this again in more detail?

> If its relevant, I cloned in Windows first and then used MSYS2 64Bit in the directory.

Edit: Testing debug build on CI now.

## elibroftw | 2022-12-04T05:48:07+00:00
I could build release-win64 btw (don't know if you get element notifications). I'll let you know tomorrow about the environment. I'm afk.

# Action History
- Created by: elibroftw | 2022-12-03T19:55:19+00:00
