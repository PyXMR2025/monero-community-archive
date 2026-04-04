---
title: '[Trezor] - Error after clicking Payment proof button'
source_url: https://github.com/monero-project/monero-gui/issues/2183
author: rating89us
assignees: []
labels:
- resolved
created_at: '2019-05-30T12:52:24+00:00'
updated_at: '2019-09-01T01:36:31+00:00'
type: issue
status: closed
closed_at: '2019-09-01T01:36:31+00:00'
---

# Original Description
When I click the P button on Transactions tab, the window "proceed to device" is not displayed and I get the following error:
`2019-05-30 12:00:58.739	E !received. THROW EXCEPTION: error::wallet_internal_error`

I receive the message "Do you really want to start refresh?" on Trezor, and when I confirm, I get the payment proof window. But it seems payment proof is wrong.

I'm using GUI last build, Ubuntu 18.04, Trezor 2.1.0

@ph4r05 

# Discussion History
## ph4r05 | 2019-05-31T08:50:08+00:00
Thanks for the report! If you could pls increase the log level and post more logs around the `error::wallet_internal_error` it would be great!


## rating89us | 2019-05-31T10:15:21+00:00
```
2019-05-31 10:03:20.624	W app startd (log: /home/asuspc/.bitmonero/monero-wallet-gui.log)
2019-05-31 10:03:20.625	W Qt:5.9.5 GUI:v0.14.0.0-206-ga5a90c7 | screen: 1920x1080 - dpi: 96 - ratio:0.637479
2019-05-31 10:03:21.137	W Failed to determine whether address '' is local, assuming not
2019-05-31 10:03:21.137	W Failed to determine whether address '' is local, assuming not
2019-05-31 10:03:21.415	W libpng warning: iCCP: known incorrect sRGB profile
2019-05-31 10:03:21.699	W file:///usr/lib/x86_64-linux-gnu/qt5/qml/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2019-05-31 10:03:24.129	D setLanguage   "en"
2019-05-31 10:03:24.137	D transfer page loaded
2019-05-31 10:03:24.139	I Generating SSL certificate
2019-05-31 10:03:24.793	D opening wallet at:  /home/asuspc/Monero/wallets/asuspc/asuspc , network type:  mainnet
2019-05-31 10:03:24.793	D Displaying processing splash
2019-05-31 10:03:24.794	D Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type, quint64): opening wallet at /home/asuspc/Monero/wallets/asuspc/asuspc, nettype = 0 
2019-05-31 10:03:24.794	D Device 0 Created
2019-05-31 10:03:24.795	D onSetWallet
2019-05-31 10:03:24.795	T refreshThreadFunc: starting refresh thread
2019-05-31 10:03:24.795	T refreshThreadFunc: waiting for refresh...
2019-05-31 10:03:24.795	I ringdb path set to /home/asuspc/.shared-ringdb
2019-05-31 10:03:24.836	W Account on device. Initing device...
2019-05-31 10:03:24.837	D Enumerating Trezor devices...
2019-05-31 10:03:24.837	D Reconnecting...
2019-05-31 10:03:24.838	T READ ENDS: Success. bytes_tr: 266
2019-05-31 10:03:24.838	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:24.842	T Libusb devices: 11
2019-05-31 10:03:24.842	T Found Trezor device: 4617:21441 dev_idx 1
2019-05-31 10:03:26.343	T Closing Trezor:UdpTransport
2019-05-31 10:03:26.343	D Enumeration yielded 2 Trezor devices
2019-05-31 10:03:26.343	D   device: BridgeTransport<path=bridge:1, info={"path":"1","vendor":4617,"product":21441,"debug":false,"session":null,"debugSession":null}, session=None>
2019-05-31 10:03:26.343	D   device: WebUsbTransport<path=webusb:005:2, vendorId=4617, productId=21441, deviceType=TrezorT>
2019-05-31 10:03:26.343	D Device Match: bridge:1
2019-05-31 10:03:26.343	D Reconnecting...
2019-05-31 10:03:26.649	T READ ENDS: Success. bytes_tr: 188
2019-05-31 10:03:26.649	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:26.649	D account_keys::set_device device type: N2hw6trezor13device_trezorE
2019-05-31 10:03:26.691	T READ ENDS: Success. bytes_tr: 385
2019-05-31 10:03:26.691	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:26.984	T READ ENDS: Success. bytes_tr: 188
2019-05-31 10:03:26.984	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:26.984	D on_button_request, code: 14
2019-05-31 10:03:26.990	D Displaying processing splash
2019-05-31 10:03:28.234	T READ ENDS: Success. bytes_tr: 188
2019-05-31 10:03:28.235	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:28.235	D on_passhprase_request, on device: 1
2019-05-31 10:03:28.235	D onDevicePassphraseRequest
2019-05-31 10:03:28.241	D Displaying processing splash
2019-05-31 10:03:28.788	T READ ENDS: Success. bytes_tr: 317
2019-05-31 10:03:28.789	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:28.789	D on_passhprase_state_request
2019-05-31 10:03:29.428	T READ ENDS: Success. bytes_tr: 379
2019-05-31 10:03:29.429	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:29.429	T Get address response received
2019-05-31 10:03:29.429	W Device inited...
2019-05-31 10:03:29.476	I caching ringdb key
2019-05-31 10:03:29.496	W Loaded wallet keys file, with public address: (deleted)
2019-05-31 10:03:29.497	I Trying to decrypt cache data
2019-05-31 10:03:29.545	E No message store file found: /home/asuspc/Monero/wallets/asuspc/asuspc.mms
2019-05-31 10:03:29.545	D Refreshing addressbook
2019-05-31 10:03:29.545	D Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type, quint64): opened wallet: (deleted), status: 0
2019-05-31 10:03:29.545	D AddressBook
2019-05-31 10:03:29.545	D getAll
2019-05-31 10:03:29.545	D Subaddress
2019-05-31 10:03:29.545	D getAll
2019-05-31 10:03:29.545	D SubaddressAccount
2019-05-31 10:03:29.545	D getAll
2019-05-31 10:03:29.557	D Hiding processing splash
2019-05-31 10:03:29.559	D >>> wallet opened: Wallet(0x7f35e0271940)
2019-05-31 10:03:29.559	D Recovering from seed:  false
2019-05-31 10:03:29.559	D restore Height 0
2019-05-31 10:03:29.560	D Address 'localhost:18081' is local
2019-05-31 10:03:29.560	D Address 'localhost:18081' is local
2019-05-31 10:03:29.560	D initializing with daemon address:  localhost:18081
2019-05-31 10:03:29.560	D "initAsync: localhost:18081"
2019-05-31 10:03:29.560	D init non async
2019-05-31 10:03:29.560	I setting daemon to localhost:18081
2019-05-31 10:03:29.560	I Generating SSL certificate
2019-05-31 10:03:29.619	D trimming to 1775599, offset 1775600
2019-05-31 10:03:30.601	D Address 'localhost:18081' is local
2019-05-31 10:03:30.608	D init async finished - starting refresh
2019-05-31 10:03:30.608	D Checking connection status
2019-05-31 10:03:30.608	D startRefresh: refresh started/resumed...
2019-05-31 10:03:30.608	T refreshThreadFunc: refresh lock acquired...
2019-05-31 10:03:30.608	T refreshThreadFunc: m_refreshEnabled: 1
2019-05-31 10:03:30.608	T refreshThreadFunc: m_status: 0
2019-05-31 10:03:30.608	T refreshThreadFunc: m_refreshShouldRescan: 0
2019-05-31 10:03:30.608	T refreshThreadFunc: refreshing...
2019-05-31 10:03:30.608	T doRefresh: doRefresh, rescan = 0
2019-05-31 10:03:30.620	W SSL peer has not been verified
2019-05-31 10:03:30.620	W SSL peer has not been verified
2019-05-31 10:03:30.621	D SSL handshake success
2019-05-31 10:03:30.622	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:03:30.622	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:30.622	T READ ENDS: Success. bytes_tr: 128
2019-05-31 10:03:30.622	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:03:30.622	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:30.622	T READ ENDS: Success. bytes_tr: 128
2019-05-31 10:03:30.623	T READ ENDS: Success. bytes_tr: 161
2019-05-31 10:03:30.623	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:30.623	T READ ENDS: Success. bytes_tr: 1318
2019-05-31 10:03:30.624	T READ ENDS: Success. bytes_tr: 171
2019-05-31 10:03:30.624	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:30.624	D NEW STATUS  Wallet::ConnectionStatus(ConnectionStatus_Connected)
2019-05-31 10:03:30.624	T READ ENDS: Success. bytes_tr: 16384
2019-05-31 10:03:30.624	D Wallet connection status changed 1
2019-05-31 10:03:30.624	T READ ENDS: Success. bytes_tr: 8577
2019-05-31 10:03:30.625	D Address 'localhost:18081' is local
2019-05-31 10:03:30.626	D Address 'localhost:18081' is local
2019-05-31 10:03:30.626	D Address 'localhost:18081' is local
2019-05-31 10:03:30.626	T READ ENDS: Success. bytes_tr: 170
2019-05-31 10:03:30.626	D Reconnecting...
2019-05-31 10:03:30.626	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:30.626	T READ ENDS: Success. bytes_tr: 3816
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Device  LOCKed
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Device  UNLOCKed
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Device  LOCKed
2019-05-31 10:03:30.627	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.627	T Device  UNLOCKed
2019-05-31 10:03:30.627	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.627	T Device  LOCKed
2019-05-31 10:03:30.628	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.628	T Device  UNLOCKed
2019-05-31 10:03:30.628	T Device  LOCKed
2019-05-31 10:03:30.628	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.628	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.628	T Device  UNLOCKed
2019-05-31 10:03:30.628	T Device  LOCKed
2019-05-31 10:03:30.628	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.628	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.628	T Device  UNLOCKed
2019-05-31 10:03:30.628	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.628	T Device  LOCKed
2019-05-31 10:03:30.628	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.628	T Device  UNLOCKed
2019-05-31 10:03:30.628	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.629	T Device  LOCKed
2019-05-31 10:03:30.629	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.629	T Device  UNLOCKed
2019-05-31 10:03:30.629	T Device  LOCKed
2019-05-31 10:03:30.629	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.629	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.629	T Device  UNLOCKed
2019-05-31 10:03:30.629	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.629	T Device  LOCKed
2019-05-31 10:03:30.629	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.629	T Device  UNLOCKed
2019-05-31 10:03:30.629	T Device  LOCKed
2019-05-31 10:03:30.629	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.629	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.629	T Device  UNLOCKed
2019-05-31 10:03:30.629	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.629	T Device  LOCKed
2019-05-31 10:03:30.630	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.630	T Device  UNLOCKed
2019-05-31 10:03:30.630	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.630	T Device  LOCKed
2019-05-31 10:03:30.630	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.630	T Device  UNLOCKed
2019-05-31 10:03:30.630	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.630	T Device  LOCKed
2019-05-31 10:03:30.630	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.630	T Device  UNLOCKed
2019-05-31 10:03:30.630	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.630	T Device  LOCKed
2019-05-31 10:03:30.631	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.631	T Device  UNLOCKed
2019-05-31 10:03:30.631	T Device  LOCKed
2019-05-31 10:03:30.631	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.631	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.631	T Device  UNLOCKed
2019-05-31 10:03:30.631	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.631	T Device  LOCKed
2019-05-31 10:03:30.631	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.631	T Device  UNLOCKed
2019-05-31 10:03:30.631	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.631	T Device  LOCKed
2019-05-31 10:03:30.632	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.632	T Device  UNLOCKed
2019-05-31 10:03:30.632	T Device  LOCKed
2019-05-31 10:03:30.632	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.632	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.632	T Device  UNLOCKed
2019-05-31 10:03:30.632	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.632	T Device  LOCKed
2019-05-31 10:03:30.632	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.632	T Device  UNLOCKed
2019-05-31 10:03:30.632	T Device  LOCKed
2019-05-31 10:03:30.632	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.632	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.632	T Device  UNLOCKed
2019-05-31 10:03:30.632	T Device  LOCKed
2019-05-31 10:03:30.633	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.633	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.633	T Device  UNLOCKed
2019-05-31 10:03:30.633	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.633	T Device  LOCKed
2019-05-31 10:03:30.633	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.633	T Device  UNLOCKed
2019-05-31 10:03:30.633	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.633	T Device  LOCKed
2019-05-31 10:03:30.633	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.633	T Device  UNLOCKed
2019-05-31 10:03:30.633	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.633	T Device  LOCKed
2019-05-31 10:03:30.633	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.633	T Device  UNLOCKed
2019-05-31 10:03:30.633	T Device  LOCKed
2019-05-31 10:03:30.633	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.634	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.634	T Device  UNLOCKed
2019-05-31 10:03:30.634	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.634	T Device  LOCKed
2019-05-31 10:03:30.634	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.634	T Device  UNLOCKed
2019-05-31 10:03:30.634	T Device  LOCKed
2019-05-31 10:03:30.634	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.634	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.634	T Device  UNLOCKed
2019-05-31 10:03:30.634	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.634	T Device  LOCKed
2019-05-31 10:03:30.635	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.635	T Device  UNLOCKed
2019-05-31 10:03:30.635	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.635	T Device  LOCKed
2019-05-31 10:03:30.635	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.635	T Device  UNLOCKed
2019-05-31 10:03:30.635	T Device  LOCKed
2019-05-31 10:03:30.635	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.639	W SSL peer has not been verified
2019-05-31 10:03:30.639	W SSL peer has not been verified
2019-05-31 10:03:30.639	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.639	T Device  UNLOCKed
2019-05-31 10:03:30.639	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.639	T Device  LOCKed
2019-05-31 10:03:30.639	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.639	T Device  UNLOCKed
2019-05-31 10:03:30.639	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.639	T Device  LOCKed
2019-05-31 10:03:30.639	D SSL handshake success
2019-05-31 10:03:30.640	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.640	T Device  UNLOCKed
2019-05-31 10:03:30.640	T Device  LOCKed
2019-05-31 10:03:30.640	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.640	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:03:30.640	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:30.640	T READ ENDS: Success. bytes_tr: 532
2019-05-31 10:03:30.640	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.640	T Device  UNLOCKed
2019-05-31 10:03:30.640	T Device  LOCKed
2019-05-31 10:03:30.640	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.640	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.640	T Device  UNLOCKed
2019-05-31 10:03:30.640	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.640	T Device  LOCKed
2019-05-31 10:03:30.640	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.640	T Device  UNLOCKed
2019-05-31 10:03:30.640	T Device  LOCKed
2019-05-31 10:03:30.640	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.641	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.641	T Device  UNLOCKed
2019-05-31 10:03:30.641	T Device  LOCKed
2019-05-31 10:03:30.641	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.641	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.641	T Device  UNLOCKed
2019-05-31 10:03:30.641	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.641	T Device  LOCKed
2019-05-31 10:03:30.641	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.641	T Device  UNLOCKed
2019-05-31 10:03:30.641	T Device  LOCKed
2019-05-31 10:03:30.641	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.641	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.641	T Device  UNLOCKed
2019-05-31 10:03:30.641	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.641	T Device  LOCKed
2019-05-31 10:03:30.642	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.642	T Device  UNLOCKed
2019-05-31 10:03:30.642	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.642	T Device  LOCKed
2019-05-31 10:03:30.642	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.642	T Device  UNLOCKed
2019-05-31 10:03:30.642	T Device  LOCKed
2019-05-31 10:03:30.642	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.642	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.642	T Device  UNLOCKed
2019-05-31 10:03:30.642	T Device  LOCKed
2019-05-31 10:03:30.642	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.642	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.642	T Device  UNLOCKed
2019-05-31 10:03:30.643	T Device  LOCKed
2019-05-31 10:03:30.643	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.643	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.643	T Device  UNLOCKed
2019-05-31 10:03:30.643	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.643	T Device  LOCKed
2019-05-31 10:03:30.643	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.643	T Device  UNLOCKed
2019-05-31 10:03:30.643	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.643	T Device  LOCKed
2019-05-31 10:03:30.643	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.643	T Device  UNLOCKed
2019-05-31 10:03:30.643	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.643	T Device  LOCKed
2019-05-31 10:03:30.644	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.644	T Device  UNLOCKed
2019-05-31 10:03:30.644	T Device  LOCKed
2019-05-31 10:03:30.644	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.644	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.644	T Device  UNLOCKed
2019-05-31 10:03:30.644	T Device  LOCKed
2019-05-31 10:03:30.644	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.644	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.644	T Device  UNLOCKed
2019-05-31 10:03:30.644	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.644	T Device  LOCKed
2019-05-31 10:03:30.645	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.645	T Device  UNLOCKed
2019-05-31 10:03:30.645	T Device  LOCKed
2019-05-31 10:03:30.645	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.645	T Device  UNLOCKed
2019-05-31 10:03:30.645	T Device  LOCKed
2019-05-31 10:03:30.645	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.645	T Device  UNLOCKed
2019-05-31 10:03:30.645	T Device  LOCKed
2019-05-31 10:03:30.645	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.645	T Device  UNLOCKed
2019-05-31 10:03:30.645	T Device  LOCKed
2019-05-31 10:03:30.646	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.646	T Device  UNLOCKed
2019-05-31 10:03:30.646	T Device  LOCKed
2019-05-31 10:03:30.646	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.646	T Device  UNLOCKed
2019-05-31 10:03:30.646	T Device  LOCKed
2019-05-31 10:03:30.646	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.646	T Device  UNLOCKed
2019-05-31 10:03:30.646	T Device  LOCKed
2019-05-31 10:03:30.646	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.646	T Device  UNLOCKed
2019-05-31 10:03:30.646	T Device  LOCKed
2019-05-31 10:03:30.646	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.646	T Device  UNLOCKed
2019-05-31 10:03:30.647	T Device  LOCKed
2019-05-31 10:03:30.647	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.647	T Device  UNLOCKed
2019-05-31 10:03:30.647	T Device  LOCKed
2019-05-31 10:03:30.647	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.647	T Device  UNLOCKed
2019-05-31 10:03:30.647	T Device  LOCKed
2019-05-31 10:03:30.647	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.647	T Device  UNLOCKed
2019-05-31 10:03:30.650	D Block is already in blockchain: ef445763e892b5fbd1578af8e535ed185c083be604f3fd3efff587e516789de5
2019-05-31 10:03:30.651	D Processed block: <09d51c32de1883bb034af3d9d70191bb1c14c9604048295f6733c26fd5a28c24>, height 1846576, 0(0/0)ms
2019-05-31 10:03:30.651	D Processed block: <c1139b8fb56c7c638a1f9ed83fd99ba82048f26f59e01ed805baefdf1268dd5c>, height 1846577, 0(0/0)ms
2019-05-31 10:03:30.651	D Processed block: <7f4987ad115c7be0150bf841b58c47e8b7e78fcbbd62cfcf8e6a866830646d62>, height 1846578, 1(0/1)ms
2019-05-31 10:03:30.652	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.652	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.652	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.652	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.652	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.652	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.652	T READ ENDS: Success. bytes_tr: 170
2019-05-31 10:03:30.652	T Device  LOCKed
2019-05-31 10:03:30.652	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:30.652	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.652	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.652	T READ ENDS: Success. bytes_tr: 3816
2019-05-31 10:03:30.652	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.652	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.652	T Device  UNLOCKed
2019-05-31 10:03:30.652	T Device  LOCKed
2019-05-31 10:03:30.652	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.652	T Device  UNLOCKed
2019-05-31 10:03:30.652	T Device  LOCKed
2019-05-31 10:03:30.652	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.652	T Device  UNLOCKed
2019-05-31 10:03:30.652	T Device  LOCKed
2019-05-31 10:03:30.653	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.653	T Device  UNLOCKed
2019-05-31 10:03:30.653	T Device  LOCKed
2019-05-31 10:03:30.653	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.653	T Device  UNLOCKed
2019-05-31 10:03:30.653	T Device  LOCKed
2019-05-31 10:03:30.653	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.653	T Device  UNLOCKed
2019-05-31 10:03:30.653	T Device  LOCKed
2019-05-31 10:03:30.653	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.653	T Device  UNLOCKed
2019-05-31 10:03:30.653	T Device  LOCKed
2019-05-31 10:03:30.653	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.653	T Device  UNLOCKed
2019-05-31 10:03:30.653	T Device  LOCKed
2019-05-31 10:03:30.654	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.654	T Device  UNLOCKed
2019-05-31 10:03:30.654	D Block is already in blockchain: 7f4987ad115c7be0150bf841b58c47e8b7e78fcbbd62cfcf8e6a866830646d62
2019-05-31 10:03:30.654	T update_pool_state start
2019-05-31 10:03:30.654	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:03:30.654	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:30.654	T READ ENDS: Success. bytes_tr: 959
2019-05-31 10:03:30.654	T update_pool_state got pool
2019-05-31 10:03:30.654	T update_pool_state done first loop
2019-05-31 10:03:30.654	T update_pool_state done second loop
2019-05-31 10:03:30.654	I Found new pool tx: <c5e60c3076b060a75d0df3de16c3707a9ed5b14a7c0b4305e466a6fb0414050e>
2019-05-31 10:03:30.654	I Found new pool tx: <b24e975601366eef1959832e43aa0fd78e5a02b2f584d97851661ccc8075db11>
2019-05-31 10:03:30.654	I Found new pool tx: <7a690f50f193a6a9da647dc831260daebbbd6fdb6601ef6bac8926c786043317>
2019-05-31 10:03:30.654	I Found new pool tx: <b9e3fff1f72ef120973f626a34ccf755009aa5dbd7cf56de1255e1b4a7e4a529>
2019-05-31 10:03:30.655	I Found new pool tx: <3a17eac108c6e60313ff3347a7d4ff8a792b463248bac9fa7266d7846453cc33>
2019-05-31 10:03:30.655	I Found new pool tx: <b9e052a2292fe99deb1b11d126ec0df7c457e4cc1a642d39670fb4eac167b83c>
2019-05-31 10:03:30.655	I Found new pool tx: <dbef274a83a15b4c5982d9f1fe65781b2fb5ffc8da2ac8beec12a9b5f9874542>
2019-05-31 10:03:30.655	I Found new pool tx: <33a98f25118739dd3a746a2a5410c79d22866ca7a7f44a1a75d36274e56c2f54>
2019-05-31 10:03:30.655	I Found new pool tx: <7f219a9e7cb8df104e3f34271c7f81d17d8319f0244e94c90c0ec03eccebc55b>
2019-05-31 10:03:30.655	I Found new pool tx: <9675f4e20e8a0f7f54cd8add3f646d2f0f42bc7c8a9ea30bbc8f07e3e45f3064>
2019-05-31 10:03:30.655	I Found new pool tx: <49551f891f23e35b6e8872cb2ee9e754d206c1446006c9aeaef4c8d1b38cbc6f>
2019-05-31 10:03:30.655	I Found new pool tx: <8e317fbd09bb058cee1473b4cfb389bc54c253ab4d03b2eb5d3b9af99ee26d76>
2019-05-31 10:03:30.655	I Found new pool tx: <d7a6c40ad36c1f7bb2c1a01f8f81dc90966fe3f1ed233f9c2f3cea9d43bd337b>
2019-05-31 10:03:30.655	I Found new pool tx: <fe7478218479af46b185685f70181b4faa70566506ea34f46bf776c3ab84b87e>
2019-05-31 10:03:30.655	I Found new pool tx: <1f223c45c219bd72b128cc921eba31714c77dcc29ee2c0d9c6d6f3a5549dcf8e>
2019-05-31 10:03:30.655	I Found new pool tx: <8e9c7735f328d51cc343fbd0b120c1f091059765403495f67f69c2a2c9182993>
2019-05-31 10:03:30.655	I Found new pool tx: <ee4183a8d6506772533d37b1d08fa515bbc9e67489cabd9c84cb75319f5594a2>
2019-05-31 10:03:30.655	I Found new pool tx: <abed71b7617d94becf51d562a575648208911f7a7d661956e253a4a63fffd8b8>
2019-05-31 10:03:30.655	I Found new pool tx: <5099eb4dae813126adab44891645998e67b4210c7fa270d722f648ffa1c4e9c2>
2019-05-31 10:03:30.655	I Found new pool tx: <362a98513a328b38723d04e9c1cac7c2fedb395d1b37121afaf948ad15a33cc9>
2019-05-31 10:03:30.655	I Found new pool tx: <179d70ad271320c16b4f9c75b00d4c0f2b4191d69e4f2bf142b0c3b0249d22ce>
2019-05-31 10:03:30.655	I Found new pool tx: <84ae4567fbd0399b522ede628782b3e4f4965e3b8ee4b00f599481460dd7add0>
2019-05-31 10:03:30.655	I Found new pool tx: <48cbed9b171b86f52c136d0af12a6a575fd20686ecdc8da50448b28cc58718d5>
2019-05-31 10:03:30.655	I Found new pool tx: <566d8acf9df99cbcc1a88bb8a3be541b4d820f90a1d10ea74a64a3b3a037bdd5>
2019-05-31 10:03:30.655	I Found new pool tx: <e2a60919c88eb7cb0e244b21256e0e64cdbbab7ac8491c2b60de0b330bbc22da>
2019-05-31 10:03:30.655	I Found new pool tx: <3229f902413680f4ec9494f97c342e153903e61016b14f3764f91103229d06e0>
2019-05-31 10:03:30.655	I Found new pool tx: <ce674acc4d0878df0ecc42f6d8fb5d50c85265ec4423715715b47d05e9afc2f4>
2019-05-31 10:03:30.655	D asking for 27 transactions
2019-05-31 10:03:30.680	T READ ENDS: Success. bytes_tr: 162
2019-05-31 10:03:30.680	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:30.680	T READ ENDS: Success. bytes_tr: 16384
2019-05-31 10:03:30.680	T READ ENDS: Success. bytes_tr: 12909
2019-05-31 10:03:30.681	D Got 1 and OK
2019-05-31 10:03:30.681	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.681	T Device  LOCKed
2019-05-31 10:03:30.681	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.681	T Device  UNLOCKed
2019-05-31 10:03:30.681	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.681	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.681	T Device  LOCKed
2019-05-31 10:03:30.681	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.681	T Device  UNLOCKed
2019-05-31 10:03:30.682	T Device  LOCKed
2019-05-31 10:03:30.682	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.682	T Device  UNLOCKed
2019-05-31 10:03:30.682	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.682	T Device  LOCKed
2019-05-31 10:03:30.682	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.682	T Device  UNLOCKed
2019-05-31 10:03:30.682	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.682	T Device  LOCKed
2019-05-31 10:03:30.682	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.682	T Device  UNLOCKed
2019-05-31 10:03:30.682	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.682	T Device  LOCKed
2019-05-31 10:03:30.682	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.683	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  UNLOCKed
2019-05-31 10:03:30.683	T Device  LOCKed
2019-05-31 10:03:30.683	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  UNLOCKed
2019-05-31 10:03:30.683	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  LOCKed
2019-05-31 10:03:30.683	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  UNLOCKed
2019-05-31 10:03:30.683	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  LOCKed
2019-05-31 10:03:30.683	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  UNLOCKed
2019-05-31 10:03:30.683	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  LOCKed
2019-05-31 10:03:30.683	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.683	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  UNLOCKed
2019-05-31 10:03:30.683	T Device  LOCKed
2019-05-31 10:03:30.683	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  UNLOCKed
2019-05-31 10:03:30.683	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  LOCKed
2019-05-31 10:03:30.683	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.683	T Device  UNLOCKed
2019-05-31 10:03:30.684	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.684	T Device  LOCKed
2019-05-31 10:03:30.684	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.684	T Device  UNLOCKed
2019-05-31 10:03:30.684	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.684	T Device  LOCKed
2019-05-31 10:03:30.684	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.684	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.684	T Device  UNLOCKed
2019-05-31 10:03:30.684	T Device  LOCKed
2019-05-31 10:03:30.684	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.684	T Device  UNLOCKed
2019-05-31 10:03:30.684	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.684	T Device  LOCKed
2019-05-31 10:03:30.684	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.684	T Device  UNLOCKed
2019-05-31 10:03:30.684	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.684	T Device  LOCKed
2019-05-31 10:03:30.684	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.684	T Device  UNLOCKed
2019-05-31 10:03:30.684	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  LOCKed
2019-05-31 10:03:30.685	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.685	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  UNLOCKed
2019-05-31 10:03:30.685	T Device  LOCKed
2019-05-31 10:03:30.685	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  UNLOCKed
2019-05-31 10:03:30.685	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  LOCKed
2019-05-31 10:03:30.685	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  UNLOCKed
2019-05-31 10:03:30.685	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  LOCKed
2019-05-31 10:03:30.685	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  UNLOCKed
2019-05-31 10:03:30.685	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  LOCKed
2019-05-31 10:03:30.685	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.685	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  UNLOCKed
2019-05-31 10:03:30.685	T Device  LOCKed
2019-05-31 10:03:30.685	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  UNLOCKed
2019-05-31 10:03:30.685	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.685	T Device  LOCKed
2019-05-31 10:03:30.686	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.686	T Device  UNLOCKed
2019-05-31 10:03:30.686	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.686	T Device  LOCKed
2019-05-31 10:03:30.686	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.686	T Device  UNLOCKed
2019-05-31 10:03:30.686	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.686	T Device  LOCKed
2019-05-31 10:03:30.686	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.686	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.686	T Device  UNLOCKed
2019-05-31 10:03:30.686	T Device  LOCKed
2019-05-31 10:03:30.686	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.686	T Device  UNLOCKed
2019-05-31 10:03:30.686	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.686	T Device  LOCKed
2019-05-31 10:03:30.686	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.686	T Device  UNLOCKed
2019-05-31 10:03:30.686	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.686	T Device  LOCKed
2019-05-31 10:03:30.687	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  UNLOCKed
2019-05-31 10:03:30.687	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  LOCKed
2019-05-31 10:03:30.687	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.687	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  UNLOCKed
2019-05-31 10:03:30.687	T Device  LOCKed
2019-05-31 10:03:30.687	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  UNLOCKed
2019-05-31 10:03:30.687	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  LOCKed
2019-05-31 10:03:30.687	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  UNLOCKed
2019-05-31 10:03:30.687	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  LOCKed
2019-05-31 10:03:30.687	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  UNLOCKed
2019-05-31 10:03:30.687	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  LOCKed
2019-05-31 10:03:30.687	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.687	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  UNLOCKed
2019-05-31 10:03:30.687	T Device  LOCKed
2019-05-31 10:03:30.687	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.687	T Device  UNLOCKed
2019-05-31 10:03:30.688	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.688	T Device  LOCKed
2019-05-31 10:03:30.688	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.688	T Device  UNLOCKed
2019-05-31 10:03:30.688	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.688	T Device  LOCKed
2019-05-31 10:03:30.688	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.688	T Device  UNLOCKed
2019-05-31 10:03:30.688	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.688	T Device  LOCKed
2019-05-31 10:03:30.688	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.688	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.688	T Device  UNLOCKed
2019-05-31 10:03:30.688	T Device  LOCKed
2019-05-31 10:03:30.688	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.688	T Device  UNLOCKed
2019-05-31 10:03:30.688	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.688	T Device  LOCKed
2019-05-31 10:03:30.688	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.688	T Device  UNLOCKed
2019-05-31 10:03:30.688	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.688	T Device  LOCKed
2019-05-31 10:03:30.689	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.689	T Device  UNLOCKed
2019-05-31 10:03:30.689	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.689	T Device  LOCKed
2019-05-31 10:03:30.689	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.689	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.689	T Device  UNLOCKed
2019-05-31 10:03:30.689	T Device  LOCKed
2019-05-31 10:03:30.689	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.689	T Device  UNLOCKed
2019-05-31 10:03:30.689	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.689	T Device  LOCKed
2019-05-31 10:03:30.689	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.689	T Device  UNLOCKed
2019-05-31 10:03:30.689	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.689	T Device  LOCKed
2019-05-31 10:03:30.689	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.689	T Device  UNLOCKed
2019-05-31 10:03:30.689	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.689	T Device  LOCKed
2019-05-31 10:03:30.689	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.689	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.689	T Device  UNLOCKed
2019-05-31 10:03:30.689	T Device  LOCKed
2019-05-31 10:03:30.690	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  UNLOCKed
2019-05-31 10:03:30.690	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  LOCKed
2019-05-31 10:03:30.690	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  UNLOCKed
2019-05-31 10:03:30.690	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  LOCKed
2019-05-31 10:03:30.690	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  UNLOCKed
2019-05-31 10:03:30.690	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  LOCKed
2019-05-31 10:03:30.690	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.690	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  UNLOCKed
2019-05-31 10:03:30.690	T Device  LOCKed
2019-05-31 10:03:30.690	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  UNLOCKed
2019-05-31 10:03:30.690	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  LOCKed
2019-05-31 10:03:30.690	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  UNLOCKed
2019-05-31 10:03:30.690	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.690	T Device  LOCKed
2019-05-31 10:03:30.691	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.691	T Device  UNLOCKed
2019-05-31 10:03:30.691	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.691	T Device  LOCKed
2019-05-31 10:03:30.691	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.691	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.691	T Device  UNLOCKed
2019-05-31 10:03:30.691	T Device  LOCKed
2019-05-31 10:03:30.691	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.691	T Device  UNLOCKed
2019-05-31 10:03:30.691	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.691	T Device  LOCKed
2019-05-31 10:03:30.691	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.691	T Device  UNLOCKed
2019-05-31 10:03:30.691	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.691	T Device  LOCKed
2019-05-31 10:03:30.691	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.691	T Device  UNLOCKed
2019-05-31 10:03:30.691	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.691	T Device  LOCKed
2019-05-31 10:03:30.691	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.691	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.691	T Device  UNLOCKed
2019-05-31 10:03:30.692	T Device  LOCKed
2019-05-31 10:03:30.692	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.692	T Device  UNLOCKed
2019-05-31 10:03:30.692	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.692	T Device  LOCKed
2019-05-31 10:03:30.692	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.692	T Device  UNLOCKed
2019-05-31 10:03:30.692	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.692	T Device  LOCKed
2019-05-31 10:03:30.692	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.692	T Device  UNLOCKed
2019-05-31 10:03:30.692	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.692	T Device  LOCKed
2019-05-31 10:03:30.692	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.692	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.692	T Device  UNLOCKed
2019-05-31 10:03:30.692	T Device  LOCKed
2019-05-31 10:03:30.692	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.692	T Device  UNLOCKed
2019-05-31 10:03:30.692	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.692	T Device  LOCKed
2019-05-31 10:03:30.692	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.692	T Device  UNLOCKed
2019-05-31 10:03:30.692	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.693	T Device  LOCKed
2019-05-31 10:03:30.693	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.693	T Device  UNLOCKed
2019-05-31 10:03:30.693	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.693	T Device  LOCKed
2019-05-31 10:03:30.693	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.693	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.693	T Device  UNLOCKed
2019-05-31 10:03:30.693	T Device  LOCKed
2019-05-31 10:03:30.693	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.693	T Device  UNLOCKed
2019-05-31 10:03:30.693	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.693	T Device  LOCKed
2019-05-31 10:03:30.693	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.693	T Device  UNLOCKed
2019-05-31 10:03:30.693	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.693	T Device  LOCKed
2019-05-31 10:03:30.696	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.696	T Device  UNLOCKed
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.696	T Device  LOCKed
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.696	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.697	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.697	T Device  UNLOCKed
2019-05-31 10:03:30.697	T Device  LOCKed
2019-05-31 10:03:30.697	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.697	T Device  UNLOCKed
2019-05-31 10:03:30.697	T Device  LOCKed
2019-05-31 10:03:30.697	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.697	T Device  UNLOCKed
2019-05-31 10:03:30.697	T Device  LOCKed
2019-05-31 10:03:30.697	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.697	T Device  UNLOCKed
2019-05-31 10:03:30.697	T Device  LOCKed
2019-05-31 10:03:30.697	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.697	T Device  UNLOCKed
2019-05-31 10:03:30.697	T Device  LOCKed
2019-05-31 10:03:30.697	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.697	T Device  UNLOCKed
2019-05-31 10:03:30.697	T Device  LOCKed
2019-05-31 10:03:30.698	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.698	T Device  UNLOCKed
2019-05-31 10:03:30.698	T Device  LOCKed
2019-05-31 10:03:30.698	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.698	T Device  UNLOCKed
2019-05-31 10:03:30.698	T Device  LOCKed
2019-05-31 10:03:30.698	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.698	T Device  UNLOCKed
2019-05-31 10:03:30.698	T Device  LOCKed
2019-05-31 10:03:30.698	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.698	T Device  UNLOCKed
2019-05-31 10:03:30.698	T Device  LOCKed
2019-05-31 10:03:30.698	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.698	T Device  UNLOCKed
2019-05-31 10:03:30.698	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.698	T Device  LOCKed
2019-05-31 10:03:30.698	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.698	T Device  UNLOCKed
2019-05-31 10:03:30.699	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  LOCKed
2019-05-31 10:03:30.699	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  UNLOCKed
2019-05-31 10:03:30.699	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  LOCKed
2019-05-31 10:03:30.699	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.699	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  UNLOCKed
2019-05-31 10:03:30.699	T Device  LOCKed
2019-05-31 10:03:30.699	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  UNLOCKed
2019-05-31 10:03:30.699	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  LOCKed
2019-05-31 10:03:30.699	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  UNLOCKed
2019-05-31 10:03:30.699	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  LOCKed
2019-05-31 10:03:30.699	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  UNLOCKed
2019-05-31 10:03:30.699	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  LOCKed
2019-05-31 10:03:30.699	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.699	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  UNLOCKed
2019-05-31 10:03:30.699	T Device  LOCKed
2019-05-31 10:03:30.699	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  UNLOCKed
2019-05-31 10:03:30.699	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  LOCKed
2019-05-31 10:03:30.699	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.699	T Device  UNLOCKed
2019-05-31 10:03:30.700	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  LOCKed
2019-05-31 10:03:30.700	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  UNLOCKed
2019-05-31 10:03:30.700	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  LOCKed
2019-05-31 10:03:30.700	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.700	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  UNLOCKed
2019-05-31 10:03:30.700	T Device  LOCKed
2019-05-31 10:03:30.700	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  UNLOCKed
2019-05-31 10:03:30.700	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  LOCKed
2019-05-31 10:03:30.700	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  UNLOCKed
2019-05-31 10:03:30.700	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  LOCKed
2019-05-31 10:03:30.700	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  UNLOCKed
2019-05-31 10:03:30.700	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  LOCKed
2019-05-31 10:03:30.700	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.700	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  UNLOCKed
2019-05-31 10:03:30.700	T Device  LOCKed
2019-05-31 10:03:30.700	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.700	T Device  UNLOCKed
2019-05-31 10:03:30.701	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  LOCKed
2019-05-31 10:03:30.701	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  UNLOCKed
2019-05-31 10:03:30.701	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  LOCKed
2019-05-31 10:03:30.701	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  UNLOCKed
2019-05-31 10:03:30.701	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  LOCKed
2019-05-31 10:03:30.701	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.701	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  UNLOCKed
2019-05-31 10:03:30.701	T Device  LOCKed
2019-05-31 10:03:30.701	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  UNLOCKed
2019-05-31 10:03:30.701	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  LOCKed
2019-05-31 10:03:30.701	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  UNLOCKed
2019-05-31 10:03:30.701	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  LOCKed
2019-05-31 10:03:30.701	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  UNLOCKed
2019-05-31 10:03:30.701	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  LOCKed
2019-05-31 10:03:30.701	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.701	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.701	T Device  UNLOCKed
2019-05-31 10:03:30.701	T Device  LOCKed
2019-05-31 10:03:30.702	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  UNLOCKed
2019-05-31 10:03:30.702	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  LOCKed
2019-05-31 10:03:30.702	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  UNLOCKed
2019-05-31 10:03:30.702	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  LOCKed
2019-05-31 10:03:30.702	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  UNLOCKed
2019-05-31 10:03:30.702	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  LOCKed
2019-05-31 10:03:30.702	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.702	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  UNLOCKed
2019-05-31 10:03:30.702	T Device  LOCKed
2019-05-31 10:03:30.702	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  UNLOCKed
2019-05-31 10:03:30.702	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  LOCKed
2019-05-31 10:03:30.702	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  UNLOCKed
2019-05-31 10:03:30.702	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  LOCKed
2019-05-31 10:03:30.702	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  UNLOCKed
2019-05-31 10:03:30.702	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.702	T Device  LOCKed
2019-05-31 10:03:30.702	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.702	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  UNLOCKed
2019-05-31 10:03:30.703	T Device  LOCKed
2019-05-31 10:03:30.703	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  UNLOCKed
2019-05-31 10:03:30.703	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  LOCKed
2019-05-31 10:03:30.703	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  UNLOCKed
2019-05-31 10:03:30.703	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  LOCKed
2019-05-31 10:03:30.703	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  UNLOCKed
2019-05-31 10:03:30.703	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  LOCKed
2019-05-31 10:03:30.703	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.703	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  UNLOCKed
2019-05-31 10:03:30.703	T Device  LOCKed
2019-05-31 10:03:30.703	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  UNLOCKed
2019-05-31 10:03:30.703	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  LOCKed
2019-05-31 10:03:30.703	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:30.703	T Device  UNLOCKed
2019-05-31 10:03:30.703	T update_pool_state end
2019-05-31 10:03:30.703	I Refresh done, blocks received: 3, balance (all accounts): 0.100223009436, unlocked: 0.100223009436
2019-05-31 10:03:30.703	D refreshed
2019-05-31 10:03:30.703	T refreshThreadFunc: waiting for refresh...
2019-05-31 10:03:30.707	D >>> wallet refreshed
2019-05-31 10:03:30.707	D Address 'localhost:18081' is local
2019-05-31 10:03:30.708	D Invalid address format
2019-05-31 10:03:30.708	D Invalid address format
2019-05-31 10:03:30.708	D >>> wallet updated
2019-05-31 10:03:30.708	D Invalid address format
2019-05-31 10:03:30.708	D Invalid address format
2019-05-31 10:03:30.711	D New block found - updating history
2019-05-31 10:03:30.981	D Aux data not found for txid: <0da0543344ecb9cbe1280decd6b398747417d21d8c9f4b11c0fc40354451ae3c>
2019-05-31 10:03:30.988	D Aux data not found for txid: <684c65e0380bd537fe1c7f4ece35feb0a0a8a74d04ed9d8132d04c8439009d8a>
2019-05-31 10:03:34.744	D getProof: Generate clicked: txid 99ded5864eb319c8b3972a8f7463afc36263c1d4c4b4e388733a3ef28f13574f, address 8BN2xq2HyQCEUgDgDB2gSWjTLTNJZBNTaDf29SE3CpBmQV33qbA4R7FdNooHRqDTfKNxMriwxCxZWQuP2BNdGqFcEZ26txQ
2019-05-31 10:03:34.744	D Getting payment proof: 
2019-05-31 10:03:34.744	D txid:  99ded5864eb319c8b3972a8f7463afc36263c1d4c4b4e388733a3ef28f13574f , address:  8BN2xq2HyQCEUgDgDB2gSWjTLTNJZBNTaDf29SE3CpBmQV33qbA4R7FdNooHRqDTfKNxMriwxCxZWQuP2BNdGqFcEZ26txQ , message:  
2019-05-31 10:03:34.745	T READ ENDS: Success. bytes_tr: 161
2019-05-31 10:03:34.745	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:34.745	T READ ENDS: Success. bytes_tr: 1164
2019-05-31 10:03:40.703	T refreshThreadFunc: refresh lock acquired...
2019-05-31 10:03:40.704	T refreshThreadFunc: m_refreshEnabled: 1
2019-05-31 10:03:40.704	T refreshThreadFunc: m_status: 0
2019-05-31 10:03:40.704	T refreshThreadFunc: m_refreshShouldRescan: 0
2019-05-31 10:03:40.704	T refreshThreadFunc: refreshing...
2019-05-31 10:03:40.704	T doRefresh: doRefresh, rescan = 0
2019-05-31 10:03:40.704	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:03:40.704	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:40.704	T READ ENDS: Success. bytes_tr: 128
2019-05-31 10:03:40.704	T READ ENDS: Success. bytes_tr: 170
2019-05-31 10:03:40.704	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:40.704	T READ ENDS: Success. bytes_tr: 3816
2019-05-31 10:03:40.705	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:40.705	T Device  LOCKed
2019-05-31 10:03:40.705	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:40.705	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:40.705	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:40.705	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:40.705	T READ ENDS: Success. bytes_tr: 170
2019-05-31 10:03:40.705	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:40.705	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:40.705	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:40.705	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:40.705	T READ ENDS: Success. bytes_tr: 3816
2019-05-31 10:03:40.705	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:40.705	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:40.705	T Device  UNLOCKed
2019-05-31 10:03:40.705	T Device  LOCKed
2019-05-31 10:03:40.705	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:40.705	T Device  UNLOCKed
2019-05-31 10:03:40.705	T Device  LOCKed
2019-05-31 10:03:40.706	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:40.706	T Device  UNLOCKed
2019-05-31 10:03:40.706	T Device  LOCKed
2019-05-31 10:03:40.706	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:40.706	T Device  UNLOCKed
2019-05-31 10:03:40.706	T Device  LOCKed
2019-05-31 10:03:40.706	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:40.706	T Device  UNLOCKed
2019-05-31 10:03:40.706	T Device  LOCKed
2019-05-31 10:03:40.706	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:40.706	T Device  UNLOCKed
2019-05-31 10:03:40.706	T Device  LOCKed
2019-05-31 10:03:40.706	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:40.706	T Device  UNLOCKed
2019-05-31 10:03:40.706	T Device  LOCKed
2019-05-31 10:03:40.707	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:40.707	T Device  UNLOCKed
2019-05-31 10:03:40.707	T Device  LOCKed
2019-05-31 10:03:40.707	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:40.707	T Device  UNLOCKed
2019-05-31 10:03:40.707	D Block is already in blockchain: 7f4987ad115c7be0150bf841b58c47e8b7e78fcbbd62cfcf8e6a866830646d62
2019-05-31 10:03:40.707	T update_pool_state start
2019-05-31 10:03:40.707	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:03:40.707	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:40.708	T READ ENDS: Success. bytes_tr: 959
2019-05-31 10:03:40.708	T update_pool_state got pool
2019-05-31 10:03:40.708	T update_pool_state done first loop
2019-05-31 10:03:40.708	T update_pool_state done second loop
2019-05-31 10:03:40.708	D Already seen <c5e60c3076b060a75d0df3de16c3707a9ed5b14a7c0b4305e466a6fb0414050e>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <b24e975601366eef1959832e43aa0fd78e5a02b2f584d97851661ccc8075db11>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <7a690f50f193a6a9da647dc831260daebbbd6fdb6601ef6bac8926c786043317>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <b9e3fff1f72ef120973f626a34ccf755009aa5dbd7cf56de1255e1b4a7e4a529>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <3a17eac108c6e60313ff3347a7d4ff8a792b463248bac9fa7266d7846453cc33>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <b9e052a2292fe99deb1b11d126ec0df7c457e4cc1a642d39670fb4eac167b83c>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <dbef274a83a15b4c5982d9f1fe65781b2fb5ffc8da2ac8beec12a9b5f9874542>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <33a98f25118739dd3a746a2a5410c79d22866ca7a7f44a1a75d36274e56c2f54>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <7f219a9e7cb8df104e3f34271c7f81d17d8319f0244e94c90c0ec03eccebc55b>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <9675f4e20e8a0f7f54cd8add3f646d2f0f42bc7c8a9ea30bbc8f07e3e45f3064>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <49551f891f23e35b6e8872cb2ee9e754d206c1446006c9aeaef4c8d1b38cbc6f>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <8e317fbd09bb058cee1473b4cfb389bc54c253ab4d03b2eb5d3b9af99ee26d76>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <d7a6c40ad36c1f7bb2c1a01f8f81dc90966fe3f1ed233f9c2f3cea9d43bd337b>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <fe7478218479af46b185685f70181b4faa70566506ea34f46bf776c3ab84b87e>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <1f223c45c219bd72b128cc921eba31714c77dcc29ee2c0d9c6d6f3a5549dcf8e>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <8e9c7735f328d51cc343fbd0b120c1f091059765403495f67f69c2a2c9182993>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <ee4183a8d6506772533d37b1d08fa515bbc9e67489cabd9c84cb75319f5594a2>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <abed71b7617d94becf51d562a575648208911f7a7d661956e253a4a63fffd8b8>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <5099eb4dae813126adab44891645998e67b4210c7fa270d722f648ffa1c4e9c2>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <362a98513a328b38723d04e9c1cac7c2fedb395d1b37121afaf948ad15a33cc9>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <179d70ad271320c16b4f9c75b00d4c0f2b4191d69e4f2bf142b0c3b0249d22ce>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <84ae4567fbd0399b522ede628782b3e4f4965e3b8ee4b00f599481460dd7add0>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <48cbed9b171b86f52c136d0af12a6a575fd20686ecdc8da50448b28cc58718d5>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <566d8acf9df99cbcc1a88bb8a3be541b4d820f90a1d10ea74a64a3b3a037bdd5>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <e2a60919c88eb7cb0e244b21256e0e64cdbbab7ac8491c2b60de0b330bbc22da>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <3229f902413680f4ec9494f97c342e153903e61016b14f3764f91103229d06e0>, and not for us, skipped
2019-05-31 10:03:40.708	D Already seen <ce674acc4d0878df0ecc42f6d8fb5d50c85265ec4423715715b47d05e9afc2f4>, and not for us, skipped
2019-05-31 10:03:40.708	T update_pool_state end
2019-05-31 10:03:40.708	I Refresh done, blocks received: 0, balance (all accounts): 0.100223009436, unlocked: 0.100223009436
2019-05-31 10:03:40.708	D refreshed
2019-05-31 10:03:40.708	T refreshThreadFunc: waiting for refresh...
2019-05-31 10:03:40.708	D >>> wallet refreshed
2019-05-31 10:03:40.708	D Checking connection status
2019-05-31 10:03:40.709	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:03:40.709	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:40.709	T READ ENDS: Success. bytes_tr: 128
2019-05-31 10:03:40.709	D >>> wallet updated
2019-05-31 10:03:50.708	T refreshThreadFunc: refresh lock acquired...
2019-05-31 10:03:50.708	T refreshThreadFunc: m_refreshEnabled: 1
2019-05-31 10:03:50.708	T refreshThreadFunc: m_status: 0
2019-05-31 10:03:50.708	T refreshThreadFunc: m_refreshShouldRescan: 0
2019-05-31 10:03:50.709	T refreshThreadFunc: refreshing...
2019-05-31 10:03:50.709	T doRefresh: doRefresh, rescan = 0
2019-05-31 10:03:50.709	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:03:50.709	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:50.709	T READ ENDS: Success. bytes_tr: 128
2019-05-31 10:03:50.710	T READ ENDS: Success. bytes_tr: 170
2019-05-31 10:03:50.710	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:50.710	T READ ENDS: Success. bytes_tr: 3816
2019-05-31 10:03:50.710	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.710	T Device  LOCKed
2019-05-31 10:03:50.710	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.711	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.711	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.711	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.711	T READ ENDS: Success. bytes_tr: 170
2019-05-31 10:03:50.711	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.711	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:50.711	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.711	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.711	T READ ENDS: Success. bytes_tr: 3816
2019-05-31 10:03:50.711	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.711	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.711	T Device  UNLOCKed
2019-05-31 10:03:50.711	T Device  LOCKed
2019-05-31 10:03:50.712	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.712	T Device  UNLOCKed
2019-05-31 10:03:50.712	T Device  LOCKed
2019-05-31 10:03:50.712	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.712	T Device  UNLOCKed
2019-05-31 10:03:50.712	T Device  LOCKed
2019-05-31 10:03:50.712	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.712	T Device  UNLOCKed
2019-05-31 10:03:50.712	T Device  LOCKed
2019-05-31 10:03:50.713	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.713	T Device  UNLOCKed
2019-05-31 10:03:50.713	T Device  LOCKed
2019-05-31 10:03:50.713	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.713	T Device  UNLOCKed
2019-05-31 10:03:50.713	T Device  LOCKed
2019-05-31 10:03:50.713	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.713	T Device  UNLOCKed
2019-05-31 10:03:50.714	T Device  LOCKed
2019-05-31 10:03:50.714	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.714	T Device  UNLOCKed
2019-05-31 10:03:50.714	T Device  LOCKed
2019-05-31 10:03:50.714	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.714	T Device  UNLOCKed
2019-05-31 10:03:50.715	D Block is already in blockchain: 7f4987ad115c7be0150bf841b58c47e8b7e78fcbbd62cfcf8e6a866830646d62
2019-05-31 10:03:50.715	T update_pool_state start
2019-05-31 10:03:50.715	T READ ENDS: Success. bytes_tr: 161
2019-05-31 10:03:50.715	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:50.715	T READ ENDS: Success. bytes_tr: 1026
2019-05-31 10:03:50.715	T update_pool_state got pool
2019-05-31 10:03:50.715	T update_pool_state done first loop
2019-05-31 10:03:50.715	T update_pool_state done second loop
2019-05-31 10:03:50.715	D Already seen <c5e60c3076b060a75d0df3de16c3707a9ed5b14a7c0b4305e466a6fb0414050e>, and not for us, skipped
2019-05-31 10:03:50.715	D Already seen <b24e975601366eef1959832e43aa0fd78e5a02b2f584d97851661ccc8075db11>, and not for us, skipped
2019-05-31 10:03:50.716	I Found new pool tx: <b445987335a9daf9edbc6f10686ce0e3a4ff7bac5e693a970ba69d3508234d14>
2019-05-31 10:03:50.716	D Already seen <7a690f50f193a6a9da647dc831260daebbbd6fdb6601ef6bac8926c786043317>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <b9e3fff1f72ef120973f626a34ccf755009aa5dbd7cf56de1255e1b4a7e4a529>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <3a17eac108c6e60313ff3347a7d4ff8a792b463248bac9fa7266d7846453cc33>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <b9e052a2292fe99deb1b11d126ec0df7c457e4cc1a642d39670fb4eac167b83c>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <dbef274a83a15b4c5982d9f1fe65781b2fb5ffc8da2ac8beec12a9b5f9874542>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <33a98f25118739dd3a746a2a5410c79d22866ca7a7f44a1a75d36274e56c2f54>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <7f219a9e7cb8df104e3f34271c7f81d17d8319f0244e94c90c0ec03eccebc55b>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <9675f4e20e8a0f7f54cd8add3f646d2f0f42bc7c8a9ea30bbc8f07e3e45f3064>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <49551f891f23e35b6e8872cb2ee9e754d206c1446006c9aeaef4c8d1b38cbc6f>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <8e317fbd09bb058cee1473b4cfb389bc54c253ab4d03b2eb5d3b9af99ee26d76>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <d7a6c40ad36c1f7bb2c1a01f8f81dc90966fe3f1ed233f9c2f3cea9d43bd337b>, and not for us, skipped
2019-05-31 10:03:50.716	I Found new pool tx: <d3cf1a648877217cc1596d364d4792a735b8c6372d33dfeccf7fc4425cc8317d>
2019-05-31 10:03:50.716	D Already seen <fe7478218479af46b185685f70181b4faa70566506ea34f46bf776c3ab84b87e>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <1f223c45c219bd72b128cc921eba31714c77dcc29ee2c0d9c6d6f3a5549dcf8e>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <8e9c7735f328d51cc343fbd0b120c1f091059765403495f67f69c2a2c9182993>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <ee4183a8d6506772533d37b1d08fa515bbc9e67489cabd9c84cb75319f5594a2>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <abed71b7617d94becf51d562a575648208911f7a7d661956e253a4a63fffd8b8>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <5099eb4dae813126adab44891645998e67b4210c7fa270d722f648ffa1c4e9c2>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <362a98513a328b38723d04e9c1cac7c2fedb395d1b37121afaf948ad15a33cc9>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <179d70ad271320c16b4f9c75b00d4c0f2b4191d69e4f2bf142b0c3b0249d22ce>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <84ae4567fbd0399b522ede628782b3e4f4965e3b8ee4b00f599481460dd7add0>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <48cbed9b171b86f52c136d0af12a6a575fd20686ecdc8da50448b28cc58718d5>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <566d8acf9df99cbcc1a88bb8a3be541b4d820f90a1d10ea74a64a3b3a037bdd5>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <e2a60919c88eb7cb0e244b21256e0e64cdbbab7ac8491c2b60de0b330bbc22da>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <3229f902413680f4ec9494f97c342e153903e61016b14f3764f91103229d06e0>, and not for us, skipped
2019-05-31 10:03:50.716	D Already seen <ce674acc4d0878df0ecc42f6d8fb5d50c85265ec4423715715b47d05e9afc2f4>, and not for us, skipped
2019-05-31 10:03:50.716	D asking for 2 transactions
2019-05-31 10:03:50.737	T READ ENDS: Success. bytes_tr: 161
2019-05-31 10:03:50.737	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:50.737	T READ ENDS: Success. bytes_tr: 2022
2019-05-31 10:03:50.737	D Got 1 and OK
2019-05-31 10:03:50.737	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.737	T Device  LOCKed
2019-05-31 10:03:50.738	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.738	T Device  UNLOCKed
2019-05-31 10:03:50.738	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.738	T Device  LOCKed
2019-05-31 10:03:50.738	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.738	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.738	T Device  UNLOCKed
2019-05-31 10:03:50.738	T Device  LOCKed
2019-05-31 10:03:50.738	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.738	T Device  UNLOCKed
2019-05-31 10:03:50.738	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.738	T Device  LOCKed
2019-05-31 10:03:50.738	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.738	T Device  UNLOCKed
2019-05-31 10:03:50.738	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.738	T Device  LOCKed
2019-05-31 10:03:50.738	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.738	T Device  UNLOCKed
2019-05-31 10:03:50.738	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.738	T Device  LOCKed
2019-05-31 10:03:50.738	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.738	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.738	T Device  UNLOCKed
2019-05-31 10:03:50.738	T Device  LOCKed
2019-05-31 10:03:50.739	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.739	T Device  UNLOCKed
2019-05-31 10:03:50.739	T Ask for LOCKING for device  in thread 
2019-05-31 10:03:50.739	T Device  LOCKed
2019-05-31 10:03:50.739	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:03:50.739	T Device  UNLOCKed
2019-05-31 10:03:50.739	T update_pool_state end
2019-05-31 10:03:50.739	I Refresh done, blocks received: 0, balance (all accounts): 0.100223009436, unlocked: 0.100223009436
2019-05-31 10:03:50.739	D refreshed
2019-05-31 10:03:50.739	T refreshThreadFunc: waiting for refresh...
2019-05-31 10:03:50.742	D >>> wallet refreshed
2019-05-31 10:03:50.742	D Checking connection status
2019-05-31 10:03:50.742	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:03:50.742	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:50.742	T READ ENDS: Success. bytes_tr: 128
2019-05-31 10:03:50.742	D >>> wallet updated
2019-05-31 10:03:50.910	D getProof: Generate clicked: txid d1530bfd0a531b6ccf0fa10874062f5e7149e6a53f160a647b76e801519d0b61, address 87K69Jpac8od7RMsNcdxoGGnSP8L9VPPngPYhSsAavpZdfBkhjeqkebTVsL6h1Ho5VKJvLXEUCPckHbWsDYsjEcRTJfQLK5
2019-05-31 10:03:50.910	D Getting payment proof: 
2019-05-31 10:03:50.910	D txid:  d1530bfd0a531b6ccf0fa10874062f5e7149e6a53f160a647b76e801519d0b61 , address:  87K69Jpac8od7RMsNcdxoGGnSP8L9VPPngPYhSsAavpZdfBkhjeqkebTVsL6h1Ho5VKJvLXEUCPckHbWsDYsjEcRTJfQLK5 , message:  
2019-05-31 10:03:50.911	T READ ENDS: Success. bytes_tr: 161
2019-05-31 10:03:50.911	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:50.912	T READ ENDS: Success. bytes_tr: 1056
2019-05-31 10:03:50.914	E !received. THROW EXCEPTION: error::wallet_internal_error
2019-05-31 10:03:50.914	W /home/asuspc/monero-gui/monero/src/wallet/wallet2.cpp:10893:N5tools5error21wallet_internal_errorE: No funds received in this tx.
2019-05-31 10:03:50.915	T READ ENDS: Success. bytes_tr: 161
2019-05-31 10:03:50.915	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:50.915	T READ ENDS: Success. bytes_tr: 1056
2019-05-31 10:03:50.963	T READ ENDS: Success. bytes_tr: 385
2019-05-31 10:03:50.963	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:51.324	T READ ENDS: Success. bytes_tr: 188
2019-05-31 10:03:51.324	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:51.324	D on_button_request, code: 8
2019-05-31 10:03:51.324	D Displaying processing splash
2019-05-31 10:03:54.377	T READ ENDS: Success. bytes_tr: 184
2019-05-31 10:03:54.377	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:54.377	D Hiding processing splash
2019-05-31 10:03:54.710	T READ ENDS: Success. bytes_tr: 505
2019-05-31 10:03:54.710	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:54.712	T READ ENDS: Success. bytes_tr: 170
2019-05-31 10:03:54.712	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:03:54.713	T READ ENDS: Success. bytes_tr: 1624
2019-05-31 10:04:00.096	D showing status message
2019-05-31 10:04:00.333	D copied to clipboard
2019-05-31 10:04:00.333	D showing status message
2019-05-31 10:04:00.739	T refreshThreadFunc: refresh lock acquired...
2019-05-31 10:04:00.739	T refreshThreadFunc: m_refreshEnabled: 1
2019-05-31 10:04:00.739	T refreshThreadFunc: m_status: 0
2019-05-31 10:04:00.739	T refreshThreadFunc: m_refreshShouldRescan: 0
2019-05-31 10:04:00.739	T refreshThreadFunc: refreshing...
2019-05-31 10:04:00.739	T doRefresh: doRefresh, rescan = 0
2019-05-31 10:04:00.740	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:04:00.740	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:04:00.740	T READ ENDS: Success. bytes_tr: 128
2019-05-31 10:04:00.741	T READ ENDS: Success. bytes_tr: 161
2019-05-31 10:04:00.741	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:04:00.741	T READ ENDS: Success. bytes_tr: 1318
2019-05-31 10:04:00.742	T READ ENDS: Success. bytes_tr: 170
2019-05-31 10:04:00.742	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:04:00.743	T READ ENDS: Success. bytes_tr: 3816
2019-05-31 10:04:00.743	T Ask for LOCKING for device  in thread 
2019-05-31 10:04:00.743	T Ask for LOCKING for device  in thread 
2019-05-31 10:04:00.743	T Ask for LOCKING for device  in thread 
2019-05-31 10:04:00.744	T Ask for LOCKING for device  in thread 
2019-05-31 10:04:00.744	T Ask for LOCKING for device  in thread 
2019-05-31 10:04:00.744	T Ask for LOCKING for device  in thread 
2019-05-31 10:04:00.744	T Ask for LOCKING for device  in thread 
2019-05-31 10:04:00.744	T READ ENDS: Success. bytes_tr: 170
2019-05-31 10:04:00.744	T Device  LOCKed
2019-05-31 10:04:00.744	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:04:00.744	T Ask for LOCKING for device  in thread 
2019-05-31 10:04:00.744	T Ask for LOCKING for device  in thread 
2019-05-31 10:04:00.744	T READ ENDS: Success. bytes_tr: 3816
2019-05-31 10:04:00.745	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:04:00.745	T Device  UNLOCKed
2019-05-31 10:04:00.745	T Device  LOCKed
2019-05-31 10:04:00.745	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:04:00.745	T Device  UNLOCKed
2019-05-31 10:04:00.745	T Device  LOCKed
2019-05-31 10:04:00.746	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:04:00.746	T Device  UNLOCKed
2019-05-31 10:04:00.746	T Device  LOCKed
2019-05-31 10:04:00.746	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:04:00.746	T Device  UNLOCKed
2019-05-31 10:04:00.746	T Device  LOCKed
2019-05-31 10:04:00.747	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:04:00.747	T Device  UNLOCKed
2019-05-31 10:04:00.747	T Device  LOCKed
2019-05-31 10:04:00.747	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:04:00.747	T Device  UNLOCKed
2019-05-31 10:04:00.747	T Device  LOCKed
2019-05-31 10:04:00.748	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:04:00.748	T Device  UNLOCKed
2019-05-31 10:04:00.748	T Device  LOCKed
2019-05-31 10:04:00.748	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:04:00.749	T Device  UNLOCKed
2019-05-31 10:04:00.749	T Device  LOCKed
2019-05-31 10:04:00.749	T Ask for UNLOCKING for device  in thread 
2019-05-31 10:04:00.749	T Device  UNLOCKed
2019-05-31 10:04:00.750	D Block is already in blockchain: 7f4987ad115c7be0150bf841b58c47e8b7e78fcbbd62cfcf8e6a866830646d62
2019-05-31 10:04:00.750	T update_pool_state start
2019-05-31 10:04:00.750	T READ ENDS: Success. bytes_tr: 161
2019-05-31 10:04:00.751	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:04:00.751	T READ ENDS: Success. bytes_tr: 1026
2019-05-31 10:04:00.751	T update_pool_state got pool
2019-05-31 10:04:00.751	T update_pool_state done first loop
2019-05-31 10:04:00.751	T update_pool_state done second loop
2019-05-31 10:04:00.751	D Already seen <c5e60c3076b060a75d0df3de16c3707a9ed5b14a7c0b4305e466a6fb0414050e>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <b24e975601366eef1959832e43aa0fd78e5a02b2f584d97851661ccc8075db11>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <b445987335a9daf9edbc6f10686ce0e3a4ff7bac5e693a970ba69d3508234d14>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <7a690f50f193a6a9da647dc831260daebbbd6fdb6601ef6bac8926c786043317>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <b9e3fff1f72ef120973f626a34ccf755009aa5dbd7cf56de1255e1b4a7e4a529>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <3a17eac108c6e60313ff3347a7d4ff8a792b463248bac9fa7266d7846453cc33>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <b9e052a2292fe99deb1b11d126ec0df7c457e4cc1a642d39670fb4eac167b83c>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <dbef274a83a15b4c5982d9f1fe65781b2fb5ffc8da2ac8beec12a9b5f9874542>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <33a98f25118739dd3a746a2a5410c79d22866ca7a7f44a1a75d36274e56c2f54>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <7f219a9e7cb8df104e3f34271c7f81d17d8319f0244e94c90c0ec03eccebc55b>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <9675f4e20e8a0f7f54cd8add3f646d2f0f42bc7c8a9ea30bbc8f07e3e45f3064>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <49551f891f23e35b6e8872cb2ee9e754d206c1446006c9aeaef4c8d1b38cbc6f>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <8e317fbd09bb058cee1473b4cfb389bc54c253ab4d03b2eb5d3b9af99ee26d76>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <d7a6c40ad36c1f7bb2c1a01f8f81dc90966fe3f1ed233f9c2f3cea9d43bd337b>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <d3cf1a648877217cc1596d364d4792a735b8c6372d33dfeccf7fc4425cc8317d>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <fe7478218479af46b185685f70181b4faa70566506ea34f46bf776c3ab84b87e>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <1f223c45c219bd72b128cc921eba31714c77dcc29ee2c0d9c6d6f3a5549dcf8e>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <8e9c7735f328d51cc343fbd0b120c1f091059765403495f67f69c2a2c9182993>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <ee4183a8d6506772533d37b1d08fa515bbc9e67489cabd9c84cb75319f5594a2>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <abed71b7617d94becf51d562a575648208911f7a7d661956e253a4a63fffd8b8>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <5099eb4dae813126adab44891645998e67b4210c7fa270d722f648ffa1c4e9c2>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <362a98513a328b38723d04e9c1cac7c2fedb395d1b37121afaf948ad15a33cc9>, and not for us, skipped
2019-05-31 10:04:00.751	D Already seen <179d70ad271320c16b4f9c75b00d4c0f2b4191d69e4f2bf142b0c3b0249d22ce>, and not for us, skipped
2019-05-31 10:04:00.752	D Already seen <84ae4567fbd0399b522ede628782b3e4f4965e3b8ee4b00f599481460dd7add0>, and not for us, skipped
2019-05-31 10:04:00.752	D Already seen <48cbed9b171b86f52c136d0af12a6a575fd20686ecdc8da50448b28cc58718d5>, and not for us, skipped
2019-05-31 10:04:00.752	D Already seen <566d8acf9df99cbcc1a88bb8a3be541b4d820f90a1d10ea74a64a3b3a037bdd5>, and not for us, skipped
2019-05-31 10:04:00.752	D Already seen <e2a60919c88eb7cb0e244b21256e0e64cdbbab7ac8491c2b60de0b330bbc22da>, and not for us, skipped
2019-05-31 10:04:00.752	D Already seen <3229f902413680f4ec9494f97c342e153903e61016b14f3764f91103229d06e0>, and not for us, skipped
2019-05-31 10:04:00.752	D Already seen <ce674acc4d0878df0ecc42f6d8fb5d50c85265ec4423715715b47d05e9afc2f4>, and not for us, skipped
2019-05-31 10:04:00.752	T update_pool_state end
2019-05-31 10:04:00.752	I Refresh done, blocks received: 0, balance (all accounts): 0.100223009436, unlocked: 0.100223009436
2019-05-31 10:04:00.761	T READ ENDS: Success. bytes_tr: 184
2019-05-31 10:04:00.761	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:04:00.761	D refreshed
2019-05-31 10:04:00.761	T refreshThreadFunc: waiting for refresh...
2019-05-31 10:04:00.762	D >>> wallet refreshed
2019-05-31 10:04:00.762	D Checking connection status
2019-05-31 10:04:00.762	T READ ENDS: Success. bytes_tr: 160
2019-05-31 10:04:00.762	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:04:00.763	T READ ENDS: Success. bytes_tr: 128
2019-05-31 10:04:00.763	D >>> wallet updated
2019-05-31 10:04:02.744	D blocking close event
2019-05-31 10:04:02.744	D sending external cmd:  ("status")
2019-05-31 10:04:04.367	D "\u001B[36m2019-05-31 10:04:03.765\tI Monero 'Boron Butterfly' (v0.14.1.0-5fbfa8a6)\n\u001B[0m\u001B[36m2019-05-31 10:04:03.766\tI Generating SSL certificate\n\u001B[0mError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2019-05-31 10:04:04.367	D close accepted
2019-05-31 10:04:04.367	D DaemonManager: exit()
2019-05-31 10:04:04.367	D ~Wallet: Closing wallet
2019-05-31 10:04:04.367	D trimming to 1775599, offset 1775600
2019-05-31 10:04:04.400	D Wallet cache stored successfully
2019-05-31 10:04:04.400	I ~WalletImpl
2019-05-31 10:04:04.400	D pauseRefresh: refresh paused...
2019-05-31 10:04:04.400	I closing wallet...
2019-05-31 10:04:04.400	I Calling wallet::stop...
2019-05-31 10:04:04.400	I wallet::stop done
2019-05-31 10:04:04.400	T Closing Trezor:BridgeTransport
2019-05-31 10:04:04.451	T READ ENDS: Success. bytes_tr: 188
2019-05-31 10:04:04.451	T http_stream_filter::parse_cached_header(*)
2019-05-31 10:04:04.452	T refreshThreadFunc: refresh lock acquired...
2019-05-31 10:04:04.452	T refreshThreadFunc: m_refreshEnabled: 0
2019-05-31 10:04:04.452	T refreshThreadFunc: m_status: 0
2019-05-31 10:04:04.452	T refreshThreadFunc: m_refreshShouldRescan: 0
2019-05-31 10:04:04.452	T refreshThreadFunc: refresh thread stopped
2019-05-31 10:04:04.452	I ~WalletImpl finished
2019-05-31 10:04:04.452	D Problems at ssl shutdown: uninitialized
2019-05-31 10:04:04.452	D Problems at cancel: Bad file descriptor
2019-05-31 10:04:04.452	D Problems at shutdown: Bad file descriptor
2019-05-31 10:04:04.454	D m_walletImpl deleted
2019-05-31 10:04:04.455	W qrc:///pages/History.qml:1103: TypeError: Cannot call method 'getTxKey' of null
2019-05-31 10:04:04.455	W qrc:///pages/History.qml:1103: TypeError: Cannot call method 'getTxKey' of null
2019-05-31 10:04:04.455	W qrc:///pages/History.qml:1103: TypeError: Cannot call method 'getTxKey' of null
2019-05-31 10:04:04.455	W qrc:///pages/History.qml:1103: TypeError: Cannot call method 'getTxKey' of null
2019-05-31 10:04:04.455	W qrc:///pages/History.qml:1103: TypeError: Cannot call method 'getTxKey' of null
2019-05-31 10:04:04.920	D Device 0 Destroyed
```

