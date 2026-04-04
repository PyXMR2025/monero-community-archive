---
title: Linux build issue with v0.15.0.5
source_url: https://github.com/monero-project/monero/issues/6412
author: kalibox
assignees: []
labels: []
created_at: '2020-04-01T07:45:16+00:00'
updated_at: '2020-04-04T17:50:37+00:00'
type: issue
status: closed
closed_at: '2020-04-04T17:50:37+00:00'
---

# Original Description
Hi,

I've followed the linux build instructions but always keep getting this error message:

[ 87%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/hmac_keccak.cpp.o
In file included from /usr/include/gtest/gtest.h:62,
                 from /home/xmr/Downloads/Temp/monero/tests/unit_tests/hmac_keccak.cpp:29:
/home/xmr/Downloads/Temp/monero/tests/unit_tests/hmac_keccak.cpp:126:1: error: static assertion failed: test_name must not be empty
  126 | TEST(keccak_hmac, )
      | ^~~~
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:388: tests/unit_tests/CMakeFiles/unit_tests.dir/hmac_keccak.cpp.o] Error 1
make[3]: Leaving directory '/home/xmr/Downloads/Temp/monero/build/Linux/release-v0.15/release'
make[2]: *** [CMakeFiles/Makefile2:4759: tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/home/xmr/Downloads/Temp/monero/build/Linux/release-v0.15/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/home/xmr/Downloads/Temp/monero/build/Linux/release-v0.15/release'
make: *** [Makefile:103: release-all] Error 2

Please can someone assist.

Thanks

# Discussion History
## sumogr | 2020-04-01T11:14:52+00:00
I dont know why you get this error on building tests, you shouldnt though, anyhow bypass building tests.
dont run `make release-all` , `make release` should be enough

## xiphon | 2020-04-01T11:19:21+00:00
https://github.com/monero-project/monero/pull/6346

## kalibox | 2020-04-01T11:27:36+00:00
> I dont know why you get this error on building tests, you shouldnt though, anyhow bypass building tests.
> dont run `make release-all` , `make release` should be enough

Thanks but I get this when building using "make" alone.

Is there another build command I should be using instead?

## sumogr | 2020-04-01T11:32:40+00:00
> > I dont know why you get this error on building tests, you shouldnt though, anyhow bypass building tests.
> > dont run `make release-all` , `make release` should be enough
> 
> Thanks but I get this when building using "make" alone.

clone again including @xiphon 's open PR that fixes this or like i said run `make release` it will exclude the tests (that are included by default in `make` or `make release-all`)

## kalibox | 2020-04-01T11:33:34+00:00
Ah I see, Got it. Thank you.

## moneromooo-monero | 2020-04-01T12:20:12+00:00
That's because it's using the OS' gtest, and they recently added a constraint on names.

## kalibox | 2020-04-01T12:45:48+00:00
Yes, "make release" works ok. My node is now running v0.15.0.5.

Out of interest, when's the next release scheduled for?

Cheers all

## moneromooo-monero | 2020-04-01T15:45:05+00:00
Not known yet.

# Action History
- Created by: kalibox | 2020-04-01T07:45:16+00:00
- Closed at: 2020-04-04T17:50:37+00:00
