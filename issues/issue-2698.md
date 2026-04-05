---
title: 'Overwrite argv '
source_url: https://github.com/xmrig/xmrig/issues/2698
author: rubenh2905
assignees: []
labels: []
created_at: '2021-11-16T12:29:14+00:00'
updated_at: '2021-11-29T18:28:12+00:00'
type: issue
status: closed
closed_at: '2021-11-29T18:28:12+00:00'
---

# Original Description
I'm making static miner that just mine for me when it run without any args required, but when I'm try to overwrite argv and argc program got core dump.
char *argvv[2];
argvv[0] = "./xmrig";
argvv[1] = "--help";
argv = argvv;
argc = 2;

it's what i'm trying to add to xmrig.cpp at int main func 

root@ubuntu:/home/ubuntu/xmrig/build# make -j$(nproc)
[  1%] Built target argon2-xop
[  2%] Built target ethash
[  4%] Built target argon2-sse2
[  4%] Built target argon2-avx512f
[  4%] Built target argon2-ssse3
[  5%] Built target argon2-avx2
[  7%] Built target xmrig-asm
[  9%] Built target argon2
Scanning dependencies of target xmrig
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
/home/ubuntu/xmrig/src/xmrig.cpp: In function ‘int main(int, char**)’:
/home/ubuntu/xmrig/src/xmrig.cpp:38:14: warning: ISO C++ forbids converting a string constant to ‘char*’ [-Wwrite-strings]
     argvv[0] = "./xmrig";
              ^
/home/ubuntu/xmrig/src/xmrig.cpp:39:14: warning: ISO C++ forbids converting a string constant to ‘char*’ [-Wwrite-strings]
     argvv[1] = "--help";
              ^
At global scope:
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
[ 10%] Linking CXX executable xmrig
[100%] Built target xmrig
root@ubuntu:/home/ubuntu/xmrig/build# ./xmrig
xmrig: src/unix/proctitle.c:53: uv_setup_args: Assertion `process_title.len + 1 == size' failed.
Aborted (core dumped)

and it's the error

# Discussion History
## Spudz76 | 2021-11-16T18:23:35+00:00
That's not how to accomplish what you're trying.

Use cmake option `-DWITH_EMBEDDED_CONFIG=ON` and edit `src/core/config/Config_default.h`.  Set whatever you need to be different from default.

## rubenh2905 | 2021-11-17T10:17:17+00:00
Thank about that, i will try it. But i'm still interested to overwrite argc and argv to prevent other argv later. My Platform is Ubuntu 16 and it have some unknown coredump not just in this program, on other programs i will get coredump while i do not enter argv in a pattern or enter some fields, it's a little random, what is the correct way to do that ? is there any course code that compatible with ubuntu 16 ?

## Spudz76 | 2021-11-17T16:24:31+00:00
argc/argv are obviously readonly inputs why would they ever be overwritable?

## rubenh2905 | 2021-11-18T06:39:34+00:00
yes they are readonly but we can make an other one and replace them with new references or just rename them to something like argcc/argvv and make a new argc/argv.

## Spudz76 | 2021-11-18T07:11:02+00:00
But

```
char *argvv[2];
argvv[0] = "./xmrig";
argvv[1] = "--help";
argv = argvv;
argc = 2;
```

That is overwriting argv/argc literally in the last two lines.  You would need to mass replace all argv/argc references with your proxy argvv/argcc since you can't reassign argv/argc.

# Action History
- Created by: rubenh2905 | 2021-11-16T12:29:14+00:00
- Closed at: 2021-11-29T18:28:12+00:00
