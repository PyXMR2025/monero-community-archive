---
title: GUI v0.12 unable to connect to remote / local daemon (error std::bad_cast)
source_url: https://github.com/monero-project/monero-gui/issues/1261
author: dEBRUYNE-1
assignees: []
labels:
- bug
- resolved
created_at: '2018-04-04T15:20:55+00:00'
updated_at: '2018-07-02T20:06:43+00:00'
type: issue
status: closed
closed_at: '2018-06-16T21:18:21+00:00'
---

# Original Description
Getting a few reports of people unable to connect to their own (local) node or remote node after upgrading to v0.12.0.0. Logs:

**Case 1:**

https://paste.fedoraproject.org/paste/QKowduN71M9OMENPNHX2Vg

https://paste.fedoraproject.org/paste/W3HZGq7O9~TTIfw3SSKJew

Reddit conversation: https://www.reddit.com/r/Monero/comments/89nn2p/monero_gui_v01200_lithium_luna_released/dws770b/

------------

**Case 2:**

https://paste.fedoraproject.org/paste/dwXoiPEYE82lO5g7FB793Q

https://paste.fedoraproject.org/paste/pj3gZVLxvpcE5VWAvDsIXA

Reddit conversation: https://www.reddit.com/r/Monero/comments/89nn2p/monero_gui_v01200_lithium_luna_released/dwsh4fc/

------------

EDIT: Three more Linux users affected [here](https://www.reddit.com/r/Monero/comments/89nofd/monero_gui_01200_lithium_luna_megathread_download/dwta3ue/). The issue *seems* specific to Linux.

EDIT2: For anyone incurring this issue: As last resort you can always run GUI v0.11 with daemon (`monerod`) v0.12. Please see instructions below for using v0.11 and being sufficiently prepared for the upcoming scheduled network upgrade:

    <dEBRUYNE> You mean v0.11?
    <dEBRUYNE> If you're using a local node -> replace monerod v0.11 w/ monerod v0.12
    <dEBRUYNE> remote node, just open v0.11 and you should be able to use it past the fork
    <dEBRUYNE> However, the wallet cache may be incompatible, because (afaik) it's only forward compatible
    <dEBRUYNE> So if you incur an issue opening the wallet, use -> <dEBRUYNE> Go to your wallet directory (Documents\Monero\<wallet-name> on Windows | ~/Monero/<wallet-name>) and rename <wallet-name> to <wallet-name>-old

After block `1546000` you should also ensure that your transaction uses ring size 7, otherwise it will be rejected by the network. 

EDIT3: Better overview of workarounds:

https://monero.stackexchange.com/questions/7999/linux-gui-v0-12-does-not-connect-to-local-or-remote-node-stdbad-cast-error

**EDIT4: GUI v0.12.2.0, which includes a fix for this particular issue, has been released:**

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

# Discussion History
## dEBRUYNE-1 | 2018-04-04T15:21:03+00:00
+bug

## badfiles | 2018-04-04T20:53:33+00:00
I run the daemon in my lan, the cli version successfully connects and syncs wallet with the blockchain.
The gui version does nothing when I push 'connect', nothing in logs, status disconnected. WTF?

## dEBRUYNE-1 | 2018-04-04T22:35:30+00:00
@badfiles: Which operating system are you using?

## memorie62 | 2018-04-05T01:00:47+00:00
same problem on Win64.  daemon fails.  log shows

2018-04-05 00:33:03.194	8536	WARN 	net.http	src/wallet/wallet_errors.h:794	C:/msys64/home/vagrant/slave/monero-gui-win64/build/monero/src/wallet/wallet2.cpp:5610:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = gettransactions

the local file does not exist.  Also, monerod.exe is not included in the Win64 download.


## stevesbrain | 2018-04-05T01:27:32+00:00
No issue here; running Arch linux version, connecting to version 0.12.0.0 node also running on Arch Linux.

## medusadigital | 2018-04-05T08:12:12+00:00
@memorie62 monerod.exe is definetely included, make sure no anti virus software removed it while unpacking

## CaptainPlanet77 | 2018-04-05T09:45:58+00:00
I'm also affected. Running Xubuntu 16.04.

## badfiles | 2018-04-05T10:25:25+00:00
Ubuntu 17.10
No connection attempts on the pool side, nothing in client logs.

## mbay1971 | 2018-04-05T11:38:22+00:00
same on Ubuntu 16.04.4 LTS

## dEBRUYNE-1 | 2018-04-05T11:51:05+00:00
@CaptainPlanet77, @badfiles, @mbay1971: As last resort you can always run GUI v0.11 with daemon (`monerod`) v0.12. Please see instructions below for using v0.11 and being sufficiently prepared for the upcoming scheduled network upgrade:

    <dEBRUYNE> You mean v0.11?
    <dEBRUYNE> If you're using a local node -> replace monerod v0.11 w/ monerod v0.12
    <dEBRUYNE> remote node, just open v0.11 and you should be able to use it past the fork
    <dEBRUYNE> However, the wallet cache may be incompatible, because (afaik) it's only forward compatible
    <dEBRUYNE> So if you incur an issue opening the wallet, use -> <dEBRUYNE> Go to your wallet directory (Documents\Monero\<wallet-name> on Windows | ~/Monero/<wallet-name>) and rename <wallet-name> to <wallet-name>-old

After block `1546000` you should also ensure that your transaction uses ring size 7, otherwise it will be rejected by the network. 

## badfiles | 2018-04-05T11:59:14+00:00
cli 0.12 works fine. and I don't need local daemon, I already have a running 0.12 daemon on another machine.

## M5M400 | 2018-04-05T16:03:04+00:00
same here. Ubuntu 17.10, v0.12 release binaries.

```2018-04-05 15:42:25.591	    7fa7dbfff700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:5610	!r. THROW EXCEPTION: error::no_connection_to_daemon
2018-04-05 15:42:25.591	    7fa7dbfff700	WARN 	net.http	src/wallet/wallet_errors.h:794	/home/vagrant/slave/monero-gui-ubuntu-amd64/build/monero/src/wallet/wallet2.cpp:5610:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = gettransactions
2018-04-05 15:42:25.591	    7fa7dbfff700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:3827	Failed to save rings, will try again next time
2018-04-05 15:42:25.593	    7fa7f9772840	ERROR	default	src/wallet/api/utils.cpp:46	error: std::bad_cast
2018-04-05 15:42:49.498	    7fa7f9772840	ERROR	default	src/wallet/api/utils.cpp:46	error: std::bad_cast
```
Same behavior for starting daemon in GUI or separately and for remote daemon.


## erols | 2018-04-05T19:42:55+00:00
Same here on Ubuntu 17.10.

I noticed that I couldn't set Wallet Mode to Local Node in the gui

![screenshot from 2018-04-05 21-33-35](https://user-images.githubusercontent.com/658656/38388035-46eae54c-391a-11e8-9446-f52b37d8555a.png)


## dEBRUYNE-1 | 2018-04-05T19:46:59+00:00
@erols - If the `Local Node` button is grey it means that the wallet mode is set to local node. 

## erols | 2018-04-05T21:24:20+00:00
@dEBRUYNE-1 thanks. 

## ghost | 2018-04-07T02:34:57+00:00
Unable to connect to daemon using monero-gui-v0.12.0.0 on Mint 18 confirmed

## notgiven688 | 2018-04-07T18:03:59+00:00
Same here. Ubuntu 17.10.

## gypzie | 2018-04-07T18:37:25+00:00
@badfiles did you need to open and run the CLI on another machine to connect to daemon.  I see that CLI works, it is also working for me.  Were you able to use this to make the GUI work?

## badfiles | 2018-04-07T21:50:19+00:00
CLI from GUI package syncs well with my remote daemon.
GUI version does not connect and also does not exit properly.
I am quite surprised you guys rolling out a release that does not connect and does not quit under most famous Linux distro. 


## dEBRUYNE-1 | 2018-04-08T09:54:53+00:00
>I am quite surprised you guys rolling out a release that does not connect and does not quit under most famous Linux distro.

None of us did incur this bug whilst testing. Frankly, we were quite surprised too this bug was present. 

For anyone that is affected, could you please test the buildbot binary from here?

https://build.getmonero.org/builders/monero-gui-ubuntu-amd64/builds/105

It *should* include a fix for this particular issue. 

## notgiven688 | 2018-04-08T10:03:23+00:00
@dEBRUYNE-1 buildbot binary also does not work.

## dEBRUYNE-1 | 2018-04-08T10:41:39+00:00
@notgiven688 - Same error in the log? 

## notgiven688 | 2018-04-08T10:45:47+00:00
I only get this error:
ERROR	default	src/wallet/api/utils.cpp:46	error: std::bad_cast


## badfiles | 2018-04-08T10:46:35+00:00
```
2018-04-08 10:43:36.934	    7f5af5d76840	ERROR	default	src/wallet/api/utils.cpp:46	error: std::bad_cast
2018-04-08 10:44:01.643	    7f5af5d76840	ERROR	default	src/wallet/api/utils.cpp:46	error: std::bad_cast
```

## dEBRUYNE-1 | 2018-04-08T11:17:05+00:00
@notgiven688 & @badfiles - are you using a local node or a remote node? 

## badfiles | 2018-04-08T11:24:20+00:00
remote node. I have no space for the whole blockchain on my laptop.

## notgiven688 | 2018-04-08T11:49:07+00:00
@dEBRUYNE-1 local

## vitalisator | 2018-04-08T16:46:38+00:00
@dEBRUYNE-1, same issue with the fix on Linux Mint x64
2018-04-08 16:42:56.522     7f70e8e447c0        ERROR   default src/wallet/api/utils.cpp:46     error: std::bad_cast

## vitalisator | 2018-04-08T17:15:19+00:00
@dEBRUYNE-1 trying to catch some debugging infos, maybe that helps (replaced my address with xxx)
Maybe we could see more with compiled debug infos.

gdb ./monero-wallet-gui 
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./monero-wallet-gui...(no debugging symbols found)...done.
(gdb) catch throw
Haltepunkt 1 (throw)
(gdb) run
Starting program: /home/me/Downloads/build/release/bin/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff0ffb700 (LWP 14610)]
app startd
[New Thread 0x7fffebfff700 (LWP 14611)]
available width:  1920
available height:  1048
devicePixelRatio:  1
screen height:  1920
screen width:  1080
screen logical dpi:  96.1263
screen Physical dpi:  141.951
screen calculated ratio:  1.10899
[New Thread 0x7fffeaffe700 (LWP 14612)]
[Thread 0x7fffeaffe700 (LWP 14612) exited]
[New Thread 0x7fffeaffe700 (LWP 14613)]
[New Thread 0x7fffe3fff700 (LWP 14614)]
qml: check next false
qml: Checking seed
qml: check next false
qml: Checking seed
qml: check next false
qml: check next false
libpng warning: iCCP: known incorrect sRGB profile
[New Thread 0x7fffe35fe700 (LWP 14615)]
libpng warning: iCCP: known incorrect sRGB profile
qml: transfer page loaded
qml: PrivacyLevel changed:0
qml: mixin count: 6
qml: qrScannerEnabled disabled
qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:241:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[New Thread 0x7fffe2d51700 (LWP 14616)]
Checking for updates
[New Thread 0x7fffe2550700 (LWP 14617)]
[New Thread 0x7fffe1d4f700 (LWP 14618)]
[New Thread 0x7fffe154e700 (LWP 14619)]
[New Thread 0x7fffe0d4d700 (LWP 14620)]
qml: languages availible:  29
[Thread 0x7fffe1d4f700 (LWP 14618) exited]
[Thread 0x7fffe2550700 (LWP 14617) exited]
[Thread 0x7fffe154e700 (LWP 14619) exited]
Checking for updates - done
[Thread 0x7fffe0d4d700 (LWP 14620) exited]
qml: initializing..
setLanguage   "de"
setLanguage: loading translation file 'monero-core_de' from '/home/me/Downloads/build/release/bin/translations
setLanguage: translation for language 'de' loaded successfully
qml: transfer page loaded
qml: PrivacyLevel changed:0
qml: mixin count: 6
qml: opening wallet at:  /home/me/Monero/wallets/wallet/wallet.keys , network type:  mainnet
Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type): opening wallet at /home/me/Monero/wallets/wallet/wallet.keys, nettype = 0 
[New Thread 0x7fffe0d4d700 (LWP 14628)]
2018-04-08 17:03:04.669     7fffe2d51700        WARN    wallet.wallet2  src/wallet/wallet2.cpp:3742     Loaded wallet keys file, with public address: xxx
[Switching to Thread 0x7fffe2d51700 (LWP 14616)]

