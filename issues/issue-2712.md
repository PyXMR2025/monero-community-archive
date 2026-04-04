---
title: Finding readline on a mac
source_url: https://github.com/monero-project/monero/issues/2712
author: danrmiller
assignees: []
labels:
- cmake
created_at: '2017-10-23T04:05:09+00:00'
updated_at: '2018-01-17T00:31:07+00:00'
type: issue
status: closed
closed_at: '2018-01-17T00:31:07+00:00'
---

# Original Description
What environment variable do I need to set so libreadline is found on osx?
My readline was installed by brew to /Cellar/readline/7.0.3_1, and linked to /usr/local/opt/readline/lib/ and /usr/local/opt/readline/include/readline/

I've tried just setting the Readline_ROOT_DIR and Readline_ROOT_DIR and Readline_INCLUDE_DIR to several different things, and several combinations of only setting one or the other.

The readline it's finding in  /usr/include/readline is "editline" which comes with OSX.

https://build.getmonero.org/builders/monero-static-osx-10.11/builds/2695/steps/compile/logs/stdio

```
 environment:
  Readline_INCLUDE_DIR=/usr/local/opt/readline/include/readline
  Readline_ROOT_DIR=/usr/local/opt/readline
```
```
-- Found Readline: /usr/include  
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Failed
-- Could not find GNU readline library so building without readline support
```

# Discussion History
## danrmiller | 2017-10-23T04:10:32+00:00
+cmake

## moneromooo-monero | 2017-10-23T09:27:06+00:00
Is this "fake" readline coming with a rlconf.h ?

## danrmiller | 2017-10-23T13:04:03+00:00
No, its just history.h and readline.h, which are wrappers for libedit

## moneromooo-monero | 2017-10-23T13:42:00+00:00
Does https://github.com/monero-project/monero/pull/2719 help ?

## danrmiller | 2017-10-23T21:43:08+00:00
I think it does keep libedit from being found, but what do I need to do to find GNU libreadline from brew?

Can I make cmake log its search more verbosely?

```
$ ls -la /usr/local/opt/readline/lib/
total 1440
drwxr-xr-x  10 administrator  admin     340 Sep  7  2016 .
drwxr-xr-x  12 administrator  admin     408 Oct 22 14:37 ..
-r--r--r--   1 administrator  admin   40072 Oct 22 14:37 libhistory.7.0.dylib
lrwxr-xr-x   1 administrator  admin      20 Sep  7  2016 libhistory.7.dylib -> libhistory.7.0.dylib
-r--r--r--   1 administrator  admin   44976 Sep  7  2016 libhistory.a
lrwxr-xr-x   1 administrator  admin      20 Sep  7  2016 libhistory.dylib -> libhistory.7.0.dylib
-r--r--r--   1 administrator  admin  233828 Oct 22 14:37 libreadline.7.0.dylib
lrwxr-xr-x   1 administrator  admin      21 Sep  7  2016 libreadline.7.dylib -> libreadline.7.0.dylib
-r--r--r--   1 administrator  admin  396976 Sep  7  2016 libreadline.a
lrwxr-xr-x   1 administrator  admin      21 Sep  7  2016 libreadline.dylib -> libreadline.7.0.dylib
7715:bitmonero administrator$ ls -la /usr/local/opt/readline/include/readline
total 160
drwxr-xr-x  10 administrator  admin    340 Sep  7  2016 .
drwxr-xr-x   3 administrator  admin    102 Sep  7  2016 ..
-rw-r--r--   1 administrator  admin   4697 Sep  7  2016 chardefs.h
-rw-r--r--   1 administrator  admin  10627 Sep  7  2016 history.h
-rw-r--r--   1 administrator  admin   3163 Sep  7  2016 keymaps.h
-rw-r--r--   1 administrator  admin  38933 Sep  7  2016 readline.h
-rw-r--r--   1 administrator  admin   2830 Sep  7  2016 rlconf.h
-rw-r--r--   1 administrator  admin   1835 Sep  7  2016 rlstdc.h
-rw-r--r--   1 administrator  admin   3193 Sep  7  2016 rltypedefs.h
-rw-r--r--   1 administrator  admin   3046 Sep  7  2016 tilde.h
```

