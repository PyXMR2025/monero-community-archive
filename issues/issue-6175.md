---
title: 'Error: failed to find transaction input in key images'
source_url: https://github.com/monero-project/monero/issues/6175
author: tevador
assignees: []
labels: []
created_at: '2019-11-23T16:55:50+00:00'
updated_at: '2023-10-21T21:21:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Windows box that was shut down for about 1 month.

Got these errors when starting monerod to sync the node:

```
2019-11-23 16:05:31.980 E failed to find transaction input in key images. img=<f334994607c99c0d2deca2dd2cb0d22855076eca9fd4f3342a63e457fa2b5064>
2019-11-23 16:05:31.980 E transaction id = <b96184bdeb662f81b85ea8775ad21f4fc0f6f2a88b9fd5e01d46f6345924a76d>
2019-11-23 16:05:31.980 E failed to find transaction input in key images. img=<cb8ccf433fa5c62c403a6dbaaa2a4e8850ba4d77457118ee343f4dd65bb81582>
2019-11-23 16:05:31.980 E transaction id = <5e2f18eebd1da33eb5ac658e2c62bfb60de3467230b6e171fd037c84d2d3ea85>
```

Whole log including the last shutdown of monerod:

```
2019-10-28 14:02:03.461	7884	INFO	msgwriter	src/common/scoped_message_writer.h:102	Stop signal sent
2019-10-28 14:02:03.476	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:80	p2p net loop stopped
2019-10-28 14:02:03.898	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:83	Stopping core RPC server...
2019-10-28 14:02:03.898	[SRV_MAIN]	INFO	global	src/daemon/daemon.cpp:209	Node stopped.
2019-10-28 14:02:03.992	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:95	Deinitializing core RPC server...
2019-10-28 14:02:04.023	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:90	Deinitializing p2p...
2019-10-28 14:02:08.051	[SRV_MAIN]	INFO	global	src/daemon/core.h:94	Deinitializing core...
2019-10-28 14:02:10.098	[SRV_MAIN]	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2019-10-28 14:02:10.098	[SRV_MAIN]	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2019-11-23 16:05:09.962	6984	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-11-23 16:05:09.994	6984	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
2019-11-23 16:05:09.994	6984	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2019-11-23 16:05:09.994	6984	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2019-11-23 16:05:09.994	6984	INFO	global	src/daemon/core.h:63	Initializing core...
2019-11-23 16:05:09.994	6984	INFO	global	src/cryptonote_core/cryptonote_core.cpp:506	Loading blockchain from folder E:\monero-blockchain\lmdb ...
2019-11-23 16:05:31.980	6984	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:445	failed to find transaction input in key images. img=<f334994607c99c0d2deca2dd2cb0d22855076eca9fd4f3342a63e457fa2b5064>
2019-11-23 16:05:31.980	6984	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:445	transaction id = <b96184bdeb662f81b85ea8775ad21f4fc0f6f2a88b9fd5e01d46f6345924a76d>
2019-11-23 16:05:31.980	6984	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:445	failed to find transaction input in key images. img=<cb8ccf433fa5c62c403a6dbaaa2a4e8850ba4d77457118ee343f4dd65bb81582>
2019-11-23 16:05:31.980	6984	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:445	transaction id = <5e2f18eebd1da33eb5ac658e2c62bfb60de3467230b6e171fd037c84d2d3ea85>
2019-11-23 16:05:55.006	6984	INFO	global	src/cryptonote_core/cryptonote_core.cpp:668	Loading checkpoints
2019-11-23 16:05:56.350	6984	INFO	global	src/daemon/core.h:73	Core initialized OK
2019-11-23 16:05:56.350	6984	INFO	global	src/daemon/p2p.h:63	Initializing p2p server...
2019-11-23 16:05:57.162	6984	INFO	global	src/daemon/p2p.h:68	p2p server initialized OK
2019-11-23 16:05:57.162	6984	INFO	global	src/daemon/rpc.h:62	Initializing core RPC server...
2019-11-23 16:05:57.162	6984	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 127.0.0.1 (IPv4):18081
2019-11-23 16:05:57.162	6984	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2019-11-23 16:05:58.053	6984	INFO	global	src/daemon/rpc.h:68	core RPC server initialized OK on port: 18081
2019-11-23 16:05:58.053	6984	INFO	global	src/daemon/rpc.h:73	Starting core RPC server...
2019-11-23 16:05:58.053	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:78	core RPC server started ok
2019-11-23 16:05:58.069	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:78	Starting p2p net loop...
2019-11-23 16:05:59.069	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1644	
2019-11-23 16:05:59.069	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1644	**********************************************************************
2019-11-23 16:05:59.069	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1644	The daemon will start synchronizing with the network. This may take a long time to complete.
2019-11-23 16:05:59.069	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1644	
2019-11-23 16:05:59.069	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1644	You can set the level of process detailization through "set_log <level|categories>" command,
2019-11-23 16:05:59.069	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1644	where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2019-11-23 16:05:59.069	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1644	
2019-11-23 16:05:59.069	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1644	Use the "help" command to see the list of available commands.
2019-11-23 16:05:59.069	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1644	Use "help <command>" to see a command's documentation.
2019-11-23 16:05:59.069	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1644	**********************************************************************
2019-11-23 16:05:59.194	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:374	[142.93.228.111:18080 OUT] Sync data returned a new top block candidate: 1954619 -> 1973328 [Your node is 18709 blocks (25 days) behind] 
2019-11-23 16:05:59.194	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:374	SYNCHRONIZATION started
```

