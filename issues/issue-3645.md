---
title: FreeBSD building error
source_url: https://github.com/monero-project/monero/issues/3645
author: monerorus
assignees: []
labels: []
created_at: '2018-04-15T16:45:28+00:00'
updated_at: '2018-06-20T09:09:05+00:00'
type: issue
status: closed
closed_at: '2018-06-20T09:09:05+00:00'
---

# Original Description
```
[ 95%] Building CXX object src/daemon/CMakeFiles/daemon.dir/rpc_command_executor.cpp.o
[ 95%] Linking CXX executable ../../bin/monerod
/usr/bin/ld: /usr/local/lib/libminiupnpc.a(miniupnpc.c.o): relocation R_X86_64_32S against `IGDstartelt' can not be used when making a shared object; recompile with -fPIC
/usr/local/lib/libminiupnpc.a: could not read symbols: Bad value
c++: error: linker command failed with exit code 1 (use -v to see invocation)
```
any ideas?

# Discussion History
## danrmiller | 2018-04-15T16:53:37+00:00
You need to recompile miniupnpc with CFLAGS="-fPIC" CPPFLAGS="-fPIC" (I actually think CPPFLAGS also affects CFLAGS, but it  won't hurt this way). If you just remove the system lib monero will use the copy included with its source and build it position independent.

## monerorus | 2018-04-22T17:03:36+00:00
pull last source and get this error:
```
[ 96%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_blackball.dir/blockchain_blackball.cpp.o
/monero/src/blockchain_utilities/blockchain_blackball.cpp:173:9: error: return type 'basic_string<[3 * ...]>' must match previous return
      type 'const basic_string<[3 * ...]>' when lambda expression has unspecified explicit return type
        return val;
        ^
In file included from /monero/src/blockchain_utilities/blockchain_blackball.cpp:33:
In file included from /monero/src/cryptonote_core/tx_pool.h:44:
In file included from /monero/src/cryptonote_basic/cryptonote_basic_impl.h:33:
In file included from /monero/src/cryptonote_basic/cryptonote_basic.h:41:
/monero/src/serialization/binary_archive.h:194:28: warning: shift count >= width of type [-Wshift-count-overflow]
      if (1 < sizeof(T)) v >>= 8;
                           ^   ~
/monero/src/serialization/binary_archive.h:187:5: note: in instantiation of function template specialization
      'binary_archive<true>::serialize_uint<unsigned char>' requested here
    serialize_uint(static_cast<typename boost::make_unsigned<T>::type>(v));
    ^
/monero/src/serialization/binary_archive.h:227:5: note: in instantiation of function template specialization
      'binary_archive<true>::serialize_int<unsigned char>' requested here
    serialize_int(t);
    ^
1 warning and 1 error generated.
*** Error code 1

Stop.
make[2]: stopped in /monero
*** Error code 1

Stop.
make[1]: stopped in /monero
*** Error code 1

Stop.
make: stopped in /monero
```


## rockhouse | 2018-06-04T10:14:16+00:00
@monerorus you can check my PR and add the `const` yourself for now

## monerorus | 2018-06-06T14:41:54+00:00
@rockhouse thx. I solve it already. @jbeich make patch for this in freebsd port (net-p2p/monero-cli).
my problem now is:
```
[ 81%] Linking CXX executable unit_tests
/usr/bin/ld: ../gtest/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32S against `a local symbol' can not be used when making a shared object; recompile with -fPIC
../gtest/libgtest.a: could not read symbols: Bad value
c++: error: linker command failed with exit code 1 (use -v to see invocation)
*** Error code 1

```
when i'm build from source.

## jbeich | 2018-06-06T15:06:46+00:00
@monerorus, better ask @vasild (downstream maintainer). I don't use Monero but according to downstream build logs `unit_tests` aren't built.
http://beefy5.nyi.freebsd.org/data/104i386-default/470749/logs/monero-cli-0.12.0.0_2.log
http://beefy6.nyi.freebsd.org/data/104amd64-default/470749/logs/monero-cli-0.12.0.0_2.log
http://beefy9.nyi.freebsd.org/data/111amd64-default/470749/logs/monero-cli-0.12.0.0_2.log
http://beefy10.nyi.freebsd.org/data/111i386-default/470749/logs/monero-cli-0.12.0.0_2.log
http://beefy11.nyi.freebsd.org/data/head-i386-default/p470749_s333820/logs/monero-cli-0.12.0.0_2.log
http://beefy12.nyi.freebsd.org/data/head-amd64-default/p470749_s333820/logs/monero-cli-0.12.0.0_2.log


## vasild | 2018-06-07T11:11:10+00:00
Hey,

I have upgraded the FreeBSD port `net-p2p/monero-cli` to the latest released version (0.12.2.0). The patches that need to be applied are (as usual) in the `files/` subdirectory: https://svnweb.freebsd.org/ports/head/net-p2p/monero-cli/files/

Also, I made is easy to compile an arbitrary git commit via the port (see the beginning of the port's Makefile). Latest HEAD (8a7b3ff13) also compiles.

Hope this helps!

## moneromooo-monero | 2018-06-20T08:57:16+00:00
The return value error is now fixed, and the -fPIC things aren't bugs, closing.

+resolved

# Action History
- Created by: monerorus | 2018-04-15T16:45:28+00:00
- Closed at: 2018-06-20T09:09:05+00:00
