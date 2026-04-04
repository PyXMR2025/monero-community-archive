---
title: Unable to build 0.18.3.1 from source
source_url: https://github.com/monero-project/monero/issues/9018
author: snex
assignees: []
labels: []
created_at: '2023-10-11T03:39:43+00:00'
updated_at: '2023-11-06T16:05:46+00:00'
type: issue
status: closed
closed_at: '2023-11-06T16:05:45+00:00'
---

# Original Description
Ubuntu Linux 22.04 amd64

```
/usr/bin/ld: CMakeFiles/unit_tests.dir/account.cpp.o: in function `testing::AssertionResult testing::internal::CmpHelperEQFailure<cryptonote::account_public_address, cryptonote::account_public_address>(char const*, char const*, cryptonote::account_public_address const&, cryptonote::account_public_address const&)':
account.cpp:(.text._ZN7testing8internal18CmpHelperEQFailureIN10cryptonote22account_public_addressES3_EENS_15AssertionResultEPKcS6_RKT_RKT0_[_ZN7testing8internal18CmpHelperEQFailureIN10cryptonote22account_public_addressES3_EENS_15AssertionResultEPKcS6_RKT_RKT0_]+0x271): undefined reference to `testing::internal2::PrintBytesInObjectTo(unsigned char const*, unsigned long, std::ostream*)'
/usr/bin/ld: account.cpp:(.text._ZN7testing8internal18CmpHelperEQFailureIN10cryptonote22account_public_addressES3_EENS_15AssertionResultEPKcS6_RKT_RKT0_[_ZN7testing8internal18CmpHelperEQFailureIN10cryptonote22account_public_addressES3_EENS_15AssertionResultEPKcS6_RKT_RKT0_]+0x57a): undefined reference to `testing::internal2::PrintBytesInObjectTo(unsigned char const*, unsigned long, std::ostream*)'
/usr/bin/ld: CMakeFiles/unit_tests.dir/epee_utils.cpp.o: in function `testing::AssertionResult testing::internal::CmpHelperOpFailure<decltype(nullptr), unsigned char*>(char const*, char const*, decltype(nullptr) const&, unsigned char* const&, char const*)':
epee_utils.cpp:(.text._ZN7testing8internal18CmpHelperOpFailureIDnPhEENS_15AssertionResultEPKcS5_RKT_RKT0_S5_[_ZN7testing8internal18CmpHelperOpFailureIDnPhEENS_15AssertionResultEPKcS5_RKT_RKT0_S5_]+0x7de): undefined reference to `testing::internal2::PrintBytesInObjectTo(unsigned char const*, unsigned long, std::ostream*)'
/usr/bin/ld: CMakeFiles/unit_tests.dir/epee_utils.cpp.o: in function `testing::AssertionResult testing::internal::CmpHelperEQ<epee::net_utils::address_type, epee::net_utils::address_type>(char const*, char const*, epee::net_utils::address_type const&, epee::net_utils::address_type const&)':
epee_utils.cpp:(.text._ZN7testing8internal11CmpHelperEQIN4epee9net_utils12address_typeES4_EENS_15AssertionResultEPKcS7_RKT_RKT0_[_ZN7testing8internal11CmpHelperEQIN4epee9net_utils12address_typeES4_EENS_15AssertionResultEPKcS7_RKT_RKT0_]+0x27d): undefined reference to `testing::internal2::PrintBytesInObjectTo(unsigned char const*, unsigned long, std::ostream*)'
/usr/bin/ld: epee_utils.cpp:(.text._ZN7testing8internal11CmpHelperEQIN4epee9net_utils12address_typeES4_EENS_15AssertionResultEPKcS7_RKT_RKT0_[_ZN7testing8internal11CmpHelperEQIN4epee9net_utils12address_typeES4_EENS_15AssertionResultEPKcS7_RKT_RKT0_]+0x57a): undefined reference to `testing::internal2::PrintBytesInObjectTo(unsigned char const*, unsigned long, std::ostream*)'
/usr/bin/ld: CMakeFiles/unit_tests.dir/epee_utils.cpp.o:epee_utils.cpp:(.text._ZN7testing8internal11CmpHelperEQIN4epee9net_utils4zoneES4_EENS_15AssertionResultEPKcS7_RKT_RKT0_[_ZN7testing8internal11CmpHelperEQIN4epee9net_utils4zoneES4_EENS_15AssertionResultEPKcS7_RKT_RKT0_]+0x27d): more undefined references to `testing::internal2::PrintBytesInObjectTo(unsigned char const*, unsigned long, std::ostream*)' follow
collect2: error: ld returned 1 exit status
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1374: tests/unit_tests/unit_tests] Error 1
make[3]: Leaving directory 'monero/build/Linux/v0.18.3.1/release'
make[2]: *** [CMakeFiles/Makefile2:5374: tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory 'monero/build/Linux/v0.18.3.1/release'
make[1]: *** [Makefile:146: all] Error 2
make[1]: Leaving directory 'monero/build/Linux/v0.18.3.1/release'
make: *** [Makefile:103: release-all] Error 2
```

# Discussion History
## snex | 2023-10-11T04:00:56+00:00
Update - it seems all the binaries get built, just some unit tests that are failing to build.

## selsta | 2023-10-11T04:04:53+00:00
All our build tests pass for v0.18.3.1, can you share which command you are using to build?

## snex | 2023-10-11T04:07:36+00:00
Checked out new branch:

```
git checkout -b v0.18.3.1 v0.18.3.1
```

Then:
```
cd build
make
```

This has always worked before.

## selsta | 2023-10-11T04:08:22+00:00
Did you try a clean build?

## snex | 2023-10-11T04:09:22+00:00
I did.

## selsta | 2023-10-11T04:12:26+00:00
cd build
make

is incorrect, you either just do make in the top level directory or you have to clean your build directly and run cmake first before running make.

## snex | 2023-10-11T04:14:35+00:00
Yeah - you are correct. I was typing that from memory. When i "make" from the root folder I get the errors I pasted above.

## selsta | 2023-10-11T04:16:37+00:00
https://github.com/monero-project/monero/actions/runs/6384731209/job/17327984375

This was a build test on Ubuntu 22.04 for v0.18.3.1 and there were no build issues.

I'll try later today in a VM but at this point I think it's an issue on your local system.

## snex | 2023-10-11T04:17:39+00:00
Since all the binaries built and seem to work fine, I'd say it's not super important anyway.

## selsta | 2023-11-05T02:44:12+00:00
Do you have libgtest-dev installed? If yes, can you try to uninstall it and build again? Seems there is some gtest header mismatch but not sure why.

## snex | 2023-11-05T21:06:40+00:00
I do not have libgtest-dev installed. I can install it and try again.

## snex | 2023-11-06T16:05:45+00:00
That did the trick. make completes now. Thanks.

# Action History
- Created by: snex | 2023-10-11T03:39:43+00:00
- Closed at: 2023-11-06T16:05:45+00:00
