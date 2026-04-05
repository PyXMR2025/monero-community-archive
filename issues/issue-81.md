---
title: Building with VS2017
source_url: https://github.com/xmrig/xmrig/issues/81
author: vladvlad777
assignees: []
labels:
- question
created_at: '2017-09-01T08:07:44+00:00'
updated_at: '2017-09-08T13:45:31+00:00'
type: issue
status: closed
closed_at: '2017-09-08T13:45:31+00:00'
---

# Original Description
Hello! Trying to build project with VS2017, have following errors. Please help

Severity	Code	Description	Project	File	Line	Suppression State
Error	LNK2001	unresolved external symbol uv_default_loop	xmrig	C:\XMRigDev\xmrig-master\build\Hashrate.obj	1	
Error	LNK2001	unresolved external symbol uv_default_loop	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2001	unresolved external symbol uv_default_loop	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2001	unresolved external symbol uv_default_loop	xmrig	C:\XMRigDev\xmrig-master\build\Network.obj	1	
Error	LNK2001	unresolved external symbol uv_default_loop	xmrig	C:\XMRigDev\xmrig-master\build\DonateStrategy.obj	1	
Error	LNK2001	unresolved external symbol uv_default_loop	xmrig	C:\XMRigDev\xmrig-master\build\Options.obj	1	
Error	LNK2001	unresolved external symbol uv_default_loop	xmrig	C:\XMRigDev\xmrig-master\build\App.obj	1	
Error	LNK2001	unresolved external symbol uv_default_loop	xmrig	C:\XMRigDev\xmrig-master\build\Console.obj	1	
Error	LNK2001	unresolved external symbol uv_default_loop	xmrig	C:\XMRigDev\xmrig-master\build\ConsoleLog.obj	1	
Error	LNK2001	unresolved external symbol uv_default_loop	xmrig	C:\XMRigDev\xmrig-master\build\FileLog.obj	1	
Error	LNK2019	unresolved external symbol uv_loop_close referenced in function "public: int __cdecl App::exec(void)" (?exec@App@@QEAAHXZ)	xmrig	C:\XMRigDev\xmrig-master\build\App.obj	1	
Error	LNK2019	unresolved external symbol uv_run referenced in function "public: int __cdecl App::exec(void)" (?exec@App@@QEAAHXZ)	xmrig	C:\XMRigDev\xmrig-master\build\App.obj	1	
Error	LNK2019	unresolved external symbol uv_stop referenced in function "private: void __cdecl App::close(void)" (?close@App@@AEAAXXZ)	xmrig	C:\XMRigDev\xmrig-master\build\App.obj	1	
Error	LNK2019	unresolved external symbol uv_tty_reset_mode referenced in function "public: int __cdecl App::exec(void)" (?exec@App@@QEAAHXZ)	xmrig	C:\XMRigDev\xmrig-master\build\App.obj	1	
Error	LNK2019	unresolved external symbol uv_signal_init referenced in function "public: __cdecl App::App(int,char * *)" (??0App@@QEAA@HPEAPEAD@Z)	xmrig	C:\XMRigDev\xmrig-master\build\App.obj	1	
Error	LNK2019	unresolved external symbol uv_signal_start referenced in function "public: int __cdecl App::exec(void)" (?exec@App@@QEAAHXZ)	xmrig	C:\XMRigDev\xmrig-master\build\App.obj	1	
Error	LNK2019	unresolved external symbol uv_signal_stop referenced in function "private: static void __cdecl App::onSignal(struct uv_signal_s *,int)" (?onSignal@App@@CAXPEAUuv_signal_s@@H@Z)	xmrig	C:\XMRigDev\xmrig-master\build\App.obj	1	
Error	LNK2019	unresolved external symbol uv_close referenced in function "private: static void __cdecl Console::onRead(struct uv_stream_s *,__int64,struct uv_buf_t const *)" (?onRead@Console@@CAXPEAUuv_stream_s@@_JPEBUuv_buf_t@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Console.obj	1	
Error	LNK2001	unresolved external symbol uv_close	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2001	unresolved external symbol uv_close	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_read_start referenced in function "public: __cdecl Console::Console(class IConsoleListener *)" (??0Console@@QEAA@PEAVIConsoleListener@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Console.obj	1	
Error	LNK2001	unresolved external symbol uv_read_start	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_is_readable referenced in function "public: __cdecl Console::Console(class IConsoleListener *)" (??0Console@@QEAA@PEAVIConsoleListener@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Console.obj	1	
Error	LNK2019	unresolved external symbol uv_tty_init referenced in function "public: __cdecl Console::Console(class IConsoleListener *)" (??0Console@@QEAA@PEAVIConsoleListener@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Console.obj	1	
Error	LNK2001	unresolved external symbol uv_tty_init	xmrig	C:\XMRigDev\xmrig-master\build\ConsoleLog.obj	1	
Error	LNK2019	unresolved external symbol uv_tty_set_mode referenced in function "public: __cdecl Console::Console(class IConsoleListener *)" (??0Console@@QEAA@PEAVIConsoleListener@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Console.obj	1	
Error	LNK2001	unresolved external symbol uv_tty_set_mode	xmrig	C:\XMRigDev\xmrig-master\build\ConsoleLog.obj	1	
Error	LNK2019	unresolved external symbol uv_write referenced in function "private: void __cdecl ConsoleLog::print(char *,char *)" (?print@ConsoleLog@@AEAAXPEAD0@Z)	xmrig	C:\XMRigDev\xmrig-master\build\ConsoleLog.obj	1	
Error	LNK2001	unresolved external symbol uv_write	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_is_writable referenced in function "private: bool __cdecl ConsoleLog::isWritable(void)const " (?isWritable@ConsoleLog@@AEBA_NXZ)	xmrig	C:\XMRigDev\xmrig-master\build\ConsoleLog.obj	1	
Error	LNK2001	unresolved external symbol uv_is_writable	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_guess_handle referenced in function "private: bool __cdecl ConsoleLog::isWritable(void)const " (?isWritable@ConsoleLog@@AEBA_NXZ)	xmrig	C:\XMRigDev\xmrig-master\build\ConsoleLog.obj	1	
Error	LNK2019	unresolved external symbol uv_buf_init referenced in function "private: void __cdecl FileLog::write(char *,unsigned __int64)" (?write@FileLog@@AEAAXPEAD_K@Z)	xmrig	C:\XMRigDev\xmrig-master\build\FileLog.obj	1	
Error	LNK2001	unresolved external symbol uv_buf_init	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_fs_req_cleanup referenced in function "public: __cdecl FileLog::FileLog(char const *)" (??0FileLog@@QEAA@PEBD@Z)	xmrig	C:\XMRigDev\xmrig-master\build\FileLog.obj	1	
Error	LNK2001	unresolved external symbol uv_fs_req_cleanup	xmrig	C:\XMRigDev\xmrig-master\build\Options.obj	1	
Error	LNK2019	unresolved external symbol uv_fs_open referenced in function "public: __cdecl FileLog::FileLog(char const *)" (??0FileLog@@QEAA@PEBD@Z)	xmrig	C:\XMRigDev\xmrig-master\build\FileLog.obj	1	
Error	LNK2001	unresolved external symbol uv_fs_open	xmrig	C:\XMRigDev\xmrig-master\build\Options.obj	1	
Error	LNK2019	unresolved external symbol uv_fs_write referenced in function "private: void __cdecl FileLog::write(char *,unsigned __int64)" (?write@FileLog@@AEAAXPEAD_K@Z)	xmrig	C:\XMRigDev\xmrig-master\build\FileLog.obj	1	
Error	LNK2019	unresolved external symbol uv_now referenced in function "public: __int64 __cdecl Client::send(char *,unsigned __int64)" (?send@Client@@QEAA_JPEAD_K@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2001	unresolved external symbol uv_now	xmrig	C:\XMRigDev\xmrig-master\build\Network.obj	1	
Error	LNK2019	unresolved external symbol uv_strerror referenced in function "private: int __cdecl Client::resolve(char const *)" (?resolve@Client@@AEAAHPEBD@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2001	unresolved external symbol uv_strerror	xmrig	C:\XMRigDev\xmrig-master\build\Options.obj	1	
Error	LNK2019	unresolved external symbol uv_is_closing referenced in function "private: void __cdecl Client::close(void)" (?close@Client@@AEAAXXZ)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_tcp_init referenced in function "private: void __cdecl Client::connect(struct sockaddr *)" (?connect@Client@@AEAAXPEAUsockaddr@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_tcp_nodelay referenced in function "private: void __cdecl Client::connect(struct sockaddr *)" (?connect@Client@@AEAAXPEAUsockaddr@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_tcp_connect referenced in function "private: void __cdecl Client::connect(struct sockaddr *)" (?connect@Client@@AEAAXPEAUsockaddr@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_init	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_init	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_init	xmrig	C:\XMRigDev\xmrig-master\build\Network.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_init	xmrig	C:\XMRigDev\xmrig-master\build\DonateStrategy.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_init	xmrig	C:\XMRigDev\xmrig-master\build\Hashrate.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_start	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_start	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_start	xmrig	C:\XMRigDev\xmrig-master\build\Network.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_start	xmrig	C:\XMRigDev\xmrig-master\build\DonateStrategy.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_start	xmrig	C:\XMRigDev\xmrig-master\build\Hashrate.obj	1	
Error	LNK2019	unresolved external symbol uv_timer_stop referenced in function "public: void __cdecl Client::disconnect(void)" (?disconnect@Client@@QEAAXXZ)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_stop	xmrig	C:\XMRigDev\xmrig-master\build\DonateStrategy.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_stop	xmrig	C:\XMRigDev\xmrig-master\build\Hashrate.obj	1	
Error	LNK2001	unresolved external symbol uv_timer_stop	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_getaddrinfo referenced in function "private: int __cdecl Client::resolve(char const *)" (?resolve@Client@@AEAAHPEBD@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_freeaddrinfo referenced in function "private: static void __cdecl Client::onResolved(struct uv_getaddrinfo_s *,int,struct addrinfo *)" (?onResolved@Client@@CAXPEAUuv_getaddrinfo_s@@HPEAUaddrinfo@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_ip4_name referenced in function "private: static void __cdecl Client::onResolved(struct uv_getaddrinfo_s *,int,struct addrinfo *)" (?onResolved@Client@@CAXPEAUuv_getaddrinfo_s@@HPEAUaddrinfo@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_hrtime referenced in function "public: __cdecl SubmitResult::SubmitResult(__int64,unsigned int)" (??0SubmitResult@@QEAA@_JI@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Client.obj	1	
Error	LNK2019	unresolved external symbol uv_version_string referenced in function "private: void __cdecl Options::showVersion(void)" (?showVersion@Options@@AEAAXXZ)	xmrig	C:\XMRigDev\xmrig-master\build\Options.obj	1	
Error	LNK2001	unresolved external symbol uv_version_string	xmrig	C:\XMRigDev\xmrig-master\build\Summary.obj	1	
Error	LNK2001	unresolved external symbol uv_version_string	xmrig	C:\XMRigDev\xmrig-master\build\Platform_win.obj	1	
Error	LNK2019	unresolved external symbol uv_fs_close referenced in function "private: void __cdecl Options::parseConfig(char const *)" (?parseConfig@Options@@AEAAXPEBD@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Options.obj	1	
Error	LNK2019	unresolved external symbol uv_exepath referenced in function "public: static char const * __cdecl Platform::defaultConfigName(void)" (?defaultConfigName@Platform@@SAPEBDXZ)	xmrig	C:\XMRigDev\xmrig-master\build\Platform.obj	1	
Error	LNK2019	unresolved external symbol uv_thread_create referenced in function "public: void __cdecl Handle::start(void (__cdecl*)(void *))" (?start@Handle@@QEAAXP6AXPEAX@Z@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Handle.obj	1	
Error	LNK2019	unresolved external symbol uv_thread_join referenced in function "public: void __cdecl Handle::join(void)" (?join@Handle@@QEAAXXZ)	xmrig	C:\XMRigDev\xmrig-master\build\Handle.obj	1	
Error	LNK2019	unresolved external symbol uv_async_init referenced in function "public: static void __cdecl Workers::start(__int64,int)" (?start@Workers@@SAX_JH@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_async_send referenced in function "public: static void __cdecl Workers::submit(class JobResult const &)" (?submit@Workers@@SAXAEBVJobResult@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_mutex_init referenced in function "public: static void __cdecl Workers::start(__int64,int)" (?start@Workers@@SAX_JH@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_mutex_lock referenced in function "public: static void __cdecl Workers::submit(class JobResult const &)" (?submit@Workers@@SAXAEBVJobResult@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_mutex_unlock referenced in function "public: static void __cdecl Workers::submit(class JobResult const &)" (?submit@Workers@@SAXAEBVJobResult@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_rwlock_init referenced in function "public: static void __cdecl Workers::start(__int64,int)" (?start@Workers@@SAX_JH@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_rwlock_rdlock referenced in function "public: static class Job __cdecl Workers::job(void)" (?job@Workers@@SA?AVJob@@XZ)	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_rwlock_rdunlock referenced in function "public: static class Job __cdecl Workers::job(void)" (?job@Workers@@SA?AVJob@@XZ)	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_rwlock_wrlock referenced in function "public: static void __cdecl Workers::setJob(class Job const &)" (?setJob@Workers@@SAXAEBVJob@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Error	LNK2019	unresolved external symbol uv_rwlock_wrunlock referenced in function "public: static void __cdecl Workers::setJob(class Job const &)" (?setJob@Workers@@SAXAEBVJob@@@Z)	xmrig	C:\XMRigDev\xmrig-master\build\Workers.obj	1	
Warning	LNK4272	library machine type 'X86' conflicts with target machine type 'x64'	xmrig	C:\XMRigDev\libuv-1.x\Debug\lib\libuv.lib	1	
Error	LNK1120	48 unresolved externals	xmrig	C:\XMRigDev\xmrig-master\build\Debug\xmrig.exe	1	


# Discussion History
## vladvlad777 | 2017-09-01T11:04:54+00:00
Update: looks like some problem with libuv. Downloaded precompiled version. Another errors now:

Severity	Code	Description	Project	File	Line	Suppression State
Error	C2065	'O_APPEND': undeclared identifier	xmrig	C:\XMRigDev\xmrig-master\src\log\FileLog.cpp	37	
Error (active)	E0020	identifier "O_CREAT" is undefined	xmrig	c:\XMRigDev\xmrig-master\src\log\FileLog.cpp	37	
Error (active)	E0020	identifier "O_APPEND" is undefined	xmrig	c:\XMRigDev\xmrig-master\src\log\FileLog.cpp	37	
Error (active)	E0020	identifier "O_WRONLY" is undefined	xmrig	c:\XMRigDev\xmrig-master\src\log\FileLog.cpp	37	
Warning	C4267	'=': conversion from 'size_t' to 'ULONG', possible loss of data	xmrig	C:\XMRigDev\xmrig-master\src\log\ConsoleLog.cpp	152	
Error	C2065	'O_CREAT': undeclared identifier	xmrig	C:\XMRigDev\xmrig-master\src\log\FileLog.cpp	37	
Error	C2065	'O_WRONLY': undeclared identifier	xmrig	C:\XMRigDev\xmrig-master\src\log\FileLog.cpp	37	
Error	C2660	'uv_fs_open': function does not take 5 arguments	xmrig	C:\XMRigDev\xmrig-master\src\log\FileLog.cpp	37	
Warning	C4267	'=': conversion from 'size_t' to 'ULONG', possible loss of data	xmrig	C:\XMRigDev\xmrig-master\src\net\Client.cpp	526	
Error	C2065	'O_RDONLY': undeclared identifier	xmrig	C:\XMRigDev\xmrig-master\src\Options.cpp	503	
Error	C2789	'fd': an object of const-qualified type must be initialized	xmrig	C:\XMRigDev\xmrig-master\src\Options.cpp	503	


## xmrig | 2017-09-01T11:11:47+00:00
There precompiled libuv used in releases https://github.com/xmrig/xmrig-deps/releases
About `O_APPEND` errors, probably you select wrong libuv version, you need libuv.lib not libuv.a
Thank you.

## vladvlad777 | 2017-09-01T11:45:47+00:00
thx! works fine

# Action History
- Created by: vladvlad777 | 2017-09-01T08:07:44+00:00
- Closed at: 2017-09-08T13:45:31+00:00
