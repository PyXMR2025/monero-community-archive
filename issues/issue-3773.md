---
title: Make doesn't work since 12.0
source_url: https://github.com/monero-project/monero/issues/3773
author: Atrides
assignees: []
labels: []
created_at: '2018-05-07T17:30:34+00:00'
updated_at: '2018-05-08T15:19:17+00:00'
type: issue
status: closed
closed_at: '2018-05-08T15:19:17+00:00'
---

# Original Description
Since 0.12.0 version make command doesn't work anymore.
Used in ubuntu 16.04, all packets from README installed

```-- Found Git: /usr/bin/git
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.11") 
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring incomplete, errors occurred!
See also "/tmp/m/monero-master/build/release/CMakeFiles/CMakeOutput.log".
See also "/tmp/m/monero-master/build/release/CMakeFiles/CMakeError.log".
Makefile:68: die Regel für Ziel „release-static“ scheiterte
make: *** [release-static] Fehler 1
```
head of /tmp/m/monero-master/build/release/CMakeFiles/CMakeError.log:


```
Determining if the pthread_create exist failed with the following output:
Change Dir: /tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_bc3fa/fast"
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird betreten
/usr/bin/make -f CMakeFiles/cmTC_bc3fa.dir/build.make CMakeFiles/cmTC_bc3fa.dir/build
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird betreten
Building C object CMakeFiles/cmTC_bc3fa.dir/CheckSymbolExists.c.o
/usr/bin/cc     -o CMakeFiles/cmTC_bc3fa.dir/CheckSymbolExists.c.o   -c /tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp/CheckSymbolExists.c
Linking C executable cmTC_bc3fa
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_bc3fa.dir/link.txt --verbose=1
/usr/bin/cc       CMakeFiles/cmTC_bc3fa.dir/CheckSymbolExists.c.o  -o cmTC_bc3fa -rdynamic 
CMakeFiles/cmTC_bc3fa.dir/CheckSymbolExists.c.o: In Funktion `main':
CheckSymbolExists.c:(.text+0x16): Nicht definierter Verweis auf `pthread_create'
collect2: error: ld returned 1 exit status
CMakeFiles/cmTC_bc3fa.dir/build.make:97: die Regel für Ziel „cmTC_bc3fa“ scheiterte
make[2]: *** [cmTC_bc3fa] Fehler 1
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen
Makefile:126: die Regel für Ziel „cmTC_bc3fa/fast“ scheiterte
make[1]: *** [cmTC_bc3fa/fast] Fehler 2
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen

File /tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp/CheckSymbolExists.c:
/* */
#include <pthread.h>

int main(int argc, char** argv)
{
  (void)argv;
#ifndef pthread_create
  return ((int*)(&pthread_create))[argc];
#else
  (void)argc;
  return 0;
#endif
}

Determining if the function memset_s exists in the c failed with the following output:
Change Dir: /tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_3195b/fast"
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird betreten
/usr/bin/make -f CMakeFiles/cmTC_3195b.dir/build.make CMakeFiles/cmTC_3195b.dir/build
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird betreten
Building C object CMakeFiles/cmTC_3195b.dir/CheckFunctionExists.c.o
/usr/bin/cc    -DCHECK_FUNCTION_EXISTS=memset_s   -o CMakeFiles/cmTC_3195b.dir/CheckFunctionExists.c.o   -c /usr/share/cmake-3.5/Modules/CheckFunctionExists.c
Linking C executable cmTC_3195b
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_3195b.dir/link.txt --verbose=1
/usr/bin/cc   -DCHECK_FUNCTION_EXISTS=memset_s    CMakeFiles/cmTC_3195b.dir/CheckFunctionExists.c.o  -o cmTC_3195b  -L/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp/string.h -rdynamic -lc -Wl,-rpath,/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp/string.h 
CMakeFiles/cmTC_3195b.dir/CheckFunctionExists.c.o: In Funktion `main':
CheckFunctionExists.c:(.text+0x15): Nicht definierter Verweis auf `memset_s'
collect2: error: ld returned 1 exit status
CMakeFiles/cmTC_3195b.dir/build.make:97: die Regel für Ziel „cmTC_3195b“ scheiterte
make[2]: *** [cmTC_3195b] Fehler 1
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen
Makefile:126: die Regel für Ziel „cmTC_3195b/fast“ scheiterte
make[1]: *** [cmTC_3195b/fast] Fehler 2
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen


Determining if the function explicit_bzero exists in the c failed with the following output:
Change Dir: /tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_a1b73/fast"
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird betreten
/usr/bin/make -f CMakeFiles/cmTC_a1b73.dir/build.make CMakeFiles/cmTC_a1b73.dir/build
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird betreten
Building C object CMakeFiles/cmTC_a1b73.dir/CheckFunctionExists.c.o
/usr/bin/cc    -DCHECK_FUNCTION_EXISTS=explicit_bzero   -o CMakeFiles/cmTC_a1b73.dir/CheckFunctionExists.c.o   -c /usr/share/cmake-3.5/Modules/CheckFunctionExists.c
Linking C executable cmTC_a1b73
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_a1b73.dir/link.txt --verbose=1
/usr/bin/cc   -DCHECK_FUNCTION_EXISTS=explicit_bzero    CMakeFiles/cmTC_a1b73.dir/CheckFunctionExists.c.o  -o cmTC_a1b73  -L/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp/strings.h -rdynamic -lc -Wl,-rpath,/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp/strings.h 
CMakeFiles/cmTC_a1b73.dir/CheckFunctionExists.c.o: In Funktion `main':
CheckFunctionExists.c:(.text+0x15): Nicht definierter Verweis auf `explicit_bzero'
collect2: error: ld returned 1 exit status
CMakeFiles/cmTC_a1b73.dir/build.make:97: die Regel für Ziel „cmTC_a1b73“ scheiterte
make[2]: *** [cmTC_a1b73] Fehler 1
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen
Makefile:126: die Regel für Ziel „cmTC_a1b73/fast“ scheiterte
make[1]: *** [cmTC_a1b73/fast] Fehler 2
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen


Determining if the -Wl,-z,noexecheap linker flag is suppored failed with the following output:
Change Dir: /tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_0cd82/fast"
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird betreten
/usr/bin/make -f CMakeFiles/cmTC_0cd82.dir/build.make CMakeFiles/cmTC_0cd82.dir/build
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird betreten
Building C object CMakeFiles/cmTC_0cd82.dir/CheckLinkerFlag.c.o
/usr/bin/cc    -Wl,-z,noexecheap    -Wl,-z,noexecheap -o CMakeFiles/cmTC_0cd82.dir/CheckLinkerFlag.c.o   -c /tmp/m/monero-master/cmake/CheckLinkerFlag.c
Linking C executable cmTC_0cd82
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_0cd82.dir/link.txt --verbose=1
/usr/bin/cc  -Wl,-z,noexecheap     CMakeFiles/cmTC_0cd82.dir/CheckLinkerFlag.c.o  -o cmTC_0cd82 -rdynamic 
/usr/bin/ld: warning: -z noexecheap ignored.
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen


```