Both of the transactions are in block 1954620, while the node was synced to 1954619 when it was started today.

The error doesn't appear anymore after restarting monerod.

# Discussion History
## unamefailed | 2020-12-19T17:09:18+00:00
On Linux ,too 
```
2020-11-28 05:19:02.397	E failed to find transaction input in key images. img=<69f4245540f9a5384c5c9d516651f11c4cd8e7a17bf7a54677c25a58a9ccf665>
2020-11-28 05:19:02.397	E transaction id = <e004fe900d2b68c325a4dd9aaeb4656f24809ca9b15528613e0b5ba6593d1904>
2020-11-28 05:19:02.399	E failed to find transaction input in key images. img=<f8bd58f22a8bd46c1695741eb77fac6e5ee4da319e1c477e61324a5c431a4706>
2020-11-28 05:19:02.399	E transaction id = <e98ec40a22281ab25b3c224823cbba31e5378190d2eece7de12dcd33f818bb05>
2020-11-28 05:19:02.403	E failed to find transaction input in key images. img=<2f964096c489e1f2920a0ca01bc90bfe6e638ceee9ce58db065d05f59fafbe48>
2020-11-28 05:19:02.403	E transaction id = <f2fa0a01bd304e893288b210d3a0fa9c9818b4abe9711410f633984fb4c0a908>
2020-11-28 05:19:02.405	E failed to find transaction input in key images. img=<54fc3cb58cc997ef42a7bcde5d9b8307fb9dc146470489ea567c8e72539fa0c7>
2020-11-28 05:19:02.405	E transaction id = <1ea9f870597276103a88fc5be31d2c5184953440c463acab0ae04b61748c920b>
2020-11-28 05:19:02.407	E failed to find transaction input in key images. img=<b8954434e0dd8e3475da5c7f321abff74f26e5a7e6ecef9b3ca19956695240a0>
2020-11-28 05:19:02.407	E transaction id = <7207c367d33195bfd289ab7d29e094993dc727ced4a1804c9e70d04331cf490c>
2020-11-28 05:19:02.409	E failed to find transaction input in key images. img=<f30db4f762fca61aa6f1af5d562c461cc277e3397f543c15b9e0c893797fb07b>
2020-11-28 05:19:02.409	E transaction id = <28983c0c4de5b02cab4dcf443dd37746da651aab2ce7445b23e1b32a70b43b0d>
2020-11-28 05:19:02.413	E failed to find transaction input in key images. img=<a7712feedc7f74309fbba4e665d0a6183af212cf55ea329e8850fe3c1e181a49>
2020-11-28 05:19:02.413	E transaction id = <d83614b3e3c695589dc04dd1de925d211a96d98962718d5e26f1cfc69f976914>
2020-11-28 05:19:02.416	E failed to find transaction input in key images. img=<fc72b8cb19f95953d2abac7e43dd35cd2b81bc9e6db2db002d9f3d3e008a02f3>
2020-11-28 05:19:02.416	E transaction id = <21c36e7647aa8116dc10cd8d3d26144dc00a6bd189a32d21099c2db961217519>
2020-11-28 05:19:02.418	E failed to find transaction input in key images. img=<d67719e8924d57f24e000d78fcc453b552b363a2f40aa7909488263c652d8afa>
2020-11-28 05:19:02.418	E transaction id = <744207301fdf0cc657b465d9a021c180691665053d730b0142065bdebcb0a81c>
2020-11-28 05:19:02.421	E failed to find transaction input in key images. img=<e607cdaa865ac482a1ad56327975445ab987aa660784a2775c9012445e5e55eb>
2020-11-28 05:19:02.421	E transaction id = <6b2d2c4b70caa32803ad22b83d14ff353e80c1b05db7101cf6a49be8c6c76a23>
2020-11-28 05:19:02.424	E failed to find transaction input in key images. img=<c8b1b697d5efcd781edf7ddc9905727293e86aa42ddec6ae68280580fa70a468>
2020-11-28 05:19:02.424	E transaction id = <47b77b07664862d6b77110a1fa478a3db3c1caa37880162ac71903485b2b1024>
2020-11-28 05:19:02.426	E failed to find transaction input in key images. img=<f01082b97b1c9d3de966df15166b79aca5e9f1af9a76a3cdd82bc24f41c374f0>
2020-11-28 05:19:02.426	E transaction id = <eec4283b387867fac87fc1b56c4b714ac6c0fbce739a897e7e4ac531c568d12a>
2020-11-28 05:19:02.428	E failed to find transaction input in key images. img=<b320b4953f0a9691aca759c94dfd3558c6ab6ce34432790f0cac3a40f5a46616>
2020-11-28 05:19:02.428	E transaction id = <f5b43bfb26d2e58b3530387028e227e074178eae1f5ca393dc72008903c34b2c>
2020-11-28 05:19:02.431	E failed to find transaction input in key images. img=<519e78608d54c0276db7e821feedad17a23a8245a85050baea248727d1562888>
2020-11-28 05:19:02.431	E transaction id = <37a45a7a8a27c9dfb7e425b1648215511b7a298b87a610166a902f0286f14c41>
2020-11-28 05:19:02.433	E failed to find transaction input in key images. img=<5776b699f3ea21602e42b0845415138bd9546129df903a6eb4543cf977b30b60>
2020-11-28 05:19:02.433	E transaction id = <241a79726c7f7053f96340828dae52dea6dc014439f3811a2530ee02094ae04a>
2020-11-28 05:19:02.436	E failed to find transaction input in key images. img=<a7679056bb146ef135f6a86ad6d29d725b1a175469c701b6df44a15ea1a8bef0>
2020-11-28 05:19:02.436	E transaction id = <4cb16a12b822d0e5b1f6ab0d0ded054b0a2ecc21a59cc9ffc086ab8656e7645c>
2020-11-28 05:19:02.439	E failed to find transaction input in key images. img=<b5459fe1517b1a1138c37e872e6aae27a0b727e5e6aa93f72fed4dfba31ee0a0>
2020-11-28 05:19:02.439	E transaction id = <56294cef0a834e849dc889847ee6a44a7f34287f9d96d461b8dae8130ff8fe62>
2020-11-28 05:19:02.441	E failed to find transaction input in key images. img=<d4a995a7b5594ed4c88399c35320c69329f34e85168bb1c86bc1d8240f725222>
2020-11-28 05:19:02.441	E transaction id = <d5dd3df702285b6acc823211fb479c1b85677bbe177b1e35f63f22c704ebd568>
2020-11-28 05:19:02.444	E failed to find transaction input in key images. img=<b70dd474c3e6e076e994234bb19168900cd54c05e618c9db33f48ac8f2d42e71>
2020-11-28 05:19:02.444	E transaction id = <efbd89be88b460ec8d75b7aaab8bd0dc34b5dceaa98a0919df3bd23e2fca3e6b>
2020-11-28 05:19:02.447	E failed to find transaction input in key images. img=<7d0613eaf7417c63cb3f2609781408bbd9f43b2da5cfcf4e675204ed153a88a5>
2020-11-28 05:19:02.447	E transaction id = <90f7867227b48ae0b3a2ceaea4e53bce337a007828f5ae43f70f911d683c166c>
2020-11-28 05:19:02.449	E failed to find transaction input in key images. img=<761a5e5dd010c8ebbd9588c69ac06e3adbd14d5a57f21f595f36ccc22a10a943>
2020-11-28 05:19:02.449	E transaction id = <2e9396c5e4af69746abf47b26d49f07e5fbeb33a12186034da2b2224e7bf7270>
2020-11-28 05:19:02.452	E failed to find transaction input in key images. img=<921dc93e9e6c6df3b7b26c7c25b5b870a1f3b0d28a03cbb3af124e867fe75140>
2020-11-28 05:19:02.452	E transaction id = <71f38a938de796af0e1f34e447a30b38e5c08d530854fb868cb385cc1e99ce7e>
2020-11-28 05:19:02.455	E failed to find transaction input in key images. img=<c8ca5cdca80384d00dcb51493b4990b1cf20778b2c8b0941c9e7e3d5d8f16056>
2020-11-28 05:19:02.455	E transaction id = <e1f9b5230ea6546a184214c5aa34aa71f6822dbdeaf44556b41e050b9b938686>
2020-11-28 05:19:02.457	E failed to find transaction input in key images. img=<7125514e77407e3713375adb5d4d16521bdbc262741930cbc2c1424b685cfaa0>
2020-11-28 05:19:02.457	E transaction id = <fda48f4576df863c11b728402b444efa5f7bbd41ad9271cddbea704be72f3d89>
2020-11-28 05:19:02.460	E failed to find transaction input in key images. img=<fec232fbcce92cf9002de03c0d2065733799398decdca615ee8004eee6280a7d>
2020-11-28 05:19:02.460	E transaction id = <f8a68aa40f81b3d51143529b38eb30a866c1e10c5f3bcde527f5b77715e82b92>
2020-11-28 05:19:02.463	E failed to find transaction input in key images. img=<945a6bdf8b87055b7dbfee79259e88f8a974cfab70a812811f11b543c53be488>
2020-11-28 05:19:02.463	E transaction id = <2fe58a96d8cdc852689bbef4b22d9595ebea006acf0a006910cb6ce21b70b09c>
2020-11-28 05:19:02.465	E failed to find transaction input in key images. img=<c40cc0d3cd93dc08ad84c755d45fb1c291357d04bb977d428f65937a85afe700>
2020-11-28 05:19:02.465	E transaction id = <e53537040789a19a2303dfbba7f51db19ad8e80b5c7545c723b80385618e0da0>
2020-11-28 05:19:02.468	E failed to find transaction input in key images. img=<bc1f288c23fce2de5420af2ef0dfbfee54d789893c20b53aeb73f65c2619d11d>
2020-11-28 05:19:02.468	E transaction id = <4cdc4e0f4bfcacd676c7a28061a0eca4bf6c98b8870c7c455f05e7c9e226aab1>
2020-11-28 05:19:02.471	E failed to find transaction input in key images. img=<4853ddb8eb172ea6a2bc914cbadbfb190988ea7cb9da4eeda73ba15decb5ebd7>
2020-11-28 05:19:02.471	E transaction id = <44133b65fcb395d3d7db8333b9b59a8a471eec4b8792ba865c52534a4e11eeb5>
2020-11-28 05:19:02.473	E failed to find transaction input in key images. img=<c84fe282063207a8f5cd06ed5425076864e391f1d1a2c634e096bae46c856894>
2020-11-28 05:19:02.473	E transaction id = <35acbbfea0f04062e86f53ea9a660d9fa130bbf38a725803d76abbdc5e856bb8>
2020-11-28 05:19:02.477	E failed to find transaction input in key images. img=<99fd2881cf95cd8407d3b18761400a0c197521fa0ec893167a9a067b46cb28db>
2020-11-28 05:19:02.477	E transaction id = <30ff360c7c0fddc75c66e61c8303a2d0a7ba6e39a0f0b9bec4a0d28eddcb9eba>
2020-11-28 05:19:02.480	E failed to find transaction input in key images. img=<ea22911f30bae97636b194a66fb16617093711ae1fc34fdb3a3c234b02e6ef66>
2020-11-28 05:19:02.480	E transaction id = <0c91079405c6a0d067b1fb839e8aefb632d74f3f6082276296622517bd0f28c7>
2020-11-28 05:19:02.483	E failed to find transaction input in key images. img=<5d8ca223f064e4889aee5fcd64a20708a9930aa8a6435e8b1c0e6ddea5399837>
2020-11-28 05:19:02.483	E transaction id = <065c285d0ccdd986475b500a43d4b17b4f7ea9576762ea18118d455802ac18d1>
2020-11-28 05:19:02.486	E failed to find transaction input in key images. img=<f3dc2da6ed95b47b0ce97bcdc0bfd28900811665fa1c10515ffca69b72d46c75>
2020-11-28 05:19:02.486	E transaction id = <ccff4064373d5e56dde76c0ceff403eee38fa6494283a33f69a3956e2aa727d7>
2020-11-28 05:19:02.488	E failed to find transaction input in key images. img=<e7811be7df877d8c694d3202eb443b648961e40e68aec20e8dffd0e07a6a08ef>
2020-11-28 05:19:02.488	E transaction id = <7a957b6b17160051233fb483a646931ede9e5ac522a5dfa8b11a12fae833d7d9>
2020-11-28 05:19:02.490	E failed to find transaction input in key images. img=<260292713230d3ccca15f72e10fc4813a79e3489571c33517f9b81a902ec939f>
2020-11-28 05:19:02.490	E transaction id = <e1d801cadb0769b0122397d8ebf98e8023f115cdc9b98fe90b2d37c3e5caf8dd>
2020-11-28 05:19:02.493	E failed to find transaction input in key images. img=<08eb0fd424a5a229415609b340a334cfe37c054ec702878cf6503bf674b29ec1>
2020-11-28 05:19:02.493	E transaction id = <19b5f319a8d8adb550f308b445ac816daec9438e6eb0679c9df8ea9315f5eede>
2020-11-28 05:19:02.495	E failed to find transaction input in key images. img=<78457949e8aff1cdc0e677e61d1d0e9e093333603c6844b73c2842b17b73a0d6>
2020-11-28 05:19:02.495	E transaction id = <3f8c773d0c32ecb6929cf73c15e197edc4bec43839c0dc133d5fba65b4c680df>
2020-11-28 05:19:02.497	E failed to find transaction input in key images. img=<9828a9dfb3ecff3bc7e6384c7bb69572e453d66a5ac9b89abbf75a970944699e>
2020-11-28 05:19:02.497	E transaction id = <79e9f5764d26cb212dd1bd6755eb3f8ad8a57e3c6dfb8de597be18519c6fdfdf>
2020-11-28 05:19:02.499	E failed to find transaction input in key images. img=<84f7b94ba93a7081609d0f8f46417e06d9e667aa23cf9a5a7e3d00def35a2b41>
2020-11-28 05:19:02.499	E transaction id = <da7f0eb477ef43ac33188f26689e9d03ff1c26191665ebe1a79bd28aafeeb3e0>
2020-11-28 05:19:02.501	E failed to find transaction input in key images. img=<33b4682b5cfb04f5d20a787311328878aadaca7598b000b651a5b9f62a808a50>
2020-11-28 05:19:02.501	E transaction id = <6a6036acc6312a7d9807df3a2f7949cfeca670ed463d8c13b68bcbd0d952a4e2>
2020-11-28 05:19:02.504	E failed to find transaction input in key images. img=<6cd8572b5de7d633317119e51a9e6e3334133dc6ef0adf974afb3f9e89cc604c>
2020-11-28 05:19:02.504	E transaction id = <088bc1f2be9c99d96ef819d58e17b4632e652ad1f8e612565f84f4a6e80895e5>
2020-11-28 05:19:02.507	E failed to find transaction input in key images. img=<cce5371a054ea2e4da5396229797f14f618f077873a0aeb76081f366cbf4dfe8>
2020-11-28 05:19:02.507	E transaction id = <a1da4947cf1430bc1580db24345d2cfc4375a71bafb611e5a9543449595239ec>
2020-11-28 05:19:02.510	E failed to find transaction input in key images. img=<fc9e242f6908d5d74cf26587fd53d7d8134126ad8a817b9c6005f089dc508ac0>
2020-11-28 05:19:02.510	E transaction id = <45dd64ae11eae8d14a8e899838ccab2d5a40bac8f73a7f96c8e3c9903f6c24f0>
2020-11-28 05:19:02.512	E failed to find transaction input in key images. img=<97219e521484e2e634c3cd8bd5046efb1bea4c75bd56b6fa6dd9eb07368416f7>
2020-11-28 05:19:02.512	E transaction id = <bd8396137166bacb6f861641027babe7d7cd9dd0e5d6be14b264d2e0a52c91fb>
2020-11-28 05:19:02.514	E failed to find transaction input in key images. img=<8add8e8dd337bb923afd362bb8d76d29cae3df6fb729159e8f36c484929113ff>
2020-11-28 05:19:02.514	E transaction id = <4c9e71fdde48096ef7d45eef84c31526541751fde2176710252c0b933686defd>
```