Thread 8 "Thread (pooled)" hit Catchpoint 1 (exception thrown), 0x000055555735a6ed in __cxa_throw ()
(gdb) next
Single stepping until exit from function __cxa_throw,
which has no line number information.
2018-04-08 17:04:07.551     7fffe2d51700        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:5634     !r. THROW EXCEPTION: error::no_connection_to_daemon
2018-04-08 17:04:07.552     7fffe2d51700        WARN    net.http        src/wallet/wallet_errors.h:794  /home/vagrant/slave/monero-gui-ubuntu-amd64/build/monero/src/wallet/wallet2.cpp:5634:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = gettransactions

Thread 8 "Thread (pooled)" hit Catchpoint 1 (exception thrown), 0x000055555735a6ed in __cxa_throw ()
(gdb) next
Single stepping until exit from function __cxa_throw,
which has no line number information.
2018-04-08 17:04:34.923     7fffe2d51700        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:3851     Failed to save rings, will try again next time
Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type): opened wallet: xxx, status: 0
AddressBook
getAll
Subaddress
getAll
qml: check next false
qml: >>> wallet opened: Wallet(0x7fffd47d2310)
qml: Recovering from seed:  false
qml: restore Height 0
[Switching to Thread 0x7ffff7fb67c0 (LWP 14603)]

Thread 1 "monero-wallet-g" hit Catchpoint 1 (exception thrown), 0x000055555735a6ed in __cxa_throw ()
(gdb) next
Single stepping until exit from function __cxa_throw,
which has no line number information.
[Thread 0x7fffe2d51700 (LWP 14616) exited]
2018-04-08 17:05:06.457     7ffff7fb67c0        ERROR   default src/wallet/api/utils.cpp:46     error: std::bad_cast
qml: initializing with daemon address:  localhost:18081
"initAsync: localhost:18081"
[New Thread 0x7fffe2d51700 (LWP 14677)]
init non async


## moneromooo-monero | 2018-04-08T18:56:00+00:00
Please post the output of "bt" when you're in gdb at that point, but before the call to next.

## vitalisator | 2018-04-08T19:03:41+00:00
@moneromooo-monero, because the catched tree times here the full output:

gdb ./monero-wallet-gui 
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./monero-wallet-gui...(no debugging symbols found)...done.
(gdb) catch throw
Haltepunkt 1 (throw)
(gdb) run
Starting program: /home/me/Downloads/build/release/bin/monero-wallet-gui 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff0ffb700 (LWP 18732)]
app startd
[New Thread 0x7fffebfff700 (LWP 18733)]
available width:  1920
available height:  1048
devicePixelRatio:  1
screen height:  1920
screen width:  1080
screen logical dpi:  96.1263
screen Physical dpi:  141.951
screen calculated ratio:  1.10899
[New Thread 0x7fffeaffe700 (LWP 18734)]
[Thread 0x7fffeaffe700 (LWP 18734) exited]
[New Thread 0x7fffeaffe700 (LWP 18735)]
[New Thread 0x7fffe3fff700 (LWP 18736)]
qml: check next false
qml: Checking seed
qml: check next false
qml: Checking seed
qml: check next false
qml: check next false
libpng warning: iCCP: known incorrect sRGB profile
[New Thread 0x7fffe35fe700 (LWP 18737)]
libpng warning: iCCP: known incorrect sRGB profile
qml: transfer page loaded
qml: PrivacyLevel changed:0
qml: mixin count: 6
qml: qrScannerEnabled disabled
qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:241:9: QML ContentItem: Binding loop detected for property "implicitWidth"
[New Thread 0x7fffe2d51700 (LWP 18738)]
Checking for updates
[New Thread 0x7fffe2550700 (LWP 18739)]
[New Thread 0x7fffe1d4f700 (LWP 18740)]
[New Thread 0x7fffe154e700 (LWP 18741)]
[New Thread 0x7fffe0d4d700 (LWP 18742)]
[Thread 0x7fffe154e700 (LWP 18741) exited]
[Thread 0x7fffe1d4f700 (LWP 18740) exited]
[Thread 0x7fffe0d4d700 (LWP 18742) exited]
[Thread 0x7fffe2550700 (LWP 18739) exited]
qml: languages availible:  29
Checking for updates - done
qml: initializing..
setLanguage   "de"
setLanguage: loading translation file 'monero-core_de' from '/home/me/Downloads/build/release/bin/translations
setLanguage: translation for language 'de' loaded successfully
qml: transfer page loaded
qml: PrivacyLevel changed:0
qml: mixin count: 6
qml: opening wallet at:  /home/me/Monero/wallets/wallet/wallet.keys , network type:  mainnet
Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type): opening wallet at /home/me/Monero/wallets/wallet/wallet.keys, nettype = 0 
[New Thread 0x7fffe0d4d700 (LWP 18753)]
2018-04-08 18:58:47.809     7fffe2d51700        WARN    wallet.wallet2  src/wallet/wallet2.cpp:3742     Loaded wallet keys file, with public address: xxx
[Switching to Thread 0x7fffe2d51700 (LWP 18738)]

