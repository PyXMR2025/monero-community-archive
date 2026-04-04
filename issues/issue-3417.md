---
title: GUI crashed if funds are recieved while trezor disconnected (Possible Privacy
  Implications)
source_url: https://github.com/monero-project/monero-gui/issues/3417
author: Crypt0-Bear
assignees: []
labels: []
created_at: '2021-04-19T23:02:58+00:00'
updated_at: '2021-05-05T02:20:33+00:00'
type: issue
status: closed
closed_at: '2021-05-05T02:20:00+00:00'
---

# Original Description
monero-gui-v0.17.1.9
Trezor Model T up to date firmware 



When using a trezor wallet with passphrase the gui asks for the usual unlock and connect the device to be able to open the wallet. When the wallet is open you are able to view your accounts and are able to generate new addresses but if the device is locked or unplugged the wallet acts like a viewonly wallet. When new transactions come in the device must be unlocked and user must accept to re-scan on the device. 

If the device is unplugged or locked then the GUI will crash (along with the monerod process). This is problematic as this could be used along with network analysis to pinpoint the IP address of a connected node by sending a small transaction to the address in question and then watching the network for a node which disappears and loses peers. 

Since there already is messages from the GUI if the hardware wallet is locked or unplugged when sending it appears that this is an uncaught error and not a design implementation. I took a look at the log files and have included the relevant portions below:

Plugging in device and opening the wallet 
ERROR   device.trezor.transport src/device_trezor/trezor/transport.cpp:1168     BridgeTransport enumeration failed:Bridge enumeration failed
WARNING wallet.wallet2  src/wallet/wallet2.cpp:4370     Device inited...
WARNING wallet.wallet2  src/wallet/wallet2.cpp:5602     Loaded wallet keys file, with public address: [REDACTED]
(Up to this point everything works) 

I then disconnect the device and send a transaction to an address (from different node) and the GUI crashes on the receiving wallet. This is the only error found on the logfile:

ERROR   device.trezor.transport src/device_trezor/trezor/transport.cpp:1120     Unable to transfer, r: -4


This is a trezor model T device without using the trezor bridge instead the UDEV rules. 





# Discussion History
## selsta | 2021-04-19T23:20:10+00:00
monerod and monero-wallet-gui are completely separate programs so the daemon should not crash in that case.

## Crypt0-Bear | 2021-04-20T00:11:23+00:00
I just double checked. You are right it doesn't kill the monerod daemon. So there is no privacy concern with the bug. 

As for the GUI crashing I am able to reproduce the GUI crashing by removing the trezor or if I recive funds while it is locked for a while. I ran it from cli to see the stdout and recived the following when it crashed 

2021-04-20 00:08:07.079 E Unable to transfer, r: -4
munmap_chunk(): invalid pointer
Aborted (core dumped)

The logfile :
ERROR   device.trezor.transport src/device_trezor/trezor/transport.cpp:1120     Unable to transfer, r: -4






## selsta | 2021-04-20T00:14:50+00:00
The GUI is not meant to be used without the hardware wallet plugged in. But it should handle the error more gracefully :)

## Crypt0-Bear | 2021-04-20T16:18:46+00:00
yeah my concerns were more the privacy implications but I realized the monerod process was still running so there isn't a big worry there. This could probably be listed as a small bug and just needs a graceful fail. There appears to already be a error catching for when you unplug the hardware wallet or if the wallet is locked and not available. So maybe certain conditions aren't triggering it 

Thanks for the quick replies btw 

## Crypt0-Bear | 2021-05-05T02:20:33+00:00
I closed the issue as it seems like there is no privacy concern. It is an informational issue and should be caught and is better suited on a backlog 

# Action History
- Created by: Crypt0-Bear | 2021-04-19T23:02:58+00:00
- Closed at: 2021-05-05T02:20:00+00:00
