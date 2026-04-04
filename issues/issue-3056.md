---
title: Cross-compiling fails running generate_translations_header
source_url: https://github.com/monero-project/monero/issues/3056
author: danrmiller
assignees: []
labels:
- cmake
created_at: '2018-01-03T20:01:10+00:00'
updated_at: '2022-04-08T14:30:21+00:00'
type: issue
status: closed
closed_at: '2022-04-08T14:30:21+00:00'
---

# Original Description
Since #2934 I cannot cross-compile because the `generate_translations_header` command is built for the target and run on the host. How should we handle this? Is there a convention for this?

I know @hyc cross-builds for ARM, and @MoroccanMalinois, so maybe they can help. Or @glv2 who wrote the change I refer to.

# Discussion History
## danrmiller | 2018-01-03T20:01:56+00:00
+cmake

## glv2 | 2018-01-04T10:42:01+00:00
@danrmiller could you check if PR #3062 improves things when cross-compiling?


## danrmiller | 2018-01-04T13:54:17+00:00
I don't know what I need to do to differentiate between when the host tools are used and when the target tools are used. Are there CMake variables I need to use? Am I explaining the issue alright?

`generate_translations_header` is run on the host, but this program will have been built for the target, because the CC and CXX environment variables point to the cross-compilers targeting android-arm. 


You can see the result here: 
https://build.getmonero.org/builders/monero-android-armv7/builds/1263/steps/compile/logs/stdio

```
[100%] Linking C executable generate_translations_header
Generating embedded translations header
./generate_translations_header: 1: ./generate_translations_header: Syntax error: word unexpected (expecting ")")
make[6]: *** [generate_translations_header] Error 2
make[6]: *** Deleting file `generate_translations_header'
```

## glv2 | 2018-01-04T14:58:03+00:00
For the Win64 build, running *generate_translations_header* doesn't work in the current master branch (a529f0a6c9a74a4a05205c75d5b3f726e8e58ea0):

```
Scanning dependencies of target generate_translations_header
make[3]: Leaving directory '/home/vagrant/slave/monero-static-win64/build/build/release'
make[3]: Entering directory '/home/vagrant/slave/monero-static-win64/build/build/release'
[  1%] Building C object translations/CMakeFiles/generate_translations_header.dir/generate_translations_header.c.obj
[  1%] Linking C executable generate_translations_header.exe
Generating embedded translations header
make[3]: Leaving directory '/home/vagrant/slave/monero-static-win64/build/build/release'
make[2]: Leaving directory '/home/vagrant/slave/monero-static-win64/build/build/release'
make[1]: Leaving directory '/home/vagrant/slave/monero-static-win64/build/build/release'
/bin/sh: generate_translations_header: command not found
make[3]: *** [translations/CMakeFiles/generate_translations_header.dir/build.make:98: translations/generate_translations_header.exe] Error 127
make[3]: *** Deleting file 'translations/generate_translations_header.exe'
make[2]: *** [CMakeFiles/Makefile2:86: translations/CMakeFiles/generate_translations_header.dir/all] Error 2
make[1]: *** [Makefile:129: all] Error 2
make: *** [Makefile:111: release-static-win64] Error 2
```

but it works with PR #3062 :

```
Scanning dependencies of target generate_translations_header
make[3]: Leaving directory '/home/vagrant/slave/monero-static-win64/build/build/release'
make[3]: Entering directory '/home/vagrant/slave/monero-static-win64/build/build/release'
[  0%] Creating directories for 'generate_translations_header'
[  0%] No download step for 'generate_translations_header'
[  0%] No patch step for 'generate_translations_header'
[  1%] No update step for 'generate_translations_header'
[  2%] Performing configure step for 'generate_translations_header'
-- The C compiler identification is GNU 7.2.0
-- The CXX compiler identification is GNU 7.2.0
-- Check for working C compiler: C:/msys64/mingw64/bin/gcc.exe
-- Check for working C compiler: C:/msys64/mingw64/bin/gcc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/msys64/mingw64/bin/g++.exe
-- Check for working CXX compiler: C:/msys64/mingw64/bin/g++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
CMake Warning at CMakeLists.txt:38 (message):
  lrelease program not found, translation files not built


