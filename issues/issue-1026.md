---
title: Assumes name of "gcc-ar" and "gcc-ranlib" for gcc>=4.9 with lto enabled
source_url: https://github.com/monero-project/monero/issues/1026
author: alown
assignees: []
labels: []
created_at: '2016-08-31T22:27:14+00:00'
updated_at: '2016-09-14T20:53:05+00:00'
type: issue
status: closed
closed_at: '2016-09-14T20:53:05+00:00'
---

# Original Description
My distribution names the compiler based upon the architecture the compiler (and related tools) are built for, so the correct version of ar to use is named $CHOST-gcc-ar (which is itself a symlink to the selected alternative) and lives under /usr/$CHOST/bin/.

Normally, I would pass this information through -DCMAKE_AR/-DCMAKE_RANLIB when running cmake, but the root CMakeLists.txt has a check which nullifies doing so around line 419 (if USE_LTO && GNU && >= 4.9.0 && NOT OPENBSD).

Removing this if section allows build.  Perhaps the best option would be to only do this if CMAKE_AR and CMAKE_RANLIB are not already passed in by the user?


# Discussion History
## radfish | 2016-09-01T02:25:28+00:00
Thanks. Would this patch work? https://github.com/radfish/bitmonero/tree/PR--cmake-chost


## alown | 2016-09-14T20:53:05+00:00
resolved with #1065 


# Action History
- Created by: alown | 2016-08-31T22:27:14+00:00
- Closed at: 2016-09-14T20:53:05+00:00
