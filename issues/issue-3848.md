---
title: in Monero-wallet-cli ERROR!!
source_url: https://github.com/monero-project/monero/issues/3848
author: workboy
assignees: []
labels: []
created_at: '2018-05-23T20:47:09+00:00'
updated_at: '2019-12-01T16:34:21+00:00'
type: issue
status: closed
closed_at: '2019-11-19T11:17:44+00:00'
---

# Original Description
I can't synchronize the balance of my wallet.


Starting refresh...
Error: refresh failed: internal error: Index out of bounds of hashchain. Blocks received: 0

VERSION : Monero 'Lithium Luna' (v0.12.0.0-master-release)

# Discussion History
## moneromooo-monero | 2018-05-23T21:15:58+00:00
0.12.1.0 is expected to fix this. It's just been tagged and binaries are on the way.


## moneromooo-monero | 2018-05-24T10:06:18+00:00
Actually, no it's not in 0.12.1.0, so much stuff is getting left unmerged that I end up with large piles of jumbled stuff, so the patch is in https://github.com/monero-project/monero/pull/3716/commits/9875f126bde384123458e9967a58652caf4dd437

## rothn | 2018-06-07T07:20:33+00:00
This happened to me! Does it mean my wallet keys are corrupted?!?!

## rothn | 2018-06-07T07:22:40+00:00
Just read the code. Looks like I'll just have to wait for this to be merged in 0.12.3.0 (hopefully) since it still affects 0.12.2.0.

## moneromooo-monero | 2018-06-07T12:25:06+00:00
I've ported the patch to current master, should also apply to the release branch: https://github.com/monero-project/monero/pull/3956

If you have a wallet with that problem, try this patch, and report whether it worked. Better to run monero-wallet-cli with --log-level 2 so you can post me a log in case it does not.

Do NOT run the master daemon if you want your blockchain to remain compatible with the release monero. Only monero-wallet-cli. Use the daemon you're using now.

To build only the wallet:
make -C build/release simplewallet

This will build monero-wallet-cli only (and its dependencies).




## rothn | 2018-06-30T05:56:24+00:00
I just cloned master and built the client. I'm getting the same error:

Monero 'Lithium Luna' (v0.12.2.0-master-a9b83f5a)
Logging to ./build/release/bin/monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): /Users/nroth/monero/default_wallet
Wallet and key files found, loading...
Wallet password: 
Opened wallet: <<<WITHHELD>>>
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Error: refresh failed: internal error: Index out of bounds of hashchain. Blocks received: 0
Background refresh thread started
[wallet <WITHHELD> (out of sync)]: 

