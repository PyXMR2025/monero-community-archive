---
title: '"Dev" install target'
source_url: https://github.com/monero-project/monero/issues/8518
author: jbakosi
assignees: []
labels: []
created_at: '2022-08-19T18:07:23+00:00'
updated_at: '2022-08-19T18:07:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I use monero and monero-cpp as external libs in an app via cmake's `ExternalProject_Add()` functionality, which runs `cmake`, followed by `make install` on external libs.

Currently, monero's install target installs the following:
```
-- Install configuration: "RELEASE"
-- Installing: ${CMAKE_INSTALL_PREFIX}/lib/liblmdb.a
-- Installing: ${CMAKE_INSTALL_PREFIX}/lib/libeasylogging.a
-- Installing: ${CMAKE_INSTALL_PREFIX}/lib/libepee.a
-- Installing: ${CMAKE_INSTALL_PREFIX}/lib/libepee_readline.a
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-wallet-rpc
-- Installing: ${CMAKE_INSTALL_PREFIX}/include/wallet/api/wallet2_api.h
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-wallet-cli
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-gen-trusted-multisig
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-gen-ssl-cert
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monerod
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-blockchain-import
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-blockchain-export
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-blockchain-mark-spent-outputs
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-blockchain-usage
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-blockchain-ancestry
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-blockchain-depth
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-blockchain-stats
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-blockchain-prune-known-spent-data
-- Installing: ${CMAKE_INSTALL_PREFIX}/bin/monero-blockchain-prune
```
This is a good "user" install target, but to use monero as a library, I find that I need to apply [this patch](https://codeberg.org/piac/piac/src/branch/master/cmake/monero-install-targets.patch) to create more files to be installed. (This way I can build and install monero and monero-cpp separately, which is easier to work with as the build is more modular.)

I wonder if it makes sense to contribute this back as a "dev" install target. It could be done optionally, triggered by some cmake variable that's off by default.

# Discussion History
# Action History
- Created by: jbakosi | 2022-08-19T18:07:23+00:00
