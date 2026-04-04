---
title: Make doesn't find zeromq on fedora
source_url: https://github.com/monero-project/monero/issues/3034
author: lhirlimann
assignees: []
labels: []
created_at: '2017-12-30T12:58:30+00:00'
updated_at: '2017-12-30T13:14:20+00:00'
type: issue
status: closed
closed_at: '2017-12-30T13:14:20+00:00'
---

# Original Description
-- Found Boost Version: 106400
-- Found Readline: /usr/include  
-- Performing Test GNU_READLINE_FOUND
-- Performing Test GNU_READLINE_FOUND - Success
-- Found readline library at: /usr
CMake Error at CMakeLists.txt:729 (message):
  Could not find required header zmq.hpp


-- Configuring incomplete, errors occurred!
See also "/home/ludo/src/monero/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/ludo/src/monero/build/release/CMakeFiles/CMakeError.log".
make: *** [Makefile:65: release-all] Error 1
[ludo@Oulanl monero]$ vi /home/ludo/src/monero/build/release/CMakeFiles/CMakeOutput.log
[ludo@Oulanl monero]$ rpm -qa |grep zero
zeromq-devel-4.1.6-2.fc26.x86_64
zeromq-4.1.6-2.fc26.x86_64
[ludo@Oulanl monero]$
[CMakeError.log](https://github.com/monero-project/monero/files/1594387/CMakeError.log)
[CMakeOutput.log](https://github.com/monero-project/monero/files/1594388/CMakeOutput.log)


# Discussion History
## lhirlimann | 2017-12-30T13:04:31+00:00
[ludo@Oulanl monero]$ rpm -ql zeromq-devel-4.1.6-2.fc26.x86_64
/usr/include/zmq.h
/usr/include/zmq_utils.h
/usr/lib64/libzmq.so
/usr/lib64/pkgconfig/libzmq.pc

## moneromooo-monero | 2017-12-30T13:10:22+00:00
Do you have zmq.hpp installed ?

## lhirlimann | 2017-12-30T13:14:20+00:00
cppzmq-devel was my missing package.

# Action History
- Created by: lhirlimann | 2017-12-30T12:58:30+00:00
- Closed at: 2017-12-30T13:14:20+00:00