## rothn | 2018-06-30T06:01:13+00:00
`2018-06-30 05:54:01.501	  0x7fffa1bcb380	INFO 	logging	contrib/epee/src/mlog.cpp:235	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-30 05:57:06.879	  0x7fffa1bcb380	INFO 	logging	contrib/epee/src/mlog.cpp:235	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-30 05:57:06.879	  0x7fffa1bcb380	INFO 	logging	contrib/epee/src/mlog.cpp:235	New log categories: *:DEBUG
2018-06-30 05:57:06.879	  0x7fffa1bcb380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

2018-06-30 05:57:06.880	  0x7fffa1bcb380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Monero 'Lithium Luna' (v0.12.2.0-master-a9b83f5a)
2018-06-30 05:57:06.880	  0x7fffa1bcb380	INFO 	wallet.wallet2	src/wallet/wallet_args.cpp:204	Setting log level = 2
2018-06-30 05:57:06.880	  0x7fffa1bcb380	INFO 	wallet.wallet2	src/wallet/wallet_args.cpp:207	Logging to: ./build/release/bin/monero-wallet-cli.log
2018-06-30 05:57:06.880	  0x7fffa1bcb380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Logging to ./build/release/bin/monero-wallet-cli.log
2018-06-30 05:57:20.361	  0x7fffa1bcb380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Wallet and key files found, loading...
2018-06-30 05:57:24.957	  0x7fffa1bcb380	DEBUG	device.ledger	src/device/device_ledger.cpp:223	Device 0 Created
2018-06-30 05:57:24.958	  0x7fffa1bcb380	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:5772	ringdb path set to /Users/nroth/.shared-ringdb
2018-06-30 05:57:25.021	  0x7fffa1bcb380	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3950	Loaded wallet keys file, with public address: <<<WITHHELD>>>
2018-06-30 05:57:25.022	  0x7fffa1bcb380	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:3970	Trying to decrypt cache data
2018-06-30 05:57:25.071	  0x7fffa1bcb380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4094	trimming to 1578999, offset 1578999
2018-06-30 05:57:25.071	  0x7fffa1bcb380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Opened wallet: <<<WITHHELD>>>
2018-06-30 05:57:25.071	  0x7fffa1bcb380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
2018-06-30 05:57:25.079	  0x7fffa1bcb380	DEBUG	net.http	src/common/util.cpp:834	Address 'http://localhost:18081' is local
2018-06-30 05:57:25.080	  0x7fffa1bcb380	INFO 	wallet.simplewallet	src/simplewallet/simplewallet.cpp:3239	Daemon is local, assuming trusted
2018-06-30 05:57:25.092	  0x7fffa1bcb380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Starting refresh...
2018-06-30 05:57:25.093	  0x7fffa1bcb380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1757	Daemon is recent enough, asking for pruned blocks
2018-06-30 05:57:25.167	  0x7fffa1bcb380	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1808	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-06-30 05:57:25.167	  0x700006abb000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1757	Daemon is recent enough, asking for pruned blocks
2018-06-30 05:57:25.167	  0x7fffa1bcb380	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/nroth/monero_git/src/wallet/wallet2.cpp:1808:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-06-30 05:57:25.233	  0x7fffa1bcb380	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2462	Another try pull_blocks (try_count=0)...
2018-06-30 05:57:25.233	  0x7fffa1bcb380	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1808	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-06-30 05:57:25.233	  0x7000083ca000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1757	Daemon is recent enough, asking for pruned blocks
2018-06-30 05:57:25.233	  0x7fffa1bcb380	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/nroth/monero_git/src/wallet/wallet2.cpp:1808:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-06-30 05:57:25.300	  0x7fffa1bcb380	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2462	Another try pull_blocks (try_count=1)...
2018-06-30 05:57:25.300	  0x7fffa1bcb380	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1808	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-06-30 05:57:25.300	  0x7fffa1bcb380	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/nroth/monero_git/src/wallet/wallet2.cpp:1808:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-06-30 05:57:25.300	  0x7000088cd000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1757	Daemon is recent enough, asking for pruned blocks
2018-06-30 05:57:25.368	  0x7fffa1bcb380	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2462	Another try pull_blocks (try_count=2)...
2018-06-30 05:57:25.368	  0x7fffa1bcb380	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1808	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-06-30 05:57:25.368	  0x7fffa1bcb380	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/nroth/monero_git/src/wallet/wallet2.cpp:1808:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-06-30 05:57:25.368	  0x7000074c1000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1757	Daemon is recent enough, asking for pruned blocks
2018-06-30 05:57:25.436	  0x7fffa1bcb380	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2467	pull_blocks failed, try_count=3
2018-06-30 05:57:25.437	  0x7fffa1bcb380	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:5806	clearing ringdb key
2018-06-30 05:57:25.437	  0x7fffa1bcb380	ERROR	wallet.simplewallet	src/simplewallet/simplewallet.cpp:4037	internal error: /Users/nroth/monero_git/src/wallet/wallet2.cpp:1808:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-06-30 05:57:25.437	  0x7fffa1bcb380	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: refresh failed: internal error: Index out of bounds of hashchain. Blocks received: 0
2018-06-30 05:57:25.437	  0x7fffa1bcb380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Background refresh thread started
2018-06-30 05:57:25.437	  0x700008950000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1757	Daemon is recent enough, asking for pruned blocks
2018-06-30 05:57:25.518	  0x700008950000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1808	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-06-30 05:57:25.518	  0x700008950000	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/nroth/monero_git/src/wallet/wallet2.cpp:1808:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-06-30 05:57:25.518	  0x7000074c1000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1757	Daemon is recent enough, asking for pruned blocks
2018-06-30 05:57:25.585	  0x700008950000	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2462	Another try pull_blocks (try_count=0)...
2018-06-30 05:57:25.585	  0x700008950000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1808	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-06-30 05:57:25.585	  0x700008950000	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/nroth/monero_git/src/wallet/wallet2.cpp:1808:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-06-30 05:57:25.585	  0x700007ec7000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1757	Daemon is recent enough, asking for pruned blocks
2018-06-30 05:57:25.650	  0x700008950000	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2462	Another try pull_blocks (try_count=1)...
2018-06-30 05:57:25.650	  0x700008950000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1808	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-06-30 05:57:25.650	  0x700008950000	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/nroth/monero_git/src/wallet/wallet2.cpp:1808:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-06-30 05:57:25.650	  0x7000074c1000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1757	Daemon is recent enough, asking for pruned blocks
2018-06-30 05:57:25.717	  0x700008950000	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2462	Another try pull_blocks (try_count=2)...
2018-06-30 05:57:25.717	  0x700008950000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1808	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-06-30 05:57:25.717	  0x700008950000	WARN 	net.http	src/wallet/wallet_errors.h:794	/Users/nroth/monero_git/src/wallet/wallet2.cpp:1808:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-06-30 05:57:25.718	  0x700006fbe000	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1757	Daemon is recent enough, asking for pruned blocks
2018-06-30 05:57:25.785	  0x700008950000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2467	pull_blocks failed, try_count=3
2018-06-30 05:57:25.786	  0x700008950000	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:5806	clearing ringdb key
2018-06-30 05:57:37.011	  0x7fffa1bcb380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:4094	trimming to 1578999, offset 1578999
2018-06-30 05:57:37.055	  0x7fffa1bcb380	DEBUG	device.ledger	src/device/device_ledger.cpp:228	Device 0 Destroyed
`

## rothn | 2018-06-30T06:02:47+00:00
Needless to say, I'm very concerned about my money. EDIT: Maybe concerned is the wrong word, since I didn't invest enough to be "concerned." Annoyed is more appropriate.

## moneromooo-monero | 2018-06-30T09:34:36+00:00
Timely. The prerequisites for my fix are now in master, so it now applies: https://github.com/monero-project/monero/pull/4087

Try this, and let me know if it works for you since I can't test.

Warning: if you're on 0.12.2.0, build only the simplewallet from this, as the daemon code changes the database format and you can't use 0.12.2.0 again if you do this. You should be able to use the wallet from this branch plus the daemon from 0.12.2.0.


## rothn | 2018-07-02T01:10:09+00:00
This PR has not yet been merged. That said, I checked it out and tried it. I opened the client 3 different times. The first time, it died due to a segmentation fault 1172. The second time, it stayed out-of-sync after "Starting refresh..." with Error: refresh failed: internal error: wrong daemon response: split starts from the first block in response. The third time, it worked.

## moneromooo-monero | 2018-07-02T10:12:50+00:00
I don't suppose you could share the wallet+cache that causes this for testing ?
ie, you could recreate from seed, move your coins away, encrypt keys/cache with my key and upload to github so I could test the patch.

## lejeczek | 2018-07-03T20:31:19+00:00
When will it be in the master? I did git clone today and I get the same error.

## moneromooo-monero | 2018-07-03T22:36:01+00:00
When I can get a test case to test with, where the patch doesn't work.

I managed to get a wallet in one of these cases today, and the patch worked on it.


## lejeczek | 2018-07-04T07:08:24+00:00
Maybe it would be possible to replicate the problem - I was on 0.11.x which worked without any problems but I had my wallet(+monerod) lagged behind and then I was looking at rate-limits which did not work I thought, I am not sure if everything synced at the time I upgraded to 0.12.0 hoping rate limits would work and then noticed those errors.

## lejeczek | 2018-07-06T11:49:41+00:00
hi, guys, being an amateur - how would I pull that specific commit using git tool(command line)? Many thanks, L. 

