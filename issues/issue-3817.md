---
title: error
source_url: https://github.com/monero-project/monero/issues/3817
author: SoraKohaku
assignees: []
labels: []
created_at: '2018-05-17T00:45:23+00:00'
updated_at: '2018-05-17T01:39:06+00:00'
type: issue
status: closed
closed_at: '2018-05-17T01:39:06+00:00'
---

# Original Description
/usr/bin/ld: /usr/lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:743: recipe for target 'tests/unit_tests/unit_tests' failed

# Discussion History
# Action History
- Created by: SoraKohaku | 2018-05-17T00:45:23+00:00
- Closed at: 2018-05-17T01:39:06+00:00
