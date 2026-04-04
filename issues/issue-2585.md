---
title: bug creating and saving GUI wallet and key files (solved)
source_url: https://github.com/monero-project/monero-gui/issues/2585
author: criptonoia
assignees: []
labels: []
created_at: '2019-12-11T20:01:47+00:00'
updated_at: '2019-12-20T00:30:53+00:00'
type: issue
status: closed
closed_at: '2019-12-20T00:30:53+00:00'
---

# Original Description
hello,
as i was creating a monero wallet, the app "GUI wallet" failed to create the files and key for the wallet. it was my first time using monero and no error message popped up for me. after using the wallet and sending 1.69926200 monero, the app closed my wallet and there is no way to recover that. 
i still have the log, i will paste a part of it here where you can see the bug
"2019-12-11 16:54:44.892  16632  ERROR  wallet.wallet2  src/wallet/wallet2.cpp:3849  failed to generate wallet keys file C:/Users/x/Documents/Monero/wallets/monero /monero .keys.new
2019-12-11 16:54:44.893  16632  ERROR  wallet.wallet2  src/wallet/wallet2.cpp:5691  !r. THROW EXCEPTION: error::file_save_error
2019-12-11 16:54:44.893  16632  ERROR  WalletAPI  src/wallet/api/wallet.cpp:917  Error saving wallet: failed to save file "C:/Users/x/Documents/Monero/wallets/monero /monero .keys"
2019-12-11 16:54:44.909  16632  ERROR  wallet.wallet2  src/wallet/wallet2.cpp:5256  !boost::filesystem::exists(m_keys_file, ignored_ec). THROW EXCEPTION: error::file_not_found
2019-12-11 16:54:44.912  16632  INFO  logging  contrib/epee/src/mlog.cpp:273  New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-12-11 16:54:44.937  9260  INFO  global  contrib/epee/src/net_ssl.cpp:127  Generating SSL certificate
2019-12-11 16:54:44.944  2188  INFO  global  contrib/epee/src/net_ssl.cpp:127  Generating SSL certificate
2019-12-11 16:54:44.964  16632  ERROR  wallet.wallet2  src/wallet/wallet2.cpp:5256  !boost::filesystem::exists(m_keys_file, ignored_ec). THROW EXCEPTION: error::file_not_found
2019-12-11 16:54:52.634  10076  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1031  daemonBlockChainHeight: Failed to connect to daemon
2019-12-11 16:54:52.635  10076  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1050  daemonBlockChainTargetHeight: Failed to connect to daemon
2019-12-11 16:54:52.635  10076  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1031  daemonBlockChainHeight: Failed to connect to daemon
2019-12-11 16:54:52.649  5108  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1031  daemonBlockChainHeight: Failed to connect to daemon
2019-12-11 16:54:52.650  6664  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1050  daemonBlockChainTargetHeight: Failed to connect to daemon
2019-12-11 16:54:52.654  6664  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1031  daemonBlockChainHeight: Failed to connect to daemon
2019-12-11 16:55:02.641  10076  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1031  daemonBlockChainHeight: Failed to connect to daemon
2019-12-11 16:55:02.644  10076  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1050  daemonBlockChainTargetHeight: Failed to connect to daemon
2019-12-11 16:55:02.647  10076  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1031  daemonBlockChainHeight: Failed to connect to daemon
2019-12-11 16:55:02.653  6664  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1031  daemonBlockChainHeight: Failed to connect to daemon
2019-12-11 16:55:02.656  14816  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1050  daemonBlockChainTargetHeight: Failed to connect to daemon
2019-12-11 16:55:02.658  14816  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1031  daemonBlockChainHeight: Failed to connect to daemon
2019-12-11 16:57:37.179  16632  ERROR  wallet.wallet2  src/wallet/wallet2.cpp:5733  !success. THROW EXCEPTION: error::file_save_error
2019-12-11 16:57:37.180  16632  ERROR  WalletAPI  src/wallet/api/wallet.cpp:917  Error saving wallet: failed to save file "C:/Users/x/Documents/Monero/wallets/monero /monero .new"
2019-12-11 16:59:10.433  16632  WARNING  frontend  src/wallet/api/wallet.cpp:410  Data set on unsupported clipboard mode. QMimeData object will be deleted.
2019-12-11 17:06:24.352  10076  WARNING  wallet.wallet2  src/wallet/wallet2.cpp:2087  Received money: 1.699162000000, with tx: <2419342b1d9a7d3cfcc92b505a8700754e7b556c3c2740011efa1014df59c4ce>
2019-12-11 17:16:09.844  16632  WARNING  frontend  src/wallet/api/wallet.cpp:410  Data set on unsupported clipboard mode. QMimeData object will be deleted.
2019-12-11 17:30:28.132  10076  ERROR  WalletAPI  src/wallet/api/wallet.cpp:1050  daemonBlockChainTargetHeight: Failed to connect to daemon
2019-12-11 17:54:44.419  12152  ERROR  wallet.wallet2  src/wallet/wallet2.cpp:5733  !success. THROW EXCEPTION: error::file_save_error
 
