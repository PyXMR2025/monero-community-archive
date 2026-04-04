---
title: 'Could NOT find GTest (missing:  GTEST_LIBRARY GTEST_MAIN_LIBRARY) '
source_url: https://github.com/monero-project/monero/issues/983
author: ghost
assignees: []
labels: []
created_at: '2016-08-24T01:24:36+00:00'
updated_at: '2016-09-02T20:29:33+00:00'
type: issue
status: closed
closed_at: '2016-09-02T20:29:33+00:00'
---

# Original Description
Looks like this is another dependency on Ubuntu 16.04:

libgtest-dev

And actually this is more complicated than it first seems because:
1. It doesn't come compiled
2. It doesn't actually work even if compiled

So I've tried compiling googletest from their git repo with no success yet...still getting failures on 'make test' for googletest itself (version 1.7.0)

Could I request future versions also include the test suite?


# Discussion History
## radfish | 2016-08-25T02:25:11+00:00
First a note: gtest is included in the source tree as a vendored dependency, so bitmonerod will build fine without gtest installed on the system. But agreed that it should also build with gtest installed on system, if one is found. I think there are two problems with that currently
1. #980 -- a bug in cmake script
2. no package on Ubuntu with built gtest (judging from your report; on Arch gest pkg does include libgtest.so) -- do you know why? there must be some reason.

Sidenote: since cmake does build the tests with in-tree gtest successfully, you could compare that working build of gest with your standalone build of gtest.


## ghost | 2016-08-25T19:58:02+00:00
Thanks @radfish. Can you give me any tips how to run the tests with in-tree gtest? 

make release-test just borks.


## radfish | 2016-08-26T05:40:46+00:00
Can you uninstall the gtest package (libgtest-dev I guess) from your system and try again?
Also, where does it bork, could you paste the output please?


## radfish | 2016-09-01T15:13:41+00:00
gtest patch merged, this can be closed


## ghost | 2016-09-02T20:29:33+00:00
Thanks! Will test this weekend hopefully.


# Action History
- Created by: ghost | 2016-08-24T01:24:36+00:00
- Closed at: 2016-09-02T20:29:33+00:00
