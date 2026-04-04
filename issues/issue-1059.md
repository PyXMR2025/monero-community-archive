---
title: 'translation_files.h: No such file or directory'
source_url: https://github.com/monero-project/monero-gui/issues/1059
author: danrmiller
assignees: []
labels: []
created_at: '2018-01-03T19:03:46+00:00'
updated_at: '2018-01-16T22:59:17+00:00'
type: issue
status: closed
closed_at: '2018-01-16T22:59:16+00:00'
---

# Original Description
https://build.getmonero.org/builders/monero-core-ubuntu-amd64/builds/1184/steps/compile/logs/stdio

```
Scanning dependencies of target obj_cryptonote_basic
[ 61%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
[ 62%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o
[ 62%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/obj_common.dir/util.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/obj_common.dir/i18n.cpp.o
/home/vagrant/slave/monero-core-ubuntu-amd64/build/monero/src/common/i18n.cpp:38:31: fatal error: translation_files.h: No such file or directory
compilation terminated.
src/common/CMakeFiles/obj_common.dir/build.make:182: recipe for target 'src/common/CMakeFiles/obj_common.dir/i18n.cpp.o' failed
```

# Discussion History
## stoffu | 2018-01-04T03:25:21+00:00
I think https://github.com/monero-project/monero/pull/3061 will fix this.

## danrmiller | 2018-01-16T22:59:16+00:00
Fixed by https://github.com/monero-project/monero/pull/3061

# Action History
- Created by: danrmiller | 2018-01-03T19:03:46+00:00
- Closed at: 2018-01-16T22:59:16+00:00
