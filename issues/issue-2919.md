---
title: Link ncurses on ubuntu
source_url: https://github.com/monero-project/monero/issues/2919
author: danrmiller
assignees: []
labels:
- cmake
created_at: '2017-12-13T16:59:27+00:00'
updated_at: '2018-01-11T11:56:26+00:00'
type: issue
status: closed
closed_at: '2018-01-11T11:56:26+00:00'
---

# Original Description
I'll add an LDFLAG but is this something we should deal with?

https://build.getmonero.org/builders/monero-static-ubuntu-amd64/builds/3022

https://build.getmonero.org/builders/monero-static-ubuntu-amd64/builds/3022/steps/compile/logs/stdio
```
-- Found Readline: /usr/include  
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Failed
-- Could not find GNU readline library so building without readline support
```

https://build.getmonero.org/builders/monero-static-ubuntu-amd64/builds/3022/steps/compile/logs/CMakeError
```
/usr/bin/c++    -DZMQ_STATIC -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=x86-64   -fno-strict-aliasing -DGNU_READLINE_FOUND    CMakeFiles/cmTC_e928c.dir/src.cxx.o  -o cmTC_e928c -rdynamic /usr/lib/x86_64-linux-gnu/libreadline.a 
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_get_screen_size':
(.text+0x201): undefined reference to `tgetnum'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_get_screen_size':
(.text+0x2cb): undefined reference to `tgetnum'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x647): undefined reference to `PC'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x65a): undefined reference to `BC'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x665): undefined reference to `UP'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x6f3): undefined reference to `tgetent'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x72f): undefined reference to `tgetstr'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x75b): undefined reference to `PC'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x771): undefined reference to `BC'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x77f): undefined reference to `UP'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x78f): undefined reference to `tgetflag'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x7d0): undefined reference to `tgetflag'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x832): undefined reference to `tgetflag'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_init_terminal_io':
(.text+0x8fb): undefined reference to `tgetent'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_backspace':
(.text+0xad5): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `rl_ding':
(.text+0xb8f): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_enable_meta_key':
(.text+0xbf5): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_disable_meta_key':
(.text+0xc47): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In function `_rl_control_keypad':
(.text+0xc7b): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o):(.text+0xcbe): more undefined references to `tputs' follow
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In function `update_line':
(.text+0x2418): undefined reference to `tgoto'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In function `update_line':
(.text+0x242a): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In function `update_line':
(.text+0x2c26): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In function `update_line':
(.text+0x2e23): undefined reference to `tgoto'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In function `update_line':
(.text+0x2e33): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In function `update_line':
(.text+0x2ea1): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In function `update_line':
(.text+0x2ebd): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In function `update_line':
(.text+0x2eec): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In function `rl_redisplay':
(.text+0x4509): undefined reference to `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o):(.text+0x481c): more undefined references to `tputs' follow
collect2: error: ld returned 1 exit status
```

on OSX adding LDFLAGS="-ltermcap" works as shown in #2712 



# Discussion History
## danrmiller | 2017-12-13T17:02:09+00:00
+cmake

## moneromooo-monero | 2017-12-13T21:06:14+00:00
It's what pkg-config was made to fix, but AFAICT cmake uses their own custom "modules". Not sure whether hacking this in is a good idea or not tbh.

## jtgrassie | 2017-12-14T21:11:20+00:00
@danrmiller 
> on OSX adding LDFLAGS="-ltermcap" works as shown in #2712

That's for homebrew specific issue so somewhat unrelated IMO

@moneromooo-monero 
> It's what pkg-config was made to fix, but AFAICT cmake uses their own custom "modules". Not sure whether hacking this in is a good idea or not tbh.

Yes it's a tricky one.
I'm not quite sure why libreadline sometimes needs termcap linking too. It's certainly not a universal issue as plenty of compiles on different setups work without explicitly adding it. We could hack it in (e.g. check the found readline to see if it requires this extra linking of termcap but it feels like a hack to me. A bit more research needed me thinks.

## ston1th | 2017-12-18T10:35:41+00:00
Isn't this kind of related to this #2874?

~~We maybe also need to link `libcurses` on all linux platforms?~~

Edit: So I just learned libtermcap and libcurses are exactly the same file on OpenBSD.
@jtgrassie have you found a way how to tell when linking more libraries is needed?

## jtgrassie | 2017-12-18T13:19:01+00:00
I'm no cmake expert but we could just add `termcap` whenever `readline` is linked. Thoughts?

## ston1th | 2017-12-19T13:00:22+00:00
I'm not sure but since `readline` almost always needs `termcap` (either linked automatically or manually) we could try it.
Do we need to exclude windows? I'm not familiar of the readline situation over there.

Do things break if a library gets linked twice (this magic autolinking on some systems) or am I completely wrong there?

## danrmiller | 2017-12-19T13:12:46+00:00
No we don't need to exclude windows, windows is having the same situation as all of the other platforms (except where we have already handled it like openbsd) where the windows builds are not including readline because of undefined references to termcap/curses

## moneromooo-monero | 2017-12-19T13:57:24+00:00
Linking a lib twice is fine. You still need to check whether the lib is installed first (I did something similar for libunwind sometimes needing liblzma). It's a bit hacky though, as it assumes the first lib needs it, and that might not be the case. I'm not sure whether that makes the final binary dependent on the secondary lib in the case the primary lib doesn't actually need it.


## hyc | 2017-12-19T16:53:09+00:00
For static libraries there's no issue. For dynamic libraries, if the lib isn't actually needed, it will still be linked as a dependency of the binary, which is sloppy. 

## jtgrassie | 2017-12-19T17:47:28+00:00
I think we need to add another compile and link test. If this fails, repeat the test but this time linking against termcap also. If that then passes add the termcap dependency to the build, otherwise fall through to no supported readline. 

## jtgrassie | 2017-12-20T13:33:31+00:00
OK, so after much research, this looks like the best approach:

https://github.com/libretro/hatari/blob/master/cmake/FindReadline.cmake

If all agree I'll make the adjustments.

This is also nice as the libedit check can be changed to use the `check_function_exists` (which I didn't know about) rather than the explicit compile test.

## moneromooo-monero | 2017-12-20T14:06:51+00:00
The top level licence is GPL, so you'll have to either find it elsewhere, or rewrite it wholly.

## jtgrassie | 2017-12-20T14:45:53+00:00
I hadn't planned on lifting as-is, rather adjusting our module using the `check_function_exists` method.

## eklitzke | 2017-12-23T20:04:06+00:00
FWIW the dependency on libtinfo (or "libtermcap") is properly exposed via the DT_NEEDED field:

```
$ ldd /lib64/libreadline.so.7
	linux-vdso.so.1 (0x00007fffbdf88000)
	libtinfo.so.6 => /lib64/libtinfo.so.6 (0x00007f7a29194000)
	libc.so.6 => /lib64/libc.so.6 (0x00007f7a28db1000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f7a2960d000)