I've tried variations and combinations of the environment variables below:
```
Readline_INCLUDE_DIR="/usr/local/opt/readline/include/"  
Readline_INCLUDE_DIR="/usr/local/opt/readline/include/readline"
Readline_LIBRARY="/usr/local/opt/readline/lib/libreadline.a"
Readline_ROOT_DIR="/usr/local/opt/readline/lib/libreadline.a"
Readline_ROOT_DIR="/usr/local/opt/"
Readline_ROOT_DIR="/usr/local/opt/readline"
```
But I always get

-- Could not find GNU readline library so building without readline support



## moneromooo-monero | 2017-10-23T22:14:26+00:00
From the cmake config, I think it should be:

Readline_ROOT_DIR="/usr/local/opt/readline"

The other two seem to have good defaults, and I'm not sure they're user selectable anyway.

There are logs in build/foo/CMakeFiles, maybe grep -ir readline build/foo/CMakeFiles might spot something interesting.

BTW, looks like the cmake config can distinguish libedit from libreadline (allegedly anyway). So what I posted above might not be needed once libreadline is found.

## danrmiller | 2017-10-23T22:24:44+00:00
Thanks.
With only Readline_ROOT_DIR="/usr/local/opt/readline" set, I still get -- Could not find GNU readline library so building without readline support.

build/release/CMakeFiles/CMakeError.log (/usr/include/readline/readline.h looks like libedit):
```
Performing C++ SOURCE FILE Test GNU_READLINE_FOUND failed with the following output:
Change Dir: /Users/administrator/bitmonero/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_dbbb7/fast"
/Applications/Xcode.app/Contents/Developer/usr/bin/make -f CMakeFiles/cmTC_dbbb7.dir/build.make CMakeFiles/cmTC_dbbb7.dir/build
Building CXX object CMakeFiles/cmTC_dbbb7.dir/src.cxx.o
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++     -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wno-reorder -Wno-missing-field-initializers -march=native   -fno-strict-aliasing -DGTEST_HAS_TR1_TUPLE=0 -DGNU_READLINE_FOUND   -o CMakeFiles/cmTC_dbbb7.dir/src.cxx.o -c /Users/administrator/bitmonero/build/release/CMakeFiles/CMakeTmp/src.cxx
/Users/administrator/bitmonero/build/release/CMakeFiles/CMakeTmp/src.cxx:7:15: error: use of undeclared identifier 'rl_copy_text'; did you mean 'rl_kill_text'?
  char * s  = rl_copy_text(0, 0);
              ^~~~~~~~~~~~
              rl_kill_text
/usr/include/readline/readline.h:210:7: note: 'rl_kill_text' declared here
int              rl_kill_text(int, int);
                 ^
/Users/administrator/bitmonero/build/release/CMakeFiles/CMakeTmp/src.cxx:7:10: error: cannot initialize a variable of type 'char *' with an rvalue of type 'int'
  char * s  = rl_copy_text(0, 0);
         ^    ~~~~~~~~~~~~~~~~~~
2 errors generated.
make[2]: *** [CMakeFiles/cmTC_dbbb7.dir/src.cxx.o] Error 1
make[1]: *** [cmTC_dbbb7/fast] Error 2

Source file was:

#include <stdio.h>
#include <readline/readline.h>
int
main()
{
  char * s  = rl_copy_text(0, 0);
}
```


## moneromooo-monero | 2017-10-23T22:26:28+00:00
Do you have any hits for "rl_copy_text" in /usr/local/opt/readline/include ? And in the libedit headers ?

## danrmiller | 2017-10-23T22:30:05+00:00
/usr/local/opt/readline/include/readline/readline.h:extern char *rl_copy_text PARAMS((int, int));

