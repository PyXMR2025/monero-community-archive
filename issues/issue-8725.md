---
title: One off crash in race condition unit test
source_url: https://github.com/monero-project/monero/issues/8725
author: moneromooo-monero
assignees: []
labels:
- bug
- tests
created_at: '2023-01-31T07:46:01+00:00'
updated_at: '2023-09-21T17:20:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is a one off, the test usually succeeds.


The following tests FAILED:
	  8 - unit_tests (Child aborted)


[----------] 2 tests from node_server
[ RUN      ] node_server.bind_same_p2p_port
[       OK ] node_server.bind_same_p2p_port (4 ms)
[ RUN      ] node_server.race_condition
terminate called without an active exception
<end of output>



#0  0x00007e90ccb3ae35 in raise () from /lib64/libc.so.6
#1  0x00007e90ccb25895 in abort () from /lib64/libc.so.6
#2  0x000058e745ce4141 in __gnu_cxx::__verbose_terminate_handler() [clone .cold] ()
#3  0x000058e747565b2c in __cxxabiv1::__terminate(void (*)()) ()
#4  0x000058e747565b97 in std::terminate() ()
#5  0x000058e745f905d2 in std::vector<std::thread, std::allocator<std::thread> >::~vector() ()
#6  0x000058e745bbc91b in node_server_race_condition_Test::TestBody()::{lambda(node_server_race_condition_Test::TestBody()::protocol_t&)#1}::operator()(node_server_race_condition_Test::TestBody()::protocol_t&) const [clone .isra.0] [clone .cold] ()
#7  0x000058e74627cddf in node_server_race_condition_Test::TestBody() ()
#8  0x000058e746dfaae9 in void testing::internal::HandleSehExceptionsInMethodIfSupported<testing::Test, void>(testing::Test*, void (testing::Test::*)(), char const*) ()
#9  0x000058e746df51ca in void testing::internal::HandleExceptionsInMethodIfSupported<testing::Test, void>(testing::Test*, void (testing::Test::*)(), char const*) ()
#10 0x000058e746dda464 in testing::Test::Run() ()
#11 0x000058e746ddace0 in testing::TestInfo::Run() ()
#12 0x000058e746ddb331 in testing::TestCase::Run() ()
#13 0x000058e746de1e2c in testing::internal::UnitTestImpl::RunAllTests() ()
#14 0x000058e746dfbc7a in bool testing::internal::HandleSehExceptionsInMethodIfSupported<testing::internal::UnitTestImpl, bool>(testing::internal::UnitTestImpl*, bool (testing::internal::UnitTestImpl::*)(), char const*) ()
#15 0x000058e746df6096 in bool testing::internal::HandleExceptionsInMethodIfSupported<testing::internal::UnitTestImpl, bool>(testing::internal::UnitTestImpl*, bool (testing::internal::UnitTestImpl::*)(), char const*) ()
#16 0x000058e746de0b32 in testing::UnitTest::Run() ()
#17 0x000058e745d10c6c in main ()


# Discussion History
## UkoeHB | 2023-02-05T20:59:58+00:00
I see this one fail occasionally on CI.

## 0xFFFC0000 | 2023-08-09T18:44:01+00:00
I do see this occasionally too. 

# Action History
- Created by: moneromooo-monero | 2023-01-31T07:46:01+00:00
