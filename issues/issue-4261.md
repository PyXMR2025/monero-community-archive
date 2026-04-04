---
title: transfer got error "tx_not_constructed"
source_url: https://github.com/monero-project/monero/issues/4261
author: olizax
assignees: []
labels: []
created_at: '2018-08-15T04:23:53+00:00'
updated_at: '2018-10-25T11:51:45+00:00'
type: issue
status: closed
closed_at: '2018-09-16T14:24:47+00:00'
---

# Original Description
LOG:

> 2018-08-15 04:17:50.758	[RPC0]	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:204	key image helper: failed to generate_key_derivation(<xxxx>, <xxxxx>)
2018-08-15 04:17:50.758	[RPC0]	ERROR	default	src/cryptonote_core/cryptonote_tx_utils.cpp:290	Key image generation failed!
2018-08-15 04:17:50.758	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:6651	!r. THROW EXCEPTION: error::tx_not_constructed
2018-08-15 04:17:50.758	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:6651:N5tools5error18tx_not_constructedE: transaction was not constructed


Appeared in recent days, any help?

# Discussion History
## moneromooo-monero | 2018-08-15T07:04:36+00:00
What version are you running ?

## olizax | 2018-08-15T07:09:52+00:00
@moneromooo-monero 
Monero 'Lithium Luna' (v0.12.3.0-release)


transfer though monero-wallet-cli got the following error logs:
2018-08-15 07:13:15.188	    7f5cd0ca1740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=11.999000000000, real_output=2, real_output_in_tx_index=0, indexes: 4214261 5698949 5769128 5931324 6504731 6840052 6843148
2018-08-15 07:13:22.061	    7f5cd0ca1740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=11.999000000000, real_output=2, real_output_in_tx_index=0, indexes: 3140696 4764995 5769128 6664109 6853190 6854419 6857269
2018-08-15 07:13:22.061	    7f5cd0ca1740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=0.010000000000, real_output=3, real_output_in_tx_index=0, indexes: 2039859 4242831 5843172 6757719 6848903 6852607 6856196
2018-08-15 07:13:22.062	    7f5cd0ca1740	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:204	key image helper: failed to generate_key_derivation(<b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000>, <ae9c100b9880f405d0b830b24b5ead39c21941dd923d707f9069b2f954752a0f>)
2018-08-15 07:13:22.062	    7f5cd0ca1740	ERROR	default	src/cryptonote_core/cryptonote_tx_utils.cpp:290	Key image generation failed!
2018-08-15 07:13:22.062	    7f5cd0ca1740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:6651	!r. THROW EXCEPTION: error::tx_not_constructed
2018-08-15 07:13:22.062	    7f5cd0ca1740	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:6651:N5tools5error18tx_not_constructedE: transaction was not constructed
Sources:
  source 0:
    amount: 11.999000000000
  source 1:
    amount: 0.010000000000
Destinations:
  0: 439kEEtN7y3Cyg6Th17PMkCY3YzCRZxjzefx8LBv86HiPSKsNq2EmqDP27J2Q6is1TCqPxPmpnp5rV5LkwsVQaXwQFWVXuZ 1.000000000000
unlock_time: 0
2018-08-15 06:58:08.934	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: tools::error::tx_not_constructed
2018-08-15 06:58:08.934	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] ./monero-wallet-cli:__wrap___cxa_throw+0x10a [0x5580c87bdc0a]
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] ./monero-wallet-cli:void tools::error::throw_wallet_ex<tools::error::tx_not_constructed, std::vector<cryptonote::tx_source_entry, std::allocator<cryptonote::tx_source_entry> >, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, cryptonote::network_type>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, std::vector<cryptonote::tx_source_entry, std::allocator<cryptonote::tx_source_entry> > const&, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> > const&, unsigned long const&, cryptonote::network_type const&)+0x299 [0x5580c86f2fb9]
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] ./monero-wallet-cli:tools::wallet2::transfer_selected_rct(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long, std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, unsigned long, unsigned long, std::vector<unsigned char, std::allocator<unsigned char> > const&, cryptonote::transaction&, tools::wallet2::pending_tx&, bool)+0x2987 [0x5580c8674ad7]
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] ./monero-wallet-cli:tools::wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::allocator<unsigned char> > const&, unsigned int, std::set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int> >, bool)+0x3a60 [0x5580c867bca0]
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] ./monero-wallet-cli:cryptonote::simple_wallet::transfer_main(int, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)+0x1a9d [0x5580c855699d]
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] ./monero-wallet-cli:epee::command_handler::process_command_str(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x2a5 [0x5580c85add35]
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] ./monero-wallet-cli:bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1} const&, std::function<void ()>)+0x886 [0x5580c8586366]
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] ./monero-wallet-cli:cryptonote::simple_wallet::run()+0x35a [0x5580c853ec2a]
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] ./monero-wallet-cli:main+0x685 [0x5580c8508225]
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf0 [0x7f5ccffb9830]
2018-08-15 06:58:08.937	    7f5cd0ca1740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] ./monero-wallet-cli:_start+0x29 [0x5580c8514d09]

## moneromooo-monero | 2018-08-15T07:17:15+00:00
Is your standard address as expected ("address" command) ?

## olizax | 2018-08-15T07:25:36+00:00
yes, only one primary address

wallet 45mVud]: address
0 45mVudxxxxxxxxxxxxxxxx  Primary address (used)

## moneromooo-monero | 2018-08-15T07:29:35+00:00
That address is generated from (partly) the view secret key, and the error you get seems to imply the view secret key is not a valid point. This particular address worked before, right ? As in, you could receive and send ?

## olizax | 2018-08-15T07:36:34+00:00
Yes, Receiving is ok and last successful send is on 12/08/2018.

## moneromooo-monero | 2018-08-15T07:38:00+00:00
Was this with the same monero version ?

## olizax | 2018-08-15T07:38:20+00:00
Yes.

## moneromooo-monero | 2018-08-15T08:06:32+00:00
Is this a cold wallet setup, or normal ?

## olizax | 2018-08-15T08:12:42+00:00
Normal.
The wallet and node running on the same server.

## moneromooo-monero | 2018-08-15T08:29:34+00:00
Try this:
http://paste.debian.net/hidden/f9feb228/
Then look at the new logs (log level 0 is fine). Check the secret key it logs is hte same as your secret key. Then paste the other logs which don;t have the secret key.

## moneromooo-monero | 2018-08-15T08:31:05+00:00
Actually, post all the new logs, after checking the secret view key is correct, and after masking it.

## olizax | 2018-08-15T08:47:39+00:00
Ok, let me try... It may need some time.

## olizax | 2018-08-15T13:39:17+00:00
@moneromooo-monero 
I builded successfully. 
Is it safe to post the log here, as it contains some `keys`...

## moneromooo-monero | 2018-08-15T13:40:36+00:00
Once you checked your secret view key is the one you expect, replace it with VIEWKEYHERE, then post.
I just need the new logs, they'll have the "INFO" level.

## olizax | 2018-08-15T13:51:44+00:00
> 
2018-08-15 13:21:52.460	    7fab8ea3d740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=11.999000000000, real_output=0, real_output_in_tx_index=0, indexes: 5769128 6039971 6379692 6402975 6471598 6853785 6855350
2018-08-15 13:21:52.460	    7fab8ea3d740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key <REAL_OUT_TX_KEY1>
2018-08-15 13:21:52.461	    7fab8ea3d740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 1, tx_public_key <TX_PUBLIC_KEY1>, skey <SKEY>
2018-08-15 13:21:57.041	    7fab8ea3d740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=11.999000000000, real_output=2, real_output_in_tx_index=0, indexes: 2584311 5678069 5769128 6682126 6809616 6854488 6860296
2018-08-15 13:21:57.041	    7fab8ea3d740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=0.010000000000, real_output=2, real_output_in_tx_index=0, indexes: 6267051 6413360 6757719 6775954 6854959 6859732 6860931
2018-08-15 13:21:57.041	    7fab8ea3d740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key <TX_PUBLIC_KEY1>
2018-08-15 13:21:57.041	    7fab8ea3d740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 1, tx_public_key <TX_PUBLIC_KEY1>, skey <SKEY>
2018-08-15 13:21:57.042	    7fab8ea3d740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key <REAL_OUT_TX_KEY2>
2018-08-15 13:21:57.042	    7fab8ea3d740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 0, tx_public_key <TX_PUBLIC_KEY2>, skey <SKEY>
2018-08-15 13:21:57.042	    7fab8ea3d740	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:205	key image helper: failed to generate_key_derivation(<TX_PUBLIC_KEY2>, <SKEY>)
2018-08-15 13:21:57.042	    7fab8ea3d740	ERROR	default	src/cryptonote_core/cryptonote_tx_utils.cpp:291	Key image generation failed!
2018-08-15 13:21:57.042	    7fab8ea3d740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:6652	!r. THROW EXCEPTION: error::tx_not_constructed
2018-08-15 13:21:57.042	    7fab8ea3d740	WARN 	net.http	src/wallet/wallet_errors.h:794	/data/downloads/monero/monero/src/wallet/wallet2.cpp:6652:N5tools5error18tx_not_constructedE: transaction was not constructed
Sources:
  source 0:
    amount: 11.999000000000
  source 1:
    amount: 0.010000000000
