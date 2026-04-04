---
title: monero-wallet-cli - cannot connect to Ledger Nano S in VMware VM instance on
  Windows Host
source_url: https://github.com/monero-project/monero-gui/issues/3976
author: pikob
assignees: []
labels: []
created_at: '2022-07-19T17:12:58+00:00'
updated_at: '2022-07-19T23:09:51+00:00'
type: issue
status: closed
closed_at: '2022-07-19T23:09:51+00:00'
---

# Original Description
Trying to connect to existing wallet, after entering wallet password, program exits with following error:

```
Error: failed to load wallet: Unable to send hidapi command. Error 64: hid_error is not implemented yet
```

Monero version: 0.17.3.2, debug build
Host: Windows 10
VMware Player 16 running Debian 5.10

Note: VMware required some configuration to keep Ledger connected when connecting an app. These lines were added to .vmx file:
```
usb.generic.allowHID = "TRUE"
usb.quirks.device0 = "0x2c97:0x1011 allow"
```

USB configuration in VM:

```
lsusb -t -v
/:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=uhci_hcd/2p, 12M
    ID 1d6b:0001 Linux Foundation 1.1 root hub
    |__ Port 1: Dev 2, If 0, Class=Human Interface Device, Driver=usbhid, 12M
        ID 0e0f:0003 VMware, Inc. Virtual Mouse
    |__ Port 2: Dev 3, If 0, Class=Hub, Driver=hub/7p, 12M
        ID 0e0f:0002 VMware, Inc. Virtual USB Hub
        |__ Port 1: Dev 4, If 0, Class=Human Interface Device, Driver=usbhid, 12M
            ID 2c97:0001 Ledger Nano S
        |__ Port 1: Dev 4, If 1, Class=Human Interface Device, Driver=usbhid, 12M
            ID 2c97:0001 Ledger Nano S
/:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=ehci-pci/6p, 480M
    ID 1d6b:0002 Linux Foundation 2.0 root hub
```

usb-devices output:
```
T:  Bus=01 Lev=00 Prnt=00 Port=00 Cnt=00 Dev#=  1 Spd=480 MxCh= 6
D:  Ver= 2.00 Cls=09(hub  ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=1d6b ProdID=0002 Rev=05.10
S:  Manufacturer=Linux 5.10.0-16-amd64 ehci_hcd
S:  Product=EHCI Host Controller
S:  SerialNumber=0000:02:03.0
C:  #Ifs= 1 Cfg#= 1 Atr=e0 MxPwr=0mA
I:  If#=0x0 Alt= 0 #EPs= 1 Cls=09(hub  ) Sub=00 Prot=00 Driver=hub

T:  Bus=02 Lev=00 Prnt=00 Port=00 Cnt=00 Dev#=  1 Spd=12  MxCh= 2
D:  Ver= 1.10 Cls=09(hub  ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=1d6b ProdID=0001 Rev=05.10
S:  Manufacturer=Linux 5.10.0-16-amd64 uhci_hcd
S:  Product=UHCI Host Controller
S:  SerialNumber=0000:02:00.0
C:  #Ifs= 1 Cfg#= 1 Atr=e0 MxPwr=0mA
I:  If#=0x0 Alt= 0 #EPs= 1 Cls=09(hub  ) Sub=00 Prot=00 Driver=hub

T:  Bus=02 Lev=01 Prnt=01 Port=00 Cnt=01 Dev#=  2 Spd=12  MxCh= 0
D:  Ver= 1.10 Cls=00(>ifc ) Sub=00 Prot=00 MxPS= 8 #Cfgs=  1
P:  Vendor=0e0f ProdID=0003 Rev=01.03
S:  Manufacturer=VMware
S:  Product=VMware Virtual USB Mouse
C:  #Ifs= 1 Cfg#= 1 Atr=c0 MxPwr=0mA
I:  If#=0x0 Alt= 0 #EPs= 1 Cls=03(HID  ) Sub=01 Prot=02 Driver=usbhid

T:  Bus=02 Lev=01 Prnt=01 Port=01 Cnt=02 Dev#=  3 Spd=12  MxCh= 7
D:  Ver= 1.10 Cls=09(hub  ) Sub=00 Prot=00 MxPS= 8 #Cfgs=  1
P:  Vendor=0e0f ProdID=0002 Rev=01.00
S:  Manufacturer=VMware, Inc.
S:  Product=VMware Virtual USB Hub
C:  #Ifs= 1 Cfg#= 1 Atr=e0 MxPwr=0mA
I:  If#=0x0 Alt= 0 #EPs= 1 Cls=09(hub  ) Sub=00 Prot=00 Driver=hub

T:  Bus=02 Lev=02 Prnt=03 Port=00 Cnt=01 Dev#=  4 Spd=12  MxCh= 0
D:  Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=2c97 ProdID=0001 Rev=02.01
S:  Manufacturer=Ledger
S:  Product=Nano S
S:  SerialNumber=0001
C:  #Ifs= 2 Cfg#= 1 Atr=c0 MxPwr=100mA
I:  If#=0x0 Alt= 0 #EPs= 2 Cls=03(HID  ) Sub=00 Prot=00 Driver=usbhid
I:  If#=0x1 Alt= 0 #EPs= 2 Cls=03(HID  ) Sub=01 Prot=01 Driver=usbhid

```

