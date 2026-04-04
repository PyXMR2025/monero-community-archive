---
title: RPC transfer fails with 16 char payment / No strict check on payment_id
source_url: https://github.com/monero-project/monero/issues/1764
author: gituser
assignees: []
labels: []
created_at: '2017-02-21T19:05:55+00:00'
updated_at: '2017-02-22T12:49:05+00:00'
type: issue
status: closed
closed_at: '2017-02-22T12:49:05+00:00'
---

# Original Description
Hi.

Using monero `Monero 'Wolfram Warptangent' (v0.10.1.0-release)`
I've been testing sending via transfer on the testnet (same as on the mainnet)  via RPC:

First payment_id: `547f5c650f87e291` (16 chars) it doesn't work:

```
$ curl -X POST http://127.0.0.1:28081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"destinations":[{"amount":100000000,"address":"xxx"}],"payment_id":"547f5c650f87e291","new_algorithm":true, "mixin":4,"get_tx_key": true}}' -H 'Content-Type: application/json'
{
  "error": {
    "code": -5,
    "message": "Payment id has invalid format: \"547f5c650f87e291\", expected 16 or 64 character string"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```

Now If I set payment_id to `547f5c650f87e291547f5c650f87e291547f5c650f` (64 chars) it works:

```
$ curl -X POST http://127.0.0.1:28081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"destinations":[{"amount":100000000,"address":"xxx"}],"payment_id":"547f5c650f87e291547f5c650f87e291547f5c650f87e291547f5c650f87e291","new_algorithm":true, "mixin":4,"get_tx_key": true}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "fee": 32611408063,
    "tx_hash": "zzz",
    "tx_key": "yyyy"
  }
}
```

Interestingly though it works fine via console:

```
[wallet dddd]:  transfer 4 xxx 0.0001 547f5c650f87e291
Sending 0.000100000000.  The transaction fee is 0.032611221461.
Is this okay?  (Y/Yes/N/No): y
Money successfully sent, transaction <yyyyy>
````

Also there is a bug (I think) if I set payment_id to some random non-hex string the payment still goes through but it has '000000000' identifier in the incoming payments. The payment_id check should be more strict imo:

```
curl -X POST http://127.0.0.1:28081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"destinations":[{"amount":100000000,"address":"xxx"}],"payment_id":"blablabla", "mixin":4,"get_tx_key": true}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "fee": 32611159269,
    "tx_hash": "xxxx",
    "tx_key": "yyyy"
  }
}
```

And in show_transfers:

```
  pool     in      07:04:14 PM       0.000100000000 xxxx 0000000000000000 -
```

Thanks.

# Discussion History
## gituser | 2017-02-21T19:13:53+00:00
I've looked src code briefly, maybe there is a typo:

```
diff --git a/src/wallet/wallet_rpc_server.cpp b/src/wallet/wallet_rpc_server.cpp
index 33e099c..d35e510 100644
--- a/src/wallet/wallet_rpc_server.cpp
+++ b/src/wallet/wallet_rpc_server.cpp
@@ -369,7 +369,7 @@ namespace tools
         cryptonote::set_payment_id_to_tx_extra_nonce(extra_nonce, long_payment_id);
       }
       /* or short payment ID */
