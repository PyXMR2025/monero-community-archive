---
title: compile error
source_url: https://github.com/monero-project/monero-gui/issues/2232
author: NacJidtyd6op
assignees: []
labels: []
created_at: '2019-06-22T15:45:21+00:00'
updated_at: '2019-07-01T22:08:26+00:00'
type: issue
status: closed
closed_at: '2019-07-01T22:08:26+00:00'
---

# Original Description
i have some errors with last version of gui

compile was successful before

[ 50%] Building CXX object src/CMakeFiles/obj_version.dir/__/version.cpp.o
^[[91mcc1plus: error: -Werror=user-defined-warnings: no option -Wuser-defined-warnings
^[[0m^[[91mmake[3]: *** [src/CMakeFiles/obj_version.dir/__/version.cpp.o] Error 1
^[[0msrc/CMakeFiles/obj_version.dir/build.make:66: recipe for target 'src/CMakeFiles/obj_version.dir/__/version.cpp.o' failed
make[3]: Leaving directory 'monero-gui/monero/build/release'
^[[91mmake[2]: *** [src/CMakeFiles/obj_version.dir/all] Error 2
^[[0mCMakeFiles/Makefile2:592: recipe for target 'src/CMakeFiles/obj_version.dir/all' failed
make[2]: Leaving directory 'monero-gui/monero/build/release'
CMakeFiles/Makefile2:641: recipe for target 'src/CMakeFiles/version.dir/rule' failed
make[1]: Leaving directory 'monero-gui/monero/build/release'
^[[91mmake[1]: *** [src/CMakeFiles/version.dir/rule] Error 2
^[[0m^[[91mmake: *** [version] Error 2
^[[0mMakefile:279: recipe for target 'version' failed
make: Leaving directory 'monero-gui/monero/build/release'
Scanning dependencies of target generate_translations_header
[  0%] Creating directories for 'generate_translations_header'
[  0%] Built target genversion
[  1%] Building CXX object src/CMakeFiles/obj_version.dir/__/version.cpp.o
^[[91mcc1plus: error: -Werror=user-defined-warnings: no option -Wuser-defined-warnings
^[[0msrc/CMakeFiles/obj_version.dir/build.make:66: recipe for target 'src/CMakeFiles/obj_version.dir/__/version.cpp.o' failed
^[[91mmake[2]: *** [src/CMakeFiles/obj_version.dir/__/version.cpp.o] Error 1
^[[0m^[[91mmake[1]: *** [src/CMakeFiles/obj_version.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....


# Discussion History
## selsta | 2019-06-22T15:54:20+00:00
Can you try with a fresh git clone?

## NacJidtyd6op | 2019-06-22T17:32:38+00:00
i did it before 10 hours...

# Action History
- Created by: NacJidtyd6op | 2019-06-22T15:45:21+00:00
- Closed at: 2019-07-01T22:08:26+00:00