## rating89us | 2019-05-31T10:19:43+00:00
I have already sent 3 transactions. Two of them have the P button working fine, one of them has the problem mentioned.

On the above log I did the following:
- Opened the GUI-Wallet
- Clicked on P (proof) button for a transaction that is working.
- Trezor didn't ask for anything.
- Closed payment proof window
- Clicked on P (proof) button of the transaction that is not working.
- Got the error `2019-05-31 10:03:50.914	W /home/asuspc/monero-gui/monero/src/wallet/wallet2.cpp:10893:N5tools5error21wallet_internal_errorE: No funds received in this tx`.
- My trezor asked for ki refresh. I authorized. My trezor displayed "refreshing -1".
- Payment proof opened normally. I closed it.
- I copied to clipboard the transaction details of the problematic transaction, which I paste below:

Tx ID: | d1530bfd0a531b6ccf0fa10874062f5e7149e6a53f160a647b76e801519d0b61
Address label: | Primary address
Address: | (deleted) - I paid from the wallet's main address (primary)
Payment ID: | ecc4ecc28757081b
Tx key: | 0000000000000000000000000000000000000000000000000000000000000000
Tx note: | (deleted) - I used a Tx note with 2 words for this transaction, no special characters
Destinations: | 0.010000000000: 87K69Jpac8od7RMsNcdxoGGnSP8L9VPPngPYhSsAavpZdfBkhjeqkebTVsL6h1Ho5VKJvLXEUCPckHbWsDYsjEcRTJfQLK5
Rings: | 593ba492033d606df03807d82af3cc30aa118f23ab4daeedf912eed8370750a0 absolute 4840859 10292096 10317455 10348987 10378640 10378945 10392262 10408877 10432930 10434025 10439645