```

It's too bad that CMake can't do transitive linking dependencies based on this automatically. I found some old mailing list posts discussing this, but it looks like it was never implemented.

If I understand the upstream GNU Readline docs correctly, you always need to combine -lreadine with either -ltermcap/-ltinfo, or with -lcurses if Readline was compiled with the --with-curses option. From their docs:
```
`--with-curses'
    This tells readline that it can find the termcap library functions
    (tgetent, et al.) in the curses library, rather than a separate
    termcap library.  Readline uses the termcap functions, but does not
    link with the termcap or curses library itself, allowing applications
    which link with readline the to choose an appropriate library.
    This option tells readline to link the example programs with the
    curses library rather than libtermcap.
```

## jtgrassie | 2017-12-23T20:35:22+00:00
#2978 fixes this. But yes, frustrating cmake doesn't detect the dependencies by default.

## hyc | 2017-12-23T23:22:57+00:00
The DT_NEEDED field only exists in shared libraries, and the dynamic linker finds such dependencies automatically. There's no reason for cmake to bother with the issue then. The only reason this problem exists is when you're doing a static build, since static libraries lack this information.
It would be trivial to add a new record type to the static library format, to carry this dependency information. I've suggested this to the GNU binutils folks multiple times, but they're entirely uninterested in adopting the feature.
https://sourceware.org/ml/binutils/2017-09/msg00158.html

## jtgrassie | 2018-01-11T04:47:43+00:00
+close 
Fixed by #2978

## dEBRUYNE-1 | 2018-01-11T11:51:45+00:00
+resolved

# Action History
- Created by: danrmiller | 2017-12-13T16:59:27+00:00
- Closed at: 2018-01-11T11:56:26+00:00
