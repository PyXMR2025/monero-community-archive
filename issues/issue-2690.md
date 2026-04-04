---
title: 'Serialization.portability_wallet test on OSX - unknown file: Failure'
source_url: https://github.com/monero-project/monero/issues/2690
author: danrmiller
assignees: []
labels:
- tests
created_at: '2017-10-20T17:24:59+00:00'
updated_at: '2017-11-17T16:22:16+00:00'
type: issue
status: closed
closed_at: '2017-11-17T16:22:16+00:00'
---

# Original Description
Is there some new configuration needed for the serialization.portability_wallet test?
This passes on linux but fails on Mac:

```
Serialization.portability_wallet test: unknown file: Failure
C++ exception with description "context: asio.ssl error" thrown in the test body.
```

https://build.getmonero.org/builders/monero-static-osx-10.10/builds/2645/steps/test/logs/LastTest
https://build.getmonero.org/builders/monero-static-osx-10.11/builds/2653/steps/test/logs/LastTest

PASS:

https://build.getmonero.org/builders/monero-static-ubuntu-amd64/builds/2676/steps/test/logs/LastTest



# Discussion History
## moneromooo-monero | 2017-10-20T17:47:26+00:00
It got changed by https://github.com/monero-project/monero/pull/2523, but I don't see that'd break on Mac. The exception seems unrelated though. I don't see why ssl would have anything to do with that test...  Is there a stack trace in the test logs ?

## danrmiller | 2017-10-20T18:55:41+00:00


```
Note: Google Test filter = Serialization.portability_wallet
[==========] Running 1 test from 1 test case.
[----------] Global test environment set-up.
[----------] 1 test from Serialization
[ RUN      ] Serialization.portability_wallet

Program received signal SIGSEGV, Segmentation fault.
0x0000000100806921 in ssl_cipher_strength_sort ()
(gdb) thread apply all bt

Thread 1 (Thread 0x1803 of process 54238):
#0  0x0000000100806921 in ssl_cipher_strength_sort ()
#1  0x00000001008062c9 in ssl_create_cipher_list ()
#2  0x0000000100801ba2 in SSL_CTX_new ()
#3  0x0000000100311c6e in boost::asio::ssl::context::context(boost::asio::ssl::context_base::method) ()
#4  0x0000000100311691 in epee::net_utils::blocked_mode_client::blocked_mode_client() ()
#5  0x00000001003112ae in epee::net_utils::http::http_simple_client::http_simple_client() ()
#6  0x0000000100310975 in tools::wallet2::wallet2(bool, bool) ()
#7  0x00000001002f0336 in Serialization_portability_wallet_Test::TestBody() ()
#8  0x00000001006f0d9a in void testing::internal::HandleSehExceptionsInMethodIfSupported<testing::TestCase, void>(testing::TestCase*, void (testing::TestCase::*)(), char const*) ()
#9  0x00000001006b4a67 in void testing::internal::HandleExceptionsInMethodIfSupported<testing::Test, void>(testing::Test*, void (testing::Test::*)(), char const*) ()
#10 0x00000001006b49a5 in testing::Test::Run() ()
#11 0x00000001006b64c8 in testing::TestInfo::Run() ()
#12 0x00000001006b7ab7 in testing::TestCase::Run() ()
#13 0x00000001006c5c1c in testing::internal::UnitTestImpl::RunAllTests() ()
#14 0x00000001006f1d0a in bool testing::internal::HandleSehExceptionsInMethodIfSupported<testing::internal::UnitTestImpl, bool>(testing::internal::UnitTestImpl*, bool (testing::internal::UnitTestImpl::*)(), char const*) ()
#15 0x00000001006c5627 in bool testing::internal::HandleExceptionsInMethodIfSupported<testing::internal::UnitTestImpl, bool>(testing::internal::UnitTestImpl*, bool (testing::internal::UnitTestImpl::*)(), char const*) ()
#16 0x00000001006c54d8 in testing::UnitTest::Run() ()
#17 0x00000001001d38d7 in main ()
```

## moneromooo-monero | 2017-10-21T09:10:53+00:00
Maybe this will help: https://github.com/moneromooo-monero/bitmonero/tree/ssl_init