I'm not sure if I'm using Qt:5.9.5 or Qt:5.9.7. I've installed Qt5.9.7 but GUI still displays 5.9.5



## ph4r05 | 2019-05-31T10:42:50+00:00
Hmm I think this problem will be resolved in the next Trezor firmware update. 

## rating89us | 2019-05-31T20:58:20+00:00
The normal transactions have a small proof:
`InProofV18RFtpNRyYUsAR8JWFhBafACoksHf3K6gQ72dzNNqkdfiUrdFZaHoKEP4qPLEeoBJVUc8QXwGsF5GnKaG3ZFHrHdwbDu4sU13q1FEKXZcMQwJ1vAvcibqkmH68ZGUT5z29AX7`

The problematic transaction has a really long proof:
`SpendProofV15tQQ5kWwgd2SEEuXUme1nEgNb412sHeznUJTCvFQDXEKRJ7oFyaJfsHDjHZLcmHf3uCq8qJe8yymre7LfsvSSu8CHvbQPodsZEDiUeZakHznRMJnsktLyUc2Xfvnv6YjF7hkU5ECCnoc9sCSiTChQagoNjdMeYTFemW9yjVbq5aEQvj6h2UkcJWC5aa4Q1Jd2WVNAPGw9c2aJ6B8kEur6vMwzouz7Cyy37jjQCxTDsBkXC5WAwCW44grUAQyGUYggdv616QoN3uYae7Fv3Wdnp9XUnAwgQKQDiPN8zNPMFsmLqcXWpjb33u2QBiboCXS8VxtZ4Fpe16izErJWneAZYG5MLJMTp8kSKaYBYEP5xzfFvtyAqdc9zEq2kr14i6QjKqPFd7g8gB1Pbrne8Mpgug4YyqWwMczTb9WP3Z3wZkrbKNiQwRY48p6TU2zFRv2mp7Xk1EZTzv7qW34LWcbxQ7uV7dQffk4GyYxBwnTzNSH1ibPXVGEr5PGkQPsHiUssbP7HWnZPX6pKABf4Ttp2FRMid4d5UdbJYYa4VT1XpjJZcXwCMkvawSHCq9VWq76DULseJeYCcMYAWMcLFfEqivk88ojhCMtahn1uxCDBbXyqaoA4g3asxbbfDHBGtCtGo55BLnefJsyvF1gjtkT1qbt2XYrk9LUZnSTPo5ibtCfKQAGJk8kHbiGfyqjsQZc2k8eqGWNiVfe3ppcMiwXqcfabypfsjKpqbNiv4rMQr2mRufyUEqCi43Kvye3AF4XrELbD9Zizoqjp4ehEfypFCQXAA97ijiBCPZjjKWmvJZ1WzgHYT4VaR8DZXAigKDppeh44sBQ9jh5zZHVPGsa2uw1BwXiE8CbqsSfPiBiKJvdp3yRDzYPkuiMm1P5Aet6Z5eKMhW6KfgBwpX4F1mXa6fgDRXGQ8PfAvCtvuWRFi71LDWNpbJVMov3JfSTSZ41XyZfU4uw`

