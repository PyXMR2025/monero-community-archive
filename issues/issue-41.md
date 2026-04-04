---
title: 'Kovri: ARMv8 dynamic build attempts to link to kovri-static directory'
source_url: https://github.com/monero-project/meta/issues/41
author: anonimal
assignees: []
labels: []
created_at: '2017-01-23T18:43:12+00:00'
updated_at: '2017-01-25T19:02:23+00:00'
type: issue
status: closed
closed_at: '2017-01-25T19:02:23+00:00'
---

# Original Description
https://build.getmonero.org/builders/kovri-all-debian-arm8/builds/116/steps/compile/logs/stdio

```
[100%] Linking CXX executable ../../kovri
/usr/bin/ld: /home/buildbot/slave/kovri-static-debian-arm8/build/deps/cpp-netlib/build/libs/network/src/libcppnetlib-client-connections.a(client.cpp.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against external symbol `_ZTVSt8bad_cast@@GLIBCXX_3.4' can not be used when making a shared object; recompile with -fPIC
/usr/bin/ld: /home/buildbot/slave/kovri-static-debian-arm8/build/deps/cpp-netlib/build/libs/network/src/libcppnetlib-client-connections.a(client.cpp.o)(.text._ZN5boost16exception_detail10clone_implINS0_19error_info_injectorISt8bad_castEEEC1ERKS4_[_ZN5boost16exception_detail10clone_implINS0_19error_info_injectorISt8bad_castEEEC1ERKS4_]+0x14): unresolvable R_AARCH64_ADR_PREL_PG_HI21 relocation against symbol `_ZTVSt8bad_cast@@GLIBCXX_3.4'
/usr/bin/ld: final link failed: Bad value
```

# Discussion History
## anonimal | 2017-01-25T19:02:23+00:00
The solution was to remove `~/.cmake`. Referencing https://github.com/monero-project/kovri/issues/524

@danrmiller I don't know how sandboxed the two builders were/are but, if the registry for the dynamic build was somehow still referencing the static, I think the issue makes more sense now.

# Action History
- Created by: anonimal | 2017-01-23T18:43:12+00:00
- Closed at: 2017-01-25T19:02:23+00:00