-      else if (!wallet2::parse_short_payment_id(payment_id_str, short_payment_id)) {
+      else if (wallet2::parse_short_payment_id(payment_id_str, short_payment_id)) {
         cryptonote::set_encrypted_payment_id_to_tx_extra_nonce(extra_nonce, short_payment_id);
       }
       else {
```

Didn't try yet, just something for you to look at.

## ghost | 2017-02-21T20:44:11+00:00
Would you mind testing against current master to see if this is still an issue? I believe it was addressed a little while back.

## moneromooo-monero | 2017-02-21T21:00:55+00:00
I fixed that a couple weeks ago.

## gituser | 2017-02-21T21:02:43+00:00
Good to know. I'll test against latest master and report back.

Is latest master is considered stable?

Thanks.

## gituser | 2017-02-21T21:07:46+00:00
Found your commit - https://github.com/monero-project/monero/commit/8c8482ac981204634d2332b5414fef572749402c

Guess this issue can be closed.

Is there any plans on new release?

## moneromooo-monero | 2017-02-21T21:17:44+00:00
Sometime today.

## gituser | 2017-02-21T21:24:11+00:00
are you serious? :)

tried to build master seems it's failing for me (boost v1.62.0):

```
[ 98%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_export.dir/blocksdat_file.cpp.o
Linking CXX executable ../../bin/monero-blockchain-export
/home/build/monero/source/src/blockchain_utilities/bootstrap_file.cpp: In member function 'seek_to_first_chunk':
/home/build/monero/source/src/blockchain_utilities/bootstrap_file.cpp:368:3: warning: 'MEM[(unsigned char &)&bfi + 1]' may be used uninitialized in this function [-Wmaybe-uninitialized]
   MINFO("bootstrap file v" << unsigned(bfi.major_version) << "." << unsigned(bfi.minor_version));
   ^
/home/build/monero/source/src/blockchain_utilities/bootstrap_file.cpp:365:24: note: 'MEM[(unsigned char &)&bfi + 1]' was declared here
   bootstrap::file_info bfi;
                        ^
/home/build/monero/source/external/easylogging++/easylogging++.h:5113:21: warning: 'MEM[(unsigned int &)&bfi + 4]' may be used uninitialized in this function [-Wmaybe-uninitialized]
                     m_messageBuilder << log;
                     ^
/home/build/monero/source/src/blockchain_utilities/bootstrap_file.cpp:365:24: note: 'MEM[(unsigned int &)&bfi + 4]' was declared here
   bootstrap::file_info bfi;
                        ^
/tmp/ccpjchYR.ltrans24.ltrans.o:(.rodata._ZZN5boost9function2INS_14iterator_rangeIN9__gnu_cxx17__normal_iteratorIPcSsEEEES5_S5_E9assign_toINS_9algorithm6detail13token_finderFINSA_10is_any_ofFIcEEEEEEvT_E13stored_vtable[_ZZN5boost9function2INS_14iterator_rangeIN9__gnu_cxx17__normal_iteratorIPcSsEEEES5_S5_E9assign_toINS_9algorithm6detail13token_finderFINSA_10is_any_ofFIcEEEEEEvT_E13stored_vtable]+0x0): multiple definition of `void boost::function2<boost::iterator_range<__gnu_cxx::__normal_iterator<char*, std::string> >, __gnu_cxx::__normal_iterator<char*, std::string>, __gnu_cxx::__normal_iterator<char*, std::string> >::assign_to<boost::algorithm::detail::token_finderF<boost::algorithm::detail::is_any_ofF<char> > >(boost::algorithm::detail::token_finderF<boost::algorithm::detail::is_any_ofF<char> >)::stored_vtable'
/home/build/monero/boost/boost.build/lib/libboost_thread.a(thread.o):(.rodata._ZZN5boost9function2INS_14iterator_rangeIN9__gnu_cxx17__normal_iteratorIPcSsEEEES5_S5_E9assign_toINS_9algorithm6detail13token_finderFINSA_10is_any_ofFIcEEEEEEvT_E13stored_vtable[_ZZN5boost9function2INS_14iterator_rangeIN9__gnu_cxx17__normal_iteratorIPcSsEEEES5_S5_E9assign_toINS_9algorithm6detail13token_finderFINSA_10is_any_ofFIcEEEEEEvT_E13stored_vtable]+0x0): first defined here
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/blockchain_export.dir/build.make:164: recipe for target 'bin/monero-blockchain-export' failed
make[3]: *** [bin/monero-blockchain-export] Error 1
make[3]: Leaving directory '/home/build/monero/source/build/release'
CMakeFiles/Makefile2:1749: recipe for target 'src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all' failed
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all] Error 2
make[2]: Leaving directory '/home/build/monero/source/build/release'
Makefile:127: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/build/monero/source/build/release'
Makefile:62: recipe for target 'release-static' failed
make: *** [release-static] Error 2
Build Failed.
```


## moneromooo-monero | 2017-02-21T21:36:09+00:00
OK, maybe tomorrow. Try without LTO (-D USE_LTO=OFF in Makefile)

## gituser | 2017-02-21T22:45:54+00:00
OK, now it's compiled.

I've tried using it with my older wallets it seems simplewallet segfaults. Guess I need to regenerate them..

Is it normal that with each new release you break wallet's metadata? Maybe there should be some mechanism which checks wallet metadata version (e.g. with which version it was created) and migrate it if neccessary automatically to the new format.

## moneromooo-monero | 2017-02-21T23:23:02+00:00
simplewallet should NOT segfault (though it might throw an exception). Though simplewallet is the old name, so make sure you're not using an old version. The new name is monero-wallet-cli.

New released should not break metadata, but there are known issues with boost versions, which do. Since the problem seems to be in boost's serialization support, we can't migrate since we can only link to one boost version. This is unfortnuate, but hopefully a thing of the past, since we now use a portable (hopefully) new boost format.


## gituser | 2017-02-21T23:39:35+00:00
I'm sorry for the words misusage of course I meant monero-wallet-rpc binary.

Well, I had to re-create the wallet to start it it didn't work otherwise and yes I'm using the same version for both monerod and monero-wallet-rpc. I can reproduce it again If you like on my old wallet and paste logs here.

EDIT: hm, yes seems you're right it's not segfaulting, I've just tried to run it with my old wallets directory. But it uses unportable wallet? 

```
2017-02-22 02:51:37.875	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:119	Exception: boost::archive::portable_binary_iarchive_exception
2017-02-22 02:51:37.875	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Unwound call stack:
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [1] /home/monero/current/monero-wallet-rpc:__wrap___cxa_throw+0x78 [0x814da8]
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [2] /home/monero/current/monero-wallet-rpc() [0x749522]
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [3] /home/monero/current/monero-wallet-rpc() [0x6efc1e]
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [4] /home/monero/current/monero-wallet-rpc:boost::archive::basic_binary_iprimitive<boost::archive::portable_binary_iarchive, char, std::char_traits<char> >::load(std::string&)+0x1d [0x74a2cd]
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [5] /home/monero/current/monero-wallet-rpc:boost::archive::portable_binary_iarchive::portable_binary_iarchive(std::istream&, unsigned int)+0x6a [0x74f81a]
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [6] /home/monero/current/monero-wallet-rpc:tools::wallet2::load(std::string const&, std::string const&)+0xa87 [0x7025b7]
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [7] /home/monero/current/monero-wallet-rpc:tools::wallet2::make_from_file(boost::program_options::variables_map const&, std::string const&)+0xca [0x7037ea]
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [8] /home/monero/current/monero-wallet-rpc:main+0x571 [0x6640f1]
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [9] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf5 [0x7f818e52cb45]
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [10] /home/monero/current/monero-wallet-rpc() [0x66f0cc]
2017-02-22 02:51:37.877	    7f818f1ee740	INFO 	stacktrace	src/common/stack_trace.cpp:158	
2017-02-22 02:51:37.877	    7f818f1ee740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2374	Failed to open portable binary, trying unportable
```
Also I'm getting this now: https://github.com/monero-project/monero/issues/1769 so can't really test RPC to make a transfer.

Boost is v1.62.0 the same I've compiled monero v0.10.1.0-release.

## moneromooo-monero | 2017-02-22T09:38:06+00:00
That exception is in fact expected. It tries the new format, and if not, tries the old one. When it saves, it will be the new format.

If the daemon's busy, wait for it to be done syncing. If it's synced, paste the output of "status" in monerod.

## gituser | 2017-02-22T12:48:30+00:00
@moneromooo-monero the daemon was in sync I pasted earlier logs from the daemon in the log it said it's synced (see https://github.com/monero-project/monero/issues/1769).

I can't type status in the daemon because it's running in the background. Maybe only via RPC?

I had to rollback to 0.10.1-release with your commit https://github.com/monero-project/monero/commit/8c8482ac981204634d2332b5414fef572749402c to get Monero working again.

I'll try again on the fresh VM with new master and see if it works.

## gituser | 2017-02-22T12:49:05+00:00
This issue is actually fixed, so let's not spend anymore time here creating offtopic.

# Action History
- Created by: gituser | 2017-02-21T19:05:55+00:00
- Closed at: 2017-02-22T12:49:05+00:00
