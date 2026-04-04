---
title: tautological-constant-out-of-range-compare as error on clang targeting android
source_url: https://github.com/monero-project/monero/issues/2713
author: danrmiller
assignees: []
labels: []
created_at: '2017-10-23T04:18:42+00:00'
updated_at: '2017-11-14T19:48:33+00:00'
type: issue
status: closed
closed_at: '2017-11-14T19:48:33+00:00'
---

# Original Description
https://build.getmonero.org/builders/monero-android-armv7/builds/489/steps/compile/logs/stdio

Cross-compiling for android-armv7 target

On irc @hyc and @moneromooo-monero told me  some places to disable checks for this behavior which isn't an "error" in this usage, but then there was talk about only disabling the check for this function because the diagnostic could point out a bug or something useful elsewhere. I got caught up doing something else and I can't find their suggestions, so I'm posting an issue here.

```
In file included from /home/vagrant/slave/monero-android-armv7/build/src/cryptonote_basic/miner.cpp:43:
In file included from /home/vagrant/slave/monero-android-armv7/build/contrib/epee/include/storages/portable_storage_template_helper.h:32:
In file included from /home/vagrant/slave/monero-android-armv7/build/contrib/epee/include/storages/portable_storage.h:33:
/home/vagrant/slave/monero-android-armv7/build/contrib/epee/include/storages/portable_storage_to_bin.h:66:40: error: comparison of constant 4611686018427387903 with expression of type 'size_t' (aka 'unsigned int') is always true [-Werror,-Wtautological-constant-out-of-range-compare]
        CHECK_AND_ASSERT_THROW_MES(val <= 4611686018427387903, "failed to pack varint - too big amount = " << val);
                                   ~~~ ^  ~~~~~~~~~~~~~~~~~~~
/home/vagrant/slave/monero-android-armv7/build/contrib/epee/include/misc_log_ex.h:172:57: note: expanded from macro 'CHECK_AND_ASSERT_THROW_MES'
#define CHECK_AND_ASSERT_THROW_MES(expr, message) {if(!(expr)) ASSERT_MES_AND_THROW(message);}
                                                        ^~~~
1 error generated.
```

# Discussion History
## moneromooo-monero | 2017-10-28T10:54:00+00:00
https://github.com/moneromooo-monero/bitmonero/tree/tauto might work, I'm not sure whether this will trigger for CLANG or whether the system needs to be different.

## stoffu | 2017-10-29T02:54:44+00:00
How about something like this?
```c++
CHECK_AND_ASSERT_THROW_MES(sizeof(val) < 8 || val <= 4611686018427387903, "failed to pack varint - too big amount = " << val);
```
I don't know how to compile it on android-armv7 so I'm not sure if this eliminates the error.

## danrmiller | 2017-10-30T18:37:45+00:00
moneromooo-monero's tauto branch works. Thanks.

## moneromooo-monero | 2017-10-31T10:35:46+00:00
Thanks, https://github.com/monero-project/monero/pull/2743 now

## moneromooo-monero | 2017-11-14T19:41:59+00:00
+resolved

# Action History
- Created by: danrmiller | 2017-10-23T04:18:42+00:00
- Closed at: 2017-11-14T19:48:33+00:00
