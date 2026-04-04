---
title: 'Buildbot: fixes required for the Windows backend'
source_url: https://github.com/monero-project/meta/issues/238
author: anonimal
assignees: []
labels: []
created_at: '2018-06-06T07:33:37+00:00'
updated_at: '2020-03-09T21:41:19+00:00'
type: issue
status: closed
closed_at: '2020-03-09T21:41:19+00:00'
---

# Original Description
Though this isn't appearing in buildbot, when I build patches remotely on the buildbot machine, I'm met with:

```
[  3%] Building CXX object src/core/CMakeFiles/kovri-core_unity.dir/cotire/kovri
In file included from C:/msys64/home/anonimal/kovri/build/src/core/cotire/kovri-core_CXX_unity.cxx:31:0:
C:\msys64\home\anonimal\kovri\src\core\util\filesystem.cc: In member function 'void kovri::core::StringStream::WriteByteAndString(const string&)':
C:\msys64\home\anonimal\kovri\src\core\util\filesystem.cc:131:0: note: -Wmisleading-indentation is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
   std::uint8_t len = string.size();

C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/as.exe: CMakeFiles/kovri-core_unity.dir/cotire/kovri-core_CXX_unity.cxx.obj: section .debug_frame$_ZN8CryptoPP31IteratedHashWithStaticTransformIjNS_10EnumToTypeINS_9ByteOrderELi1EEELj64ELj20ENS_4SHA1ELj0ELb0EED2Ev: string table overflow at offset 10000031
C:\msys64\tmp\cc8q50BT.s: Assembler messages:
C:\msys64\tmp\cc8q50BT.s: Fatal error: can't close CMakeFiles/kovri-core_unity.dir/cotire/kovri-core_CXX_unity.cxx.obj: File too big
make[4]: *** [src/core/CMakeFiles/kovri-core_unity.dir/build.make:1051: src/core/CMakeFiles/kovri-core_unity.dir/cotire/kovri-core_CXX_unity.cxx.obj] Error 1
make[4]: Leaving directory '/home/anonimal/kovri/build'
make[3]: *** [CMakeFiles/Makefile2:324: src/core/CMakeFiles/kovri-core_unity.dir/all] Error 2
make[3]: Leaving directory '/home/anonimal/kovri/build'
make[2]: *** [CMakeFiles/Makefile2:366: src/core/CMakeFiles/all_unity.dir/rule] Error 2
make[2]: Leaving directory '/home/anonimal/kovri/build'
make[1]: *** [Makefile:229: all_unity] Error 2
make[1]: Leaving directory '/home/anonimal/kovri/build'
make: *** [Makefile:162: release] Error 2
```

and as such, can't do Windows development. cotire/pre-compiled headers are a memory hog. Is buildbot somehow acquiring more memory than another user would?

# Discussion History
## coneiric | 2018-06-06T19:03:24+00:00
I was getting these errors as well when trying to do multiprocessor Windows builds with cotire.

You've probably come across this section of the [manual](https://github.com/sakra/cotire/blob/master/MANUAL.md#configuring-the-generation-of-the-unity-source). Maybe decreasing the maximum number of unity includes would help?

## anonimal | 2018-06-06T21:15:07+00:00
~~Thanks @coneiric! That solved the cotire issue. I had to set `COTIRE_MAXIMUM_NUMBER_OF_UNITY_INCLUDES=-j1` in addition to bumping down to the usual `-j1`. Maybe cotire does this automatically within buildbot's environment (buildbot only exposing 1 core availability?).~~ Nevermind... the issue is repro'd once the client lib starts building.

I'd like to keep this issue open though because the windows VMs need more power.

## coneiric | 2018-06-11T20:05:42+00:00
> Nevermind... the issue is repro'd once the client lib starts building.

Agh! So close...

> I'd like to keep this issue open though because the windows VMs need more power.

Strap a bigger engine on those VMs, let's hit lightspeed!

## anonimal | 2018-06-24T21:42:13+00:00
The issue now affects buildbot. @danrmiller We appear to need more memory and disk space:

- https://build.getmonero.org/builders/kovri-all-win32/builds/1041/steps/compile/logs/stdio
- https://build.getmonero.org/builders/kovri-static-win32/builds/529/steps/compile/logs/stdio
- https://build.getmonero.org/builders/kovri-static-win64/builds/538/steps/compile/logs/stdio

## anonimal | 2018-06-29T21:12:03+00:00
Thanks to iDunk, this appears to solve the win32 build https://github.com/monero-project/monero/issues/3521#issuecomment-377466568.

## anonimal | 2018-06-30T03:58:53+00:00
iDunk has also supplied us with a side-step for win64. The issue appears entirely windows related. The patch is intrusive but it's the best we've got right now, so thanks to iDunk for patching. 

## danrmiller | 2018-07-14T17:11:25+00:00
@anonimal What do you need done here?

## anonimal | 2018-07-15T22:06:22+00:00
@danrmiller a working win32 build https://build.getmonero.org/builders/kovri-all-win32/builds/1141 https://build.getmonero.org/builders/kovri-static-win32/builds/550

## danrmiller | 2018-07-28T18:34:26+00:00
Here is the latest attempts. Any ideas?

https://build.getmonero.org/builders/kovri-static-win32/builds/564/steps/compile/logs/stdio

# Action History
- Created by: anonimal | 2018-06-06T07:33:37+00:00
- Closed at: 2020-03-09T21:41:19+00:00
