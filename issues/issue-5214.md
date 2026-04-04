---
title: Latest wallet win cli cannot transfer fund while last version worked, should
  I wait until hf complete?
source_url: https://github.com/monero-project/monero/issues/5214
author: x151973
assignees: []
labels: []
created_at: '2019-03-03T01:01:52+00:00'
updated_at: '2019-03-08T22:16:21+00:00'
type: issue
status: closed
closed_at: '2019-03-08T22:16:21+00:00'
---

# Original Description
v0.13.0.4 worked
Latest win v0.14.0.0-release not work, recovered from 25 mem seeds

```
monero-wallet-cli.exe
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Boron Butterfly' (v0.14.0.0-release)
Logging to monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): xxx
Wallet and key files found, loading...
Wallet password:
Opened wallet: 4xxxmaskxxxE
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Error: wallet failed to connect to daemon: http://localhost:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
Background refresh thread started
[wallet xxx(no daemon)]: set_daemon uwillrunanodesoon.moneroworld.com:18089
Daemon set to uwillrunanodesoon.moneroworld.com:18089, untrusted
[wallet xxx]: refresh
Starting refresh...
Refresh done, blocks received: 0
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: xxx, unlocked balance: xxx
[wallet xxx]: status
Refreshed 1783150/1783150, synced, daemon RPC v2.1
[wallet xxx]: transfer unimportant addressmask 0.001
Wallet password:

Transaction 1/1:
Spending from address index 0
Sending 0.001000000000.  The transaction fee is 0.000036410000
Is this okay?  (Y/Yes/N/No): Y
**Error: transaction <mask> was rejected by daemon with status: Failed
Error: There was an error, which could mean the node may be trying to get you to retry creating a transaction, and zero in on which outputs you own. Or it could be a bona fide error. It may be prudent to disconnect from this node, and not try to send a transaction immediately. Alternatively, connect to another node so the original node cannot correlate information.**
```

# Discussion History
## moneromooo-monero | 2019-03-03T09:34:30+00:00
Run again with --log-level 1, there will be more information in the log about why it failed.

## x151973 | 2019-03-03T11:42:29+00:00


<details><summary>CLICK ME</summary>
<p>



```Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
2019-03-03 11:20:03.308	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Warning: using an untrusted daemon at 47.90.35.145:18081, privacy will be lessened
2019-03-03 11:20:04.214	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Starting refresh...
2019-03-03 11:20:06.318	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2398	Found new pool tx: <89188bcaf2379a0bd5bfe80e063a3805cf524b1935fa1799a76cf80b7349eb2c>
2019-03-03 11:20:06.318	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2398	Found new pool tx: <ca88ea41b33dad965c3b1dc427455bb9f36c5b3950b97e2582b769b57fac2af9>
2019-03-03 11:20:06.568	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2788	Refresh done, blocks received: 0, balance (all accounts): 0.013515183000, unlocked: 0.013515183000
2019-03-03 11:20:06.569	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Refresh done, blocks received: 0
2019-03-03 11:20:06.571	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Untagged accounts:
2019-03-03 11:20:06.573	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	          Account               Balance      Unlocked balance                 Label
2019-03-03 11:20:06.575	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	 *       0 42yQye        0.013515183000        0.013515183000       Primary account
2019-03-03 11:20:06.576	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	----------------------------------------------------------------------------------
2019-03-03 11:20:06.577	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	          Total        0.013515183000        0.013515183000
2019-03-03 11:20:06.580	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Currently selected account: [0] Primary account
2019-03-03 11:20:06.582	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Tag: (No tag assigned)
2019-03-03 11:20:06.594	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Balance: 0.013515183000, unlocked balance: 0.013515183000
2019-03-03 11:20:06.596	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Background refresh thread started
2019-03-03 11:20:08.744	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2788	Refresh done, blocks received: 0, balance (all accounts): 0.013515183000, unlocked: 0.013515183000
2019-03-03 11:21:40.696	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2398	Found new pool tx: <36942f28153ba2e6a041d77e760894ab5dc61ca55b4bfbcb73f47715d43f5186>
2019-03-03 11:21:40.941	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2788	Refresh done, blocks received: 0, balance (all accounts): 0.013515183000, unlocked: 0.013515183000
2019-03-03 11:23:12.674	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2398	Found new pool tx: <c5220befd9c0b2e3aa93c46c68e5978dc28cc496249e32ef7f63701ab3fb5d6e>
2019-03-03 11:23:12.674	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2398	Found new pool tx: <f6623649dd57b8acd38f03ba53402e51e7e839b09bf6905abc0d517225ede779>
2019-03-03 11:23:12.930	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2788	Refresh done, blocks received: 0, balance (all accounts): 0.013515183000, unlocked: 0.013515183000
2019-03-03 11:24:44.289	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2398	Found new pool tx: <da76df6fbd400f8b7b0a2b3530f975344fa71ea8a31d3f238fe8ba22da9f7527>
2019-03-03 11:24:44.289	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2398	Found new pool tx: <cbdcac91104da9e927bb20f8a9caa59a50b028919359670fdbc6e461fcfc4c46>
2019-03-03 11:24:44.290	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2398	Found new pool tx: <f9695d0479a393ff136ba06d41f59954a3d6f7f8027df15d20f6efe47fd203d7>
2019-03-03 11:24:44.541	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2788	Refresh done, blocks received: 1, balance (all accounts): 0.013515183000, unlocked: 0.013515183000
2019-03-03 11:26:16.294	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2788	Refresh done, blocks received: 0, balance (all accounts): 0.013515183000, unlocked: 0.013515183000
2019-03-03 11:27:48.294	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2788	Refresh done, blocks received: 1, balance (all accounts): 0.013515183000, unlocked: 0.013515183000
2019-03-03 11:28:44.239	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Starting refresh...
2019-03-03 11:28:45.127	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2398	Found new pool tx: <1728620b9a7b739d73dbecd5d8d0af124d167205e5effb66d78c94e66c54979f>
2019-03-03 11:28:45.385	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2788	Refresh done, blocks received: 0, balance (all accounts): 0.013515183000, unlocked: 0.013515183000
2019-03-03 11:28:45.386	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Refresh done, blocks received: 0
2019-03-03 11:28:45.388	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Currently selected account: [0] Primary account
2019-03-03 11:28:45.389	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Tag: (No tag assigned)
2019-03-03 11:28:45.390	51560	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Balance: 0.013515183000, unlocked balance: 0.013515183000
2019-03-03 11:28:47.120	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2788	Refresh done, blocks received: 0, balance (all accounts): 0.013515183000, unlocked: 0.013515183000
2019-03-03 11:29:06.392	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:8478	Found preferred rct inputs for rct tx: 39 (0.013515183000) 
2019-03-03 11:29:06.415	54076	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2019-03-03 11:29:06.415	54076	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2019-03-03 11:29:10.611	51560	WARN 	net.dns	src/common/dns_utils.cpp:519	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2019-03-03 11:29:11.896	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:6903	8552024 unlocked rct outputs
2019-03-03 11:29:11.896	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:6928	Fake output makeup: 67 requested: 0 recent, 0 pre-fork, 0 post-fork, 67 full-chain
2019-03-03 11:29:11.897	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:6989	Selecting real output: 8972174 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 7707021 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 7799106 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8022359 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8152659 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8173763 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8185216 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8189987 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8285390 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8388560 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8406902 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8413377 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8419556 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8445928 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8465432 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8470349 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8474712 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8485375 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8492332 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8506751 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8507923 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8509185 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8511410 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8514578 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8516131 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8517615 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8518311 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8522208 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8524816 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8526299 for 0.000000000000
2019-03-03 11:29:11.902	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8526603 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8528749 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8533282 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8535438 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8536241 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8537575 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8540829 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8541517 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8541901 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8542696 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8543946 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8544474 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8544807 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8546463 for 0.000000000000
2019-03-03 11:29:11.912	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8546533 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8546809 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8547469 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8547479 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8547883 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8548036 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8548828 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8548839 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8549583 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8549716 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8550109 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8550171 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8550194 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8550289 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8550501 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8550631 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8550792 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8550838 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8550866 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8551114 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8551618 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8551726 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8551751 for 0.000000000000
2019-03-03 11:29:11.913	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:7111	asking for output 8972174 for 0.000000000000
2019-03-03 11:29:12.094	51560	WARN 	wallet.wallet2	src/wallet/wallet2.h:1847	amount=0.013515183000, real_output=10, real_output_in_tx_index=0, indexes: 8189987 8413377 8474712 8492332 8507923 8509185 8547883 8548036 8550194 8551726 8972174 
2019-03-03 11:29:12.097	51560	INFO 	default	src/cryptonote_core/cryptonote_tx_utils.cpp:256	Encrypted payment ID: <182be13a9f058f40>
2019-03-03 11:29:12.107	51560	INFO 	perf	src/common/perf_timer.cpp:111	PERF             ----------
2019-03-03 11:29:12.107	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF     1149    PROVE_v
2019-03-03 11:29:12.802	51560	INFO 	bulletproofs	src/ringct/bulletproofs.cc:170	Hi/Gi cache size: 64 kB
2019-03-03 11:29:12.802	51560	INFO 	bulletproofs	src/ringct/bulletproofs.cc:171	Hi_p3/Gi_p3 cache size: 320 kB
2019-03-03 11:29:12.802	51560	INFO 	bulletproofs	src/ringct/bulletproofs.cc:172	Straus cache size: 300 kB
2019-03-03 11:29:12.802	51560	INFO 	bulletproofs	src/ringct/bulletproofs.cc:173	Pippenger cache size: 320 kB
2019-03-03 11:29:12.802	51560	INFO 	bulletproofs	src/ringct/bulletproofs.cc:175	Total cache size: 1004kB
2019-03-03 11:29:12.807	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF     4442      PROVE_v
2019-03-03 11:29:12.807	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF       44      PROVE_aLaR
2019-03-03 11:29:12.879	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF    71844      PROVE_step1
2019-03-03 11:29:12.886	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF     6068      PROVE_step2
2019-03-03 11:29:13.015	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF   129783      PROVE_step3
2019-03-03 11:29:13.828	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF   813112      PROVE_step4
2019-03-03 11:29:13.873	51560	INFO 	construct_tx	src/cryptonote_core/cryptonote_tx_utils.cpp:596	transaction_created: <cfe0c1100035d01ecb782bf7df273f1e3837a182ad564adfef8c7a645cdb6f04>
{
  "version": 2, 
  "unlock_time": 0, 
  "vin": [ {
      "key": {
        "amount": 0, 
        "key_offsets": [ 8189987, 223390, 61335, 17620, 15591, 1262, 38698, 153, 2158, 1532, 420448
        ], 
        "k_image": "9f7dde726affcadd7006dac7bc05a98abd5b4c6c9c72611a21c3b43cfccee4ee"
      }
    }
  ], 
  "vout": [ {
      "amount": 0, 
      "target": {
        "key": "795034d7f47ec64dbde44438af1a2be01f98e6e94674dd1620fa43e14b704612"
      }
    }, {
      "amount": 0, 
      "target": {
        "key": "feb195a99c661f90bbbea2943fcc0c72dfcbbc66f978343d5fedadfb4f1e98a7"
      }
    }
  ], 
  "extra": [ 2, 9, 1, 24, 43, 225, 58, 159, 5, 143, 64, 1, 85, 208, 143, 192, 145, 113, 234, 133, 36, 213, 58, 189, 9, 219, 17, 187, 15, 60, 249, 43, 73, 64, 167, 92, 223, 2, 47, 4, 156, 94, 112, 110
  ], 
  "rct_signatures": {
    "type": 4, 
    "txnFee": 38211745, 
    "ecdhInfo": [ {
        "amount": "e3883f828a607453"
      }, {
        "amount": "83f6dbc8c88812ba"
      }], 
    "outPk": [ "cef0582684e4ae9c9e53ef34cb4a90eb143a654a4df7b1863bde6c60d7cff3f1", "3e1400bb7956fb88d67819c17e2174fa8a1eb42591bde32bcd359a97fe749fa1"]
  }, 
  "rctsig_prunable": {
    "nbp": 1, 
    "bp": [ {
        "A": "5f15dc8e25405c1b16712266835a02f980684de9fb528987b220fc65df71cec2", 
        "S": "6bbbb9590f1004b99b350ffd43293ed064fcaf4b26592859c6be934a1a77e7cb", 
        "T1": "88c676ca678028cc8cbb313516e56c22a77451333a37a58725d6207863bf6e48", 
        "T2": "837aa74ac976feb2eda65b1adb395e86da44742e26f9e2ef1e9bfe16e5c72a9c", 
        "taux": "52ff8ea40a9a968b86ed8111142e63c9442e50874cbc0bb31938a3725b1cba04", 
        "mu": "83bb0b174e9a7a522511e036be9a712c9634606c51c594430ea5d1b4eb60fc0b", 
        "L": [ "12b05684e92f3953bad737548eaf89ade2c88a9c1eb57a85f8e464366c180497", "5e7172750707fb6dbe0d2eac6362c719082ef3f19d5242da9bc6e7757fe41cb7", "c322426314ddfcf7b48af2c9080c6f4f7ab81d79d0d90a69807de18772e753c1", "7ad472605d011ec5c9fb90380a123eb673dd592fd4c5befb8d2c64dc3a13a725", "c9b2eb505df968dd45e3afccf6b41f2094ca1fe8d4a3657eba3c64e10da696e8", "2ba55b07e835066ae49436c5fc0976160c4b86d0faec64d6c2a42684b67ef2f3", "3f860f5c3dde0fa28e98f98a1c4eb79f64130eb0c33ee3575ceeb95060cd6567"
        ], 
        "R": [ "8c969f4086582c57024b0d6cea71d7d66245cb81162185503000093ec25ae7aa", "ea0aec00fb869bbf8b28ca04427ee8aeea6899e40719e6442f34b103713c016f", "b4dc5eee398845c7f2a9ac9316550bc04958ab59e191ed6d2be91a257e7c6a4b", "349cf567fb6202cb42ab459b3a7b0d4081f23a466bd1ff2661471258214014e3", "eb959c9fbddfb6f385b96052bfafd6e3f97f524a31f2288c9df6e1ac65b3dd99", "e6c848c417459e3d090bc1303ef1f9129701f3c9e20bb62add73abfaa0edbd06", "48b731d44c7d5ae2ca6cc10a1eb299aa14e6ef7ec365795e468f30fb906f27c0"
        ], 
        "a": "4b3c3d3744fb82dfe40df15fec869191970925a8b20619766f6116e282f4430b", 
        "b": "a3aab23818c94b13f9718433ae7246892ffaa2997a522df8709daadb89bffb03", 
        "t": "c947a4d00cc61a86c47609ee7cd255a59accf331b1bcd233803d1a51a24d8508"
      }
    ], 
    "MGs": [ {
        "ss": [ [ "33dac0738b45f533242bb86ca5aff113a3e247b96669a7f2d884ac5d8fc3bc07", "d04817bf3bd0b0a9920c8ef200063844ba5d2160c4e6d5a3f23180e66f34c500"], [ "cdd4d9e9157d2126e18b6cca41b5b5ffe62ba4eb281043c6c080379b1657be0f", "dc9a3c9d333358ece82dd78bafd8853e19b5049352a6b2e275cb04ad86d32702"], [ "95e3fe9681b9fd09b26aae4c90a966801062bc07476a18494375e201cf27a80f", "45ead504c579bb9b7be62448ea3dbe1e89e9fbc900d7ac027abc5e4607b0370b"], [ "66d3bba13d2c575500f1d82ac2cbdafc3a107a0a1876338a162db674cf4e180d", "909f2212f459e23b99d76d1cb129df7747a951e0cedaf17909affc830f65dc0e"], [ "097c1b0db920808cf6b44790e79fccf822315598871410a3117fb46aa1110f0a", "4bda9bcc929f2fa8c87e32905ee95ec325e3efa6e7b1fdc12767c8357b607104"], [ "8074914c96ec20d1f57d424f1156cf0e9248237265e72a77d3fa0a08b5ba990b", "9f9780e99eacb1e59b2dbe0811aa9f1da89e5865a35dd59ea259df2644b31405"], [ "80b0ae3ec5d2dec7e64e7352fb07498e8a9f9751aad7fa188bd11bfa38d9d202", "59047a1c2fc285e9070088011b781cac2c4d93a11bfe045e447775e24979fb0c"], [ "3cb8e1de6e400311d2bcc4be76416b2bc98fb36a90655db1d07eddd7ee218802", "bbc82944345f6b233297afd62d06d46597c551dfd75b0cba254fc4f89a409a09"], [ "ba99de31cf26a7375df00e97f193755a46b74ba68cd981563f1dbde86b5e2f0c", "89fd0da941c4533efd803f3681468da495a1aa3a51bfe2b4ca591bb5e64d070e"], [ "dfce610cde97b85dfda10ada9b8387ed6a6f49247734606ed84e759b20ca6a0c", "1b276775e9c51a2e4a379cc5d9704c353b5a79587acaa4e42aeb6a4c61e2df03"], [ "b9ec9440e3d0fa49fd318b39413f6c379890987bc9dbbb6d010dda4853031603", "8a6b99ef1540364d95fef6af7575872e42ae3ff9b007aeb4e81a30210a46290f"]], 
        "cc": "8d9bd37da9ebc398405ab28b57e912af67e98a5832ed57aba7c5106d58bc660e"
      }], 
    "pseudoOuts": [ "6e62800e17d5e330bae864258b33a3e11a9a754d7505c6b72047f4548ad67dd5"]
  }
}

2019-03-03 11:29:13.874	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:8737	Done creating 1 transactions, 0.000038211745 total fee, 0.012476971255 total change
2019-03-03 11:29:13.876	51560	WARN 	wallet.wallet2	src/wallet/wallet2.h:1847	amount=0.013515183000, real_output=10, real_output_in_tx_index=0, indexes: 8189987 8413377 8474712 8492332 8507923 8509185 8547883 8548036 8550194 8551726 8972174 
2019-03-03 11:29:13.878	51560	INFO 	default	src/cryptonote_core/cryptonote_tx_utils.cpp:256	Encrypted payment ID: <ef5bacf637dd2317>
2019-03-03 11:29:13.887	51560	INFO 	perf	src/common/perf_timer.cpp:111	PERF             ----------
2019-03-03 11:29:13.887	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF      127    PROVE_v
2019-03-03 11:29:13.891	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF     3875      PROVE_v
2019-03-03 11:29:13.891	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF       45      PROVE_aLaR
2019-03-03 11:29:13.963	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF    72173      PROVE_step1
2019-03-03 11:29:13.969	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF     5806      PROVE_step2
2019-03-03 11:29:14.100	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF   130881      PROVE_step3
2019-03-03 11:29:14.930	51560	INFO 	perf	src/common/perf_timer.cpp:140	PERF   829718      PROVE_step4
2019-03-03 11:29:14.974	51560	INFO 	construct_tx	src/cryptonote_core/cryptonote_tx_utils.cpp:596	transaction_created: <738cef4a8e2fb33e80f253b3af9eb32159d4bd3e2a667a85ca2e30f95cd2188a>
{
  "version": 2, 
  "unlock_time": 0, 
  "vin": [ {
      "key": {
        "amount": 0, 
        "key_offsets": [ 8189987, 223390, 61335, 17620, 15591, 1262, 38698, 153, 2158, 1532, 420448
        ], 
        "k_image": "9f7dde726affcadd7006dac7bc05a98abd5b4c6c9c72611a21c3b43cfccee4ee"
      }
    }
  ], 
  "vout": [ {
      "amount": 0, 
      "target": {
        "key": "8838faa7dbd51413198970f130996fb519a7cfc5fe783051fca06977abfcb2d2"
      }
    }, {
      "amount": 0, 
      "target": {
        "key": "6c0c074cd9ea6c9977afcf3a7113e9994e3ef9b711c83cb18c8c12153a206a4c"
      }
    }
  ], 
  "extra": [ 2, 9, 1, 239, 91, 172, 246, 55, 221, 35, 23, 1, 34, 72, 155, 157, 233, 210, 102, 211, 96, 222, 137, 227, 53, 29, 50, 156, 153, 22, 201, 107, 218, 100, 182, 107, 148, 208, 65, 28, 98, 124, 232, 169
  ], 
  "rct_signatures": {
    "type": 4, 
    "txnFee": 36450000, 
    "ecdhInfo": [ {
        "amount": "272492a818e0f863"
      }, {
        "amount": "97a6c30cfa0cc475"
      }], 
    "outPk": [ "67269f1137fa94f0916e728ba74cd49f11165626547aea87dd98643b6871e73a", "bd30f816a017049d31443d3cff168b788ce2c48d4cd9142a9066c588f68921c4"]
  }, 
  "rctsig_prunable": {
    "nbp": 1, 
    "bp": [ {
        "A": "98ba87fcaa95dcb4ce3d563e06a13d90f2b6c3cff31a283833513252178cf269", 
        "S": "abf88591f6b0cecc2fcfed90b230e7b3681360921fd4b539a25c3fe31cbc005e", 
        "T1": "66ecc80203b159c4d23ce1f3ab1f4c5199772ebb2314939e84ce7f8abe7128c4", 
        "T2": "bed5945846c42575a9caa3f774d0bf5854a1825cab43f6fe226eb45ca87dee4b", 
        "taux": "658ebefd13663a0c122079d18ceef64fb14a45b107cd2752efe009258270170f", 
        "mu": "b06cef3fd6a91037bff615edec5606fd40a39c864ef768269ecd01438d4d180b", 
        "L": [ "017631c8dfcde301c3476bc835b6850d02973c2c5cdc29ebd499fe7a6dd82f0e", "ddb0606d16bea91d23929e551b7bcbd723617beb42d185ce0c4ad8169cc96b60", "3a365694fb8467a44dca3a7618d898c74b118297d9b9ebb11e73672a3f691c05", "a0803c61ebd2836e645c54cdfc6081d0fd1ef06a9c643f04cbb1637729199ce0", "a5dbd9d9867f372a64a26930d41c551eb17f0f100c0fd72083f450b8196ac892", "2eb679414d2a1baac07fc1dc0166edffba413ccc8697596deae91358bfef65a1", "f26a9087cad8fc386b463909ed51f1a61d9a6e595c919afda9d1054210e1262e"
        ], 
        "R": [ "9f43a56fbff1808758bbf3748cc253fb8de826b214eec46119892fd152b3d78c", "0bc406cfd4dce547687614f8f83f6d2cf0372a9ca2fb2e43c4f374be3449b3bf", "100c9a4fda5cbdadfa214484e2a321eed0ae13d3dc53c627abefd559ff399873", "1848817f13c875ad365c7e51fff84c285e9b1898beea9e0821bfc7acd2f4bbde", "159c4fdd5cdba8307546c3da550fd03345061f4a7dc33520a6b2ac44b3269a0d", "b8982c56926113e0377139c355cdb841a1ea9ca57985a6bcaa2e4e47e1ef15b6", "b77cd17918f7a1cb22bb6a25ace49bdcc17fb2a5f376c46c0caaa3a2eba8cc1a"
        ], 
        "a": "30229ec5270ab2e04a6747b5c56639f12b4f9159a0d2ee257d875a602fa8fd0c", 
        "b": "fad0d462bbeff97ea1796db9062e54613fef3d5bd78c0d56cc0b274fc455c802", 
        "t": "21530d2e062541d9755e9bfe0868801455e708846409c675a526cf408686890e"
      }
    ], 
    "MGs": [ {
        "ss": [ [ "b2161202f006571e5edfafac2cf4d97ae7699818cb1367d220bd01e453162a08", "ec46528d362778ea40f616cb672fd1a77b877424b828050bfa91fc23c3605e0f"], [ "7f32b7ed2b6fa9a00caec9bcae1bb6c503fad9deeb23e330a80691c100f4df06", "edc58dec527e06a9f3f0bae66ed4d92c14fe9b293328a3dfe17ecd6ebaed550c"], [ "e18bd006bf58471241f0a69d6e2fa93976fd5f7e2574e01b58c8023187e11f0e", "fc005a9b485383d868ce49b9ecfd51831863436e08b707f45add05bd447b2508"], [ "940323fad360f5fec433b89f4ae4d2b8c885ad67140fce65b1616332789b4502", "1ded70a14f0ffcaf8b2b586b365d31cf68021d801f33fe1934f6a6ac1ebb2a0b"], [ "df9290a2b6c821d95b346e46ee4288294f8a4fa33f911fa204bb8bf01f791c0c", "4267ff03f7c1f9ac96e050784b09a02cfeeaac1f92fc3a7b77c517b137cfc209"], [ "b8a81d8c5ff52788f2638ca23832b0d11274a8f154d39ed0d5b7ae2bd747fe0d", "0456102cede6c2e0895641a42cbdc2c8900c03719a6b8b826116fc37ea2a5000"], [ "54735aee0c202534f74db62c72f303ee33b61d3e3dc42d218cb04c5dba81a206", "a669ec02ee51bc241bb9f048d3d2e2a45363da76ba6f27d1638ae46926c78504"], [ "5995a361d19d282cc5191777ebcb1d0fd6cd66986620dcabb99bea0097bfd004", "e87888b9aca5325c5d8404fef460fde392cbb916e92691c5245167862590ef03"], [ "41f5728673f489ae1712b32aeb3971bc6c15933bd610da0af59b0c6e19cc5704", "02cd6176ef8a57aedc831a017162dd564250a14aa50227663fdd5a0ecb3fd208"], [ "104f739682f22f1ababf9f931fd61389a89d10e27a27dc37d5e838fefc932b01", "017269932c9db0518f3e4876cf32d01c285e32fd84586c1a2f29e8ee9744720b"], [ "61f2fbe649df2302ba44830fb519ee208274888fdcf809aea4fefb6eab365407", "556c94f83db87287fd38dad98fdbb9bcf69bc68be8e0662b3695ba620626c80c"]], 
        "cc": "e39d4c70b96b10b251a47175788f5aac9551eddeebf302cf7b2c297128e6a00a"
      }], 
    "pseudoOuts": [ "79906f5215f564f1c1682f76f11045b1b9a1d88d53287d9c83a64e8a66886814"]
  }
}

2019-03-03 11:29:14.979	51560	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:8785	  Transaction 1/1 <738cef4a8e2fb33e80f253b3af9eb32159d4bd3e2a667a85ca2e30f95cd2188a>: 1773 weight, sending 0.013515183000 in 1 outputs to 1 destination(s), including 0.000036450000 fee, 0.012478733000 change
2019-03-03 11:29:20.215	51560	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:5369	daemon_send_resp.status != CORE_RPC_STATUS_OK. THROW EXCEPTION: error::tx_rejected
2019-03-03 11:29:20.216	51560	WARN 	net.http	src/wallet/wallet_errors.h:814	C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:5369:N5tools5error11tx_rejectedE: transaction was rejected by daemon, status = Failed, tx:
{
  "version": 2, 
  "unlock_time": 0, 
  "vin": [ {
      "key": {
        "amount": 0, 
        "key_offsets": [ 8189987, 223390, 61335, 17620, 15591, 1262, 38698, 153, 2158, 1532, 420448
        ], 
        "k_image": "9f7dde726affcadd7006dac7bc05a98abd5b4c6c9c72611a21c3b43cfccee4ee"
      }
    }
  ], 
  "vout": [ {
      "amount": 0, 
      "target": {
        "key": "8838faa7dbd51413198970f130996fb519a7cfc5fe783051fca06977abfcb2d2"
      }
    }, {
      "amount": 0, 
      "target": {
        "key": "6c0c074cd9ea6c9977afcf3a7113e9994e3ef9b711c83cb18c8c12153a206a4c"
      }
    }
  ], 
  "extra": [ 2, 9, 1, 239, 91, 172, 246, 55, 221, 35, 23, 1, 34, 72, 155, 157, 233, 210, 102, 211, 96, 222, 137, 227, 53, 29, 50, 156, 153, 22, 201, 107, 218, 100, 182, 107, 148, 208, 65, 28, 98, 124, 232, 169
  ], 
  "rct_signatures": {
    "type": 4, 
    "txnFee": 36450000, 
    "ecdhInfo": [ {
        "amount": "272492a818e0f863"
      }, {
        "amount": "97a6c30cfa0cc475"
      }], 
    "outPk": [ "67269f1137fa94f0916e728ba74cd49f11165626547aea87dd98643b6871e73a", "bd30f816a017049d31443d3cff168b788ce2c48d4cd9142a9066c588f68921c4"]
  }, 
  "rctsig_prunable": {
    "nbp": 1, 
    "bp": [ {
        "A": "98ba87fcaa95dcb4ce3d563e06a13d90f2b6c3cff31a283833513252178cf269", 
        "S": "abf88591f6b0cecc2fcfed90b230e7b3681360921fd4b539a25c3fe31cbc005e", 
        "T1": "66ecc80203b159c4d23ce1f3ab1f4c5199772ebb2314939e84ce7f8abe7128c4", 
        "T2": "bed5945846c42575a9caa3f774d0bf5854a1825cab43f6fe226eb45ca87dee4b", 
        "taux": "658ebefd13663a0c122079d18ceef64fb14a45b107cd2752efe009258270170f", 
        "mu": "b06cef3fd6a91037bff615edec5606fd40a39c864ef768269ecd01438d4d180b", 
        "L": [ "017631c8dfcde301c3476bc835b6850d02973c2c5cdc29ebd499fe7a6dd82f0e", "ddb0606d16bea91d23929e551b7bcbd723617beb42d185ce0c4ad8169cc96b60", "3a365694fb8467a44dca3a7618d898c74b118297d9b9ebb11e73672a3f691c05", "a0803c61ebd2836e645c54cdfc6081d0fd1ef06a9c643f04cbb1637729199ce0", "a5dbd9d9867f372a64a26930d41c551eb17f0f100c0fd72083f450b8196ac892", "2eb679414d2a1baac07fc1dc0166edffba413ccc8697596deae91358bfef65a1", "f26a9087cad8fc386b463909ed51f1a61d9a6e595c919afda9d1054210e1262e"
        ], 
        "R": [ "9f43a56fbff1808758bbf3748cc253fb8de826b214eec46119892fd152b3d78c", "0bc406cfd4dce547687614f8f83f6d2cf0372a9ca2fb2e43c4f374be3449b3bf", "100c9a4fda5cbdadfa214484e2a321eed0ae13d3dc53c627abefd559ff399873", "1848817f13c875ad365c7e51fff84c285e9b1898beea9e0821bfc7acd2f4bbde", "159c4fdd5cdba8307546c3da550fd03345061f4a7dc33520a6b2ac44b3269a0d", "b8982c56926113e0377139c355cdb841a1ea9ca57985a6bcaa2e4e47e1ef15b6", "b77cd17918f7a1cb22bb6a25ace49bdcc17fb2a5f376c46c0caaa3a2eba8cc1a"
        ], 
        "a": "30229ec5270ab2e04a6747b5c56639f12b4f9159a0d2ee257d875a602fa8fd0c", 
        "b": "fad0d462bbeff97ea1796db9062e54613fef3d5bd78c0d56cc0b274fc455c802", 
        "t": "21530d2e062541d9755e9bfe0868801455e708846409c675a526cf408686890e"
      }
    ], 
    "MGs": [ {
        "ss": [ [ "b2161202f006571e5edfafac2cf4d97ae7699818cb1367d220bd01e453162a08", "ec46528d362778ea40f616cb672fd1a77b877424b828050bfa91fc23c3605e0f"], [ "7f32b7ed2b6fa9a00caec9bcae1bb6c503fad9deeb23e330a80691c100f4df06", "edc58dec527e06a9f3f0bae66ed4d92c14fe9b293328a3dfe17ecd6ebaed550c"], [ "e18bd006bf58471241f0a69d6e2fa93976fd5f7e2574e01b58c8023187e11f0e", "fc005a9b485383d868ce49b9ecfd51831863436e08b707f45add05bd447b2508"], [ "940323fad360f5fec433b89f4ae4d2b8c885ad67140fce65b1616332789b4502", "1ded70a14f0ffcaf8b2b586b365d31cf68021d801f33fe1934f6a6ac1ebb2a0b"], [ "df9290a2b6c821d95b346e46ee4288294f8a4fa33f911fa204bb8bf01f791c0c", "4267ff03f7c1f9ac96e050784b09a02cfeeaac1f92fc3a7b77c517b137cfc209"], [ "b8a81d8c5ff52788f2638ca23832b0d11274a8f154d39ed0d5b7ae2bd747fe0d", "0456102cede6c2e0895641a42cbdc2c8900c03719a6b8b826116fc37ea2a5000"], [ "54735aee0c202534f74db62c72f303ee33b61d3e3dc42d218cb04c5dba81a206", "a669ec02ee51bc241bb9f048d3d2e2a45363da76ba6f27d1638ae46926c78504"], [ "5995a361d19d282cc5191777ebcb1d0fd6cd66986620dcabb99bea0097bfd004", "e87888b9aca5325c5d8404fef460fde392cbb916e92691c5245167862590ef03"], [ "41f5728673f489ae1712b32aeb3971bc6c15933bd610da0af59b0c6e19cc5704", "02cd6176ef8a57aedc831a017162dd564250a14aa50227663fdd5a0ecb3fd208"], [ "104f739682f22f1ababf9f931fd61389a89d10e27a27dc37d5e838fefc932b01", "017269932c9db0518f3e4876cf32d01c285e32fd84586c1a2f29e8ee9744720b"], [ "61f2fbe649df2302ba44830fb519ee208274888fdcf809aea4fefb6eab365407", "556c94f83db87287fd38dad98fdbb9bcf69bc68be8e0662b3695ba620626c80c"]], 
        "cc": "e39d4c70b96b10b251a47175788f5aac9551eddeebf302cf7b2c297128e6a00a"
      }], 
    "pseudoOuts": [ "79906f5215f564f1c1682f76f11045b1b9a1d88d53287d9c83a64e8a66886814"]
  }
}
2019-03-03 11:29:20.217	51560	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: transaction <738cef4a8e2fb33e80f253b3af9eb32159d4bd3e2a667a85ca2e30f95cd2188a> was rejected by daemon with status: Failed
2019-03-03 11:29:20.219	51560	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: There was an error, which could mean the node may be trying to get you to retry creating a transaction, and zero in on which outputs you own. Or it could be a bona fide error. It may be prudent to disconnect from this node, and not try to send a transaction immediately. Alternatively, connect to another node so the original node cannot correlate information.
2019-03-03 11:29:21.941	54040	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2788	Refresh done, blocks received: 0, balance (all accounts): 0.013515183000, unlocked: 0.013515183000

```

</p>
</details>




## moneromooo-monero | 2019-03-03T12:32:07+00:00
For some reason your wallet is trying to send new style transactions. These aren't accepted before v10, on or around the 9th. This can happen with old daemons that have no updated to the current version yet, and since you use a third party daemon, it seems likely this daemon is mistakenly telling you to use those new rules already.

# Action History
- Created by: x151973 | 2019-03-03T01:01:52+00:00
- Closed at: 2019-03-08T22:16:21+00:00
