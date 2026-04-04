---
title: monero-wallet-cli wants to create a new wallet when entering the name of an
  existing wallet
source_url: https://github.com/monero-project/monero/issues/1969
author: lllauri
assignees: []
labels: []
created_at: '2017-04-13T14:10:14+00:00'
updated_at: '2017-04-14T05:31:31+00:00'
type: issue
status: closed
closed_at: '2017-04-14T05:31:31+00:00'
---

# Original Description
Log:
> ubuntu@pine64:\~$ desktop/monero-v0.10.3.1/monero-wallet-cli
Monero 'Wolfram Warptangent' (v0.10.3.1-release)
Logging to desktop/monero-v0.10.3.1/monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): hoho
No wallet found with that name. Confirm creation of new wallet named: hoho
(Y/Yes/N/No): n
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): ^C
ubuntu@pine64:\~$ ls -ln desktop/monero-v0.10.3.1/
total 144012
-rw------- 1 1000 1000 44427573 Apr 13 09:50 hoho
-rw------- 1 1000 1000       95 Apr  3 16:06 hoho.address.txt
-rw------- 1 1000 1000      879 Apr  3 16:06 hoho.keys
-rwxr-xr-x 1 1000 1000  9791664 Mar 27 01:24 monero-blockchain-export
-rwxr-xr-x 1 1000 1000  9850440 Mar 27 01:19 monero-blockchain-import
-rw-rw-r-- 1 1000 1000     4442 Mar 31 16:16 monero-blockchain-import.log
-rwxr-xr-x 1 1000 1000  3812528 Mar 27 01:20 monero-utils-deserialize
-rwxr-xr-x 1 1000 1000 13214896 Mar 27 01:00 monero-wallet-cli
-rw------- 1 1000 1000   271610 Apr 13 13:36 monero-wallet-cli.log
-rwxr-xr-x 1 1000 1000 13523176 Mar 27 00:55 monero-wallet-rpc
-rwxr-xr-x 1 1000 1000 52547272 Mar 27 01:14 monerod


The wallet was restored from seed using the same monero-wallet-cli , looks like I mistyped the seed the 1st time:
> 2017-04-03 16:02:31.122         INFO    global  src/simplewallet/simplewallet.cpp:179   Confirm wallet name: hoho
2017-04-03 16:02:33.773         INFO    global  src/simplewallet/simplewallet.cpp:179   Generating new wallet...
2017-04-03 16:03:59.170         ERROR   global  src/simplewallet/simplewallet.cpp:179   Error: Electrum-style word list failed verification
2017-04-03 16:03:59.170         ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:4468  Failed to initialize wallet
2017-04-03 16:04:08.155         INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-04-03 16:04:12.909         INFO    global  src/simplewallet/simplewallet.cpp:179   Confirm wallet name: hoho
2017-04-03 16:04:16.469         INFO    global  src/simplewallet/simplewallet.cpp:179   Generating new wallet...
\*lots of warnings from default src/mnemonics/language_base.h\*
2017-04-03 16:06:47.590         INFO    global  src/simplewallet/simplewallet.cpp:179   Generated new wallet: _address_
2017-04-03 16:06:47.591         INFO    global  src/simplewallet/simplewallet.cpp:179   **********************************************************************
Your wallet has been generated!


If I specified the path using --wallet-file:
> ubuntu@pine64:~$ desktop/monero-v0.10.3.1/monero-wallet-cli --wallet-file desktop/monero-v0.10.3.1/hoho
Monero 'Wolfram Warptangent' (v0.10.3.1-release)
Logging to desktop/monero-v0.10.3.1/monero-wallet-cli.log
Wallet password:

then it worked and synced and I could send a tx.

Using ARMv8 build from getmonero.org

# Discussion History
## ghost | 2017-04-13T14:15:34+00:00
The wallet only searches the present working directory for the wallet files if run without --wallet-file. 

Otherwise it could find multiple potential wallet files with the same name in different places on your system. 

## lllauri | 2017-04-13T15:10:06+00:00
Ah yes, seems to be the case, I'm in different directory now compared to when I created the wallet.

But isn't it more logical to store the wallet in the working directory of monero-wallet-cli? The user can be all over the place while executables are usually static.

If this is a non-issue then feel free to close/delete it.

Thanks for the help.

## moneromooo-monero | 2017-04-13T21:10:26+00:00
No, it would be less logical.

## ghost | 2017-04-13T23:12:48+00:00
@lllauri It's easier if you close it yourself :)

# Action History
- Created by: lllauri | 2017-04-13T14:10:14+00:00
- Closed at: 2017-04-14T05:31:31+00:00
