---
title: 'debug build: epee-related build error on macOS M1'
source_url: https://github.com/monero-project/monero/issues/9486
author: philipmw
assignees: []
labels:
- reproduction needed
- build system
created_at: '2024-09-15T20:32:12+00:00'
updated_at: '2024-09-15T21:39:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am trying to build the source tagged `v0.18.3.4` on a MacBook Air M1 running macOS 14.6.1 (23G93).

I installed dependencies using Homebrew as per the README. All dependencies are up-to-date as of today.

My command: `make debug`

The error:

```
[ 32%] Building CXX object contrib/epee/src/CMakeFiles/obj_epee_readline.dir/readline_buffer.cpp.o
[ 32%] Built target obj_epee_readline
[ 33%] Linking CXX shared library libepee_readline.dylib
ld: warning: -undefined error is deprecated
Undefined symbols for architecture arm64:
  "epee::string_tools::trim_right(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>&)", referenced from:
      handle_line(char*) in readline_buffer.cpp.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[3]: *** [contrib/epee/src/libepee_readline.dylib] Error 1
make[2]: *** [contrib/epee/src/CMakeFiles/epee_readline.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [debug] Error 2
```

The same error also occurs when building using dependencies provided by Nix (unstable channel) instead of Homebrew.

I am attaching the full build log:
[build.log](https://github.com/user-attachments/files/17007333/build.log)

# Discussion History
## selsta | 2024-09-15T21:23:26+00:00
Since this is a debug build, do the same issues happen with a release build? Also can you share which command you used to build?

## philipmw | 2024-09-15T21:33:14+00:00
For the attached log, I used `make debug` as my command. After making the log, I realized that it omits some of the build process because I am repeating it without cleaning the build directory. I can redo the log from a clean state, if needed.

When I try to build using just `make` (without `debug`), I do *not* run into this problem:

```
[ 23%] Linking CXX static library libepee.a
[ 23%] Built target epee
[ 23%] Building CXX object contrib/epee/src/CMakeFiles/obj_epee_readline.dir/readline_buffer.cpp.o
[ 23%] Built target obj_epee_readline
[ 23%] Linking CXX static library libepee_readline.a
[ 23%] Built target epee_readline
```

## selsta | 2024-09-15T21:34:57+00:00
The second build error you posted is expected without applying https://github.com/monero-project/monero/pull/9450 / https://github.com/monero-project/monero/pull/9462

## selsta | 2024-09-15T21:36:00+00:00
It seems the issue is specifically debug related, can you update the issue title to add debug build?

# Action History
- Created by: philipmw | 2024-09-15T20:32:12+00:00
