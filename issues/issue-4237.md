---
title: Failure to Access Ledger Wallet on Linux ( Fail SCard API error )
source_url: https://github.com/monero-project/monero/issues/4237
author: bbelo
assignees: []
labels: []
created_at: '2018-08-08T09:15:09+00:00'
updated_at: '2018-10-09T08:09:01+00:00'
type: issue
status: closed
closed_at: '2018-10-09T08:09:01+00:00'
---

# Original Description
When trying to access my Ledger wallet created with monero-v0.12.2.0 I get this error:

`Couldn't open wallet: Fail SCard API : (2148532227) Invalid handle. Device=0, hCard=0, hContext=2090181845`

in both monero-gui-v0.12.3.0 and monero-v0.12.3.0

I have since found out, that switching the USB port helps to solve this issue. I believe that the concerned USB port producing this error is a USB3 port.

OS: ubuntu 16.04 LTS
HW: Generic Toshiba notebook


# Discussion History
## wuzzap | 2018-08-12T10:14:01+00:00
I have the same Issue. On every Usb Port i have. Cant solve it -.-

OS: Arch Linux
HW: Dell E7240 , Dell e6430, Asrock Z77

edit: i followed this guide to solve the problem: https://wiki.archlinux.org/index.php/Common_Access_Card

## moneromooo-monero | 2018-09-09T12:43:48+00:00
So this problem is not with monero, but wit the pcsd software/config ?

## moneromooo-monero | 2018-10-09T08:02:43+00:00
libpcsc-lite is now removed, replaced by libhidapi, so this particular bug is now moot.

+resolved

# Action History
- Created by: bbelo | 2018-08-08T09:15:09+00:00
- Closed at: 2018-10-09T08:09:01+00:00
