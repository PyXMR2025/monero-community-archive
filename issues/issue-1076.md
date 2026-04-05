---
title: how to compile with QT creator cmake
source_url: https://github.com/xmrig/xmrig/issues/1076
author: sherifomran
assignees: []
labels:
- question
created_at: '2019-07-28T05:26:26+00:00'
updated_at: '2019-07-28T15:14:48+00:00'
type: issue
status: closed
closed_at: '2019-07-28T15:14:48+00:00'
---

# Original Description
QT Creator can import a cmakelist file. However, when i tried to load it, it first complained with libuv but then i compiled it under windows and added src/3rdparty/libuv folder, in which i added uv folder and uv.h, in the uv folder there are all header files and uv.dll, uv.exp, uv.ilk, uv.lib, uv.pdb, uv_a.lib

i added to the cmake file the following
add_subdirectory(src/3rdparty/libuv)

but it identifies VS as the compiler and i want to use gcc, and even it fails.



# Discussion History
## xmrig | 2019-07-28T09:46:28+00:00
You don't need extra steps like add files into source tree, if you able build project via plain cmake you can do it wit Qt Creator too.
Thank you.

## sherifomran | 2019-07-28T14:50:30+00:00
I can not build the project with cmake
i get undefined references and tried it with 64 and 32 bits compilers, i get the same.
UV_INCLUDE_DIR  was set to c:/libuv-1.x/include
UV_LIBRARY was set to c:/libuv-1.x/out/cmake
i don't know the reason. Any help is appreciated.
i get also cmake_code_blocks_executable_notfound ?