## moneromooo-monero | 2018-07-06T12:16:39+00:00
git branch test4087 master
git checkout test4087
git fetch origin pull/4087/head:pr4087
git cherry-pick pr4087

When you want to go back to master:
git checkout master

## lejeczek | 2018-07-10T15:25:58+00:00
hi, when I build then:
...
[ 58%] Building CXX object tests/fuzz/CMakeFiles/load-from-binary_fuzz_tests.dir/load_from_binary.cpp.o
Scanning dependencies of target load-from-json_fuzz_tests
make[3]: Leaving directory '/home/rpmbuild/gits/monero/build/release'
make[3]: Entering directory '/home/rpmbuild/gits/monero/build/release'
[ 59%] Building CXX object tests/fuzz/CMakeFiles/load-from-json_fuzz_tests.dir/load_from_json.cpp.o
[ 59%] Building CXX object tests/fuzz/CMakeFiles/load-from-binary_fuzz_tests.dir/fuzzer.cpp.o
[ 59%] Building CXX object tests/fuzz/CMakeFiles/load-from-json_fuzz_tests.dir/fuzzer.cpp.o
[ 59%] Linking CXX executable load-from-binary_fuzz_tests
cc1plus: all warnings being treated as errors
make[3]: *** [src/wallet/CMakeFiles/obj_wallet.dir/build.make:63: src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o] Error 1
make[3]: Leaving directory '/home/rpmbuild/gits/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:2227: src/wallet/CMakeFiles/obj_wallet.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
make[3]: Leaving directory '/home/rpmbuild/gits/monero/build/release'
[ 59%] Built target load-from-binary_fuzz_tests
[ 59%] Linking CXX executable load-from-json_fuzz_tests
make[3]: Leaving directory '/home/rpmbuild/gits/monero/build/release'
[ 59%] Built target load-from-json_fuzz_tests
make[2]: Leaving directory '/home/rpmbuild/gits/monero/build/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/home/rpmbuild/gits/monero/build/release'
make: *** [Makefile:73: release-all] Error 2

If you need me to gather more info then please let me know what/how.

## moneromooo-monero | 2018-07-11T15:02:00+00:00
Include the actual error too, not just the end of the log.

## lejeczek | 2018-07-11T16:53:35+00:00
How do I do that? What I pasted is the output of shell terminal from: make -j3
Do you mean some log files where is more info?

## moneromooo-monero | 2018-07-12T11:36:00+00:00
Are you *really* sure there was no output before what you pasted ?

## rothn | 2018-07-12T18:48:46+00:00
The PR does solve the problem. I'm sorry that I don't want to give out my wallet address, but it could possibly cause problems for me if I did.

Best of luck though!

## moneromooo-monero | 2018-07-12T21:44:08+00:00
Thanks for letting me know. I don't need a wallet which my patch fixes, only one it does not :)

## lejeczek | 2018-07-13T12:15:00+00:00
I've pasted only the bits from which errors started to appear, so I think, I'll paste the whole output soon again.

## moneromooo-monero | 2018-07-13T23:37:55+00:00
Very unlikely, given the output there. There was a previous error in wallet2.cpp which does not appear on the log excerpt. It could also be an OOM, there'd be a Killed message though.

## lejeczek | 2018-07-16T10:31:55+00:00
But there is "Error 1" and "Error 2" in my output snipped.
Here is another run, difference: now - make vs previous - make -j3

make[3]: Leaving directory '/home/rpmbuild/gits/monero/build/release'
make[3]: Entering directory '/home/rpmbuild/gits/monero/build/release'
[ 58%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
/home/rpmbuild/gits/monero/src/wallet/wallet2.cpp: In member function ‘void tools::wallet2::refresh(bool, uint64_t, uint64_t&, bool&)’:
/home/rpmbuild/gits/monero/src/wallet/wallet2.cpp:2453:36: error: catching polymorphic type ‘const struct tools::error::out_of_hashchain_bounds_error’ by value [-Werror=catch-value=]
         catch (const tools::error::out_of_hashchain_bounds_error)
                                    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cc1plus: all warnings being treated as errors
make[3]: *** [src/wallet/CMakeFiles/obj_wallet.dir/build.make:63: src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o] Error 1
make[3]: Leaving directory '/home/rpmbuild/gits/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:2227: src/wallet/CMakeFiles/obj_wallet.dir/all] Error 2
make[2]: Leaving directory '/home/rpmbuild/gits/monero/build/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/home/rpmbuild/gits/monero/build/release'
make: *** [Makefile:73: release-all] Error 2

Should I paste complete output here or maybe send it directly over to you somehow?

## moneromooo-monero | 2018-07-16T22:14:36+00:00
Right, that's the error here.

I updated the patch in 4087, which should fix this.


## lejeczek | 2018-07-18T12:41:55+00:00
many!! thanks. It builds okey now.
I start my wallet and this shows:

Starting refresh...
Error: refresh failed: internal error: wrong daemon response: split starts from the first block in response 3b8cf4465c835e964c1f9691ff199bf80c6632230c3a1072f36eb550d8722b02 (height 1578999), local block id at this height: a151c5014256f8caf097551f90c5ce472bd8597bd2bef9973f7690db01c02371. Blocks received: 0
Background refresh thread started

So, different problem. That is, if it is a problem indeed?

## moneromooo-monero | 2018-07-18T14:15:57+00:00
Please redo this with --log-level 2, and paste that log to fpaste.org or paste.debian.net.
If you want that log kept confidential since it will have info about your txes, you can compress it and encrypt it with my GPG pubkey (utils/gpg_keys/moneromooo.asc) and paste the result as above.

## lejeczek | 2018-07-20T10:15:32+00:00
Could it be that it was caused by the fact that dir in which tools reside was not writeable to the process owner?
I've changed that now and when I start wallet - that was when the error popped out, just after start - I do not get that error any more.

## moneromooo-monero | 2018-07-20T13:36:31+00:00
That should not be a problem.

## lejeczek | 2018-07-20T16:21:50+00:00
It definitely was that. Wallet could not create log file in that dir, since I changed it it modified/updated wallet file(that file named after my wallet name) and now it works without errors. Absolutely nothing else was changed.

## moneromooo-monero | 2018-07-20T17:31:17+00:00
So if you set to read only again, it causes the error again ?

## vijayr2410 | 2018-08-01T17:02:02+00:00
@moneromooo-monero - I am still seeing the error. I used the the latest 0.12.0.3 release to sync the daemon and the start the cli-wallet. 


**Monero>monero-wallet-cli.exe** 
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on an another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

**Monero 'Lithium Luna' (v0.12.3.0-release)**

**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
**Starting refresh...
Error: refresh failed: internal error: Index out of bounds of hashchain. Blocks received: 0**
Background refresh thread started
[wallet 43YVuz (out of sync)]:
_______________________________________________________________________________________
I also see the same errors in the **monero-wallet-rpc**:

**Monero>monero-wallet-rpc.exe** 
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.3.0-release)
Logging to C:\CoinClients\Monero\monero-wallet-rpc.log
2018-08-01 16:17:39.990 5508    WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:2956   Loading wallet...
2018-08-01 16:17:40.568 5508    WARN    wallet.wallet2  src/wallet/wallet2.cpp:3783     Loaded wallet keys file, with public address: 43YVuzk1oSp.......................
2018-08-01 16:17:41.209 5508    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1736     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-08-01 16:17:41.209 5508    WARN    net.http        src/wallet/wallet_errors.h:794  C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1736:N5tools5error21wallet_internal_errorE: Index out of bou
nds of hashchain
2018-08-01 16:17:41.303 5508    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1736     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-08-01 16:17:41.303 5508    WARN    net.http        src/wallet/wallet_errors.h:794  C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1736:N5tools5error21wallet_internal_errorE: Index out of bou
nds of hashchain
2018-08-01 16:17:41.412 5508    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1736     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-08-01 16:17:41.412 5508    WARN    net.http        src/wallet/wallet_errors.h:794  C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1736:N5tools5error21wallet_internal_errorE: Index out of bou
nds of hashchain
2018-08-01 16:17:41.491 5508    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1736     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-08-01 16:17:41.491 5508    WARN    net.http        src/wallet/wallet_errors.h:794  C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1736:N5tools5error21wallet_internal_errorE: Index out of bou
nds of hashchain
2018-08-01 16:17:41.568 5508    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2329     pull_blocks failed, try_count=3
**2018-08-01 16:17:41.568 5508    ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:2998   Wallet initialization failed: Index out of bounds of hashchain**