Thread 8 "Thread (pooled)" hit Catchpoint 1 (exception thrown), 0x000055555735a6ed in __cxa_throw ()
(gdb) bt
#0  0x000055555735a6ed in __cxa_throw ()
#1  0x00005555558c2c10 in void boost::throw_exception<boost::system::system_error>(boost::system::system_error const&) ()
#2  0x00005555558de5b3 in boost::asio::detail::do_throw_error(boost::system::error_code const&, char const*) ()
#3  0x00005555558edba3 in epee::net_utils::blocked_mode_client::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::chrono::duration<long, std::ratio<1l, 1000l> >, bool, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#4  0x000055555591f83f in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::invoke(boost::basic_string_ref<char, std::char_traits<char> >, boost::basic_string_ref<char, std::char_traits<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::chrono::duration<long, std::ratio<1l, 1000l> >, epee::net_utils::http::http_response_info const**, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > const&) ()
#5  0x0000555555a6a674 in bool epee::net_utils::invoke_http_json<cryptonote::COMMAND_RPC_GET_TRANSACTIONS::request, cryptonote::COMMAND_RPC_GET_TRANSACTIONS::response, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client> >(boost::basic_string_ref<char, std::char_traits<char> >, cryptonote::COMMAND_RPC_GET_TRANSACTIONS::request const&, cryptonote::COMMAND_RPC_GET_TRANSACTIONS::response&, epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>&, std::chrono::duration<long, std::ratio<1l, 1000l> >, boost::basic_string_ref<char, std::char_traits<char> >) ()
#6  0x00005555559689a3 in tools::wallet2::find_and_save_rings(bool) ()
#7  0x00005555559b4262 in tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&) ()
#8  0x00005555558ad2fa in Monero::WalletImpl::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#9  0x00005555558d3099 in Monero::WalletManagerImpl::openWallet(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, Monero::NetworkType) ()
#10 0x000055555586ebb9 in WalletManager::openWallet(QString const&, QString const&, NetworkType::Type) ()
#11 0x0000555555873380 in QtConcurrent::RunFunctionTask<Wallet*>::run() ()
#12 0x00005555570866fb in QThreadPoolThread::run() ()
#13 0x000055555708a115 in QThreadPrivate::start(void*) ()
#14 0x00007ffff62986ba in start_thread (arg=0x7fffe2d51700) at pthread_create.c:333
#15 0x00007ffff5cc541d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
(gdb) next
Single stepping until exit from function __cxa_throw,
which has no line number information.
2018-04-08 18:59:44.479     7fffe2d51700        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:5634     !r. THROW EXCEPTION: error::no_connection_to_daemon
2018-04-08 18:59:44.479     7fffe2d51700        WARN    net.http        src/wallet/wallet_errors.h:794  /home/vagrant/slave/monero-gui-ubuntu-amd64/build/monero/src/wallet/wallet2.cpp:5634:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = gettransactions

Thread 8 "Thread (pooled)" hit Catchpoint 1 (exception thrown), 0x000055555735a6ed in __cxa_throw ()
(gdb) bt
#0  0x000055555735a6ed in __cxa_throw ()
#1  0x0000555555a0f497 in void tools::error::throw_wallet_ex<tools::error::no_connection_to_daemon, char [16]>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, char const (&) [16]) ()
#2  0x0000555555968aef in tools::wallet2::find_and_save_rings(bool) ()
#3  0x00005555559b4262 in tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&) ()
#4  0x00005555558ad2fa in Monero::WalletImpl::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#5  0x00005555558d3099 in Monero::WalletManagerImpl::openWallet(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, Monero::NetworkType) ()
#6  0x000055555586ebb9 in WalletManager::openWallet(QString const&, QString const&, NetworkType::Type) ()
#7  0x0000555555873380 in QtConcurrent::RunFunctionTask<Wallet*>::run() ()
#8  0x00005555570866fb in QThreadPoolThread::run() ()
#9  0x000055555708a115 in QThreadPrivate::start(void*) ()
#10 0x00007ffff62986ba in start_thread (arg=0x7fffe2d51700) at pthread_create.c:333
#11 0x00007ffff5cc541d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
(gdb) next
Single stepping until exit from function __cxa_throw,
which has no line number information.
2018-04-08 19:00:03.483     7fffe2d51700        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:3851     Failed to save rings, will try again next time
Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type): opened wallet: xxx, status: 0
AddressBook
getAll
Subaddress
getAll
qml: check next false
qml: >>> wallet opened: Wallet(0x7fffd47d2310)
qml: Recovering from seed:  false
qml: restore Height 0
[Switching to Thread 0x7ffff7fb67c0 (LWP 18728)]

Thread 1 "monero-wallet-g" hit Catchpoint 1 (exception thrown), 0x000055555735a6ed in __cxa_throw ()
(gdb) bt
#0  0x000055555735a6ed in __cxa_throw ()
#1  0x0000555557364322 in __cxa_bad_cast ()
#2  0x00005555573a926c in std::__cxx11::collate<char> const& std::use_facet<std::__cxx11::collate<char> >(std::locale const&) ()
#3  0x0000555555cc8669 in boost::re_detail::cpp_regex_traits_base<char>::imbue(std::locale const&) ()
#4  0x0000555555cdd1a7 in boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::do_assign(char const*, char const*, unsigned int) ()
#5  0x00005555558e11a7 in boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::basic_regex(char const*, unsigned int) ()
#6  0x000055555591b848 in epee::net_utils::parse_url(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, epee::net_utils::http::url_content&) ()
#7  0x0000555555b7e789 in tools::is_local_address(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#8  0x0000555555929741 in Monero::Utils::isAddressLocal(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#9  0x0000555555870e21 in WalletManager::isDaemonLocal(QString const&) const ()
#10 0x00005555558a0a46 in WalletManager::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) ()
#11 0x00005555558a0f68 in WalletManager::qt_metacall(QMetaObject::Call, int, void**) ()
#12 0x0000555556d8c691 in QQmlObjectOrGadget::metacall(QMetaObject::Call, int, void**) const ()
#13 0x0000555556d25c1c in CallMethod(QQmlObjectOrGadget const&, int, int, int, int*, QV4::ExecutionEngine*, QV4::CallData*) [clone .constprop.159] ()
#14 0x0000555556d27746 in CallPrecise(QQmlObjectOrGadget const&, QQmlPropertyData const&, QV4::ExecutionEngine*, QV4::CallData*) [clone .constprop.157] ()
#15 0x0000555556d282bd in QV4::QObjectMethod::callInternal(QV4::CallData*) const ()
#16 0x0000555556d3e37a in QV4::Runtime::callProperty(QV4::ExecutionEngine*, int, QV4::CallData*) ()
#17 0x00007ffff7e0a4aa in ?? ()
#18 0x00007fffeb000498 in ?? ()
#19 0x0000555558767010 in ?? ()
#20 0x00007fffeb0004d8 in ?? ()
#21 0x0000555556d3b97e in QV4::Runtime::getProperty(QV4::ExecutionEngine*, QV4::Value const&, int) ()
#22 0x00007fffe932e230 in ?? ()
#23 0x0000000000000000 in ?? ()
(gdb) 


## sanderfoobar | 2018-04-08T19:09:41+00:00
Thanks @vitalisator

