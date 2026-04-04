---
title: 'Ledger device not found after updating firmware (2.0.0) and Monero application
  (1.7.6) within Ledger Live '
source_url: https://github.com/monero-project/monero-gui/issues/3482
author: ghost
assignees: []
labels: []
created_at: '2021-05-16T14:51:41+00:00'
updated_at: '2021-07-13T22:20:48+00:00'
type: issue
status: closed
closed_at: '2021-07-13T22:20:48+00:00'
---

# Original Description
Running CLI 17.2.0 on Mac OS X (have also tried the latest GUI release and featherwallet).  

I installed Ledger firmware update and also updated the Ledger app to the latest version.  Ledger Live is able to recognize my device so long as Monero application is not running.  When I open the Monero application on my Ledger, it disconnects from Ledger Live.  At this point my Ledger device is connected, unlocked, and the Monero application is running, monerod has synced with the netowrk and I launch monero-wallet-cli.  My wallet and key files are found and I enter my password.  I receive an error "Error: failed to load wallet: No device found."  Following this same process, but with Ledger Live closed, results in the same error.  

I have restarted my Ledger and Mac, and have reset PRAM on my Mac as well (suggested in Ledger support article). I have tried multiple USB ports on my Mac, but again Ledger Live is able to connect to my device without problem when Monero application is not running. Below is the text which is appended to monero-wallet-cli.log each time I attempt to access my wallet unsuccessfully: 

> 2021-05-16 02:27:52.103	     0x110cdae00	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO


# Discussion History
## selsta | 2021-05-17T20:00:53+00:00
Did this work before updating your Ledger firmware? Or did it never work?

## selsta | 2021-05-17T20:14:04+00:00
Also which macOS version?

## ghost | 2021-05-18T01:51:58+00:00
The CLI worked previously in order to access my Ledger wallet. Since the last successful access of my wallet I have upgraded Ledger firmware, Monero application through Ledger Manager (v1.7.6) and have also upgraded to Mac OS X 11.3.1 

## ghost | 2021-05-22T15:30:49+00:00
I was able to add udev rules on a Linux machine and am in the process of restoring my wallet.  The device was never able to be found on mac, but after adding udev on Linux it was recognized and connected.  The issue appears to be related to the Mac OS X 11.3.1 update since I was able to use on OS X 11.2 

## selsta | 2021-05-25T03:34:21+00:00
I can't reproduce with macOS 11.3.1

## selsta | 2021-07-13T22:20:48+00:00
Closing, this discussion can continue in #3622

# Action History
- Created by: ghost | 2021-05-16T14:51:41+00:00
- Closed at: 2021-07-13T22:20:48+00:00