## ph4r05 | 2019-06-03T15:38:08+00:00
Did you pls check the "long" proof, whether it verifies correctly?

## rating89us | 2019-06-03T16:28:03+00:00
I get a "Bad signature" on GUI for every transaction with the error `/monero-gui/monero/src/wallet/wallet2.cpp:10893:N5tools5error21wallet_internal_errorE: No funds received in this tx.`

## rating89us | 2019-06-13T13:03:02+00:00
This problem persists after updating Trezor firmware to v2.1.1.

## ph4r05 | 2019-06-13T13:28:52+00:00
> This problem persists after updating Trezor firmware to v2.1.1.

Thanks for info! This upgrade and the following one fixes several UI problems with "proceed to the device" but they don't fix the payment proofs.

I will take a look at it this month whether I can reproduce it, but it won't be fixed in the next monero release for sure (v0.14.1). 

Another interesting fact is that Trezor is only required for computing TX proof for outgoing transactions, i.e., those signed on the Trezor. For incoming transactions the proof is basically `tx_pub * view_priv` and as the host knows the private view key no device interaction is required. 

The transaction you want tx proof for is outgoing or incoming? Thanks!



## ph4r05 | 2019-06-13T17:17:47+00:00
Aah I've just noticed that you mentioned one working transaction proof starts with "InProofV1", which is the tx_proof, but the other long proof of the "invalid transaction" starts with "SpendProofV1", which is a different feature, the spend_proof. spend_proofs are not yet supported on Trezor. 