`CMakeFiles\xmrig-notls.dir/objects.a(NetworkState.cpp.obj):NetworkState.cpp:(.text+0xd7): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(NetworkState.cpp.obj):NetworkState.cpp:(.text+0xdf): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(NetworkState.cpp.obj):NetworkState.cpp:(.text+0x137): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(NetworkState.cpp.obj):NetworkState.cpp:(.text+0x13f): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(NetworkState.cpp.obj):NetworkState.cpp:(.text+0x1c6): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(NetworkState.cpp.obj):NetworkState.cpp:(.text+0x1ce): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x15): undefined reference to `uv_tty_reset_mode'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0xc4): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0xcc): undefined reference to `uv_stop'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x189): undefined reference to `uv_tty_reset_mode'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x1e5): undefined reference to `uv_tty_reset_mode'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x245): undefined reference to `uv_tty_reset_mode'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x2f9): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x301): undefined reference to `uv_stop'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x58b): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x59b): undefined reference to `uv_run'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x5a2): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x5aa): undefined reference to `uv_loop_close'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x5e8): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x5f0): undefined reference to `uv_stop'
CMakeFiles\xmrig-notls.dir/objects.a(Watcher.cpp.obj):Watcher.cpp:(.text+0x39): undefined reference to `uv_timer_stop'
CMakeFiles\xmrig-notls.dir/objects.a(Watcher.cpp.obj):Watcher.cpp:(.text+0x6c): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(Watcher.cpp.obj):Watcher.cpp:(.text+0xb2): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Watcher.cpp.obj):Watcher.cpp:(.text+0xbe): undefined reference to `uv_fs_event_init'
CMakeFiles\xmrig-notls.dir/objects.a(Watcher.cpp.obj):Watcher.cpp:(.text+0xd4): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Watcher.cpp.obj):Watcher.cpp:(.text+0xe0): undefined reference to `uv_timer_init'
CMakeFiles\xmrig-notls.dir/objects.a(Watcher.cpp.obj):Watcher.cpp:(.text+0x109): undefined reference to `uv_fs_event_start'
CMakeFiles\xmrig-notls.dir/objects.a(Watcher.cpp.obj):Watcher.cpp:(.text+0x15d): undefined reference to `uv_timer_stop'
CMakeFiles\xmrig-notls.dir/objects.a(Watcher.cpp.obj):Watcher.cpp:(.text+0x190): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(Watcher.cpp.obj):Watcher.cpp:(.text+0x1e1): undefined reference to `uv_fs_event_start'
CMakeFiles\xmrig-notls.dir/objects.a(Entry.cpp.obj):Entry.cpp:(.text+0xdd): undefined reference to `uv_version_string'
CMakeFiles\xmrig-notls.dir/objects.a(Process.cpp.obj):Process.cpp:(.text+0x11c): undefined reference to `uv_exepath'
CMakeFiles\xmrig-notls.dir/objects.a(Process.cpp.obj):Process.cpp:(.text+0x1b1): undefined reference to `uv_cwd'
CMakeFiles\xmrig-notls.dir/objects.a(Signals.cpp.obj):Signals.cpp:(.text+0x45): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Signals.cpp.obj):Signals.cpp:(.text+0x54): undefined reference to `uv_signal_init'
CMakeFiles\xmrig-notls.dir/objects.a(Signals.cpp.obj):Signals.cpp:(.text+0x6e): undefined reference to `uv_signal_start'
CMakeFiles\xmrig-notls.dir/objects.a(Arguments.cpp.obj):Arguments.cpp:(.text+0x83): undefined reference to `uv_setup_args'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0x20): undefined reference to `uv_fs_event_stop'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0x30): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0x50): undefined reference to `uv_cancel'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0x60): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0x83): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0xa0): undefined reference to `uv_signal_stop'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0xb0): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0xd7): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0xf0): undefined reference to `uv_timer_stop'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0x100): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(CommonConfig.cpp.obj):CommonConfig.cpp:(.text+0xdfe): undefined reference to `uv_version_string'
CMakeFiles\xmrig-notls.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0x82): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0x9e): undefined reference to `uv_tty_init'
CMakeFiles\xmrig-notls.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0xa6): undefined reference to `uv_is_readable'
CMakeFiles\xmrig-notls.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0xba): undefined reference to `uv_tty_set_mode'
CMakeFiles\xmrig-notls.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0xd2): undefined reference to `uv_read_start'
CMakeFiles\xmrig-notls.dir/objects.a(Console.cpp.obj):Console.cpp:(.text+0x6c): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x102): undefined reference to `uv_is_writable'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x148): undefined reference to `uv_guess_handle'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x172): undefined reference to `uv_try_write'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x20f): undefined reference to `uv_is_writable'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x258): undefined reference to `uv_guess_handle'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x282): undefined reference to `uv_try_write'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x2b8): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x2d4): undefined reference to `uv_tty_init'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x2e8): undefined reference to `uv_tty_set_mode'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x381): undefined reference to `uv_is_writable'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x39b): undefined reference to `uv_guess_handle'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x40e): undefined reference to `uv_is_writable'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x458): undefined reference to `uv_guess_handle'
CMakeFiles\xmrig-notls.dir/objects.a(ConsoleLog.cpp.obj):ConsoleLog.cpp:(.text+0x482): undefined reference to `uv_try_write'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x1a): undefined reference to `uv_fs_req_cleanup'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x14f): undefined reference to `uv_buf_init'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x176): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x1ae): undefined reference to `uv_fs_write'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x2fb): undefined reference to `uv_buf_init'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x322): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x35a): undefined reference to `uv_fs_write'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x392): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x3c1): undefined reference to `uv_fs_open'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x3cf): undefined reference to `uv_fs_req_cleanup'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x3f7): undefined reference to `uv_buf_init'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x41e): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(FileLog.cpp.obj):FileLog.cpp:(.text+0x456): undefined reference to `uv_fs_write'
CMakeFiles\xmrig-notls.dir/objects.a(Log.cpp.obj):Log.cpp:(.text+0x1a): undefined reference to `uv_mutex_lock'
CMakeFiles\xmrig-notls.dir/objects.a(Log.cpp.obj):Log.cpp:(.text+0x58): undefined reference to `uv_mutex_unlock'
CMakeFiles\xmrig-notls.dir/objects.a(Log.cpp.obj):Log.cpp:(.text+0x8a): undefined reference to `uv_mutex_lock'
CMakeFiles\xmrig-notls.dir/objects.a(Log.cpp.obj):Log.cpp:(.text+0xc1): undefined reference to `uv_mutex_unlock'
CMakeFiles\xmrig-notls.dir/objects.a(Log.cpp.obj):Log.cpp:(.text+0x17d): undefined reference to `uv_mutex_init'
CMakeFiles\xmrig-notls.dir/objects.a(Log.cpp.obj):Log.cpp:(.text+0x1f9): undefined reference to `uv_mutex_init'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x145): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x16f): undefined reference to `uv_getaddrinfo'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x1a8): undefined reference to `uv_strerror'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x27c): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x2a6): undefined reference to `uv_getaddrinfo'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x2e3): undefined reference to `uv_strerror'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x97b): undefined reference to `uv_is_closing'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x9b6): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xa1f): undefined reference to `uv_is_closing'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xa57): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xc63): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xc8d): undefined reference to `uv_getaddrinfo'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xccd): undefined reference to `uv_strerror'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xe3c): undefined reference to `uv_is_writable'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xe54): undefined reference to `uv_buf_init'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xe7a): undefined reference to `uv_try_write'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xe83): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xe90): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xf4d): undefined reference to `uv_is_writable'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xf6b): undefined reference to `uv_buf_init'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xf91): undefined reference to `uv_try_write'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xf9a): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0xfa2): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x105e): undefined reference to `uv_ip4_name'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x10c2): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x10ce): undefined reference to `uv_tcp_init'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x10e4): undefined reference to `uv_tcp_nodelay'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x1102): undefined reference to `uv_tcp_connect'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x117f): undefined reference to `uv_ip6_name'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x11fa): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x1206): undefined reference to `uv_tcp_init'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x121c): undefined reference to `uv_tcp_nodelay'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x123a): undefined reference to `uv_tcp_connect'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x1358): undefined reference to `uv_is_writable'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x1368): undefined reference to `uv_buf_init'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x138e): undefined reference to `uv_try_write'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x1397): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x139f): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x1429): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x1431): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x2ac4): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x2acc): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x2da3): undefined reference to `uv_is_closing'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x2ed2): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x306b): undefined reference to `uv_freeaddrinfo'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x30d5): undefined reference to `uv_strerror'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x3172): undefined reference to `uv_freeaddrinfo'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x333b): undefined reference to `uv_is_writable'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x334f): undefined reference to `uv_buf_init'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x3372): undefined reference to `uv_try_write'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x337f): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x3387): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x4ccf): undefined reference to `uv_read_start'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x4d1f): undefined reference to `uv_strerror'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x4d7d): undefined reference to `uv_is_closing'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x72f3): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x72fb): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x794f): undefined reference to `uv_strerror'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x79ac): undefined reference to `uv_is_closing'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x7b71): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x7b79): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x4d9f): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(Client.cpp.obj):Client.cpp:(.text+0x79d2): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(SubmitResult.cpp.obj):SubmitResult.cpp:(.text+0x45): undefined reference to `uv_hrtime'
CMakeFiles\xmrig-notls.dir/objects.a(SubmitResult.cpp.obj):SubmitResult.cpp:(.text+0x67): undefined reference to `uv_hrtime'
CMakeFiles\xmrig-notls.dir/objects.a(Controller.cpp.obj):Controller.cpp:(.text+0x2ed): undefined reference to `uv_mutex_init'
CMakeFiles\xmrig-notls.dir/objects.a(Network.cpp.obj):Network.cpp:(.text+0x50c): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Network.cpp.obj):Network.cpp:(.text+0x514): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(Network.cpp.obj):Network.cpp:(.text+0xc40): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Network.cpp.obj):Network.cpp:(.text+0xc4c): undefined reference to `uv_timer_init'
CMakeFiles\xmrig-notls.dir/objects.a(Network.cpp.obj):Network.cpp:(.text+0xc7c): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(Network.cpp.obj):Network.cpp:(.text+0xe88): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Network.cpp.obj):Network.cpp:(.text+0xe90): undefined reference to `uv_now'
CMakeFiles\xmrig-notls.dir/objects.a(DonateStrategy.cpp.obj):DonateStrategy.cpp:(.text+0x4d): undefined reference to `uv_timer_stop'
CMakeFiles\xmrig-notls.dir/objects.a(DonateStrategy.cpp.obj):DonateStrategy.cpp:(.text+0x2a4): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(DonateStrategy.cpp.obj):DonateStrategy.cpp:(.text+0x742): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(DonateStrategy.cpp.obj):DonateStrategy.cpp:(.text+0x7a6): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(DonateStrategy.cpp.obj):DonateStrategy.cpp:(.text+0x80a): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(DonateStrategy.cpp.obj):DonateStrategy.cpp:(.text+0x8a5): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(DonateStrategy.cpp.obj):DonateStrategy.cpp:(.text+0x90d): more undefined references to `uv_timer_start' follow
CMakeFiles\xmrig-notls.dir/objects.a(DonateStrategy.cpp.obj):DonateStrategy.cpp:(.text+0x109a): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(DonateStrategy.cpp.obj):DonateStrategy.cpp:(.text+0x10a6): undefined reference to `uv_timer_init'
CMakeFiles\xmrig-notls.dir/objects.a(DonateStrategy.cpp.obj):DonateStrategy.cpp:(.text+0x113c): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0x2a): undefined reference to `uv_thread_join'
CMakeFiles\xmrig-notls.dir/objects.a(Handle.cpp.obj):Handle.cpp:(.text+0x56): undefined reference to `uv_thread_create'
CMakeFiles\xmrig-notls.dir/objects.a(Hashrate.cpp.obj):Hashrate.cpp:(.text+0xe3): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Hashrate.cpp.obj):Hashrate.cpp:(.text+0xef): undefined reference to `uv_timer_init'
CMakeFiles\xmrig-notls.dir/objects.a(Hashrate.cpp.obj):Hashrate.cpp:(.text+0x120): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(Hashrate.cpp.obj):Hashrate.cpp:(.text+0xbea): undefined reference to `uv_timer_stop'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x216): undefined reference to `uv_mutex_lock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x28d): undefined reference to `uv_mutex_unlock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x307): undefined reference to `uv_rwlock_rdlock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x31c): undefined reference to `uv_rwlock_rdunlock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x33c): undefined reference to `uv_mutex_lock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x34e): undefined reference to `uv_mutex_unlock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x36c): undefined reference to `uv_mutex_lock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x37e): undefined reference to `uv_mutex_unlock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x6fa): undefined reference to `uv_rwlock_wrlock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x980): undefined reference to `uv_rwlock_wrunlock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xa0c): undefined reference to `uv_timer_stop'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xa2b): undefined reference to `uv_close'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xab1): undefined reference to `uv_mutex_lock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xaeb): undefined reference to `uv_mutex_unlock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xb23): undefined reference to `uv_mutex_lock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xb66): undefined reference to `uv_mutex_unlock'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xf93): undefined reference to `uv_mutex_init'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xf9f): undefined reference to `uv_rwlock_init'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xfd1): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xfe9): undefined reference to `uv_async_init'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xfee): undefined reference to `uv_default_loop'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xffe): undefined reference to `uv_timer_init'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0x1032): undefined reference to `uv_timer_start'
CMakeFiles\xmrig-notls.dir/objects.a(Workers.cpp.obj):Workers.cpp:(.text+0xafd): undefined reference to `uv_async_send'
CMakeFiles\xmrig-notls.dir/objects.a(Platform_win.cpp.obj):Platform_win.cpp:(.text+0xc9): undefined reference to `uv_version_string'
collect2.exe: error: ld returned 1 exit status
mingw32-make.exe[2]: *** [CMakeFiles\xmrig-notls.dir\build.make:1465: xmrig-notls.exe] Error 1
mingw32-make.exe[1]: *** [CMakeFiles\Makefile2:67: CMakeFiles/xmrig-notls.dir/all] Error 2
mingw32-make.exe: *** [Makefile:83: all] Error 2
16:46:56: The process "C:\Program Files (x86)\CMake\bin\cmake.exe" exited with code 2.
Error while building/deploying project xmrig (kit: Qt 5.13.0 MinGW 32-bit - Static)
When executing step "CMake Build"`


## sherifomran | 2019-07-28T15:14:17+00:00
i could compile it:
in UV_LIBRARY we should set C:\libuv-1.x\out\cmake\uv.lib

# Action History
- Created by: sherifomran | 2019-07-28T05:26:26+00:00
- Closed at: 2019-07-28T15:14:48+00:00
