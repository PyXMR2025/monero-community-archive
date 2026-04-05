---
title: Windows 10 VS2017 Compiling
source_url: https://github.com/xmrig/xmrig/issues/79
author: f0rb1dd3n
assignees: []
labels: []
created_at: '2017-08-30T13:48:11+00:00'
updated_at: '2019-08-22T17:21:09+00:00'
type: issue
status: closed
closed_at: '2017-08-30T14:48:53+00:00'
---

# Original Description
Hello, sorry I am getting stuck on that easy stuff, but I would like some help with it. Can someone help me to figure out it?

I installed vs2017 community on windows 10 machine, installed cmake, compiled libuv and installed Toolset v140_xp. 

So I am getting this error:

$ cmake .. -G "Visual Studio 15 2017 Win64" -T v140_xp -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR=C:\Users\F0rb1dd3n\Desktop\libuv\include -DUV_LIBRARY=C:\Users\F0rb1dd3n\Desktop\libuv\Debug\lib\libuv.lib
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_C_COMPILER could be found.



CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.



-- Configuring incomplete, errors occurred!
See also "C:/Users/F0rb1dd3n/Desktop/xmrig/build/CMakeFiles/CMakeOutput.log".
See also "C:/Users/F0rb1dd3n/Desktop/xmrig/build/CMakeFiles/CMakeError.log".

-----------------------------------------------------------------------------------------------------------------
$ cat C:/Users/F0rb1dd3n/Desktop/xmrig/build/CMakeFiles/CMakeOutput.log
The system is: Windows - 10.0.15063 - AMD64

-----------------------------------------------------------------------------------------------------------------

$ cat C:/Users/F0rb1dd3n/Desktop/xmrig/build/CMakeFiles/CMakeError.log
Compiling the C compiler identification source file "CMakeCCompilerId.c" failed.
Compiler:
Build flags:
Id flags:

The output was:
1
Microsoft(R) Build Engine vers▒o 15.3.409.57025 para .NET Framework
Copyright (C) Microsoft Corporation. Todos os direitos reservados.

Compila▒▒o de 30/08/2017 10:46:42 iniciada.
Projeto "C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj" no n▒ 1 (destinos padr▒o).
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Platforms\x64\PlatformToolsets\v140_xp\Toolset.targets(36,5): warning MSB8003: Could not find WindowsSdkDir_71A variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]
PrepareForBuild:
  Criando o diret▒rio "Debug\".
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppBuild.targets(366,5): warning MSB8003: Could not find WindowsSDKDir variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]
  Criando o diret▒rio "Debug\CompilerIdC.tlog\".
InitializeBuildStatus:
  Criando "Debug\CompilerIdC.tlog\unsuccessfulbuild" porque "AlwaysCreate" foi especificado.
ClCompile:
  C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\CL.exe /c /nologo /W0 /WX- /Od /D _USING_V110_SDK71_ /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc140.pdb" /Gd /TC /errorReport:queue CMakeCCompilerId.c
  CMakeCCompilerId.c
Link:
  C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdC.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdC.pdb" /SUBSYSTEM:CONSOLE,"5.02" /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdC.lib" /MACHINE:X64 Debug\CMakeCCompilerId.obj
LINK : fatal error LNK1181: n▒o foi poss▒vel abrir o arquivo de entrada 'kernel32.lib' [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]
Projeto de compila▒▒o pronto "C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj" (destinos padr▒o) -- FALHA.

FALHA da compila▒▒o.

"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj" (destino padr▒o) (1) ->
(CheckWindowsSDK71A destino) ->
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Platforms\x64\PlatformToolsets\v140_xp\Toolset.targets(36,5): warning MSB8003: Could not find WindowsSdkDir_71A variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]


"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj" (destino padr▒o) (1) ->
(PrepareForBuild destino) ->
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppBuild.targets(366,5): warning MSB8003: Could not find WindowsSDKDir variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]


"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj" (destino padr▒o) (1) ->
(Link destino) ->
  LINK : fatal error LNK1181: n▒o foi poss▒vel abrir o arquivo de entrada 'kernel32.lib' [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]

    2 Aviso(s)
    1 Erro(s)