Nothing in the libedit stuff in /usr/include/readline.


## moneromooo-monero | 2017-10-23T22:32:09+00:00
Is there a rl_kil_text in libedit headers ? Nevermind, I see the path to the header, it's trying libedit first, and then not trying the other next...

## danrmiller | 2017-10-23T22:34:33+00:00
/usr/include/readline/history.h:int              rl_kill_text(int, int);
/usr/include/readline/readline.h:int             rl_kill_text(int, int);


(assuming you mean rl_kill_text and not rl_kil_text)

## moneromooo-monero | 2017-10-23T22:35:12+00:00
Try this:
```
diff --git a/cmake/FindReadline.cmake b/cmake/FindReadline.cmake
index 9ccef7a..65b43b0 100644
--- a/cmake/FindReadline.cmake
+++ b/cmake/FindReadline.cmake
@@ -18,11 +18,13 @@
 #  Readline_INCLUDE_DIR      The readline include directories. 
 #  Readline_LIBRARY          The readline library.
 
-find_path(Readline_ROOT_DIR
-    NAMES include/readline/readline.h
-    PATHS /opt/local/ /usr/local/ /usr/
-    NO_DEFAULT_PATH
-)
+if (${Readline_ROOT_DIR} STREQUAL "")
+    find_path(Readline_ROOT_DIR
+        NAMES include/readline/readline.h
+        PATHS /opt/local/ /usr/local/ /usr/
+        NO_DEFAULT_PATH
+    )
+endif()
 
 find_path(Readline_INCLUDE_DIR
     NAMES readline/readline.h
```

## danrmiller | 2017-10-23T22:49:40+00:00
```
CMake Error at cmake/FindReadline.cmake:21 (if):
  if given arguments:

    "STREQUAL" ""

  Unknown arguments specified
Call Stack (most recent call first):
  CMakeLists.txt:682 (find_package)


-- Configuring incomplete, errors occurred!
```

## moneromooo-monero | 2017-10-23T22:54:46+00:00
OK, this instead. I see both raw and ${} and I have no idea what's the difference.

```
diff --git a/cmake/FindReadline.cmake b/cmake/FindReadline.cmake
index 9ccef7a..3c3907c 100644
--- a/cmake/FindReadline.cmake
+++ b/cmake/FindReadline.cmake
@@ -18,11 +18,13 @@
 #  Readline_INCLUDE_DIR      The readline include directories. 
 #  Readline_LIBRARY          The readline library.
 
-find_path(Readline_ROOT_DIR
-    NAMES include/readline/readline.h
-    PATHS /opt/local/ /usr/local/ /usr/
-    NO_DEFAULT_PATH
-)
+if (Readline_ROOT_DIR STREQUAL "")
+    find_path(Readline_ROOT_DIR
+        NAMES include/readline/readline.h
+        PATHS /opt/local/ /usr/local/ /usr/
+        NO_DEFAULT_PATH
+    )
+endif()
 
 find_path(Readline_INCLUDE_DIR
     NAMES readline/readline.h
```