## moneromooo-monero | 2018-08-02T18:14:49+00:00
Is this a wallet you can share the keys/cache ?

## moneromooo-monero | 2018-08-04T12:46:02+00:00
Try https://github.com/monero-project/monero/pull/4221

## vijayr2410 | 2018-08-13T13:57:46+00:00
@moneromooo-monero - is it possible to get a windows build of #4221? Thank you!

## moneromooo-monero | 2018-08-14T14:57:44+00:00
https://build.getmonero.org/downloads/monero-3f6abde8-win64.tar.gz, through the win64 build bot, linked from the bottom of the bug page.

## vijayr2410 | 2018-08-21T20:52:13+00:00
@moneromooo-monero - Thank you!. I still get the following error (can you please help):
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.3.0-master-3f6abde8)
Logging to C:\Monero\monero-wallet-rpc.log
2018-08-21 20:49:34.235 6456    WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3197   Loading wallet...
2018-08-21 20:49:34.423 6456    WARN    wallet.wallet2  src/wallet/wallet2.cpp:4009     Loaded wallet keys file, with public address:
PVTX8k4tLuhcEyyni46WXWE3YQymt
2018-08-21 20:49:34.610 6456    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1825     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2018-08-21 20:49:34.610 6456    WARN    net.http        src/wallet/wallet_errors.h:805  C:/msys64/home/vagrant/slave/monero-static-win64/build/src/wallet/wallet2.cpp:1825:N5tools5error29out_of_hashcha
in_bounds_errorE: Index out of bounds of of hashchain
2018-08-21 20:49:38.438 6456    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1935     current_index == start_height. THROW EXCEPTION: error::wallet_internal_error
2018-08-21 20:49:38.438 6456    WARN    net.http        src/wallet/wallet_errors.h:805  C:/msys64/home/vagrant/slave/monero-static-win64/build/src/wallet/wallet2.cpp:1935:N5tools5error21wallet_interna
l_errorE: wrong daemon response: split starts from the first block in response 3b8cf4465c835e964c1f9691ff199bf80c6632230c3a1072f36eb550d8722b02 (height 1578999), local block id at this height: a151c50
14256f8caf097551f90c5ce472bd8597bd2bef9973f7690db01c02371
2018-08-21 20:49:40.266 6456    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1935     current_index == start_height. THROW EXCEPTION: error::wallet_internal_error
2018-08-21 20:49:40.266 6456    WARN    net.http        src/wallet/wallet_errors.h:805  C:/msys64/home/vagrant/slave/monero-static-win64/build/src/wallet/wallet2.cpp:1935:N5tools5error21wallet_interna
l_errorE: wrong daemon response: split starts from the first block in response 3b8cf4465c835e964c1f9691ff199bf80c6632230c3a1072f36eb550d8722b02 (height 1578999), local block id at this height: a151c50
14256f8caf097551f90c5ce472bd8597bd2bef9973f7690db01c02371
2018-08-21 20:49:42.172 6456    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1935     current_index == start_height. THROW EXCEPTION: error::wallet_internal_error
2018-08-21 20:49:42.189 6456    WARN    net.http        src/wallet/wallet_errors.h:805  C:/msys64/home/vagrant/slave/monero-static-win64/build/src/wallet/wallet2.cpp:1935:N5tools5error21wallet_interna
l_errorE: wrong daemon response: split starts from the first block in response 3b8cf4465c835e964c1f9691ff199bf80c6632230c3a1072f36eb550d8722b02 (height 1578999), local block id at this height: a151c50
14256f8caf097551f90c5ce472bd8597bd2bef9973f7690db01c02371
2018-08-21 20:49:42.189 6456    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2516     pull_blocks failed, try_count=3
2018-08-21 20:49:42.204 6456    ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:3239   Wallet initialization failed: wrong daemon response: split starts from the first block in response 3b8cf

