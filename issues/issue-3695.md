---
title: OSX compile error
source_url: https://github.com/monero-project/monero-gui/issues/3695
author: 3s3s
assignees: []
labels: []
created_at: '2021-09-12T17:48:32+00:00'
updated_at: '2021-10-29T21:37:37+00:00'
type: issue
status: closed
closed_at: '2021-10-29T21:37:30+00:00'
---

# Original Description
When I follow this instruction https://github.com/monero-project/monero-gui#building-on-os-x
I have this error : "clang: error: the clang compiler does not support '-march=x86-64'"

More logs from terminal:
```
-- Found ICU: /opt/homebrew/opt/icu4c/include (found version "69.1") 
-- Configuring done
CMake Warning (dev) at monero/src/CMakeLists.txt:93 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /Users/a12345/monero-gui/monero/src/rpc/instanciations.cpp
Call Stack (most recent call first):
  monero/src/CMakeLists.txt:81 (monero_add_library_with_deps)
  monero/src/rpc/CMakeLists.txt:101 (monero_add_library)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Generating done
-- Build files have been written to: /Users/a12345/monero-gui/build/release
[  1%] Automatic MOC and UIC for target gui_version
[  1%] Built target gui_version_autogen
[  1%] Built target genversiongui
[  1%] Automatic MOC and UIC for target obj_gui_version
[  1%] Built target obj_gui_version_autogen
[  1%] Building CXX object CMakeFiles/obj_gui_version.dir/obj_gui_version_autogen/mocs_compilation.cpp.o
clang: error: the clang compiler does not support '-march=x86-64'
make[3]: *** [CMakeFiles/obj_gui_version.dir/obj_gui_version_autogen/mocs_compilation.cpp.o] Error 1
make[2]: *** [CMakeFiles/obj_gui_version.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release] Error 2

```

How can this be fixed?

# Discussion History
## selsta | 2021-09-12T18:42:09+00:00
Do you have a M1 Mac?

## 3s3s | 2021-09-12T19:11:38+00:00
> 
> 
> Do you have a M1 Mac?

Seems yes. 
Mac OS Big Sur
version 11.5.2
Chip Apple M1


## selsta | 2021-09-13T00:34:25+00:00
Try #3697

## 3s3s | 2021-09-13T14:23:16+00:00
> 
> 
> Try #3697

Not helped. 

```
[ 22%] Building C object monero/external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[ 22%] Linking C static library liblmdb.a
[ 22%] Built target lmdb
[ 22%] Building CXX object monero/external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
clang: error: the clang compiler does not support '-march=x86-64'
make[3]: *** [monero/external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o] Error 1
make[2]: *** [monero/external/easylogging++/CMakeFiles/easylogging.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release] Error 2
```



## selsta | 2021-09-13T19:08:39+00:00
It did help, there is a different issue now. You also have to apply https://github.com/monero-project/monero/pull/7435/commits/1ac7134832b8daaa8a04e7b1cad1b38d41e21a84 inside the monero submodule.

## 3s3s | 2021-09-14T04:59:29+00:00
Still not working (((

```
[ 22%] Built target unbound
Consolidate compiler generated dependencies of target lmdb
[ 23%] Built target lmdb
Consolidate compiler generated dependencies of target easylogging
[ 23%] Built target easylogging
Consolidate compiler generated dependencies of target qrcodegen
[ 24%] Built target qrcodegen
[ 24%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/byte_slice.cpp.o
clang: error: the clang compiler does not support '-march=x86-64'
make[3]: *** [monero/contrib/epee/src/CMakeFiles/epee.dir/byte_slice.cpp.o] Error 1
make[2]: *** [monero/contrib/epee/src/CMakeFiles/epee.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release] Error 2
```

## selsta | 2021-10-29T21:37:30+00:00
Delete this line and do the other explained steps in this issue, then it will compile fine: https://github.com/monero-project/monero-gui/blob/master/CMakeLists.txt#L27

Confirmed myself on a M1 Mac.

Next Monero GUI release (v0.17.3.0) will have proper support for M1, then you will only have to enter `make`.

# Action History
- Created by: 3s3s | 2021-09-12T17:48:32+00:00
- Closed at: 2021-10-29T21:37:30+00:00
