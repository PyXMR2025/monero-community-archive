---
title: 'ArchARM RPi: messages_map.hpp:47:10: fatal error: messages/messages.pb.h:
  No such file or directory'
source_url: https://github.com/monero-project/monero/issues/4822
author: moneroexamples
assignees: []
labels: []
created_at: '2018-11-08T01:03:27+00:00'
updated_at: '2018-11-22T19:09:33+00:00'
type: issue
status: closed
closed_at: '2018-11-09T21:35:27+00:00'
---

# Original Description
```
[ 42%] Building CXX object src/device_trezor/CMakeFiles/obj_device_trezor.dir/device_trezor.cpp.o
In file included from /home/mwo/monero/src/device_trezor/trezor/transport.hpp:49,
                 from /home/mwo/monero/src/device_trezor/trezor.hpp:36,
                 from /home/mwo/monero/src/device_trezor/device_trezor.hpp:43,
                 from /home/mwo/monero/src/device_trezor/device_trezor.cpp:30:
/home/mwo/monero/src/device_trezor/trezor/messages_map.hpp:47:10: fatal error: messages/messages.pb.h: No such file or directory                                                                                 
 #include "messages/messages.pb.h"
          ^~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
make[3]: *** [src/device_trezor/CMakeFiles/obj_device_trezor.dir/build.make:63: src/device_trezor/CMakeFiles/obj_device_trezor.dir/device_trezor.cpp.o] Error 1                                                  
make[3]: Leaving directory '/home/mwo/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:3540: src/device_trezor/CMakeFiles/obj_device_trezor.dir/all] Error 2
make[2]: Leaving directory '/home/mwo/monero/build/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/home/mwo/monero/build/release'
make: *** [Makefile:95: release-all] Error 2
```

It fails becasue https://github.com/monero-project/monero/tree/master/src/device_trezor/trezor/messages is empty. 

All compiles well on normal arch, so don't know at present why Arch ARM for Raspberry Pi fails. Any ideas?

# Discussion History
## moneromooo-monero | 2018-11-08T08:36:11+00:00
Is the build log complaining about not finding "protoc" earlier ?

## moneroexamples | 2018-11-08T11:42:09+00:00
Haven't seen any such message. But Im rebuilding again. It takes ages on RPi2, so will know more in few hours.

## moneroexamples | 2018-11-09T21:35:27+00:00
`python-protobuf` was missing. Its interesting because I don't have it installed on my regular arch. 

Anyway, maybe its good time to actually revisit https://github.com/monero-project/monero#dependencies , as I wanted to provide one liners for fedora and arch as well, and update the table since, e.g., hidapi, is missing from dependencies. 

## jtgrassie | 2018-11-20T16:55:12+00:00
This should probably be reopened. It not only creates a dependency of python-protobuf, but also python 3. Without both these dependencies, builds can fail.

## moneroexamples | 2018-11-20T23:17:40+00:00
I don't have `python-protobuf` on my arch, and build works for me. I only encountered this issue on archarm. On regular arch I have:

```
yay -Qs protobuf
local/protobuf 3.6.1-1
    Protocol Buffers - Google's data interchange format
local/protobuf-c 1.3.1-1
    Protocol Buffers implementation in C
```

## jtgrassie | 2018-11-21T01:35:00+00:00
I was getting build errors on OSX because the default python was 2.7 and trezor cmake requires 3+ and the python protobuf bindings. Easy enough to work around but a default compile should not try to build in non-essential code (trezor in this case) if it cannot meet the requirements. That's why I wanted this issue open again, to remind me to have a look at fixing the trezor cmake file for the case I was encountering.

## jtgrassie | 2018-11-21T01:49:39+00:00
```
CMake Warning at src/device_trezor/CMakeLists.txt:79 (message):
  Trezor protobuf messages could not be regenerated (err=No such file or
  directory, python ).OUT: , ERR: .Please read
  src/device_trezor/trezor/tools/README.md

```

Followed by a bunch of undefined errors later during build:
```
[ 53%] Linking CXX executable ../../bin/monero-wallet-rpc
Undefined symbols for architecture x86_64:
  "hw::trezor::MessageMapper::get_message_wire_number(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&)", referenced from:
...
  "hw::trezor::device_trezor_base::disconnect()", referenced from:
      hw::trezor::device_trezor::~device_trezor() in libdevice_trezor.a(device_trezor.cpp.o)
```

Which is happening because the trezor cmake file is still trying to compile and link device_trezor.cpp even though the protobuf messages failed to be generated.


## moneroexamples | 2018-11-21T01:54:04+00:00
I had the same issue. Though I don't understand why python-protobuf is required. Is it fallback? 

## jtgrassie | 2018-11-21T02:01:42+00:00
No it seems a requirement. Both python3 and python-protobuf. The cmake file is the issue though - it should just disable trezor support when trezor dependencies are not met.

## jtgrassie | 2018-11-21T02:03:55+00:00
Looks like this is fixed in #4839

## ph4r05 | 2018-11-21T12:59:02+00:00
It should be fixed also in the earlier, already approved PR #4824. Can you give it a try?

## ph4r05 | 2018-11-21T13:08:03+00:00
Anyway, assuming #4824 - There is no `python-protobuf` dependency. CMake check is now more robust. If message generation fails Trezor is not compiled.

In order to compile Trezor the protobuf library is needed (`libprotobuf-dev` on Ubuntu) and simple Python3. The #4824 also enables to use Python2 for the compilation if no Py3 is present:

```bash
export PYTHON3=python
pip install backports.tempfile
```

## jtgrassie | 2018-11-21T14:01:32+00:00
#4824 doesn't address properly. The later #4839 does.

## ph4r05 | 2018-11-21T14:02:14+00:00
> #4824 doesn't address properly. The later #4839 does.

How come? Is the build failing for you if there is a problem with missing protobuf?

## jtgrassie | 2018-11-21T14:39:10+00:00
#4824 was not picking up python. #4839 resolves.

## ph4r05 | 2018-11-22T19:09:32+00:00
#4824 is updated so it contains the full fix.

# Action History
- Created by: moneroexamples | 2018-11-08T01:03:27+00:00
- Closed at: 2018-11-09T21:35:27+00:00
