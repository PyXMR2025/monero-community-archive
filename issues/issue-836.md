---
title: UNBOUND_LIBRARIES error building on Ubuntu 14.04
source_url: https://github.com/monero-project/monero/issues/836
author: laanwj
assignees: []
labels: []
created_at: '2016-05-11T10:44:58+00:00'
updated_at: '2016-07-07T20:00:52+00:00'
type: issue
status: closed
closed_at: '2016-07-07T20:00:52+00:00'
---

# Original Description
I get the following error running cmake on Ubuntu 14.04 (cmake is version 2.8.12.2):

```
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
UNBOUND_LIBRARIES
    linked by target "unit_tests" in directory /home/ubuntu/bitmonero/tests/unit_tests
```

Both `v0.9.4` and `master` suffer from this.

According to `git bisect` this broke with commit 34957fcbb97052532b8f16f7cb2bd637904e047b:

```
34957fcbb97052532b8f16f7cb2bd637904e047b is the first bad commit
commit 34957fcbb97052532b8f16f7cb2bd637904e047b
Author: moneromooo-monero <moneromooo-monero@users.noreply.github.com>
Date:   Tue Mar 29 17:56:42 2016 +0100

    tests: add test for needed OpenSSL algorithms in unbound

    These can be compiled out of libunbound, leading to failure
    to check DNSSEC validity.

:040000 040000 62634aa5c46564ec73045609a54073f7c6e94725 1abfe5464ee2743d47d8025394a470e937fe2e79 M      tests
```

I see that the problem was also reported here on bitcoin talk: https://bitcointalk.org/index.php?topic=652305.msg14613563#msg14613563

Building without tests works around this problem.


# Discussion History
## dEBRUYNE-1 | 2016-05-12T15:35:20+00:00
Quoting @hyc here:

> Yes, tests got broken in a recent commit. You should use the v0.9.4 tag instead of master. Or you can merge this patch into your build tree: https://github.com/monero-project/bitmonero/pull/811

Source: https://www.reddit.com/r/Monero/comments/4gakjp/maam_13_monero_ask_anything_monday/d2gvq8o?context=3

EDIT: It seems like v0.9.4 doesn't work for you too.


## laanwj | 2016-05-12T16:46:49+00:00
Thanks, but that indeed seems like a different issue.
Also #811 is a change in the source code, as cmake complains I'd expect to fix this would need a change in the cmake file.


## dEBRUYNE-1 | 2016-05-12T18:33:48+00:00
I see, after reading the thread these other "fixes" were suggested:

@hyc suggested:

> Pretty sure that UNBOUND problem was introduced _after_ the 0.9.4 release. Quick workaround is to edit build/release/CMakeCache.txt and change "BUILD_TESTS" from "ON" to "OFF" then do "make rebuild_cache" and then "make" again.

@iamsmooth suggested:

> Maybe try compiling 0.9.4 itself rather than possibly-unstable changes after that
> 
> git checkout v0.9.4
> make clean (this will wipe out the 'build' subdirectory; make sure you don't have any wallets in there)
> make

EDIT: Seems like you've already tried both these "fixes" though, but I'll leave them here in case anyone else stumbles upon the same issue. 

P.S. I've forwarded the issue to @moneromooo-monero as well. 


## moneromooo-monero | 2016-05-12T19:34:59+00:00
Fixed in https://github.com/monero-project/bitmonero/pull/831


## hyc | 2016-05-13T15:50:34+00:00
Specifically, in commit https://github.com/monero-project/bitmonero/pull/831/commits/7a663873cebd135eb32ca68ad1f05873e29248a9


## laanwj | 2016-05-14T07:50:00+00:00
Can confirm that #831 fixes this issue.


## fluffypony | 2016-07-07T20:00:52+00:00
Fixed


# Action History
- Created by: laanwj | 2016-05-11T10:44:58+00:00
- Closed at: 2016-07-07T20:00:52+00:00