And monero-wallet-cli.log, relevant part:

```
WARNING wallet.wallet2  src/wallet/wallet2.cpp:4344     Account on device. Initing device...
DEBUG   device.ledger   src/device/device_ledger.cpp:520        Device 0 HIDUSB inited
DEBUG   device.io       src/device/device_io_hid.cpp:118        Looking for HID Device with interface_number 0 or usage_page 65440
DEBUG   device.io       src/device/device_io_hid.cpp:127        SELECTED HID Device path 0002:0004:00 interface_number 0 usage_page 0
DEBUG   device.io       src/device/device_io_hid.cpp:127        SKIPPED  HID Device path 0002:0004:01 interface_number 1 usage_page 0
DEBUG   device.ledger   src/device/device_ledger.cpp:374        CMD  : 04 02 00 00 09 00302e31372e332e32
ERROR   device.io       src/device/device_io_hid.cpp:201        Unable to send hidapi command. Error 64: hid_error is not implemented yet
INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
INFO    stacktrace      src/common/stack_trace.cpp:172      [1] ./monero-wallet-cli(+0x645077) [0x559e27cf2077] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [2] ./monero-wallet-cli(+0x8a439d) [0x559e27f5139d] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [3] ./monero-wallet-cli(+0x88ca5f) [0x559e27f39a5f] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [4] ./monero-wallet-cli(+0x88e14b) [0x559e27f3b14b] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [5] ./monero-wallet-cli(+0x88e465) [0x559e27f3b465] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [6] ./monero-wallet-cli(+0x32336b) [0x559e279d036b] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [7] ./monero-wallet-cli(+0x325386) [0x559e279d2386] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [8] ./monero-wallet-cli(+0x37de24) [0x559e27a2ae24] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [9] ./monero-wallet-cli(+0x1cd5ea) [0x559e2787a5ea] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [10] ./monero-wallet-cli(+0x2089da) [0x559e278b59da] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [11] ./monero-wallet-cli(+0x20dcfc) [0x559e278bacfc] 
INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0xea) [0x7f3fd740ed0a]:_64-linux-gnu/libc.so.6(__libc_start_main+0xea) [0x7f3fd740ed0a]
INFO    stacktrace      src/common/stack_trace.cpp:172      [13] ./monero-wallet-cli(+0x18576a) [0x559e2783276a] 
INFO    stacktrace      src/common/stack_trace.cpp:172  
ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: failed to load wallet: Unable to send hidapi command. Error 64: hid_error is not implemented yet



# Discussion History
## selsta | 2022-07-19T17:16:08+00:00
Did you compile monero-wallet-cli yourself? If yes, which libusb and which hidapi version? Does it work with release binaries from getmonero.org?

The error you posted is with libusb, but I'm not sure what it exactly means: https://github.com/libusb/hidapi/blob/master/libusb/hid.c#L1477

## pikob | 2022-07-19T17:25:04+00:00
Release binaries give same error. I tried that first, then I build debug. It did randomly work one time after retrying a couple of times.

I'm not sure if these are what is linked in debug build, but this is what is installed. If there's other way to check, let me know.

```
apt search "libusb|hidapi" | grep installed

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

libftdi1-2/stable,now 1.5-5+b1 amd64 [installed,automatic]
libgusb2/stable,now 0.3.5-1 amd64 [installed,automatic]
libhidapi-dev/stable,now 0.10.1+dfsg-1 amd64 [installed]
libhidapi-hidraw0/stable,now 0.10.1+dfsg-1 amd64 [installed,automatic]
libhidapi-libusb0/stable,now 0.10.1+dfsg-1 amd64 [installed,automatic]
libusb-0.1-4/stable,now 2:0.1.12-32 amd64 [installed,automatic]
libusb-1.0-0/stable,now 2:1.0.24-3 amd64 [installed,automatic]
libusb-1.0-0-dev/stable,now 2:1.0.24-3 amd64 [installed]
libusb-1.0-doc/stable,now 2:1.0.24-3 all [installed,automatic]
libusbmuxd6/stable,now 2.0.2-3 amd64 [installed,automatic]
```

To layman programmer me it seems that this fails to find the correct device: https://github.com/monero-project/monero/blob/9a124f681119855949f6406ecd69c2ad91da9770/src/device/device_io_hid.cpp#L106

## pikob | 2022-07-19T23:09:51+00:00
It looks like issue is with libhidapi 0.10.1 that is included in debian stable. I manually compiled hidapi 0.12.0 and added them to the build, now the issue seems to be gone. I haven't checked hidapi 0.11.2 which is currently in debian testing repos.

# Action History
- Created by: pikob | 2022-07-19T17:12:58+00:00
- Closed at: 2022-07-19T23:09:51+00:00
