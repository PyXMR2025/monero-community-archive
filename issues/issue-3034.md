---
title: '*BSD build instructions?'
source_url: https://github.com/monero-project/monero-gui/issues/3034
author: dchmelik
assignees: []
labels: []
created_at: '2020-08-02T04:57:22+00:00'
updated_at: '2023-11-04T02:01:42+00:00'
type: issue
status: closed
closed_at: '2022-03-16T19:53:35+00:00'
---

# Original Description
I see *BSD mentioned in the source code, but no instructions.  How would you build it on *BSD, such as FreeBSD 13-CURRENT?

# Discussion History
## selsta | 2020-08-07T09:55:36+00:00
I don’t think there are any instructions currently.

## selsta | 2022-03-16T19:53:35+00:00
None of the contributors use *BSD, so I will close this. If someone is able to build it I would appreciate a PR with instructions :)

## theoden8 | 2022-06-07T22:01:54+00:00
Using clang-13 on FreeBSD 13.1-RELEASE. Building master (v0.17.3.2)

Install these packages:

```
pkg install git cmake ccache boost-libs libzmq3 protobuf libsodium qt5 unbound
```

* It doesn't find `zmq_send_const`, change it to `zmq_send`.
* It complains about `el::base::debug::StackTrace` linkage errors referenced from `monero/src/common/stack_trace.cpp`-related object, make sure `monero/external/easylogging++/ea_config.h` defines `ELPP_FEATURE_CRASH_LOG`, otherwise `easylogging++.cpp` file won't compile implementations of most of its functions.

A party to make a PR would have to think through the above two problems in a bit more detail.

# Action History
- Created by: dchmelik | 2020-08-02T04:57:22+00:00
- Closed at: 2022-03-16T19:53:35+00:00
