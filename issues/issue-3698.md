---
title: monerod symbol not found (OSX)
source_url: https://github.com/monero-project/monero/issues/3698
author: quantumproducer
assignees: []
labels:
- invalid
created_at: '2018-04-25T02:37:04+00:00'
updated_at: '2018-07-12T23:25:01+00:00'
type: issue
status: closed
closed_at: '2018-07-12T23:25:01+00:00'
---

# Original Description
~/monero-wallet-cli
dyld: Symbol not found: __ZNK5boost16re_detail_10660031cpp_regex_traits_implementationIcE17transform_primaryEPKcS4_
  Referenced from: /usr/local/bin/monero-wallet-cli
  Expected in: /usr/local/opt/boost/lib/libboost_regex-mt.dylib
 in /usr/local/bin/monero-wallet-cli
Abort trap: 6

how do I fix this?

# Discussion History
## moneromooo-monero | 2018-04-25T09:41:54+00:00
Did you build with the same boost version ?

## jtgrassie | 2018-04-25T10:10:53+00:00
Or have you recently upgraded/changed your installed boost version?

## quantumproducer | 2018-04-25T13:28:43+00:00
Not sure, sounds like I need to rebuild boost?

## jtgrassie | 2018-04-25T13:50:50+00:00
Just rebuild monero if you already have boost installed.

## moneromooo-monero | 2018-07-12T22:17:14+00:00
Wrong boost being used by user.

+invalid


# Action History
- Created by: quantumproducer | 2018-04-25T02:37:04+00:00
- Closed at: 2018-07-12T23:25:01+00:00