-- Generating done
-- Build files have been written to: C:/msys64/home/vagrant/slave/monero-static-win64/build/build/release/translations
[  2%] Performing build step for 'generate_translations_header'
make[4]: Entering directory '/C/msys64/home/vagrant/slave/monero-static-win64/build/build/release/translations'
make[5]: Entering directory '/C/msys64/home/vagrant/slave/monero-static-win64/build/build/release/translations'
make[6]: Entering directory '/C/msys64/home/vagrant/slave/monero-static-win64/build/build/release/translations'
Scanning dependencies of target generate_translations_header
make[6]: Leaving directory '/C/msys64/home/vagrant/slave/monero-static-win64/build/build/release/translations'
make[6]: Entering directory '/C/msys64/home/vagrant/slave/monero-static-win64/build/build/release/translations'
[ 50%] Building C object CMakeFiles/generate_translations_header.dir/generate_translations_header.c.obj
[100%] Linking C executable generate_translations_header.exe
Generating embedded translations header
make[6]: Leaving directory '/C/msys64/home/vagrant/slave/monero-static-win64/build/build/release/translations'
[100%] Built target generate_translations_header
make[5]: Leaving directory '/C/msys64/home/vagrant/slave/monero-static-win64/build/build/release/translations'
make[4]: Leaving directory '/C/msys64/home/vagrant/slave/monero-static-win64/build/build/release/translations'
[  3%] Performing install step for 'generate_translations_header'

[  3%] Completed 'generate_translations_header'
make[3]: Leaving directory '/home/vagrant/slave/monero-static-win64/build/build/release'
[  3%] Built target generate_translations_header
```

So there is some improvement.

For the android-armv7 build (with PR #3062), the message:

```
./generate_translations_header: 1: ./generate_translations_header: Syntax error: word unexpected (expecting ")")
```

looks like a shell script error (I'm not sure what script would cause that). I think trying to run a binary compiled for the wrong architecture would print something like:

```
./generate_translations_header: cannot execute binary file: Exec format error
```

  

## glv2 | 2018-01-04T16:15:18+00:00
For the armv7 cross-compilation, if cmake peeks the armv7 toolchain instead of the x86_64 toolchain when configuring *generate_translations_header* because the ```CC``` and ```CXX``` environment variables are set to ```clang``` and ```clang++```, maybe it could be solved by not setting ```CC``` and ```CXX``` and using

```
cd build/release && cmake -D CMAKE_C_COMPILER=clang  -D CMAKE_CXX_COMPILER=clang++ -D BUILD_TESTS=OFF -D ARCH="armv7-a" -D STATIC=ON -D BUILD_64=OFF -D CMAKE_BUILD_TYPE=release -D BUILD_TAG="linux-armv7" ../.. && $(MAKE)
```

instead of

```
cd build/release && cmake -D BUILD_TESTS=OFF -D ARCH="armv7-a" -D STATIC=ON -D BUILD_64=OFF -D CMAKE_BUILD_TYPE=release -D BUILD_TAG="linux-armv7" ../.. && $(MAKE)
```

in the Makefile.

@danrmiller What do you think?


## glv2 | 2018-01-04T18:02:30+00:00
The monero-android-armv7 cross-compilation test in PR #3066 unsets the ```CC``` and ```CXX``` environment variables before building *generate_translations_header* to force *cmake* to find the toolchain for the host, but apparently some target toolchain binaries still get in the way (probably a ```PATH``` issue).

In https://build.getmonero.org/builders/monero-android-armv7/builds/1277/steps/compile/logs/stdio:

```
Scanning dependencies of target generate_translations_header
make[3]: Leaving directory `/home/vagrant/slave/monero-android-armv7/build/build/release'
make[3]: Entering directory `/home/vagrant/slave/monero-android-armv7/build/build/release'
[  1%] Creating directories for 'generate_translations_header'
[  1%] No download step for 'generate_translations_header'
[  1%] No patch step for 'generate_translations_header'
[  2%] No update step for 'generate_translations_header'
[  3%] Performing configure step for 'generate_translations_header'
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- broken
-- Configuring incomplete, errors occurred!

