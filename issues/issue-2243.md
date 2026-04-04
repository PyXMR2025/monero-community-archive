---
title: '[Trezor] Trezor not being detected on macOS'
source_url: https://github.com/monero-project/monero-gui/issues/2243
author: rating89us
assignees: []
labels: []
created_at: '2019-07-01T18:20:55+00:00'
updated_at: '2019-08-21T20:19:50+00:00'
type: issue
status: closed
closed_at: '2019-08-21T20:19:50+00:00'
---

# Original Description
Latest GUI (0.14.1 beta) is not detecting Trezor Model T (firmware v2.1.1) on macOS 10.14.3 (Mojave).
The device is working fine on online Trezor beta wallet.

@ph4r05

# Discussion History
## selsta | 2019-07-01T18:34:21+00:00
Can you try restarting your Mac? Also make sure that the you don’t use the Trezor web wallet at the same time (close your browser).

## rating89us | 2019-07-01T19:06:34+00:00
It's still not working after restart. Trezor web wallet isn't being used at the same time.
Error: "failed to generate wallet: Device connect failed"

## rating89us | 2019-07-01T19:13:07+00:00
I discovered what was wrong. Trezor bridge was not installed.

## ph4r05 | 2019-07-01T19:20:31+00:00
@Selsta is the GUI binary compiled with libusb library? It should work also without Trezor bridge :/

## selsta | 2019-07-01T19:26:38+00:00
@ph4r05 I don’t know but this is the first time I’m hearing about libusb so most likely not.

## ph4r05 | 2019-07-01T19:36:47+00:00
When I build it locally it works with libusb compiled in, but we would have to verify if released versions have the libusb compiled.

## dEBRUYNE-1 | 2019-07-01T20:10:23+00:00
@ph4r05 - Can you perhaps check with the beta v0.14.1.0 Mac OS binary?

https://github.com/monero-project/monero-gui/releases/tag/v0.14.1.0

## ph4r05 | 2019-07-08T13:03:00+00:00
@dEBRUYNE-1 how were the GUI binaries built pls? With the `build.sh`? 

## ph4r05 | 2019-07-08T14:42:44+00:00
I've checked the binary and apparently it does not link `libusb`. 
There are no symbols related to the `libusb` / `webusb` transport in the statically linked monero-core.

```bash
nm -gU ~/Downloads/monero-gui-v0.14.1.0/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui  | grep -i trezor | grep -i usb
```

-> Thus `WITH_DEVICE_TREZOR_WEBUSB` macro was not defined during the build 
-> `HAVE_TREZOR_LIBUSB` was not defined by the Cmake
-> CMake could not detect usable libusb, 1.0.18+ should be OK.

The resolve logic is handled by `cmake/FindLibUSB.cmake` and `cmake/CheckTrezor.cmake`.

Successful resolution should yield following lines from Cmake:

```
-- LibUSB Compilation test: TRUE
-- Trezor compatible LibUSB found at: /usr/local/Cellar/libusb/1.0.21/include/libusb-1.0
```

The monero-core build is handled by `get_libwallet_api.sh`, its Cmake output should indicate whether libusb is included or not.

# Action History
- Created by: rating89us | 2019-07-01T18:20:55+00:00
- Closed at: 2019-08-21T20:19:50+00:00