Tempo Decorrido 00:00:02.57


Compiling the C compiler identification source file "CMakeCCompilerId.c" failed.
Compiler:
Build flags:
Id flags:

The output was:
1
Microsoft(R) Build Engine vers▒o 15.3.409.57025 para .NET Framework
Copyright (C) Microsoft Corporation. Todos os direitos reservados.

Compila▒▒o de 30/08/2017 10:46:46 iniciada.
Projeto "C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj" no n▒ 1 (destinos padr▒o).
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Platforms\x64\PlatformToolsets\v140_xp\Toolset.targets(36,5): warning MSB8003: Could not find WindowsSdkDir_71A variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]
PrepareForBuild:
  Criando o diret▒rio "Debug\".
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppBuild.targets(366,5): warning MSB8003: Could not find WindowsSDKDir variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]
  Criando o diret▒rio "Debug\CompilerIdC.tlog\".
InitializeBuildStatus:
  Criando "Debug\CompilerIdC.tlog\unsuccessfulbuild" porque "AlwaysCreate" foi especificado.
ClCompile:
  C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\CL.exe /c /nologo /W0 /WX- /Od /D _USING_V110_SDK71_ /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc140.pdb" /Gd /TC /errorReport:queue CMakeCCompilerId.c
  CMakeCCompilerId.c
Link:
  C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdC.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdC.pdb" /SUBSYSTEM:CONSOLE,"5.02" /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdC.lib" /MACHINE:X64 Debug\CMakeCCompilerId.obj
LINK : fatal error LNK1181: n▒o foi poss▒vel abrir o arquivo de entrada 'kernel32.lib' [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]
Projeto de compila▒▒o pronto "C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj" (destinos padr▒o) -- FALHA.

FALHA da compila▒▒o.

"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj" (destino padr▒o) (1) ->
(CheckWindowsSDK71A destino) ->
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Platforms\x64\PlatformToolsets\v140_xp\Toolset.targets(36,5): warning MSB8003: Could not find WindowsSdkDir_71A variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]


"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj" (destino padr▒o) (1) ->
(PrepareForBuild destino) ->
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppBuild.targets(366,5): warning MSB8003: Could not find WindowsSDKDir variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]


"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj" (destino padr▒o) (1) ->
(Link destino) ->
  LINK : fatal error LNK1181: n▒o foi poss▒vel abrir o arquivo de entrada 'kernel32.lib' [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdC\CompilerIdC.vcxproj]

    2 Aviso(s)
    1 Erro(s)

Tempo Decorrido 00:00:01.84


Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" failed.
Compiler:
Build flags:
Id flags:

The output was:
1
Microsoft(R) Build Engine vers▒o 15.3.409.57025 para .NET Framework
Copyright (C) Microsoft Corporation. Todos os direitos reservados.

Compila▒▒o de 30/08/2017 10:46:48 iniciada.
Projeto "C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj" no n▒ 1 (destinos padr▒o).
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Platforms\x64\PlatformToolsets\v140_xp\Toolset.targets(36,5): warning MSB8003: Could not find WindowsSdkDir_71A variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]
PrepareForBuild:
  Criando o diret▒rio "Debug\".
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppBuild.targets(366,5): warning MSB8003: Could not find WindowsSDKDir variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]
  Criando o diret▒rio "Debug\CompilerIdCXX.tlog\".
InitializeBuildStatus:
  Criando "Debug\CompilerIdCXX.tlog\unsuccessfulbuild" porque "AlwaysCreate" foi especificado.
ClCompile:
  C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\CL.exe /c /nologo /W0 /WX- /Od /D _USING_V110_SDK71_ /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc140.pdb" /Gd /TP /errorReport:queue CMakeCXXCompilerId.cpp
  CMakeCXXCompilerId.cpp
Link:
  C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdCXX.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdCXX.pdb" /SUBSYSTEM:CONSOLE,"5.02" /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdCXX.lib" /MACHINE:X64 Debug\CMakeCXXCompilerId.obj
