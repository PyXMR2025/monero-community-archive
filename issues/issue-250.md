---
title: How was boost built on the freebsd machine?
source_url: https://github.com/monero-project/meta/issues/250
author: anonimal
assignees: []
labels: []
created_at: '2018-06-26T03:05:32+00:00'
updated_at: '2020-03-09T21:54:56+00:00'
type: issue
status: closed
closed_at: '2020-03-09T21:54:56+00:00'
---

# Original Description
https://build.getmonero.org/builders/kovri-all-freebsd64/builds/991/steps/compile/logs/stdio

# Discussion History
## anonimal | 2018-06-26T03:06:33+00:00
#248

## danrmiller | 2018-07-15T03:57:00+00:00
Boost 1.66 from https://www.boost.org/users/history/version_1_66_0.html

user-config.jam:
```
using clang : : c++ : <cxxflags>"-fvisibility=hidden -fPIC" <linkflags>"" <archiver>"ar" <striper>"strip"  <ranlib>"ranlib" <rc>"" : ;
```
```
./bootstrap.sh --with-libraries=chrono,log,program_options,date_time,thread,system,filesystem,regex,test
```

```
./b2 -d0 runtime-link=shared threadapi=pthread threading=multi link=static variant=release --layout=tagged --build-type=complete --user-config=user-config.jam -sNO_BZIP2=1 --prefix=/usr/local install cxxflags="-fPIC" linkflags="-fPIC"
```

## coneiric | 2018-07-19T01:02:34+00:00
Tried to reproduce the issue locally, and everything builds fine.

System details:

* FreeBSD 11.1
* Boost 1.66 (system package)
* Clang 4.0.0
* build command: `make all-options`,`make release`, and `make release-static` complete successfully

## danrmiller | 2018-07-30T00:16:00+00:00
@coneiric We can't use the system packages if we will also build a static monero because we will need them build with the -fPIC flag.

## coneiric | 2018-07-31T03:35:12+00:00
@danrmiller I didn't realize that, thanks for cluing me in :) Will continue to help troubleshoot.

# Action History
- Created by: anonimal | 2018-06-26T03:05:32+00:00
- Closed at: 2020-03-09T21:54:56+00:00
