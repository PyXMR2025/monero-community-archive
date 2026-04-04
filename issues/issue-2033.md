---
title: Unable to close GUI
source_url: https://github.com/monero-project/monero-gui/issues/2033
author: kasperaitis
assignees: []
labels:
- bug
created_at: '2019-03-25T19:58:54+00:00'
updated_at: '2020-02-29T13:01:08+00:00'
type: issue
status: closed
closed_at: '2019-06-21T19:44:18+00:00'
---

# Original Description
It seems there is a problem with closing GUI in windows 10 x64. When trying to close GUI it doesn't closes. 

![monero](https://user-images.githubusercontent.com/1422212/54983000-9be9a900-4fb4-11e9-89c3-057f8560b6ed.gif)

branch: master (also release-v0.14)
os: Windows 10 x64
MSYS2 MinGW 64-bit
GUI version: v0.14.0.0-20-g4bab4c5 (Qt 5.12.2)
Embedded Monero version: v0.14.0.2-3-g8039b8d9

It was compiles by instructions in README.md.

Hopefully it's not just for me and will be fixed.

Video:
[2019-03-25_21-52-39.zip](https://github.com/monero-project/monero-gui/files/3005216/2019-03-25_21-52-39.zip)

Error log:
https://pastebin.com/HMG2K4DV

Edit: Added GIF. 




# Discussion History
## dEBRUYNE-1 | 2019-03-26T16:30:49+00:00
Does the issue also occur if you use the release binary from the official Monero website? 

## sanderfoobar | 2019-03-26T16:32:17+00:00
Does the GUI freeze when you click on that close button?

## kasperaitis | 2019-03-26T17:34:12+00:00
> 
> 
> Does the issue also occur if you use the release binary from the official Monero website?

@dEBRUYNE-1 No it doesn't. Release version works. The problem is with compiled one.

## kasperaitis | 2019-03-26T17:49:02+00:00
> 
> 
> Does the GUI freeze when you click on that close button?

@xmrdsc No. It seems GUI still functional. But it disappears and reappears in Task Manager when trying to close it second and other times.

![monero2](https://user-images.githubusercontent.com/1422212/55020747-260b2f00-5000-11e9-9edd-78912aa86592.gif)


## sanderfoobar | 2019-03-27T02:31:49+00:00
Thanks for the additional information. Very weird bug and I have no idea what could cause this.

## kasperaitis | 2019-03-28T06:05:42+00:00
I tried to compile in other machine (Win 10 x64). It seems the problem is consistent and even worse. I was unable to launch monero-wallet-gui.exe.

![monero3](https://user-images.githubusercontent.com/1422212/55133752-63220f00-512f-11e9-8b5d-c70fe10e5422.gif)

I was able to launch in Low Graphics Mode by start-low-graphics-mode.bat but as in other machine I was unable to close.

![monero4](https://user-images.githubusercontent.com/1422212/55133816-92d11700-512f-11e9-80a1-2fb5550e8fec.gif)

Link to error log: https://pastebin.com/Xha0i9BR


## dEBRUYNE-1 | 2019-03-28T07:08:28+00:00
Are you using the QT package from MSYS2/MinGW64? Because that one does not have graphic fallback included and thus logically does not work in a VM. 

## kasperaitis | 2019-03-29T10:09:21+00:00
@dEBRUYNE-1 Yes I'm using QT from MSYS2/MinGW64. But it's not Virtual Machines. It's actual PCs with Windows installed.

## dEBRUYNE-1 | 2019-03-29T13:12:46+00:00
I misread, my previous comment still applies though. That is, there's no fallback in case the initial graphic rendering does not work properly. 

## selsta | 2019-04-02T21:48:24+00:00
Seems to be related to Qt 5.12.2.

```
2019-04-02 19:29:31.672	     0x111b505c0	DEBUG	frontend	src/wallet/api/wallet.cpp:395	close accepted
2019-04-02 19:29:31.672	     0x111b505c0	DEBUG	frontend	src/wallet/api/wallet.cpp:395	DaemonManager: exit()
2019-04-02 19:29:31.672	     0x111b505c0	DEBUG	frontend	src/wallet/api/wallet.cpp:395	~Wallet: Closing wallet
2019-04-02 19:29:31.672	     0x111b505c0	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:5288	trimming to 1748760, offset 1748760
2019-04-02 19:29:31.715	     0x111b505c0	DEBUG	frontend	src/wallet/api/wallet.cpp:395	Wallet cache stored successfully
2019-04-02 19:29:31.715	     0x111b505c0	INFO	WalletAPI	src/wallet/api/wallet.cpp:444	~WalletImpl
2019-04-02 19:29:31.715	     0x111b505c0	DEBUG	WalletAPI	src/wallet/api/wallet.cpp:2141	pauseRefresh: refresh paused...
2019-04-02 19:29:31.716	     0x111b505c0	INFO	WalletAPI	src/wallet/api/wallet.cpp:752	closing wallet...
2019-04-02 19:29:31.716	     0x111b505c0	INFO	WalletAPI	src/wallet/api/wallet.cpp:763	Calling wallet::stop...
2019-04-02 19:29:31.716	     0x111b505c0	INFO	WalletAPI	src/wallet/api/wallet.cpp:765	wallet::stop done
2019-04-02 19:29:31.716	     0x111b505c0	INFO	WalletAPI	src/wallet/api/wallet.cpp:452	~WalletImpl finished
2019-04-02 19:29:31.716	     0x111b505c0	DEBUG	net	contrib/epee/include/net/net_helper.h:631	Problems at ssl shutdown: uninitialized
2019-04-02 19:29:31.716	     0x111b505c0	DEBUG	net	contrib/epee/include/net/net_helper.h:565	Problems at cancel: Bad file descriptor
2019-04-02 19:29:31.716	     0x111b505c0	DEBUG	net	contrib/epee/include/net/net_helper.h:568	Problems at shutdown: Bad file descriptor
2019-04-02 19:29:31.719	     0x111b505c0	DEBUG	net	contrib/epee/include/net/net_helper.h:631	Problems at ssl shutdown: uninitialized
2019-04-02 19:29:31.719	     0x111b505c0	DEBUG	net	contrib/epee/include/net/net_helper.h:565	Problems at cancel: Bad file descriptor
2019-04-02 19:29:31.719	     0x111b505c0	DEBUG	net	contrib/epee/include/net/net_helper.h:568	Problems at shutdown: Bad file descriptor
2019-04-02 19:29:31.722	     0x111b505c0	DEBUG	frontend	src/wallet/api/wallet.cpp:395	m_walletImpl deleted
2019-04-02 19:29:33.718	     0x111b505c0	DEBUG	frontend	src/wallet/api/wallet.cpp:395	blocking close event
2019-04-02 19:29:33.718	     0x111b505c0	DEBUG	frontend	src/wallet/api/wallet.cpp:395	sending external cmd:  ("status")
2019-04-02 19:29:35.274	     0x111b505c0	DEBUG	frontend	src/wallet/api/wallet.cpp:395	"\u001B[36m2019-04-02 19:29:34.736\t     0x118ec15c0\tINFO\tglobal\tsrc/daemon/main.cpp:280\tMonero 'Boron Butterfly' (v0.14.1.0-c5a834da)\n\u001B[0m\u001B[36m2019-04-02 19:29:34.746\t     0x118ec15c0\tINFO\tglobal\tcontrib/epee/src/net_ssl.cpp:75\tGenerating SSL certificate\n\u001B[0mError: Couldn't connect to daemon: 127.0.0.1:18081\n"
2019-04-02 19:29:35.274	     0x111b505c0	DEBUG	frontend	src/wallet/api/wallet.cpp:395	close accepted
2019-04-02 19:29:35.274	     0x111b505c0	DEBUG	frontend	src/wallet/api/wallet.cpp:395	DaemonManager: exit()
2019-04-02 19:29:35.274	     0x111b505c0	ERROR	frontend	src/wallet/api/wallet.cpp:407	Trying to close non existing wallet  QObject(0x0)
```

## selsta | 2019-04-03T15:46:41+00:00
In the meantime, you can use Qt 5.12.1 to get a functioning close button.

+bug

## kasperaitis | 2019-04-15T15:54:03+00:00
@selsta 
Thanks. It seems Mac also has this problem with Qt 5.12.2.

## feugen | 2019-05-30T23:54:14+00:00
Same issue on linux with qt version 5.12.3. I used this package: https://aur.archlinux.org/packages/monero-wallet-qt

## ghost | 2019-06-10T20:02:26+00:00
I couldn't close the GUI window, too. Error was: I was using Ledger Nano S and didn't press "Export View Key" on the device. Once I pressed it, the GUI window closed immediately.

## adrelanos | 2019-10-28T13:08:55+00:00
This isn't fixed for me. Close button does nothing.

`monero-gui-v0.14.1.0` on Qubes-Whonix 15 (Debian `buster` based).

## adrelanos | 2020-02-29T09:17:15+00:00
Please reopen.

## selsta | 2020-02-29T10:59:34+00:00
@adrelanos Can you open a new issue with detailed information? This issue here is definitely fixed.

# Action History
- Created by: kasperaitis | 2019-03-25T19:58:54+00:00
- Closed at: 2019-06-21T19:44:18+00:00
