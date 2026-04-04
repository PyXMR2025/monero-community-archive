---
title: Monero created a fork problem？？？
source_url: https://github.com/monero-project/monero/issues/3239
author: msionf
assignees: []
labels: []
created_at: '2018-02-07T09:19:17+00:00'
updated_at: '2018-03-17T14:55:57+00:00'
type: issue
status: closed
closed_at: '2018-02-07T10:04:17+00:00'
---

# Original Description
I want to create one, monero forks, but encountered some problems.
First of all, I downloaded the Monero source code, made the following changes, and after trying make, I did not know how to create the “genesis tx” value and what to do next. Please help me. thank you all. Thank you
------------------------------------------------------------------------------------
cryptonote_config.h
   #define CRYPTONOTE_NAME                         "abc"
  uint16_t const P2P_DEFAULT_PORT = 17122;
  uint16_t const RPC_DEFAULT_PORT = 17123;
  -----------------------------------------------------------
CMakeLists.txt
      OUTPUT_NAME "cpciond")
--------------------------------------------------------------
namespace config
{
  uint64_t const DEFAULT_FEE_ATOMIC_XMR_PER_KB = 500; // Just a placeholder!  Change me!
  uint8_t const FEE_CALCULATION_MAX_RETRIES = 10;
  uint64_t const DEFAULT_DUST_THRESHOLD = ((uint64_t)1);
  uint64_t const BASE_REWARD_CLAMP_THRESHOLD = ((uint64_t)100000000); // pow(10, 8)
  std::string const P2P_REMOTE_DEBUG_TRUSTED_PUB_KEY = "0000000000000000000000000000000000000000000000000000000000000000";

  uint64_t const CRYPTONOTE_PUBLIC_ADDRESS_BASE58_PREFIX = 0x2419;
  uint64_t const CRYPTONOTE_PUBLIC_INTEGRATED_ADDRESS_BASE58_PREFIX = 0x7096;
  uint16_t const P2P_DEFAULT_PORT = 17122;
  uint16_t const RPC_DEFAULT_PORT = 17123;
  boost::uuids::uuid const NETWORK_ID = { {
      0x10, 0x24, 0x23, 0xE1, 0x8E, 0xC2, 0xE3, 0xF8, 0xEA, 0x5D, 0xD1, 0x2C, 0x85, 0x8E, 0xC8, 0x39
    } };
  std::string const GENESIS_TX = "";
  uint32_t const GENESIS_NONCE = 10000;

  namespace testnet
  {
    uint64_t const CRYPTONOTE_PUBLIC_ADDRESS_BASE58_PREFIX = 0x5520;
    uint64_t const CRYPTONOTE_PUBLIC_INTEGRATED_ADDRESS_BASE58_PREFIX = 0xd3096;
    uint16_t const P2P_DEFAULT_PORT = 27122;
    uint16_t const RPC_DEFAULT_PORT = 27123;
    boost::uuids::uuid const NETWORK_ID = { {
        0x10, 0x24, 0x23, 0x40, 0x66, 0xC2, 0x04, 0xA4, 0xEA, 0x5D, 0xD1, 0x2C, 0x85, 0x8E, 0xC8, 0x40
      } };
    std::string const GENESIS_TX = "";
    uint32_t const GENESIS_NONCE = 10001;
  }
}
-------------------------------------------------------------------------------------------------------------------
Execute "make" the following error

ubuntu@ubuntu-virtual-machine:~/Desktop/abc$ cd build/release/
ubuntu@ubuntu-virtual-machine:~/Desktop/abc/build/release$ cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- Building without build tag
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled
CMake Error at /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:148 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_LIBRARIES
  OPENSSL_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:388 (_FPHSA_FAILURE_MESSAGE)
  /usr/share/cmake-3.5/Modules/FindOpenSSL.cmake:370 (find_package_handle_standard_args)
  CMakeLists.txt:332 (find_package)


-- Configuring incomplete, errors occurred!
See also "/home/ubuntu/Desktop/abc/build/release/CMakeFiles/CMakeOutput.log".


------------------------------------------------------------------------------------------------------------
The system has been installed 
"sudo apt-get install gcc cmake pkgconf boost-devel openssl-devel cppzmq-devel unbound-devel libsodium-devel miniupnpc-devel libunwind-devel xz-devel readline-devel ldns-devel expat-devel gtest-devel doxygen graphviz -y "
and 
“sudo apt-get install libgtest-dev && cd / usr / src / gtest && sudo cmake. && sudo make && sudo mv libg * / usr / lib /” 




# Discussion History
## fluffypony | 2018-02-07T10:04:17+00:00
No.

## msionf | 2018-02-07T10:07:59+00:00
？？？

## mardarfar | 2018-02-07T17:46:46+00:00
You're missing libssl/libssl-dev it's in the fucking error message
How can you be this clueless yet try to tackle a beast like Monero?

## sammy007 | 2018-02-07T17:55:31+00:00
When ICO?

## tekcash | 2018-02-07T17:59:26+00:00
lol these scammers aint loyal

## crebbo | 2018-02-07T18:09:44+00:00
Electroneum guys might be able to give you some pointers, especially around block 202612

## binaryFate | 2018-02-07T18:27:30+00:00
Scam fork with "top-notch dev team" incoming in 3...2...1...   

...

... ah, no. They are so bad nowadays they can't compile.

## Starmute | 2018-02-07T18:41:13+00:00
@crebbo That one comment right there is worth all the death threats I received for reporting that bug. 😂😂😂

## serhack | 2018-02-07T19:28:33+00:00
> #define CRYPTONOTE_NAME "abc"

That's cool, I will invest in abc coin.

## crebbo | 2018-02-07T19:44:28+00:00
@Starmute I'm glad mate, I was thinking of you when I wrote that

# Action History
- Created by: msionf | 2018-02-07T09:19:17+00:00
- Closed at: 2018-02-07T10:04:17+00:00