## danrmiller | 2017-10-21T22:15:59+00:00
#2696 didn't seem to make a difference, but I'm going to try https://github.com/moneromooo-monero/bitmonero/tree/ssl_init again to be sure.

By the way, I am also getting a different test failure on freebsd that looks very similar:

```
[----------] 2 tests from select_outputs
[ RUN      ] select_outputs.one_out_of_N
[New Thread 803406400 (LWP 100901/unit_tests)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 803406400 (LWP 100901/unit_tests)]
0x0000000000aedc55 in ssl_create_cipher_list ()
(gdb) thread apply all bt

Thread 2 (Thread 803406400 (LWP 100901/unit_tests)):
#0  0x0000000000aedc55 in ssl_create_cipher_list ()
#1  0x00000008014f11db in SSL_CTX_new () from /usr/lib/libssl.so.7
#2  0x00000000006bbb0f in boost::asio::ssl::context::context ()
#3  0x00000000006bb861 in epee::net_utils::blocked_mode_client::blocked_mode_client ()
#4  0x00000000006bb568 in epee::net_utils::http::http_simple_client::http_simple_client ()
#5  0x00000000006939b4 in tools::wallet2::wallet2 ()
#6  0x00000000007294a2 in select_outputs_one_out_of_N_Test::TestBody ()
#7  0x00000000009e9d23 in testing::internal::HandleSehExceptionsInMethodIfSupported<testing::Test, void> ()
#8  0x00000000009d4787 in testing::internal::HandleExceptionsInMethodIfSupported<testing::Test, void> ()
#9  0x00000000009ac197 in testing::Test::Run ()
#10 0x00000000009ad50c in testing::TestInfo::Run ()
#11 0x00000000009ae305 in testing::TestCase::Run ()
#12 0x00000000009ba855 in testing::internal::UnitTestImpl::RunAllTests ()
#13 0x00000000009e60b3 in testing::internal::HandleSehExceptionsInMethodIfSupported<testing::internal::UnitTestImpl, bool> ()
#14 0x00000000009d73d7 in testing::internal::HandleExceptionsInMethodIfSupported<testing::internal::UnitTestImpl, bool> ()
#15 0x00000000009ba425 in testing::UnitTest::Run ()
#16 0x00000000005bfeef in main ()
```



## radfish | 2017-10-22T14:57:34+00:00
Try running through valgrind maybe?

## danrmiller | 2017-10-23T03:30:56+00:00
I've been running them several times under osx and strangely they succeed occasionally.
The rest of the time they are failing: file not found "tests/data/wallet_9svHk1.keys"                               

