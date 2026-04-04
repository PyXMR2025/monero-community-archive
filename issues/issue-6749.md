---
title: 'CMake Error: Could not create named generator MSYS Makefiles'
source_url: https://github.com/monero-project/monero/issues/6749
author: jiebanghan
assignees: []
labels: []
created_at: '2020-08-07T07:50:19+00:00'
updated_at: '2022-02-19T04:18:26+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:18:26+00:00'
---

# Original Description
when I am on Window, I installed the msys2 environment  just  according to https://github.com/monero-project/monero.
and I installed cmake as command:
`pacman -S  cmake`
```
root@DESKTOP-EEM7CKJ MSYS ~/monero-project/monero
$ pacman -Ss cmake
mingw32/mingw-w64-i686-cmake 3.17.3-1
    A cross-platform open-source make system (mingw-w64)
mingw32/mingw-w64-i686-cmake-doc-qt 3.17.3-1
    CMake documentation in Qt Help format
mingw32/mingw-w64-i686-cotire 1.8.1_3.17-1
    CMake module to speed up builds (automated PCH, unity builds) (mingw-w64)
mingw32/mingw-w64-i686-extra-cmake-modules 5.68.0-1
    Extra CMake modules (mingw-w64)
mingw64/mingw-w64-x86_64-cmake 3.17.3-1 [已安装]
    A cross-platform open-source make system (mingw-w64)
mingw64/mingw-w64-x86_64-cmake-doc-qt 3.17.3-1
    CMake documentation in Qt Help format
mingw64/mingw-w64-x86_64-cotire 1.8.1_3.17-1
    CMake module to speed up builds (automated PCH, unity builds) (mingw-w64)
mingw64/mingw-w64-x86_64-extra-cmake-modules 5.68.0-1
    Extra CMake modules (mingw-w64)
msys/cmake 3.17.3-2 [已安装]
    A cross-platform open-source make system
msys/cmake-emacs 3.17.3-2
    A cross-platform open-source make system (Emacs mode)
msys/cmake-vim 3.17.3-2
    A cross-platform open-source make system (vim mode)
msys/icmake 9.03.01-1
    A program maintenance (make) utility using a C-like grammar

```
then I  begin to make  :

```
root@DESKTOP-EEM7CKJ MSYS ~/monero-project/monero
$ make release-static-win64
fatal: 不是一个 git 仓库（或者任何父目录）：.git
mkdir -p build/"MSYS_NT-10.0-18362/"/release
cd build/"MSYS_NT-10.0-18362/"/release && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=C:/tools/msys64/ ../../../.. && make
CMake Error: Could not create named generator MSYS Makefiles

Generators
* Unix Makefiles               = Generates standard UNIX makefiles.
  Ninja                        = Generates build.ninja files.
  Ninja Multi-Config           = Generates build-<Config>.ninja files.
  CodeBlocks - Ninja           = Generates CodeBlocks project files.
  CodeBlocks - Unix Makefiles  = Generates CodeBlocks project files.
  CodeLite - Ninja             = Generates CodeLite project files.
  CodeLite - Unix Makefiles    = Generates CodeLite project files.
  Sublime Text 2 - Ninja       = Generates Sublime Text 2 project files.
  Sublime Text 2 - Unix Makefiles
                               = Generates Sublime Text 2 project files.
  Kate - Ninja                 = Generates Kate project files.
  Kate - Unix Makefiles        = Generates Kate project files.
  Eclipse CDT4 - Ninja         = Generates Eclipse CDT 4.0 project files.
  Eclipse CDT4 - Unix Makefiles= Generates Eclipse CDT 4.0 project files.

make: *** [Makefile:155：release-static-win64] 错误 1
```
is shows above : CMake Error: Could not create named generator MSYS Makefiles. So how  to solve it ,thank you.

# Discussion History
## selsta | 2020-08-07T09:59:07+00:00
Did you clone the repository using git? Do you have git installed?

## iDunk5400 | 2020-08-07T10:02:26+00:00
You are trying to build in the wrong shell.

![msys2_wrong_shell](https://user-images.githubusercontent.com/20195079/89634321-773e5a80-d8a5-11ea-8b60-15097e0ca097.PNG)

Start the correct `MinGW-w64-Win64 Shell` (could also be called `MSYS2 MinGW 64-bit`) instead of `MSYS2 MSYS` shell.

![shell_instructions](https://user-images.githubusercontent.com/20195079/89634505-cedcc600-d8a5-11ea-9e2f-76fb6f2a64f4.PNG)


## jiebanghan | 2020-08-07T10:19:11+00:00
Thank you for @selsta 

> Did you clone the repository using git? Do you have git installed?
I did not clone, i just download  the zip file and unzip it to the aim directory.



## jiebanghan | 2020-08-07T10:20:42+00:00
Thank you for @iDunk5400 
Done after  did what you told me. It appears another error:

```
root@DESKTOP-EEM7CKJ MINGW64 ~/monero-project/monero
$ make release-static-win64
fatal: 不是一个 git 仓库（或者任何父目录）：.git
mkdir -p build/"MINGW64_NT-10.0-18362/"/release
cd build/"MINGW64_NT-10.0-18362/"/release && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=C:/tools/msys64/ ../../../.. && make
CMake Error: The source directory "C:/tools/msys64/home/root/monero-project" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
make: *** [Makefile:155：release-static-win64] 错误 1

```
would you please tell me how to  solve it? thank you .

## selsta | 2020-08-07T10:21:37+00:00
@jiebanghan You have to follow the README closely. please try `git clone --recursive https://github.com/monero-project/monero.git` to clone the repository, don’t download the .zip.

## jiebanghan | 2020-08-07T10:25:58+00:00
thank you for @iDunk5400 , the more exact information is below, the CMakeLists.txt   is at ~/monero-project/monero
```
root@DESKTOP-EEM7CKJ MINGW64 ~/monero-project/monero
$ make release-static-win64
fatal: 不是一个 git 仓库（或者任何父目录）：.git
mkdir -p build/"MINGW64_NT-10.0-18362/"/release
cd build/"MINGW64_NT-10.0-18362/"/release && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=C:/tools/msys64/ ../../../.. && make
CMake Error: The source directory "C:/tools/msys64/home/root/monero-project" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
make: *** [Makefile:155：release-static-win64] 错误 1

root@DESKTOP-EEM7CKJ MINGW64 ~/monero-project/monero
$ ls
ANONYMITY_NETWORKS.md  cmake           CMakeLists_IOS.txt  CONTRIBUTING.md  Doxyfile  include            LICENSE   README.i18n.md  src    translations  ZMQ.md
build                  CMakeLists.txt  contrib             Dockerfile       external  LEVIN_PROTOCOL.md  Makefile  README.md       tests  utils

root@DESKTOP-EEM7CKJ MINGW64 ~/monero-project/monero
$ pwd
/home/root/monero-project/monero
```


## jiebanghan | 2020-08-07T10:28:10+00:00
> @jiebanghan You have to follow the README closely. please try `git clone --recursive https://github.com/monero-project/monero.git` to clone the repository, don’t download the .zip.

thank you for @selsta. I will try it.

## jiebanghan | 2020-08-11T07:46:07+00:00
it  didi well after  done  according to @selsta @iDunk5400  's suggestion. thank you  @selsta @iDunk5400

# Action History
- Created by: jiebanghan | 2020-08-07T07:50:19+00:00
- Closed at: 2022-02-19T04:18:26+00:00
