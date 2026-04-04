---
title: 'Building macOS non-vendored dependencies fail on macOS Big Sur  '
source_url: https://github.com/monero-project/monero/issues/7871
author: kwvg
assignees: []
labels: []
created_at: '2021-08-16T14:55:23+00:00'
updated_at: '2022-05-25T10:28:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Description

Monero's non-vendored dependencies do not build on macOS Big Sur 11.5. Cause is attributed to a change in macOS Big Sur, for more information see https://github.com/ponylang/ponyc/issues/3684.

[Doesn't seem to have been addressed by `libiconv`](https://fossies.org/linux/libiconv/ChangeLog)

## Steps to reproduce

```
$ git clone https://github.com/monero-project/monero --recurse-submodules
$ cd monero
$ make depends target=x86_64-apple-darwin20 # fails at building libiconv
...
Preprocessing libiconv...
patching file preload/configure
Configuring libiconv...
checking for a BSD-compatible install... /usr/local/bin/ginstall -c
checking whether build environment is sane... yes
checking for x86_64-apple-darwin20-strip... no
checking for strip... strip
checking for a thread-safe mkdir -p... /usr/local/bin/gmkdir -p
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make sets $(MAKE)... (cached) yes
checking for x86_64-apple-darwin20-gcc... /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -mmacosx-version-min=10.8
checking whether the C compiler works... no
configure: error: in `[deleted]/contrib/depends/work/build/x86_64-apple-darwin20/libiconv/1.15-16e8a1a0ad0':
configure: error: C compiler cannot create executables
See `config.log' for more details
```

## System information

* `uname -a`

```
Darwin 20.6.0 Darwin Kernel Version 20.6.0: Wed Jun 23 00:26:31 PDT 2021; root:xnu-7195.141.2~5/RELEASE_X86_64 x86_64
```

* `config.log`
```
configure:4117: $? = 1
configure:4137: checking whether the C compiler works
configure:4159: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -mmacosx-version-min=10$
ld: library not found for -lSystem
clang: error: linker command failed with exit code 1 (use -v to see invocation)
configure:4163: $? = 1
configure:4201: result: no
configure: failed program was:
| /* confdefs.h */
| #define PACKAGE_NAME "libiconv"
| #define PACKAGE_TARNAME "libiconv"
| #define PACKAGE_VERSION "1.15"
| #define PACKAGE_STRING "libiconv 1.15"
| #define PACKAGE_BUGREPORT ""
| #define PACKAGE_URL ""
| #define PACKAGE "libiconv"
| #define VERSION "1.15"
| /* end confdefs.h.  */
|
| int
| main ()
| {
|
|   ;
|   return 0;
| }
configure:4206: error: in `[deleted]/depends/work/build/x86_64-apple-darwin20/libiconv/1.15-16e8a1a0a$
configure:4208: error: C compiler cannot create executables
See `config.log' for more details
```

# Discussion History
## selsta | 2021-08-16T14:58:18+00:00
`make depends` cross compiling to Mac currently only works on Linux unfortunately.

## BEET-ONLINE | 2021-08-23T17:32:07+00:00
> ## Description
> Monero's non-vendored dependencies do not build on macOS Big Sur 11.5. Cause is attributed to a change in macOS Big Sur, for more information see [ponylang/ponyc#3684](https://github.com/ponylang/ponyc/issues/3684).
> 
> [Doesn't seem to have been addressed by `libiconv`](https://fossies.org/linux/libiconv/ChangeLog)
> 
> ## Steps to reproduce
> ```
> $ git clone https://github.com/monero-project/monero --recurse-submodules
> $ cd monero
> $ make depends target=x86_64-apple-darwin20 # fails at building libiconv
> ...
> Preprocessing libiconv...
> patching file preload/configure
> Configuring libiconv...
> checking for a BSD-compatible install... /usr/local/bin/ginstall -c
> checking whether build environment is sane... yes
> checking for x86_64-apple-darwin20-strip... no
> checking for strip... strip
> checking for a thread-safe mkdir -p... /usr/local/bin/gmkdir -p
> checking for gawk... no
> checking for mawk... no
> checking for nawk... no
> checking for awk... awk
> checking whether make sets $(MAKE)... yes
> checking whether make supports nested variables... yes
> checking whether make sets $(MAKE)... (cached) yes
> checking for x86_64-apple-darwin20-gcc... /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -mmacosx-version-min=10.8
> checking whether the C compiler works... no
> configure: error: in `[deleted]/contrib/depends/work/build/x86_64-apple-darwin20/libiconv/1.15-16e8a1a0ad0':
> configure: error: C compiler cannot create executables
> See `config.log' for more details
> ```
> 
> ## System information
> * `uname -a`
> 
> ```
> Darwin 20.6.0 Darwin Kernel Version 20.6.0: Wed Jun 23 00:26:31 PDT 2021; root:xnu-7195.141.2~5/RELEASE_X86_64 x86_64
> ```
> 
> * `config.log`
> 
> ```
> configure:4117: $? = 1
> configure:4137: checking whether the C compiler works
> configure:4159: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -mmacosx-version-min=10$
> ld: library not found for -lSystem
> clang: error: linker command failed with exit code 1 (use -v to see invocation)
> configure:4163: $? = 1
> configure:4201: result: no
> configure: failed program was:
> | /* confdefs.h */
> | #define PACKAGE_NAME "libiconv"
> | #define PACKAGE_TARNAME "libiconv"
> | #define PACKAGE_VERSION "1.15"
> | #define PACKAGE_STRING "libiconv 1.15"
> | #define PACKAGE_BUGREPORT ""
> | #define PACKAGE_URL ""
> | #define PACKAGE "libiconv"
> | #define VERSION "1.15"
> | /* end confdefs.h.  */
> |
> | int
> | main ()
> | {
> |
> |   ;
> |   return 0;
> | }
> configure:4206: error: in `[deleted]/depends/work/build/x86_64-apple-darwin20/libiconv/1.15-16e8a1a0a$
> configure:4208: error: C compiler cannot create executables
> See `config.log' for more details
> ```



# Action History
- Created by: kwvg | 2021-08-16T14:55:23+00:00