## danrmiller | 2017-10-23T23:02:52+00:00
```
-- Could NOT find Readline (missing:  Readline_INCLUDE_DIR) 
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Failed
-- Could not find GNU readline library so building without readline support
```
```
Performing C++ SOURCE FILE Test GNU_READLINE_FOUND failed with the following output:
Change Dir: /Users/administrator/bitmonero/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_22bbe/fast"
/Applications/Xcode.app/Contents/Developer/usr/bin/make -f CMakeFiles/cmTC_22bbe.dir/build.make CMakeFiles/cmTC_22bbe.dir/build
Building CXX object CMakeFiles/cmTC_22bbe.dir/src.cxx.o
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++     -DZMQ_STATIC -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wno-reorder -Wno-missing-field-initializers -march=x86-64   -fno-strict-aliasing -DGTEST_HAS_TR1_TUPLE=0 -DGNU_READLINE_FOUND   -o CMakeFiles/cmTC_22bbe.dir/src.cxx.o -c /Users/administrator/bitmonero/build/release/CMakeFiles/CMakeTmp/src.cxx
/Users/administrator/bitmonero/build/release/CMakeFiles/CMakeTmp/src.cxx:7:15: error: use of undeclared identifier 'rl_copy_text'; did you mean 'rl_kill_text'?
  char * s  = rl_copy_text(0, 0);
              ^~~~~~~~~~~~
              rl_kill_text
/usr/include/readline/readline.h:210:7: note: 'rl_kill_text' declared here
int              rl_kill_text(int, int);
                 ^
/Users/administrator/bitmonero/build/release/CMakeFiles/CMakeTmp/src.cxx:7:10: error: cannot initialize a variable of type 'char *' with an rvalue of type 'int'
  char * s  = rl_copy_text(0, 0);
         ^    ~~~~~~~~~~~~~~~~~~
2 errors generated.
make[2]: *** [CMakeFiles/cmTC_22bbe.dir/src.cxx.o] Error 1
make[1]: *** [cmTC_22bbe/fast] Error 2

Source file was:

#include <stdio.h>
#include <readline/readline.h>
int
main()
{
  char * s  = rl_copy_text(0, 0);
}

```

## moneromooo-monero | 2017-10-23T23:08:01+00:00
do you make clean between tests ? cmake has an annoying tendency to cache stuff and forget to recreate when it should.

## danrmiller | 2017-10-23T23:10:54+00:00
Yes, I am running "make clean". I noticed on other platforms cmake caching and using where it previously found things in ~/.cmake but I don't see that here. I'll try as another user or get a clean build dir somehow and try again. 

## moneromooo-monero | 2017-10-23T23:16:30+00:00
Out of ideas then. Need to work out how to beat up cmake into submission with some obscure trick :/

## radfish | 2017-10-24T00:16:26+00:00
Yes, you definitely need to clear (rm -r) your build directory for library checks to change. make clean is not enough.
Also, how are you setting the Readline_ROOT_DIR? I'm not sure whether setting it via env var will take any effect. Did you try `cmake -DReadline_ROOT_DIR=/whatever/`?

You can use message("var ${var}") from within cmake/FindReadline.cmake to find out what it knows.

## moneromooo-monero | 2017-10-24T10:41:22+00:00
Do I have access to one of the machines where this happens ? If so, which one ?

## danrmiller | 2017-11-01T14:53:41+00:00
@moneromooo-monero Yes it happens on all of the osx machines I use, including what you have access to. If you'd like access to another or need the connection info, hit me up on irc.

@radfish Thanks, yes I was trying to set the cmake variables as environment variables. I seem to forget and make that mistake again every so often.

Here is the error with -DReadline_ROOT_DIR=/usr/local/opt/readline

