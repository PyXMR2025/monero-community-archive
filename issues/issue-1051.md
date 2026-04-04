---
title: 'Daemon is failling to start '
source_url: https://github.com/monero-project/monero-gui/issues/1051
author: hammelj97
assignees: []
labels:
- resolved
created_at: '2017-12-28T21:09:46+00:00'
updated_at: '2018-01-01T13:45:11+00:00'
type: issue
status: closed
closed_at: '2018-01-01T13:45:11+00:00'
---

# Original Description
I get the message "Daemon failed to start.
Please check your wallet and daemon log for errors. You can also try to start monerod.exe manually."

the Daemon log says 
2017-12-28 20:30:04.475	760	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-28 20:30:26.985	760	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-28 20:30:46.536	760	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-28 20:30:46.835	4404	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-12-28 20:30:46.879	4404	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-12-28 20:30:46.879	4404	WARN 	net.http	src/wallet/wallet_errors.h:707	C:/msys64/home/vagrant/slave/monero-core-win64/build/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-12-28 20:30:46.879	4404	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
2017-12-28 20:30:46.880	8396	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-12-28 20:30:47.936	4404	ERROR	WalletAPI	src/wallet/api/wallet.cpp:553	Status_Critical - not storing wallet
2017-12-28 20:32:44.643	760	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-28 20:32:44.696	4336	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 42fu5WXS454bxz6xwfk9zrbGS65r8pcQk391GioSxpaadhPv5gceFz8CXdcEbacWgjgWgdvLfGSHA3VhxxWSKu1N7bp157c

if I launch monerod.exe manually even as an administrator it crashes out

if I run it via command prompt it tells me
it failed to open db handle for m_hf_starting_heights: MDB Corrupted: located page was wrong type -  you may want to --db-salvage

What should I do?



# Discussion History
## SleepswithGators | 2017-12-29T23:05:24+00:00
I have been reading about similar situations all day through reddit and other Monero communities.

I have gone as far as deleting the entire wallet and starting all over again, though now it won't even start asking about running monerorod.

I have the wallet running on Ubuntu just fine, just can't seem to get it to run on Windows 10.

## dEBRUYNE-1 | 2017-12-30T16:17:23+00:00
@SleepswithGators & @hammelj97 Can you guys check this issue and see if anything is applicable to your situation(s)?

https://github.com/monero-project/monero-gui/issues/890

## hammelj97 | 2017-12-30T18:36:59+00:00
@dEBRUYNE-1 I have read through it before posting here and It didn't work

these are the last 600 lines of the log
[https://paste.fedoraproject.org/paste/Q8WlKoIwZtAHLxgM-Mwh2A](url)

## dEBRUYNE-1 | 2017-12-30T22:39:39+00:00
@hammelj97 I see. There's nothing apparent in that log. However, I missed this part from your initial post:

>it failed to open db handle for m_hf_starting_heights: MDB Corrupted: located page was wrong type - you may want to --db-salvage

Which indicates that your blockchain is likely corrupted. Try this guide:

https://monero.stackexchange.com/questions/6586/daemon-shuts-down-on-startup-mdb-bad-txn-transaction-must-abort-has-a-child/

## hammelj97 | 2017-12-30T22:43:18+00:00
@dEBRUYNE-1 Thanks!!!

## dEBRUYNE-1 | 2018-01-01T13:41:59+00:00
+resolved

# Action History
- Created by: hammelj97 | 2017-12-28T21:09:46+00:00
- Closed at: 2018-01-01T13:45:11+00:00
