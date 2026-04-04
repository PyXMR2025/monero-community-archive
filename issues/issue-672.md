---
title: Only runs the first time in a flatpak
source_url: https://github.com/monero-project/monero-gui/issues/672
author: snaggen
assignees: []
labels:
- resolved
created_at: '2017-04-11T15:16:52+00:00'
updated_at: '2018-11-18T17:00:34+00:00'
type: issue
status: closed
closed_at: '2018-11-18T17:00:34+00:00'
---

# Original Description
I posted a few days ago on redit /r/Monero about my attempt at creating a flatpaked version of the Monero Gui Wallet. 
I have now got the flatpak to work as far as the Wallet is actually starting the first time. I run and finish the setup wizard. The block chain syncs, and everything seems fine. So far so good.... 

Now the problems start.... 
The second time I start it, the application crashes.. something about  "portable_storage: wrong binary format - signature missmatch"
and password error... 

```
2017-04-11 09:53:26.328     7f985e49b700    ERROR   net.http    contrib/epee/include/storages/portable_storage.h:161    portable_storage: wrong binary format - signature missmatch
2017-04-11 09:53:26.328     7f985e49b700    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2081 !r. THROW EXCEPTION: error::invalid_password
2017-04-11 09:53:26.328     7f985e49b700    WARN    net.http    src/wallet/wallet_errors.h:697  /run/build/monero-core-gui/monero/src/wallet/wallet2.cpp:2081:N5tools5error16invalid_passwordE: invalid password
2017-04-11 09:53:26.329     7f985e49b700    ERROR   WalletAPI   src/wallet/api/wallet.cpp:502   Error opening wallet: invalid password

    Thread 15 "Thread (pooled)" received signal SIGABRT, Aborted.
[Switching to LWP 83]
0x00000032efe3304f in raise () from /lib/libc.so.6
(gdb) bt
#0  0x00000032efe3304f in raise () from /lib/libc.so.6
#1  0x00000032efe3447a in abort () from /lib/libc.so.6
#2  0x00007f98865b4321 in ?? () from /lib/libQt5Core.so.5
#3  0x00007f98865b073a in QMessageLogger::fatal(char const*, ...) const () from /lib/libQt5Core.so.5
#4  0x00007f98865a96e5 in qt_assert_x(char const*, char const*, char const*, int) () from /lib/libQt5Core.so.5
#5  0x00007f988680492d in QCoreApplicationPrivate::checkReceiverThread(QObject*) () from /lib/libQt5Core.so.5
#6  0x00007f9887ba2b22 in QApplication::notify(QObject*, QEvent*) () from /lib/libQt5Widgets.so.5
#7  0x00007f9886805732 in QCoreApplication::notifyInternal2(QObject*, QEvent*) () from /lib/libQt5Core.so.5
#8  0x00007f98868097b0 in QCoreApplication::sendEvent(QObject*, QEvent*) () from /lib/libQt5Core.so.5
#9  0x00007f988684150e in QObjectPrivate::setParent_helper(QObject*) () from /lib/libQt5Core.so.5
#10 0x00007f988683fa1f in QObject::~QObject() () from /lib/libQt5Core.so.5
#11 0x0000000000478c26 in ?? ()
#12 0x0000000000478c42 in ?? ()
#13 0x0000000000451a85 in ?? ()
#14 0x0000000000451b6c in ?? ()
#15 0x00000000004484e4 in ?? ()
#16 0x000000000044d863 in ?? ()
#17 0x000000000044d710 in ?? ()
#18 0x00007f98865c4ba9 in ?? () from /lib/libQt5Core.so.5
#19 0x00007f98865cb046 in ?? () from /lib/libQt5Core.so.5
#20 0x00007f988606b3f4 in ?? () from /lib/libpthread.so.0
#21 0x00000032efee827f in clone () from /lib/libc.so.6

```
I have tried to see what files the applications use, and make sure they are preserved between the sessions (since flatpak can clear out some data), but everything seems to be saved between the sessions. So I don't think it is pure flatpak related, so I need help from someone that knows the code to find out what is going wrong here... 

My github repository containing my work so far is at: 
https://github.com/snaggen/monero-wallet-flatpak

To build this you need the kde sdk:
```
flatpak remote-add kderuntime --from https://distribute.kde.org/kderuntime.flatpakrepo
flatpak install kderuntime org.kde.Platform
flatpak install kderuntime org.kde.Sdk

```
After that you should be able to build it using: 
```
make
flatpak --user remote-add --no-gpg-verify local-monero repo
flatpak --user install local-monero org.getmonero.Wallet

```
Then to run a flatpak from the commandline you do: 
`flatpak run org.getmonero.Wallet`

This may seem like flatpaks are hard to use, but that is only the buildsteps. The goal is for the end user to install this with a one liner:
`flatpak install --from https://getmonero.org/downloads/monerowallet.flatpakref`
And then run i from the normal desktop UI and update it using gnome-software or just "flatpak update". 
So, the end user experience of a flatpak is really smooth... 

Here is a link to the original post as a reference to follow some of my debugging efforts and methods: 
https://www.reddit.com/r/Monero/comments/64c5pj/need_help_trying_to_build_a_flatpak_of_the_monero/


# Discussion History
## snaggen | 2017-09-28T14:52:34+00:00
I'm currently trying to get the Monero wallet in to flathub, but they would prefer to have a native build instead of a repackage of the binary. However, it seems that this issue still remains so help would be greatly appreciated. 
https://github.com/flathub/flathub/pull/94

## snaggen | 2017-09-28T19:55:46+00:00
As i commented in the flathub issue: 
It seems that it is the call
r = epee::serialization::load_t_from_binary(m_account, account_data);
in wallet2.cpp that fails, due to
2017-09-28 19:12:52.612 7fb763bff700 ERROR net.http contrib/epee/include/storages/portable_storage.h:161 portable_storage: wrong binary format - signature mismatch

So, why does that happen in a flatpak built from source, but not repackaged.... and only the second time the wallet is opened. It doesn't happen when the wallet is opened from the wizard. 

## erciccione | 2018-11-18T13:29:12+00:00
Related to old versions. Please reopen if still valid

+resolved

# Action History
- Created by: snaggen | 2017-04-11T15:16:52+00:00
- Closed at: 2018-11-18T17:00:34+00:00
