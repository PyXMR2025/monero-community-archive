---
title: wallet gui can't connect to daemon
source_url: https://github.com/monero-project/monero-gui/issues/899
author: chamalis
assignees: []
labels:
- resolved
created_at: '2017-10-11T08:52:56+00:00'
updated_at: '2018-12-18T15:24:54+00:00'
type: issue
status: closed
closed_at: '2018-11-18T14:09:29+00:00'
---

# Original Description
## 1st case) Using binaries from Download page  [monero-linux-x64-v0.11.0.0.tar.bz2](https://downloads.getmonero.org/cli/linux64)

### Sub-case 1.1: `monerod` already running (binary produced building from [monero](https://github.com/monero-project/monero) subproject)

Running

```
$ ./start-gui.sh 
2017-Oct-11 11:03:02.133318 ERROR /home/vagrant/slave/monero-core-ubuntu-amd64/build/monero/contrib/epee/include/storages/portable_storage.h:161 portable_storage: wrong binary format - signature missmatch
2017-Oct-11 11:03:02.134275 ERROR /home/vagrant/slave/monero-core-ubuntu-amd64/build/monero/src/wallet/wallet2.cpp:1959 !r. THROW EXCEPTION: error::invalid_password
2017-Oct-11 11:03:02.134532 /home/vagrant/slave/monero-core-ubuntu-amd64/build/monero/src/wallet/wallet2.cpp:1959:N5tools5error16invalid_passwordE: invalid password
2017-Oct-11 11:03:02.135011 ERROR /home/vagrant/slave/monero-core-ubuntu-amd64/build/monero/src/wallet/api/wallet.cpp:298 Error opening wallet: invalid password
qml: Error opening wallet with empty password:  invalid password
2017-Oct-11 11:03:02.180429 ~WalletImpl
2017-Oct-11 11:03:02.180599 closing wallet...
2017-Oct-11 11:03:02.180658 wallet::store done
2017-Oct-11 11:03:02.180703 Calling wallet::stop...
2017-Oct-11 11:03:02.182131 wallet::stop done
2017-Oct-11 11:03:02.183315 ~WalletImpl finished
2017-Oct-11 11:03:06.751204 Loaded wallet keys file, with public address: 48U9NYMmyZPh1XnEAG1Rw2d3vj85RvkFTjZFjHyYHxVq6P5EwpQys8bFQVH7LTJLHpUMpLoeeQyyWKopC2AEp4PEMjXMdUD
2017-Oct-11 11:03:06.751291 Trying to decrypt cache data
```

**Will stay forever at "Waiting on daemon synchronization to finish"**