Some more gdb, tested against [this debug build](https://build.getmonero.org/builders/monero-gui-debug-ubuntu-amd64/builds/0) on Ubuntu 17 64bit (virtualbox vm from [here](https://www.osboxes.org/ubuntu/)) with debugging symbols.

```
[----------------------------------registers-----------------------------------]
RAX: 0x555558b75ce0 --> 0x5555586f12e8 --> 0x5555573e4720 (<_ZNSt8bad_castD2Ev>:        lea    rax,[rip+0x130cbb1]        # 0x5555586f12d8 <_ZTVSt8bad_cast>)
RBX: 0x555558b75ce0 --> 0x5555586f12e8 --> 0x5555573e4720 (<_ZNSt8bad_castD2Ev>:        lea    rax,[rip+0x130cbb1]        # 0x5555586f12d8 <_ZTVSt8bad_cast>)
RCX: 0x0
RDX: 0x5555573e4720 (<_ZNSt8bad_castD2Ev>:      lea    rax,[rip+0x130cbb1]        # 0x5555586f12d8 <_ZTVSt8bad_cast>)
RSI: 0x5555586f12c0 --> 0x5555586f0778 --> 0x5555573e33f0 (<_ZN10__cxxabiv120__si_class_type_infoD2Ev>: lea    rax,[rip+0x130d371]        # 0x5555586f0768 <_ZTVN10__cxxabiv120__si_class_type_infoE>)
RDI: 0x555558b75ce0 --> 0x5555586f12e8 --> 0x5555573e4720 (<_ZNSt8bad_castD2Ev>:        lea    rax,[rip+0x130cbb1]        # 0x5555586f12d8 <_ZTVSt8bad_cast>)
RBP: 0x5555586f12c0 --> 0x5555586f0778 --> 0x5555573e33f0 (<_ZN10__cxxabiv120__si_class_type_infoD2Ev>: lea    rax,[rip+0x130d371]        # 0x5555586f0768 <_ZTVN10__cxxabiv120__si_class_type_infoE>)
RSP: 0x7fffffffc740 --> 0x7fffffffc7c0 --> 0x555558764700 --> 0x1f
RIP: 0x5555573d9a3d (<__cxa_throw+13>:  nop)
R8 : 0x7ffff5f82b98 --> 0x7ffff5f82b88 --> 0x5555594963f0 --> 0x18
R9 : 0x5555586f1a98 --> 0x5555586f1460 --> 0x5555573e5730 (<_ZN10__cxxabiv117__class_type_infoD2Ev>:    lea    rax,[rip+0x130bd19]        # 0x5555586f1450 <_ZTVN10__cxxabiv117__class_type_infoE>)
R10: 0x555558b75c60 --> 0x0
R11: 0x5555587638f0 --> 0x5555586f3eb8 --> 0x55555741eb90 (<_ZNSt7codecvtIDic11__mbstate_tED2Ev>:       lea    rax,[rip+0x12d5261]        # 0x5555586f3df8 <_ZTVSt23__codecvt_abstract_baseIDic11__mbstate_tE>)
R12: 0x5555573e4720 (<_ZNSt8bad_castD2Ev>:      lea    rax,[rip+0x130cbb1]        # 0x5555586f12d8 <_ZTVSt8bad_cast>)
R13: 0x5555577b8afc --> 0x3c20746e756f6300 ('')
R14: 0x100000
R15: 0x7fffffffc7f0 --> 0x555558764700 --> 0x1f
EFLAGS: 0x206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5555573d9a36 <__cxa_throw+6>:      mov    rbp,rsi
   0x5555573d9a39 <__cxa_throw+9>:      push   rbx
   0x5555573d9a3a <__cxa_throw+10>:     mov    rbx,rdi
=> 0x5555573d9a3d <__cxa_throw+13>:     nop
   0x5555573d9a3e <__cxa_throw+14>:     call   0x5555573e54a0 <__cxa_get_globals>
   0x5555573d9a43 <__cxa_throw+19>:     add    DWORD PTR [rax+0x8],0x1
   0x5555573d9a47 <__cxa_throw+23>:     mov    DWORD PTR [rbx-0x80],0x1
   0x5555573d9a4e <__cxa_throw+30>:     sub    rbx,0x20
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffc740 --> 0x7fffffffc7c0 --> 0x555558764700 --> 0x1f
0008| 0x7fffffffc748 --> 0x7fffffffc7c0 --> 0x555558764700 --> 0x1f
0016| 0x7fffffffc750 --> 0x7fffffffc7d0 --> 0x555558764700 --> 0x1f
0024| 0x7fffffffc758 --> 0x5555573e3672 (nop    WORD PTR cs:[rax+rax*1+0x0])
0032| 0x7fffffffc760 --> 0x5555577b8afc --> 0x3c20746e756f6300 ('')
0040| 0x7fffffffc768 --> 0x55555742820c (nop    DWORD PTR [rax+0x0])
0048| 0x7fffffffc770 --> 0x7fffffffc7f0 --> 0x555558764700 --> 0x1f
0056| 0x7fffffffc778 --> 0x555555d44659 (<_ZN5boost9re_detail21cpp_regex_traits_baseIcE5imbueERKSt6locale+73>:  mov    QWORD PTR [rbx+0x18],rax)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Thread 1 "monero-wallet-g" hit Catchpoint 1 (exception thrown), 0x00005555573d9a3d in __cxa_throw ()

gdb-peda$ bt
#0  0x00005555573d9a3d in __cxa_throw ()
#1  0x00005555573e3672 in __cxa_bad_cast ()
#2  0x000055555742820c in std::__cxx11::collate<char> const& std::use_facet<std::__cxx11::collate<char> >(std::locale const&) ()
#3  0x0000555555d44659 in boost::re_detail::cpp_regex_traits_base<char>::imbue(std::locale const&) ()
#4  0x0000555555d59197 in boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::do_assign(char const*, char const*, unsigned int) ()
#5  0x00005555558de248 in boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::assign (f=<optimized out>, p2=<optimized out>, p1=<optimized out>,
    this=0x55555871ce10 <epee::net_utils::parse_url(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, epee::net_utils::http::url_content&)::rexp_match_uri>) at /usr/include/boost/regex/v4/basic_regex.hpp:380
#6  boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::assign (f=<optimized out>, p=<optimized out>,
    this=0x55555871ce10 <epee::net_utils::parse_url(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, epee::net_utils::http::url_content&)::rexp_match_uri>) at /usr/include/boost/regex/v4/basic_regex.hpp:365
#7  boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::basic_regex (
    this=0x55555871ce10 <epee::net_utils::parse_url(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, epee::net_utils::http::url_content&)::rexp_match_uri>, p=<optimized out>, f=<optimized out>)
    at /usr/include/boost/regex/v4/basic_regex.hpp:334
#8  0x0000555555925acf in epee::net_utils::parse_url (url_str="", content=...) at /home/vagrant/slave/monero-gui-debug-ubuntu-amd64/build/monero/contrib/epee/include/net/net_parse_helpers.h:138
#9  0x0000555555bb92b1 in tools::is_local_address (address="") at /home/vagrant/slave/monero-gui-debug-ubuntu-amd64/build/monero/src/common/util.cpp:620
#10 0x000055555592e919 in Monero::Utils::isAddressLocal (address=...) at /home/vagrant/slave/monero-gui-debug-ubuntu-amd64/build/monero/src/wallet/api/utils.cpp:44
#11 0x0000555555860673 in WalletManager::isDaemonLocal (this=0x5555588c5fa0, daemon_address=...) at ../src/libwalletqt/WalletManager.cpp:275
#12 0x000055555589a419 in WalletManager::qt_static_metacall (_o=0x5555588c5fa0, _c=QMetaObject::InvokeMetaMethod, _id=0x26, _a=0x7fffffffd2c0) at moc_WalletManager.cpp:390
#13 0x000055555589ae5f in WalletManager::qt_metacall (this=0x5555588c5fa0, _c=QMetaObject::InvokeMetaMethod, _id=0x26, _a=0x7fffffffd2c0) at moc_WalletManager.cpp:497
#14 0x0000555556e0c401 in QQmlObjectOrGadget::metacall(QMetaObject::Call, int, void**) const ()
#15 0x0000555556da598c in CallMethod(QQmlObjectOrGadget const&, int, int, int, int*, QV4::ExecutionEngine*, QV4::CallData*) [clone .constprop.159] ()
#16 0x0000555556da74b6 in CallPrecise(QQmlObjectOrGadget const&, QQmlPropertyData const&, QV4::ExecutionEngine*, QV4::CallData*) [clone .constprop.157] ()
#17 0x0000555556da802d in QV4::QObjectMethod::callInternal(QV4::CallData*) const ()
#18 0x0000555556dbe0ea in QV4::Runtime::callProperty(QV4::ExecutionEngine*, int, QV4::CallData*) ()
#19 0x00007fffee16df5a in ?? ()
#20 0x0000000000000000 in ?? ()
gdb-peda$ 
```

So it does:

`Monero::Utils::isAddressLocal -> tools::is_local_address -> epee::net_utils::parse_url -> boost::basic_regex -> boost::re_detail -> dies here`

Bug in boost?

```
root@osboxes:~# locale
LANG=en_US.UTF-8
LANGUAGE=
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=en_US.UTF-8
```

```
# ldd monero-wallet-gui
        linux-vdso.so.1 =>  (0x00007ffc9c7f9000)
        libpcsclite.so.1 => /lib/x86_64-linux-gnu/libpcsclite.so.1 (0x00007f921a19f000)
        libxcb-glx.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-glx.so.0 (0x00007f9219f86000)
        libX11-xcb.so.1 => /usr/lib/x86_64-linux-gnu/libX11-xcb.so.1 (0x00007f9219d84000)
        libxcb.so.1 => /usr/lib/x86_64-linux-gnu/libxcb.so.1 (0x00007f9219b62000)
        libfontconfig.so.1 => /usr/lib/x86_64-linux-gnu/libfontconfig.so.1 (0x00007f921991f000)
        libfreetype.so.6 => /usr/lib/x86_64-linux-gnu/libfreetype.so.6 (0x00007f9219670000)
        libX11.so.6 => /usr/lib/x86_64-linux-gnu/libX11.so.6 (0x00007f9219337000)
        libEGL.so.1 => /usr/lib/x86_64-linux-gnu/mesa-egl/libEGL.so.1 (0x00007f92190fe000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f9218efa000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f9218cf2000)
        libGL.so.1 => /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1 (0x00007f9218a80000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f9218860000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f9218557000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f9218190000)
        /lib64/ld-linux-x86-64.so.2 (0x000055b108ea3000)
        libXau.so.6 => /usr/lib/x86_64-linux-gnu/libXau.so.6 (0x00007f9217f8c000)
        libXdmcp.so.6 => /usr/lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007f9217d86000)
        libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007f9217b5c000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f921793e000)
        libpng16.so.16 => /usr/lib/x86_64-linux-gnu/libpng16.so.16 (0x00007f921770c000)
        libxcb-dri2.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-dri2.so.0 (0x00007f9217507000)
        libxcb-dri3.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-dri3.so.0 (0x00007f9217304000)
        libxcb-present.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-present.so.0 (0x00007f9217101000)
        libxcb-xfixes.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-xfixes.so.0 (0x00007f9216ef9000)
        libxcb-sync.so.1 => /usr/lib/x86_64-linux-gnu/libxcb-sync.so.1 (0x00007f9216cf0000)
        libxshmfence.so.1 => /usr/lib/x86_64-linux-gnu/libxshmfence.so.1 (0x00007f9216aed000)
        libwayland-client.so.0 => /usr/lib/x86_64-linux-gnu/libwayland-client.so.0 (0x00007f92168de000)
        libwayland-server.so.0 => /usr/lib/x86_64-linux-gnu/libwayland-server.so.0 (0x00007f92166cc000)
        libgbm.so.1 => /usr/lib/x86_64-linux-gnu/libgbm.so.1 (0x00007f92164bf000)
        libmirclient.so.9 => /usr/lib/x86_64-linux-gnu/libmirclient.so.9 (0x00007f9216217000)
        libdrm.so.2 => /usr/lib/x86_64-linux-gnu/libdrm.so.2 (0x00007f9216004000)
        libglapi.so.0 => /usr/lib/x86_64-linux-gnu/libglapi.so.0 (0x00007f9215dd5000)
        libXext.so.6 => /usr/lib/x86_64-linux-gnu/libXext.so.6 (0x00007f9215bc3000)
        libXdamage.so.1 => /usr/lib/x86_64-linux-gnu/libXdamage.so.1 (0x00007f92159c0000)
        libXfixes.so.3 => /usr/lib/x86_64-linux-gnu/libXfixes.so.3 (0x00007f92157ba000)
        libXxf86vm.so.1 => /usr/lib/x86_64-linux-gnu/libXxf86vm.so.1 (0x00007f92155b4000)
        libffi.so.6 => /usr/lib/x86_64-linux-gnu/libffi.so.6 (0x00007f92153aa000)
        libxkbcommon.so.0 => /usr/lib/x86_64-linux-gnu/libxkbcommon.so.0 (0x00007f921516a000)
        libmircommon.so.7 => /usr/lib/x86_64-linux-gnu/libmircommon.so.7 (0x00007f9214f23000)
        libmirprotobuf.so.3 => /usr/lib/x86_64-linux-gnu/libmirprotobuf.so.3 (0x00007f9214ca2000)
        libcapnp-0.5.3.so => /usr/lib/x86_64-linux-gnu/libcapnp-0.5.3.so (0x00007f9214a1d000)
        libmircore.so.1 => /usr/lib/x86_64-linux-gnu/libmircore.so.1 (0x00007f9214812000)
        libboost_system.so.1.62.0 => /usr/lib/x86_64-linux-gnu/libboost_system.so.1.62.0 (0x00007f921460e000)
        libprotobuf-lite.so.10 => /usr/lib/x86_64-linux-gnu/libprotobuf-lite.so.10 (0x00007f92143c0000)
        libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f9214038000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f9213e21000)
        libboost_filesystem.so.1.62.0 => /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.62.0 (0x00007f9213c06000)
        libkj-0.5.3.so => /usr/lib/x86_64-linux-gnu/libkj-0.5.3.so (0x00007f92139df000)
```

## stoffu | 2018-04-09T06:38:24+00:00
According to https://svn.boost.org/trac10/ticket/4671, it seems to be due to the compiler's bug:

> This is a problem with the locale you are using - for whatever reason it doesn't contain a `std::collate<char>` facet - as it's required to do so by the standard.

This issue can hopefully be fixed by upgrading the compiler to some newer version. FWIW the version of my compiler is `g++ (Ubuntu 5.4.0-6ubuntu1~16.04.9) 5.4.0 20160609`, and the binaries built with it don't exhibit this error.

Alternatively, a less desirable but easy workaround is to stop calling `tools::is_local_address()` and bring back the code removed in #1015.


## stoffu | 2018-04-09T08:58:29+00:00
#1298 

## joelstahre | 2018-04-09T20:39:33+00:00
Same issue for me.

## dEBRUYNE-1 | 2018-04-12T19:36:33+00:00
For anyone that is affected by the issue, please check whether this one works:

https://build.getmonero.org/builders/monero-gui-linux-qt57/builds/4

## vitalisator | 2018-04-12T19:58:24+00:00
@dEBRUYNE-1 , can you please include the qt in the build?
./start-gui.sh 
./monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Qml.so.5: version `Qt_5' not found (required by ./monero-wallet-gui)
./monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Quick.so.5: version `Qt_5' not found (required by ./monero-wallet-gui)
./monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Widgets.so.5: version `Qt_5' not found (required by ./monero-wallet-gui)
./monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Gui.so.5: version `Qt_5' not found (required by ./monero-wallet-gui)
./monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Core.so.5: version `Qt_5.7' not found (required by ./monero-wallet-gui)
./monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Core.so.5: version `Qt_5' not found (required by ./monero-wallet-gui)

## DamnTele | 2018-04-12T20:02:48+00:00
I was having this issue on Ubuntu 16.04 then I upgraded to the 18.04 beta and now I'm have an intermediate connection to the daemon that fails every couple of minutes and then reconnects.

When I run the build you linked I get this.
```
$ ./start-gui.sh 

This application failed to start because it could not find or load the Qt platform plugin "xcb"
in "".

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, xcb, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx.

Reinstalling the application may fix this problem.
./start-gui.sh: line 7: 18278 Aborted                 (core dumped) "$SCRIPT_DIR"/monero-wallet-gui
```

## ghost | 2018-04-12T20:07:46+00:00
Failed on MINT 18

## sanderfoobar | 2018-04-12T20:32:54+00:00
@eggsdontbounce Could you post the output of `./monero-wallet-gui`, using the build dEBRUYNE linked?

## sanderfoobar | 2018-04-12T20:38:01+00:00
@vitalisator `qtchooser -print-env` / `qmake -v` / `apt-cache madison qt5-default` (assuming you have `apt`)

## pazos | 2018-04-12T20:56:42+00:00
@DamnTele: what happens if you run the application with `./monero-wallet-gui -platform xcb`

## DamnTele | 2018-04-12T21:19:42+00:00
@pazos that got it running but i still have the intermediate connection issue, this is what it says in the console
```
Checking connection status
2018-04-12 21:11:01.709	    7f044c6adc40	ERROR	net.http	contrib/epee/include/net/http_client.h:456	Unexpected recv fail
2018-04-12 21:11:01.709	    7f044c6adc40	ERROR	WalletAPI	src/wallet/api/wallet.cpp:893	daemonBlockChainTargetHeight: possibly lost connection to daemon

```

## ghost | 2018-04-12T21:20:13+00:00
@skftn I deleted the package after it failed then reverted back to the cli version. Will have a better look at it later in the day

## dEBRUYNE-1 | 2018-04-12T21:56:17+00:00
@DamnTele - `Unexpected recv fail` usually means you already have a daemon (monerod) running. Could you check your process list? 

## grigio | 2018-04-12T22:27:17+00:00
@skftn 
```
bin ⟩ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 17.10
Release:	17.10
Codename:	artful
bin ⟩ qtchooser -print-env
QT_SELECT="default"
QTTOOLDIR="/usr/lib/x86_64-linux-gnu/qt4/bin"
QTLIBDIR="/usr/lib/x86_64-linux-gnu"
bin ⟩ qmake -v
qmake: could not exec '/usr/lib/x86_64-linux-gnu/qt4/bin/qmake': No such file or directory
bin ⟩ apt-cache madison qt5-default
qt5-default | 5.9.1+dfsg-10ubuntu1 | http://it.archive.ubuntu.com/ubuntu artful/universe amd64 Packages

```

```
bin ⟩ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 17.10
Release:	17.10
Codename:	artful
bin ⟩ qtchooser -print-env
QT_SELECT="default"
QTTOOLDIR="/usr/lib/x86_64-linux-gnu/qt4/bin"
QTLIBDIR="/usr/lib/x86_64-linux-gnu"
bin ⟩ qmake -v
qmake: could not exec '/usr/lib/x86_64-linux-gnu/qt4/bin/qmake': No such file or directory
bin ⟩ apt-cache madison qt5-default
qt5-default | 5.9.1+dfsg-10ubuntu1 | http://it.archive.ubuntu.com/ubuntu artful/universe amd64 Packages

```

## DamnTele | 2018-04-13T05:57:48+00:00
@dEBRUYNE-1 there's only one monerod running, the disconnecting seems to only happen when the daemon is still syncing, once it reaches 100% the gui stays connected.

also i noticed this in the daemon log 
```Height: 1549828/1549828 (100.0%) on mainnet, not mining, net hash 466.42 MH/s, v7, up to date, 0(out)+0(in) connections, uptime 0d 0h 0m 1s

Height: 1550066/1550066 (100.0%) on mainnet, not mining, net hash 445.83 MH/s, v7, up to date, 6(out)+4(in) connections, uptime 0d 0h 8m 11s

Height: 1550066/1550601 (99.9%) on mainnet, not mining, net hash 445.83 MH/s, v7, up to date, 5(out)+5(in) connections, uptime 0d 0h 8m 20s

Height: 1550066/1550601 (99.9%) on mainnet, not mining, net hash 445.83 MH/s, v7, up to date, 7(out)+3(in) connections, uptime 0d 0h 8m 49s

Height: 1550066/1550066 (100.0%) on mainnet, not mining, net hash 445.83 MH/s, v7, up to date, 8(out)+3(in) connections, uptime 0d 0h 10m 55s

Height: 1550074/1550659 (99.9%) on mainnet, not mining, net hash 446.58 MH/s, v7, up to date, 8(out)+4(in) connections, uptime 0d 0h 22m 34s

Height: 1550075/1550075 (100.0%) on mainnet, not mining, net hash 445.80 MH/s, v7, up to date, 8(out)+5(in) connections, uptime 0d 0h 29m 22s
```
the number of blocks keeps going up and down by about 600, is this normal?

## vitalisator | 2018-04-13T06:42:53+00:00
@skftn 
qtchooser -print-env ;qmake -v ; apt-cache madison qt5-default
QT_SELECT="default"
QTTOOLDIR="/usr/lib/x86_64-linux-gnu/qt4/bin"
QTLIBDIR="/usr/lib/x86_64-linux-gnu"
qmake: could not exec '/usr/lib/x86_64-linux-gnu/qt4/bin/qmake': No such file or directory
qt5-default | 5.5.1+dfsg-16ubuntu7.5 | http://mirror.netcologne.de/ubuntu xenial-updates/universe amd64 Packages
qt5-default | 5.5.1+dfsg-16ubuntu7 | http://mirror.netcologne.de/ubuntu xenial/universe amd64 Packages

lsb_release -a
LSB Version:    core-9.20160110ubuntu0.2-amd64:core-9.20160110ubuntu0.2-noarch:security-9.20160110ubuntu0.2-amd64:security-9.20160110ubuntu0.2-noarch
Distributor ID: LinuxMint
Description:    Linux Mint 18.3 Sylvia
Release:        18.3
Codename:       sylvia

## el00ruobuob | 2018-04-13T08:58:32+00:00
@skftn same as vitalisator here: 

```
Téléchargements/build/release/bin/start-gui.sh 
Téléchargements/build/release/bin/monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Qml.so.5: version `Qt_5' not found (required by Téléchargements/build/release/bin/monero-wallet-gui)
Téléchargements/build/release/bin/monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Quick.so.5: version `Qt_5' not found (required by Téléchargements/build/release/bin/monero-wallet-gui)
Téléchargements/build/release/bin/monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Widgets.so.5: version `Qt_5' not found (required by Téléchargements/build/release/bin/monero-wallet-gui)
Téléchargements/build/release/bin/monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Gui.so.5: version `Qt_5' not found (required by Téléchargements/build/release/bin/monero-wallet-gui)
Téléchargements/build/release/bin/monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Core.so.5: version `Qt_5.7' not found (required by Téléchargements/build/release/bin/monero-wallet-gui)
Téléchargements/build/release/bin/monero-wallet-gui: /usr/lib/x86_64-linux-gnu/libQt5Core.so.5: version `Qt_5' not found (required by Téléchargements/build/release/bin/monero-wallet-gui)
```

```
qtchooser -print-env ;qmake -v ; apt-cache madison qt5-default
QT_SELECT="default"
QTTOOLDIR="/usr/lib/x86_64-linux-gnu/qt5/bin"
QTLIBDIR="/usr/lib/x86_64-linux-gnu"
QMake version 3.0
Using Qt version 5.5.1 in /usr/lib/x86_64-linux-gnu
qt5-default | 5.5.1+dfsg-16ubuntu7.5 | http://fr.archive.ubuntu.com/ubuntu xenial-updates/universe amd64 Packages
qt5-default | 5.5.1+dfsg-16ubuntu7 | http://fr.archive.ubuntu.com/ubuntu xenial/universe amd64 Packages
```

## el00ruobuob | 2018-04-13T09:25:54+00:00
@DamnTele @dEBRUYNE-1 Same behavior here: 

```
2018-04-13 09:12:54.142	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[85.114.17.187:50836 INC] Sync data returned a new top block candidate: 1547734 -> 1550169 [Your node is 2435 blocks (3 days) behind] 
SYNCHRONIZATION started
2018-04-13 09:14:26.092	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[217.25.221.123:55642 INC] Sync data returned a new top block candidate: 1547734 -> 1550169 [Your node is 2435 blocks (3 days) behind] 
SYNCHRONIZATION started
2018-04-13 09:15:14.911	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[67.5.251.222:18080 OUT] Sync data returned a new top block candidate: 1547734 -> 1550458 [Your node is 2724 blocks (3 days) behind] 
SYNCHRONIZATION started
2018-04-13 09:15:37.406	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[77.41.132.51:44136 INC] Sync data returned a new top block candidate: 1547734 -> 1550820 [Your node is 3086 blocks (4 days) behind] 
SYNCHRONIZATION started
```

## dEBRUYNE-1 | 2018-04-13T16:04:29+00:00
@el00ruobuob - Your daemon is probably connected to a bad peer (i.e. a peer on the wrong (alternative) chain). The daemon should eventually ban this bad peer. In addition, a restart typically fixes these kind of issues. 

## tonighx | 2018-04-15T22:07:03+00:00
also affects Linux Mint 18.3

## milargos | 2018-04-16T06:00:27+00:00
As @stoffu said.
I can also confirm that compiling from source works fine for me.
```
$ lsb_release -a
Description:	Ubuntu 16.04.4 LTS

$ gcc --version
gcc (Ubuntu 5.4.1-2ubuntu1~16.04) 5.4.1 20160904

$ g++ --version
g++ (Ubuntu 5.4.1-2ubuntu1~16.04) 5.4.1 20160904

$ qmake --version
QMake version 3.1
Using Qt version 5.10.1 in /usr/share/qt5-prop/5.10.1/gcc_64/lib
```

## citkane | 2018-04-16T12:55:28+00:00
I can also confirm that I was affected by the subject of this issue (from distributeable) and that compiling from source works for me.
```
$ lsb_release -a
Description:	Ubuntu 17.10

$ gcc --version
gcc (Ubuntu 7.2.0-8ubuntu3.2) 7.2.0

$ g++ --version
g++ (Ubuntu 7.2.0-8ubuntu3.2) 7.2.0

$ qmake --version
QMake version 3.1
Using Qt version 5.9.1 in /usr/lib/x86_64-linux-gnu
```

To note also, compile instructions for monero-gui (ubuntu > 16.04) are incorrect. `libqt5qml-graphicaleffects` is no longer an ubuntu package. To compile and run, the following packages are required:

```
qml-module-qtgraphicaleffects
qml-module-qt-labs-folderlistmodel
qml-module-qtquick-controls2
```

## Mafaka8 | 2018-04-18T15:21:17+00:00
When I try to build from source I get the following error: 

/usr/bin/ld: cannot find -lwallet_merged
/usr/bin/ld: cannot find -lepee
/usr/bin/ld: cannot find -leasylogging
/usr/bin/ld: cannot find -llmdb
collect2: error: ld returned 1 exit status
Makefile:379: recipe for target 'release/bin/monero-wallet-gui' failed
make: *** [release/bin/monero-wallet-gui] Error 1


## stoffu | 2018-04-18T23:04:11+00:00
@Mafaka8 
These error messages mean that something wrong happened while building the Monero libraries which the GUI depends on. Try these commands and check for any error messages:

```
make -C monero/build/release/external install
make -C monero/build/release/contrib install
make -C monero/build/release/src/wallet install
```


## pedroaugustomontes | 2018-04-18T23:54:48+00:00
Hello guys, since I updated my wallet to 0.12 gui I can't start daemon anymore, I'm a beginner Ubuntu 16.04 user, someone can help me?

```
qml: initializing with daemon address:  localhost:18081
"initAsync: localhost:18081"
init non async
qml: Displaying processing splash
" [] "
"starting monerod /home/petter/Downloads/monero-gui-linux-x64-v0.12.0.0/monerod"
With command line arguments  ("--detach", "--bootstrap-daemon-address", "node.moneroworld.com:18089", "--check-updates", "disabled")
2018-04-18 23:50:09.885	    7fb752ba1740	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
Forking to background...
sending external cmd:  ("status")
"\u001B[31m2018-04-18 23:51:51.752\t    7fe7c1b00740\tERROR\tnet.http\tcontrib/epee/include/net/http_client.h:456\tUnexpected recv fail\n\u001B[0mError: Problem fetching info-- rpc_request: \n"
daemon not running. checking again in 2 seconds.
qml: daemon start failed
qml: Hiding processing splash
refreshed
qml: >>> wallet refreshed
Checking connection status
Checking connection status
Checking connection status
qml: >>> wallet updated
NEW STATUS  Wallet::ConnectionStatus(ConnectionStatus_Disconnected)
qml: Wallet connection status changed 0
2018-04-18 23:51:52.519	    7fbedb7947c0	ERROR	default	src/wallet/api/utils.cpp:46	error: std::bad_cast
refreshed
qml: >>> wallet refreshed
Checking connection status
qml: >>> wallet updated
refreshed
qml: >>> wallet refreshed
Checking connection status
qml: >>> wallet updated
qml: showing status message
qml: showing status message
qml: showing status message
qml: resetting android close
refreshed
qml: >>> wallet refreshed
Checking connection status
qml: >>> wallet updated
refreshed

```

## Mafaka8 | 2018-04-19T02:21:49+00:00
@stoffu 

root@miner:~/monero-gui# make -C monero/build/release/external install
make: Entering directory '/monero-gui/monero/build/release/external'
make: *** No rule to make target 'install'.  Stop.
make: Leaving directory '/monero-gui/monero/build/release/external'
root@miner:~/monero-gui# make -C monero/build/release/contrib install
make: Entering directory '/monero-gui/monero/build/release/contrib'
make: *** No rule to make target 'install'.  Stop.
make: Leaving directory '/monero-gui/monero/build/release/contrib'
root@miner:~/monero-gui# make -C monero/build/release/src/wallet install
make: Entering directory '/monero-gui/monero/build/release/src/wallet'
make: *** No rule to make target 'install'.  Stop.
make: Leaving directory '/monero-gui/monero/build/release/src/wallet'


## stoffu | 2018-04-19T04:28:35+00:00
@Mafaka8 
That's strange. What if you dropped the word `install` at the end of the command?

Also, what do you see if you just run `./get_libwallet_api.sh`? This script is internally called from `build.sh` and is responsible for compiling the Monero libraries.


## Mafaka8 | 2018-04-19T05:54:59+00:00
root@miner:~/monero-gui# make -C monero/build/release/external
make: Entering directory '/monero-gui/monero/build/release/external'
make: *** No targets specified and no makefile found.  Stop.
make: Leaving directory '/monero-gui/monero/build/release/external'


## Mafaka8 | 2018-04-19T05:58:21+00:00
running the ./get_libwallet_api.sh I get: 

-- Looking for rl_copy_text
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Readline_LIBRARY
    linked by target "cmTC_27cb0" in directory /monero-gui/monero/build/release/CMakeFiles/CMakeTmp

CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Readline_LIBRARY
    linked by target "cmTC_6f6ac" in directory /monero-gui/monero/build/release/CMakeFiles/CMakeTmp

CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Looking for rl_filename_completion_function - not found
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/bin/git
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.11")
-- Performing Test HAVE_C11
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
Readline_LIBRARY
    linked by target "cmTC_e5ff3" in directory /monero-gui/monero/build/release/CMakeFiles/CMakeTmp

CMake Error: Internal CMake error, TryCompile configure of cmake failed
-- Performing Test HAVE_C11 - Failed
-- Configuring incomplete, errors occurred!


## rysade | 2018-04-19T08:50:30+00:00
> For anyone that is affected by the issue, please check whether this one works:

> https://build.getmonero.org/builders/monero-gui-linux-qt57/builds/4

@dEBRUYNE-1 Do you still care to have the output of this?

I am affected by this issue on Lubuntu 16.04.04. monerod is run locally. At first I thought this was an RPC issue and was very frustrated with the lack of info on how the GUI wallet communicates with the daemon. Is it through RPC?

## stoffu | 2018-04-19T10:01:26+00:00
@Mafaka8 
Sorry to say this so late, but I think it'd be more appropriate to open a separate ticket for any build-related issues. This thread is for discussing the `std::bad_cast` problem.

## Mafaka8 | 2018-04-19T11:54:05+00:00
No problem, I am affected by the std::bad_cast issue with the binary as well. I also tried that builds/4 and no luck still std::bad_cast issue lol 

## pedroaugustomontes | 2018-04-19T16:53:47+00:00
As I can see only expert Linux user are knowing how to fix that, please we need help =(

## dEBRUYNE-1 | 2018-04-19T20:57:36+00:00
@rysade (and anyone else affected by this particular issue) - Could you test these binaries?

https://build.getmonero.org/builders/monero-gui-ubuntu-amd64/builds/201

## rysade | 2018-04-20T00:54:24+00:00
> @rysade (and anyone else affected by this particular issue) - Could you test these binaries?

> https://build.getmonero.org/builders/monero-gui-ubuntu-amd64/builds/201


That appears to have worked.
stdout:
`app startd
available width:  1871
available height:  1047
devicePixelRatio:  1
screen height:  1920
screen width:  1080
screen logical dpi:  96
screen Physical dpi:  102.598
screen calculated ratio:  0.801544
qml: check next false
qml: Checking seed
qml: check next false
qml: Checking seed
qml: check next false
qml: check next false
2018-04-20 00:50:06.285	    7f750424a7c0	WARN 	net.http	src/common/util.cpp:627	Failed to determine whether address '' is local, assuming not
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
qml: transfer page loaded
qml: PrivacyLevel changed:0
qml: mixin count: 6
qml: qrScannerEnabled disabled
qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:241:9: QML ContentItem: Binding loop detected for property "implicitWidth"
Checking for updates
qml: languages availible:  29
qml: initializing..
setLanguage   "en"
qml: transfer page loaded
qml: PrivacyLevel changed:0
qml: mixin count: 6
qml: opening wallet at:  /home/rysade/.local/monero/default-wallet.keys , network type:  mainnet
Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type): opening wallet at /home/rysade/.local/monero/default-wallet.keys, nettype = 0 
2018-04-20 00:50:25.166	    7f74e4d09700	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3718	Loaded wallet keys file, with public address: 44ZBNkbTqsdTW4b5r6grVFRCShhPEeeTBS9vNxz6WJSbYm9jRC5nyzuH9DhGu29irXLF16oJ2JGDzJ4NCLRmXvxwK8h3nrh
Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type): opened wallet: 44ZBNkbTqsdTW4b5r6grVFRCShhPEeeTBS9vNxz6WJSbYm9jRC5nyzuH9DhGu29irXLF16oJ2JGDzJ4NCLRmXvxwK8h3nrh, status: 0
AddressBook
getAll
Subaddress
getAll
qml: check next false
qml: >>> wallet opened: Wallet(0x7f74d02db2c0)
qml: Recovering from seed:  false
qml: restore Height 0
qml: initializing with daemon address:  localhost:18081
"initAsync: localhost:18081"
init non async
init async finished - starting refresh
Checking connection status
NEW STATUS  Wallet::ConnectionStatus(ConnectionStatus_Disconnected)
qml: Wallet connection status changed 0
refreshed
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
qml: >>> wallet refreshed
qml: >>> wallet updated
refreshed
qml: >>> wallet refreshed
Checking connection status
qml: >>> wallet updated
qml: Displaying processing splash
" [] "
"starting monerod /home/rysade/.local/monero/monerod"
With command line arguments  ("--detach", "--check-updates", "disabled")
2018-04-20 00:50:37.974	    7f74e5d0b700	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
Checking for updates - done
2018-04-20 00:50:38.424	    7fe1c522a740	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
Forking to background...
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Height: 1554976/1554976 (100.0%) on mainnet, not mining, net hash 459.02 MH/s, v7, up to date, 0(out)+0(in) connections, uptime 0d 0h 0m 27s\n"
daemon is started. Waiting 5 seconds to let daemon catch up
qml: daemon started
qml: Hiding processing splash
Checking connection status
NEW STATUS  Wallet::ConnectionStatus(ConnectionStatus_Connected)
qml: Wallet connection status changed 1
refreshed
qml: >>> wallet refreshed
qml: >>> wallet updated
refreshed
qml: >>> wallet refreshed
Checking connection status
qml: >>> wallet updated
`
GUI is showing 'Wallet is synchronized' and 'Daemon is synchronized (1554978)' and my balance is correct.

What was the issue? I am guessing it wasn't RPC if there was some kind of compiler snafu.

The last batch of binaries I may have neglected to fully test. I assumed we were only testing the GUI, and so swapped it out. This time, I copy-pasted the entire folder into my monero directory, replacing everything including monerod.

I'll try whatever you like if you're interested. I've always wanted to help out with an open source project, and Monero is one of my favorites.

## vitalisator | 2018-04-20T06:14:40+00:00
@dEBRUYNE-1 , that works for me too now. Good work!

some debug output with private data Xed:
./start-gui.sh 
app startd
available width:  1920
available height:  1048
devicePixelRatio:  1
screen height:  1920
screen width:  1080
screen logical dpi:  96.1263
screen Physical dpi:  141.951
screen calculated ratio:  1.10899
qml: check next false
qml: Checking seed
qml: check next false
qml: Checking seed
qml: check next false
qml: check next false
2018-04-20 06:05:05.783     7fe77fffd7c0        WARN    net.http        src/common/util.cpp:627 Failed to determine whether address '' is local, assuming not
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
qml: transfer page loaded
qml: PrivacyLevel changed:0
qml: mixin count: 6
qml: qrScannerEnabled disabled
qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:241:9: QML ContentItem: Binding loop detected for property "implicitWidth"                                                                      
Checking for updates                                                                                                                                                                                               
qml: languages availible:  29                                                                                                                                                                                      
Checking for updates - done                                                                                                                                                                                        
qml: initializing..                                                                                                                                                                                                
setLanguage   "de"                                                                                                                                                                                                 
setLanguage: loading translation file 'monero-core_de' from '/home/me/Downloads/build (2)/release/bin/translations                                                                                              
setLanguage: translation for language 'de' loaded successfully                                                                                                                                                     
qml: transfer page loaded                                                                                                                                                                                          
qml: PrivacyLevel changed:0                                                                                                                                                                                        
qml: mixin count: 6                                                                                                                                                                                                
qml: opening wallet at:  /home/me/Monero/wallets/wallet/wallet.keys , network type:  mainnet                                                                                                                    
Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type): opening wallet at /home/me/Monero/wallets/wallet/wallet.keys, nettype = 0                                                 
2018-04-20 06:05:23.725     7fe76ad51700        DEBUG   device.ledger   src/device/device_ledger.cpp:199        Device 0 Created                                                                                   
2018-04-20 06:05:23.725     7fe76ad51700        INFO    wallet.wallet2  src/wallet/wallet2.cpp:5482     ringdb path set to /home/me/.shared-ringdb                                                              
2018-04-20 06:05:23.804     7fe76ad51700        WARN    wallet.wallet2  src/wallet/wallet2.cpp:3718     Loaded wallet keys file, with public address: XXX                                                                                                                                                                                 
2018-04-20 06:05:23.811     7fe76ad51700        INFO    wallet.wallet2  src/wallet/wallet2.cpp:3737     Trying to decrypt cache data                                                                               
2018-04-20 06:05:23.900     7fe76ad51700        DEBUG   wallet.wallet2  src/wallet/api/address_book.cpp:98      Refreshing addressbook                                                                             
Wallet* WalletManager::openWallet(const QString&, const QString&, NetworkType::Type): opened wallet: XXX, status: 0    
AddressBook                                                                                                                                                                                                        
getAll                                                                                                                                                                                                             
Subaddress                                                                                                                                                                                                         
getAll                                                                                                                                                                                                             
qml: check next false
qml: >>> wallet opened: Wallet(0x7fe75c529af0)
qml: Recovering from seed:  false
qml: restore Height 0
2018-04-20 06:05:23.905     7fe77fffd7c0        DEBUG   net.http        src/common/util.cpp:641 Address 'localhost:18081' is local
qml: initializing with daemon address:  localhost:18081
"initAsync: localhost:18081"
init non async
2018-04-20 06:05:23.905     7fe76ad51700        DEBUG   net.http        src/common/util.cpp:641 Address 'localhost:18081' is local
init async finished - starting refresh
Checking connection status
2018-04-20 06:05:23.920     7fe77fffd7c0        DEBUG   WalletAPI       src/wallet/api/wallet.cpp:1807  startRefresh: refresh started/resumed...
2018-04-20 06:05:23.921     7fe76ad51700        WARN    net     contrib/epee/include/net/net_helper.h:188       Some problems at connect, message: Verbindungsaufbau abgelehnt
NEW STATUS  Wallet::ConnectionStatus(ConnectionStatus_Disconnected)
qml: Wallet connection status changed 0
2018-04-20 06:05:23.921     7fe768d4d700        WARN    net     contrib/epee/include/net/net_helper.h:188       Some problems at connect, message: Verbindungsaufbau abgelehnt
refreshed
2018-04-20 06:05:23.921     7fe77fffd7c0        DEBUG   net.http        src/common/util.cpp:647 Address 'xxx.xxx.xxx.xxx:18081' is not local
qml: >>> wallet refreshed
qml: >>> wallet updated
2018-04-20 06:05:33.922     7fe768d4d700        WARN    net     contrib/epee/include/net/net_helper.h:188       Some problems at connect, message: Verbindungsaufbau abgelehnt
refreshed
qml: >>> wallet refreshed
Checking connection status
2018-04-20 06:05:33.924     7fe76ad51700        WARN    net     contrib/epee/include/net/net_helper.h:188       Some problems at connect, message: Verbindungsaufbau abgelehnt
qml: >>> wallet updated
2018-04-20 06:05:43.923     7fe768d4d700        WARN    net     contrib/epee/include/net/net_helper.h:188       Some problems at connect, message: Verbindungsaufbau abgelehnt
refreshed
qml: >>> wallet refreshed
Checking connection status
2018-04-20 06:05:43.924     7fe76ad51700        WARN    net     contrib/epee/include/net/net_helper.h:188       Some problems at connect, message: Verbindungsaufbau abgelehnt
qml: >>> wallet updated
2018-04-20 06:05:53.924     7fe768d4d700        WARN    net     contrib/epee/include/net/net_helper.h:188       Some problems at connect, message: Verbindungsaufbau abgelehnt
refreshed
qml: >>> wallet refreshed
Checking connection status
2018-04-20 06:05:53.925     7fe76ad51700        WARN    net     contrib/epee/include/net/net_helper.h:188       Some problems at connect, message: Verbindungsaufbau abgelehnt
qml: >>> wallet updated
2018-04-20 06:06:03.925     7fe768d4d700        WARN    net     contrib/epee/include/net/net_helper.h:188       Some problems at connect, message: Verbindungsaufbau abgelehnt
refreshed
qml: >>> wallet refreshed
Checking connection status
2018-04-20 06:06:03.926     7fe76ad51700        WARN    net     contrib/epee/include/net/net_helper.h:188       Some problems at connect, message: Verbindungsaufbau abgelehnt
qml: >>> wallet updated
2018-04-20 06:06:09.975     7fe77fffd7c0        DEBUG   WalletAPI       src/wallet/api/wallet.cpp:1827  pauseRefresh: refresh paused...
qml: Displaying processing splash
" [] "
"starting monerod /home/me/Downloads/build (2)/release/bin/monerod"
With command line arguments  ("--detach", "--check-updates", "disabled")
2018-04-20 06:06:11.014     7fc3d6f6c740        INFO    global  src/daemon/main.cpp:280 Monero 'Lithium Luna' (v0.12.0.0-master-release)
Forking to background...
sending external cmd:  ("status")
"Height: 1547392/1547392 (100.0%) on mainnet, not mining, net hash 387.12 MH/s, v7, up to date, 0(out)+0(in) connections, uptime 0d 0h 0m 1s\n"
daemon is started. Waiting 5 seconds to let daemon catch up
qml: daemon started
qml: Hiding processing splash
Checking connection status
2018-04-20 06:06:18.270     7fe77fffd7c0        DEBUG   WalletAPI       src/wallet/api/wallet.cpp:1807  startRefresh: refresh started/resumed...
NEW STATUS  Wallet::ConnectionStatus(ConnectionStatus_Connected)
qml: Wallet connection status changed 1
2018-04-20 06:06:18.285     7fe77fffd7c0        DEBUG   cn      src/cryptonote_basic/cryptonote_basic_impl.cpp:220      Invalid address format
2018-04-20 06:06:18.285     7fe77fffd7c0        DEBUG   cn      src/cryptonote_basic/cryptonote_basic_impl.cpp:220      Invalid address format
2018-04-20 06:06:18.290     7fe77fffd7c0        DEBUG   net.http        src/common/util.cpp:647 Address '192.168.77.15:18081' is not local
2018-04-20 06:06:33.446     7fe768d4d700        DEBUG   net     contrib/epee/include/net/net_helper.h:398       Problems at read: Vorgang abgebrochen
2018-04-20 06:06:33.446     7fe768d4d700        ERROR   net.http        contrib/epee/include/net/http_client.h:456      Unexpected recv fail
2018-04-20 06:06:33.447     7fe768d4d700        INFO    net.http        contrib/epee/include/storages/http_abstract_invoke.h:53 Failed to invoke http request to  /json_rpc
2018-04-20 06:06:33.447     7fe768d4d700        ERROR   WalletAPI       src/wallet/api/wallet.cpp:893   daemonBlockChainTargetHeight: possibly lost connection to daemon
2018-04-20 06:06:33.447     7fe768d4d700        DEBUG   net.http        contrib/epee/include/net/http_client.h:365      Reconnecting...

## pedroaugustomontes | 2018-04-20T16:23:53+00:00
I'm very frustrated with this wallet, I need my money but I can not access it, only get badcast issue :(

## sanderfoobar | 2018-04-20T16:49:51+00:00
@MrPMontes Try the CLI or wait for updates.

## badfiles | 2018-04-20T20:52:12+00:00
It finally works, thank you.

## gagarin55 | 2018-04-21T05:10:00+00:00
same issue for me
Ubuntu 17.04

## el00ruobuob | 2018-04-24T09:49:49+00:00
@dEBRUYNE-1 https://build.getmonero.org/builders/monero-gui-ubuntu-amd64/builds/201 works perfectly!

## RemiMorin | 2018-04-24T23:27:15+00:00
Works perfectly, Ubuntu 16 upgraded a while back, I look through the commit and can't figure out what's change? Is it only a change in the build environment?

## dEBRUYNE-1 | 2018-04-25T11:30:51+00:00
@RemiMorin - It's merely a change in the build environment. If I recall correctly, upgrading boost from 1.58 to 1.59 resolved the bad_cast issue. 

## PanderMusubi | 2018-04-27T18:06:53+00:00
Build 201 fixes it for Ubuntu 17.10. If a new public release can be made, please. Also less tech-savvy users would like to use it.

## RemiMorin | 2018-04-27T18:14:56+00:00
I agree that a new public build improve confidence and normalize the situation but you don't need to be tech-savvy.

Just go on the the 201 build page you will see a link directly to the build archive:
monero-gui-db5e71c-linux-amd64.tar.gz
https://build.getmonero.org/downloads/monero-gui-db5e71c-linux-amd64.tar.gz

inside this archive you will find the release folder. This folder content is the same as an official public release. Just allow execution of the start-gui script and you are done.


## DreadfulCode | 2018-05-11T01:08:03+00:00
It's still an issue in 64 bit Linux. Just did a fresh install and this month-old bug is still happening. I can work around this but it takes a software guy like me to figure it out. Why is this still a problem?

## pmatulis | 2018-05-11T01:31:13+00:00
The latest client is fatally broken even though the cause has been known for weeks. Why there has been no update is beyond me. 

## grigio | 2018-05-11T17:00:28+00:00
Please

## stoffu | 2018-05-12T00:28:04+00:00
This is a build-related problem which will be fixed in the next point release. Meanwhile, you can use an unofficial binary built by buildbot https://build.getmonero.org/builders/monero-gui-ubuntu-amd64/builds/201 as suggested above https://github.com/monero-project/monero-gui/issues/1261#issuecomment-382878443.

## bananajamma | 2018-05-12T15:20:43+00:00
~build 201 did not work for me... using the cli work-around~

edit: build 201 did resolve the `bad_cast` issue for me, but the application appeared frozen due to window behavior, #1431 

## sanderfoobar | 2018-05-12T16:44:31+00:00
@bananajamma Did you experience the `bad_cast` error on build 201? If it was something else, please open a new issue. If you did, please post OS details here.

## panupan | 2018-05-15T12:19:49+00:00
+1 happening on Ubuntu 16.04 LTS.  Broken even after clean wipe of data dir and wallet.  imo XMR is probably the most underrated coin out here... but it's issues like this that have caused its lackluster performance as of late.

## laudai | 2018-05-16T04:54:22+00:00
same problem on Ubuntu 16.04 +1

## Jaggfab | 2018-06-05T19:09:27+00:00
Same problem here, Ubuntu 16.04.

## augustynr | 2018-06-08T04:40:25+00:00
This still does not work, official website has old binary and the link from this thread is dead

## el00ruobuob | 2018-06-08T04:57:06+00:00
This link? https://build.getmonero.org/builders/monero-gui-ubuntu-amd64/builds/201 ~~looks ok IMO~~ edit: no such resource on build file, it's indeed broken.  

## augustynr | 2018-06-08T05:04:05+00:00
Yep, Can I download it from anywhere?

## stoffu | 2018-06-08T05:51:51+00:00
This is the most recent build for the master which works for me: https://build.getmonero.org/builders/monero-gui-ubuntu-amd64/builds/472

## el00ruobuob | 2018-06-08T07:08:05+00:00
Thanks @stoffu!

## sanderfoobar | 2018-06-16T21:15:42+00:00
Alright, this one seems fixed now.

Unofficial release of 0.12.2: https://www.reddit.com/r/Monero/comments/8rkwyt/unofficial_release_of_gui_wallet_version_0122/

If you want the official releases, wait a bit.

+resolved

## dEBRUYNE-1 | 2018-07-02T20:06:10+00:00
GUI v0.12.2.0, which includes a fix for this particular issue, has been released:

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

# Action History
- Created by: dEBRUYNE-1 | 2018-04-04T15:20:55+00:00
- Closed at: 2018-06-16T21:18:21+00:00
