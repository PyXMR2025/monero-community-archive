---
title: Can't build 16.0.3 in Ubuntu 20.04
source_url: https://github.com/monero-project/monero-gui/issues/3109
author: rating89us
assignees: []
labels: []
created_at: '2020-09-25T12:31:08+00:00'
updated_at: '2021-01-15T11:53:31+00:00'
type: issue
status: closed
closed_at: '2021-01-15T11:53:31+00:00'
---

# Original Description
Log:
```
/home/asuspc/Qt/5.14.1/gcc_64/lib/libQt5Gui.so /home/asuspc/Qt/5.14.1/gcc_64/lib/libQt5QmlModels.so /home/asuspc/Qt/5.14.1/gcc_64/lib/libQt5Qml.so /home/asuspc/Qt/5.14.1/gcc_64/lib/libQt5Network.so /home/asuspc/Qt/5.14.1/gcc_64/lib/libQt5Core.so -lGL -lpthread   
/usr/bin/ld: /home/asuspc/moneronew2/monero-gui/monero/lib/libwallet_merged.a(device_default.cpp.o): in function `hw::core::device_default::derive_subaddress_public_key(crypto::public_key const&, crypto::key_derivation const&, unsigned long, crypto::public_key&)':
device_default.cpp:(.text+0x11e): undefined reference to `monero_crypto_amd64_64_24k_generate_subaddress_public_key'
/usr/bin/ld: /home/asuspc/moneronew2/monero-gui/monero/lib/libwallet_merged.a(device_default.cpp.o): in function `hw::core::device_default::generate_key_derivation(crypto::public_key const&, epee::mlocked<tools::scrubbed<crypto::ec_scalar> > const&, crypto::key_derivation&) [clone .localalias]':
device_default.cpp:(.text+0x38c): undefined reference to `monero_crypto_amd64_64_24k_generate_key_derivation'
/usr/bin/ld: /home/asuspc/moneronew2/monero-gui/monero/lib/libwallet_merged.a(device_default.cpp.o): in function `hw::core::device_default::encrypt_payment_id(crypto::hash8&, crypto::public_key const&, epee::mlocked<tools::scrubbed<crypto::ec_scalar> > const&)':
device_default.cpp:(.text+0x85e): undefined reference to `monero_crypto_amd64_64_24k_generate_key_derivation'
/usr/bin/ld: /home/asuspc/moneronew2/monero-gui/monero/lib/libwallet_merged.a(device_default.cpp.o): in function `hw::core::device_default::generate_output_ephemeral_keys(unsigned long, cryptonote::account_keys const&, crypto::public_key const&, epee::mlocked<tools::scrubbed<crypto::ec_scalar> > const&, cryptonote::tx_destination_entry const&, boost::optional<cryptonote::account_public_address> const&, unsigned long, bool const&, std::vector<epee::mlocked<tools::scrubbed<crypto::ec_scalar> >, std::allocator<epee::mlocked<tools::scrubbed<crypto::ec_scalar> > > > const&, std::vector<crypto::public_key, std::allocator<crypto::public_key> >&, std::vector<rct::key, std::allocator<rct::key> >&, crypto::public_key&)':
device_default.cpp:(.text+0x2f5d): undefined reference to `monero_crypto_amd64_64_24k_generate_key_derivation'
/usr/bin/ld: device_default.cpp:(.text+0x30ae): undefined reference to `monero_crypto_amd64_64_24k_generate_key_derivation'
collect2: error: ld returned 1 exit status
make: *** [Makefile:703: release/bin/monero-wallet-gui] Error 1
```


# Discussion History
## selsta | 2020-09-25T12:32:32+00:00
Please try to remove the build directory and then:

`USE_SINGLE_BUILDDIR=ON DEV_MODE=ON make release -j4`

If you have to use a specific Qt directory do:

`CMAKE_PREFIX_PATH=/home/asuspc/Qt/5.14.1/gcc_64/ USE_SINGLE_BUILDDIR=ON DEV_MODE=ON make release -j4`

Resulting binary should be in build/release/bin directory.

## rating89us | 2020-09-25T12:36:00+00:00
`./build.sh CMAKE_PREFIX_PATH=/home/asuspc/moneronew2/monero-gui/ USE_SINGLE_BUILDDIR=ON DEV_MODE=ON make release -j4`

returns:
`Valid build types are release, release-static, release-android, debug-android and debug`


## selsta | 2020-09-25T12:36:27+00:00
No, without ./build.sh, we have a new build system and didn’t update the documentation yet, also you have to set your CMAKE_PREFIX_PATH to your Qt installation folder like I did in the previous comment.

## rating89us | 2020-09-25T12:42:15+00:00
`CMAKE_PREFIX_PATH=/home/asuspc/moneronew2/monero-gui/ USE_SINGLE_BUILDDIR=ON DEV_MODE=ON make release -j4`

returns:
`make: *** No rule to make target 'release'.  Stop.`

## selsta | 2020-09-25T12:44:59+00:00
You have to set your CMAKE_PREFIX_PATH to your Qt installation folder, not the GUI folder. See my first comment.

Can you try to build master? If it still fails please post the full console output including the folder you are currently in.

## rating89us | 2020-09-25T17:45:51+00:00
`CMAKE_PREFIX_PATH=/home/asuspc/Qt/5.14.1/gcc_64/ USE_SINGLE_BUILDDIR=ON DEV_MODE=ON make release -j4` returns:

```
[100%] Linking CXX executable ../bin/monero-wallet-gui
/usr/bin/ld: cannot find -lQt5QmlModels
/usr/bin/ld: cannot find -lQt5XmlPatterns
/usr/bin/ld: cannot find -lQt5QmlModels
/usr/bin/ld: cannot find -lQt5XmlPatterns
collect2: error: ld returned 1 exit status
make[3]: *** [src/CMakeFiles/monero-wallet-gui.dir/build.make:1035: bin/monero-wallet-gui] Error 1
make[3]: Leaving directory '/home/asuspc/moneronew4/monero-gui/build/release'
make[2]: *** [CMakeFiles/Makefile2:4358: src/CMakeFiles/monero-wallet-gui.dir/all] Error 2
make[2]: Leaving directory '/home/asuspc/moneronew4/monero-gui/build/release'
make[1]: *** [Makefile:130: all] Error 2
make[1]: Leaving directory '/home/asuspc/moneronew4/monero-gui/build/release'
make: *** [Makefile:37: release] Error 2
```

`USE_SINGLE_BUILDDIR=ON DEV_MODE=ON make release -j4` returns:

```
[ 90%] Linking CXX executable ../bin/monero-wallet-gui
/usr/bin/ld: cannot find -lQt5QmlModels
/usr/bin/ld: cannot find -lQt5XmlPatterns
/usr/bin/ld: cannot find -lQt5QmlModels
/usr/bin/ld: cannot find -lQt5XmlPatterns
collect2: error: ld returned 1 exit status
make[3]: *** [src/CMakeFiles/monero-wallet-gui.dir/build.make:1035: bin/monero-wallet-gui] Error 1
make[3]: Leaving directory '/home/asuspc/moneronew4/monero-gui/build/release'
make[2]: *** [CMakeFiles/Makefile2:4358: src/CMakeFiles/monero-wallet-gui.dir/all] Error 2
make[2]: Leaving directory '/home/asuspc/moneronew4/monero-gui/build/release'
make[1]: *** [Makefile:130: all] Error 2
make[1]: Leaving directory '/home/asuspc/moneronew4/monero-gui/build/release'
make: *** [Makefile:37: release] Error 2
```




## xiphon | 2020-09-25T21:46:34+00:00
> CMAKE_PREFIX_PATH=/home/asuspc/Qt/5.14.1/gcc_64/ USE_SINGLE_BUILDDIR=ON DEV_MODE=ON make release -j4 returns:

Did you do a clean build?

## selsta | 2020-09-25T21:47:41+00:00
I helped him on IRC, apparently our linux cmake build does not work with installer Qt 5.14 and 5.15, it does work with 5.12

## xiphon | 2021-01-15T11:53:31+00:00
Has been fixed a while ago. We do support Linux installer Qt 5.14 and 5.15 builds now.

# Action History
- Created by: rating89us | 2020-09-25T12:31:08+00:00
- Closed at: 2021-01-15T11:53:31+00:00
