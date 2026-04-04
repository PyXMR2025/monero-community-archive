---
title: Failed on build
source_url: https://github.com/monero-project/monero-gui/issues/850
author: Ernillew
assignees: []
labels:
- resolved
created_at: '2017-09-03T16:27:16+00:00'
updated_at: '2019-07-22T05:00:53+00:00'
type: issue
status: closed
closed_at: '2018-03-30T02:18:19+00:00'
---

# Original Description
lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.3 LTS
Release:        16.04
Codename:       xenial

All packages is up-to-date.

/build.sh release-static

Error:

/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libcrypto.a(dso_dlfcn.o): undefined reference to symbol 'dlclose@@GLIBC_2.2.5'
//lib/x86_64-linux-gnu/libdl.so.2: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status
Makefile:274: recipe for target 'release/bin/monero-wallet-gui' failed
make: *** [release/bin/monero-wallet-gui] Error 1

# Discussion History
## italocoin-project | 2017-11-11T10:40:42+00:00
So, apparently you get this error because you need to instal QT from source!

## sanderfoobar | 2018-03-30T02:08:07+00:00
Resolving this issue for now. 

Please create a new issue if this happens on current master (and verified QT +5.7 is present).

## sanderfoobar | 2018-03-30T02:08:12+00:00
+resolved

## reeyon | 2019-07-22T05:00:53+00:00
> Resolving this issue for now.
> 
> Please create a new issue if this happens on current master (and verified QT +5.7 is present).

@xmrdsc may I know how did you resolve this error ?
it searched around with no solution.
debian 9.9
compiled everything with static. except for Qt.


# Action History
- Created by: Ernillew | 2017-09-03T16:27:16+00:00
- Closed at: 2018-03-30T02:18:19+00:00