Update: I've just checked monero-gui code and in case of a failure for the tx_proof it tries to generate spend_proof which is then returned to you. So the problem is with the tx_proof.

## ph4r05 | 2019-06-13T17:23:56+00:00
Can you try to get tx_key? It should return other than zero vector. 

## rating89us | 2019-06-13T17:43:37+00:00
The transactions with problem are outgoing transactions.

**Working transaction:**
```
2019-06-13 17:51:25.415	D getProof: Generate clicked: txid e784472334a23d8b614ac4894d670fd970f8287f802572781e6f18c45caadfea, address (hidden)
2019-06-13 17:51:25.415	D Getting payment proof:
2019-06-13 17:51:25.415	D txid: e784472334a23d8b614ac4894d670fd970f8287f802572781e6f18c45caadfea , address: (hidden), message:
```

_Result (GUI):_
`InProofV1NZ3dLmZk69rQkxKEGD6od3CZQrKpkUTX7DqAdxre9fLJgZAcaULnnsB7rvHsZJg2Se9hcGRBj2ecnh6QYnd1FzRXDiBc2X8DVnZUPBheCPnc8rVDRpjwz8d1TLEJXUiuGqwK`

_get_tx_key txid:_
`Error: no tx keys found for this txid`

_get_tx_proof txid address:_
`signature file saved to: monero_tx_proof`