![monero1](https://user-images.githubusercontent.com/908356/31428763-9d6313b2-ae74-11e7-9b45-7f3222e94659.png)

* Client log: monero-wallet-cli.log  is empty


* Also tried from the gui -> settings -> Start Daemon (localhost:18081) 
which writes to the gui logs the following:  "Unknown command" as can be seen below:

```Creating the logger system

Monero 'Wolfram Warptangent' (v0.10.1.0-dd580d7)
Commands: 
  alt_chain_info          Print information about alternative chains
  ban                     Ban a given IP for a time
  bans                    Show the currently banned IPs
  diff                    Show difficulty
  exit                    Stop the daemon
  flush_txpool            Flush a transaction from the tx pool by its txid, or the whole tx pool
  hard_fork_info          Print hard fork voting information
  help                    Show this help
  hide_hr                 Stop showing hash rate
  is_key_image_spent      Prints whether a given key image is in the spent key images set, is_key_image_spent <key_image>
  limit                   limit <kB/s> - Set download and upload limit
  limit_down              limit <kB/s> - Set download limit
  limit_up                limit <kB/s> - Set upload limit
  out_peers               Set max number of out peers
  output_histogram        Print output histogram (amount, instances)
  print_bc                Print blockchain info in a given blocks range, print_bc <begin_height> [<end_height>]
  print_block             Print block, print_block <block_hash> | <block_height>
  print_cn                Print connections
  print_coinbase_tx_sum   Print sum of coinbase transactions (start height, block count)
  print_height            Print local blockchain height
  print_pl                Print peer list
  print_pool              Print transaction pool (long format)
  print_pool_sh           Print transaction pool (short format)
  print_pool_stats        Print transaction pool statistics
  print_status            Prints daemon status
  print_tx                Print transaction, print_tx <transaction_hash>
  q                       ignored
  save                    Save blockchain
  set_log                 set_log <level> - Change current log detalization level, <level> is a number 0-4
  show_hr                 Start showing hash rate
  start_mining            Start mining for specified address, start_mining <addr> [<threads>], default 1 thread
  start_save_graph        Start save data for dr monero
  status                  Show status
  stop_daemon             Stop the daemon
  stop_mining             Stop mining
  stop_save_graph         Stop save data for dr monero
  unban                   Unban a given IP
  

Unknown command
```

### Sub-case 2.2: `monerod` NOT running, lets let the gui run the daemon itself:

This time I get **"Wallet is not connected to daemon"**

![monero2](https://user-images.githubusercontent.com/908356/31429144-dba51ae8-ae75-11e7-81b9-1b52ff2615be.png)

same logs, stdout, etc



## Second case - buildind from source (current repo):

### Sub-case 2.1: `monerod` already running (binary produced building from [monero](https://github.com/monero-project/monero) subproject)

![monero_2 1](https://user-images.githubusercontent.com/908356/31430683-431ad510-ae7a-11e7-8cd0-ec80e1523a9c.png)


```
$ ./build/release/bin/monero-wallet-gui 
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
2017-10-11 08:37:00.921	    7fc0cab0b700	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-10-11 08:37:00.922	    7fc0cab0b700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-10-11 08:37:00.922	    7fc0cab0b700	WARN 	net.http	src/wallet/wallet_errors.h:707	/home/stelarov/hacking/mining/monero-gui-src/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-10-11 08:37:00.925	    7fc0cab0b700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
qml: Error opening wallet with empty password:  invalid password
2017-10-11 08:37:00.986	    7fc0cab0b700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
[1507711023] libunbound[18062:0] error: outgoing tcp: connect: Invalid argument for fe80::1
[1507711023] libunbound[18062:0] error: serviced_tcp_initiate: failed to send tcp query
[1507711023] libunbound[18062:0] error: outgoing tcp: connect: Invalid argument for fe80::1
[1507711023] libunbound[18062:0] error: serviced_tcp_initiate: failed to send tcp query
[1507711024] libunbound[18062:0] error: outgoing tcp: connect: Invalid argument for fe80::1
[1507711024] libunbound[18062:0] error: serviced_tcp_initiate: failed to send tcp query
2017-10-11 08:37:06.434	    7fc0cab0b700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 48U9NYMmyZPh1XnEAG1Rw2d3vj85RvkFTjZFjHyYHxVq6P5EwpQys8bFQVH7LTJLHpUMpLoeeQyyWKopC2AEp4PEMjXMdUD
[1507711029] libunbound[18062:0] error: outgoing tcp: connect: Invalid argument for fe80::1
[1507711029] libunbound[18062:0] error: serviced_tcp_initiate: failed to send tcp query
[1507711034] libunbound[18062:0] error: outgoing tcp: connect: Invalid argument for fe80::1
[1507711034] libunbound[18062:0] error: serviced_tcp_initiate: failed to send tcp query
[1507711035] libunbound[18062:0] error: outgoing tcp: connect: Invalid argument for fe80::1
[1507711035] libunbound[18062:0] error: serviced_tcp_initiate: failed to send tcp query
[1507711036] libunbound[18062:0] error: outgoing tcp: connect: Invalid argument for fe80::1
[1507711036] libunbound[18062:0] error: serviced_tcp_initiate: failed to send tcp query
[1507711036] libunbound[18062:0] error: outgoing tcp: connect: Invalid argument for fe80::1
[1507711036] libunbound[18062:0] error: serviced_tcp_initiate: failed to send tcp query
[1507711040] libunbound[18062:0] error: outgoing tcp: connect: Invalid argument for fe80::1
[1507711040] libunbound[18062:0] error: serviced_tcp_initiate: failed to send tcp query
[1507711040] libunbound[18062:0] error: outgoing tcp: connect: Invalid argument for fe80::1
[1507711040] libunbound[18062:0] error: serviced_tcp_initiate: failed to send tcp query
```

The log file:

```
$ cat ./build/release/bin/monero-wallet-gui.log
2017-10-11 08:36:08.550	    7fb6245b6780	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:36:08.974	    7fb6245b6780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:36:09.555	    7fb6245b6780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:36:09.675	    7fb5e7fff700	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-10-11 08:36:09.675	    7fb5e7fff700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-10-11 08:36:09.675	    7fb5e7fff700	WARN 	net.http	src/wallet/wallet_errors.h:707	/home/stelarov/hacking/mining/monero-gui-src/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-10-11 08:36:09.676	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: tools::error::invalid_password
2017-10-11 08:36:09.676	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monero-wallet-gui:__cxa_throw+0xfa [0x55690cf8815a]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monero-wallet-gui+0x23671e [0x55690d00671e]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monero-wallet-gui+0x1e6006 [0x55690cfb6006]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monero-wallet-gui+0x1e988e [0x55690cfb988e]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monero-wallet-gui+0xb6543 [0x55690ce86543]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monero-wallet-gui+0xd2159 [0x55690cea2159]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./build/release/bin/monero-wallet-gui+0x75f28 [0x55690ce45f28]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monero-wallet-gui+0x7b280 [0x55690ce4b280]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /usr/lib/x86_64-linux-gnu/libQt5Core.so.5+0xa8581 [0x7fb61fdd6581]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] /usr/lib/x86_64-linux-gnu/libQt5Core.so.5+0xac29d [0x7fb61fdda29d]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] /lib/x86_64-linux-gnu/libpthread.so.0+0x7494 [0x7fb61f88c494]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [12] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7fb61ed36abf]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [13] [(nil)]
2017-10-11 08:36:09.677	    7fb5e7fff700	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-11 08:36:09.677	    7fb5e7fff700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
2017-10-11 08:36:09.779	    7fb5e7fff700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2017-10-11 08:36:15.349	    7fb6245b6780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:36:15.442	    7fb5e7fff700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 48U9NYMmyZPh1XnEAG1Rw2d3vj85RvkFTjZFjHyYHxVq6P5EwpQys8bFQVH7LTJLHpUMpLoeeQyyWKopC2AEp4PEMjXMdUD
2017-10-11 08:36:59.809	    7fc0fee56780	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:37:00.202	    7fc0fee56780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:37:00.792	    7fc0fee56780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:37:00.921	    7fc0cab0b700	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-10-11 08:37:00.922	    7fc0cab0b700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-10-11 08:37:00.922	    7fc0cab0b700	WARN 	net.http	src/wallet/wallet_errors.h:707	/home/stelarov/hacking/mining/monero-gui-src/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-10-11 08:37:00.922	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: tools::error::invalid_password
2017-10-11 08:37:00.922	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monero-wallet-gui:__cxa_throw+0xfa [0x55f7cb3de15a]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monero-wallet-gui+0x23671e [0x55f7cb45c71e]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monero-wallet-gui+0x1e6006 [0x55f7cb40c006]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monero-wallet-gui+0x1e988e [0x55f7cb40f88e]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monero-wallet-gui+0xb6543 [0x55f7cb2dc543]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monero-wallet-gui+0xd2159 [0x55f7cb2f8159]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./build/release/bin/monero-wallet-gui+0x75f28 [0x55f7cb29bf28]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monero-wallet-gui+0x7b280 [0x55f7cb2a1280]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /usr/lib/x86_64-linux-gnu/libQt5Core.so.5+0xa8581 [0x7fc0fa676581]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] /usr/lib/x86_64-linux-gnu/libQt5Core.so.5+0xac29d [0x7fc0fa67a29d]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] /lib/x86_64-linux-gnu/libpthread.so.0+0x7494 [0x7fc0fa12c494]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [12] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7fc0f95d6abf]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [13] [(nil)]
2017-10-11 08:37:00.925	    7fc0cab0b700	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-11 08:37:00.925	    7fc0cab0b700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
2017-10-11 08:37:00.986	    7fc0cab0b700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2017-10-11 08:37:06.357	    7fc0fee56780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:37:06.434	    7fc0cab0b700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 48U9NYMmyZPh1XnEAG1Rw2d3vj85RvkFTjZFjHyYHxVq6P5EwpQys8bFQVH7LTJLHpUMpLoeeQyyWKopC2AEp4PEMjXMdUD
```


### Sub-case 2.2: `monerod` NOT running, lets let the gui run the daemon itself:

![monero_2 2](https://user-images.githubusercontent.com/908356/31430367-51c823ac-ae79-11e7-8c31-2243dd46c99c.png)

```
$ ./build/release/bin/monero-wallet-gui 
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
2017-10-11 08:27:25.106	    7f9cdf7a2700	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-10-11 08:27:25.107	    7f9cdf7a2700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-10-11 08:27:25.107	    7f9cdf7a2700	WARN 	net.http	src/wallet/wallet_errors.h:707	/home/stelarov/hacking/mining/monero-gui-src/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-10-11 08:27:25.109	    7f9cdf7a2700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
qml: Error opening wallet with empty password:  invalid password
2017-10-11 08:27:25.146	    7f9cdf7a2700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2017-10-11 08:27:29.279	    7f9cdf7a2700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 48U9NYMmyZPh1XnEAG1Rw2d3vj85RvkFTjZFjHyYHxVq6P5EwpQys8bFQVH7LTJLHpUMpLoeeQyyWKopC2AEp4PEMjXMdUD
Monero 'Helium Hydra' (v0.11.0.0-15b0ff2c)
Commands: 
  alt_chain_info          Print information about alternative chains
  ban                     Ban a given IP for a time
  bans                    Show the currently banned IPs
  bc_dyn_stats            Print information about current blockchain dynamic state
  diff                    Show difficulty
  exit                    Stop the daemon
  flush_txpool            Flush a transaction from the tx pool by its txid, or the whole tx pool
  hard_fork_info          Print hard fork voting information
  help                    Show this help
  hide_hr                 Stop showing hash rate
  is_key_image_spent      Prints whether a given key image is in the spent key images set, is_key_image_spent <key_image>
  limit                   limit <kB/s> - Set download and upload limit
  limit_down              limit <kB/s> - Set download limit
  limit_up                limit <kB/s> - Set upload limit
  out_peers               Set max number of out peers
  output_histogram        Print output histogram (amount, instances)
  print_bc                Print blockchain info in a given blocks range, print_bc <begin_height> [<end_height>]
  print_block             Print block, print_block <block_hash> | <block_height>
  print_cn                Print connections
  print_coinbase_tx_sum   Print sum of coinbase transactions (start height, block count)
  print_height            Print local blockchain height
  print_pl                Print peer list
  print_pl_stats          Print peer list stats
  print_pool              Print transaction pool (long format)
  print_pool_sh           Print transaction pool (short format)
  print_pool_stats        Print transaction pool statistics
  print_status            Prints daemon status
  print_tx                Print transaction, print_tx <transaction_hash>
  q                       ignored
  relay_tx                Relay a given transaction by its txid
  save                    Save blockchain
  set_log                 set_log <level>|<categories> - Change current loglevel, <level> is a number 0-4
  show_hr                 Start showing hash rate
  start_mining            Start mining for specified address, start_mining <addr> [<threads>] [do_background_mining] [ignore_battery], default 1 thread, no background mining
  start_save_graph        Start save data for dr monero
  status                  Show status
  stop_daemon             Stop the daemon
  stop_mining             Stop mining
  stop_save_graph         Stop save data for dr monero
  sync_info               Print information about blockchain sync state
  unban                   Unban a given IP
  update                  subcommands: check (check if an update is available), download (download it if there is), update (not implemented)
  
Unknown command
^C
````

The log file:
```
$ cat ./build/release/bin/monero-wallet-gui.log
2017-10-11 08:25:37.321	    7fd27fba8780	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:25:37.814	    7fd27fba8780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:25:38.351	    7fd27fba8780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:25:38.403	    7fd2439bb700	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-10-11 08:25:38.403	    7fd2439bb700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-10-11 08:25:38.403	    7fd2439bb700	WARN 	net.http	src/wallet/wallet_errors.h:707	/home/stelarov/hacking/mining/monero-gui-src/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-10-11 08:25:38.403	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: tools::error::invalid_password
2017-10-11 08:25:38.403	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monero-wallet-gui:__cxa_throw+0xfa [0x55d67fa9715a]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monero-wallet-gui+0x23671e [0x55d67fb1571e]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monero-wallet-gui+0x1e6006 [0x55d67fac5006]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monero-wallet-gui+0x1e988e [0x55d67fac888e]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monero-wallet-gui+0xb6543 [0x55d67f995543]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monero-wallet-gui+0xd2159 [0x55d67f9b1159]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./build/release/bin/monero-wallet-gui+0x75f28 [0x55d67f954f28]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monero-wallet-gui+0x7b280 [0x55d67f95a280]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /usr/lib/x86_64-linux-gnu/libQt5Core.so.5+0xa8581 [0x7fd27b3c8581]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] /usr/lib/x86_64-linux-gnu/libQt5Core.so.5+0xac29d [0x7fd27b3cc29d]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] /lib/x86_64-linux-gnu/libpthread.so.0+0x7494 [0x7fd27ae7e494]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [12] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7fd27a328abf]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [13] [(nil)]
2017-10-11 08:25:38.406	    7fd2439bb700	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-11 08:25:38.407	    7fd2439bb700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
2017-10-11 08:25:38.423	    7fd2439bb700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2017-10-11 08:25:43.570	    7fd27fba8780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:25:43.669	    7fd2439bb700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 48U9NYMmyZPh1XnEAG1Rw2d3vj85RvkFTjZFjHyYHxVq6P5EwpQys8bFQVH7LTJLHpUMpLoeeQyyWKopC2AEp4PEMjXMdUD
2017-10-11 08:27:24.113	    7f9d1b942780	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:27:24.462	    7f9d1b942780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:27:24.987	    7f9d1b942780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:27:25.106	    7f9cdf7a2700	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-10-11 08:27:25.107	    7f9cdf7a2700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-10-11 08:27:25.107	    7f9cdf7a2700	WARN 	net.http	src/wallet/wallet_errors.h:707	/home/stelarov/hacking/mining/monero-gui-src/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-10-11 08:27:25.108	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:120	Exception: tools::error::invalid_password
2017-10-11 08:27:25.108	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:121	Unwound call stack:
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [1] ./build/release/bin/monero-wallet-gui:__cxa_throw+0xfa [0x557fed42b15a]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [2] ./build/release/bin/monero-wallet-gui+0x23671e [0x557fed4a971e]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [3] ./build/release/bin/monero-wallet-gui+0x1e6006 [0x557fed459006]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [4] ./build/release/bin/monero-wallet-gui+0x1e988e [0x557fed45c88e]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [5] ./build/release/bin/monero-wallet-gui+0xb6543 [0x557fed329543]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [6] ./build/release/bin/monero-wallet-gui+0xd2159 [0x557fed345159]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [7] ./build/release/bin/monero-wallet-gui+0x75f28 [0x557fed2e8f28]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [8] ./build/release/bin/monero-wallet-gui+0x7b280 [0x557fed2ee280]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [9] /usr/lib/x86_64-linux-gnu/libQt5Core.so.5+0xa8581 [0x7f9d17162581]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [10] /usr/lib/x86_64-linux-gnu/libQt5Core.so.5+0xac29d [0x7f9d1716629d]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [11] /lib/x86_64-linux-gnu/libpthread.so.0+0x7494 [0x7f9d16c18494]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [12] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7f9d160c2abf]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	    [13] [(nil)]
2017-10-11 08:27:25.109	    7f9cdf7a2700	INFO 	stacktrace	src/common/stack_trace.cpp:159	
2017-10-11 08:27:25.109	    7f9cdf7a2700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
2017-10-11 08:27:25.146	    7f9cdf7a2700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2017-10-11 08:27:29.203	    7f9d1b942780	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-11 08:27:29.279	    7f9cdf7a2700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 48U9NYMmyZPh1XnEAG1Rw2d3vj85RvkFTjZFjHyYHxVq6P5EwpQys8bFQVH7LTJLHpUMpLoeeQyyWKopC2AEp4PEMjXMdUD
```

PS1: After rebooting I only managed to **run successfully case 2.1 but only once** - after I shutdown the gui and redo all the steps, I am still getting the above behavior. Something like a stochastic process.

PS2: The "wrong password" logs are written upon execution before I even write the password.

# Discussion History
## radfish | 2017-10-11T13:27:48+00:00
Can you please also attach daemon logs (for the built-from-master case)?
I'm having a potentially similar issue: https://github.com/monero-project/monero/issues/2545

## dEBRUYNE-1 | 2017-10-11T15:08:21+00:00
>Monero 'Wolfram Warptangent' (v0.10.1.0-dd580d7)

Is that a typo or were you really running an old daemon? Otherwise it'd explain (for that part) why it wasn't working properly. 

## chamalis | 2017-10-11T16:41:58+00:00
@radfish 
The daemon (`monerod`) doesn't produce any log file. 

```
$ find . -iname *log
./build/release/CMakeFiles/CMakeOutput.log
./build/release/CMakeFiles/CMakeError.log
./external/unbound/doc/Changelog
```

I also tried with:

`$./build/release/bin/monerod --log-file monerod.log`

The only output is stdout which is like this:
```
2017-10-11 16:27:59.482	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[188.68.58.97:18080 OUT] Sync data returned a new top block candidate: 1204019 -> 1418434 [Your node is 214415 blocks (297 days) behind] 
SYNCHRONIZATION started
2017-10-11 16:28:01.847	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[188.68.58.97:18080 OUT]  Synced 1204119/1418434
2017-10-11 16:28:04.626	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[94.100.221.211:18080 OUT]  Synced 1204219/1418434
........
2017-10-11 16:29:27.475	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[82.217.110.51:50020 INC] Sync data returned a new top block candidate: 1210219 -> 1418435 [Your node is 208216 blocks (289 days) behind] 
SYNCHRONIZATION started
2017-10-11 16:29:47.730	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[94.100.221.211:18080 OUT]  Synced 1210319/1418435
....
```

@dEBRUYNE-1 
That's the binary from [getmonero.org](https://getmonero.org/downloads/) download page (the exact version is linked in bold in the first header of the issue). I suppose we should focus on the **case 2 (current repo ~ master branch)**


## dEBRUYNE-1 | 2017-10-11T18:55:09+00:00
@chefarov: The log is in `~/.bitmonero`.

Re: version, I see, but still weird it'd display something like that. 

## chamalis | 2017-10-11T22:05:57+00:00
@dEBRUYNE-1 
Missed that :S Thank you for the info! The current log file is:


[monerod.log](https://github.com/monero-project/monero-core/files/1377337/monerod.log)

which contains no errors at all. 

Some earlier error messages (I can't reproduce them since I don't know what triggered them) are provided below:


```
$ grep -i error monerod.0.log
2017-10-11 21:18:22.021	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:928	returned not all requested objects (context.m_requested_objects.size()=20), dropping connection
2017-10-11 21:18:22.456	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[195.154.169.129:18020 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-11 21:18:22.933	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.191.99.191:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
....
....
2017-10-11 21:20:07.722	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.191.99.191:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-11 21:20:09.289	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[81.169.150.217:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-11 21:20:54.123	[SRV_MAIN]	WARN 	net.p2p	src/p2p/net_node.inl:797	[123.52.229.55:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
```





## dEBRUYNE-1 | 2017-10-27T13:44:20+00:00
Can you try v0.11.1.0? 

## chamalis | 2017-10-29T21:52:50+00:00
monerod is also killing CPU (hadn't noticed before). Built from source v0.11.1.0-c328163f (current stable)

```
<path>/monero-gui-src/monero$ ./build/release/bin/monerod --log-file monero-gui-src-0.11.1 --log-level 1 
2017-10-29 21:28:40.455	    7ff7c9057d00	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-c328163f)
2017-10-29 21:28:40.455	    7ff7c9057d00	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-10-29 21:28:40.455	    7ff7c9057d00	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-10-29 21:28:40.456	    7ff7c9057d00	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-10-29 21:28:45.214	    7ff7c9057d00	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-10-29 21:28:45.214	    7ff7c9057d00	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-10-29 21:28:45.214	    7ff7c9057d00	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-10-29 21:28:45.214	    7ff7c9057d00	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-10-29 21:28:45.214	    7ff7c9057d00	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-10-29 21:28:45.215	    7ff7c9057d00	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/stelarov/.bitmonero/lmdb ...
2017-10-29 21:28:45.411	    7ff7c9057d00	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:421	Loading checkpoints
2017-10-29 21:28:46.124	    7ff7c9057d00	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:578	[batch] DB resize needed
2017-10-29 21:28:46.130	    7ff7c9057d00	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 41637MiB, New: 42661MiB
2017-10-29 21:28:46.131	    7ff7c9057d00	INFO 	global	src/daemon/core.h:78	Core initialized OK
2017-10-29 21:28:46.131	    7ff7c9057d00	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2017-10-29 21:28:46.132	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-10-29 21:28:46.132	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2017-10-29 21:28:47.133	[P2P1]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1258	
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2017-10-29 21:28:47.388	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[176.9.0.89:8180 OUT] Sync data returned a new top block candidate: 1391528 -> 1431563 [Your node is 40035 blocks (55 days) behind] 
SYNCHRONIZATION started
2017-10-29 21:29:03.030	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[176.9.0.89:8180 OUT]  Synced 1391548/1431563
2017-10-29 21:29:16.870	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391568/1431563
2017-10-29 21:29:23.930	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391588/1431563
2017-10-29 21:29:33.752	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391608/1431563
2017-10-29 21:29:42.033	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391628/1431563
2017-10-29 21:29:48.606	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391648/1431563
2017-10-29 21:30:00.646	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391668/1431563
2017-10-29 21:30:07.157	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391688/1431563
2017-10-29 21:30:16.877	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391708/1431563
2017-10-29 21:30:26.907	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391728/1431563
2017-10-29 21:30:27.386	[P2P4]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[193.70.103.86:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-10-29 21:30:27.687	[P2P0]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[193.70.103.86:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-10-29 21:30:39.776	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391748/1431563
2017-10-29 21:30:48.916	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391768/1431563
2017-10-29 21:31:03.956	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391788/1431563
2017-10-29 21:31:19.447	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391808/1431563
2017-10-29 21:31:31.813	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391828/1431563
2017-10-29 21:31:39.963	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391848/1431563
2017-10-29 21:31:48.365	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:834	[163.172.255.59:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-10-29 21:31:49.442	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391868/1431563
2017-10-29 21:31:50.601	[P2P9]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[163.172.255.59:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-10-29 21:31:50.602	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:851	[163.172.255.59:18080 OUT] COMMAND_TIMED_SYNC Failed
2017-10-29 21:31:55.623	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391888/1431563
2017-10-29 21:32:00.770	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 113.161.184.198:18080
2017-10-29 21:32:08.743	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391908/1431563
2017-10-29 21:32:21.042	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391928/1431563
2017-10-29 21:32:27.178	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391948/1431563
2017-10-29 21:32:27.997	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 93.134.49.21:18080
2017-10-29 21:32:29.022	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[104.140.244.186:59462 INC] Sync data returned a new top block candidate: 1391948 -> 1431564 [Your node is 39616 blocks (55 days) behind] 
SYNCHRONIZATION started
2017-10-29 21:32:30.997	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[93.134.49.21:63727 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-10-29 21:32:34.032	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391968/1431564
2017-10-29 21:32:44.834	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1391988/1431564
2017-10-29 21:32:53.549	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392008/1431564
2017-10-29 21:32:55.687	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[98.249.196.132:51039 INC] Sync data returned a new top block candidate: 1392008 -> 1431565 [Your node is 39557 blocks (54 days) behind] 
SYNCHRONIZATION started
2017-10-29 21:32:57.687	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 98.249.196.132:18080
2017-10-29 21:32:59.031	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392028/1431564
2017-10-29 21:33:06.708	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392048/1431564
2017-10-29 21:33:09.867	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[173.244.36.81:51425 INC] Sync data returned a new top block candidate: 1392048 -> 1431565 [Your node is 39517 blocks (54 days) behind] 
SYNCHRONIZATION started
2017-10-29 21:33:10.605	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 173.244.36.81:18080
2017-10-29 21:33:11.957	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 208.69.48.12:18080
2017-10-29 21:33:12.766	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392068/1431565
2017-10-29 21:33:23.152	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392088/1431565
2017-10-29 21:33:29.408	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392108/1431565
2017-10-29 21:33:37.207	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392128/1431565
2017-10-29 21:33:42.097	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392148/1431565
2017-10-29 21:33:42.784	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:759	[72.208.207.32:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-10-29 21:33:42.786	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:808	[72.208.207.32:18080 OUT] COMMAND_HANDSHAKE Failed
2017-10-29 21:33:47.998	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392168/1431565
2017-10-29 21:33:55.241	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392188/1431565
2017-10-29 21:33:58.250	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 193.111.173.253:18080
2017-10-29 21:34:10.290	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392208/1431565
2017-10-29 21:34:15.640	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 118.69.176.205:18080
2017-10-29 21:34:20.217	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392228/1431565
2017-10-29 21:34:31.822	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392248/1431565
2017-10-29 21:34:45.369	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392268/1431565
2017-10-29 21:34:45.794	[P2P0]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:933	returned not all requested objects (context.m_requested_objects.size()=40), dropping connection
2017-10-29 21:34:45.794	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:834	[208.104.15.80:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-10-29 21:34:55.160	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:759	[174.45.144.45:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-10-29 21:34:55.160	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:808	[174.45.144.45:18080 OUT] COMMAND_HANDSHAKE Failed
2017-10-29 21:34:59.476	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392288/1431565
2017-10-29 21:35:05.997	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392308/1431565
2017-10-29 21:35:12.631	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392328/1431565
2017-10-29 21:35:18.048	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392348/1431565
2017-10-29 21:35:21.165	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:1195	Failed to connect to any of seed peers, trying fallback seeds
2017-10-29 21:35:21.166	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:1206	Failed to connect to any of seed peers, continuing without seeds
2017-10-29 21:35:25.233	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392368/1431565
2017-10-29 21:35:31.652	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392388/1431565
2017-10-29 21:35:31.802	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 113.161.184.198:18080
2017-10-29 21:35:38.409	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392408/1431565
2017-10-29 21:35:43.621	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392428/1431565
2017-10-29 21:35:49.643	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392448/1431565
2017-10-29 21:35:54.701	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392468/1431565
2017-10-29 21:35:55.351	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:914	[68.3.163.220:18080 OUT] sent wrong NOTIFY_RESPONSE_GET_OBJECTS: block with id=f70bd73c745c5c1c309910b837029be54d25e5d3ccc3a548323884b20c70e0c9 wasn't requested, dropping connection
2017-10-29 21:35:55.353	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:834	[68.3.163.220:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-10-29 21:35:59.226	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:914	[176.9.12.46:18080 OUT] sent wrong NOTIFY_RESPONSE_GET_OBJECTS: block with id=f70bd73c745c5c1c309910b837029be54d25e5d3ccc3a548323884b20c70e0c9 wasn't requested, dropping connection
2017-10-29 21:36:01.777	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392488/1431565
2017-10-29 21:36:08.822	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392508/1431565
2017-10-29 21:36:21.600	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[163.172.255.59:18080 OUT]  Synced 1392528/1431565
2017-10-29 21:36:21.687	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[163.172.255.59:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:21.693	[P2P8]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[163.172.255.59:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-10-29 21:36:23.657	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.661	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.662	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.663	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.664	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.665	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.666	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.667	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.668	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.669	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.671	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.673	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.676	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.677	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.678	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.679	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.680	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.680	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.681	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.682	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.683	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.684	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.685	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.686	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.688	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.689	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.691	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.693	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.694	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.696	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.699	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.700	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.701	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.702	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.703	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.704	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.705	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.705	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.706	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.707	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.708	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.709	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.710	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.711	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.712	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.713	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.714	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.714	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.715	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.716	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.717	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.718	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.719	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.720	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.721	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.722	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.724	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.725	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.726	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.727	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.728	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.729	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.731	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.732	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.733	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.734	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.735	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.736	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.737	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.738	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.739	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.740	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.744	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.746	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.746	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.747	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.748	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.749	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.750	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.751	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.752	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.752	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.753	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.754	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.755	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.756	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.757	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.758	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.760	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.762	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.763	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.764	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.765	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.767	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.769	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.770	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.773	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.775	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.776	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.777	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.778	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.779	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.780	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.781	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.782	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.783	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.783	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.784	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.785	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.786	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.787	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.788	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.789	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.789	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:23.790	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[98.235.213.182:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:30.578	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[111.231.109.66:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:36:33.386	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[45.76.5.171:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-10-29 21:36:51.076	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392548/1431565
2017-10-29 21:36:51.119	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1025	[37.59.49.7:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-10-29 21:37:11.200	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392568/1431567
2017-10-29 21:37:21.286	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392588/1431567
2017-10-29 21:37:24.741	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 109.230.30.221:18080
2017-10-29 21:37:28.725	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 118.69.176.205:18080
2017-10-29 21:37:29.696	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392608/1431567
2017-10-29 21:37:43.279	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392628/1431567
2017-10-29 21:37:48.066	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 83.239.140.120:18080
2017-10-29 21:37:51.848	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392648/1431567
2017-10-29 21:37:59.074	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392668/1431568
2017-10-29 21:38:03.413	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 173.239.240.184:18080
2017-10-29 21:38:12.252	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392688/1431568
2017-10-29 21:38:22.733	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392708/1431568
2017-10-29 21:38:27.229	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392728/1431568
2017-10-29 21:38:34.603	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392748/1431568
2017-10-29 21:38:40.072	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392768/1431568
2017-10-29 21:38:40.463	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 84.227.31.220:18080
2017-10-29 21:38:45.785	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392788/1431568
2017-10-29 21:38:48.893	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 184.171.194.243:18080
2017-10-29 21:38:53.670	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392808/1431568
2017-10-29 21:38:56.316	[P2P2]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 113.161.184.198:18080
2017-10-29 21:39:03.632	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392828/1431568
2017-10-29 21:39:13.319	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392848/1431568
2017-10-29 21:39:19.507	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392868/1431568
2017-10-29 21:39:25.022	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392888/1431568
2017-10-29 21:39:30.382	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:834	[37.59.49.7:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-10-29 21:39:34.452	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392908/1431568
2017-10-29 21:39:41.391	[P2P9]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[37.59.49.7:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-10-29 21:39:41.391	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:851	[37.59.49.7:18080 OUT] COMMAND_TIMED_SYNC Failed
2017-10-29 21:39:45.086	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392928/1431568
2017-10-29 21:39:58.791	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392948/1431568
^[2017-10-29 21:40:05.934	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:933	returned not all requested objects (context.m_requested_objects.size()=20), dropping connection
2017-10-29 21:40:05.934	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:834	[222.189.245.140:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
^[2017-10-29 21:40:13.678	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392968/1431568
2017-10-29 21:40:14.461	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 188.162.163.60:18080
2017-10-29 21:40:19.572	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 192.150.210.200:18080
2017-10-29 21:40:28.860	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1392988/1431568
2017-10-29 21:40:38.649	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393008/1431568
2017-10-29 21:40:50.981	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393028/1431568
2017-10-29 21:41:04.265	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393048/1431568
2017-10-29 21:41:04.912	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[62.210.104.31:58300 INC] Sync data returned a new top block candidate: 1393048 -> 1431569 [Your node is 38521 blocks (53 days) behind] 
SYNCHRONIZATION started
2017-10-29 21:41:16.576	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393068/1431569
2017-10-29 21:41:16.576	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 62.210.104.31:18080
2017-10-29 21:41:16.577	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:759	[222.189.245.140:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-10-29 21:41:16.577	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[62.210.104.31:58300 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-10-29 21:41:16.577	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:808	[222.189.245.140:18080 OUT] COMMAND_HANDSHAKE Failed
2017-10-29 21:41:16.577	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[77.230.101.160:60993 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-10-29 21:41:17.518	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1567	[0.0.0.0:0 OUT] back ping connect failed to 77.230.101.160:18080
2017-10-29 21:41:22.578	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:834	[83.239.140.120:49799 INC] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-10-29 21:41:25.216	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:933	returned not all requested objects (context.m_requested_objects.size()=20), dropping connection
2017-10-29 21:41:25.217	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:834	[77.58.165.226:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-10-29 21:41:27.165	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393088/1431569
2017-10-29 21:41:35.073	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393108/1431569
2017-10-29 21:41:47.301	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393128/1431569
2017-10-29 21:41:48.434	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:914	[173.239.240.184:55877 INC] sent wrong NOTIFY_RESPONSE_GET_OBJECTS: block with id=7950ee62a7f070842535c9f642d3b22c7960b512c896d86c1f7bbccff902c137 wasn't requested, dropping connection
2017-10-29 21:41:50.786	[P2P0]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[83.239.140.120:49799 INC] [levin_protocol] -->> start_outer_call failed
2017-10-29 21:41:50.790	[P2P0]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[83.239.140.120:49799 INC] [levin_protocol] -->> start_outer_call failed
2017-10-29 21:41:53.143	[P2P4]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[163.172.18.61:41890 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-10-29 21:42:00.702	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393148/1431569
2017-10-29 21:42:10.689	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393168/1431569
2017-10-29 21:42:21.992	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393188/1431569
2017-10-29 21:42:27.145	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:1629	[94.242.227.160:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-10-29 21:42:27.655	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:834	[184.171.194.243:57726 INC] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-10-29 21:42:34.656	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393208/1431569
2017-10-29 21:42:47.019	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393228/1431569
2017-10-29 21:42:57.947	[P2P2]	WARN 	net.p2p	src/p2p/net_node.inl:780	[94.176.233.212:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
2017-10-29 21:42:57.948	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:808	[94.176.233.212:18080 OUT] COMMAND_HANDSHAKE Failed
^C2017-10-29 21:42:58.733	[SRV_MAIN]	WARN 	net.p2p	src/p2p/net_node.inl:834	[98.235.213.182:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-10-29 21:42:58.957	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[37.59.49.7:18080 OUT]  Synced 1393248/1431567
2017-10-29 21:42:58.961	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2017-10-29 21:42:59.002	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
2017-10-29 21:42:59.002	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:145	Node stopped.
2017-10-29 21:42:59.002	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-10-29 21:42:59.002	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-10-29 21:42:59.260	[SRV_MAIN]	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-10-29 21:42:59.418	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-10-29 21:42:59.418	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
```

[monero-gui-src-0.11.1.log](https://github.com/monero-project/monero-core/files/1425521/monero-gui-src-0.11.1.log)


```
$ ./build/release/bin/monero-wallet-gui
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml:210:25: QML ListView: Binding loop detected for property "model"
qrc:///pages/Settings.qml:503: TypeError: Cannot read property 'walletCreationHeight' of undefined
qrc:///pages/Settings.qml:520: TypeError: Cannot read property 'walletCreationHeight' of undefined
2017-10-29 21:41:12.131	    7fcfb7961700	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-10-29 21:41:12.131	    7fcfb7961700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-10-29 21:41:12.131	    7fcfb7961700	WARN 	net.http	src/wallet/wallet_errors.h:707	/home/stelarov/ext/hacking/mining/monero-gui-src/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-10-29 21:41:12.133	    7fcfb7961700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
qml: Error opening wallet with empty password:  invalid password
qrc:///pages/Settings.qml:520: TypeError: Cannot read property 'walletCreationHeight' of undefined
qrc:///pages/Settings.qml:503: TypeError: Cannot read property 'walletCreationHeight' of undefined
2017-10-29 21:41:12.202	    7fcfb7961700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2017-10-29 21:41:16.618	    7fcfb7961700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 8UbFQVH7LTJeeQyyWKopC2AEp4PEMjXMdLH9P5EwpQysEAGRvkFTjNYMmyZPh1XnyYHxVq61Rw3d3vj85ZFjH8pUMpLoUD
```

![gui_from_src_v0 11 1 0](https://user-images.githubusercontent.com/908356/32148699-91a7bbf2-bd03-11e7-96ee-28bca323657c.png)




## downrightmike | 2017-12-19T05:07:06+00:00
I have this same issue. I put it in a VM, WMWare Win7. First time I only gave it 40GB of disk space and that ran out b/c the DB. This has happened now a second time, but occurs after a unclean shutdown, host crashed. Even though the host and VM are fine w/o addtional errors in EventViewer, the daemon won't start. 

## dEBRUYNE-1 | 2017-12-19T12:39:05+00:00
>This has happened now a second time, but occurs after a unclean shutdown, host crashed. 

This probably corrupted the chain. 

## erciccione | 2018-11-18T13:57:59+00:00
Related to old version. Please reopen if problem still exists in 0.13.04

+resolved

## ionics | 2018-12-17T14:07:03+00:00
@erciccione 

Bug report: Still happens in v0.13.04-relase after vm-system crash.

check for word "ERROR" in log below...
=> 'Got block with unknown parent which was not requested'

invoke command used:
./monerod --detach --log-file ~/.bitmonero/monerod.log --limit-rate 10000 --block-sync-size 10 --log-level 1 --db-salvage

./monerod still downloading blockchain BUT "syncing" does not work as:
-rw-r--r-- 1 user user 35680604160 Dec 17 14:42 data.mdb
=> the file size of data.mdb is not growing... so the ./monerod sync got stuck again and i have to start over again from the beginning which will last for 1+ days ;-(

For future versions it would be great to have some mechanism where monerod would be able to continue with syncing and data.mdb build even after system crash/outage.



Version:
`./monerod --version

`2018-12-17 13:54:24,159 INFO  [default] Page size: 4096
Monero 'Beryllium Bullet' (v0.13.0.4-release)

tail -f .bitmonero/monerod.log
----------------------------------------
```
2018-12-17 13:52:24.436 [P2P8]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1526    [91.187.128.249:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=10, txs.size()=0requested blocks count=10 / 10 from 1457403, first hash <8d09b1938f9c68550f7faccd222387a0da00bbc8a34013b115d27a530a84121b>
2018-12-17 13:52:24.666 [P2P2]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:841     [176.37.20.170:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (10 blocks, 0 txes)
2018-12-17 13:52:24.669 [P2P2]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [176.37.20.170:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-17 13:52:24.669 [P2P2]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1558    [176.37.20.170:18080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=32, start_from_current_chain 0
2018-12-17 13:52:24.773 [P2P2]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:841     [139.18.109.249:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (10 blocks, 0 txes)
2018-12-17 13:52:24.782 [P2P2]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [139.18.109.249:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-17 13:52:24.782 [P2P2]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1558    [139.18.109.249:18080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=32, start_from_current_chain 0
2018-12-17 13:52:24.821 [P2P8]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1621    [176.37.20.170:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10000, m_start_height=1457402, m_total_height=1728553
2018-12-17 13:52:24.824 [P2P8]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1526    [176.37.20.170:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=10, txs.size()=0requested blocks count=10 / 10 from 1457413, first hash <030c3e9eb691583d35271fedfdaee7bc9e5df97d2cc5d0a5053d745334797725>
2018-12-17 13:52:25.189 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1621    [139.18.109.249:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10000, m_start_height=1449885, m_total_height=1728553
2018-12-17 13:52:25.193 [P2P7]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1526    [139.18.109.249:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=10, txs.size()=0requested blocks count=10 / 10 from 1449885, first hash <a201e293d54c5a31408b3fe1a3cac611aba97abbb5be47b9a69d27d28e6a4451>
2018-12-17 13:52:25.365 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:841     [176.37.20.170:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (10 blocks, 0 txes)
2018-12-17 13:52:25.368 [P2P7]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [176.37.20.170:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-17 13:52:25.368 [P2P7]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1558    [176.37.20.170:18080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=32, start_from_current_chain 0
2018-12-17 13:52:25.503 [P2P4]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1621    [176.37.20.170:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10000, m_start_height=1457422, m_total_height=1728553
2018-12-17 13:52:25.506 [P2P4]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1526    [176.37.20.170:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=10, txs.size()=0requested blocks count=10 / 10 from 1457423, first hash <23b824806c39d38a1cf18a699d3cf305f50b484b1859137484ea846b60affba5>
2018-12-17 13:52:25.538 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:841     [91.187.128.249:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (10 blocks, 0 txes)
2018-12-17 13:52:25.540 [P2P7]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [91.187.128.249:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-17 13:52:25.540 [P2P7]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1558    [91.187.128.249:18080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=32, start_from_current_chain 0
2018-12-17 13:52:25.756 [P2P3]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1621    [91.187.128.249:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10000, m_start_height=1457412, m_total_height=1728553
2018-12-17 13:52:25.760 [P2P3]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1526    [91.187.128.249:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=10, txs.size()=0requested blocks count=10 / 10 from 1457433, first hash <cf846cce4b636b2af40c542032ea1d796024f113b3c2a374faa685a9560e540b>
2018-12-17 13:52:26.218 [P2P9]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:841     [176.37.20.170:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (10 blocks, 0 txes)
2018-12-17 13:52:26.219 [P2P9]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [176.37.20.170:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-17 13:52:26.220 [P2P9]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1558    [176.37.20.170:18080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=32, start_from_current_chain 0
2018-12-17 13:52:26.334 [P2P8]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:841     [139.18.109.249:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (10 blocks, 0 txes)
2018-12-17 13:52:26.335 [P2P8]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [139.18.109.249:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-17 13:52:26.336 [P2P8]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1558    [139.18.109.249:18080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=32, start_from_current_chain 0
2018-12-17 13:52:26.351 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1621    [176.37.20.170:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10000, m_start_height=1457432, m_total_height=1728553
2018-12-17 13:52:26.355 [P2P7]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1526    [176.37.20.170:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=10, txs.size()=0requested blocks count=10 / 10 from 1457443, first hash <0d67f616f1969fadf0fc9866b60453bcbd8bde1daa9d492a134ede66d56b1e6d>
2018-12-17 13:52:26.604 [P2P9]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:841     [91.187.128.249:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (10 blocks, 0 txes)
2018-12-17 13:52:26.606 [P2P9]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [91.187.128.249:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-17 13:52:26.606 [P2P9]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1558    [91.187.128.249:18080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=32, start_from_current_chain 0
2018-12-17 13:52:26.811 [P2P0]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1621    [91.187.128.249:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10000, m_start_height=1457442, m_total_height=1728553
2018-12-17 13:52:26.815 [P2P0]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1526    [91.187.128.249:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=10, txs.size()=0requested blocks count=10 / 10 from 1457453, first hash <2c5633945c27957a10e9ec21366ca9e8cf83388e9eb0183c3d6602043553368f>
2018-12-17 13:52:26.840 [P2P4]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1621    [139.18.109.249:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10000, m_start_height=1449894, m_total_height=1728553
2018-12-17 13:52:26.843 [P2P4]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1526    [139.18.109.249:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=10, txs.size()=0requested blocks count=10 / 10 from 1449894, first hash <3376f1164242f3e63510a58a7b9c03f6bdc106b0768882741a3f2dc400dce2aa>
2018-12-17 13:52:27.069 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:841     [176.37.20.170:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (10 blocks, 0 txes)
2018-12-17 13:52:27.076 [P2P7]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [176.37.20.170:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-17 13:52:27.076 [P2P7]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1558    [176.37.20.170:18080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=32, start_from_current_chain 0

```

System Info:


lsb_release --all

- No LSB modules are available.
- Distributor ID: Debian
- Description:    Debian GNU/Linux 9.6 (stretch)
- Release:        9.6
- Codename:       stretch


Kind regards,
Raphael

## dEBRUYNE-1 | 2018-12-17T14:57:24+00:00
@ionics: Fwiw, adding `--db-sync-mode=safe` as startup flag should ensure that the daemon guards against corruption in case of an unexpected shutdown. 

## ionics | 2018-12-18T10:27:12+00:00
@dEBRUYNE-1 
thank you for your advice: i did add --db-sync-mode=safe to /.monerd startup command

Command:
./monerod --detach --log-file ~/.bitmonero/monerod.log --limit-rate 10000 --db-sync-mode=safe --log-level 2 

BUT LOG shows after some time (first hours of syncing with fresh data.mdb everything runs smooth than...):
```
2018-12-18 10:16:57.446 [P2P8]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [74.134.176.35:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:16:59.228 [P2P8]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [76.168.134.232:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:01.697 [P2P7]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [178.128.13.239:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:01.820 [P2P7]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [158.69.255.67:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:02.720 [P2P8]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [74.134.176.35:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:03.709 [P2P6]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [76.168.134.232:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:04.342 [P2P1]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [158.69.255.67:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:06.250 [P2P2]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [76.168.134.232:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:06.445 [P2P1]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [158.69.255.67:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:06.527 [P2P4]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [74.134.176.35:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:07.184 [P2P9]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1604 Block recognized as orphaned and rejected, id = <5bb7c61fe11f89406dd846c9ef75638c5b331e911859b55c637e4b9e17eac886>, height 1537662, parent in alt 0, parent in main 0 (parent <6b4542e1dd55f285885b8e17e156a82e57bf422b4a6ac5a84503dc0d78624c74>, current top <54b13c85eddaaeb358e6a8274aa4db17a8ee10375b956a7d64d4ea11fb20ffb5>, chain height 1537661)
2018-12-18 10:17:07.945 [P2P9]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [178.128.13.239:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:08.167 [P2P1]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [158.69.255.67:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:10.279 [P2P8]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [76.168.134.232:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:12.470 [P2P5]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [158.69.255.67:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:12.982 [P2P6]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [178.128.13.239:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:13.565 [P2P4]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [74.134.176.35:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:15.317 [P2P6]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [158.69.255.67:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:17.032 [P2P3]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [76.168.134.232:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:17.672 [P2P1]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [158.69.255.67:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:21.327 [P2P2]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [76.168.134.232:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:22.428 [P2P0]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [158.69.255.67:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2018-12-18 10:17:23.279 [P2P1]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1037    [178.128.13.239:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
```

Any additional advice?
Right now with  v0.13.04-relase i am unable to create a full node on debian 9 stretch.

it performed well up to ~ 46GigaByte than it got stuck:
user@vm-monero:~/.bitmonero/lmdb$ ls -ltcha
total 46G
```
-rw-r--r-- 1 user user 8.0K Dec 18 11:21 lock.mdb
drwxr-xr-x 3 user user 4.0K Dec 18 10:42 ..
-rw-r--r-- 1 user user 46G Dec 18 09:23 data.mdb
drwxr-xr-x 2 user user 4.0K Dec 17 22:40 .
```

After gracerfull shutdown /.monerd exit

and restart with above command ERROR-Log reports:
```
2018-12-18 10:25:46.436     7f54c521b780        ERROR   net.p2p src/p2p/net_node.inl:2056       UPNP_AddPortMapping failed, error: ConflictInMappingEntry
2018-12-18 10:25:52.993 [P2P1]  WARN    net.p2p src/p2p/net_node.inl:733        [133.242.137.166:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2018-12-18 10:25:58.054 [P2P5]  WARN    net.p2p src/p2p/net_node.inl:733        [78.19.65.156:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2018-12-18 10:26:08.257 [P2P1]  WARN    net.p2p src/p2p/net_node.inl:733        [133.242.137.166:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2018-12-18 10:26:14.283 [P2P9]  WARN    net.p2p src/p2p/net_node.inl:1642       [78.19.65.156:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
```




 

## erciccione | 2018-12-18T15:24:53+00:00
@ionics I asked @moneromooo-monero about your issue. Answer:

>I see some repeated sync retries, that's likely fixed in the pruning branch.

So, this will be likely fixed shortly, once the pruning feature is tested and merged

# Action History
- Created by: chamalis | 2017-10-11T08:52:56+00:00
- Closed at: 2018-11-18T14:09:29+00:00
