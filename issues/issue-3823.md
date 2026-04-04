---
title: Fail to build on Fedora 27
source_url: https://github.com/monero-project/monero/issues/3823
author: hegjon
assignees: []
labels:
- invalid
created_at: '2018-05-17T18:58:24+00:00'
updated_at: '2018-05-20T13:16:49+00:00'
type: issue
status: closed
closed_at: '2018-05-20T13:16:49+00:00'
---

# Original Description
I am trying to make a RPM file for Fedora, but it fails during build.

Source tar-ball: `monero-0.12.0.0.tar.gz`

Build steps:
```
mkdir -p build
cd build
%cmake -D CMAKE_BUILD_TYPE=release ..
make %{?_smp_mflags}
```

%{cmake} macro expanded:
```
$ rpm --eval %{cmake}

  CFLAGS="${CFLAGS:--O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables}" ; export CFLAGS ; 
  CXXFLAGS="${CXXFLAGS:--O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables}" ; export CXXFLAGS ; 
  FFLAGS="${FFLAGS:--O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -I/usr/lib64/gfortran/modules}" ; export FFLAGS ; 
  FCFLAGS="${FCFLAGS:--O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -I/usr/lib64/gfortran/modules}" ; export FCFLAGS ; 
  LDFLAGS="${LDFLAGS:--Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld}" ; export LDFLAGS ; 
  /usr/bin/cmake \
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
        -DCMAKE_INSTALL_PREFIX:PATH=/usr \
        -DINCLUDE_INSTALL_DIR:PATH=/usr/include \
        -DLIB_INSTALL_DIR:PATH=/usr/lib64 \
        -DSYSCONF_INSTALL_DIR:PATH=/etc \
        -DSHARE_INSTALL_PREFIX:PATH=/usr/share \
%if "lib64" == "lib64" 
        -DLIB_SUFFIX=64 \
%endif 
        -DBUILD_SHARED_LIBS:BOOL=ON
```

