---
title: Permission denied error for monero-blockchain-blackball
source_url: https://github.com/monero-project/monero/issues/3915
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2018-06-03T19:00:42+00:00'
updated_at: '2018-09-14T12:01:06+00:00'
type: issue
status: closed
closed_at: '2018-09-14T12:01:06+00:00'
---

# Original Description
Original post on StackExchange [here](https://monero.stackexchange.com/questions/8485/permission-denied-error-for-monero-blockchain-blackball).

I'm attempting to run the monero-blockchain-blackball utility in PureOS, and I'm running into a permission error.

I used the syntax to select the tool, then the Monero blockchain, then a forked blockchain (I'm using Monero v6 for testing). The syntax is described [here](https://monero.stackexchange.com/questions/8225/how-can-i-use-monero-blockchain-blackball-to-improve-my-privacy).

Upon running the command, I receive the following text:

[![Failed to create a transaction for the db: Permission denied][1]][1]


  [1]: https://i.stack.imgur.com/orfSs.png

I deleted the `/.shared-ringdb` folder, but the error persists.

# Discussion History
## stoffu | 2018-06-04T03:10:41+00:00
#3919 

## stoffu | 2018-06-04T08:56:45+00:00
It turns out that the above patch is still not enough for processing the old v6 chains due to DB version mismatch, see #3923 

## moneromooo-monero | 2018-09-14T11:22:49+00:00
+resolved

# Action History
- Created by: SamsungGalaxyPlayer | 2018-06-03T19:00:42+00:00
- Closed at: 2018-09-14T12:01:06+00:00
