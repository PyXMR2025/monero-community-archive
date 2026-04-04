---
title: segfault on exit in destructor
source_url: https://github.com/monero-project/monero-gui/issues/894
author: radfish
assignees: []
labels:
- bug
- resolved
created_at: '2017-09-28T04:02:05+00:00'
updated_at: '2018-11-18T15:18:31+00:00'
type: issue
status: closed
closed_at: '2018-11-18T15:18:31+00:00'
---

# Original Description
Arch Linux on x86_64. Current master: 4c75fe47f955603fd9faf416c0f06f942cb575ec
Built with Qt 5.9.1, openssl1-0.

```
Thread 1 "monero-wallet-q" received signal SIGSEGV, Segmentation fault.
0x00007ffff47060d4 in ?? () from /usr/lib/libQt5Qml.so.5
(gdb) bt all
No symbol "all" in current context.
(gdb) bt
#0  0x00007ffff47060d4 in ?? () from /usr/lib/libQt5Qml.so.5
#1  0x00007ffff407fef9 in QHashData::free_helper(void (*)(QHashData::Node*)) ()
   from /usr/lib/libQt5Core.so.5
#2  0x00007ffff4899de5 in QQmlOpenMetaObjectType::~QQmlOpenMetaObjectType() ()
   from /usr/lib/libQt5Qml.so.5
#3  0x00007ffff4899e1a in QQmlOpenMetaObjectType::~QQmlOpenMetaObjectType() ()
   from /usr/lib/libQt5Qml.so.5
#4  0x00007ffff4898d2e in QQmlOpenMetaObject::~QQmlOpenMetaObject() ()
   from /usr/lib/libQt5Qml.so.5
#5  0x00007ffff4978c54 in ?? () from /usr/lib/libQt5Qml.so.5
#6  0x00007ffff4238e4a in QObjectPrivate::~QObjectPrivate() () from /usr/lib/libQt5Core.so.5
#7  0x00007ffff4238eca in QObjectPrivate::~QObjectPrivate() () from /usr/lib/libQt5Core.so.5
#8  0x00007ffff4240f36 in QObject::~QObject() () from /usr/lib/libQt5Core.so.5
#9  0x00007ffff42412da in QObject::~QObject() () from /usr/lib/libQt5Core.so.5
#10 0x00007ffff497e30f in ?? () from /usr/lib/libQt5Qml.so.5
#11 0x00007ffff497e491 in ?? () from /usr/lib/libQt5Qml.so.5
#12 0x00007ffff497e4d9 in ?? () from /usr/lib/libQt5Qml.so.5
#13 0x00007ffff497e779 in QQmlListModel::~QQmlListModel() () from /usr/lib/libQt5Qml.so.5
#14 0x00007ffff48a6bcd in ?? () from /usr/lib/libQt5Qml.so.5
#15 0x00007ffff42372ad in QObjectPrivate::deleteChildren() () from /usr/lib/libQt5Core.so.5
#16 0x00007ffff4240eec in QObject::~QObject() () from /usr/lib/libQt5Core.so.5
#17 0x00007ffff5e0b5d7 in QQuickItem::~QQuickItem() () from /usr/lib/libQt5Quick.so.5
#18 0x00007ffff5e2697f in ?? () from /usr/lib/libQt5Quick.so.5
#19 0x00007ffff42372ad in QObjectPrivate::deleteChildren() () from /usr/lib/libQt5Core.so.5
#20 0x00007ffff4240eec in QObject::~QObject() () from /usr/lib/libQt5Core.so.5
#21 0x00007ffff5e0b5d7 in QQuickItem::~QQuickItem() () from /usr/lib/libQt5Quick.so.5
#22 0x00007ffff5e2697f in ?? () from /usr/lib/libQt5Quick.so.5
#23 0x00007ffff42372ad in QObjectPrivate::deleteChildren() () from /usr/lib/libQt5Core.so.5
#24 0x00007ffff4240eec in QObject::~QObject() () from /usr/lib/libQt5Core.so.5
#25 0x00007ffff5e0b5d7 in QQuickItem::~QQuickItem() () from /usr/lib/libQt5Quick.so.5
#26 0x00007ffff5e26847 in ?? () from /usr/lib/libQt5Quick.so.5
#27 0x00007ffff42372ad in QObjectPrivate::deleteChildren() () from /usr/lib/libQt5Core.so.5
#28 0x00007ffff4240eec in QObject::~QObject() () from /usr/lib/libQt5Core.so.5
#29 0x00007ffff5e18227 in QQuickWindow::~QQuickWindow() () from /usr/lib/libQt5Quick.so.5
#30 0x00007ffff5ece2cc in ?? () from /usr/lib/libQt5Quick.so.5
#31 0x00007ffff4932f36 in QQmlApplicationEnginePrivate::cleanUp() ()
   from /usr/lib/libQt5Qml.so.5
#32 0x00007ffff4932fba in QQmlApplicationEngine::~QQmlApplicationEngine() ()
   from /usr/lib/libQt5Qml.so.5
#33 0x00005555555c3e30 in ?? ()
#34 0x00007ffff30dbf6a in __libc_start_main () from /usr/lib/libc.so.6
#35 0x00005555555cc45a in ?? ()

```

# Discussion History
## dEBRUYNE-1 | 2017-10-16T19:06:00+00:00
+bug

## dEBRUYNE-1 | 2017-10-27T13:44:46+00:00
Can you try v0.11.1.0?

## erciccione | 2018-11-18T13:57:04+00:00
Related to old version. Can be reopened if still valid for 0.13.0.4

+resolved

# Action History
- Created by: radfish | 2017-09-28T04:02:05+00:00
- Closed at: 2018-11-18T15:18:31+00:00
