---
title: Compliation Error on OSX - QUIRC
source_url: https://github.com/monero-project/monero-gui/issues/3322
author: breadsax
assignees: []
labels: []
created_at: '2021-01-31T02:20:30+00:00'
updated_at: '2021-05-13T04:27:55+00:00'
type: issue
status: closed
closed_at: '2021-05-13T04:27:55+00:00'
---

# Original Description
Receive the following error on Mojave even though WITH_SCANNER should be set to OFF by default:

[ 57%] Building C object external/CMakeFiles/quirc.dir/quirc/lib/quirc.c.o
Scanning dependencies of target openpgp
/Users/hiro1/monero-gui/external/quirc/lib/quirc.c:126:22: error: result [ 57%] Generating monero-core.qm
of comparison of constant 8 with expression of type 'quirc_decode_error_t' is always true [-Werror,-Wtautological-constant-out-of-range-compare]
        if (err >= 0 && err < sizeof(error_table) / sizeof(error_table[0]))
                        ~~~ ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1 error generated.

# Discussion History
## selsta | 2021-01-31T22:56:44+00:00
Can you post the exact steps you used to build?

## breadsax | 2021-02-01T14:34:25+00:00
@selsta I followed the steps from the github instructions. The only thing I noticed just now is that it says to install full XCode and I've only ever needed the XCode Command Line Tools. Did that change perhaps?

On OS X:
Install Xcode from AppStore

Install homebrew

Install monero dependencies:

brew install boost hidapi zmq libpgm libsodium miniupnpc ldns expat libunwind-headers protobuf libgcrypt

Install Qt:
brew install qt5 (or download QT 5.9.7+ from qt.io)

Grab an up-to-date copy of the monero-gui repository

git clone --recursive https://github.com/monero-project/monero-gui.git
cd monero-gui
Start the build

make release -j4

## selsta | 2021-02-01T14:43:26+00:00
Can you try deleting line 459 and 460 from CMakeLists.txt? (The lines containing werror). Afterwards please try again.

## breadsax | 2021-02-01T18:46:59+00:00
@selsta  I was able to compile successfully with this workaround. Thank you!

## selsta | 2021-02-01T23:05:51+00:00
@xiphon Looks like quirc has an warning during compilation on older macOS systems which becomes an error with -Werror. What should we do here?

## xiphon | 2021-02-02T20:24:52+00:00
Could you please post complete `make release -j4 VERBOSE=1` output? Consider to strip sensitive information.

## selsta | 2021-05-08T21:23:28+00:00
Related: https://bugs.llvm.org//show_bug.cgi?id=16154

# Action History
- Created by: breadsax | 2021-01-31T02:20:30+00:00
- Closed at: 2021-05-13T04:27:55+00:00
