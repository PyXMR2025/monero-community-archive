---
title: No stack trace on fedora 37 unless forcing libunwind
source_url: https://github.com/monero-project/monero/issues/8690
author: ovhpse
assignees: []
labels: []
created_at: '2022-12-31T13:44:19+00:00'
updated_at: '2022-12-31T18:05:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,

After building on fedora 37 I was stuck with https://github.com/monero-project/monero/issues/8132

It is a double issue:
- Exception during synchronization
- Stack trace in hex only

I solved the second issue by changing the code to force the usage of libunwind and not easylogging++. I has also to add `#include <iomanip>` in stack_trace.cpp.

I'm not a developer myself and don't know what would be the solution to not impact users of other OS/distros.

```
diff --git a/CMakeLists.txt b/CMakeLists.txt
index b8aed2379..48f8de285 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -531,6 +531,8 @@ add_definitions("-DBLOCKCHAIN_DB=${BLOCKCHAIN_DB}")
 # Can't install hook in static build on OSX, because OSX linker does not support --wrap
 # On ARM, having libunwind package (with .so's only) installed breaks static link.
 # When possible, avoid stack tracing using libunwind in favor of using easylogging++.
+option(FORCE_UNWIND "Force the use of libunwind" ON)
+
 if (APPLE)
   set(DEFAULT_STACK_TRACE OFF)
   set(LIBUNWIND_LIBRARIES "")
@@ -539,8 +541,14 @@ elseif (DEPENDS AND NOT LINUX)
   set(LIBUNWIND_LIBRARIES "")
 elseif(CMAKE_C_COMPILER_ID STREQUAL "GNU" AND NOT MINGW)
   set(DEFAULT_STACK_TRACE ON)
-  set(STACK_TRACE_LIB "easylogging++") # for diag output only
-  set(LIBUNWIND_LIBRARIES "")
+  if(FORCE_UNWIND)
+    find_package(Libunwind)
+    set(STACK_TRACE_LIB "libunwind") # for diag output only
+    add_definitions(-DFORCE_UNWIND)
+  else()
+    set(STACK_TRACE_LIB "easylogging++") # for diag output only
+    set(LIBUNWIND_LIBRARIES "")
+  endif()
 elseif (ARM)
   set(DEFAULT_STACK_TRACE OFF)
   set(LIBUNWIND_LIBRARIES "")
@@ -558,7 +566,7 @@ endif()
 option(STACK_TRACE "Install a hook that dumps stack on exception" ${DEFAULT_STACK_TRACE})
 
 if(STACK_TRACE)
-  message(STATUS "Stack trace on exception enabled (using ${STACK_TRACE_LIB})")
+  message(STATUS "Stack trace on exception enabled (using ${STACK_TRACE_LIB}) from : ${LIBUNWIND_LIBRARIES}")
 else()
   message(STATUS "Stack trace on exception disabled")
 endif()
diff --git a/src/common/stack_trace.cpp b/src/common/stack_trace.cpp
index 130ba4d81..7571fee86 100644
--- a/src/common/stack_trace.cpp
+++ b/src/common/stack_trace.cpp
@@ -26,7 +26,7 @@
 // STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
 // THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 
-#if !defined __GNUC__ || defined __MINGW32__ || defined __MINGW64__ || defined __ANDROID__
+#if !defined __GNUC__ || defined __MINGW32__ || defined __MINGW64__ || defined __ANDROID__ || defined FORCE_UNWIND
 #define USE_UNWIND
 #else
 #define ELPP_FEATURE_CRASH_LOG 1
@@ -34,6 +34,7 @@
 #include "easylogging++/easylogging++.h"
 
 #include <stdexcept>
+#include <iomanip>
 #ifdef USE_UNWIND
 #define UNW_LOCAL_ONLY
 #include <libunwind.h>
```


# Discussion History
# Action History
- Created by: ovhpse | 2022-12-31T13:44:19+00:00