Destinations:
  0: OUT_ADDRESS 1.000000000000
unlock_time: 0
2018-08-15 13:21:57.042	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: tools::error::tx_not_constructed
2018-08-15 13:21:57.042	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] ./bin/monero-wallet-cli:__wrap___cxa_throw+0x10a [0x55cdbcee5faa]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] ./bin/monero-wallet-cli:void tools::error::throw_wallet_ex<tools::error::tx_not_constructed, std::vector<cryptonote::tx_source_entry, std::allocator<cryptonote::tx_source_entry> >, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, cryptonote::network_type>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, std::vector<cryptonote::tx_source_entry, std::allocator<cryptonote::tx_source_entry> > const&, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> > const&, unsigned long const&, cryptonote::network_type const&)+0x299 [0x55cdbce1a7f9]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] ./bin/monero-wallet-cli:tools::wallet2::transfer_selected_rct(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long, std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, unsigned long, unsigned long, std::vector<unsigned char, std::allocator<unsigned char> > const&, cryptonote::transaction&, tools::wallet2::pending_tx&, bool)+0x2978 [0x55cdbcdaafd8]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] ./bin/monero-wallet-cli:tools::wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::allocator<unsigned char> > const&, unsigned int, std::set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int> >, bool)+0x3a60 [0x55cdbcdb21a0]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] ./bin/monero-wallet-cli:cryptonote::simple_wallet::transfer_main(int, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)+0x1c0f [0x55cdbcc83a1f]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] ./bin/monero-wallet-cli:epee::command_handler::process_command_str(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x2a5 [0x55cdbccdbd35]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] ./bin/monero-wallet-cli:bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1} const&, std::function<void ()>)+0x796 [0x55cdbccb2d46]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] ./bin/monero-wallet-cli:cryptonote::simple_wallet::run()+0x3ea [0x55cdbcc6e0ca]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] ./bin/monero-wallet-cli:main+0x681 [0x55cdbcc34e71]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf0 [0x7fab8db4a830]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] ./bin/monero-wallet-cli:_start+0x29 [0x55cdbcc41b99]
2018-08-15 13:21:57.046	    7fab8ea3d740	INFO 	stacktrace	src/common/stack_trace.cpp:163
2018-08-15 13:21:57.046	    7fab8ea3d740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: transaction was not constructed

SKEY is the same with my secret  view key. 



## moneromooo-monero | 2018-08-15T15:27:30+00:00
You also masked the public keys :)

## olizax | 2018-08-16T02:14:19+00:00
Sorry...


> 2018-08-15 13:21:52.460	    7fab8ea3d740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=11.999000000000, real_output=0, real_output_in_tx_index=0, indexes: 5769128 6039971 6379692 6402975 6471598 6853785 6855350
2018-08-15 13:21:52.460	    7fab8ea3d740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key <0cdda48136c9fa787cd01a1e58c0c6e8b2dc20f52327c76f064be0f1daa522d8>
2018-08-15 13:21:52.461	    7fab8ea3d740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 1, tx_public_key <0cdda48136c9fa787cd01a1e58c0c6e8b2dc20f52327c76f064be0f1daa522d8>, skey <SKEY>
2018-08-15 13:21:57.041	    7fab8ea3d740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=11.999000000000, real_output=2, real_output_in_tx_index=0, indexes: 2584311 5678069 5769128 6682126 6809616 6854488 6860296
2018-08-15 13:21:57.041	    7fab8ea3d740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=0.010000000000, real_output=2, real_output_in_tx_index=0, indexes: 6267051 6413360 6757719 6775954 6854959 6859732 6860931
2018-08-15 13:21:57.041	    7fab8ea3d740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key <0cdda48136c9fa787cd01a1e58c0c6e8b2dc20f52327c76f064be0f1daa522d8>
2018-08-15 13:21:57.041	    7fab8ea3d740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 1, tx_public_key <0cdda48136c9fa787cd01a1e58c0c6e8b2dc20f52327c76f064be0f1daa522d8>, skey <SKEY>
2018-08-15 13:21:57.042	    7fab8ea3d740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key <b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000>
2018-08-15 13:21:57.042	    7fab8ea3d740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 0, tx_public_key <b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000>, skey <SKEY>
2018-08-15 13:21:57.042	    7fab8ea3d740	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:205	key image helper: failed to generate_key_derivation(<b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000>, <SKEY>)
2018-08-15 13:21:57.042	    7fab8ea3d740	ERROR	default	src/cryptonote_core/cryptonote_tx_utils.cpp:291	Key image generation failed!
2018-08-15 13:21:57.042	    7fab8ea3d740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:6652	!r. THROW EXCEPTION: error::tx_not_constructed


## moneromooo-monero | 2018-08-16T17:22:23+00:00
It's missing some logs, before what you pasted, with txids.

## moneromooo-monero | 2018-08-16T17:24:17+00:00
Also some of the logs are missing some information. Did you cut off some non-secret-key bits again or are they really like this ?

## olizax | 2018-08-20T03:01:50+00:00
@moneromooo-monero no, there are no txids, thats all the logs.

## moneromooo-monero | 2018-08-20T10:31:40+00:00
My fault, the log was only in the non-rct branch of the code. Here: http://paste.debian.net/hidden/5350725b/. Interestingly, I also see the missing fields now, it seems they were inisible due to being surrounded with <> brackets. Anyway, please try that new patch and paste the logs again.

## olizax | 2018-08-20T14:02:59+00:00
> 2018-08-20 13:58:00.080	    7f1203df2740	INFO 	global	src/wallet/wallet2.cpp:6614	creating tx with source entry from txid <5e0faa9dc821cb558f0e10fbf0e810a95633366980508e991f644099c68b1b20>, key image <3c9e2af33de1321888bd306c9dc3373e1192f8f1388e0bce9189ac3b1554d137> , flags 1/0, pubkey <1a6788acebdc87a4f470bd0e7b11e3326572c1c238584bbd7b1252a736518d04>
2018-08-20 13:58:00.081	    7f1203df2740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=0.260000000000, real_output=1, real_output_in_tx_index=0, indexes: 5111337 5736262 6281147 6536948 6818651 6907119 6915737
2018-08-20 13:58:00.081	    7f1203df2740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key <4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11>
2018-08-20 13:58:00.081	    7f1203df2740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 1, tx_public_key <4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11>, skey <PRIVATE_KEY>
2018-08-20 13:58:10.937	    7f1203df2740	INFO 	global	src/wallet/wallet2.cpp:6614	creating tx with source entry from txid <5e0faa9dc821cb558f0e10fbf0e810a95633366980508e991f644099c68b1b20>, key image <3c9e2af33de1321888bd306c9dc3373e1192f8f1388e0bce9189ac3b1554d137> , flags 1/0, pubkey <1a6788acebdc87a4f470bd0e7b11e3326572c1c238584bbd7b1252a736518d04>
2018-08-20 13:58:10.937	    7f1203df2740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=0.260000000000, real_output=1, real_output_in_tx_index=0, indexes: 3758082 5736262 5807235 6598426 6904910 6913328 6914476
2018-08-20 13:58:10.937	    7f1203df2740	INFO 	global	src/wallet/wallet2.cpp:6614	creating tx with source entry from txid <e5f0c0b1c482e036b8aa2a8cce3e6956a0a9959c0ee1304e28fbd40ca221efca>, key image <e00bdaba684428291b16d330bc6cb8d788ebf323aa8a3c16a56003a5eb22ff85> , flags 1/0, pubkey <abf8d23e2cae39626bc31cf46bf3cd036556febd7dc2d53d4ec4282b65fe97a4>
2018-08-20 13:58:10.937	    7f1203df2740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=0.010000000000, real_output=2, real_output_in_tx_index=0, indexes: 5775823 6612437 6757719 6837338 6908970 6912779 6915724
2018-08-20 13:58:10.938	    7f1203df2740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key <4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11>
2018-08-20 13:58:10.938	    7f1203df2740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 1, tx_public_key <4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11>, skey <PRIVATE_KEY>
2018-08-20 13:58:10.938	    7f1203df2740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key <b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000>
2018-08-20 13:58:10.938	    7f1203df2740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 0, tx_public_key <b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000>, skey <PRIVATE_KEY>
2018-08-20 13:58:10.938	    7f1203df2740	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:205	key image helper: failed to generate_key_derivation(<b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000>, <PRIVATE_KEY>)
2018-08-20 13:58:10.938	    7f1203df2740	ERROR	default	src/cryptonote_core/cryptonote_tx_utils.cpp:291	Key image generation failed!
2018-08-20 13:58:10.938	    7f1203df2740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:6653	!r. THROW EXCEPTION: error::tx_not_constructed
2018-08-20 13:58:10.938	    7f1203df2740	WARN 	net.http	src/wallet/wallet_errors.h:794	/data/downloads/monero/monero/src/wallet/wallet2.cpp:6653:N5tools5error18tx_not_constructedE: transaction was not constructed
Sources:
  source 0:
    amount: 0.260000000000
  source 1:
    amount: 0.010000000000