## moneromooo-monero | 2018-08-22T09:58:41+00:00
That doesn't seem to have the previous patch in. I rebased to current master, there should be a new build linked from #4221 in a couple hours.

## vijayr2410 | 2018-08-22T14:12:56+00:00
@moneromooo-monero - would you be able to share the latest windows build with that patch? Thank you. Also, any thoughts on when this patch be part of an official release?

## moneromooo-monero | 2018-08-22T15:36:14+00:00
As I said, the build bot will make one whenever it gets to it, it'll be linked from the bug page.

## moneromooo-monero | 2018-08-22T15:37:16+00:00
It seems to be done, and links to https://build.getmonero.org/downloads/monero-62511df6-win64.tar.gz

## moneromooo-monero | 2018-08-28T20:44:47+00:00
Did it work ?

## vijayr2410 | 2018-09-07T18:22:45+00:00
@moneromooo-monero - apologies for the delayed response. We are still facing issues only for one wallet. We have other wallets running the  v0.12.3.0 and haven't seen this error, so not sure what is happening

## moneromooo-monero | 2018-09-09T10:07:23+00:00
Are the issues for that one wallet the ones in this bug ?

## vijayr2410 | 2018-09-12T14:42:39+00:00
Yes this is the only wallet that is throwing the error. Index out of bounds
Please find below the error:

```
Monero 'Lithium Luna' (v0.12.3.0-master-62511df6)
Logging to C:\CoinClients\Monero\monero-wallet-rpc.log
2018-09-12 14:35:28.443 3680    WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3259   Loading wallet...
2018-09-12 14:35:28.786 3680    WARN    wallet.wallet2  src/wallet/wallet2.cpp:4019     Loaded wallet keys file, with public address: 43YVuzk1oSpY2mBALahfKTWdXyTT8axNBg1pjJTfQtcgivMsM2nrwuD1whXPUz7Wxe
PVTX8k4tLuhcEyyni46WXWE3YQymt
2018-09-12 14:35:31.184 3680    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1835     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2018-09-12 14:35:31.184 3680    WARN    net.http        src/wallet/wallet_errors.h:805  C:/msys64/home/vagrant/slave/monero-static-win64/build/src/wallet/wallet2.cpp:1835:N5tools5error29out_of_hashcha
in_bounds_errorE: Index out of bounds of of hashchain
2018-09-12 14:36:01.454 3680    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1945     current_index == start_height. THROW EXCEPTION: error::wallet_internal_error
2018-09-12 14:36:01.454 3680    WARN    net.http        src/wallet/wallet_errors.h:805  C:/msys64/home/vagrant/slave/monero-static-win64/build/src/wallet/wallet2.cpp:1945:N5tools5error21wallet_interna
l_errorE: wrong daemon response: split starts from the first block in response 3b8cf4465c835e964c1f9691ff199bf80c6632230c3a1072f36eb550d8722b02 (height 1578999), local block id at this height: a151c50
14256f8caf097551f90c5ce472bd8597bd2bef9973f7690db01c02371
2018-09-12 14:36:04.298 3680    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1945     current_index == start_height. THROW EXCEPTION: error::wallet_internal_error
2018-09-12 14:36:04.298 3680    WARN    net.http        src/wallet/wallet_errors.h:805  C:/msys64/home/vagrant/slave/monero-static-win64/build/src/wallet/wallet2.cpp:1945:N5tools5error21wallet_interna
l_errorE: wrong daemon response: split starts from the first block in response 3b8cf4465c835e964c1f9691ff199bf80c6632230c3a1072f36eb550d8722b02 (height 1578999), local block id at this height: a151c50
14256f8caf097551f90c5ce472bd8597bd2bef9973f7690db01c02371
2018-09-12 14:36:06.345 3680    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1945     current_index == start_height. THROW EXCEPTION: error::wallet_internal_error
2018-09-12 14:36:06.345 3680    WARN    net.http        src/wallet/wallet_errors.h:805  C:/msys64/home/vagrant/slave/monero-static-win64/build/src/wallet/wallet2.cpp:1945:N5tools5error21wallet_interna
l_errorE: wrong daemon response: split starts from the first block in response 3b8cf4465c835e964c1f9691ff199bf80c6632230c3a1072f36eb550d8722b02 (height 1578999), local block id at this height: a151c50
14256f8caf097551f90c5ce472bd8597bd2bef9973f7690db01c02371
2018-09-12 14:36:06.360 3680    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2526     pull_blocks failed, try_count=3
2018-09-12 14:36:06.360 3680    ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:3301   Wallet initialization failed: wrong daemon response: split starts from the first block in response 3b8cf
4465c835e964c1f9691ff199bf80c6632230c3a1072f36eb550d8722b02 (height 1578999), local block id at this height: a151c5014256f8caf097551f90c5ce472bd8597bd2bef9973f7690db01c02371
```

## moneromooo-monero | 2018-09-12T19:24:17+00:00
That doesn't seem to be running with the patch, does it ?

