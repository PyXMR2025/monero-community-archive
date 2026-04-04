---
title: translation_header android
source_url: https://github.com/monero-project/monero/issues/4291
author: takelberry41
assignees: []
labels: []
created_at: '2018-08-22T07:59:51+00:00'
updated_at: '2018-08-24T09:38:09+00:00'
type: issue
status: closed
closed_at: '2018-08-24T09:38:09+00:00'
---

# Original Description
i'm trying to build for android arm64 v8a without docker but no luck until now.
no problem on windows or linux.
any suggestion?

Scanning dependencies of target generate_translations_header
Scanning dependencies of target genversion
[  0%] Creating directories for 'generate_translations_header'
[  1%] Generating ../version.cpp
Scanning dependencies of target easylogging
Scanning dependencies of target lmdb
-- You are currently on commit db26776a
Scanning dependencies of target libminiupnpc-static
[  1%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
-- The most recent tag was at e2c39f6b
-- You are ahead of or behind a tagged release
[  2%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
[  2%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o
[  2%] Built target genversion
[  3%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.o
[  4%] No download step for 'generate_translations_header'
[  4%] No patch step for 'generate_translations_header'
[  4%] No update step for 'generate_translations_header'
[  5%] Performing configure step for 'generate_translations_header'
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.o
[  5%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.o
[  6%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
-- The C compiler identification is Clang 3.8.275480
Scanning dependencies of target obj_cncrypto
[  6%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
-- The CXX compiler identification is Clang 3.8.275480
-- Check for working C compiler: /opt/android/toolchain-arm/bin/clang
[  6%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniwget.c.o
-- Check for working C compiler: /opt/android/toolchain-arm/bin/clang -- works
-- Detecting C compiler ABI info
Scanning dependencies of target obj_ringct_basic
Scanning dependencies of target obj_ringct
Scanning dependencies of target unbound
Scanning dependencies of target obj_device
[  6%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.o
[  6%] Building C object external/unbound/CMakeFiles/unbound.dir/services/authzone.c.o
-- Detecting C compiler ABI info - done
[  7%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
[  8%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpcommands.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/services/authzone.c:44:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[  9%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
-- Detecting C compile features
[  9%] Building CXX object src/device/CMakeFiles/obj_device.dir/device.cpp.o
[  9%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpdev.c.o
Scanning dependencies of target obj_checkpoints
[  9%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpreplyparse.c.o
[  9%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.o
[ 10%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnperrors.c.o
[ 11%] Building CXX object src/checkpoints/CMakeFiles/obj_checkpoints.dir/checkpoints.cpp.o
-- Detecting C compile features - done
-- Check for working CXX compiler: /opt/android/toolchain-arm/bin/clang++
[ 11%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/connecthostport.c.o
[ 11%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
[ 12%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/portlistingparse.c.o
-- Check for working CXX compiler: /opt/android/toolchain-arm/bin/clang++ -- works
-- Detecting CXX compiler ABI info
[ 13%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
[ 13%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/receivedata.c.o
[ 13%] Linking C static library libminiupnpc.a
-- Detecting CXX compiler ABI info - done
[ 13%] Built target libminiupnpc-static
[ 13%] Building CXX object src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Warning at CMakeLists.txt:38 (message):
  lrelease program not found, translation files not built


-- Configuring done
-- Generating done
-- Build files have been written to: /opt/android/monero-gui/monero/build/release/translations
[ 13%] Performing build step for 'generate_translations_header'
Scanning dependencies of target generate_translations_header
[ 50%] Building C object CMakeFiles/generate_translations_header.dir/generate_translations_header.c.o
[100%] Linking C executable generate_translations_header
Generating embedded translations header
./generate_translations_header: 1: ./generate_translations_header: ELF·p@@š@8@@@@@@ÈÈ@È@@@ffAA00A0Aàààà@à@Qåtd/system/bin/linker64Androidr143770861
: not found
./generate_translations_header: 2: ./generate_translations_header: ^è@ªñÿAc
A?@MñÿAuñÿA@}: not found
./generate_translations_header: 1: ./generate_translations_header: @libdl.solibc.sofprintffgetcfopen__libc_init__cxa_atexitfclose_edata__bss_start_endmain__PREINIT_ARRAY____end____FINI_ARRAY____bss_start____INIT_ARRAY____bss_end__LIBC: not found
./generate_translations_header: 2: ./generate_translations_header: c
µA: not found
./generate_translations_header: 3: ./generate_translations_header: P@2A: not found
./generate_translations_header: 3: ./generate_translations_header: Syntax error: Unterminated quoted string
make[5]: *** [generate_translations_header] Error 2
make[5]: *** Deleting file `generate_translations_header'
make[4]: *** [CMakeFiles/generate_translations_header.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [generate_translations_header-prefix/src/generate_translations_header-stamp/generate_translations_header-build] Error 2
make[1]: *** [CMakeFiles/generate_translations_header.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 13%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.o
[ 13%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[ 14%] Linking C static library liblmdb.a
[ 14%] Built target lmdb
[ 15%] Building C object src/ringct/CMakeFiles/obj_ringct_basic.dir/rctCryptoOps.c.o
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
1 warning generated.
[ 17%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/dns.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/services/cache/dns.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 17%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
[ 17%] Building CXX object src/ringct/CMakeFiles/obj_ringct_basic.dir/bulletproofs.cc.o
[ 18%] Building CXX object src/device/CMakeFiles/obj_device.dir/device_default.cpp.o
1 warning generated.
[ 18%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/infra.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/services/cache/infra.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 18%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/rrset.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/services/cache/rrset.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 20%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/dname.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/data/dname.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 20%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
1 warning generated.
[ 20%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgencode.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/data/msgencode.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 21%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
[ 21%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
[ 22%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
[ 22%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgparse.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/data/msgparse.c:39:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 23%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/msgreply.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/data/msgreply.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 23%] Building CXX object src/device/CMakeFiles/obj_device.dir/log.cpp.o
[ 24%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
[ 24%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
1 warning generated.
[ 24%] Building C object external/unbound/CMakeFiles/unbound.dir/util/data/packed_rrset.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/data/packed_rrset.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 25%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iterator.c.o
1 warning generated.
In file included from /opt/android/monero-gui/monero/external/unbound/iterator/iterator.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 25%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_delegpt.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/iterator/iter_delegpt.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 26%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_donotq.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/iterator/iter_donotq.c:44:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 26%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
1 warning generated.
[ 26%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_fwd.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/iterator/iter_fwd.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 27%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
1 warning generated.
[ 28%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_hints.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/iterator/iter_hints.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 28%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_priv.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/iterator/iter_priv.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 28%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_resptype.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/iterator/iter_resptype.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 29%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_scrub.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/iterator/iter_scrub.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 29%] Building C object external/unbound/CMakeFiles/unbound.dir/iterator/iter_utils.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/iterator/iter_utils.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 30%] Building C object external/unbound/CMakeFiles/unbound.dir/respip/respip.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/respip/respip.c:12:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 30%] Building C object external/unbound/CMakeFiles/unbound.dir/services/listen_dnsport.c.o
1 warning generated.
In file included from /opt/android/monero-gui/monero/external/unbound/services/listen_dnsport.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 30%] Building C object external/unbound/CMakeFiles/unbound.dir/services/localzone.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/services/localzone.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 31%] Building C object external/unbound/CMakeFiles/unbound.dir/services/mesh.c.o
1 warning generated.
[ 31%] Building C object external/unbound/CMakeFiles/unbound.dir/services/modstack.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/services/mesh.c:45:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/services/modstack.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outbound_list.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/services/outbound_list.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/services/outside_network.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/services/outside_network.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 32%] Building C object external/unbound/CMakeFiles/unbound.dir/services/view.c.o
1 warning generated.
[ 33%] Building C object external/unbound/CMakeFiles/unbound.dir/util/alloc.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/services/view.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/util/alloc.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 33%] Building C object external/unbound/CMakeFiles/unbound.dir/util/as112.c.o
1 warning generated.
[ 34%] Building C object external/unbound/CMakeFiles/unbound.dir/util/config_file.c.o
[ 34%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configlexer.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/config_file.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/util/configlexer.c:1:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/configparser.c.o
In file included from ./util/configparser.y:39:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/fptr_wlist.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/fptr_wlist.c:46:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 35%] Building C object external/unbound/CMakeFiles/unbound.dir/util/locks.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/locks.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 36%] Building C object external/unbound/CMakeFiles/unbound.dir/util/log.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/log.c:40:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 36%] Building C object external/unbound/CMakeFiles/unbound.dir/util/mini_event.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/mini_event.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 37%] Building C object external/unbound/CMakeFiles/unbound.dir/util/module.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/module.c:40:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 37%] Building C object external/unbound/CMakeFiles/unbound.dir/util/netevent.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/netevent.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 37%] Building C object external/unbound/CMakeFiles/unbound.dir/util/net_help.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/net_help.c:40:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/util/random.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/random.c:60:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 38%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rbtree.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/rbtree.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 40%] Building C object external/unbound/CMakeFiles/unbound.dir/util/regional.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/regional.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
1 warning generated.
[ 40%] Building C object external/unbound/CMakeFiles/unbound.dir/util/rtt.c.o
[ 40%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/dnstree.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/rtt.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/util/storage/dnstree.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 41%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lookup3.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/storage/lookup3.c:48:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 41%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/lruhash.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/storage/lruhash.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 42%] Building C object external/unbound/CMakeFiles/unbound.dir/util/storage/slabhash.c.o
1 warning generated.
[ 42%] Building C object external/unbound/CMakeFiles/unbound.dir/util/timehist.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/storage/slabhash.c:45:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/util/timehist.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 43%] Building C object external/unbound/CMakeFiles/unbound.dir/util/tube.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/tube.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
1 warning generated.
[ 43%] Building C object external/unbound/CMakeFiles/unbound.dir/util/ub_event.c.o
[ 43%] Building C object external/unbound/CMakeFiles/unbound.dir/util/winsock_event.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/util/ub_event.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/util/winsock_event.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 44%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/autotrust.c.o
[ 44%] Built target obj_ringct_basic
[ 44%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_anchor.c.o
1 warning generated.
In file included from /opt/android/monero-gui/monero/external/unbound/validator/autotrust.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/validator.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/validator/val_anchor.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/validator/validator.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kcache.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/validator/val_kcache.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 45%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_kentry.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/validator/val_kentry.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 46%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_neg.c.o
1 warning generated.
[ 46%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/validator/val_neg.c:44:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 47%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
[ 47%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec3.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/validator/val_nsec3.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_nsec.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/validator/val_nsec.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_secalgo.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/validator/val_secalgo.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 48%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_sigcrypt.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/validator/val_sigcrypt.c:43:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 49%] Building C object external/unbound/CMakeFiles/unbound.dir/validator/val_utils.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/validator/val_utils.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 49%] Building C object external/unbound/CMakeFiles/unbound.dir/dns64/dns64.c.o
[ 50%] Linking CXX static library libeasylogging.a
In file included from /opt/android/monero-gui/monero/external/unbound/dns64/dns64.c:42:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 51%] Building C object external/unbound/CMakeFiles/unbound.dir/testcode/checklocks.c.o
[ 51%] Built target easylogging
[ 51%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/keyraw.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/testcode/checklocks.c:36:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/sldns/keyraw.c:13:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 52%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/sbuffer.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/sldns/sbuffer.c:14:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 52%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/wire2str.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/sldns/wire2str.c:17:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
1 warning generated.
[ 52%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parse.c.o
[ 53%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/parseutil.c.o
[ 53%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/rrdef.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/sldns/parse.c:10:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/sldns/parseutil.c:15:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/sldns/str2wire.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/sldns/rrdef.c:15:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/sldns/str2wire.c:14:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/explicit_bzero.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/compat/explicit_bzero.c:6:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
1 warning generated.
[ 54%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/reallocarray.c.o
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/compat/getentropy_linux.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/compat/reallocarray.c:18:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
In file included from /opt/android/monero-gui/monero/external/unbound/compat/getentropy_linux.c:19:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 55%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/context.c.o
1 warning generated.
In file included from /opt/android/monero-gui/monero/external/unbound/libunbound/context.c:41:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
[ 56%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/libunbound.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/libunbound/libunbound.c:47:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
[ 56%] Building C object external/unbound/CMakeFiles/unbound.dir/libunbound/libworker.c.o
In file included from /opt/android/monero-gui/monero/external/unbound/libunbound/libworker.c:44:
/opt/android/monero-gui/monero/build/release/external/unbound/config.h:446:9: warning: 'HAVE_STRPTIME' macro redefined [-Wmacro-redefined]
#define HAVE_STRPTIME
        ^
<command line>:5:9: note: previous definition is here
#define HAVE_STRPTIME 1
        ^
1 warning generated.
1 warning generated.
[ 56%] Built target obj_device
[ 56%] Built target obj_cncrypto
1 warning generated.
1 warning generated.
1 warning generated.
1 warning generated.
[ 56%] Linking C static library libunbound.a
[ 56%] Built target unbound
[ 56%] Built target obj_ringct
[ 56%] Built target obj_checkpoints
make: *** [all] Error 2

# Discussion History
## moneromooo-monero | 2018-08-22T10:00:16+00:00
What is the output of: file build/release/translations/generate_translations_header

## takelberry41 | 2018-08-22T21:32:37+00:00
There is nowhere this file....

## moneromooo-monero | 2018-08-22T21:51:56+00:00
It's run in the log you pasted. Look for generate_translations_header elsewhere in the build tree:

 Generating embedded translations header
./generate_translations_header: 1: ./generate_translations_header: �ELF����·�p�@@š�@8�@����@@@@@�������È�È�@È�@�����@@f�f������A�A�������0�0�A0�Aà�à����à�à�@à�@���Qåtd��/system/bin/linker64���Android�r143770861����

## MoroccanMalinois | 2018-08-22T21:55:46+00:00
duplicate #3056 ?

## takelberry41 | 2018-08-22T22:06:43+00:00
i swear there is not.
i double checked!

i dont think is 3056 because recognize correct cross-compiler.

## takelberry41 | 2018-08-22T22:08:30+00:00
maybe is smth connected with  boost_locale.
boost_locale need icu,iconv and i think is not cross compiled 

not   sure...

## MoroccanMalinois | 2018-08-22T22:16:11+00:00
> boost_locale need icu,iconv and i think is not cross compiled

It needs one of the two (ICU is harder to deal with), and weirdly, if you add '--with-local' to boost compilation and it doesn't find ICU or iconv, it will simply not build it, without showing any error

## takelberry41 | 2018-08-22T22:23:20+00:00
i tried to compile https://github.com/pelya/libiconv-libicu-android
but failed.

generally until now is not possible to cross compile boost_locale for android.

but is that the problem or is smth else?

## takelberry41 | 2018-08-22T22:24:39+00:00
and the most strange is that there is no official android version.

## SRCoughlin | 2018-08-22T22:25:44+00:00
I've been having trouble with that library too and haven't gotten ICU to build on Arm. There's a few posts on StackExchange that give pointers but they're missing important details. I'm very interested if you figure this out. 

## SRCoughlin | 2018-08-22T22:32:43+00:00
@takelberry41 There's a response to [this StackOverflow post](https://stackoverflow.com/questions/46703505/how-to-build-boostlocale-for-android) but when I follow the steps nothing improves. Perhaps you'll have better results.

## MoroccanMalinois | 2018-08-22T22:35:25+00:00
I successfully built ICU using this [guidelines](https://gist.github.com/DanielSerdyukov/188d47e29150622352f1) (except using clang, libc++ and latest version of NDK) (have to do a native build first) but failed to have boost recognize it. boost_locale builds fine with iconv.

@takelberry41 for me, your problem definitely looks like #3056; i.e. generating arm binary and running it in x86 system


## takelberry41 | 2018-08-22T22:51:01+00:00
i dont understand "generating arm binary and running it in x86 system"
because i run  make and cmake with CC=clang CXX=clang++
so code is compiled with right  compiler or is not enough??

## MoroccanMalinois | 2018-08-22T23:07:04+00:00
`CC=clang` is just for instructing cmake to use `clang` and not `gcc`. 

Your global `$PATH` is configured so that it will pick "/opt/android/toolchain-arm/bin/clang" which by default targets `Android`.

Android ([ARM](https://en.wikipedia.org/wiki/ARM_architecture)) and your system(most probably [x86](https://en.wikipedia.org/wiki/X86)) have different processor architectures. Binaries are not compatible between them; i.e. when you build for Android, you are building binaries that cannot run in your local system. During the build process of Monero, there is a generated binary (generate_translations_header) that needs to run locally, hence problems.

## takelberry41 | 2018-08-22T23:13:31+00:00
ah got it generate_translations_header is arm binary!!!

why generate_translations_header is not created at all

so is not running


## MoroccanMalinois | 2018-08-22T23:17:39+00:00
https://github.com/monero-project/monero/pull/4294/files ;)

## takelberry41 | 2018-08-22T23:47:22+00:00

almost same

https://pastebin.com/AYKvcKDw

## takelberry41 | 2018-08-23T14:01:36+00:00
back.

docker on arm7 succeed so latest commits works!!

things to do is changing 64dockerfile.

i'll try.

things started because i was lazzy to work with docker and arm binary wont execute on x64 linux!

so was note boost_locale issue.

thnx Moroccan.

if no one has smth to say i close issue

# Action History
- Created by: takelberry41 | 2018-08-22T07:59:51+00:00
- Closed at: 2018-08-24T09:38:09+00:00
