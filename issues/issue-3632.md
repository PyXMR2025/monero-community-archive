---
title: 'release-v0.12 error: ''conceal_derivation'' overrides a member function'
source_url: https://github.com/monero-project/monero/issues/3632
author: m2049r
assignees: []
labels: []
created_at: '2018-04-13T20:27:20+00:00'
updated_at: '2018-04-30T21:27:13+00:00'
type: issue
status: closed
closed_at: '2018-04-30T21:27:13+00:00'
---

# Original Description
```C
-- Build files have been written to: /opt/android/monero/build/release.arm
Scanning dependencies of target obj_device
[  0%] Building CXX object src/device/CMakeFiles/obj_device.dir/device.cpp.o
In file included from /opt/android/monero/src/device/device.cpp:31:
/opt/android/monero/src/device/device_default.hpp:96:19: error: 'conceal_derivation' overrides a member function
      but is not marked 'override' [-Werror,-Winconsistent-missing-override]
            bool  conceal_derivation(crypto::key_derivation &derivation, const crypto::public_key &tx_pub...
                  ^
/opt/android/monero/src/device/device.hpp:148:23: note: overridden virtual function is here
        virtual bool  conceal_derivation(crypto::key_derivation &derivation, const crypto::public_key &tx...
                      ^
1 error generated.
```

# Discussion History
## m2049r | 2018-04-13T20:36:28+00:00
introduced in commit d481410

## moneromooo-monero | 2018-04-13T21:19:53+00:00
If this compiler is going to need override every time a function is overridden, it'll be unsupported.
What compiler is that ? Does it moan about other places where this happens ? This one's a one off so OK to change, but if it's all of them, it can go to hell.

## moneromooo-monero | 2018-04-13T21:23:33+00:00
And does https://github.com/moneromooo-monero/bitmonero/tree/conceal-0.12 fix it (for the whole codebase) ?

## vtnerd | 2018-04-14T05:05:53+00:00
Its a warning flag that can be disabled. Its enabled by `-Wall`. Its triggering because as the name suggests, `override` is used in other places in the class, but not in all possible places. I suggested adding the `override` keyword in the review because the design had base implementations for every virtual method. If the signature changes in one of the functions, the code will still compile but the derived implementation will never be called (because its declaring a new virtual method in the derived class). Arguably, its better to never have a default implementation for a virtual function (like classes in wallet2_api.h), which would've been my preferred proposal if I had done the review earlier. In fact, I think I did propose that, but it was probably too much of an edit for the author at the time.



## vtnerd | 2018-04-14T05:10:42+00:00
Correction: It looks like the base class is all pure virtual methods, so the override keyword provides less utility here. I would still recommend it (I usually mark  everything as `override final` where possible), but the situation isn't as bad as I described. Did @m2049r change this, or was I mistaken about the original PR?

## m2049r | 2018-04-14T06:22:23+00:00
@moneromooo-monero this is the only place this happens. compiler is Clang 5.0.300080

>  And does https://github.com/moneromooo-monero/bitmonero/tree/conceal-0.12 fix it (for the whole codebase) ?

yes, it does.

## moneromooo-monero | 2018-04-14T09:03:54+00:00
OK, if it only moans when override is partly used, then it's fine. I'll PR that change then, thanks.

# Action History
- Created by: m2049r | 2018-04-13T20:27:20+00:00
- Closed at: 2018-04-30T21:27:13+00:00
