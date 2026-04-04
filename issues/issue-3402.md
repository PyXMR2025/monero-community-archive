---
title: Create a new wallet from hardware
source_url: https://github.com/monero-project/monero-gui/issues/3402
author: zip39
assignees: []
labels: []
created_at: '2021-04-15T09:10:06+00:00'
updated_at: '2021-04-15T11:59:56+00:00'
type: issue
status: closed
closed_at: '2021-04-15T11:57:57+00:00'
---

# Original Description
When attempting to "create a new wallet from hardware", there is a dropdown menu ("Choose your hardware device") which should show the options Trezor or Ledger. However, this dropdown menu doesn't work at all for me. The only thing that happens when I press it is that the little arrow on the right hand side alternates between pointing down or up. My Trezor model T is updated to the latest firmware (2.3.6), and connected and unlocked at this point. I do not have any other wallets open (such as Trezor Suite).

OS: Manjaro
Programs: _monero-gui_ and _monero_ (arch linux packages)
(I also have installed the packages _trezor-udev_ and _trezor-suite-appimage_)

![image](https://user-images.githubusercontent.com/82575673/114842454-250cec00-9dd9-11eb-94e7-fdd3d210608b.png)

I also tried to achieve the same by using the monero-wallet-cli, by
```
$ monero-wallet-cli --hw-device Trezor --generate-from-device trezor
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.
Monero 'Oxygen Orion' (v0.17.1.9-release)
Logging to monero-wallet-cli.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
Enter a new password for the wallet: 
Confirm password: 
Device asks for passphrase. Do you want to enter the passphrase on device (Y) (or on the host (N))?: N
Enter device passphrase: 
munmap_chunk(): invalid pointer
[1]    16737 abort (core dumped)  monero-wallet-cli --hw-device Trezor --generate-from-device trezor_
```


# Discussion History
## selsta | 2021-04-15T11:31:16+00:00
Please try the getmonero.org binary and report if it works correctly. The arch package had issues in the past.

## zip39 | 2021-04-15T11:57:57+00:00
That binary did work. Thanks

## selsta | 2021-04-15T11:58:37+00:00
Please report to arch package maintainer.

## zip39 | 2021-04-15T11:59:56+00:00
Will do

# Action History
- Created by: zip39 | 2021-04-15T09:10:06+00:00
- Closed at: 2021-04-15T11:57:57+00:00
