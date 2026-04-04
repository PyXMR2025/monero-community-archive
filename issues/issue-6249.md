---
title: peer claims higher version that we think (60 for 1998284 instead of 12) - we
  may be forked from the network and a software upgrade may be needed
source_url: https://github.com/monero-project/monero/issues/6249
author: TheBudda
assignees: []
labels:
- invalid
created_at: '2019-12-18T00:51:23+00:00'
updated_at: '2020-01-10T02:01:31+00:00'
type: issue
status: closed
closed_at: '2019-12-18T02:09:29+00:00'
---

# Original Description
I have been running a monero for many years now. I am now getting this error below. I have tried compiling from the master with no issues. I have tried your pre-compiled binary files and still get the same errors below  

peer claims higher version that we think (60 for 1998284 instead of 12) - we may be forked from the network and a software upgrade may be needed

monerod is running on an OVH dedicated server
Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
OS: Ubuntu Linux 18.04.3

Please see attached screenshot

Kind regards
TheBudda
![monderod_Screenshot](https://user-images.githubusercontent.com/16983376/71046537-80b95d80-2130-11ea-9235-ea154655e543.png)


# Discussion History
## TheBudda | 2019-12-18T00:52:26+00:00
My server system is running the correct time clocks set to London, United Kingdom

## hyc | 2019-12-18T01:59:36+00:00
+invalid

This is not an error, ignore it.

## ahook | 2020-01-10T01:46:00+00:00
FYI, the handful of peers currently sending version 60 for forks are most likely Monero Classic nodes that connected to the wrong network.

https://github.com/monero-classic/monero/blob/master/src/cryptonote_core/blockchain.cpp#L112

# Action History
- Created by: TheBudda | 2019-12-18T00:51:23+00:00
- Closed at: 2019-12-18T02:09:29+00:00