Output:
```
Scanning dependencies of target simplewallet
make[2]: Leaving directory '/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build'
make -f src/simplewallet/CMakeFiles/simplewallet.dir/build.make src/simplewallet/CMakeFiles/simplewallet.dir/build
make[2]: Entering directory '/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build'
[ 93%] Building CXX object src/simplewallet/CMakeFiles/simplewallet.dir/simplewallet.cpp.o
cd /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/simplewallet && /usr/bin/c++  -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBUILD_SHARED_LIBS -DDEFAULT_DB_TYPE=\"lmdb\" -DHAVE_EXPLICIT_BZERO -DHAVE_READLINE -DHAVE_STRPTIME -DPER_BLOCK_CHECKPOINT -DSTACK_TRACE -DUPNP_DYNAMIC -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external/easylogging++ -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/src -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/contrib/epee/include -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/translations -I/usr/include/miniupnpc -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external/db_drivers/liblmdb  -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=native  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DNDEBUG -Ofast    -Werror -o CMakeFiles/simplewallet.dir/simplewallet.cpp.o -c /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/src/simplewallet/simplewallet.cpp
[ 93%] Building CXX object src/daemon/CMakeFiles/daemon.dir/daemon.cpp.o
cd /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/daemon && /usr/bin/c++  -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBUILD_SHARED_LIBS -DDEFAULT_DB_TYPE=\"lmdb\" -DHAVE_EXPLICIT_BZERO -DHAVE_READLINE -DHAVE_STRPTIME -DPER_BLOCK_CHECKPOINT -DSTACK_TRACE -DUPNP_DYNAMIC -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external/easylogging++ -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/src -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/contrib/epee/include -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/translations -I/usr/include/miniupnpc -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external/db_drivers/liblmdb  -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=native  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DNDEBUG -Ofast    -Werror -o CMakeFiles/daemon.dir/daemon.cpp.o -c /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/src/daemon/daemon.cpp
[ 94%] Building CXX object src/daemon/CMakeFiles/daemon.dir/executor.cpp.o
cd /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/daemon && /usr/bin/c++  -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBUILD_SHARED_LIBS -DDEFAULT_DB_TYPE=\"lmdb\" -DHAVE_EXPLICIT_BZERO -DHAVE_READLINE -DHAVE_STRPTIME -DPER_BLOCK_CHECKPOINT -DSTACK_TRACE -DUPNP_DYNAMIC -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external/easylogging++ -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/src -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/contrib/epee/include -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/translations -I/usr/include/miniupnpc -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external/db_drivers/liblmdb  -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=native  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DNDEBUG -Ofast    -Werror -o CMakeFiles/daemon.dir/executor.cpp.o -c /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/src/daemon/executor.cpp
[ 95%] Building CXX object src/daemon/CMakeFiles/daemon.dir/main.cpp.o
cd /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/daemon && /usr/bin/c++  -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBUILD_SHARED_LIBS -DDEFAULT_DB_TYPE=\"lmdb\" -DHAVE_EXPLICIT_BZERO -DHAVE_READLINE -DHAVE_STRPTIME -DPER_BLOCK_CHECKPOINT -DSTACK_TRACE -DUPNP_DYNAMIC -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external/easylogging++ -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/src -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/contrib/epee/include -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/translations -I/usr/include/miniupnpc -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external/db_drivers/liblmdb  -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=native  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DNDEBUG -Ofast    -Werror -o CMakeFiles/daemon.dir/main.cpp.o -c /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/src/daemon/main.cpp
[ 95%] Building CXX object src/daemon/CMakeFiles/daemon.dir/rpc_command_executor.cpp.o
cd /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/daemon && /usr/bin/c++  -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBUILD_SHARED_LIBS -DDEFAULT_DB_TYPE=\"lmdb\" -DHAVE_EXPLICIT_BZERO -DHAVE_READLINE -DHAVE_STRPTIME -DPER_BLOCK_CHECKPOINT -DSTACK_TRACE -DUPNP_DYNAMIC -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external/easylogging++ -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/src -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/contrib/epee/include -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/translations -I/usr/include/miniupnpc -I/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/external/db_drivers/liblmdb  -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=native  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DNDEBUG -Ofast    -Werror -o CMakeFiles/daemon.dir/rpc_command_executor.cpp.o -c /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/src/daemon/rpc_command_executor.cpp
{standard input}: Assembler messages:
{standard input}:910418: Warning: end of file not at end of a line; newline inserted
{standard input}:910680: Error: unknown pseudo-op: `.l'
{standard input}: Error: open CFI at the end of file; missing .cfi_endproc directive
c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See <http://bugzilla.redhat.com/bugzilla> for instructions.
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:66: src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o] Error 4
make[2]: Leaving directory '/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build'
make[1]: *** [CMakeFiles/Makefile2:2174: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 96%] Linking CXX executable ../../bin/monerod
cd /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/daemon && /usr/bin/cmake -E cmake_link_script CMakeFiles/daemon.dir/link.txt --verbose=1
/usr/bin/c++  -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=native  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DNDEBUG -Ofast   -Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -rdynamic CMakeFiles/daemon.dir/command_parser_executor.cpp.o CMakeFiles/daemon.dir/command_server.cpp.o CMakeFiles/daemon.dir/daemon.cpp.o CMakeFiles/daemon.dir/executor.cpp.o CMakeFiles/daemon.dir/main.cpp.o CMakeFiles/daemon.dir/rpc_command_executor.cpp.o blocksdat.o  -o ../../bin/monerod -Wl,-rpath,/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/daemonizer:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/rpc:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/serialization:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/cryptonote_protocol:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/p2p:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/cryptonote_core:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/blockchain_db:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/external/db_drivers/liblmdb:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/multisig:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/ringct:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/cryptonote_basic:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/checkpoints:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/device:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/common:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/crypto:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/external/easylogging++: -lrt -ldl ../daemonizer/libdaemonizer.so ../rpc/libdaemon_rpc_server.so ../../contrib/epee/src/libepee.a ../../contrib/epee/src/libepee_readline.a -lboost_chrono -lboost_filesystem -lboost_program_options -lboost_regex -lboost_system -pthread -lzmq -lsodium -lreadline -lrt -ldl ../rpc/librpc.so ../rpc/librpc_base.so ../serialization/libserialization.so ../cryptonote_protocol/libcryptonote_protocol.so ../p2p/libp2p.so ../cryptonote_core/libcryptonote_core.so ../blockchain_db/libblockchain_db.so ../../external/db_drivers/liblmdb/liblmdb.so ../multisig/libmultisig.so ../ringct/libringct.so ../cryptonote_basic/libcryptonote_basic.so ../checkpoints/libcheckpoints.so ../device/libdevice.so ../ringct/libringct_basic.so ../common/libcommon.so ../crypto/libcncrypto.so -lunbound -lboost_regex -lboost_date_time ../../contrib/epee/src/libepee.a -lssl -lcrypto ../libversion.so -lminiupnpc -lboost_chrono -lboost_filesystem -lboost_program_options -lboost_system -lboost_thread -lboost_serialization ../../external/easylogging++/libeasylogging.so -lrt -ldl -Wl,-rpath-link,/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/rpc 
make[2]: Leaving directory '/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build'
[ 96%] Built target daemon
[ 96%] Linking CXX executable ../../bin/monero-wallet-cli
cd /home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/simplewallet && /usr/bin/cmake -E cmake_link_script CMakeFiles/simplewallet.dir/link.txt --verbose=1
/usr/bin/c++  -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=native  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DNDEBUG -Ofast   -Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -rdynamic CMakeFiles/simplewallet.dir/simplewallet.cpp.o  -o ../../bin/monero-wallet-cli -Wl,-rpath,/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/wallet:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/rpc:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/cryptonote_core:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/mnemonics:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/blockchain_db:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/multisig:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/ringct:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/cryptonote_basic:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/device:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/checkpoints:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/external/db_drivers/liblmdb:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/common:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/src/crypto:/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build/external/easylogging++: -lrt -ldl ../wallet/libwallet.so ../rpc/librpc_base.so ../cryptonote_core/libcryptonote_core.so ../mnemonics/libmnemonics.so ../../contrib/epee/src/libepee.a ../../contrib/epee/src/libepee_readline.a ../libversion.so -lboost_chrono -lboost_program_options -lboost_filesystem -lboost_thread -pthread -lreadline -lrt -ldl ../blockchain_db/libblockchain_db.so ../multisig/libmultisig.so ../ringct/libringct.so ../cryptonote_basic/libcryptonote_basic.so ../device/libdevice.so ../ringct/libringct_basic.so ../checkpoints/libcheckpoints.so ../../external/db_drivers/liblmdb/liblmdb.so -lboost_serialization ../common/libcommon.so ../crypto/libcncrypto.so -lunbound -lboost_date_time -lboost_system ../../contrib/epee/src/libepee.a -lboost_filesystem -lssl -lrt -ldl -lcrypto -lboost_program_options -lboost_thread -lboost_regex ../../external/easylogging++/libeasylogging.so 
make[2]: Leaving directory '/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build'
[ 96%] Built target simplewallet
make[1]: Leaving directory '/home/jonny/rpmbuild/BUILD/monero-0.12.0.0/build'
make: *** [Makefile:144: all] Error 2
error: Bad exit status from /var/tmp/rpm-tmp.OYayqQ (%build)


