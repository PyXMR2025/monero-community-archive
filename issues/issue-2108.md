---
title: debian compile fails
source_url: https://github.com/monero-project/monero/issues/2108
author: golangdude
assignees: []
labels: []
created_at: '2017-06-23T07:27:09+00:00'
updated_at: '2017-06-23T15:03:12+00:00'
type: issue
status: closed
closed_at: '2017-06-23T15:03:12+00:00'
---

# Original Description
Building latest head 038e6cd, debian stretch 64-bit:

# make release-static
...
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec3.c.o
[ 33%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec.c.o
[ 33%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.o
/root/monero/external/unbound/validator/val_secalgo.c: In function 'setup_dsa_sig':
/root/monero/external/unbound/validator/val_secalgo.c:256:8: error: dereferencing pointer to incomplete type 'DSA_SIG {aka struct DSA_SIG_st}'
  dsasig->r = R;
        ^~
/root/monero/external/unbound/validator/val_secalgo.c: In function 'setup_ecdsa_sig':
/root/monero/external/unbound/validator/val_secalgo.c:291:11: error: dereferencing pointer to incomplete type 'ECDSA_SIG {aka struct ECDSA_SIG_st}'
  ecdsa_sig->r = BN_bin2bn(*sig, bnsize, ecdsa_sig->r);
           ^~
/root/monero/external/unbound/validator/val_secalgo.c: In function 'verify_canonrrset':
/root/monero/external/unbound/validator/val_secalgo.c:513:13: error: storage size of 'ctx' isn't known
  EVP_MD_CTX ctx;
             ^~~
/root/monero/external/unbound/validator/val_secalgo.c:564:5: warning: implicit declaration of function 'EVP_MD_CTX_cleanup' [-Wimplicit-function-declaration]
  if(EVP_MD_CTX_cleanup(&ctx) == 0) {
     ^~~~~~~~~~~~~~~~~~
external/unbound/CMakeFiles/unbound.dir/build.make:1334: recipe for target 'external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.o' failed
make[3]: *** [external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.o] Error 1
make[3]: Leaving directory '/root/monero/build/release'
CMakeFiles/Makefile2:204: recipe for target 'external/unbound/CMakeFiles/unbound.dir/all' failed
make[2]: *** [external/unbound/CMakeFiles/unbound.dir/all] Error 2
make[2]: Leaving directory '/root/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero/build/release'
Makefile:62: recipe for target 'release-static' failed
make: *** [release-static] Error 2

# Discussion History
## golangdude | 2017-06-23T07:35:37+00:00
It happens with 0.10.3.1 as well.

## golangdude | 2017-06-23T08:11:05+00:00
# make  (non static) failed too:

[ 78%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/address_from_url.cpp.o
[ 79%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/ban.cpp.o
/root/monero/tests/unit_tests/ban.cpp: In function 'bool is_blocked(Server&, uint32_t, time_t*)':
/root/monero/tests/unit_tests/ban.cpp:79:43: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   std::map<uint32_t, time_t> ips = server.get_blocked_ips();
                                           ^~~~~~~~~~~~~~~
In file included from /root/monero/tests/gtest/include/gtest/gtest.h:58:0,
                 from /root/monero/tests/unit_tests/ban.cpp:31:
/root/monero/tests/unit_tests/ban.cpp: In member function 'virtual void ban_add_Test::TestBody()':
/root/monero/tests/unit_tests/ban.cpp:100:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   ASSERT_TRUE(server.get_blocked_ips().empty());
                      ^
/root/monero/tests/unit_tests/ban.cpp:105:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'block_ip'; did you mean 'block_host'?
   ASSERT_TRUE(server.block_ip(MAKE_IP(1,2,3,4)));
                      ^
/root/monero/tests/unit_tests/ban.cpp:106:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   ASSERT_TRUE(server.get_blocked_ips().size() == 1);
                      ^
/root/monero/tests/unit_tests/ban.cpp:111:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'block_ip'; did you mean 'block_host'?
   ASSERT_TRUE(server.block_ip(MAKE_IP(1,2,3,4)));
                      ^
/root/monero/tests/unit_tests/ban.cpp:112:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   ASSERT_TRUE(server.get_blocked_ips().size() == 1);
                      ^
/root/monero/tests/unit_tests/ban.cpp:117:23: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'unblock_ip'; did you mean 'unblock_host'?
   ASSERT_FALSE(server.unblock_ip(MAKE_IP(1,2,3,5)));
                       ^
/root/monero/tests/unit_tests/ban.cpp:118:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   ASSERT_TRUE(server.get_blocked_ips().size() == 1);
                      ^
/root/monero/tests/unit_tests/ban.cpp:123:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'unblock_ip'; did you mean 'unblock_host'?
   ASSERT_TRUE(server.unblock_ip(MAKE_IP(1,2,3,4)));
                      ^
/root/monero/tests/unit_tests/ban.cpp:124:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   ASSERT_TRUE(server.get_blocked_ips().size() == 0);
                      ^
/root/monero/tests/unit_tests/ban.cpp:129:23: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'unblock_ip'; did you mean 'unblock_host'?
   ASSERT_FALSE(server.unblock_ip(MAKE_IP(1,2,3,4)));
                       ^
/root/monero/tests/unit_tests/ban.cpp:130:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   ASSERT_TRUE(server.get_blocked_ips().size() == 0);
                      ^
/root/monero/tests/unit_tests/ban.cpp:135:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'block_ip'; did you mean 'block_host'?
   ASSERT_TRUE(server.block_ip(MAKE_IP(1,2,3,4), 1));
                      ^
/root/monero/tests/unit_tests/ban.cpp:136:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'block_ip'; did you mean 'block_host'?
   ASSERT_TRUE(server.block_ip(MAKE_IP(1,2,3,5), 3));
                      ^
/root/monero/tests/unit_tests/ban.cpp:137:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   ASSERT_TRUE(server.get_blocked_ips().size() == 2);
                      ^
/root/monero/tests/unit_tests/ban.cpp:140:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'unblock_ip'; did you mean 'unblock_host'?
   ASSERT_TRUE(server.unblock_ip(MAKE_IP(1,2,3,4)));
                      ^
/root/monero/tests/unit_tests/ban.cpp:141:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'unblock_ip'; did you mean 'unblock_host'?
   ASSERT_TRUE(server.unblock_ip(MAKE_IP(1,2,3,5)));
                      ^
/root/monero/tests/unit_tests/ban.cpp:160:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'block_ip'; did you mean 'block_host'?
   ASSERT_TRUE(server.block_ip(MAKE_IP(1,2,3,4), 2));
                      ^
/root/monero/tests/unit_tests/ban.cpp:161:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   ASSERT_TRUE(server.get_blocked_ips().size() == 1);
                      ^
/root/monero/tests/unit_tests/ban.cpp:165:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'block_ip'; did you mean 'block_host'?
   ASSERT_TRUE(server.block_ip(MAKE_IP(1,2,3,4), 9));
                      ^
/root/monero/tests/unit_tests/ban.cpp:166:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   ASSERT_TRUE(server.get_blocked_ips().size() == 1);
                      ^
/root/monero/tests/unit_tests/ban.cpp:170:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'block_ip'; did you mean 'block_host'?
   ASSERT_TRUE(server.block_ip(MAKE_IP(1,2,3,4), 5));
                      ^
/root/monero/tests/unit_tests/ban.cpp:171:22: error: 'Server {aka class nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<test_core> >}' has no member named 'get_blocked_ips'; did you mean 'get_blocked_hosts'?
   ASSERT_TRUE(server.get_blocked_ips().size() == 1);
                      ^
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:86: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/ban.cpp.o' failed
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/ban.cpp.o] Error 1
make[3]: Leaving directory '/root/monero/build/release'
CMakeFiles/Makefile2:2605: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/root/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero/build/release'
Makefile:58: recipe for target 'release-all' failed
make: *** [release-all] Error 2

## moneromooo-monero | 2017-06-23T11:55:17+00:00
These are fixed in 2089 and 2095.

## hyc | 2017-06-23T11:57:56+00:00
First part - Debian has upgraded to OpenSSL 1.1, addressed in PR #2089 . As for unit tests, that's addressed in PR #2095 . You should close this issue since these are all already known and patches are available.

## golangdude | 2017-06-23T15:03:12+00:00
Closing per comments.

# Action History
- Created by: golangdude | 2017-06-23T07:27:09+00:00
- Closed at: 2017-06-23T15:03:12+00:00
