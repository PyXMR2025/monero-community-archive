---
title: How to generate Xcode project
source_url: https://github.com/monero-project/monero/issues/3000
author: dennisfedorko
assignees: []
labels: []
created_at: '2017-12-24T00:20:33+00:00'
updated_at: '2022-07-20T19:40:25+00:00'
type: issue
status: closed
closed_at: '2022-07-20T19:40:25+00:00'
---

# Original Description
Is there a simple way to generate a clean, working project in Xcode? 

I have tried cmake -G Xcode but then I get the error:
```
clang: error: no such file or directory: '/Downloads/monero-master/src/crypto/Debug/libcncrypto.a'
```
along with similar errors where it can't find Debug libs in src.

# Discussion History
## moneromooo-monero | 2017-12-30T23:11:57+00:00
Sounds like a cmake or xcode question maybe ?

## dennisfedorko | 2017-12-31T02:49:07+00:00
I assumed there was a dev working on a Mac out there, is there a specific IDE that works well with this build on a Mac that the devs on this project use? Would be nice to have instructions for project setup for interested devs.

Nice work on the project so far btw, keep up the good fight!

## jtgrassie | 2018-01-03T17:47:24+00:00
There's no XCode support. To my knowledge all the Mac folk are happy with the command line build.

As you asked, my "IDE" is vim, which works like a charm on OSX.

If you're wedded to developing in XCode, the simplest method would be to create a blank project, add the source tree of monero to the project, Add a 'Run script phase' in 'Build phases' in XCode to run the `make ...` and remove any other build phases. That should give you a way to edit code in XCode IDE and hit build/run.

## ghost | 2018-01-07T21:25:33+00:00
I'll just hop in to say that, if someone needs a more "Guided" GUI, CLion does the trick to.

## selsta | 2022-07-20T19:40:25+00:00
```diff
 src/CMakeLists.txt        | 7 +++----
 src/blocks/CMakeLists.txt | 2 +-
 2 files changed, 4 insertions(+), 5 deletions(-)

diff --git a/src/CMakeLists.txt b/src/CMakeLists.txt
index 9904c5de7..d01f249e5 100644
--- a/src/CMakeLists.txt
+++ b/src/CMakeLists.txt
@@ -93,14 +93,13 @@ function (monero_add_library_with_deps)
   # libwallet, which combines multiple components.
   set(objlib obj_${MONERO_ADD_LIBRARY_NAME})
   add_library(${objlib} OBJECT ${MONERO_ADD_LIBRARY_SOURCES})
-  add_library("${MONERO_ADD_LIBRARY_NAME}" $<TARGET_OBJECTS:${objlib}>)
+  add_library(${MONERO_ADD_LIBRARY_NAME} ${MONERO_ADD_LIBRARY_SOURCES})
   monero_set_target_no_relink("${MONERO_ADD_LIBRARY_NAME}")
   if (MONERO_ADD_LIBRARY_DEPENDS)
-    add_dependencies(${objlib} ${MONERO_ADD_LIBRARY_DEPENDS})
+    #add_dependencies(${objlib} ${MONERO_ADD_LIBRARY_DEPENDS})
+    add_dependencies(${MONERO_ADD_LIBRARY_NAME} ${MONERO_ADD_LIBRARY_DEPENDS})
   endif()
   set_property(TARGET "${MONERO_ADD_LIBRARY_NAME}" PROPERTY FOLDER "libs")
-  target_compile_definitions(${objlib}
-    PRIVATE $<TARGET_PROPERTY:${MONERO_ADD_LIBRARY_NAME},INTERFACE_COMPILE_DEFINITIONS>)
 endfunction ()
 
 include(Version)
diff --git a/src/blocks/CMakeLists.txt b/src/blocks/CMakeLists.txt
index 445596a66..383b8f431 100644
--- a/src/blocks/CMakeLists.txt
+++ b/src/blocks/CMakeLists.txt
@@ -45,4 +45,4 @@ foreach(BLOB_NAME checkpoints testnet_blocks stagenet_blocks)
     )
 endforeach()
 
-monero_add_library(blocks blocks.cpp ${GENERATED_SOURCES})
+add_library(blocks blocks.cpp ${GENERATED_SOURCES})
```

Apply this diff and then use `-G Xcode`.

# Action History
- Created by: dennisfedorko | 2017-12-24T00:20:33+00:00
- Closed at: 2022-07-20T19:40:25+00:00