## CodeForcer | 2018-09-26T09:43:09+00:00
I am getting the same issue, downloaded the latest software only a couple days ago. Ran Monerod as a service to expose the daemon, created a fresh wallet with monero-wallet-cli, and then tried to expose the RPC wallet:
```
monero-wallet-rpc --wallet-file testwallet --password "password" --rpc-bind-port 18082 --disable-rpc-login --daemon-login username:password --log-level 2
```
Result:
```
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.3.0-release)
2018-09-26 09:42:19.351	    7f7a2ecad740	INFO 	wallet.wallet2	src/wallet/wallet_args.cpp:196	Setting log level = 2
2018-09-26 09:42:19.351	    7f7a2ecad740	INFO 	wallet.wallet2	src/wallet/wallet_args.cpp:199	Logging to: monero-wallet-rpc.log
Logging to monero-wallet-rpc.log
2018-09-26 09:42:19.352	    7f7a2ecad740	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:2956	Loading wallet...
2018-09-26 09:42:19.352	    7f7a2ecad740	DEBUG	device.ledger	src/device/device_ledger.cpp:225	Device 0 Created
2018-09-26 09:42:19.389	    7f7a2ecad740	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:5552	ringdb path set to /home/ubuntu/.shared-ringdb
2018-09-26 09:42:20.275	    7f7a2ecad740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3783	Loaded wallet keys file, with public address: 46Un9ZY5qDoDXMAs1u57oPG3a5AEGZ8TiLATX2NSib67KNk4hrGYAWrQNy85NJjdsBiXN1ggqLrBVTLMVAZoSbahMucxgnC
2018-09-26 09:42:20.276	    7f7a2ecad740	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:3802	Trying to decrypt cache data
2018-09-26 09:42:21.276	    7f7a2ecad740	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:3927	trimming to 1578999, offset 1578999
2018-09-26 09:42:21.277	    7f7a2ecad740	DEBUG	net.http	contrib/epee/include/net/http_client.h:365	Reconnecting...
2018-09-26 09:42:21.444	    7f7a2ecad740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2144	Blocks start before blockchain offset: 0 1578999
2018-09-26 09:42:21.485	    7f7a2ecad740	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1685	Daemon is recent enough, asking for pruned blocks
2018-09-26 09:42:21.916	    7f7a2daa0700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1685	Daemon is recent enough, asking for pruned blocks
2018-09-26 09:42:21.934	    7f7a2ecad740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1736	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-09-26 09:42:21.934	    7f7a2ecad740	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1736:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-09-26 09:42:22.325	    7f7a2ecad740	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2324	Another try pull_blocks (try_count=0)...
2018-09-26 09:42:22.325	    7f7a2ecad740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1736	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-09-26 09:42:22.325	    7f7a2ecad740	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1736:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-09-26 09:42:22.364	    7f7a2daa0700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1685	Daemon is recent enough, asking for pruned blocks
2018-09-26 09:42:22.774	    7f7a2ecad740	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2324	Another try pull_blocks (try_count=1)...
2018-09-26 09:42:22.775	    7f7a2ecad740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1736	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-09-26 09:42:22.775	    7f7a2ecad740	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1736:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-09-26 09:42:22.814	    7f7a2daa0700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1685	Daemon is recent enough, asking for pruned blocks
2018-09-26 09:42:23.204	    7f7a2ecad740	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2324	Another try pull_blocks (try_count=2)...
2018-09-26 09:42:23.204	    7f7a2ecad740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1736	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
2018-09-26 09:42:23.204	    7f7a2ecad740	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1736:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
2018-09-26 09:42:23.248	    7f7a2daa0700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1685	Daemon is recent enough, asking for pruned blocks
2018-09-26 09:42:23.621	    7f7a2ecad740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2329	pull_blocks failed, try_count=3
2018-09-26 09:42:23.621	    7f7a2ecad740	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:2998	Wallet initialization failed: Index out of bounds of hashchain
2018-09-26 09:42:23.659	    7f7a2ecad740	DEBUG	device.ledger	src/device/device_ledger.cpp:230	Device 0 Destroyed
```

Is there any solution for this issue or is the wallet RPC unusable at the moment? For my purposes I need the wallet RPC and cannot suffice with GUI's

## vijayr2410 | 2018-09-26T13:24:47+00:00
> That doesn't seem to be running with the patch, does it ?

@moneromooo-monero - I did run both the patches that you sent me the links to. It seems to be an issue with the wallet. I guess it was a wallet that was created with the old version. 
Is it a known issue in case of wallet generated using the 0.11 version when used against the latest?

## moneromooo-monero | 2018-09-26T14:12:29+00:00
CodeForcer, this does not have the patch. You seem to have downloaded a release binary, which is too old. 0.13.x.y binaries will be available soon, and will include the patch.

vijay2410, a wallet generated with 0.11 is compatible with the latest code, except bugs, which we will fix. In your log, you get a out_of_hashchain_bounds_error exception, but you don't get the message which should follow it ("Daemon claims next refresh block is out of hash chain bounds, resetting hash chain"). Maybe since this is an INFO message, your log level simply silenced it. Can you try again with --log-level 1, which will catch that message ? If it appears, it looks like there's still a bug. If it does not appear, then you're not running with the patches.

## vijayr2410 | 2018-09-26T16:13:06+00:00
@moneromooo-monero : I will set the loglevel to 1 and let you know the results.

## CodeForcer | 2018-09-26T17:21:58+00:00
> CodeForcer, this does not have the patch. You seem to have downloaded a release binary, which is too old. 0.13.x.y binaries will be available soon, and will include the patch.

