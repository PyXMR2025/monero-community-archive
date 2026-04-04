---
title: monero-wallet-gui segfault at startup
source_url: https://github.com/monero-project/monero-gui/issues/1055
author: eklitzke
assignees: []
labels:
- resolved
created_at: '2018-01-01T02:11:01+00:00'
updated_at: '2018-11-18T14:27:31+00:00'
type: issue
status: closed
closed_at: '2018-11-18T14:27:31+00:00'
---

# Original Description
I have built monero-wallet-gui from source, but it won't run. Most of the time it segfaults, sometimes it doesn't segfault but no graphical frame is ever launched. I am running Fedora 27. This happens both in the v0.11.1.0 tag, as well as in master. The information in this report is for a build from master.

Build information:

```
$ gcc --version
gcc (GCC) 7.2.1 20170915 (Red Hat 7.2.1-2)
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

$ qmake --version
QMake version 3.1
Using Qt version 5.9.2 in /usr/lib64
```

Backtrace looks like this:

```
(gdb) bt
#0  0x0000000000000000 in  ()
#1  0x00007ffff3d87b1e in QObject::connect(QObject const*, char const*, QObject const*, char const*, Qt::ConnectionType) (sender=0x10c3b60, signal=0x86ffd1 "sequencePressed(QVariant,QVariant)", receiver=0x7fffc40ec300, method=0x86ffa9 "sequencePressed(QVariant,QVariant)", type=Qt::AutoConnection) at kernel/qobject.cpp:2712
#2  0x0000000000432b0a in main ()
```

I'm not sure why GDB isn't printing a line number in `main` (this is a debug build, produced from `./build.sh debug`). It might be line 2712, because I see the following when I use `list`:

```
(gdb) list
2707	    const char *method_arg = method;
2708	    ++method; // skip code
2709	
2710	    QArgumentTypeArray methodTypes;
2711	    QByteArray methodName = QMetaObjectPrivate::decodeMethodSignature(method, methodTypes);
2712	    const QMetaObject *rmeta = receiver->metaObject();
2713	    int method_index_relative = -1;
2714	    Q_ASSERT(QMetaObjectPrivate::get(rmeta)->revision >= 7);
2715	    switch (membcode) {
2716	    case QSLOT_CODE:
```

However, I don't know how reliable this line number information is, since it's not printed elsewhere by GDB.

These warnings are also printed to stderr before the segfault:

```
QQmlApplicationEngine failed to load component
qrc:///main.qml:32 module "QtQuick.Controls.Styles" is not installed
qrc:///main.qml:31 module "QtQuick.Controls" is not installed
qrc:///main.qml:33 module "QtQuick.Dialogs" is not installed
qrc:///main.qml:32 module "QtQuick.Controls.Styles" is not installed
qrc:///main.qml:31 module "QtQuick.Controls" is not installed
qrc:///main.qml:33 module "QtQuick.Dialogs" is not installed
qrc:///main.qml:32 module "QtQuick.Controls.Styles" is not installed
qrc:///main.qml:31 module "QtQuick.Controls" is not installed
qrc:///main.qml:33 module "QtQuick.Dialogs" is not installed
```

As I mentioned earlier, occasionally the process does not segfault, but still fails to create a new window frame. In the situations where there is no segfault, I see the following additional error messages logged to stderr:

```
QObject::connect: Cannot connect filter::sequencePressed(QVariant,QVariant) to (null)::sequencePressed(QVariant,QVariant)
QObject::connect: Cannot connect filter::sequenceReleased(QVariant,QVariant) to (null)::sequenceReleased(QVariant,QVariant)
QObject::connect: Cannot connect filter::mousePressed(QVariant,QVariant,QVariant) to (null)::mousePressed(QVariant,QVariant,QVariant)
QObject::connect: Cannot connect filter::mouseReleased(QVariant,QVariant,QVariant) to (null)::mouseReleased(QVariant,QVariant,QVariant)
```

I ran my debug build from master under Valgrind, and there is one invalid read that I see while the program is starting up, after the warning messages above are printed. I don't know if it's actually related, but it's still suspicious:

```
==15111== Invalid read of size 8
==15111==    at 0x432ADF: main (in /home/evan/code/monero-gui/build/debug/bin/monero-wallet-gui)
==15111==  Address 0x24b996b0 is 0 bytes after a block of size 16 alloc'd
==15111==    at 0x4C2FB6B: malloc (vg_replace_malloc.c:299)
==15111==    by 0x8B532DB: QListData::detach(int) (qlist.cpp:120)
==15111==    by 0x432A77: main (in /home/evan/code/monero-gui/build/debug/bin/monero-wallet-gui)
==15111== 
```

I tried using vgdb to halt the program at the invalid read, but since there are no line numbers the output isn't very useful:

```
(gdb) bt
#0  0x0000000000432adf in main ()
(gdb) where
#0  0x0000000000432adf in main ()
(gdb) list
1	in <built-in>
```

I can try to debug this more on my end with a little guidance on how to get a build with better debug information. I can also provide a core dump and executable if that helps.

There's nothing particularly helpful in the `monero-wallet-gui.log` log file. The only line that's logged is:
```
2018-01-01 03:21:07.889     7fe106181ec0        INFO    logging contrib/epee/src/mlog.cpp:185   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
```

# Discussion History
## stoffu | 2018-01-02T08:39:16+00:00
The same error message is commonly observed with a quick web search:

- https://stackoverflow.com/questions/21430469/error-module-qtquick-controls-is-not-installed
- https://bugs.launchpad.net/ubuntu/+source/kdenlive/+bug/1634478
 - https://github.com/webcamoid/webcamoid/issues/69

Does installing the said components fix the issue?

    sudo apt-get install qml-module-qtquick-dialogs qml-module-qtquick-control

## sanderfoobar | 2018-03-30T01:11:22+00:00
Could you try again using latest master + tips from stoffu?

## erciccione | 2018-11-18T14:18:06+00:00
Related to older version. Please reopen if the problem exists in the new version.

+resolved

# Action History
- Created by: eklitzke | 2018-01-01T02:11:01+00:00
- Closed at: 2018-11-18T14:27:31+00:00
