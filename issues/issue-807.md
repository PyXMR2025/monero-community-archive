---
title: Compile fail, ubuntu 14.04
source_url: https://github.com/monero-project/monero/issues/807
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-04-16T14:04:25+00:00'
updated_at: '2016-05-10T12:30:56+00:00'
type: issue
status: closed
closed_at: '2016-05-10T12:30:56+00:00'
---

# Original Description
[ 78%] Building CXX object tests/functional_tests/CMakeFiles/functional_tests.dir/transactions_flow_test.cpp.o
/home/bob/bitmonero/tests/functional_tests/transactions_flow_test.cpp: In function ‘bool do_send_money(tools::wallet2&, tools::wallet2&, size_t, uint64_t, cryptonote::transaction&, size_t)’:
/home/bob/bitmonero/tests/functional_tests/transactions_flow_test.cpp:88:168: error: no matching function for call to ‘tools::wallet2::transfer(std::vectorcryptonote::tx_destination_entry&, size_t&, int, const uint64_t&, std::vector<unsigned char>, void (&)(const std::vectorcryptonote::tx_destination_entry&, const cryptonote::tx_destination_entry&, uint64_t, std::vectorcryptonote::tx_destination_entry&, std::vectorcryptonote::tx_destination_entry&), tools::tx_dust_policy, cryptonote::transaction&, tools::wallet2::pending_tx&, bool)’
     w1.transfer(dsts, mix_in_factor, 0, TEST_FEE, std::vector<uint8_t>(), tools::detail::null_split_strategy, tools::tx_dust_policy(TEST_DUST_THRESHOLD), tx, ptx, true);
                                                                                                                                                                        ^
/home/bob/bitmonero/tests/functional_tests/transactions_flow_test.cpp:88:168: note: candidates are:
In file included from /home/bob/bitmonero/tests/functional_tests/transactions_flow_test.cpp:37:0:
/home/bob/bitmonero/src/wallet/wallet2.h:277:10: note: template<class T> void tools::wallet2::transfer(const std::vectorcryptonote::tx_destination_entry&, size_t, const std::vector<long unsigned int>&, uint64_t, uint64_t, const std::vector<unsigned char>&, T, const tools::tx_dust_policy&, bool)
     void transfer(const std::vectorcryptonote::tx_destination_entry& dsts, const size_t fake_outputs_count, const std::vector<size_t> &unused_transfers_indices, uint64_t unlock_time, uint64_t fee, const std::vector<uint8_t>& extra, T destination_split_strategy, const tx_dust_policy& dust_policy, bool trusted_daemon);
          ^
/home/bob/bitmonero/src/wallet/wallet2.h:277:10: note:   template argument deduction/substitution failed:
/home/bob/bitmonero/tests/functional_tests/transactions_flow_test.cpp:88:168: note:   cannot convert ‘0’ (type ‘int’) to type ‘const std::vector<long unsigned int>&’
     w1.transfer(dsts, mix_in_factor, 0, TEST_FEE, std::vector<uint8_t>(), tools::detail::null_split_strategy, tools::tx_dust_policy(TEST_DUST_THRESHOLD), tx, ptx, true);
                                                                                                                                                                        ^
In file included from /home/bob/bitmonero/tests/functional_tests/transactions_flow_test.cpp:37:0:
/home/bob/bitmonero/src/wallet/wallet2.h:279:10: note: template<class T> void tools::wallet2::transfer(const std::vectorcryptonote::tx_destination_entry&, size_t, const std::vector<long unsigned int>&, uint64_t, uint64_t, const std::vector<unsigned char>&, T, const tools::tx_dust_policy&, cryptonote::transaction&, tools::wallet2::pending_tx&, bool)
     void transfer(const std::vectorcryptonote::tx_destination_entry& dsts, const size_t fake_outputs_count, const std::vector<size_t> &unused_transfers_indices, uint64_t unlock_time, uint64_t fee, const std::vector<uint8_t>& extra, T destination_split_strategy, const tx_dust_policy& dust_policy, cryptonote::transaction& tx, pending_tx& ptx, bool trusted_daemon);
          ^
/home/bob/bitmonero/src/wallet/wallet2.h:279:10: note:   template argument deduction/substitution failed:
/home/bob/bitmonero/tests/functional_tests/transactions_flow_test.cpp:88:168: note:   cannot convert ‘0’ (type ‘int’) to type ‘const std::vector<long unsigned int>&’
     w1.transfer(dsts, mix_in_factor, 0, TEST_FEE, std::vector<uint8_t>(), tools::detail::null_split_strategy, tools::tx_dust_policy(TEST_DUST_THRESHOLD), tx, ptx, true);
                                                                                                                                                                        ^
In file included from /home/bob/bitmonero/tests/functional_tests/transactions_flow_test.cpp:37:0:
/home/bob/bitmonero/src/wallet/wallet2.h:280:10: note: void tools::wallet2::transfer(const std::vectorcryptonote::tx_destination_entry&, size_t, const std::vector<long unsigned int>&, uint64_t, uint64_t, const std::vector<unsigned char>&, bool)
     void transfer(const std::vectorcryptonote::tx_destination_entry& dsts, const size_t fake_outputs_count, const std::vector<size_t> &unused_transfers_indices, uint64_t unlock_time, uint64_t fee, const std::vector<uint8_t>& extra, bool trusted_daemon);
          ^
/home/bob/bitmonero/src/wallet/wallet2.h:280:10: note:   candidate expects 7 arguments, 10 provided
/home/bob/bitmonero/src/wallet/wallet2.h:281:10: note: void tools::wallet2::transfer(const std::vectorcryptonote::tx_destination_entry&, size_t, const std::vector<long unsigned int>&, uint64_t, uint64_t, const std::vector<unsigned char>&, cryptonote::transaction&, tools::wallet2::pending_tx&, bool)
     void transfer(const std::vectorcryptonote::tx_destination_entry& dsts, const size_t fake_outputs_count, const std::vector<size_t> &unused_transfers_indices, uint64_t unlock_time, uint64_t fee, const std::vector<uint8_t>& extra, cryptonote::transaction& tx, pending_tx& ptx, bool trusted_daemon);
          ^
/home/bob/bitmonero/src/wallet/wallet2.h:281:10: note:   candidate expects 9 arguments, 10 provided
make[3]: **\* [tests/functional_tests/CMakeFiles/functional_tests.dir/transactions_flow_test.cpp.o] Error 1
make[3]: Leaving directory `/home/bob/bitmonero/build/release'
make[2]: *** [tests/functional_tests/CMakeFiles/functional_tests.dir/all] Error 2
make[2]: Leaving directory`/home/bob/bitmonero/build/release'
make[1]: **\* [all] Error 2
make[1]: Leaving directory `/home/bob/bitmonero/build/release'
make: **\* [release-all] Error 2


# Discussion History
## Gingeropolous | 2016-04-16T14:08:38+00:00
1c66fe04bcebf50102abe6c96322f0fa5ce740ec


## hyc | 2016-04-16T14:26:51+00:00
Looks like it was broken by 48d0747d005c80fde3837fc4bcdb3eff26907d74


## fluffypony | 2016-05-10T12:30:56+00:00
Fixed


# Action History
- Created by: Gingeropolous | 2016-04-16T14:04:25+00:00
- Closed at: 2016-05-10T12:30:56+00:00