Destinations:
  0: 46SJi3tGk5MZqVLm9zvim6hVxo6fK3DgcY7tJ5vTbuNzMrzG6GhKCfT8KVr856bhh3DRVee23EbNZV1AgUXmT18gKyqnUjq 0.010000000000
unlock_time: 0
2018-08-20 13:58:10.938	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: tools::error::tx_not_constructed
2018-08-20 13:58:10.939	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] ./monero-wallet-cli:__wrap___cxa_throw+0x10a [0x557010529daa]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] ./monero-wallet-cli:void tools::error::throw_wallet_ex<tools::error::tx_not_constructed, std::vector<cryptonote::tx_source_entry, std::allocator<cryptonote::tx_source_entry> >, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, cryptonote::network_type>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, std::vector<cryptonote::tx_source_entry, std::allocator<cryptonote::tx_source_entry> > const&, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> > const&, unsigned long const&, cryptonote::network_type const&)+0x299 [0x55701045e599]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] ./monero-wallet-cli:tools::wallet2::transfer_selected_rct(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long, std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, unsigned long, unsigned long, std::vector<unsigned char, std::allocator<unsigned char> > const&, cryptonote::transaction&, tools::wallet2::pending_tx&, bool)+0x2bba [0x5570103eedaa]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] ./monero-wallet-cli:tools::wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::allocator<unsigned char> > const&, unsigned int, std::set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int> >, bool)+0x3a60 [0x5570103f5f90]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] ./monero-wallet-cli:cryptonote::simple_wallet::transfer_main(int, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)+0x1c0f [0x5570102c6e6f]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] ./monero-wallet-cli:epee::command_handler::process_command_str(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x2a5 [0x55701031fa25]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] ./monero-wallet-cli:bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1} const&, std::function<void ()>)+0x796 [0x5570102f6a66]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] ./monero-wallet-cli:cryptonote::simple_wallet::run()+0x3ea [0x5570102b152a]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] ./monero-wallet-cli:main+0x681 [0x557010278371]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf0 [0x7f1202eff830]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] ./monero-wallet-cli:_start+0x29 [0x557010284f69]
2018-08-20 13:58:10.942	    7f1203df2740	INFO 	stacktrace	src/common/stack_trace.cpp:163
2018-08-20 13:58:10.943	    7f1203df2740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: transaction was not constructed

## moneromooo-monero | 2018-08-20T14:29:20+00:00
The line starting with "2018-08-20 13:58:10.938 7f1203df2740" is missing the value of real_out_tx_key. Can you check in your log ? I suspect it's github masking these.

## olizax | 2018-08-21T02:49:26+00:00
oh, i see. let me delete the brackets.

> 2018-08-20 13:58:00.080	    7f1203df2740	INFO 	global	src/wallet/wallet2.cpp:6614	creating tx with source entry from txid 5e0faa9dc821cb558f0e10fbf0e810a95633366980508e991f644099c68b1b20, key image 3c9e2af33de1321888bd306c9dc3373e1192f8f1388e0bce9189ac3b1554d137 , flags 1/0, pubkey 1a6788acebdc87a4f470bd0e7b11e3326572c1c238584bbd7b1252a736518d04
2018-08-20 13:58:00.081	    7f1203df2740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=0.260000000000, real_output=1, real_output_in_tx_index=0, indexes: 5111337 5736262 6281147 6536948 6818651 6907119 6915737
2018-08-20 13:58:00.081	    7f1203df2740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key 4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11
2018-08-20 13:58:00.081	    7f1203df2740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 1, tx_public_key 4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11, skey <PRIVATE_KEY>
2018-08-20 13:58:10.937	    7f1203df2740	INFO 	global	src/wallet/wallet2.cpp:6614	creating tx with source entry from txid 5e0faa9dc821cb558f0e10fbf0e810a95633366980508e991f644099c68b1b20, key image 3c9e2af33de1321888bd306c9dc3373e1192f8f1388e0bce9189ac3b1554d137 , flags 1/0, pubkey 1a6788acebdc87a4f470bd0e7b11e3326572c1c238584bbd7b1252a736518d04
2018-08-20 13:58:10.937	    7f1203df2740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=0.260000000000, real_output=1, real_output_in_tx_index=0, indexes: 3758082 5736262 5807235 6598426 6904910 6913328 6914476
2018-08-20 13:58:10.937	    7f1203df2740	INFO 	global	src/wallet/wallet2.cpp:6614	creating tx with source entry from txid e5f0c0b1c482e036b8aa2a8cce3e6956a0a9959c0ee1304e28fbd40ca221efca, key image e00bdaba684428291b16d330bc6cb8d788ebf323aa8a3c16a56003a5eb22ff85 , flags 1/0, pubkey abf8d23e2cae39626bc31cf46bf3cd036556febd7dc2d53d4ec4282b65fe97a4
2018-08-20 13:58:10.937	    7f1203df2740	WARN 	wallet.wallet2	src/wallet/wallet2.h:1693	amount=0.010000000000, real_output=2, real_output_in_tx_index=0, indexes: 5775823 6612437 6757719 6837338 6908970 6912779 6915724
2018-08-20 13:58:10.938	    7f1203df2740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key 4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11
2018-08-20 13:58:10.938	    7f1203df2740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 1, tx_public_key 4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11, skey <PRIVATE_KEY>
2018-08-20 13:58:10.938	    7f1203df2740	INFO 	global	src/cryptonote_core/cryptonote_tx_utils.cpp:284	construct_tx_with_tx_key:  real_out_tx_key b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000
2018-08-20 13:58:10.938	    7f1203df2740	INFO 	global	src/cryptonote_basic/cryptonote_format_utils.cpp:204	XXX: r 0, tx_public_key b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000, skey <PRIVATE_KEY>
2018-08-20 13:58:10.938	    7f1203df2740	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:205	key image helper: failed to generate_key_derivation(b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000, <PRIVATE_KEY>)
2018-08-20 13:58:10.938	    7f1203df2740	ERROR	default	src/cryptonote_core/cryptonote_tx_utils.cpp:291	Key image generation failed!
2018-08-20 13:58:10.938	    7f1203df2740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:6653	!r. THROW EXCEPTION: error::tx_not_constructed

## moneromooo-monero | 2018-08-21T09:55:49+00:00
Thanks, that "missing" pubkey is somehow corrupted. Clearing the wallet cache to force a rescan should fix it, though that doesn't tell us why it is corrupted in the first place.
Did you use the GUI on that wallet before ?


## olizax | 2018-08-22T07:12:06+00:00
May i ask how to clear the wallet cache?

No, only rpc and cli.