## mondsen | 2021-01-09T07:13:08+00:00
I just compiled  v0.17.1.19 on RP4 with Ubuntu 20.04 and get the following:

This happened only after first startup! Second startup is OK.

```2021-01-09 07:10:43.097 I Initializing core...
2021-01-09 07:10:43.098 I Loading blockchain from folder /home/ethereum/.bitmonero/lmdb ...
2021-01-09 07:10:46.655 E failed to find transaction input in key images. img=<92170408a716cb839ebae86e0a58a0177f55c8121d85d63ffcab69c7695dd725>
2021-01-09 07:10:46.655 E transaction id = <9ad8aee6b97644e3fc9a18402f17df9ecce5f0462c767ea966b0eb61e18e4594>
2021-01-09 07:10:46.656 E failed to find transaction input in key images. img=<6d3e1c1fbaaee5a4d537aadd54bd56b88613e06c9b2d466b9557b4ae5e543e26>
2021-01-09 07:10:46.657 E transaction id = <2319808ee3d65fb2e9d0eea1df6f15535917de8e5d59fc9b8eafec709cb8f9bf>
2021-01-09 07:10:46.658 E failed to find transaction input in key images. img=<b84e48f8f38c7bdba02688b471cc63e6159db8f54650fcde6cc7852e16188743>
2021-01-09 07:10:46.658 E transaction id = <f9f27e2d3a0f259c058905b5a5dc2506caeec71dd6902065fdfe1f8cc02deddf>
2021-01-09 07:10:46.659 E failed to find transaction input in key images. img=<853bee404ae5aa8d6884bb7e75f0265cefc565a8a38301a0d200d1bfc9c8f182>
2021-01-09 07:10:46.660 E transaction id = <e1b5c62302d85e66d3c0a978b8d969b6a9f99f7cbe48c67c9b31f6149e0be2e4>
2021-01-09 07:10:48.868 I Loading checkpoints
2021-01-09 07:10:48.872 I Core initialized OK
2021-01-09 07:10:48.873 I Initializing p2p server...
2021-01-09 07:10:49.736 I p2p server initialized OK
2021-01-09 07:10:49.736 I Initializing core RPC server...
2021-01-09 07:10:49.737 I Binding on 127.0.0.1 (IPv4):18089
2021-01-09 07:10:52.370 I core RPC server initialized OK on port: 18089
2021-01-09 07:10:52.371 I Initializing restricted RPC server...
2021-01-09 07:10:52.371 I Binding on 0.0.0.0 (IPv4):18081
2021-01-09 07:10:54.345 I restricted RPC server initialized OK on port: 18081
2021-01-09 07:10:54.356 I Starting core RPC server...
2021-01-09 07:10:54.357 I core RPC server started ok
2021-01-09 07:10:54.357 I Starting restricted RPC server...
2021-01-09 07:10:54.357 I restricted RPC server started ok
2021-01-09 07:10:54.362 I Public RPC port 18081 will be advertised to other peers over P2P
2021-01-09 07:10:54.362 I Starting p2p net loop...```

## maogo | 2022-11-02T01:22:38+00:00
the problem remains unresolved.

## maxweisspoker | 2023-10-21T21:21:42+00:00
Just commenting that I ran into this issue when I ran monerod with low priority.  Running it with the default (or high) priority fixed the issue.

# Action History
- Created by: tevador | 2019-11-23T16:55:50+00:00