**Problematic transaction:**
```
2019-06-13 17:52:12.535	D getProof: Generate clicked: txid 2627a6b2379b557778ea91de6ee335e51c0dd49636184bcbf149a097d2e53f51, address (hidden)
2019-06-13 17:52:12.535	D Getting payment proof:
2019-06-13 17:52:12.535	D txid: 2627a6b2379b557778ea91de6ee335e51c0dd49636184bcbf149a097d2e53f51 , address: (hidden), message:
2019-06-13 17:52:12.538	E !received. THROW EXCEPTION: error::wallet_internal_error
2019-06-13 17:52:12.538	W /home/asuspc/monero-gui/monero/src/wallet/wallet2.cpp:10893:N5tools5error21wallet_internal_errorE: No funds received in this tx.
```

_Result (GUI):_
`SpendProofV1DYoGXZZJPKndiUXDD1PFujesjhCto5KuaMMuRaQtnisSSapUQeWUFweC9txFpKQv5rNn1sZ8g69ugit2AQvzzUwkFr1bANWUhtMRyf1StndhLn4fpsbGbhMb4PnVDzhavXAgBegC1umuhQHXK53MeJtUK69sH5Wet5jUiWSX6XRhmqJFSoePeALh17F6emHVBchXtDQcBkhUfpXMjY5Lw7Mi94SgRH7JnC9KSCKANEz6zg2yL3Xuh4PMZpeqqQJfX5NbA8eA9yeVB9WiRyaeScCLRsqQRuhxLwHZwzjpo8jGLf2x7tNNXkSyPfwd3Q4GTcjimNYX557qsSn3KZTKaU7yn4fRHGkpjaupp9NiP9rAUYBDT6gVBR7s6Zpm54xTm9V2kXmyus4zC5cqRLiu2GnPCPqyFkf53wdUkZDPwtauzMsn8deQS85pNiU2hB1f9vDHaqY4TQJ7E5TTTyBgiPWNN2WhvehZHCAqLTmM4AmD3b2BRFjmzA2Qfi7TLNpTCivHPGKh8UmVtAnYNTpZ7LuP61XPaWzk7w9Udj44o5eLRgp5eQX3Nn8GCywX8hZm8dXgcwfWJaxLxUZtMYS5a765bRg7sPFoBp73gf5QVEj58NSrdKhQyv7BvNBBuiCd8ueFGQLrYd1wdriUbF1r6Bp6DXfEYCEFKZiWZPQnnh1VSvaXtB6bQW9NFKBNgyzMYUYiYm6NqE4dvhzvJtoGpuM4Ac56r3SKnArrY5QHkECb1b8XcURYc1ZXcThQFr262YZaNthKkekJggW1DFe3pdXLTX47GoS1pupGGhb8DGMZDpJMQq4PhtUCFCR3GzR64Km7WzDrj5mki9YMC3D52Le4SQGobdTa69Mot7whBPgDpYatHMRwzCL1pyR94iNLuwch94aK6YDVKudN5UZLUyJJCwsxJcWtWBMZH2KVSbzQBbCzkv3Rg2gejzEYfcsA3TugXvse5X59mY7d8rsfXAQ7z1o8DmZGDCxx7fYfyXKenPbwvAyncJe1pc2u4B6f3pCRDVjfA9UyAiM4TW4JKP688ycncucbNCXAC7WVtcMamZ11mbV1a1MhNt1GSFYze2iRGp9NQahkaHS8opUymfggn1UmEB7GXgXPNAgSp3t5H7hjNyKfVpq6gyEkPUsQP8XBsqy8rjSaJNCKy8bGQDKzFCM41DwVSQdzfM4GWgWmxiKMQj39Saohaf9TraQNaauswB1zBqtDWgwbT6dH8ajNQqo4x5hdtzLeBfLM3ED3c17djHQVqcVA4e3Nar5yJqYNvNLYTrNPdVGRVQasCHpZb31XEB5ScWw1Q3ovXNxnC8Yw5vBJz8we1vxYViBHE9c2t5E7Ke9De32xqF3DW5WBk3kDBf9KxZmVM6cbcH2KnxJULbKBQDARbBZJm8RhYMzcXaSyA5XYhrhK8xi7ZG7FoSENzqT6j5przrzHsavk6oabC7AvWxMcabNJBd7QLGRKsfcYVMuRM2go8o6iFbLEdF1UHGTn41wT4QjPNEpR4ThVDKJDhi9pfbvAdfmtEarRjZFjkLs6t5M5t5ENNcbbjWWoQSnVWqBheUYomvUoLhQtFbFMgxWuE364koshLWF5SHJHJPrAyDZ7LKdEwm5KQbP7dReuFvdBw95er4aSeQSVbHST6R7iwL3Z56uQ4AhGC3dkffncc89PVnVTMKakdMXfUwTa2hYj4nHrKarZ9P7M6UgRXXtAvNvB9Mm9TRWe3dK45JhN4Bu1fwtcWfdGKgeZQ1jECj2j8zPSqPR1AzPtBjVSpUA3rd24ACBn5N7EeJetmgCcMmqmYUuzyciMz1hiQo3nSXNEjT5FQCp5jcttQ3ce1RskHHBErvZhoPBVZL9nAy7wszWJhPz3fbHXocQcgrS528KvJsgUBxcX9EyAGCxET6C4UNJHgvi5XdQ9tQ6DG77cBmry`