LINK : fatal error LNK1181: n▒o foi poss▒vel abrir o arquivo de entrada 'kernel32.lib' [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]
Projeto de compila▒▒o pronto "C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj" (destinos padr▒o) -- FALHA.

FALHA da compila▒▒o.

"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj" (destino padr▒o) (1) ->
(CheckWindowsSDK71A destino) ->
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Platforms\x64\PlatformToolsets\v140_xp\Toolset.targets(36,5): warning MSB8003: Could not find WindowsSdkDir_71A variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]


"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj" (destino padr▒o) (1) ->
(PrepareForBuild destino) ->
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppBuild.targets(366,5): warning MSB8003: Could not find WindowsSDKDir variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]


"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj" (destino padr▒o) (1) ->
(Link destino) ->
  LINK : fatal error LNK1181: n▒o foi poss▒vel abrir o arquivo de entrada 'kernel32.lib' [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]

    2 Aviso(s)
    1 Erro(s)

Tempo Decorrido 00:00:02.04


Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" failed.
Compiler:
Build flags:
Id flags:

The output was:
1
Microsoft(R) Build Engine vers▒o 15.3.409.57025 para .NET Framework
Copyright (C) Microsoft Corporation. Todos os direitos reservados.

Compila▒▒o de 30/08/2017 10:46:51 iniciada.
Projeto "C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj" no n▒ 1 (destinos padr▒o).
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Platforms\x64\PlatformToolsets\v140_xp\Toolset.targets(36,5): warning MSB8003: Could not find WindowsSdkDir_71A variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]
PrepareForBuild:
  Criando o diret▒rio "Debug\".
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppBuild.targets(366,5): warning MSB8003: Could not find WindowsSDKDir variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]
  Criando o diret▒rio "Debug\CompilerIdCXX.tlog\".
InitializeBuildStatus:
  Criando "Debug\CompilerIdCXX.tlog\unsuccessfulbuild" porque "AlwaysCreate" foi especificado.
ClCompile:
  C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\CL.exe /c /nologo /W0 /WX- /Od /D _USING_V110_SDK71_ /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc140.pdb" /Gd /TP /errorReport:queue CMakeCXXCompilerId.cpp
  CMakeCXXCompilerId.cpp
Link:
  C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdCXX.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdCXX.pdb" /SUBSYSTEM:CONSOLE,"5.02" /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdCXX.lib" /MACHINE:X64 Debug\CMakeCXXCompilerId.obj
LINK : fatal error LNK1181: n▒o foi poss▒vel abrir o arquivo de entrada 'kernel32.lib' [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]
Projeto de compila▒▒o pronto "C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj" (destinos padr▒o) -- FALHA.

FALHA da compila▒▒o.

"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj" (destino padr▒o) (1) ->
(CheckWindowsSDK71A destino) ->
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Platforms\x64\PlatformToolsets\v140_xp\Toolset.targets(36,5): warning MSB8003: Could not find WindowsSdkDir_71A variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]


"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj" (destino padr▒o) (1) ->
(PrepareForBuild destino) ->
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppBuild.targets(366,5): warning MSB8003: Could not find WindowsSDKDir variable from the registry.  TargetFrameworkVersion or PlatformToolset may be set to an invalid version number. [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]


"C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj" (destino padr▒o) (1) ->
(Link destino) ->
  LINK : fatal error LNK1181: n▒o foi poss▒vel abrir o arquivo de entrada 'kernel32.lib' [C:\Users\F0rb1dd3n\Desktop\xmrig\build\CMakeFiles\3.9.1\CompilerIdCXX\CompilerIdCXX.vcxproj]

    2 Aviso(s)
    1 Erro(s)

Tempo Decorrido 00:00:01.98



# Discussion History
## f0rb1dd3n | 2017-08-30T14:49:21+00:00
I have found where I missing

## Wolowin | 2019-08-22T17:21:09+00:00
Hey, f0rb1dd3n!

Would you mind sharing what was the solution?

# Action History
- Created by: f0rb1dd3n | 2017-08-30T13:48:11+00:00
- Closed at: 2017-08-30T14:48:53+00:00
