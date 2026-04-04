---
title: Why does monero-gui now need libhidapi?
source_url: https://github.com/monero-project/monero-gui/issues/1683
author: oneEyedCharlie
assignees: []
labels:
- resolved
created_at: '2018-10-18T22:41:55+00:00'
updated_at: '2018-11-02T22:53:27+00:00'
type: issue
status: closed
closed_at: '2018-10-19T11:09:22+00:00'
---

# Original Description
The purpose of that package is to access bluetooth and weird keyboards.  Why does monero-gui now need that?  I'm sure there is a reasonable explanation, but it seems suspicious to want access to non-standard input devices.  

# Discussion History
## xiphon | 2018-10-18T22:49:24+00:00
Ledger support. Using hidapi instead of pcsclite now.

## oneEyedCharlie | 2018-10-18T22:57:36+00:00
Ah ok.  Thank you.  Now I have to figure out how to get that into Linux Mint 19, which doesn't have any of the hidapi packages.  

## xiphon | 2018-10-18T22:59:14+00:00
Actually don't close this. Looks like a correct issue. The library should be statically linked.

## oneEyedCharlie | 2018-10-18T23:04:42+00:00
Done.

## sanderfoobar | 2018-10-19T00:55:38+00:00
Fixed since https://github.com/monero-project/monero-gui/commit/a34608a801e462ae9d732452ebd25fdc592aebb7 (master) https://github.com/monero-project/monero-gui/commit/669e0f442545d7a58f8e42a3c9c8da8bf655fed6 (release v0.13 branch)

v0.13.0.4 should be out soon.

## dEBRUYNE-1 | 2018-10-19T11:07:55+00:00
+resolved

## oneEyedCharlie | 2018-11-02T22:16:21+00:00
This should be re-opened?  I just downloaded the new 0.13.0.4 version, and am still getting the error.

`error while loading shared libraries: libhidapi-libusb.so.0: cannot open shared object file: No such file or directory`

I know I can install libhidapi-dev and make this go away, but I figured I should still let you know.

## sanderfoobar | 2018-11-02T22:53:10+00:00
@oneEyedCharlie  Thanks for the headsup. We are aware and are working on getting `libhidapi` statically included.

# Action History
- Created by: oneEyedCharlie | 2018-10-18T22:41:55+00:00
- Closed at: 2018-10-19T11:09:22+00:00
