---
title: Build on windows fails
source_url: https://github.com/monero-project/monero/issues/3714
author: Sylvyrfysh
assignees: []
labels: []
created_at: '2018-04-27T04:24:08+00:00'
updated_at: '2018-05-12T23:41:47+00:00'
type: issue
status: closed
closed_at: '2018-04-30T22:01:24+00:00'
---

# Original Description
I have followed the windows compile instructions, but the building fails with 
```
/C/msys64/mingw64/bin/cmake.exe -E remove -f CMakeFiles/cmTC_22620.dir/objects.a
ar cr CMakeFiles/cmTC_22620.dir/objects.a "CMakeFiles/cmTC_22620.dir/CheckFunctionExists.c.obj" 
/C/msys64/mingw64/bin/x86_64-w64-mingw32-gcc.exe  -fno-strict-aliasing -maes -std=c11 -D_GNU_SOURCE -m64 -DWIN32_LEAN_AND_MEAN  -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-error=unused-value -Wno-error=unused-but-set-variable -Waggregate-return -Wnested-externs -Wold-style-definition -Wstrict-prototypes -march=x86-64  -fPIC  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DCHECK_FUNCTION_EXISTS=rl_filename_completion_function    -Wl,--whole-archive CMakeFiles/cmTC_22620.dir/objects.a -Wl,--no-whole-archive  -o cmTC_22620.exe -Wl,--major-image-version,0,--minor-image-version,0 /C/msys64/mingw64/lib/libreadline.a -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 
C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0xa3f): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0xb6d): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0xbcf): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0x1895): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0x2a27): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0x2d21): more undefined references to `tputs' follow

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x20c): undefined reference to `tgetnum'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x2e9): undefined reference to `tgetnum'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x714): undefined reference to `tgetent'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x752): undefined reference to `tgetstr'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x7b3): undefined reference to `tgetflag'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x802): undefined reference to `tgetflag'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x877): undefined reference to `tgetflag'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xaf7): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xba9): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xc17): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xc6d): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xc9d): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xce0): more undefined references to `tputs' follow

collect2.exe: error: ld returned 1 exit status

make[2]: *** [CMakeFiles/cmTC_22620.dir/build.make:89: cmTC_22620.exe] Error 1
make[2]: Leaving directory '/c/Users/njohn/Documents/GitHub/monero/build/release/CMakeFiles/CMakeTmp'
make[1]: *** [Makefile:126: cmTC_22620/fast] Error 2
make[1]: Leaving directory '/c/Users/njohn/Documents/GitHub/monero/build/release/CMakeFiles/CMakeTmp'
```

In #3508, moneromoo suggests changing a line to `Readline_LIBRARY:FILEPATH=C:/msys64/mingw64/lib/libreadline.a libncurses.so`, but the build still fails, without touching or creating new CMakeError or CMakeLog files.

# Discussion History
## moneromooo-monero | 2018-04-27T07:17:19+00:00
Maybe add libtinfo.so too to this Readline_LIBTARY variable.


## Sylvyrfysh | 2018-04-28T02:06:58+00:00
That does not change the outcome, and fails with the same message.

## moneromooo-monero | 2018-04-28T08:16:38+00:00
Then find where tputs is defined on your system.

## Sylvyrfysh | 2018-04-30T22:01:24+00:00
Not sire how I fixed it, but it now works. Thanks!

## DavidOfDoncaster | 2018-05-12T23:40:27+00:00
@Sylvyrfysh Having the same issue... How did you resolve the issue? Adding libncurses.a vs .so?

## Sylvyrfysh | 2018-05-12T23:41:47+00:00
I added libncurses.a and libreadline.a, which fixed my problem.

On Sat, May 12, 2018, 18:40 DavidOfDoncaster <notifications@github.com>
wrote:

> @Sylvyrfysh <https://github.com/Sylvyrfysh> Having the same issue... How
> did you resolve the issue? Adding libncurses.a vs .so?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/3714#issuecomment-388590693>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AOafQCUFQp8bqLvlzGzTk4uMUT0XkW_5ks5tx3L0gaJpZM4Tpv6q>
> .
>


# Action History
- Created by: Sylvyrfysh | 2018-04-27T04:24:08+00:00
- Closed at: 2018-04-30T22:01:24+00:00