```
Performing C++ SOURCE FILE Test GNU_READLINE_FOUND failed with the following output:
Change Dir: /Users/administrator/monero/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_d5a3f/fast"
/Applications/Xcode.app/Contents/Developer/usr/bin/make -f CMakeFiles/cmTC_d5a3f.dir/build.make CMakeFiles/cmTC_d5a3f.dir/build
Building CXX object CMakeFiles/cmTC_d5a3f.dir/src.cxx.o
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++    -I/usr/local/opt/readline/include  -DZMQ_STATIC -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURC
E   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-e
rror=undef -Wno-error=uninitialized -Wno-reorder -Wno-missing-field-initializers -march=x86-64   -fno-strict-aliasing -DGTEST_HAS_TR1_TUPLE=0 -DGNU_READLINE_FOUND   -o CMakeFiles/cmTC_d5a3f.di
r/src.cxx.o -c /Users/administrator/monero/build/release/CMakeFiles/CMakeTmp/src.cxx
Linking CXX executable cmTC_d5a3f
/usr/local/Cellar/cmake/3.6.2/bin/cmake -E cmake_link_script CMakeFiles/cmTC_d5a3f.dir/link.txt --verbose=1
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++    -DZMQ_STATIC -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wno-reorder -Wno-missing-field-initializers -march=x86-64   -fno-strict-aliasing -DGTEST_HAS_TR1_TUPLE=0 -DGNU_READLINE_FOUND -Wl,-search_paths_first -Wl,-headerpad_max_install_names   CMakeFiles/cmTC_d5a3f.dir/src.cxx.o  -o cmTC_d5a3f  /usr/local/opt/readline/lib/libreadline.a 
Undefined symbols for architecture x86_64:
  "_BC", referenced from:
      __rl_init_terminal_io in libreadline.a(terminal.o)
  "_PC", referenced from:
      __rl_init_terminal_io in libreadline.a(terminal.o)
  "_UP", referenced from:
      __rl_init_terminal_io in libreadline.a(terminal.o)
  "_tgetent", referenced from:
      __rl_init_terminal_io in libreadline.a(terminal.o)
  "_tgetflag", referenced from:
      __rl_init_terminal_io in libreadline.a(terminal.o)
  "_tgetnum", referenced from:
      __rl_get_screen_size in libreadline.a(terminal.o)
  "_tgetstr", referenced from:
      __rl_init_terminal_io in libreadline.a(terminal.o)
  "_tgoto", referenced from:
      _update_line in libreadline.a(display.o)
  "_tputs", referenced from:
      _rl_redisplay in libreadline.a(display.o)
      _update_line in libreadline.a(display.o)
      __rl_clear_to_eol in libreadline.a(display.o)
      __rl_move_vert in libreadline.a(display.o)
      __rl_move_cursor_relative in libreadline.a(display.o)
      _rl_clear_visible_line in libreadline.a(display.o)
      __rl_clear_screen in libreadline.a(display.o)
      ...
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[1]: *** [cmTC_d5a3f] Error 1
```


## hyc | 2017-11-01T15:19:25+00:00
Your readline needs -ltermcap or -lterminfo.

## jtgrassie | 2017-11-02T16:40:44+00:00
To add to @radfish's comment. I believe you will also need to set Readline_LIBRARY and Readline_INCLUDE_DIR (in addition to Readline_ROOT_DIR):

```
cmake -DReadline_ROOT_DIR=/usr/local/opt/readline -DReadline_INCLUDE_DIR=/usr/local/opt/readline/include/readline -DReadline_LIBRARY=/usr/local/opt/readline/lib/libreadline.a
```

As per @hyc's comment, you may may need to edit the the cmake file to also link against ncurses/termcap/terminfo (which ever your version of readline was built against). It's probably easier to add LDFLAGS for these in the environment though.

## danrmiller | 2017-11-20T01:37:57+00:00
Thanks.

```
$ LDFLAGS="-ltermcap" cmake  -DReadline_ROOT_DIR=/usr/local/opt/readline -DReadline_INCLUDE_DIR=/usr/local/opt/readline/include/readline -DReadline_LIBRARY=/usr/local/opt/readline/lib/libreadline.a -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release -D BUILD_TAG="mac-x64" ../.. 
```
```
-- Found Readline: /usr/local/opt/readline/include/readline  
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Failed
-- Could not find GNU readline library so building without readline support
```