See also "/home/vagrant/slave/monero-android-armv7/build/build/release/translations/CMakeFiles/CMakeOutput.log".
See also "/home/vagrant/slave/monero-android-armv7/build/build/release/translations/CMakeFiles/CMakeError.log".
CMake Error at /usr/share/cmake-3.5/Modules/CMakeTestCCompiler.cmake:61 (message):
  The C compiler "/usr/bin/cc" is not able to compile a simple test program.

  It fails with the following output:

   Change Dir: /home/vagrant/slave/monero-android-armv7/build/build/release/translations/CMakeFiles/CMakeTmp

  Run Build Command:"/home/vagrant/android/tool32/bin/make" "cmTC_2827c/fast"

  make[4]: Entering directory
  `/home/vagrant/slave/monero-android-armv7/build/build/release/translations/CMakeFiles/CMakeTmp'

  /home/vagrant/android/tool32/bin/make -f
  CMakeFiles/cmTC_2827c.dir/build.make CMakeFiles/cmTC_2827c.dir/build

  make[5]: Entering directory
  `/home/vagrant/slave/monero-android-armv7/build/build/release/translations/CMakeFiles/CMakeTmp'

  Building C object CMakeFiles/cmTC_2827c.dir/testCCompiler.c.o

  /usr/bin/cc -o CMakeFiles/cmTC_2827c.dir/testCCompiler.c.o -c
  /home/vagrant/slave/monero-android-armv7/build/build/release/translations/CMakeFiles/CMakeTmp/testCCompiler.c

  as: unrecognized option '--64'

  make[5]: *** [CMakeFiles/cmTC_2827c.dir/testCCompiler.c.o] Error 1

  make[5]: Leaving directory
  `/home/vagrant/slave/monero-android-armv7/build/build/release/translations/CMakeFiles/CMakeTmp'

  make[4]: *** [cmTC_2827c/fast] Error 2

  make[4]: Leaving directory
  `/home/vagrant/slave/monero-android-armv7/build/build/release/translations/CMakeFiles/CMakeTmp'

CMake will not be able to correctly generate this project.
Call Stack (most recent call first):
  CMakeLists.txt:34 (project)


make[3]: *** [generate_translations_header-prefix/src/generate_translations_header-stamp/generate_translations_header-configure] Error 1
make[2]: *** [CMakeFiles/generate_translations_header.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release-static-android] Error 2
```

  

## danrmiller | 2018-01-04T18:26:19+00:00
OK I can adjust the paths for the build job, but do you know for which tools?

It seems this part is using /usr/bin/cc  - gcc-5 (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609 and /usr/bin/as GNU assembler (GNU Binutils for Ubuntu) 2.26.1 for a target of `x86_64-linux-gnu' which I would think is what we want for the step building generate_translations_header.

I'll look into it, but thanks, it seems like this will work.

## SpliffyMap | 2018-02-01T15:30:07+00:00
Do we have a solution for that: unrecognized option '--64' error?

## danrmiller | 2018-02-01T15:42:30+00:00
You need to make sure that the `as` run in this step is the one for the host and not the target. I'm sorry I've been busy with other things, I will add looking at this to my list for sometime over the next 2 days.

## SpliffyMap | 2018-02-01T22:04:15+00:00
Thank you @danrmiller  :+1: 

## danrmiller | 2018-02-05T20:37:57+00:00
I'm sorry I didn't have a chance to look at it this weekend. I found this approach we can try:

https://cmake.org/Wiki/CMake_Cross_Compiling#Using_executables_in_the_build_created_during_the_build

https://stackoverflow.com/questions/36173840/how-to-instruct-cmake-to-use-the-build-architecture-compiler/36294332#36294332


## JPig | 2018-03-22T03:39:35+00:00
Did anyone manage to solve this or is it still an issue, any workarounds/further insight would be much appreciated 🙂

## selsta | 2022-04-08T14:30:21+00:00
#4294

# Action History
- Created by: danrmiller | 2018-01-03T20:01:10+00:00
- Closed at: 2022-04-08T14:30:21+00:00