RPM build errors:
    Bad exit status from /var/tmp/rpm-tmp.OYayqQ (%build)
```

Library versions:
```
gcc-7.3.1-5.fc27.x86_64
cmake-3.11.0-1.fc27.x86_64
pkgconf-1.3.12-2.fc27.x86_64
boost-devel-1.64.0-5.fc27.x86_64
openssl-devel-1.1.0h-3.fc27.x86_64
cppzmq-devel-4.1.6-2.fc26.x86_64
unbound-devel-1.7.0-4.fc27.x86_64
libsodium-devel-1.0.14-1.fc27.x86_64
miniupnpc-devel-2.0-6.fc27.x86_64
libunwind-devel-1.2.1-3.fc27.x86_64
xz-devel-5.2.3-4.fc27.x86_64
readline-devel-7.0-7.fc27.x86_64
ldns-devel-1.7.0-11.fc27.x86_64
expat-devel-2.2.5-1.fc27.x86_64
gtest-devel-1.7.0-11.fc27.x86_64
doxygen-1.8.13-10.fc27.x86_64
graphviz-2.40.1-10.fc27.x86_64
```

# Discussion History
## hegjon | 2018-05-17T19:59:35+00:00
It builds fine on the Fedora build infrastructure https://koji.fedoraproject.org/koji/taskinfo?taskID=27021085

Not sure why it fails on my laptop. 

## moneromooo-monero | 2018-05-17T20:21:47+00:00
Is this an OOM ? dmesg should tell. The "Killed" is usually a telltale OOM, but the asm errors make me doubt it is.
In any case, do you have any funky config, like non default assembler, several compilers/assemblers, etc ?

## hegjon | 2018-05-17T21:18:30+00:00
Ah, you are correct, I did not think it would happen on my machine. 

```
[36029.567042] Out of memory: Kill process 15952 (cc1plus) score 160 or sacrifice child
[36029.567050] Killed process 15952 (cc1plus) total-vm:3010020kB, anon-rss:1195448kB, file-rss:0kB, shmem-rss:0kB
[36030.115594] oom_reaper: reaped process 15952 (cc1plus), now anon-rss:0kB, file-rss:0kB, shmem-rss:0kB
```
12G of RAM + 6GB of swap, but Firefox seems to use a lot of memory....

## moneromooo-monero | 2018-05-20T13:09:18+00:00
That was an OOM, closing. FWIW, 3GB seems to be enough for wallet2.cpp (the heaviest).

+invalid


# Action History
- Created by: hegjon | 2018-05-17T18:58:24+00:00
- Closed at: 2018-05-20T13:16:49+00:00
