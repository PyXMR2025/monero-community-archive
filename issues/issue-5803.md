---
title: Compile monerod for SunOS (SmartOS) - failures - ULLONG_MAX
source_url: https://github.com/monero-project/monero/issues/5803
author: kayront
assignees: []
labels: []
created_at: '2019-08-10T19:00:46+00:00'
updated_at: '2019-08-11T08:02:23+00:00'
type: issue
status: closed
closed_at: '2019-08-11T08:02:23+00:00'
---

# Original Description
```
[ 74%] Built target block_fuzz_tests                                                                                                                                                                                                          
Scanning dependencies of target cnv4-jit-tests                                                                                                                                                                                                
[ 74%] Building C object tests/crypto/CMakeFiles/cnv4-jit-tests.dir/cnv4-jit.c.o                                                                                                                                                              
/home/admin/src/monero/tests/crypto/cnv4-jit.c: In function 'main':                                                                                                                                                                           
/home/admin/src/monero/tests/crypto/cnv4-jit.c:64:57: error: 'ULLONG_MAX' undeclared (first use in this function)                                                                                                                             
     if ((start_height == 0 && errno) || start_height == ULLONG_MAX)                                                                                                                                                                          
                                                         ^~~~~~~~~~                                                                                                                                                                           
/home/admin/src/monero/tests/crypto/cnv4-jit.c:64:57: note: 'ULLONG_MAX' is defined in header '<limits.h>'; did you forget to '#include <limits.h>'?                                                                                          
/home/admin/src/monero/tests/crypto/cnv4-jit.c:36:1:                                                                                                                                                                                          
+#include <limits.h>                                                                                                                                                                                                                          
                                                                                                                                                                                                                                              
/home/admin/src/monero/tests/crypto/cnv4-jit.c:64:57:                                                                                                                                                                                         
     if ((start_height == 0 && errno) || start_height == ULLONG_MAX)                                                                                                                                                                          
                                                         ^~~~~~~~~~                                                                                                                                                                           
/home/admin/src/monero/tests/crypto/cnv4-jit.c:64:57: note: each undeclared identifier is reported only once for each function it appears in                                                                                                  
make[2]: *** [tests/crypto/CMakeFiles/cnv4-jit-tests.dir/build.make:63: tests/crypto/CMakeFiles/cnv4-jit-tests.dir/cnv4-jit.c.o] Error 1                                                                                                      
make[1]: *** [CMakeFiles/Makefile2:4799: tests/crypto/CMakeFiles/cnv4-jit-tests.dir/all] Error 2                                                                                                                                              
make: *** [Makefile:141: all] Error 2    
```

# Discussion History
## vtnerd | 2019-08-10T23:57:20+00:00
The fix here appears to be in the error message.

## kayront | 2019-08-11T08:02:23+00:00
You're right. Closing this one.

# Action History
- Created by: kayront | 2019-08-10T19:00:46+00:00
- Closed at: 2019-08-11T08:02:23+00:00
