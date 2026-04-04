---
title: '[Testnet] Error: internal error: Multisig wallets cannot spend non rct outputs'
source_url: https://github.com/monero-project/monero/issues/4774
author: lacksfish
assignees: []
labels: []
created_at: '2018-11-01T13:31:12+00:00'
updated_at: '2018-11-05T01:47:43+00:00'
type: issue
status: closed
closed_at: '2018-11-01T15:57:43+00:00'
---

# Original Description
Setting up a local monero testnet following closely [this guide](https://github.com/moneroexamples/private-testnet), I've set up wallet 2 and 3 to be a multisig wallet following [stackoverflow instructions](https://monero.stackexchange.com/a/5647).

After mining a couple thousand blocks, I've sent 500 testnet coins (from wallet 1) to the multisig wallet (wallet 2 and 3). I've sent those coins with a ringsize of 1 (if that matters, how can I set the minimum ringsize in testnet?)

The coins arrived in the multisig wallet, but can now not be spent giving the error:

> Error: internal error: Multisig wallets cannot spend non rct outputs

Any help very appreciated. Also, is there a block set at which bulletproofs and all the hardforks activate on testnet? I might've simply missed it...

# Discussion History
## lacksfish | 2018-11-01T13:38:05+00:00
```
2018-11-01 13:36:05.955	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v8 rules
2018-11-01 13:36:06.043	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v7 rules
2018-11-01 13:36:06.131	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v6 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v2 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v8 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v5 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v2 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v8 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v8 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v4 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v8 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v4 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v8 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v5 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v3 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:9085	Not using v8 rules
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8326	transfer: adding 50.000000000000, for a total of 50.000000000000
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8360	Candidate subaddress index for spending: 0
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8427	Starting with 1 non-dust outputs and 0 dust outputs
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8452	checking preferred
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8488	done checking preferred
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8502	Start of loop with 1 0, tx.dsts.size() 0
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8503	unused_transfers_indices: 0
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8504	unused_dust_indices: 
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8505	dsts size 1, first 50.000000000000
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8506	adding_fee 0, use_rct 0
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8548	Picking output 0, amount 500.000000000000, ki <ff0d0d1264fd8e96c9c0d7fbb82d3e7755e84a943948a6d03b5c730b75e7f1e0>
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8569	We can fully pay BgKp5cURVi838MqjqwUunPC66uSnFNYQc2h8uFip6xmYE5L15nXCTtBezfLhud3oZj6ntUA2hJrzbGqe5nUtQULP82NdcYF for 50.000000000000
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8589	Considering whether to create a tx now, 1 inputs, tx limit 19400
2018-11-01 13:36:06.219	    7f29e26ba780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8624	Trying to create a tx now, with 1 outputs and 1 inputs
2018-11-01 13:36:06.219	    7f29e26ba780	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:7249	m_multisig. THROW EXCEPTION: error::wallet_internal_error
2018-11-01 13:36:06.219	    7f29e26ba780	WARN 	net.http	src/wallet/wallet_errors.h:814	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:7249:N5tools5error21wallet_internal_errorE: Multisig wallets cannot spend non rct outputs
2018-11-01 13:36:06.219	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:133	Exception: tools::error::wallet_internal_error
2018-11-01 13:36:06.219	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [1] ./monero-v0.13.0.4/monero-wallet-cli:__wrap___cxa_throw+0x10a [0x5623313075ea]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monero-v0.13.0.4/monero-wallet-cli:void tools::error::throw_wallet_ex<tools::error::wallet_internal_error, char [46]>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, char const (&) [46])+0x18e [0x56233120810e]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monero-v0.13.0.4/monero-wallet-cli:void tools::wallet2::transfer_selected<void (*)(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> > const&, cryptonote::tx_destination_entry const&, unsigned long, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >&, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >&)>(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> > const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long, std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, unsigned long, unsigned long, std::vector<unsigned char, std::allocator<unsigned char> > const&, void (*)(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> > const&, cryptonote::tx_destination_entry const&, unsigned long, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >&, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >&), tools::tx_dust_policy const&, cryptonote::transaction&, tools::wallet2::pending_tx&)+0x574 [0x562331275044]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monero-v0.13.0.4/monero-wallet-cli:tools::wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::allocator<unsigned char> > const&, unsigned int, std::set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int> >)+0x4bb4 [0x56233118d244]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monero-v0.13.0.4/monero-wallet-cli:cryptonote::simple_wallet::transfer_main(int, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)+0x182b [0x562331080e3b]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monero-v0.13.0.4/monero-wallet-cli:epee::command_handler::process_command_str(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x381 [0x5623310ce861]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monero-v0.13.0.4/monero-wallet-cli:bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1} const&, std::function<void ()>)+0x790 [0x5623310a3f90]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monero-v0.13.0.4/monero-wallet-cli:cryptonote::simple_wallet::run()+0x3bf [0x56233106fdbf]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monero-v0.13.0.4/monero-wallet-cli:main+0x6c3 [0x56233102e163]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [10] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf0 [0x7f29e1a15830]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monero-v0.13.0.4/monero-wallet-cli:_start+0x29 [0x562331038f39]
2018-11-01 13:36:06.223	    7f29e26ba780	INFO 	stacktrace	src/common/stack_trace.cpp:172	
2018-11-01 13:36:06.223	    7f29e26ba780	ERROR	wallet.simplewallet	src/simplewallet/simplewallet.cpp:483	internal error: /DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:7249:N5tools5error21wallet_internal_errorE: Multisig wallets cannot spend non rct outputs
2018-11-01 13:36:06.223	    7f29e26ba780	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: internal error: Multisig wallets cannot spend non rct outputs
```

## moneromooo-monero | 2018-11-01T14:03:46+00:00
This is expected. Not implemented. There's going to be very very few new non rct outs today, if any.
I think (not sure) stoffu might have implemented it for aeon, in which case it could be used.

## lacksfish | 2018-11-01T14:15:07+00:00
How can I switch my current testnet to v9 with bulletproofs then?

## moneromooo-monero | 2018-11-01T14:41:08+00:00
Sync it. Seed nodes might be down atm, but when they aren't :)

## lacksfish | 2018-11-01T15:31:12+00:00
I'm not connected to the global testnet, I'm running a local testnet with maybe 50,000 blocks so far.

## moneromooo-monero | 2018-11-01T15:53:15+00:00
Then either mine a lot, or change the fork heights near the top of blockchain.cpp


## lacksfish | 2018-11-01T15:57:43+00:00
Thanks!

## stoffu | 2018-11-05T01:47:43+00:00
FWIW I have implemented multisig for spending pre-RingCT outputs https://github.com/stoffu/monero/commit/559bc3bd932849b42381d3382ce420647a907c41, which wasn't reviewed and didn't go into production.

# Action History
- Created by: lacksfish | 2018-11-01T13:31:12+00:00
- Closed at: 2018-11-01T15:57:43+00:00