2019-12-11 17:54:44.419  12152  ERROR  WalletAPI  src/wallet/api/wallet.cpp:917  Error saving wallet: failed to save file "C:/Users/x/Documents/Monero/wallets/monero /monero .new"
2019-12-11 17:54:44.437  16632  ERROR  frontend  src/wallet/api/wallet.cpp:414  Trying to close non existing wallet  QObject(0x0)
2019-12-11 17:56:24.404  16632  ERROR  frontend  src/wallet/api/wallet.cpp:414  shellItem: SHCreateItemFromParsingName(file:///c/Users/x/Documents/Monero/wallets)) failed (An attempt was made to reference a token that does not exist.)
2019-12-11 17:56:24.406  16632  ERROR  frontend  src/wallet/api/wallet.cpp:414  shellItem: SHCreateItemFromParsingName(file:///c/Users/x/Documents/Monero/wallets)) failed (The operation completed successfully.)
2019-12-11 17:57:17.483  10712  INFO  logging  contrib/epee/src/mlog.cpp:273  New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-12-11 17:57:17.483  10712  WARNING  frontend  src/wallet/api/wallet.cpp:410  app startd (log: C:/Users/x/AppData/Roaming/monero-wallet-gui/monero-wallet-gui.log)
2019-12-11 17:57:17.484  10712  WARNING  frontend  src/wallet/api/wallet.cpp:410  Qt:5.9.7 GUI:v0.15.0.1 | screen: 1920x1080 - dpi: 120 - ratio:1.10899"

# Discussion History
## selsta | 2019-12-11T20:27:02+00:00
Do you still have the seed?

## criptonoia | 2019-12-11T20:37:40+00:00
no, i never had the seed

## selsta | 2019-12-11T20:46:09+00:00
Did it display a seed during wallet creation?

## criptonoia | 2019-12-11T21:40:31+00:00
i cannot remember, but i surely do not have it now

## selsta | 2019-12-11T21:55:10+00:00
Please press Windows+R, enter `%TEMP%` and a folder will open which should contain a wallet and .key file. Save them to the desktop and try to open them with the GUI.

## criptonoia | 2019-12-11T22:20:03+00:00
when i try that it just says wrong password

## selsta | 2019-12-11T22:20:35+00:00
Can you try with no password?

## criptonoia | 2019-12-11T22:22:00+00:00
when you "open wallet from file" it automatically asks you for the password, how to access it without the password?

## selsta | 2019-12-11T22:22:24+00:00
Enter a blank password

## criptonoia | 2019-12-11T22:25:48+00:00
so this got me into those wallets, there are 4 temp files, they each end with a different character (H, p or q) but all of them look empty, (0 balance)

## selsta | 2019-12-11T22:31:42+00:00
Make sure to save all of them on desktop.

Is one of them matching with the address you sent coins to?

## criptonoia | 2019-12-11T22:33:41+00:00
yes, i have saved all of them, and it does match the address, but it still shows up empty

## selsta | 2019-12-11T22:34:29+00:00
What does it say in the bottom left corner? Are both bars synchronized?

## criptonoia | 2019-12-11T22:36:51+00:00
thank you for your help, i did find my money now. this has been really helpful.

## selsta | 2019-12-11T22:37:28+00:00
Can you open the issue again so we can find out why it didn't save the wallet in the first place?

## criptonoia | 2019-12-11T22:38:00+00:00
yes sure, i can send you the log if you want

## criptonoia | 2019-12-11T22:39:55+00:00
some guy said it might be because there was a space at the end of the wallet name, as mentioned in this line of the log "2019-12-11 16:57:37.180 16632 ERROR WalletAPI src/wallet/api/wallet.cpp:917 Error saving wallet: failed to save file "C:/Users/x/Documents/Monero/wallets/monero /**monero .new**""

## selsta | 2019-12-11T22:40:46+00:00
Spaces should be okay.

Did you use the installer?

## criptonoia | 2019-12-11T22:42:12+00:00
yes, i used the installer version

## criptonoia | 2019-12-11T22:44:40+00:00
there is more stuff in the log if you want the whole transcript

# Action History
- Created by: criptonoia | 2019-12-11T20:01:47+00:00
- Closed at: 2019-12-20T00:30:53+00:00