## moneromooo-monero | 2018-08-22T09:30:21+00:00
Either "rescan_bc" in the wallet (don't use that except when it's actually corrupted), or exit, then remove the file FOO is your key file is called FOO.keys.
In both cases, you will lose things like tx keys, destination addresses, etc (evrything that can't be extracted from the blockchain).

## olizax | 2018-08-23T02:01:21+00:00
After executed rescan_bc, the error still occurred.

## moneromooo-monero | 2018-08-23T08:16:11+00:00
OK, I will prepare another patch to add logs tracking that pubkey to see where it's going wrong.

## moneromooo-monero | 2018-08-23T08:28:08+00:00
In the meantime, can you please paste the result of this command in monerod:

print_tx e5f0c0b1c482e036b8aa2a8cce3e6956a0a9959c0ee1304e28fbd40ca221efca +hex


## moneromooo-monero | 2018-08-23T08:45:10+00:00
http://paste.debian.net/hidden/bf0b3706/

This replaces the previous patch. Please rescan the chain again with this patch, it'll print info when it gets to the two transactions in your previous log.

Please also paste the result of the command in the previous comment.


## olizax | 2018-08-23T10:16:40+00:00
print_tx e5f0c0b1c482e036b8aa2a8cce3e6956a0a9959c0ee1304e28fbd40ca221efca +hex

Found in blockchain at height 1632603
0200010200078ef2c402bbaa11f0bd42da8002878701853de019091c2919e39878a7ee499a7a8ed86138a75a1917a4cd7bcd7f61975464526659020002abf8d23e2cae39626bc31cf46bf3cd036556febd7dc2d53d4ec4282b65fe97a400029c93ac20f572b57eb6f2ea346649602f97cb7b568d719ad53a5e66fd401180e0a7010221006e719b750756e029828c44132ee0b8454a5483c42a5795abb3887b47088d1da201b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f00000402b37dff1f323e05add027309dd0181c3d0c47b2a2fdce9d8267f570cc523d26d9b37dff1f323e05add027309dd0181c3d0c47b2a2fdce9d8267f570cc523d26d901b37dff1f323e05add027309dd0181c3d0c47b2a2fdce9d8267f570cc523d26d901e09ee9c9080ffb0450457ea152a718d9304c116c63b6a17522f3a1a5d9ec3993ddae81f80ad1c08e6b7f856c5ec6abb64e8b8559427bdfc07cfcae5306a6e4786cf1546b0ddbc3e26f9af396f2fb19bae3ba25d945669a5b25e8d64d6180402104c4519b068784f5c7f5cba1f8b6d80557e0fd380b3a794b4e5d93ddfefa6d25e9609da30dd1e14a251c040bcf5eff548806d16e94b8f0121ed5351eed70a9d8c5d616b940035be4d570cbcfa161da23175655ea0519972caba35a83906311c8e782e325c5df8f57d27143c1babadf8698b6e229df92f9987dad964cd2f2865b50bddb2e0d8e6b43e99fbd89f6e98f5f5b7a1c18a686640e32cde833131f19331510b1de0ee03687c930d026676ebbfb8a5a1e5a7695c8ae721eb6a39c95fbab4d20034d0a1cc5ffcc54ed4f7c66b4427478212019e9086e765f05e592a49bfcf2c1afe103fa139a72eddd0e1ddef9bb4c8cfd6390812bc83afdb27d7e8f3be3e007010106fc2653f5f3f865961bfe3e66e72ae373ff27ce1a54babbffd2caa09a8244d10c8767312a1690bde8fa93708051deb273ba8eb20d750d6f30130077cae9c8a509ee9a9f16c9de0c9de4f5f1b5fbd1b14a536638cd93728b12402870e1b5290501e60178ad4a7685a52366a8dac35630a44b41e9a295539b2ec42325811d3d8307a35ca9a9441894c4d7f7e2cfb5916be9363423bf5b1fe3e762f64067eef9360183d5938ada8da87761218d6cec769e9acb255c4f6f4d7cb8f446715b675ffd0c389157124dc277d1090d9114af4dd161ff5ed042e2ec68380886a8ab03833e08bd37bcca179367dddbf98e8c6921d4df56cfd60cbec58c74424ce44e0e78950aee8cee82a56e08f64b0eafec9d9e5bf4793dff33aca18460f5a3b97206656b0228d14cedad9118494d9d461475225dc6f314c4f078896b5d9fc79e0e5353fd0005903264ffc9d754b2f0bbe30d3b84eb7750b8a14bf53c1560b9129c77694c069d30278d9659eba751b0800ed0a50b44b43f4790dec88039a778fa8b373ddc061428ec3b5b08f502bfacb378ea4d98334cafe89636ea0b775d891d4338fbb80d872a48fe43816c93fade209ef92f6547cbc6f27335476224bd8ad273ce23cf0893f23a2845f40888419e1b71695b45659d6aada0e52c44b598b21bd24eee4709557196c18fd2cfb67704d65231f0c047f461c6520fa1a1106140dd07817e0407296e67c69d57404b4d9f23ec92b6c5f90c1eeb8e2d5c91e68b830d1b31fa9606dd20c0286351b1c3eb7e7fb882e95ae6c0ef676303f29e9a0d0aef6d4273f50ac7d937be33b82ae633a511fe93880450f953c14382ccc6a2eb80a017775fd40e169fd75a8be51b06f6c5edeb986236f2d4b16a0d58e0d3fa112c7dbc42ed8406af7d23445f78286eb775695d22dee2cc552ad508b2df8223fb0b7f5b0b60ab046a1a8a4adaea5d5a5079105778ab54f5a02f16e8f473dc23f4c86a8fb27fcd049708c74dd58db21231aed20c4477993c4a72d13b60cf63abb6e7d16be2606d01e96ec1292376399f931fd3f494ccf102b08481d4faa711d13304c50b7103e20672b2632c822fda10ffab799853bf7f2fa87cf6bac8db43d0cefd72742f632e09116efb2310875f764136ea291bab57eed07dcb2288cce884ac607a8b5e94a70c8c8df752ef2d0f60184711b71536cf31bc1bf480c5c0e71036e1cf055458c407d2e2cf8124211bec9872e9fb72ceb371ae4d04954f9ae272ad46d6079ef60a0aff54fc351266ada4bce578153a6908238fd0ac410f7ca7aefe9969cfdb773d064fa0aace2574abdce4cbea14227984ac768223ff08097f7a132fe1588f3b3d0913399ff331a0dbb4078f127738152c927645685ee1a2fa1033dcb09cc46e8c0bc85df1ac90eced8f386ca5d5391ac2bdb5f01fa4269f3d1cc3de1d41e034a706be1cdb0d19908821c20509974846f612ef60d9947aed6efb5bf93ddea1c7340eb2d8213ee82efb168fd26f122d02d885076aa4b00c9da8c979c30179030c5d01f3f6aedd487a76e8b1e0495b402259bc6057b35ec3e5540eca45eeab4bbf3d0ee7ce7fbdd0450a6e16ad7d708c810545233e4786cc901960f52125950400900d1582a9f9d2db8d530f75538cec5855c510464d804101eb5e046e5ea6e7e49d095e917a6d9f6f70dd6674bd95c9bbe153e0dc15ef59f75f6e6c05873a54e4430d4a4c922d5d51adceae141307ad23a463207b13f8adfa2da27439f9031344830324dfbc970e92481fd2e83b2466356a2b71f2a782cc2193670cec33b6c3edc9088ee4456f9682bd62e3ddd088cbd47c7c5ebc542e6b9a714ad60a5716d0cfee0be291e08edfdba221f2fd742e3b4b972d401b6585e0a1723611250d19e6709805b7818a855aa85e17644340404376dc0ac920b41c7b6f3c83ea87c93f87b1c706540b0e113aa13d9719f273587cd89ad1cd1e1a5ac306a2378bf18a4a92a14904b133b716befa96a46b9903604d52c36e9612ed008c18770e8af609a620b78a0f46fecf88bdfb65f2f1d4b4e8a0684931d50f83fdc11417591b21164e4eb51606e87600ef4c7fdfbbac67b7deeb8fc2eb097c490b0433cda31066d9ee9b0f5a03ae69b3e8b607d6f00ec0685e3ab75f443f2dca5b52126f049297332063f4b60b6714a9c606ed9e856fc28aa89ae45da0e87b59c7b41e11e8016be8219919a40fe1305eeff701e8f410a3b58c60297c6bc596e3208a0c8293ecc4a891f98e4104b935046d0bb9557f851534dc61a967a8f8fcbeb889eded07881ea1f0e58ab406804c319782fce3658fda06138bc1e1a0af03d314c9694a407121b92fb83f5503d6478fe9acfa2ecc8dfbb7ec5f0683692b53f5939517172b8a34269bd0d17a006ce89ce1874f0d6d6ac64ee72a180646aaf11ee27471a6e1fc33a5e0936fa5067783f12042600892e6de015a8b4e78f1224edce0a37d23c4d83161fb55969d087638d7a8e1aba964dd0b68591ada0551d4a40c9416997dffa6d213035c7e8f0969685218d9b5a816e023b3971240abcdddd0fe7414cf91920c5926493c3bf80cbf25784559d838de83680b9c0fe55ca4ecffa843b5b9705242946a4b13d15e0777de64930f41a0491529f5d7b3f63a7f8393add099f6b2f5d88770fc3269000d9f00c56f3eccae27d9cf490209910d6fd8f2a7964d9000e83296b1ba3fbd2d03951571d1c2bea8a9e8426d0d8839ad6f35efd3f76770e8e49fb3b4e505fa1b08ea9107ae969ab7c8d1ba8a5eff1efb0cf708a86d33ace5c301f281dbc6c03c0437de386e1e2b2693d3c71a75393b5b8ef3edab664a448ec16f7ecff1b60fd805fc3071e3c8524f22226750e580b9ba5ff7cfb0b19a6b5dff130ff522951873056f7f3040d57425433f28d76cf729ae23c75341b7317f2e0cd1e9ad12fc4629025e10e9e50fbb00c640738023b1d8d2ac6a32984d0a7a3d865d255c5b74a6f40d27ce9c80addb83d22a68574cef0d058969c52260f4d2e4518880ff727fd82302851b35c6aea901482f898388dc1fff56dbc9d772f4843d50631d9e530aef66054d8c20f1b1a83de5e50867c802d470f34de0088e1456c2a1771041fd83bd77023f3a4e1ce1e5a7e22b3669bc8afd2651f943245639ee27cee09d0b9ec9fc520a6d6e2857ddd927794c15b7d882e4e928b32b9dc92dca12f4686b1d710a9c4305908d41d21e36676b4bb61b8658f2e9454476fa610dd5be14b3456b3678dbb0033e619b1b6d19d061914b343338c478b557b36db01f5b3a453cd3112a8fd8320f429a4d29d7d164ade2400764d3b88099b4af0780a9adb397fa1258c2c587630a1c97e7f2eb3d2a7fa3428996c4735982f43fbd769483489d4dfce080bf22bd0f56a70c0229747699892c7848d382d9942c110358698c41ea30cdeafe6bb78d05f8b208b488306a174d4905272e2839a48182bbc4bc844a7b3a0e8fa303eaf508381d212c5adf043b4ff762685b7cc7a11293c2ab2ebde114916e00fa3fc3170ac2e42308b9947ab90a7a0395d7725e5d98402f5cae3873770132812071f3070c81217df9af48a8e6663a03d4d6de02bfdbf5109dc7e4f73ef2020c5e2c978d035026609f19f48fe7df9d8642688f88bee7625f536ccfbbe26d79f9861de1620f1e98b1ec3bb2a257e7996e5ac7b8608207f5d29e5860d8821aefdfb127a64b0ed604f07d7388b58bd2405aa8eb233549e2e13da2b3ce9aa712bf54acce59b00df589078316eae6775469edfc74fc083668a0c5f3382ea370caeef1385faa390aefcb894c199f45ba2c85f0ac20a96f73c12306cf614623854c8a218675102b0531bcfe9fd6d1482fa129bc6efd5f882d02212239c263507409399864b6ee8a070874166a6f8c398a03a8c4a733ab849719dad812d6f3f83931e65ecaa7096f00941672a360b3ab1463ea2a06fcb004a0618983382abcd548af34863f10f9a20fa4f58370ab42a25c7b07348b136f59a618cac4944501882a663881e65ace960e58d86ff670fc121a8302ad8c13d021fd1dfd4557a93b03f195fb020892233b088d0f2dc0c94fd92b84c218b3431a4a1f9fce84aa3b910659a32852bda427e400764f8c001bfbf89ab7ece0c3f8e6326e4a44fc1cfb003be67a3094517204650e395b40a771e6a8245e26c073f68cb07a7d547522b111b07f6990a5ee32e0ea06686ae712b13bd9636c27671f1190fc6029b1825b31920e3a5712c147b0038707494588003214dfd1e9f3a398a8cdc32684cfa5db8c080c450cdec07ba2692a09ae9a65c67ee103a8f9f57928de5d0dfeac4372fcc38a01257021d8ee2bd62f02b4fe5b675af07d2168c143f1281fdfa91cce002d89c97f0a59fbf7b2a6370e058c900f56b1e1531f398812326f070d87be29a27066f8dc10b50886d88fc0fd0145ed5b7305d3d4737f77d212fa963b837c4150602a5b786aa94dd50bac1ffd029e0daf1c57cd42aa06ff45e49399410847e8f9e965d5f1fdb0d275b22ebbc9056d579c7b5bca45ee04247407a137549ca9fceeb712f8800243226b48a2c9540a9e2a3e1a40e04b48f274a72b1cd93875ccc397323c4ddb80bdbfc8a356239c09454acf5ca6ed50b950a08c90b095fd7bd64d2f6824ac27e1d0ce9476a778c60add8d9c9d72ff86557ae9a4878761f730e1a7ab44f69bd4c76a6d05e6b3c71d036da10e33ab4a2d5e2ca581843ea8944c39a07d0d89e02b369faa3e0f1cf2a500ad06ee514445bcd9396455318947d1d290af81e2467d84692af98983723be00ecd7c62b3b6fa136beb2a66ff0cc34951a1c6737488234bb6b0facd1733c60e09a045c8eeaa193d47731d5ff2e88c910ce57095e03fa74c8c1f30d5ad59fe4108b704f8838e1c49846aad72851e583606cbc558c2717566429f1907d53326d7072bac9fdfd6bd9be3d773f863ba8108e38d3f9f47a63ce1193b9f2347079ff30311cba2a94d1ff42aa9bc850387ddff41a57224685bc559e87da326666c1ba90f3ff60a4a120ef5dc7974cd2d87b2a58bbec9d0d4f3a7b7b9077d8eedae621d0adbe3d468c3bc45f724e10736771dafc04f90182af5704034c24d5c9f471dfd0a26681c257f1a4b132d2bdf6ded662cca1f43f2ff1d95feb9abde0d1b546b0e0553204bdc4773d684841587eeca8bac0ffb226897b9f949a0565025fc8f5c8d07644b2dd466527b8f4f73f6a71b9ee1a1cb527b64d856bfb8c7bca99ecea0230e65b0812a7406c78a2e637a9cf58ae18a15bc4e3f353c0b12360ad782da6d22066f33aa1111d274c6d66f17f9b8dfea076c032e7c0f641270f8e8cd999bbb350413eb03f5b1bc424640eae1aa0088438a6c4f6debad0c392c104a42d6d25d380394dae387d01aff714af79e5e8795f66e079fc89abee6766d95bd5c305b7d650333464f668617f169b598bc7e31334b47a097017284bfe4bed4406f425c1f910871666785ff21612839c86dbf4c85c95408c8e550234ea2025645648530a48204cb00816aa689f732cd11a4aa31a990b9c4c78f71fec08b8540a3b908ff2d1803dd3fb0692bd80238c9211d56749694e4b8a94892b6671ef5d58fbf66adce200ac4d1cdf21a7bc0bc39a184ef663afdf4e32a313c72ae10b5868f139e3bede6292dabef8e89eafe391759b473a881a5145168290bec45f5062982e7e0825a8f7bd9b7ef2950db4ea495c58b9a5f4f9fff29e381904877e1dcd2b81803efed051cec15a73ff97ca4c8a9546873b7df5a68cb363d49d4746e61ba579bea93a57c6fa90ff6a4484feebbfa600b63a6b71193ae294e117197880e0787401ca669a5f66a2412feabecc6e1d9808ec1ff5d60fbbb48f2b0ad584ad734d50095643121f48b283bda8f32c1c7bb3e60110e20f00ff5a9c23deadc151661fca4b559bbd58261830be11ed2987cc03d86804deaf5d5eeeb165bd60d0080bd06aae89c85eb219c761511a3851760b4466068ca3a6342d882ecef601e587eeb7a9a3c33d79ce282b0c78c9611fa9c5ae3de375610f748766ece4968642cc05f3c4d53a7d933ec68f99722797c2cf28f3ef60a3b526e8625867c7dd113a021543b2eceba81ebda58df3acbd991dd2aec20f31c5f417d8072ee8da43feea5362efcbc6778cfc021158333027f68f3ccfe9711f1ef50f29351d34ceb9cabde3dec692f18e3ce019544ba38a3ed59cc3f1b21af8cdd3bee573c7efb10795148af35334cfe6eb5f0051e46d2c23b2b7ad88496dae8cc9f998e32c280ddab3fd3d03eb222b2189443260b74cc07e80e82f96341c85d361692cbc67c5eddffb7c6ff3ef0e35f68eba3b04a235fe963f8a5b5ba66d84cb19bb1e74d449ae28bdbd2f4d5627bb207c51458f84846de432fb30b7098312f216bfbf54b88a6181713ffb8545edc75e59df63116a308509a0f7601548ae2be9222ce77273986cbbafa5bd44a5d602a0e8ab2384a5ced7e39abf0e89c954050c8cc62c2cdb6fca74be734d1b0ee97115a9acc85ffc1bfba81481bd9e13d5d87b8a1ee41bdc842812a1fd8cf4d4480209a00ed831b5433ebc41c580b4372f8dddb2f454766eeabd7d476533aa262cd32f4d3fe24824bd503313739bc7ace8e3f36080da176466b9712b7e3897fe52c43d4909e6baf1998c55de68758a735c7ecc7460981de3df44d092e114934da64e21081e9d49a08c4326fe5639b966ff46d3911747abbbcc3ec418b649d4ad025f5f42746b2cf41548642d0ebf3540b306e21df3dde947b291c743c809e799e2cfe1540efeaafaa32b9842ed9ed02ec8715882bd1c6c34f68391763f1a18ec37012fb5768b2c3d36564a7cefcbb2d00795c9c30c06eb92e2bab1594ab41bd1e8b27155378e8cbdcae7985f0e42279eb010205d853e68515963e0b263492f4e286b475b6306478c2323f9a6a6dea49249e7b23ace3aed6e828198591b246377c8a3f5db535efb8f10dc1061bccbff1e3627da626fb8afa545820c362e1877081474a9ed22b161bafc5e2cf526e3b2d5286ad96696b9e7923e7e418aadb9815eae7ffeda637a2216e1a3a761fc228a6676812ae78d2c5dde50aed92729f7fd0c825cad868321f18986d41a6e0628acbea155959847a82a2ba47456d33c6d09fa2da62a065b0b50a6074feb2d2719956a3f0b034d5c1e31a6fa5b3edea4a9b872f1604eaeb1fc8706ce35bfe8408ebc6e0df712c34824bdd357c2ada190c647b14209fb49113648e25e61c316be222401a9b44a34156dcb050bd4d7e6a6c389107be7e53e55541ae853c39c61f86b480aa827dfda37ed72625c71363adb2c389a5392dbec0519575c18f23340255d40d99f6bdc946755e08210ab6dd8dbf5e4540b01a138f3994d65a2855fd5f83c56285bab8ab63d2eaaffa10b69ed96c3fb9b8a957ba874df6eda4f330dd22227b9cfaeabd607a99d894e750aed639ab2346310e0e24500a5af504444a13e69b64751cfb3ede8515b4e14a5a6527216a3a0af7a6d95a96ca7bc8d35c6b3a5c1b849ccc1189f6beff3037c72eac1e2267b24276b5078afc19bebcdc9e8b2e56fd02f1eed0d4102196c2e36bc20a4337fc7ec38d66fa7ffba7e947892751aea924c92f01b0b8192d1cead94d8cc19e17afa21e617e6799bb0b90d0078323bff357e13cd5cc3f50da676b11193fc8afccb5c1b5ff40ad4d975f0909507ad9d3c143f41ad2529a55bc6ee723f840df464f4fbbd471e11892ca839c20b83ddf4d727f0625e549a47d19d5db05c2b9b653c0eb2862ddbfc802f2676995106d92a9bffca2e08fdca3d85886df61dabd8cfe415c9c2a0acb1ae936e942d9bfa7494b467d81cab4a8edd1c81ad911f13a7556a66bb6495739cc330fddf6cfbdbf0df1a1f693d2f40bda0bd6467772a03ef37dd6c973062d9cf27ab207543977b560937b9352c934a2b560515d496d4a8e9466ee842c6d42f59452eeb179d975706d5e3f747eb3b5f502d37cd2719abc8208153820561c24b7fabdf887816cb2cc9fe965ddabb05f59685350e871b60b412c0169776bc8f1c11dd83f0af59d97e30d5845398a3cc2aa21f3e61ba079c5bae1eea6205996bc763fdf5219fc5e739a45ca9aa3c04786fd6a03de1177ca9adbf6f19970aa8af2229cfcfc2dedc325bbc83d9e16035bbc59c0464f729754c0401e3553d4317b1d42772c68aca36f17e2a6aa129d29e1b7770b980cda174b3700452daa4fac7a538cb018b6b7fc6c4056d2b3d886e674ab92711446e3671b69517ba8bb72863610a7f34e34f89cab6d8912cf55802faa9f4ebc3962cc51af9b068b9e3f115db3e13e3c43a00a3697e116f0e0e20a4fc8899a2cfcd37cf444d47f10fcec382ebab9b924adb60d8cafacbde0e96b59bb2edfc791499ea9c5b18758acdb6a55383721d51a17c647d7f4399917016cebb3a1cbf593309328e53146be6da154c9572e4a1aa1235deb5fe43a3249c62b74182d8db5376f505ee38f411fab9bb63e4159e7b1a4955586cd0b425d36810736befc669398aa55a13a9f352633902c6b8a383f1b2cb309020ded898285e984b86010d0e59764e06dfb5a770fbb6cfa267808b9e54fc3db440c53b216c1f442e0898ffe580bd813a62c4677ead30577a584e1976ef4eabac6082676cea4609f2cedfef2bc1545792783f7fdcf2560de858618b73cf1026eaf00f11c6c72de4c15c2d96032a2d8f36f4cd2f5b95a318aef212aeb7e906649070d522aac1643428e0065e3edbd4de3e6f72c92d6e91a4eb90c79c2bca59ee6c806f0749f214fd5ae8ab6e93f1729d488591b921fd6cf7db9d6c29054330e414b0c0dade3950136fa52bdf80bd145fc620fbcdbc79d28f0811c26ef8a10417b64035694a4c30a088b1c947c86784330f09517be057ebe4764e4b548f46d3359f60147f7f81c049e5692e5a4fc393dea4186fa2d38a7f80285247b2c1d1d46fe650f81e2206bca6ebd873c392b35e430ff3da873a8f19f30cd69795d23ec2062d208fca6e39872316967e50770d7978181e7150459c4923c81704341ed248eb8a6047581c86093db81938120ecc259d77beb5cbfd0503085782ab5694aefef063d010573debae3646396e51c3824d6f1f1edc3a8283abcde317f6a2872c1847a1100490be6e005fd0cc94d0f3072b1f721ecc484e3532f63848b60627f8b0929eb059a9247c767abf7c4c81d5fd0e9c38aa520bb45f14f52d9440c7587c2200983017a485752fb04d1745217be373d8fe01a50fc73869ceb207cacb10f6e0fb6c60ef68109349500f74fba1bea0bdd46fa3dbf3a3c07a5c44426ea344e3302d8fb04488423d6273720920af791fd273903b5c22d1f14ec9a853d6930a6bc05c05d02cfd0df405ca4ee5a04dd5287969c540e38739b3f842da6cd78aff14a8687310e2e2f39881bba5eae501c2e91d24527307a28cd53e59a962b6f2bb1ed5c44e302b19179c088d6b920d527fc484f62f36e3fc1e3ec8534c7dd235a70821b2aca06c7a1bde6a2fd46074305ec6f1d952ad189d49edafb58f62e498ac072177d6709b7a3efc80e519efbcab6b4bbe046a00ef059db6d6d703da3890bd66e6b0d8a0f577d546a97073bcaad2911338dfb51e6c0cc9dffa4265ff6607255b1ecbb410a94eb0aba44b5e38536dcb03dac84ebf2cdb68bce959e920495811a2501d73e06486d86bb878cf1988b4fe92f0f994828ef5684649ff455af7d2170750e56cd0bfbdea9270d0af8d4e38d69771e2d46d464e79dd0887a3a84752ee3c36d2da80f06e083c9520151d6a3932405b8fae56474f843242c32aede1bea3ec6de84e700e6125b012e917a9afa2cda6cabcf19554415261fb1945cdffff9007f1a09b70ffbdae5635e534adaef20494310c657bef2011948009e56024a52b81168192d0b46e3a65cda93e7827eca85a7aea54234354c68c3592ac6c698253b1870a14c03c3d43650cc756fa8dbc7ed5e7b3b4e2f781977fb2a001a6265904e301dd65c0f325849955221336757f1e843ef5e0602dc1e7500fd79d9544f70a8232dfe37049d773171a6ad4f23aaef4afd2e0f431963af1f829f81ef17aada236de0eb2a01dc36dc7608882e358b0b9fd2e535f23bcaaf631f7a9a1632f991509c36c14e0172ff5d6e0c3bcfbcdf0f9ba099960c418df838257f8c62b126f9acdbaa791a068fa2ef30a511feb3cb744ab44b5c5a3ea617f74e6f2b179d29905f77ba5f58069631bf74d4a602965c0b02e8cf4b0ac838a359cb3a984254761c48299c94a30ef657c25a79fa7955af1fb281d57c0b6f16a26fa4ff687f2223952a79bfdb8b053da27f27dd054779e1bf5b3a283dde1590e765fb20782a36fea56e4637790c0119ddae784936a240f07778b7ea866f0848e9dda1b1bd872362531bc55dd42c08348800829db4e3c853ffb822fb478a05d009beb1d1618183b148de2d5980e80b04ce5147a0c5fc77d7aac965cbc5b477bff4e54305a6856b26033979ad40ab031b1e3945f6c72b95b11425b208c78b0f270607514cd73568355357f761fc3009b2491ab541219730085fc55ac451e318f958b1c3dd63e08595ebf4ff04851807878f95582d8ada6214173ccdd5afea8e43bcf4ab42b35784aa22e96eaf2cfe089b8700498734d2b119c0dcbbdf5a2ddb7f8df1380c994c0b27b2ca3d68a088074c3c05b3956c1d08852e5501147031ff7ca6541d0ca9713a21c6937e1c293d0e2851b8c175c99a85e585ef61ea21b86036bd116f379f4e09af3a4d21f66ad60d3c0d11a4541fd34952af3b3b624d1df3a15b985292e21e71cba76ae00053920e08ce39dfe586d4f772f17946b93e026f96c75b82f2ecf5d6f7d2474996290303945214f9fbe67c91737bd42f5d8b74406f1f30933c40e9ad797d966cb6d5b60c9cea21ae1923439ee7700abc79d97f472af51321b052746f76746ebac616d80164c063545bf459655d470b48ee0a5ce6ce6236c4dcf7920523599836dfbed90dddc26964421460faef2a9b1b4a0a1bd7824cd155a9179f9bc6e15a326980a101d4bfe94c3121a77886bf9235e58c129757f476684cdd375be100daabb37cfc0dc4f03c7cbe7875337af04a7cd705879a6a8d0a5ec77af256c3ad1ec2cc6ccc0b52c68542ec025ca65e9e5015aa784e4a48b7978a0e718564a329fba7b2926f0a2fbabf44462ad11370ec6bb14f5cdfce75283fdf1d9257ac2c71431f1db38a0d168508fa83b09b6dc57cadd7727a17a79df80c279f5a4a7e429230c72d823f00dffa3f8b6e2c63a8dcb60544ff43b00584ff8c328244c95c4e8b809bb716650c1d275d4518ac7a7b804ddf0a898066c4222dfcc24430137d0a6660ae4d457e0ed47d7658bdad3a3c5dee675fc5f56ce93359ebc29358cddef36e38e771a1a307c51a104b04ca560207d661a74f7977b153b6b9ce0e0689d6acb3c0a43019c4041ad3a85d514015643f00b9e714604c00535677ee04c1ecd9267e3298e987960134f2d2ebbbb0c3b4a69b9ee5e5048dc784961ddd44a1a93a577c89d8dde0b307ad54392a80c89970a3b7eda699b258198c72739a8bc3c5da90eefb8631da810e2d6f27061be707c16dea8b97534cc109d775f809ef9df2945f6006f019854004c81dac5c28fef37835bc80acb7e01d301b9444efd950d4a8f397e210af625c04c5d01a7f122887ad5f76d02ed50a6023ab72cc76ca47d6c147d90854b11e00012ae9cf5cd1c74fb80c40c611716a54338a89c5d43bdfaf3cecbf756211f6bb00fb0b2325079ab59e570ac0f7fd68b84101c7990438a03d2a6bec3e8c0ca0270b70a823ec65f4177cfcaff89c376fc1d9b0781f0efcb69d201cc935316528af0cae0cc603420f0a3d813caeea247671787cf872c898942baf5e1e9bd9d68900031c6b72f996a5960a10fd14d1e80b1066fc076b16a21233114b159e9874627508775e206c3e7cc19f23196783e85e8f7f6c28d61e9e850631db377ffcda116004a86021e2ea74745ab592cd2a450b717ebaa1de086832615aba3a84fa4708c903d1a88251d10f6cc12eb8adfbac0ef232f329a1ea39c893bcb2f7019b6e9f6d0853278a178f994d327ce4da3214f1d456377ab445bb3d84810c850e00edf45a04544f993ec98e21080bc77cd1e50a348d64a097603631da1871d974b90718f60ea3c9accc6ef8e72b66c81d66d5094719ae4f524a463a0a8e99520aaa3203520540f23a10123abfb12d7121ce4c2189b16bb97ca019accc7431cdff71c7019e09bbfb0726a1d9175d04dbdd923d4a1e439352b110101023616d1c252f5953a500a7dd004154048f1cdf1415e7a3bd4ab63273f702f834faa5fa28072306681206dda783aa1e5202643be3f43b6308f60d0bd9e83f08ceac1c9eee9df0276b9706d5b85a4c1aeb353454ac7049ff54f02cbe0cf52a0b4092944bd475c92690c608936fd3933b458ab977929abd6d61a2de16ba71840cb81e7bf690e38b9de72b00aeee53ee8c7ee3074c38799c6866ccff45312dc6cc7ad1a37d5189cf8c2a6b057133a450741ddb58d0019180680a5b00407bd57841ad6eeecf47c1a5a0e443074e6f0c84ace783274138bd898b35405b12c5000384a1d1987f9138841a66fe03fdd6ba30e615277d8a1149dfd90febfb95ddca74cf3efabf1c456f27727a8308995c4bbd79b6af867989967d5083905cb2ff3e45fdae3ff521d887297ed6170da8f44051cbbb1bc28a3274937470aa6ff1a0594df656cf94589a64b74aeb6a0df6fc6b3484a6818dc7000ab56009f507666865681c27f56a17154a984a6d7e0a634fc59774b31e18fa27106ecbf46983509f52e15a1f44ba58ce9a01ed23090bb694aeeff7811f05424f253e52c552d8435c5aaba6e80b2cf95015c0b1aca1016c952589582aefb875d274ee20499b0ba3e19db9d54a0727b88d201e1f113d0f7261815691998ced91fa6ed22baa36e173c33a3bb1e65f4efea118989595000cb6198dde54c99521419bb6be962aa1bbc43c24628b4f90c3a8a737d973436008b097363ede519da5a0f21a108d5044ec48119eb36a84ba1979d728997e1d09077fd40a63642db70ed008892800775c0e1f24cbac040d7afa307a40bd3c1fbc0df917e57ae1accfab53d059503eefd4d8e17b6ab8b9e6fba1cbf6ea2117a02d067318874a944f09c6e8272e281461191b3bb892b4ec9f42ff1ffcd1278c45600d32bbbef8e1f35ac3534ab4a7fcecee0f25a9c1405cbe5f4df5756c73f7cd08013ce5d7d8bb98006c34a682f9b91ac684b07062d7522b483bc8400695899e7b0db1ec31ad2cb14e87798b17f2e1ecc5739f5d9f67e95e272b3edbdad212205d05e2dfde992e8452c04863843fb1ee9a7d88ea943fa3d37ef00dec1537099a2f007e80904f74555848c5c0973067e40516b57b8d7f62ea09f44a7bb4b2198c470f091d280d47e785a9963f380d561551ec3417b645a7b5a496ec03e73a16d17602bf042149856172137f252c33fc726287fe075d83f757da59f83c64498998ad08e05bccd42676fe050c7bf3c24c63e37f082b4660b2610c0a10207a68287b010934a381401cc5aa2554a27cd932b65e55a2bf9c481522798ffb65d2acb0192602a0f87fbcc068ab6ca935dadd87c30e9d7fc80413df51b237f533d9297534e50fd236996be6ba423f912229a369dd878bc6adff87fa173c1cd1cb16648862a30590f3be2379eaa3c56e8ba1eb4f46dbde9c64ca57cc54c5502d396df5d46b840b8a2967b827f3d4fce34c20f41a7f247d80b2ca83c1b6201da92256301bea7e065daf0faaa7c4041aa0687a9968ce571d13e0b407f91060f1452f41288cb85c0a07cc38d93b554222989c6e5dd1e65213034039b408277e39b392b9b51df68e0bcb3558d2b0bad83cfa2cc5f51da1c72f40141e09570f555bb7bca6ec3d740804bc70ce4374c2df5ae1bdeada27636c392031d740f4a21dc3d98132a19204eb0d675154f215c9ac04832614e1a46ab66ec94c3cdecd412d8ba0ddeb658dcf5505161abace5a5d0608b30677e5495ea2ed12aae26d607c8f1a8c469f9f512e5e03a6cc724396f773be5a1e4d871fe154ca804a78cec405ac616054fec1a3ca6809309c8122974ba0ef3c0f9fd279cdbbd51cab8c5d903e51a3ea231780939139014b87c42388d24d239516e1da687beb0c39605b0763b99a41f61f47cd84a0b40b988515b4c33a890e9a3436871f0d846430ff96d0f8d5c7196b3e06664960f606ab76caa4ee7d132ba95d14c2f304011344da44015579a2b2250af6229ff5200b247dff41a1b4b7170a960e310e3d2fb52af18d53cea1adc43329c79375ace00426e140b28cec10e8208e9768e9544dd08a58599e04eca8a1fd54dee9e6314cf82ab57f8af8923bbf7e494519e459aaae69cf085132292a4a1400f3faae56545635d66a9bcd0a85591324bb1370b08d4bee27970c833718c92764378c9c1491a8e74a342532a46ccf10bfa0c784a8da6d49b9d41267b81edd387b2be87560a700b87d161edbd8e7416fb4da191cd46c333cf2bed93cbb8c0aefda3c400d9d8e10db6ca6c5e138631d4e4334debd4521adf9f4a7390e4fab53d15f16dc767e446747acbb20ad01b2fa517ef9ae72b62361a21a8794f72ca020bc52a681a274173a0956a8713738f06654428c15a4ad683dd288545c0baa27516ffbce8653de3a6f2a81a1a16e103faaeb721814729cf53bb8e8cc3a89452a890b5f9218025379b5bd8343b8caa0dac2418fa6ed7d434f38d7421e34377f6bf6e1c7763e9c43fa8850ab7631bf74a2978eca240a16694ab5ed2d2685a234bbbc9b716536ab526e4bd4689cd88d012da2d58c88f8f3554fd509b78d576cd0210a82052c1bc70516f544f7e4da96b70e1bc5ce3e54b5e4b778036dfd84b2cd970e2c4405efdc5f18ad0be61f385dd66f79130f6fd16b1de7f6f868ab985db5cb60223929de1e446476ef7d5d31acdfda6f14a0ef4a198566d67cfec442e9a20f6a155bdf91febc79c105b1c93f1f097c8bf45142c0896d4a13921a78eb42c2c367386ededca0fccbdb99bbf383324680234863524c9d044773c9bcb2b4d56725fcd274d45f9e3b3f0a9fc82f4d06a734ec9f1cd8070e166760a763e2a18989931c718d3edec2cdbd9154e8e193739c256dce496be9b71b284bb0cca2caa5a6c80ace2f9ff673dc90fda0cb522533ab9e29f81d89f52dc968859ee1fdfd16daf636a411d12c32f1b411c9cf759f95e47abecc98eee3adf2eec61aade29fd0569141c1016f34c9a44b12b812f4319eb1c6280cfac759aaf8ae8a13f4772ef6a19923eb6539c875ee7b41633fdc002b5e1929d41f8025c2198ce8f9de68568c0ba9b1da17afdf5c69f16f9c14c15311ad021f85fa02f50a61f387f855596b160983c88a779485cfa186e303a5441f157bca9da85d122a51fae906a93b0750646cfd193eb1f7328dc184236abc704a197ea1a625c4357784189fb3c3e81c58faef16e5cd534fa1286529407f9a521ad0a1f947958847956fbf160388fe192bc221036dcb8a67a9b7c27aa98e574bbae97e624a5c558bafb92162410737a1611848c120e6363b663ad918468a0ba38b252f3c58d1ab7f89a7d8b86bc2c4d860c4480488c54a6a1131f8933394b46204c4aec88d62a0a89251565a731e4c7113323fa72a9fce67de1e012c44df3e32ab761cc611485830300a270b3df0d7ce8f79fb51dde2b74af530ab08fa14cdc189247ba6284c21d3119769dc664fb50187e3b0c3e543dd74896d4c9ffc16b2b8cf4fb53bf5a18af8620b0eb78a816ea86d9141810ef7d55ad4b677e922f19621e7319fcd56343748eec49b91b037903c1856f0b238d546b98a7a82018ffebc253c2f357a9eeca307261a3b8e797f46521decbe87de36238c932e3535bb6587beba5b1f755be49354984808800faded6ee808bca2ea03fd6db0fe7a24cc579edafff4108fced1102a53f737866babffd53342dd437dc17aea6be025c0918388f4a0235a74c6d896aa800cdb278e903c54feb681042ccd20f8b83cf8a63a02a029185d90bb98bdc8a0918dc48ea0f4bfb341b2061e719967c7704ebe32d0708fb54fc46735c6c7585f4789751105fea692da4ac006dc103150790a5fb6ef3c3dd3fbb6d650afccf2e6bed69d131979f27b9ae31b5c775cab4ee20d1fa64fc12dc7ed8e72727f92f6a86ab5104c6d34d1c1c101175dfb1472ad6608fc674be7ec45dff91887b5a12b8f0648115bf30d53ae68999fc98697db00ca81a2e2f872dfc4985bac77bcdf9020fca8b3811f8aee296fb6b91875abd21f61cfcfc6038dabf2f904682ae310597c5806889aaec677624ee84ca82f739a135058b5338220d3bbc329aa607f60b783af7d22ab8fb6aa856b02e651287ae251ec748b3785afdb240675fba5208b96db496d9086df7fd1b0def9c27a892cd7ccd60281c3dceeddacf6de6c9870774bac14c542a4dfb2c016f7bd034ab40778d523e0e6a97373cf0fb301c1c505a4043312cfd94f77865a14ef33a520f08d093b775323165c81d581b58488531f596ef9222d1536f465fbf6161dd60d4b3fd13ffe7d508b68699d996d6d1c2b9460b60c5d9dea06401bbafde38866bf0af3d111c065e9d0c73a38b1dcdfa9a52c19efe8263349ec3f4fa4537282b6eca3a8ebc539a587b65375ae549ec6c0ba726ecc9f959dee32cc2d9c80100b4e95ae2c1323b65bd1b94a66079a06e5668d8a0570f3d1b3113a9ad92e8107be8438af8f815d2e545e17892b5655f5b98f925426ea1496ee7b797c8075851b5b60c2cbde78155cd07e40c86fd474a9f30cd677c8b4380afa68b1b928386824ba0415329f996a621c5e075474f0fff01dba751d1456fc1f53cba8afaa49fa2cde3f9c2fb5a3d3a3ad082aca7c7e6b5de5c324e793c06e85cd2e170e82ffa5d370f5a797eb92668137ffc681026d6299db5a0914290e8fe31ecb49c6d0eea3ce7e46d7678ad6dee6c7874f20408e4e82809a934839db1cc83cfae1d2e2ebbd74f421631993e8c063004f08b1303a20cb0067d3c226a09e1c30b52c0a184e818e846e762f001b5e9c24f13c643b2266e9f0ff3c6517b8c0d653054d60612a4ab5304e47fe17a33900e47d73905d89aa1e2498556bef719d95fe0c5666a3cd5f75e5bea918870839f8ab2619a0c63dd53b2ce5b85361bac2843a908db6d6fd4ab5152ae329edf892fb6a894fd13d5c789a1e242eb45506026b2333bf89127f95c1721e162759c73a8137ea720559822b108d7b5b116583de56187d8277e7e4c2dbeb130bbff29c7a112d9ee3099ca9b15c051a7854a763d2c3e453e808e229e250b7080a85cca2de94ce55350a62e4408aa788c59ed6a06480871630f457b4c1c9f13d40ae7323ac9130e9c802c8c6779290a18f37e41b30b0b3c8f8e40d1a574920095e6696f34e01ae6023081bc2ab3499759c4e2a4e4c8e918e4cb86f5d13868e7fea148cb781f4ae766e01d16072f98299ae045df8450e9a299d1b0b5a0c32b49d259d632818ffbb763209ddfc59723ecaddb226a6480d0f90335cc6740899a804658f06b3d1d4bdfe72088e0bf17aa773256ad41aaea6bbfeb31731ee4cfd57ad44747800c1514faee20060467b087dafc8af5bb190a184a397cfdb02e7be2abc79fac054c35f6be69503bcd5ffc822f2e31f3bf262e349a3ad60ae28eb1e75d80e85240728e6ed0a62015d0cd6b87bd2d0bbbdf30df2361df79c62efbc78742a5f6903e22c26d0731a06cf75d1b33f48f32a9421be4c0deb4c8810edd1ec40129a58334c16581a7d3109607b360008dedc4285117f7e05e717547f11bafbea0cc6051ad4642be577ca08357880402b7d3f18b743f2aac225b13a65f4196b120b3c38de93ca41b55e3f07

## olizax | 2018-08-23T10:23:07+00:00
The patch can't be applied:

➜  monero git:(release-v0.12) ✗ git apply ../bf0b3706

> fatal: patch fragment without header at line 14: @@ -208,6 +209,7 @@ namespace cryptonote

## moneromooo-monero | 2018-08-23T10:49:10+00:00
That's not a problem, the dump above helped, I see what the problem is, I'll post a possible fix asap.

## moneromooo-monero | 2018-08-23T10:59:06+00:00
Actually, I'll need more info. What commit hash are you running exactly so I can make the patch against that version ?

## olizax | 2018-08-23T11:00:50+00:00
a486cae407b109a7a95060daa85e4efed2046c01

tag: v0.12.3.0

## moneromooo-monero | 2018-08-23T13:57:10+00:00
Here's a patch in git format on the same commit, and with a bit more info.
http://paste.debian.net/hidden/e0e59936/

## olizax | 2018-08-24T03:36:09+00:00
These are the logs durning rescan_bc.

> 2018-08-24 02:51:45.453	    7fce5671a740	ERROR	net.http	src/cryptonote_basic/cryptonote_format_utils.h:175	obj_to_json_str failed: serialization::serialize returned false
2018-08-24 02:51:45.453	    7fce5671a740	INFO 	global	src/wallet/wallet2.cpp:1108	Processing tx 5e0faa9dc821cb558f0e10fbf0e810a95633366980508e991f644099c68b1b20 at height 1572290:
2018-08-24 02:51:45.453	    7fce5671a740	INFO 	global	src/wallet/wallet2.cpp:1147	Got pubkey: 4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11
2018-08-24 02:51:45.454	    7fce5671a740	INFO 	global	src/wallet/wallet2.cpp:1258	Got outs, pubkey 4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11
2018-08-24 02:51:45.454	    7fce5671a740	INFO 	global	src/wallet/wallet2.cpp:1288	Stored at 32 with pubkey 4c4ce6b845e705982d448ef05d6495cad2077abaa43077fb04b0f8bf3f5dea11, index 0
2018-08-24 02:51:45.454	    7fce5671a740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1324	Received money: 0.260000000000, with tx: 5e0faa9dc821cb558f0e10fbf0e810a95633366980508e991f644099c68b1b20
Height 1572290, txid 5e0faa9dc821cb558f0e10fbf0e810a95633366980508e991f644099c68b1b20, 0.260000000000, idx 0/0


> 2018-08-24 03:20:52.532	    7fce5671a740	ERROR	net.http	src/cryptonote_basic/cryptonote_format_utils.h:175	obj_to_json_str failed: serialization::serialize returned false
2018-08-24 03:20:52.532	    7fce5671a740	INFO 	global	src/wallet/wallet2.cpp:1108	Processing tx e5f0c0b1c482e036b8aa2a8cce3e6956a0a9959c0ee1304e28fbd40ca221efca at height 1632603:
2018-08-24 03:20:52.532	    7fce5671a740	INFO 	global	src/wallet/wallet2.cpp:1147	Got pubkey: b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000
2018-08-24 03:20:52.533	    7fce5671a740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1160	Failed to generate key derivation from tx pubkey, skipping
2018-08-24 03:20:52.534	    7fce5671a740	INFO 	global	src/wallet/wallet2.cpp:1258	Got outs, pubkey b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000
2018-08-24 03:20:52.534	    7fce5671a740	INFO 	global	src/wallet/wallet2.cpp:1288	Stored at 160 with pubkey b0a0e53bb655000001000000000000003052edf8b77f000001000000fd7f0000, index 0
2018-08-24 03:20:52.534	    7fce5671a740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1324	Received money: 0.010000000000, with tx: e5f0c0b1c482e036b8aa2a8cce3e6956a0a9959c0ee1304e28fbd40ca221efca
Height 1632603, txid e5f0c0b1c482e036b8aa2a8cce3e6956a0a9959c0ee1304e28fbd40ca221efca, 0.010000000000, idx 0/0

## moneromooo-monero | 2018-08-24T09:53:31+00:00
The problem was a bit more complex than I thought. http://paste.debian.net/hidden/aec4bd30/ might fix it. 

## moneromooo-monero | 2018-08-24T09:54:22+00:00
Do you know what software created that tx btw ? It included a bogus tx key, and duplicate additional keys, which also are in the main tx pub key. It's borked and wasteful.

## olizax | 2018-08-24T12:15:11+00:00
Yeah! It worked! Thank you very much! You are awesome!

Do't have a clue.. I only used cli and rpc wallet.

## moneromooo-monero | 2018-09-02T23:02:09+00:00
https://github.com/monero-project/monero/pull/4330

I hate it when I fix something then forget to PR it...

## moneromooo-monero | 2018-09-16T14:22:26+00:00
+resolved

## stoffu | 2018-10-25T11:51:45+00:00
Was the cause of that bogus tx key identified?

# Action History
- Created by: olizax | 2018-08-15T04:23:53+00:00
- Closed at: 2018-09-16T14:24:47+00:00
