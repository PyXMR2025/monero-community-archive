---
title: Hidapi seems to require that it is built in source, when building static release
  binaries.
source_url: https://github.com/monero-project/monero/issues/4453
author: sedited
assignees: []
labels: []
created_at: '2018-09-26T11:48:13+00:00'
updated_at: '2018-10-06T13:13:19+00:00'
type: issue
status: closed
closed_at: '2018-10-06T13:13:19+00:00'
---

# Original Description
When compiling with `make release-static-linux-x86_64`, the build currently fails with: https://paste.debian.net/1044459/ , a whole bunch of hidapi linking errors. To me this looks like hidapi needs to be built in tree, and then object files need to be directly linked to, like here: https://github.com/edorfaus/TEMPered/blob/master/CMakeLists.txt#L40 . 
@anonimal can you add hidapi as a submodule? You can use my depends recipes in contrib/depends/packages for a hint on how to compile hidapi and its dependencies. The hidapi repo readme also contains some hints on how to build: https://github.com/signal11/hidapi . On linux, I would strongly recommend to build hiadpi-libusb. It is enough to make just hidapi a submodule. Its eudev and libusb dependencies don't need to be included in tree, they can be linked from the host system. 

# Discussion History
## iDunk5400 | 2018-09-26T18:09:17+00:00
I did not have such errors building `release-static-linux-x86_64` on Ubuntu 16.04. However, I did have to edit CMakeLists.txt a bit. Does this help you get past the errors?
```diff
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 994d476..53d676f 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -435,7 +435,9 @@ if(STATIC AND NOT IOS)
   endif()
 endif()

-find_package(HIDAPI)
+if(NOT STATIC)
+  find_package(HIDAPI)
+endif()
```
/EDIT: Nevermind, that won't work.

## sedited | 2018-09-26T19:22:56+00:00
Did you check `ldd monerod` and see if hidapi was dynamically linked? 

## iDunk5400 | 2018-09-26T20:07:43+00:00
The thing is, with the above diff `HIDAPI_FOUND` would never be set and binaries would not have hardware device support.

## cslashm | 2018-09-28T07:34:40+00:00
I add this pacman package mingw-w64-x86_64-hidapi 0.8.0rc1-4 to get compiled



## sedited | 2018-09-28T09:54:43+00:00
@cslashm I think the windows static cross compile works out of the box, same goes for macOS. It's just linux, where it seems like an in tree build is required to achieve a static binary.

## sedited | 2018-10-06T13:13:19+00:00
Fixed with #4506 , luckily no in-tree source is required after all. 

# Action History
- Created by: sedited | 2018-09-26T11:48:13+00:00
- Closed at: 2018-10-06T13:13:19+00:00