_get_tx_key txid:_
`Error: no tx keys found for this txid`

_get_tx_proof txid address:_
`Error: error: Tx secret key wasn't found in the wallet file.`

## rating89us | 2019-06-13T18:23:19+00:00
(updated)

## ph4r05 | 2019-06-13T18:52:51+00:00
Aah this is quite helpful! Thanks! The "InProofV1" suggest the working transaction is incoming and as I indicated above, those work without the Trezor interaction and thus are working fine. 

Outgoing transactions, on the other hand, require Trezor to decrypt private ephemeral tx_keys.
The log `Error: no tx keys found for this txid` says it was not possible to get the tx_keys. Isn't there a log line above this error indicating possible cause of this failure? That would help a lot.

Tx_proof and get_tx_key do not work for recovered wallets. The transaction data have to be stored in the wallet cache file for the outgoing transaction. When the wallet is recovered from the blockchain the cached transaction data is lost (not stored on blockchain) and it is not possible to get the transaction tx_keys anymore. Can it be your case or you just create a new transaction and then you try to generate transaction proof?

To get more info I would need to insert more logging messages to the tx proof logic. For that you would need to compile my version of the monero-gui. Otherwise there are very few options I can help. I could add PR to the monero.git with new logging messages but it would take some time to get merged and we would need more messages for this debugging anyway.

