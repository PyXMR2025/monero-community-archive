---
title: '[TREZOR T] Can''t create transaction in Trezor T with passphrase'
source_url: https://github.com/monero-project/monero-gui/issues/2920
author: Alfavio
assignees: []
labels: []
created_at: '2020-05-21T07:26:04+00:00'
updated_at: '2020-05-21T10:10:28+00:00'
type: issue
status: closed
closed_at: '2020-05-21T10:10:28+00:00'
---

# Original Description
Hi,

I activated passphrase on my Trezor T wallet and now I can't create transaction in the Monero GUI.

**Monero GUI info**:
GUI version: v0.15.0.5 (Qt 5.14.2)
Embedded Monero version: v0.15.0.5
Wallet mode: Advanced modeOpenGL

**Trezor Firmware version:**
2.3.0 

**monero-wallet-gui.log**:
```
2020-05-21 07:17:55.211	    628a2a216700	TRACE	device.trezor	src/device_trezor/device_trezor_base.cpp:203	Ask for UNLOCKING for device  in thread 
2020-05-21 07:17:55.211	    628a2a216700	TRACE	device.trezor	src/device_trezor/device_trezor_base.cpp:205	Device  UNLOCKed
2020-05-21 07:17:55.211	    628a2a216700	INFO	wallet.wallet2	src/wallet/wallet2.cpp:937	Decrypted payment ID: <0000000000000000>
2020-05-21 07:17:55.211	    628a2a216700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:10393	Using v10 rules
2020-05-21 07:17:55.379	    628a2a216700	TRACE	net	../monero/contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 197
2020-05-21 07:17:55.380	    628a2a216700	TRACE	net.http	../monero/contrib/epee/include/net/http_client.h:785	http_stream_filter::parse_cached_header(*)
2020-05-21 07:17:55.420	    628a2a216700	TRACE	net	../monero/contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 319
2020-05-21 07:17:55.889	    628a2a216700	TRACE	net	../monero/contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 591
2020-05-21 07:17:55.889	    628a2a216700	TRACE	net.http	../monero/contrib/epee/include/net/http_client.h:785	http_stream_filter::parse_cached_header(*)
2020-05-21 07:17:56.316	    628a2a216700	TRACE	net	../monero/contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 184
2020-05-21 07:17:56.317	    628a2a216700	TRACE	net.http	../monero/contrib/epee/include/net/http_client.h:785	http_stream_filter::parse_cached_header(*)
2020-05-21 07:17:56.317	    628a2a216700	DEBUG	device.trezor	src/device_trezor/device_trezor_base.cpp:455	on_passhprase_request, on device: 0
2020-05-21 07:17:56.317	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-05-21 07:17:56.317	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x114) [0xeda8d5d781e]:__cxa_throw+0x114) [0xeda8d5d781e]
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/bin/monero-wallet-gui(+0x290aaf) [0xeda8d6e8aaf] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /usr/bin/monero-wallet-gui(+0x314da9) [0xeda8d76cda9] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /usr/bin/monero-wallet-gui(+0x314dee) [0xeda8d76cdee] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /usr/bin/monero-wallet-gui(+0x7280c1) [0xeda8db800c1] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /usr/bin/monero-wallet-gui(+0x7287ba) [0xeda8db807ba] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /usr/bin/monero-wallet-gui(+0x64250b) [0xeda8da9a50b] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /usr/bin/monero-wallet-gui(+0x634deb) [0xeda8da8cdeb] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /usr/bin/monero-wallet-gui(+0x6377f5) [0xeda8da8f7f5] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/bin/monero-wallet-gui(+0x3bf7a6) [0xeda8d8177a6] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /usr/bin/monero-wallet-gui(+0x28e7ad) [0xeda8d6e67ad] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /usr/bin/monero-wallet-gui(+0x28f197) [0xeda8d6e7197] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] /usr/bin/monero-wallet-gui(+0x28d518) [0xeda8d6e5518] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] /usr/bin/monero-wallet-gui(+0x202016) [0xeda8d65a016] 
2020-05-21 07:17:56.318	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] /usr/bin/monero-wallet-gui(+0x202169) [0xeda8d65a169] 
2020-05-21 07:17:56.319	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] /usr/bin/monero-wallet-gui(+0x224de2) [0xeda8d67cde2] 
2020-05-21 07:17:56.319	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] /usr/lib/libQt5Core.so.5(+0xcd001) [0x628a4be7e001] 
2020-05-21 07:17:56.319	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] /usr/lib/libQt5Core.so.5(+0xc9dd5) [0x628a4be7add5] 
2020-05-21 07:17:56.319	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] /usr/lib/libpthread.so.0(+0x9421) [0x628a4bd98421] 
2020-05-21 07:17:56.319	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] /usr/lib/libc.so.6(clone+0x42) [0x628a4b989b82] 
2020-05-21 07:17:56.319	    628a2a216700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-05-21 07:17:56.319	    628a2a216700	DEBUG	WalletAPI	src/wallet/api/wallet.cpp:2165	startRefresh: refresh started/resumed...
2020-05-21 07:17:56.319	    628a11d88700	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2113	refreshThreadFunc: refresh lock acquired...
2020-05-21 07:17:56.319	    628a11d88700	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2114	refreshThreadFunc: m_refreshEnabled: 1
2020-05-21 07:17:56.319	    628a11d88700	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2115	refreshThreadFunc: m_status: 1
2020-05-21 07:17:56.319	    628a11d88700	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2116	refreshThreadFunc: m_refreshShouldRescan: 0
2020-05-21 07:17:56.319	    628a11d88700	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2118	refreshThreadFunc: refreshing...
2020-05-21 07:17:56.319	    628a11d88700	TRACE	WalletAPI	src/wallet/api/wallet.cpp:2131	doRefresh: doRefresh, rescan = 0
2020-05-21 07:17:56.319	    628a11d88700	TRACE	wallet.wallet2	src/wallet/wallet2.cpp:2834	update_pool_state start
2020-05-21 07:17:56.330	    628a48c39ac0	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Transaction created
2020-05-21 07:17:56.330	    628a48c39ac0	DEBUG	frontend	src/wallet/api/wallet.cpp:402	Hiding processing splash
2020-05-21 07:17:56.334	    628a48c39ac0	ERROR	frontend	src/wallet/api/wallet.cpp:414	Can't create transaction:  unexpected error: Not supported
2020-05-21 07:17:56.335	    628a48c39ac0	WARNING	frontend	src/wallet/api/wallet.cpp:410	"Could not convert argument 0 at"
2020-05-21 07:17:56.335	    628a48c39ac0	WARNING	frontend	src/wallet/api/wallet.cpp:410		 "onTransactionCreated@qrc:/main.qml:784"
2020-05-21 07:17:56.335	    628a48c39ac0	WARNING	frontend	src/wallet/api/wallet.cpp:410	"Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
2020-05-21 07:17:56.335	    628a48c39ac0	WARNING	frontend	src/wallet/api/wallet.cpp:410	"This will throw a JavaScript TypeError in future releases of Qt!"
2020-05-21 07:17:56.495	    628a11d88700	TRACE	net	../monero/contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 197
2020-05-21 07:17:56.495	    628a11d88700	TRACE	net.http	../monero/contrib/epee/include/net/http_client.h:785	http_stream_filter::parse_cached_header(*)
2020-05-21 07:17:56.537	    628a11d88700	TRACE	net	../monero/contrib/epee/include/net/net_helper.h:460	READ ENDS: Success. bytes_tr: 856
2020-05-21 07:17:56.537	    628a11d88700	TRACE	wallet.wallet2	src/wallet/wallet2.cpp:2856	update_pool_state got pool
2020-05-21 07:17:56.538	    628a11d88700	TRACE	wallet.wallet2	src/wallet/wallet2.cpp:2913	update_pool_state done first loop
2020-05-21 07:17:56.538	    628a11d88700	TRACE	wallet.wallet2	src/wallet/wallet2.cpp:2922	update_pool_state done second loop
```
![Screenshot from 2020-05-21 09-19-24](https://user-images.githubusercontent.com/5478075/82533961-da84e000-9b33-11ea-91b6-3c249ffeb2ed.png)


# Discussion History
## rating89us | 2020-05-21T10:04:29+00:00
https://www.reddit.com/r/monerosupport/comments/gcaat1/a_note_for_trezor_monero_users/

## Alfavio | 2020-05-21T10:10:14+00:00
Thank you :heart: 

# Action History
- Created by: Alfavio | 2020-05-21T07:26:04+00:00
- Closed at: 2020-05-21T10:10:28+00:00
