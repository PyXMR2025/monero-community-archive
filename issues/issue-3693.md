---
title: the image file xmrig.exe is valid, but is for machine type other than current
  machine
source_url: https://github.com/xmrig/xmrig/issues/3693
author: CorkPromo
assignees: []
labels: []
created_at: '2025-08-12T20:21:45+00:00'
updated_at: '2025-08-14T08:31:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello!
I am new user. have configured as per manual. Run on machine with CPU Asus i7.
How to fix it?

# Discussion History
## geekwilliams | 2025-08-12T22:16:54+00:00
What operating system are you using? 

## CorkPromo | 2025-08-13T04:59:56+00:00
Processor	Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz (1.50 GHz)
Installed RAM	8.00 GB (7.75 GB usable)
System type	64-bit operating system, x64-based processor
Edition	Windows 11 Home
Version	24H2
Installed on	‎11/‎11/‎2024
OS build	26100.4946
Experience	Windows Feature Experience Pack 1000.26100.197.0



## geekwilliams | 2025-08-13T14:07:13+00:00
How are you attempting to run the application? 

## CorkPromo | 2025-08-13T16:47:43+00:00
Have created .bat file with - xmrig.exe --donate-level 5 -o 127.0.0.1:18081 -u WalletNr --coin monero --daemon --tls -o xmr.pool.gntl.co.uk:20009 -u MyWalletNr -k --tls -p Worker

## SChernykh | 2025-08-13T19:24:33+00:00
Double check what archive you downloaded
```
 xmrig-6.24.0-windows-arm64.zip
```
is only for Windows on ARM systems. If you downloaded it, it will not work on Intel(R) Core(TM) i7-1065G7 CPU

You need to download `xmrig-6.24.0-windows-x64.zip`

## CorkPromo | 2025-08-14T08:31:20+00:00
Thanks. Sorted. You were right. 

# Action History
- Created by: CorkPromo | 2025-08-12T20:21:45+00:00