```
Note: Google Test filter = Serialization.*
[==========] Running 12 tests from 1 test case.
[----------] Global test environment set-up.
[----------] 12 tests from Serialization
[ RUN      ] Serialization.BinaryArchiveInts
[       OK ] Serialization.BinaryArchiveInts (0 ms)
[ RUN      ] Serialization.BinaryArchiveVarInts
[       OK ] Serialization.BinaryArchiveVarInts (0 ms)
[ RUN      ] Serialization.Test1
[       OK ] Serialization.Test1 (0 ms)
[ RUN      ] Serialization.Overflow
[       OK ] Serialization.Overflow (0 ms)
[ RUN      ] Serialization.serializes_vector_uint64_as_varint
[       OK ] Serialization.serializes_vector_uint64_as_varint (0 ms)
[ RUN      ] Serialization.serializes_vector_int64_as_fixed_int
[       OK ] Serialization.serializes_vector_int64_as_fixed_int (0 ms)
[ RUN      ] Serialization.serializes_transacion_signatures_correctly
[       OK ] Serialization.serializes_transacion_signatures_correctly (0 ms)
[ RUN      ] Serialization.serializes_ringct_types
[       OK ] Serialization.serializes_ringct_types (56 ms)
[ RUN      ] Serialization.portability_wallet
2017-10-23 02:44:43.797   0x7fff742e9000        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2697     e || !exists. THROW EXCEPTION: error::file_not_found
2017-10-23 02:44:43.797   0x7fff742e9000        WARN    net.http        src/wallet/wallet_errors.h:707  /Users/administrator/bitmonero/src/wallet/wallet2.cpp:2697:N5tools5error15file_error_baseILi1EEE: file not found "tests/data/wallet_9svHk1.keys"                                                                                                                                        
/Users/administrator/bitmonero/tests/unit_tests/serialization.cpp:685: Failure
Value of: r
  Actual: false
Expected: true
[  FAILED  ] Serialization.portability_wallet (1 ms)
[ RUN      ] Serialization.portability_outputs
/Users/administrator/bitmonero/tests/unit_tests/serialization.cpp:798: Failure
Value of: r
  Actual: false
Expected: true
[  FAILED  ] Serialization.portability_outputs (0 ms)
[ RUN      ] Serialization.portability_unsigned_tx
/Users/administrator/bitmonero/tests/unit_tests/serialization.cpp:914: Failure
Value of: r
  Actual: false
Expected: true
[  FAILED  ] Serialization.portability_unsigned_tx (0 ms)
[ RUN      ] Serialization.portability_signed_tx
/Users/administrator/bitmonero/tests/unit_tests/serialization.cpp:1062: Failure
Value of: r
  Actual: false
Expected: true
[  FAILED  ] Serialization.portability_signed_tx (0 ms)
[----------] 12 tests from Serialization (57 ms total)

[----------] Global test environment tear-down
[==========] 12 tests from 1 test case ran. (57 ms total)
[  PASSED  ] 8 tests.
[  FAILED  ] 4 tests, listed below:
[  FAILED  ] Serialization.portability_wallet
[  FAILED  ] Serialization.portability_outputs
[  FAILED  ] Serialization.portability_unsigned_tx
[  FAILED  ] Serialization.portability_signed_tx

 4 FAILED TESTS
7715:unit_tests administrator$ clear
7715:unit_tests administrator$ ./unit_tests
Note: Google Test filter = Serialization.*
[==========] Running 12 tests from 1 test case.
[----------] Global test environment set-up.
[----------] 12 tests from Serialization
[ RUN      ] Serialization.BinaryArchiveInts
[       OK ] Serialization.BinaryArchiveInts (0 ms)
[ RUN      ] Serialization.BinaryArchiveVarInts
[       OK ] Serialization.BinaryArchiveVarInts (0 ms)
[ RUN      ] Serialization.Test1
[       OK ] Serialization.Test1 (0 ms)
[ RUN      ] Serialization.Overflow
[       OK ] Serialization.Overflow (0 ms)
[ RUN      ] Serialization.serializes_vector_uint64_as_varint
[       OK ] Serialization.serializes_vector_uint64_as_varint (0 ms)
[ RUN      ] Serialization.serializes_vector_int64_as_fixed_int
[       OK ] Serialization.serializes_vector_int64_as_fixed_int (0 ms)
[ RUN      ] Serialization.serializes_transacion_signatures_correctly
[       OK ] Serialization.serializes_transacion_signatures_correctly (0 ms)
[ RUN      ] Serialization.serializes_ringct_types
[       OK ] Serialization.serializes_ringct_types (57 ms)
[ RUN      ] Serialization.portability_wallet
2017-10-23 02:44:54.828   0x7fff742e9000        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2697     e || !exists. THROW EXCEPTION: error::file_not_found
2017-10-23 02:44:54.829   0x7fff742e9000        WARN    net.http        src/wallet/wallet_errors.h:707  /Users/administrator/bitmonero/src/wallet/wallet2.cpp:2697:N5tools5error15file_error_baseILi1EEE: file not found "tests/data/wallet_9svHk1.keys"
/Users/administrator/bitmonero/tests/unit_tests/serialization.cpp:685: Failure
Value of: r
  Actual: false
Expected: true
[  FAILED  ] Serialization.portability_wallet (1 ms)
[ RUN      ] Serialization.portability_outputs
/Users/administrator/bitmonero/tests/unit_tests/serialization.cpp:798: Failure
Value of: r
  Actual: false
Expected: true
[  FAILED  ] Serialization.portability_outputs (0 ms)
[ RUN      ] Serialization.portability_unsigned_tx
/Users/administrator/bitmonero/tests/unit_tests/serialization.cpp:914: Failure
Value of: r
  Actual: false
Expected: true
[  FAILED  ] Serialization.portability_unsigned_tx (0 ms)
[ RUN      ] Serialization.portability_signed_tx
/Users/administrator/bitmonero/tests/unit_tests/serialization.cpp:1062: Failure
Value of: r
  Actual: false
Expected: true
[  FAILED  ] Serialization.portability_signed_tx (0 ms)
[----------] 12 tests from Serialization (58 ms total)

[----------] Global test environment tear-down
[==========] 12 tests from 1 test case ran. (58 ms total)
[  PASSED  ] 8 tests.
[  FAILED  ] 4 tests, listed below:
[  FAILED  ] Serialization.portability_wallet
[  FAILED  ] Serialization.portability_outputs
[  FAILED  ] Serialization.portability_unsigned_tx
[  FAILED  ] Serialization.portability_signed_tx

 4 FAILED TESTS
```

