---
title: '[cmake/osx] help needed - Linking issues, need cmake to build so I can work
  in CLion'
source_url: https://github.com/monero-project/monero/issues/1851
author: gubatron
assignees: []
labels: []
created_at: '2017-03-08T09:27:26+00:00'
updated_at: '2017-03-17T06:33:45+00:00'
type: issue
status: closed
closed_at: '2017-03-17T06:33:12+00:00'
---

# Original Description
# linking issue

When I try to make using the cmake generated Makefile, the build fails around 75% of the way when it starts linking shared library `libblockchain_db.dylib`, right here:

```
[ 75%] Built target obj_blockchain_db
Scanning dependencies of target blockchain_db
[ 75%] Linking CXX shared library libblockchain_db.dylib
Undefined symbols for architecture x86_64:
  "cryptonote::HardFork::add(cryptonote::block const&, unsigned long long)", referenced from:
      cryptonote::BlockchainDB::add_block(cryptonote::block const&, unsigned long const&, unsigned long long const&, unsigned long long const&, std::__1::vector<cryptonote::transaction, std::__1::allocator<cryptonote::transaction> > const&) in blockchain_db.cpp.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [src/blockchain_db/libblockchain_db.dylib] Error 1
make[1]: *** [src/blockchain_db/CMakeFiles/blockchain_db.dir/all] Error 2
make: *** [all] Error 2
```

I'd really like to get the project to work using only cmake so that I can properly work in CLion and start contributing at a decent pace.

This is the output I get when I invoke `cmake .` in the root folder:

```
$ cmake .
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries with position independent code
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception disabled
-- Using OpenSSL found at /usr/local/opt/openssl
-- Could not find miniupnp
-- Using miniupnpc from local source tree (/external/miniupnpc)
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/local/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- AES support enabled
-- Found Boost Version: 106200
-- Found Git: /usr/local/bin/git
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/gubatron/workspace/monero
```

--

# Other questions

What is `DEVELOPER_LOCAL_TOOLS` supposed to be in env?
What is `DEVELOPER_LIBUNBOUND_OLD` supposed to be in env?
What should `DATABASE` in env be pointing to? Shouldn't we use an env variable prefixed with `MONERO_` or something similar to avoid environment variable collisions?


# Discussion History
## gubatron | 2017-03-08T09:55:43+00:00
installed some more dependencies with home brew
```
brew install libunwind-headers --force
brew link libunwind-headers --force
brew install miniupnpc

brew install ldns
brew link ldns

brew install expat
brew link expat --force

brew install doxygen
```

redid `cmake .`
```bash
cmake .
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries with position independent code
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception disabled
-- Using OpenSSL found at /usr/local/opt/openssl
-- Found the miniupnpc libraries at /usr/local/lib/libminiupnpc.dylib
-- Found the miniupnpc headers at /usr/local/include/miniupnpc
-- Detecting version of miniupnpc in path: /usr/local/include/miniupnpc
-- Performing Test MINIUPNPC_VERSION_1_7_OR_HIGHER
-- Performing Test MINIUPNPC_VERSION_1_7_OR_HIGHER - Success
-- Found miniupnpc version is v1.7 or higher
-- Using shared miniupnpc found at /usr/local/include/miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/local/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- AES support enabled
-- Found Boost Version: 106200
-- Found Git: /usr/local/bin/git
-- Found Doxygen: /usr/local/bin/doxygen (found version "1.8.13") 
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/gubatron/workspace.frostwire/monero
```

Still having issues on the same spot:
```bash
[ 76%] Linking CXX shared library libblockchain_db.dylib
Undefined symbols for architecture x86_64:
  "cryptonote::HardFork::add(cryptonote::block const&, unsigned long long)", referenced from:
      cryptonote::BlockchainDB::add_block(cryptonote::block const&, unsigned long const&, unsigned long long const&, unsigned long long const&, std::__1::vector<cryptonote::transaction, std::__1::allocator<cryptonote::transaction> > const&) in blockchain_db.cpp.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [src/blockchain_db/libblockchain_db.dylib] Error 1
make[1]: *** [src/blockchain_db/CMakeFiles/blockchain_db.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 76%] Built target obj_wallet
make: *** [all] Error 2
```

## kenshi84 | 2017-03-17T02:38:04+00:00
Could you please close this issue which was solved by #1853?

## gubatron | 2017-03-17T06:33:45+00:00
Sorry about that, didn't know the dynamic. Thought this was closed already.

# Action History
- Created by: gubatron | 2017-03-08T09:27:26+00:00
- Closed at: 2017-03-17T06:33:12+00:00