I've tried to compile the source code after following the exact instructions from README.md but the compile fails. I'm installing on fresh Ubuntu server OS and installed all listed dependencies first:
```
[ 78%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/wipeable_string.cpp.o
In file included from /usr/include/gtest/gtest.h:58:0,
                 from /home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:31:
/home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp: In member function ‘virtual void wipeable_string_parse_hexstr_Test::TestBody()’:
/home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:197:3: error: no matching function for call to ‘testing::AssertionResult::AssertionResult(boost::optional<epee::wipeable_string>&)’
   ASSERT_TRUE((s = epee::wipeable_string("").parse_hexstr()));
   ^
In file included from /home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:31:0:
/usr/include/gtest/gtest.h:262:12: note: candidate: testing::AssertionResult::AssertionResult(bool)
   explicit AssertionResult(bool success) : success_(success) {}
            ^
/usr/include/gtest/gtest.h:262:12: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘bool’
/usr/include/gtest/gtest.h:260:3: note: candidate: testing::AssertionResult::AssertionResult(const testing::AssertionResult&)
   AssertionResult(const AssertionResult& other);
   ^
/usr/include/gtest/gtest.h:260:3: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘const testing::AssertionResult&’
In file included from /usr/include/gtest/gtest.h:58:0,
                 from /home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:31:
/home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:199:3: error: no matching function for call to ‘testing::AssertionResult::AssertionResult(boost::optional<epee::wipeable_string>&)’
   ASSERT_TRUE((s = epee::wipeable_string("00").parse_hexstr()));
   ^
In file included from /home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:31:0:
/usr/include/gtest/gtest.h:262:12: note: candidate: testing::AssertionResult::AssertionResult(bool)
   explicit AssertionResult(bool success) : success_(success) {}
            ^
/usr/include/gtest/gtest.h:262:12: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘bool’
/usr/include/gtest/gtest.h:260:3: note: candidate: testing::AssertionResult::AssertionResult(const testing::AssertionResult&)
   AssertionResult(const AssertionResult& other);
   ^
/usr/include/gtest/gtest.h:260:3: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘const testing::AssertionResult&’
In file included from /usr/include/gtest/gtest.h:58:0,
                 from /home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:31:
/home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:201:3: error: no matching function for call to ‘testing::AssertionResult::AssertionResult(boost::optional<epee::wipeable_string>&)’
   ASSERT_TRUE((s = epee::wipeable_string("41").parse_hexstr()));
   ^
In file included from /home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:31:0:
/usr/include/gtest/gtest.h:262:12: note: candidate: testing::AssertionResult::AssertionResult(bool)
   explicit AssertionResult(bool success) : success_(success) {}
            ^
/usr/include/gtest/gtest.h:262:12: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘bool’
/usr/include/gtest/gtest.h:260:3: note: candidate: testing::AssertionResult::AssertionResult(const testing::AssertionResult&)
   AssertionResult(const AssertionResult& other);
   ^
/usr/include/gtest/gtest.h:260:3: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘const testing::AssertionResult&’
In file included from /usr/include/gtest/gtest.h:58:0,
                 from /home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:31:
/home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:203:3: error: no matching function for call to ‘testing::AssertionResult::AssertionResult(boost::optional<epee::wipeable_string>&)’
   ASSERT_TRUE((s = epee::wipeable_string("414243").parse_hexstr()));
   ^
In file included from /home/ubuntu/monero/tests/unit_tests/wipeable_string.cpp:31:0:
/usr/include/gtest/gtest.h:262:12: note: candidate: testing::AssertionResult::AssertionResult(bool)
   explicit AssertionResult(bool success) : success_(success) {}
            ^
/usr/include/gtest/gtest.h:262:12: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘bool’
/usr/include/gtest/gtest.h:260:3: note: candidate: testing::AssertionResult::AssertionResult(const testing::AssertionResult&)
   AssertionResult(const AssertionResult& other);
   ^
/usr/include/gtest/gtest.h:260:3: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘const testing::AssertionResult&’
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1310: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/wipeable_string.cpp.o' failed
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/wipeable_string.cpp.o] Error 1
make[3]: Leaving directory '/home/ubuntu/monero/build/Linux/release-v0.13/release'
CMakeFiles/Makefile2:4568: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/home/ubuntu/monero/build/Linux/release-v0.13/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/ubuntu/monero/build/Linux/release-v0.13/release'
Makefile:85: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

## moneromooo-monero | 2018-09-27T10:18:32+00:00
That's fixed in https://github.com/monero-project/monero/pull/4424.

## CodeForcer | 2018-09-27T14:29:48+00:00
Ok, so following your instructions I rebuilt new binaries from the latest source code and tried again. However, I'm now getting a similar error:
```
ubuntu@ip-172-16-10-90:/usr/bin$ sudo monero-wallet-rpc --wallet-file testwallet2 --password "password" --rpc-bind-port 18082 --disable-rpc-login --daemon-login user:password
2018-09-27 14:27:27,519 INFO  [default] Page size: 4096
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Beryllium Bullet' (v0.13.0.1-rc-release)
Logging to monero-wallet-rpc.log
2018-09-27 14:27:28.522	    7f7195ee7bc0	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:3346	Loading wallet...
2018-09-27 14:27:28.653	    7f7195ee7bc0	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:4341	Loaded wallet keys file, with public address: 46FgTQSyfGzME2YgLFMmDUVadQoSd6sfi1uLVAL7chrzdynRpxnkusYhgwiF5ddnhe2V48djPEzPiSBt7aCcfA5S8qTakQX
2018-09-27 14:27:29.262	    7f7195ee7bc0	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2464	Blocks start before blockchain offset: 0 1668900
2018-09-27 14:27:29.338	    7f7195ee7bc0	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1983	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2018-09-27 14:27:34.709	    7f7195ee7bc0	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2644	m_blockchain.size() != stop_height. THROW EXCEPTION: error::wallet_internal_error
```

## moneromooo-monero | 2018-09-27T22:58:59+00:00
<s>Add "--log-level 1" please.</s> Nevermind, not needed, that last log line helps.

## moneromooo-monero | 2018-09-27T23:05:58+00:00
Please apply this patch (save as FILENAME, then "patch -p1 < FILENAME"), and run with --log-level 1 and paste the logs:

<pre>
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index 7517884..eff176a 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -2641,6 +2641,9 @@ void wallet2::refresh(bool trusted_daemon, uint64_t start_height, uint64_t & blo
           short_chain_history.clear();
           get_short_chain_history(short_chain_history);
           fast_refresh(stop_height, blocks_start_height, short_chain_history, true);
+MGINFO("m_blockchain.size(): " << m_blockchain.size());
+MGINFO("stop_height: " << stop_height);
+MGINFO("m_blockchain.offset(): " << m_blockchain.offset());
           THROW_WALLET_EXCEPTION_IF(m_blockchain.size() != stop_height, error::wallet_internal_error, "Unexpected hashchain size");
           THROW_WALLET_EXCEPTION_IF(m_blockchain.offset() != 0, error::wallet_internal_error, "Unexpected hashchain offset");
           for (const auto &h: tip)
</pre>

## moneromooo-monero | 2018-09-27T23:07:33+00:00
Also, was your daemon running at the time ? If so, was it synced ? If not, how far off was it ?


## CodeForcer | 2018-09-28T07:14:23+00:00
Happy to report that I got it working. I deleted the old data and resynced the Blockchain with the new daemon, then set up a new wallet with monero-wallet-cli, and then ran the daemon on a new port with:
```
sudo monero-wallet-rpc --wallet-file testwallet --password "walletpassword" --rpc-bind-port 18083 --disable-rpc-login --daemon-login usernme:password --log-level 2
```

Then while running the RPC service I was able to communicate with it from a seperate process:
```
curl -u username:password --digest -X POST http://127.0.0.1:18083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_balance","params":{"account_index":0,"address_indices":[0,1]}}' -H 'Content-Type: application/json'
```
Result:
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "balance": 0,
    "multisig_import_needed": false,
    "per_subaddress": [{
      "address": "46Un9ZY5qDoDXMAs1u57oPG3a5AEGZ8TiLATX2NSib67KNk4hrGYAWrQNy85NJjdsBiXN1ggqLrBVTLMVAZoSbahMucxgnC",
      "address_index": 0,
      "balance": 0,
      "label": "Primary account",
      "num_unspent_outputs": 0,
      "unlocked_balance": 0
    },{
      "address": "842Nogm5AonJ3d6RSDUaUqhg8NK5YS2TaHbE16mQ9JMLBitxdinsdMcMfJpbF5uczWByx527rP7T2jagUCtaWDoyBDuUVzg",
      "address_index": 1,
      "balance": 0,
      "label": "",
      "num_unspent_outputs": 0,
      "unlocked_balance": 0
    }],
    "unlocked_balance": 0
  }
}
```