## rating89us | 2019-06-13T21:15:15+00:00
>  the working transaction is incoming 

That's right. I realized my working "outgoing" transactions are all churn transactions.

I did some tests. I sent a new transaction, and checked before and after restarting GUI and CLI. Tx_key always returned 0000000000000000000000000000000000000000000000000000000000000000.

**Before closing wallet:**
```
2019-06-13 20:27:02.735	D Invalid address format
2019-06-13 20:27:02.735	D getProof: Error checking TxId and/or address
2019-06-13 20:27:02.736	D getProof: Generate clicked: txid 5d38dcaf282ee0ab389bbaa104098b670a64f3bd289030d42db7c380f6438ead, address
2019-06-13 20:27:02.736	D Getting payment proof:
2019-06-13 20:27:02.736	D txid: 5d38dcaf282ee0ab389bbaa104098b670a64f3bd289030d42db7c380f6438ead , address: , message:
```

(note the "Invalid address format" message. It also seems address is not included in getProof).

Result:
`SpendProofV1FVVosb92by4Rd3PoHzXXVYTyiBM8LaXm6iLHyzv1mxPBFsxnUFEAYQzZRZdCUVSy7UU2R9Z99j8E2HpJDrXSigaWCWQbU7UwA7tUD7EcJMXW9eHLnAtg9cPmTQbbBdiQdDCcd6u9SJ3mFgBZLm7k56kqcmbUEoukome1uiEHfj7T1ByBMQaMAz5iZAU1xxQxUzs4KvdCJTCmxj26HHZxfBbh913UAgttu48A86nM185ubz4TZ9iyCvwStK3xDEXb4yigvELJRTG8zXuE2bTA64qDQddeq76PtjtbGMv9z4V5EZhrZTShDnemcuxA5sYPjie26k51NvWYkbTgutSWDKfXLrZ5aVugDVZM2fuL8GC4pr9q1DSybb158cwvJP7R9LkrfgKkEpp9cctzbM3w39VW2bq8xYaox5ANT39Jq4gLHetceMECQ6G3B6aeeEtRCb18XBbmX3CaJVYqnxkDEfPoD6NFdcoSgfGVio5CpJ4a6k5QqX6629XYaEKLq13kRBa73BEgSX8emFxG3u8PAejEKeR8M1zAW1axmcF5xiBXKs5YRKHpKN6Wn98TbCEwMdTs3Lf9CGPs3v3QvJe8zCGywGxpn9AhMYhgn5FSBVjfeqW1ZQJAtEgNAVTzzmSVxPAwiMSS4LtGsYd6krNTVLupQRMzxCjBSnWUm1kTbiMSxgrDHuB968hZmob15jffgzCcFzBqp9oYiGYmgZaAfE4UkVkc6JZk3K4gVuCoXs3U7GnErHMmEPBZUALkAgidwESSWNLPxiyFJMQqmfYrZeyqToAXx2N8d75A4sQB2zxrtoMsjfYFpbeuP2j3e5ZuZrBT2ozSnK5i6faWD17u7n9z1sMutoa5RH8o7VaPwq1pHRUUARcrHfpGhpT9BVmHPBkNJQFdk4CJVSMvv5tiGW3tT8k73EfRsJvjaoWZ9kutRSvK4vFRt3e3ZTnKV3Wi3uhGxrWA`

Tx key: 0000000000000000000000000000000000000000000000000000000000000000


**After restarting GUI or CLI:**

```
2019-06-13 20:29:45.680	D getProof: Generate clicked: txid 5d38dcaf282ee0ab389bbaa104098b670a64f3bd289030d42db7c380f6438ead, address 8Bq5mQWRSKWSrBsieHEnDaWziqsW6Hi6SbbTuNsgao5Rfn8pp5EyMgPeser2hodX3Q9C8jDFkYVPZE6weskWBv9wBuYwyGs
2019-06-13 20:29:45.680	D Getting payment proof:
2019-06-13 20:29:45.680	D txid: 5d38dcaf282ee0ab389bbaa104098b670a64f3bd289030d42db7c380f6438ead , address: 8Bq5mQWRSKWSrBsieHEnDaWziqsW6Hi6SbbTuNsgao5Rfn8pp5EyMgPeser2hodX3Q9C8jDFkYVPZE6weskWBv9wBuYwyGs , message:
2019-06-13 20:29:45.682	E !received. THROW EXCEPTION: error::wallet_internal_error
2019-06-13 20:29:45.682	W /home/asuspc/monero-gui/monero/src/wallet/wallet2.cpp:10893:N5tools5error21wallet_internal_errorE: No funds received in this tx.
```
(no more "Invalid address format" message. Address is included in getProof).

Result:
`SpendProofV16P5uyQYuKPQXbjfEexw4bbNsvgxo4ps3TWtYzncuW8RzNZ7kQsCVntbZ9JwmnR4trEXJsmYui4cEfQSxYjTWEqKRDkv3xcNZgf84YjP1mjQEMrTdameHQmTAbgVhkDhb5xA5fqZhwuwdUYuhyWstwBFaNqg8XHmwAUzNRBduiffjmtojWr6tiHBMGsLDFq8fGNtxpN9yjPWr3qz5M16soLnf5HJB4eYSjPvF2Q9GJBgSsodWt7UmnnyhABNVJ28f4pLzQLEW2eiqfUQfTkNA1Hn8yME83bfiJut4RybJ9Ss6h4bWErQWLsnuVa4NUCc1N9Ue5r5F9AdLXF6N7extkHR7WBk17NwBiDLLWKuNwG2DJsbifduXxVPwaY65eysHDJLABpkmX19aA3kH9DjDZAQSpxouPnZj7p7aLnznSigCZUdnEXMXcVrY8K4J7qVgxiDMMqgpXRvEyfDbjxeysKEzfMY4vCfVyCJe99mryjpCFQQCrwGpwWmJShELiCbNqCLH3cR3ooTzbr3FBeoGRx8Se62eRAsh9qQEhsbSLQ85DbgmpQ9kqUfxKvHoGwz2avtzD4HZWRUpWRe5XHRZ5xJzFqBCpUPZkiP9bQoCKZoBczCstZG2tqNMUx1wWTVy3F1JHjtL2GfCBuvbDw2K9V52BarnDAzZDYTz4HNq4LjAwQYEg1VuC5YcatHyyJ5xYheLxA7N4UrBuyeDLe2Bggc5dz9da8doMNZX61dy5h6jWaD157SpReMDeabmF6V2tVeC7Na4Dvne3ZdHhmBzKCDZLYSLHCYZP2cGsAW3qsochCjcuPHYXFVA6H8rFZes2kCR6EKMsnB9dni2TnTFu4Gjpe2HbXztDGaZu2fBKJPMZbgmUt764RTvaErQtxqEGiH88KPcTkMAV4v1RYkti45XY7fQLW5xy2w2m1EP5K8pLNE7gwgYhmzpnZE7LUsgrHMBTvSu`

Tx key: 0000000000000000000000000000000000000000000000000000000000000000


## ph4r05 | 2019-06-14T13:50:10+00:00
I found the problem. The culprit is the tx key cache returns a zero vector which is falsely accepted as the tx key. Thus further check fails. When I fix this issue, Trezor decrypts transaction key and proof works. But there are some deadlocks on GUI that need to be fixed. So I will have to address this with dedicated PRs.

Thanks for your reports! It was very helpful to locate the culprit.

## rating89us | 2019-06-15T19:23:34+00:00
Great!

Just out of curiosity, how proof is generated in recovered wallets, since it is not possible to get the transaction tx_keys?

## ph4r05 | 2019-06-16T12:50:36+00:00
In order to generate the OutProofV1 you need tx_key, which is lost for recovered wallets. It is not possible.

## selsta | 2019-09-01T01:23:17+00:00
+resolved

# Action History
- Created by: rating89us | 2019-05-30T12:52:24+00:00
- Closed at: 2019-09-01T01:36:31+00:00
