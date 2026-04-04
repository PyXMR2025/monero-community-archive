---
title: ' NetBSD; "Warning: reference to the libc supplied alloca(3); this most likely
  will not work"'
source_url: https://github.com/monero-project/monero/issues/5187
author: thomasvaughan
assignees: []
labels: []
created_at: '2019-02-23T11:17:17+00:00'
updated_at: '2019-02-24T15:14:49+00:00'
type: issue
status: closed
closed_at: '2019-02-23T21:06:45+00:00'
---

# Original Description
Building with gcc on NetBSD results in two warnings:

`spawn.cpp:(.text+0x41): warning: Warning: reference to the libc supplied alloca(3); this most likely will not work. Please use the compiler provided version of alloca(3), by supplying the appropriate compiler flags (e.g. not -std=c89).`

`tree-hash.c:(.text+0x85): warning: Warning: reference to the libc supplied alloca(3); this most likely will not work. Please use the compiler provided version of alloca(3), by supplying the appropriate compiler flags (e.g. not -std=c89).`

The spawn.cpp warning occurs 10 times and the tree-hash.c warning occurs once.

The tree-hash.c warning goes away if I add ` #define alloca  __builtin_alloca` immediately below the ` #include <stdlib.h>` in src/crypto/monero, but I don't know if this addition is wise or foolish (if wise, it presumably still needs to be wrapped up in some sort of conditional). This is a purely script-kiddie solution, influenced by https://github.com/dotnet/coreclr/pull/3189 and https://github.com/dotnet/coreclr/commit/6ad35ca6638ed7b57bbbf21aa9d082e3f39f1d6b and by my reading of the NetBSD /usr/include/stdlib.h.

I haven't attempted to understand the spawn.cpp warning, but I'm happy to test any suggestions and describe the result here.

# Discussion History
## thomasvaughan | 2019-02-23T11:21:25+00:00
Edit: The ` #define alloca __builtin_alloca` was added in src/crypt/tree-hash.c. (GitHub isn't letting me correct the error in what I wrote a moment ago.)

## moneromooo-monero | 2019-02-23T12:05:13+00:00
That seems to be a good change after looking around a bit.
Can you check whether tests pass with https://github.com/moneromooo-monero/bitmonero/tree/alloca ?

## thomasvaughan | 2019-02-23T14:26:41+00:00
Your alloca branch eliminates the warning from tree-hash.c, but I'm seeing 17 occurrences of `spawn.cpp:(.text+0x41): warning: Warning: reference to the libc supplied alloca(3); this most likely will not work. Please use the compiler provided version of alloca(3), by supplying the appropriate compiler flags (e.g. not -std=c89).`

Previously I ran `gmake release`, but on your alloca branch I ran `gmake release-test` so the warning is showing up more times. Also, building the tests gets only as far as:

    [ 80%] Building CXX object tests/performance_tests/CMakeFiles/performance_tests.dir/main.cpp.o
    In file included from /home/t/usr/src/bitmonero/tests/performance_tests/main.cpp:36:0:
    /home/t/usr/src/bitmonero/tests/performance_tests/performance_utils.h: In function ‘void set_process_affinity(int)’:
    /home/t/usr/src/bitmonero/tests/performance_tests/performance_utils.h:53:3: error: ‘cpu_set_t’ was not declared in this scope
       cpu_set_t cpuset;

## moneromooo-monero | 2019-02-23T16:19:33+00:00
Typo. Fixed :) And the tests problem should now be fixed too.

## thomasvaughan | 2019-02-23T20:40:46+00:00
Yes, your alloca branch has now eliminated the two warnings.

Given the title of this issue, perhaps I should now close it. However your other fix, in performance_utils.h, has revealed the following:

    [ 98%] Linking CXX executable unit_tests
    ld: /usr/pkg/lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
    ld: final link failed: Nonrepresentable section on output
    tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1678: recipe for target 'tests/unit_tests/unit_tests' failed




## moneromooo-monero | 2019-02-23T21:01:14+00:00
That's your own problem this time. Either uninstall libgtest (monero ships one) or install one built with -fPIC.

## thomasvaughan | 2019-02-23T21:06:45+00:00
Understood; thank you for the help. I'll close this issue.

## moneromooo-monero | 2019-02-24T15:14:49+00:00
Don't close bugs before the patch is merged. Half the time when that happens I'll forget to PR the patch.

# Action History
- Created by: thomasvaughan | 2019-02-23T11:17:17+00:00
- Closed at: 2019-02-23T21:06:45+00:00
