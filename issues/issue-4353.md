---
title: Need "make" twice.
source_url: https://github.com/monero-project/monero/issues/4353
author: ViperRu
assignees: []
labels: []
created_at: '2018-09-09T15:21:21+00:00'
updated_at: '2018-12-01T12:13:25+00:00'
type: issue
status: closed
closed_at: '2018-12-01T12:13:25+00:00'
---

# Original Description
There is the error after first trying "make":
```
-- AES support enabled
-- Found Boost Version: 105800
-- Could NOT find Readline (missing:  Readline_INCLUDE_DIR Readline_LIBRARY) 
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - not found
-- Looking for rl_copy_text
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Readline_LIBRARY
    linked by target "cmTC_3a02d" in directory /home/monero/bitmonero/build/release/CMakeFiles/CMakeTmp

CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Readline_LIBRARY
    linked by target "cmTC_483b1" in directory /home/monero/bitmonero/build/release/CMakeFiles/CMakeTmp

CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Looking for rl_filename_completion_function - not found
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
-- Could NOT find GTest (missing:  GTEST_LIBRARY GTEST_MAIN_LIBRARY) 
-- GTest not found on the system: will use GTest bundled with this source
Doxygen: graphviz not found - graphs disabled
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.7") 
-- Performing Test HAVE_C11
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Readline_LIBRARY
    linked by target "cmTC_2f975" in directory /home/monero/bitmonero/build/release/CMakeFiles/CMakeTmp

CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Performing Test HAVE_C11 - Failed
-- Configuring incomplete, errors occurred!
See also "/home/monero/bitmonero/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/monero/bitmonero/build/release/CMakeFiles/CMakeError.log".
make: *** [release-all] Error 1
```
The repeat of the "make" continues to build the project.
```
> dpkg -l | grep cmake
ii  cmake3                                      3.5.1-1ubuntu3~14.04.1                               amd64        cross-platform, open-source make system
ii  cmake3-data                                 3.5.1-1ubuntu3~14.04.1                               all          CMake data files (modules, templates and documentation)
```
```

# Discussion History
## jtgrassie | 2018-09-10T12:08:12+00:00
What version of gcc are you using? 

## ViperRu | 2018-09-12T21:38:50+00:00
```
> gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/5/lto-wrapper
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 5.5.0-12ubuntu1~14.04' --with-bugurl=file:///usr/share/doc/gcc-5/README.Bugs --enable-languages=c,ada,c++,java,go,d,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-5 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=gcc4-compatible --disable-libstdcxx-dual-abi --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --with-system-zlib --disable-browser-plugin --enable-java-awt=gtk --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-5-amd64/jre --enable-java-home --with-jvm-root-dir=/usr/lib/jvm/java-1.5.0-gcj-5-amd64 --with-jvm-jar-dir=/usr/lib/jvm-exports/java-1.5.0-gcj-5-amd64 --with-arch-directory=amd64 --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --enable-objc-gc --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 5.5.0 20171010 (Ubuntu 5.5.0-12ubuntu1~14.04)
```

## moneromooo-monero | 2018-09-14T11:27:25+00:00
It seems to be a bug in the cmake module for readline detection, or its use in the cmake machinery.

## jtgrassie | 2018-09-14T11:32:41+00:00
I'm not sure that's correct. `-- Performing Test HAVE_C11 - Failed` is a flag to me. @ViperRu can you pastebin the cmake logs please.

## moneromooo-monero | 2018-09-14T11:40:56+00:00
Oh, good spotting, you may be onto something here.

## ViperRu | 2018-09-18T11:08:12+00:00
https://pastebin.com/aP2rgsTW
https://pastebin.com/peF9bGtY

## moneromooo-monero | 2018-10-09T11:07:46+00:00
"int main(void) { return 0; }" is valid C11 AFAIK. If it's failing to compile this, maybe your compiler does not have C11 support. Try:

<pre>
echo 'int main(void) { return 0; }' | gcc -x c -std=c11 - && echo $?
</pre>

## ViperRu | 2018-10-10T12:24:34+00:00
```
~ > echo 'int main(void) { return 0; }' | gcc -x c -std=c11 - && echo $?
0
~ > 
```


## moneromooo-monero | 2018-10-10T12:39:44+00:00
Did you update GCC or binutils or the like since then ? Does a make clean && make still break the same way ?

## ViperRu | 2018-10-10T12:58:24+00:00
```
~ > sudo apt-get dist-upgrade
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
~ > git pull
Already up-to-date.
~ > make clean
WARNING: Back-up your wallet if it exists within ./build/Linux/master!
This will destroy the build directory, continue (y/N)?: y
rm -rf build/"Linux/master"
~ > make
...
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Readline_LIBRARY
    linked by target "cmTC_d32fb" in directory /home/bitmonero/build/Linux/master/release/CMakeFiles/CMakeTmp

CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Readline_LIBRARY
    linked by target "cmTC_c3b91" in directory /home/bitmonero/build/Linux/master/release/CMakeFiles/CMakeTmp

CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Looking for rl_filename_completion_function - not found
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
-- Could NOT find GTest (missing:  GTEST_LIBRARY GTEST_MAIN_LIBRARY) 
-- GTest not found on the system: will use GTest bundled with this source
Doxygen: graphviz not found - graphs disabled
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.7") 
-- Performing Test HAVE_C11
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Readline_LIBRARY
    linked by target "cmTC_0257d" in directory /home/bitmonero/build/Linux/master/release/CMakeFiles/CMakeTmp

CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Performing Test HAVE_C11 - Failed
-- Configuring incomplete, errors occurred!
See also "/home/bitmonero/build/Linux/master/release/CMakeFiles/CMakeOutput.log".
See also "/home/bitmonero/build/Linux/master/release/CMakeFiles/CMakeError.log".
make: *** [release-all] Error 1
```

## moneromooo-monero | 2018-10-10T15:32:14+00:00
This is really odd, since the cmake log you posted earlier has cmake fail on that same small program...

## moneromooo-monero | 2018-10-26T11:48:03+00:00
Does https://github.com/monero-project/monero/pull/4730 help ?

## moneromooo-monero | 2018-11-04T23:29:55+00:00
ping

## ViperRu | 2018-12-01T12:13:25+00:00
Hello, Sorry for delay. The problem is solved. Thank you.

# Action History
- Created by: ViperRu | 2018-09-09T15:21:21+00:00
- Closed at: 2018-12-01T12:13:25+00:00
