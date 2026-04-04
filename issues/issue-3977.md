---
title: Error building from source for windows
source_url: https://github.com/monero-project/monero-gui/issues/3977
author: ronnkling
assignees: []
labels: []
created_at: '2022-07-21T10:23:00+00:00'
updated_at: '2022-07-24T15:40:35+00:00'
type: issue
status: closed
closed_at: '2022-07-24T15:40:35+00:00'
---

# Original Description
I'm trying to build from source and having an issue.

I have never had msys on this machine before so it is clean install.

The first thing is following the directions the step

Exit the MSYS shell using Alt+F4

Edit the properties for the MSYS2 Shell shortcut changing "msys2_shell.bat" to "msys2_shell.cmd -mingw64" for 64-bit builds or "msys2_shell.cmd -mingw32" for 32-bit builds

is incorrect now, there is no msys2_shell.bat in the shortcut

so I bring up the 64 bit window

![image](https://user-images.githubusercontent.com/2185334/180187215-d7f8c6cf-44ea-42a2-b957-a864a5153dd2.png)

and I do the following commands
pacman -Syu
pacman -S mingw-w64-x86_64-toolchain make mingw-w64-x86_64-cmake mingw-w64-x86_64-boost mingw-w64-x86_64-openssl mingw-w64-x86_64-zeromq mingw-w64-x86_64-libsodium mingw-w64-x86_64-hidapi mingw-w64-x86_64-unbound

used the git cmd window to clone monero

then in the msys window I did 

cd monero

make release-static-win64

and get this error

$ make release-static-win64
/bin/sh: line 1: git: command not found
mkdir -p build/"MINGW64_NT-10.0-19044/"/release
cd build/"MINGW64_NT-10.0-19044/"/release && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=../../../../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=C:/msys64/ ../../../.. && make
CMake Warning:
  Ignoring extra path from command line:

   "../../../.."


CMake Error: The source directory "C:/msys64/home/klingr" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
make: *** [Makefile:155: release-static-win64] Error 1
mkdir

# Discussion History
## selsta | 2022-07-21T13:38:55+00:00
> used the git cmd window to clone monero

Why? You have to use the `mingw64` shell for the whole process.

Your logs says `git: command not found` but `mingw-w64-x86_64-toolchain` installs `git`.

## ronnkling | 2022-07-21T23:52:19+00:00
I get an unrecognized command if I do that

![PDIeN1La0VIy92sl](https://user-images.githubusercontent.com/2185334/180410595-1a223f9e-1cdf-4e2b-b58e-ce884ec509ec.png)


## selsta | 2022-07-22T11:00:17+00:00
Try also to install `mingw-w64-x86_64-tools-git` and then post the full log.

## ronnkling | 2022-07-22T18:16:57+00:00
$ pacman -S  mingw-w64-x86_64-tools-git
warning: mingw-w64-x86_64-tools-git-10.0.0.r54.gb4116e310-1 is up to date -- reinstalling
resolving dependencies...
looking for conflicting packages...

Packages (1) mingw-w64-x86_64-tools-git-10.0.0.r54.gb4116e310-1

Total Installed Size:  0.98 MiB
Net Upgrade Size:      0.00 MiB

:: Proceed with installation? [Y/n] y
(1/1) checking keys in keyring                     [#####################] 100%
(1/1) checking package integrity                   [#####################] 100%
(1/1) loading package files                        [#####################] 100%
(1/1) checking for file conflicts                  [#####################] 100%
(1/1) checking available disk space                [#####################] 100%
:: Processing package changes...
(1/1) reinstalling mingw-w64-x86_64-tools-git      [#####################] 100%

klingr@Kronos4 MINGW64 ~
$ cd monero/

klingr@Kronos4 MINGW64 ~/monero
$ make release-statc-win64
/bin/sh: line 1: git: command not found
make: *** No rule to make target 'release-statc-win64'.  Stop.

This is really strange, the log does a reinstall I get the same error


## selsta | 2022-07-22T18:41:47+00:00
Something is wrong with your msys2 / mingw64 environment. If you install git you also should have git as an available command.

## ronnkling | 2022-07-23T16:49:32+00:00
I was able to fix this using pacman -S git

## selsta | 2022-07-23T17:52:55+00:00
Is this issue resolved now? Does monero build? To me it sounds like you started a normal msys2 shell, not in mingw64 mode.

## ronnkling | 2022-07-23T20:03:20+00:00
yes it does

On 7/23/2022 1:53 PM, selsta wrote:
>
> Is this issue resolved now? Does monero build?
>
> —
> Reply to this email directly, view it on GitHub 
> <https://github.com/monero-project/monero-gui/issues/3977#issuecomment-1193163544>, 
> or unsubscribe 
> <https://github.com/notifications/unsubscribe-auth/AAQVQ5TNEAZVIFRUX76W2N3VVQWQDANCNFSM54HC4PTQ>.
> You are receiving this because you authored the thread.Message ID: 
> ***@***.***>
>

# Action History
- Created by: ronnkling | 2022-07-21T10:23:00+00:00
- Closed at: 2022-07-24T15:40:35+00:00