CMakeFiles/CMakeError.log:
```
Performing C++ SOURCE FILE Test GNU_READLINE_FOUND failed with the following output:
Change Dir: /Users/administrator/monero/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_d3846/fast"
/Applications/Xcode.app/Contents/Developer/usr/bin/make -f CMakeFiles/cmTC_d3846.dir/build.make CMakeFiles/cmTC_d3846.dir/build
Building CXX object CMakeFiles/cmTC_d3846.dir/src.cxx.o
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   -I/usr/local/opt/readline/include/readline  -DZMQ_STATIC -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wno-reorder -Wno-missing-field-initializers -march=x86-64   -fno-strict-aliasing -DGTEST_HAS_TR1_TUPLE=0 -DGNU_READLINE_FOUND -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk   -o CMakeFiles/cmTC_d3846.dir/src.cxx.o -c /Users/administrator/monero/build/release/CMakeFiles/CMakeTmp/src.cxx
/Users/administrator/monero/build/release/CMakeFiles/CMakeTmp/src.cxx:7:15: error: use of undeclared identifier 'rl_copy_text'; did you mean 'rl_kill_text'?
  char * s  = rl_copy_text(0, 0);
              ^~~~~~~~~~~~
              rl_kill_text
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/usr/include/readline/readline.h:210:7: note: 'rl_kill_text' declared here
int              rl_kill_text(int, int);
                 ^
/Users/administrator/monero/build/release/CMakeFiles/CMakeTmp/src.cxx:7:10: error: cannot initialize a variable of type 'char *' with an rvalue of type 'int'
  char * s  = rl_copy_text(0, 0);
         ^    ~~~~~~~~~~~~~~~~~~
2 errors generated.
make[1]: *** [CMakeFiles/cmTC_d3846.dir/src.cxx.o] Error 1
make: *** [cmTC_d3846/fast] Error 2

Source file was:

#include <stdio.h>
#include <readline/readline.h>
int
main()
{
  char * s  = rl_copy_text(0, 0);
}

```

## jtgrassie | 2017-11-20T01:55:15+00:00
Your Readline_INCLUDE_DIR shouldn't have readline at the end. Because that's there, the the include in the test is picking up the Mac libedit header.


## danrmiller | 2017-11-20T07:58:35+00:00
Thanks @jtgrassie, it now finds libreadline.

I think a case could be made that installing libreadline via brew is a "standard" way of installing on OSX and we should support that. But even then, readline is a "keg-only" install, so its not linked from /Cellular to /usr/local/opt. I forced that link for purposes of this issue. 

And if we do that, I suppose we should also add  -ltermcap.

If that's the way to go, I'm sure I'll end up needing your help with the cmake files.


## hyc | 2017-11-20T11:18:27+00:00
By the way. we should probably change our `cmake/FindReadline.cmake` because our code no longer uses `rl_copy_text()`. 

## jtgrassie | 2017-11-20T11:45:16+00:00
@hyc I believe we still require GNU readline (not libedit) though so the test in the cmake file still seems worthwhile (even though we don't use that specific function anymore).

@danrmiller I totally agree we need to be supporting homebrew but I don't know enough about brew to know why it installed readline the way it did on your system. Do all brew installed libraries get installed in their own sub-directories or was it just readline?

## jtgrassie | 2017-11-20T11:54:18+00:00
@danrmiller OK I found this https://gist.github.com/matsuda/1280514
This seems like an odd decision as something installed to /usr/local wont conflict with the system libs. A minor change to the cmake file can account for homebrew I guess though.

## danrmiller | 2017-11-20T15:23:10+00:00
@jtgrassie wrote:
> Do all brew installed libraries get installed in their own sub-directories or was it just readline?

Brew libraries get installed in their own sub-directories, but they are usually then symlinked to /usr/local/. 

Readline is considered "keg-only" so it isn't linked because of the concerns about potential conflict with libedit, but you can force it with ```brew link --force```


## mridangam | 2017-12-23T08:59:58+00:00
Would it not be cleaner to do it in FindReadline.cmake like this:
```
find_path(Readline_ROOT_DIR
    NAMES include/readline/readline.h
    PATHS /usr/local/opt/readline/ /opt/local/ /usr/local/ /usr/
    NO_DEFAULT_PATH
)
```
Finds my brew-installed readline.

## danrmiller | 2018-01-17T00:31:07+00:00
Fixed by #2978 

# Action History
- Created by: danrmiller | 2017-10-23T04:05:09+00:00
- Closed at: 2018-01-17T00:31:07+00:00
