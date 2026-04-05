---
title: '[Solved] Build issue.'
source_url: https://github.com/xmrig/xmrig/issues/96
author: lolcocks123
assignees: []
labels:
- question
created_at: '2017-09-07T07:10:09+00:00'
updated_at: '2017-09-08T06:22:05+00:00'
type: issue
status: closed
closed_at: '2017-09-08T06:22:05+00:00'
---

# Original Description
I am trying to build xmrig but getting a shit load of 'undefined reference' errors.

I am using this:
https://github.com/xmrig/xmrig-deps/releases







`CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x7f): undefined refe
rence to `uv_signal_stop'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x99): undefined refe
rence to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x15c): undefined ref
erence to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x24b): undefined ref
erence to `uv_signal_start'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x260): undefined ref
erence to `uv_signal_start'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x275): undefined ref
erence to `uv_signal_start'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x2d2): undefined ref
erence to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x2dc): undefined ref
erence to `uv_run'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x2e3): undefined ref
erence to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x2eb): undefined ref
erence to `uv_loop_close'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x2f0): undefined ref
erence to `uv_tty_reset_mode'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x393): undefined ref
erence to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x49d): undefined ref
erence to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x4a9): undefined ref
erence to `uv_signal_init'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0xa6): undefined refe
rence to `uv_stop'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x169): undefined ref
erence to `uv_stop'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x39f): undefined ref
erence to `uv_stop'
CMakeFiles/xmrig.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0x52): undefi
ned reference to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0x66): undefi
ned reference to `uv_tty_init'
CMakeFiles/xmrig.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0x6e): undefi
ned reference to `uv_is_readable'
CMakeFiles/xmrig.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0x89): undefi
ned reference to `uv_tty_set_mode'
CMakeFiles/xmrig.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0x38): undefi
ned reference to `uv_close'
CMakeFiles/xmrig.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0xa4): undefi
ned reference to `uv_read_start'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x55):
undefined reference to `uv_is_writable'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x76):
undefined reference to `uv_guess_handle'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x1d6):
 undefined reference to `uv_write'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x22e):
 undefined reference to `uv_is_writable'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x248):
 undefined reference to `uv_guess_handle'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x2fa):
 undefined reference to `uv_write'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x32a):
 undefined reference to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x33e):
 undefined reference to `uv_tty_init'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x34c):
 undefined reference to `uv_tty_set_mode'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x3ac):
 undefined reference to `uv_is_writable'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x3c6):
 undefined reference to `uv_guess_handle'
CMakeFiles/xmrig.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x459):
 undefined reference to `uv_write'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x14): undefi
ned reference to `uv_fs_req_cleanup'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x12e): undef
ined reference to `uv_buf_init'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x14b): undef
ined reference to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x179): undef
ined reference to `uv_fs_write'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x293): undef
ined reference to `uv_buf_init'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x2b0): undef
ined reference to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x2d7): undef
ined reference to `uv_fs_write'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x310): undef
ined reference to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x335): undef
ined reference to `uv_fs_open'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x340): undef
ined reference to `uv_fs_req_cleanup'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x363): undef
ined reference to `uv_buf_init'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x380): undef
ined reference to `uv_default_loop'
CMakeFiles/xmrig.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x3ae): undef
ined reference to `uv_fs_write'
CMakeFiles/xmrig.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x370): undefin
ed reference to `uv_is_writable'
CMakeFiles/xmrig.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x3c8): undefin
ed reference to `uv_buf_init'`

# Discussion History
## xmrig | 2017-09-07T13:28:31+00:00
You trying build with wrong libuv version, maybe x86 version in x64 build or something like that.

## lolcocks123 | 2017-09-08T06:21:24+00:00
Thank you, that's exactly what happened, I had the x64 mingw path in environment variables instead of x86.

# Action History
- Created by: lolcocks123 | 2017-09-07T07:10:09+00:00
- Closed at: 2017-09-08T06:22:05+00:00