## danrmiller | 2017-10-23T04:27:05+00:00
radfish thanks, the freebsd test issue isn't happening for me now from the ssl_init PR branch. If I see it again, I'll run it in valgrind and open a new issue.


## moneromooo-monero | 2017-10-23T08:54:38+00:00
Run this way:
./build/release/tests/unit_tests/unit_tests
Otherwise you've got to pass the data directory as argument.


## radfish | 2017-10-24T00:03:41+00:00
It should not matter what your working directory is, it should work without args when launched from any dir. What does matter is what your build directory is. The default behavior (that's how it was before and how it is now) expects two levels: build/release. If your build directory is build/ then the file will not be found. If your dir is build/release, then please run with `strace -f -e trace=file ...` to find exactly why it's looking in the wrong place.

## moneromooo-monero | 2017-10-24T09:23:43+00:00
https://github.com/monero-project/monero/pull/2720

## danrmiller | 2017-11-01T15:25:44+00:00
I get the same results with #2720 

@moneromooo-monero wrote:

> Run this way:
> ./build/release/tests/unit_tests/unit_tests 

I am running "make release-test" in dir /Users/buildbot/slave/monero-static-osx-10_11/build

(The directory name "build" can be a little confusing, but it is the root directory buildbot clones the project into, a subordinate "build" directory is created by the makefile.)

https://build.getmonero.org/builders/monero-static-osx-10.11/builds/2703

```
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && /Applications/Xcode.app/Contents/Developer/usr/bin/make && /Applications/Xcode.app/Contents/Developer/usr/bin/make test
```

https://build.getmonero.org/builders/monero-static-osx-10.11/builds/2703/steps/test/logs/LastTest

```
Command: "/Users/buildbot/slave/monero-static-osx-10_11/build/build/release/tests/unit_tests/unit_tests" "--data-dir" "/Users/buildbot/slave/monero-static-osx-10_11/build/tests/data"
Directory: /Users/buildbot/slave/monero-static-osx-10_11/build/build/release/tests/unit_tests
```

So is the point that here it should be "--data-dir" "/Users/buildbot/slave/monero-static-osx-10_11/build/build/release/tests/data" instead of "/Users/buildbot/slave/monero-static-osx-10_11/build/tests/data"?


## moneromooo-monero | 2017-11-01T16:40:08+00:00
Oh, is that something you generate yourself ? I recently changed it to use a --data-dir argument, so if so, you'd have to chance it yes. Sorry I did not realize you had those commands separately as they're in the makefile.

## danrmiller | 2017-11-01T16:56:53+00:00
No the only thing I run is "make release-test".

From running that I find those commands in the build/release/Testing/Temporary/LastTest.log file and the above is an excerpt of that.

## moneromooo-monero | 2017-11-01T19:03:22+00:00
OK, I was confused, the command shows "--data-dir", but I read your comment as implying the directory was there alone. This does seem to be a red herring then.

## danrmiller | 2017-11-01T19:16:58+00:00
+tests

## danrmiller | 2017-11-17T16:22:16+00:00
These are passing now.

# Action History
- Created by: danrmiller | 2017-10-20T17:24:59+00:00
- Closed at: 2017-11-17T16:22:16+00:00