tail -n 100 of error file:

```make[2]: *** [cmTC_3da22] Fehler 1
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen
Makefile:126: die Regel für Ziel „cmTC_3da22/fast“ scheiterte
make[1]: *** [cmTC_3da22/fast] Fehler 2
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen


Determining if the function rl_filename_completion_function exists failed with the following output:
Change Dir: /tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_f83ad/fast"
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird betreten
/usr/bin/make -f CMakeFiles/cmTC_f83ad.dir/build.make CMakeFiles/cmTC_f83ad.dir/build
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird betreten
Building C object CMakeFiles/cmTC_f83ad.dir/CheckFunctionExists.c.o
/usr/bin/cc    -fno-strict-aliasing -maes -std=c11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Waggregate-return -Wnested-externs -Wold-style-definition -Wstrict-prototypes -march=x86-64  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DCHECK_FUNCTION_EXISTS=rl_filename_completion_function   -o CMakeFiles/cmTC_f83ad.dir/CheckFunctionExists.c.o   -c /usr/share/cmake-3.5/Modules/CheckFunctionExists.c
/usr/share/cmake-3.5/Modules/CheckFunctionExists.c:6:1: warning: function declaration isn’t a prototype [-Wstrict-prototypes]
 char CHECK_FUNCTION_EXISTS();
 ^
Linking C executable cmTC_f83ad
/usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_f83ad.dir/link.txt --verbose=1
/usr/bin/cc   -fno-strict-aliasing -maes -std=c11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Waggregate-return -Wnested-externs -Wold-style-definition -Wstrict-prototypes -march=x86-64  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DCHECK_FUNCTION_EXISTS=rl_filename_completion_function    CMakeFiles/cmTC_f83ad.dir/CheckFunctionExists.c.o  -o cmTC_f83ad -rdynamic /usr/lib/x86_64-linux-gnu/libreadline.a 
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `_rl_move_cursor_relative':
(.text+0xe64): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `_rl_move_cursor_relative':
(.text+0xeb5): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `_rl_move_cursor_relative':
(.text+0xf9d): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `_rl_move_vert':
(.text+0x1032): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `_rl_move_vert':
(.text+0x1085): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o):(.text+0x1ed4): Weitere nicht definierte Verweise auf `tputs' folgen
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `update_line':
(.text+0x2418): Nicht definierter Verweis auf `tgoto'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `update_line':
(.text+0x242a): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `update_line':
(.text+0x2c26): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `update_line':
(.text+0x2e23): Nicht definierter Verweis auf `tgoto'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `update_line':
(.text+0x2e33): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `update_line':
(.text+0x2ea1): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `update_line':
(.text+0x2ebd): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `update_line':
(.text+0x2eec): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o): In Funktion `rl_redisplay':
(.text+0x4509): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(display.o):(.text+0x481c): Weitere nicht definierte Verweise auf `tputs' folgen
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_get_screen_size':
(.text+0x201): Nicht definierter Verweis auf `tgetnum'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_get_screen_size':
(.text+0x2cb): Nicht definierter Verweis auf `tgetnum'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x647): Nicht definierter Verweis auf `PC'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x65a): Nicht definierter Verweis auf `BC'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x665): Nicht definierter Verweis auf `UP'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x6f3): Nicht definierter Verweis auf `tgetent'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x72f): Nicht definierter Verweis auf `tgetstr'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x75b): Nicht definierter Verweis auf `PC'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x771): Nicht definierter Verweis auf `BC'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x77f): Nicht definierter Verweis auf `UP'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x78f): Nicht definierter Verweis auf `tgetflag'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x7d0): Nicht definierter Verweis auf `tgetflag'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x832): Nicht definierter Verweis auf `tgetflag'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_init_terminal_io':
(.text+0x8fb): Nicht definierter Verweis auf `tgetent'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_backspace':
(.text+0xad5): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `rl_ding':
(.text+0xb8f): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_enable_meta_key':
(.text+0xbf5): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_disable_meta_key':
(.text+0xc47): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o): In Funktion `_rl_control_keypad':
(.text+0xc7b): Nicht definierter Verweis auf `tputs'
/usr/lib/x86_64-linux-gnu/libreadline.a(terminal.o):(.text+0xcbe): Weitere nicht definierte Verweise auf `tputs' folgen
collect2: error: ld returned 1 exit status
CMakeFiles/cmTC_f83ad.dir/build.make:98: die Regel für Ziel „cmTC_f83ad“ scheiterte
make[2]: *** [cmTC_f83ad] Fehler 1
make[2]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen
Makefile:126: die Regel für Ziel „cmTC_f83ad/fast“ scheiterte
make[1]: *** [cmTC_f83ad/fast] Fehler 2
make[1]: Verzeichnis „/tmp/m/monero-master/build/release/CMakeFiles/CMakeTmp“ wird verlassen


```


# Discussion History
## moneromooo-monero | 2018-05-07T18:25:13+00:00
See above in the console output for the actual error.

## Atrides | 2018-05-08T00:00:24+00:00
Please close, it's related to #3495 

## Atrides | 2018-05-08T00:24:11+00:00
May be you can notice in README to have boost >=1.62 because with 1.58 it doesn't work
Ubuntu 16.04 LTS has only 1.58, therefore new boost must be compiled

# Action History
- Created by: Atrides | 2018-05-07T17:30:34+00:00
- Closed at: 2018-05-08T15:19:17+00:00
