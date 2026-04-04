---
title: 'monero-wallet-cli: failed to load wallet: basic_string::_M_replace_aux'
source_url: https://github.com/monero-project/monero/issues/1106
author: nthterm
assignees: []
labels: []
created_at: '2016-09-20T00:57:47+00:00'
updated_at: '2017-08-07T19:00:23+00:00'
type: issue
status: closed
closed_at: '2017-08-07T19:00:23+00:00'
---

# Original Description
Wallet created in 0.9.4, ubuntu 16.04 pre-built binaries using simplewallet. Upon deleting db and resyncing db for 0.10.0, I tried to load old simplewallet wallet into monero-wallet-cli and got the following error:

monoero-wallet-cli error:
failed to load wallet: basic_string::_M_replace_aux

Output of monero-wallet-cli.log:
2016-Sep-19 17:42:50.714003 Loaded wallet keys file, with public address: 47YFBeAeygoec1hXHEChthVht2S8wvsFRXB1FHSsnWLi3cwQetsk1JsUq8SJCW4dzqDmVgenonRMxcw4wxm3oHrX3oVSmMM

2016-Sep-19 17:42:52.158224 Error: failed to load wallet: basic_string::_M_replace_aux

2016-Sep-19 17:42:52.183977 Error: You may want to remove the file "walletissue" and try again

2016-Sep-19 17:42:52.184036 ERROR /DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:1432 failed to open account

2016-Sep-19 17:42:52.184053 ERROR /DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:3928 Failed to initialize wallet

The issue is reproducible on my end, so I've created a test wallet that reproduces the error and can be inspected. Wallet password is the same as the wallet name: "walletissue"

wallet files: https://github.com/nthterm/monero_test_wallet


# Discussion History
## moneroexamples | 2016-09-20T06:02:37+00:00
I guess format changed. You can remove the cache file as suggested by the message, and new one should be generated after refresh. Have backup before trying off course:-)


## nthterm | 2016-09-20T16:21:41+00:00
Removing the cache file as suggested and refreshing fixes the issue.


## moneromooo-monero | 2016-09-20T16:21:50+00:00
With boost versions are 0.9.4 and 0.10.0 using ? ldd bitmonerod will tell you.


## nthterm | 2016-09-20T16:23:07+00:00
Will confirm boost versions across 0.9.4 and 0.10.0 in approx 8 hours and update this post.


## moneromooo-monero | 2016-09-20T22:04:34+00:00
Could you also please post the output of: ldd simplewallet (the 0.9.4 version)


## nthterm | 2016-09-20T22:24:35+00:00
ldd simplewallet

linux-vdso.so.1 =>  (0x00007fff9b19e000)                                    

libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f294b4c8000)         

libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f294b1bf000)           

libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f294afa1000)

libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f294abd8000)

/lib64/ld-linux-x86-64.so.2 (0x0000564f0aa16000)


## nthterm | 2016-09-20T22:32:52+00:00
Boost version installed on my system:
Version: 1.58.0.1ubuntu1


## moneromooo-monero | 2016-09-21T07:33:00+00:00
What I found yesterday debugging this:
- I can't load the wallet cache you supplied with current code and boost 1.59
- the loading fails trying to read a string from boost serialization near startup
- if I built current code with boost 1.55, it gets past that, but finds an unexpected version
- the version is 14, which boost 1.60 and 1.61 write, while boost 1.55 writes 10

That kinda hints that the wallet was created with a mix of boost 1.55 and 1.60, which seems very strange. Unless the data read isn't really a version, but is read as one. I'll continue looking at this bug this evening.


## moneromooo-monero | 2016-09-21T17:16:13+00:00
I can open the wallet cache if (1) I build with boost 1.55, and (2) I take out the version check in boost.

When I then resave the wallet, it's saved with version 10 (which corresponds to boost 1.55, as expected).

So AFAICT, the wallet cache was saved with some kind of bastard mix of boost 1.55 and boost 1.60/1.61.


## nthterm | 2016-09-21T17:25:21+00:00
If i created the wallet using one version of Boost, and later refreshed and updated the cache after upgrading to a different Boost version, could that explain the bastardization?


## moneromooo-monero | 2016-09-21T17:36:18+00:00
No, since you used 0.9.4 binaries from getmonero.org, which are statically linked against boost, so updating boost will not have an effect on this. The wallet will be written with whatever boost version is linked with 0.9.4. Whatever it was originally created with does not matter.


## ghost | 2016-09-23T22:26:11+00:00
I've got almost the same message here.
I'm under GNU/Linux Debian. I'm upgrading from monero_0.9.4.0, just copied my wallet file and wallet.keys and wallet.address.txt from my previous monero version.

The log tells me:

```
2016-Sep-24 00:15:12.568117 Monero 'Wolfram Warptangent' (v0.10.0.0-release)
2016-Sep-24 00:15:12.568146 Setting log level = 0
2016-Sep-24 00:15:12.568157 default_log: ./monero-wallet-cli.log
2016-Sep-24 00:15:12.568175 Logging at log level 0 to /home/user/monero_10.0.0/./monero-wallet-cli.log
2016-Sep-24 00:15:12.568206 Loading wallet...
2016-Sep-24 00:15:12.583152 Loaded wallet keys file, with public address: 51P9SG4URLDFfzSxvUYUxTLftcR398DT5Mv0B4JLMRih3icqrjVJiY8Jr9YF1PAXN7UFBDx4vKq4s3ozUpH5rEAuEioytyKJ
2016-Sep-24 00:15:12.740045 ERROR /DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:3901 Wallet initialization failed: basic_string::_M_replace_aux
```

Let me know if you need more information.


## moneromooo-monero | 2016-09-24T06:36:31+00:00
Did you compile your own 0.9.4, or were you using the prebuilt one from getmonero.org ?


## nthterm | 2016-09-24T06:43:24+00:00
Prebuilt

Edit: just noticed you were asking chaica


## ghost | 2016-09-24T11:54:48+00:00
Prebuilt too


## ghost | 2016-09-27T08:55:22+00:00
Let me know if you need more information. I'm just stuck using monero because of this bug :(


## netmonk | 2016-09-27T09:15:06+00:00
Chaica, what are you doing here ? :+1: 
Sorry for the noise, but happy to see him in the Monero adventure. 


## moneromooo-monero | 2016-09-27T20:08:27+00:00
For now, I'm pretty sure that if you build with boost 1.55, and disable the version check in boost/archive/impl/basic_binary_iarchive.ipp like below, your wallet cache will load.

--- ./boost/archive/impl/basic_binary_iarchive.ipp      2016-09-27 21:07:19.088000000 +0100
+++ /tmp/basic_binary_iarchive.ipp      2016-09-27 21:07:09.972000000 +0100
@@ -137,5 +137,5 @@
-    if(BOOST_ARCHIVE_VERSION() < input_library_version)
-    if(0 && BOOST_ARCHIVE_VERSION() < input_library_version)
       boost::serialization::throw_exception(
           archive_exception(archive_exception::unsupported_version)
       );


## ghost | 2016-09-27T23:10:56+00:00
@moneromooo-monero ok it worked. I also had to change Boost version line 570 of CMakeLists.txt but after that it built successfully with boost 1.55, thanks for the lead.


## anal0g | 2016-10-13T07:21:41+00:00
@nthterm @moneromooo-monero 
Guys i am getting the exact same error "failed to load wallet: basic_string::_M_replace_aux" when importing keys generated in a Windows 10 0.10 wallet to an Ubuntu 16.04 0.10 prebuilt wallet. Can you please specify where this cache file is located so i can delete it?


## moneromooo-monero | 2016-10-18T15:07:35+00:00
Same place as the keys file.
I recommend just renaming it away, so you still have a copy, should you need it later.


## tsirolnik | 2017-01-10T16:02:56+00:00
Getting this error too, on Ubuntu x64 while logging into my wallet after putting my password in

```Logging at log level 0 to /home/monero/./monero-wallet-cli.log                  
Loaded wallet keys file, with public address: 
 Error: failed to load wallet: basic_string::_M_replace_aux             
 ERROR /DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:1191 failed to open account  
 ERROR /DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:3993 Failed to initialize wallet
```

Edit:

Successfully logged in, monerod died straight after I did log in. (Wallet output at right, monerod on left)
```
 ...count 19637), but key does not exist
Use "help" command to see the list of available commands.                                                             │2017- [P2P9]Attempting to get output pubkey by global index (amount 90000, index 20357, count 20
**********************************************************************                                                │350), but key does not exist
Error: wallet failed to connect to daemon: http://localhost:18081. Daemon either is not started or wrong port was pass│ [P2P9]EXCEPTION: Attempting to get output pubkey by global index (amount 90000, index 2035
ed. Please make sure daemon is running or restart the wallet with the correct daemon address.                         │7, count 20350), but key does not exist
Error: wallet failed to connect to daemon: http://localhost:18081. Daemon either is not started or wrong port was pass│ [P2P9]Attempting to get output pubkey by global index (amount 100000, index 19639, count 1
ed. Please make sure daemon is running or restart the wallet with the correct daemon address.                         │9626), but key does not exist
Background refresh thread started                                                                                     │Killed
```

## moneromooo-monero | 2017-01-22T11:52:45+00:00
The "not found" is OK in some cases, so it doesn't mean something is wrong, per se.
The "Killed" is likely the OOM killer shooting monerod, and is almost certainly unrelated.

## moneromooo-monero | 2017-08-07T17:30:34+00:00
Fixed with the switch to portable boost format.

+resolved

# Action History
- Created by: nthterm | 2016-09-20T00:57:47+00:00
- Closed at: 2017-08-07T19:00:23+00:00
