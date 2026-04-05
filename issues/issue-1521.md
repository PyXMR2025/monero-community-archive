---
title: Failed to build
source_url: https://github.com/xmrig/xmrig/issues/1521
author: Evaexe117
assignees: []
labels:
- question
created_at: '2020-01-29T05:18:59+00:00'
updated_at: '2020-02-01T09:56:28+00:00'
type: issue
status: closed
closed_at: '2020-02-01T09:56:28+00:00'
---

# Original Description
Hello !
I'm actually trying to build Xmrig on windows.
But i get error.
I'm on windows 10, Visual studio installed.

My input commande : 
cmake .. -G "Visual Studio 16 2019" -A Win64 -DXMRIG_DEPS=c:\xmrig-deps\msvc2019\x64

My output console : 
-------------------------------------------------------------------------------------------------------
CMake Error at CMakeLists.txt:2 (project):
  Failed to run MSBuild command:

 C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe

  to get the value of VCTargetsPath:

    Microsoft (R) Build Engine version 16.4.0+e901037fe pour .NET Framework
    Copyright (C) Microsoft Corporation. Tous droits réservés.

    La génération a démarré 29/01/2020 06:21:52.
    Projet "C:\xmrig-master\build\CMakeFiles\3.16.3\VCTargetsPath.vcxproj" sur le noud 1 (cibles par défaut).
    C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Current\Bin\Microsoft.Common.CurrentVersion.targets(775,5): error : The OutputPath property is not set for project 'VCTargetsPath.vcxproj'.  Please check to make sure that you have specified a valid combination of Configuration and Platform for this project.  Configuration='Debug'  Platform='Win64'.  You may be seeing this message because you are trying to build a project without a solution file, and have specified a non-default Configuration or Platform that doesn't exist for this project. [C:\xmrig-master\build\CMakeFiles\3.16.3\VCTargetsPath.vcxproj]
    Génération du projet "C:\xmrig-master\build\CMakeFiles\3.16.3\VCTargetsPath.vcxproj" terminée (cibles par défaut) -- ÉCHEC.

    ÉCHEC de la build.

    "C:\xmrig-master\build\CMakeFiles\3.16.3\VCTargetsPath.vcxproj" (cible par défaut) (1) ->
    (_CheckForInvalidConfigurationAndPlatform cible) ->
      C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Current\Bin\Microsoft.Common.CurrentVersion.targets(775,5): error : The OutputPath property is not set for project 'VCTargetsPath.vcxproj'.  Please check to make sure that you have specified a valid combination of Configuration and Platform for this project.  Configuration='Debug'  Platform='Win64'.  You may be seeing this message because you are trying to build a project without a solution file, and have specified a non-default Configuration or Platform that doesn't exist for this project. [C:\xmrig-master\build\CMakeFiles\3.16.3\VCTargetsPath.vcxproj]

        0 Avertissement(s)
        1 Erreur(s)

    Temps écoulé 00:00:00.10


  Exit code: 1




--------------------------------------------------------------------------------------------------------

The output of CMakeOutput.log :
`The system is: Windows - 10.0.17763 - AMD64`

So my quesiton is ofc, how can i correct this error and build Xmrig ?
Thanks ! 

# Discussion History
## ValoWaking | 2020-01-30T18:41:21+00:00
i think flag A is wrong, try this:
`-G "Visual Studio 16 2019" -A x64`

## xmrig | 2020-02-01T09:13:48+00:00
Definitely `-A` option should looks like above comment.
Thank you.

## Evaexe117 | 2020-02-01T09:56:28+00:00
That work ! thanks !! 

# Action History
- Created by: Evaexe117 | 2020-01-29T05:18:59+00:00
- Closed at: 2020-02-01T09:56:28+00:00
