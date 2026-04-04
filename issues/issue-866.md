---
title: No build when libunwind is absent.
source_url: https://github.com/monero-project/monero/issues/866
author: ViperRu
assignees: []
labels: []
created_at: '2016-06-20T16:22:37+00:00'
updated_at: '2016-06-21T07:30:16+00:00'
type: issue
status: closed
closed_at: '2016-06-21T07:30:16+00:00'
---

# Original Description
...
-- Could not find libunwind (missing:  LIBUNWIND_INCLUDE_DIR LIBUNWIND_LIBRARIES)
-- Stack traces disabled
...
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
LIBUNWIND_LIBRARIES (ADVANCED)
    linked by target "common" in directory /home/andrey/Проекты/bitmonero/src/common

-- Configuring incomplete, errors occurred!
See also "/home/andrey/Проекты/bitmonero/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/andrey/Проекты/bitmonero/build/release/CMakeFiles/CMakeError.log".


# Discussion History
## ViperRu | 2016-06-20T16:36:20+00:00
When I added pkg libunwind8-dev into Ubuntu, the project is not building by "make release-static". There are records:
`
/home/bitmonero/src/blockchain_utilities/bootstrap_file.cpp: In member function ‘seek_to_first_chunk’:
/usr/include/c++/4.9/ostream:196:50: warning: ‘MEM[(unsigned char &)&bfi + 1]’ may be used uninitialized in this function [-Wmaybe-uninitialized]
  return _M_insert(static_cast<unsigned long>(__n));
                                                  ^
/home/bitmonero/src/blockchain_utilities/bootstrap_file.cpp:395:24: note: ‘MEM[(unsigned char &)&bfi + 1]’ was declared here
   bootstrap::file_info bfi;
                        ^
/home/bitmonero/src/blockchain_utilities/bootstrap_file.cpp:395:24: warning: ‘MEM[(unsigned int &)&bfi + 4]’ may be used uninitialized in this function [-Wmaybe-uninitialized]
/usr/lib/gcc/x86_64-linux-gnu/4.9/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function`xz_uncompressed_size':
/build/buildd/libunwind-1.1/src/elfxx.c:194: undefined reference to `lzma_stream_footer_decode'
/build/buildd/libunwind-1.1/src/elfxx.c:201: undefined reference to`lzma_index_buffer_decode'
/build/buildd/libunwind-1.1/src/elfxx.c:205: undefined reference to `lzma_index_size'
/build/buildd/libunwind-1.1/src/elfxx.c:210: undefined reference to`lzma_index_end'
/build/buildd/libunwind-1.1/src/elfxx.c:207: undefined reference to `lzma_index_uncompressed_size'
/build/buildd/libunwind-1.1/src/elfxx.c:210: undefined reference to`lzma_index_end'
/usr/lib/gcc/x86_64-linux-gnu/4.9/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `_Uelf64_extract_minidebuginfo':
/build/buildd/libunwind-1.1/src/elfxx.c:278: undefined reference to`lzma_stream_buffer_decode'
collect2: error: ld returned 1 exit status
make[3]: **\* [bin/blockchain_export] Error 1
make[3]: Exit from dirrectory `/home/bitmonero/build/release'
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all] Error 2
make[2]: Exit from dirrectory`/home/bitmonero/build/release'
make[1]: **\* [all] Error 2
make[1]: Exit from dirrectory `/home/bitmonero/build/release'
make: *** [release-static-64] Error 2
`


## fluffypony | 2016-06-20T16:38:32+00:00
Ubuntu doesn't contain static packages for libunwind, unfortunately, so you'll have to `make release` instead.

We may be dropping `libunwind` and moving to `easylogging++`, so I'm loathe to put in the effort to bring `unwind` into the source tree right now:)


## ViperRu | 2016-06-20T16:50:59+00:00
I leave old version without libunwind because I need transfer binary file to the system where part of libraries are outdated.


## ViperRu | 2016-06-20T17:22:21+00:00
I made the folowing changes:
--- CMakeLists.txt.bck  2016-06-20 19:44:37.534164211 +0300
+++ CMakeLists.txt      2016-06-20 20:07:51.471180927 +0300
@@ -243,13 +243,6 @@

-find_package(Libunwind)
-if(LIBUNWIND_FOUND)
-message(STATUS "Using libunwind to provide stack traces")
-add_definitions("-DHAVE_LIBUNWIND")
-else()
-message(STATUS "Stack traces disabled")
-endif()

@@ -282,9 +275,6 @@

-# Final setup for libunwind
-include_directories(${LIBUNWIND_INCLUDE})
-link_directories(${LIBUNWIND_LIBRARY_DIRS})

--- src/common/stack_trace.cpp.bck      2016-06-20 19:44:37.990171072 +0300
+++ src/common/stack_trace.cpp  2016-06-20 19:52:10.452984255 +0300
@@ -113,7 +113,6 @@

-#warning libunwind disabled, no stack traces

The project was builded. Didn't I anything break except stack trace?


## moneromooo-monero | 2016-06-20T18:24:11+00:00
Fixed in https://github.com/monero-project/bitmonero/pull/868


## moneromooo-monero | 2016-06-20T18:36:27+00:00
And your changes did not break anything, it all seems fine.


## ViperRu | 2016-06-21T03:11:31+00:00
Thank you. #868 working for me after remove libunwind package.


# Action History
- Created by: ViperRu | 2016-06-20T16:22:37+00:00
- Closed at: 2016-06-21T07:30:16+00:00