A small recommendation, it might be useful to create some documentation for new users on the process of setting up the RPC server, including running the daemon & RPC as a service, and also setting up the wallet separately to the RPC server. As someone with technical experience I found this process non-trivial even with direct help from the developers, I imagine many newbies would try and give up.

## moneromooo-monero | 2018-09-28T16:50:43+00:00
Great. So the wallet could not reload the hash chain because the daemon could not supply the data.

Do you want to writeup those instructions from your experience ? It could be added to getmonero.org's doc section,


## mmortal03 | 2018-10-08T00:45:28+00:00
@CodeForcer , what was the cause of this bug? Can it be considered fixed?

## lessless | 2019-01-20T11:24:36+00:00
It's also present in `monero-wallet-rpc` 

```
monero-wallet-rpc  --testnet --trusted-daemon --wallet-file wallets/b1fded9f-129d-47ce-bbe7-cd0765c3d8f9/b1fded9f-129d-47ce-bbe7-cd0765c3d8f9 --rpc-bind-port 40404 --prompt-for-password  
2019-01-20 11:18:55,856 INFO  [default] Page size: 4096
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Beryllium Bullet' (v0.13.0.4-release)
Logging to monero-wallet-rpc.log
2019-01-20 11:18:56.860	     0x10454f5c0	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:3400	Loading wallet...
Wallet password: 
2019-01-20 11:18:57.950	     0x10454f5c0	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:4590	Loaded wallet keys file, with public address: A2hY1CXDTA56ViFu74ZkVxegsy19y4A6eK6qoy6Uaume67GBEAMK2bqXGr82e79KZgcAH2DmDM1oYJ2p4hv4J7Ru5UTUgpd
2019-01-20 11:18:58.020	     0x10454f5c0	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2537	Blocks start before blockchain offset: 0 1058600
2019-01-20 11:18:58.070	     0x10454f5c0	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2056	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2019-01-20 11:18:58.385	     0x10454f5c0	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2717	m_blockchain.size() != stop_height. THROW EXCEPTION: error::wallet_internal_error
2019-01-20 11:18:58.387	  0x70000e150000	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:1094	Failed to parse block from blob
2019-01-20 11:18:58.387	  0x70000e653000	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:1094	Failed to parse block from blob

< line repeats 100s times or so >
 
2019-01-20 11:19:00.960	     0x10454f5c0	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:225	RPC username/password is stored in file monero-wallet-rpc.40404.login
2019-01-20 11:19:00.960	     0x10454f5c0	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:40404
2019-01-20 11:19:00.962	     0x10454f5c0	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:3453	Starting wallet RPC server
2019-01-20 11:19:20.988	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2537	Blocks start before blockchain offset: 0 1058600
2019-01-20 11:19:21.049	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2056	!m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2019-01-20 11:19:21.422	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2717	m_blockchain.size() != stop_height. THROW EXCEPTION: error::wallet_internal_error
```

Got it twice in a row, in one blockchain created from scratch after another

## moneromooo-monero | 2019-01-20T13:05:37+00:00
https://github.com/monero-project/monero/pull/5084 might fix it.

## KushGoyal | 2019-04-16T08:53:36+00:00
I received the below error:

`Error: refresh failed: internal error: Index out of bounds of hashchain. Blocks received: 0`

this happens with the latest baron butterfly version.

I am using ledger wallet. This error comes when an output is found.

## dEBRUYNE-1 | 2019-04-16T09:32:55+00:00
@KushGoyal - That issue should be fixed in master. Have you tried compiling a binary from master and using that? 

## KushGoyal | 2019-05-07T15:05:35+00:00
@dEBRUYNE-1 I couldn't build the binary. Do you know when will this fix be released? Without this fix I cannot access my ledger wallet. Thanks.

## dEBRUYNE-1 | 2019-05-07T17:19:22+00:00
There will be a release soonish. 

## jonathancross | 2019-11-12T15:23:14+00:00
@KushGoyal Have you tried the latest v0.15.0.0 ?

**To all:** Does it still make sense to keep this thread open considering it seems to be just a jumble of (somewhat unrelated) cli issues in different releases?

## moneromooo-monero | 2019-11-19T11:13:44+00:00
I think this can be closed, the hash chain thing got fixed ages ago. Any further bug can be opened separately.

+resolved


## n0n0n0n0 | 2019-12-01T16:19:03+00:00
same error for me
```

2019-12-01 16:18:21.308	E Blocks start before blockchain offset: 0 1958000
2019-12-01 16:18:22.003	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2019-12-01 16:18:22.435	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2019-12-01 16:18:42.834	E Blocks start before blockchain offset: 0 1958000
2019-12-01 16:18:43.671	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2019-12-01 16:18:44.118	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error

```
latest monero from site

## n0n0n0n0 | 2019-12-01T16:34:20+00:00
in monero-wallet-rpc

# Action History
- Created by: workboy | 2018-05-23T20:47:09+00:00
- Closed at: 2019-11-19T11:17:44+00:00
