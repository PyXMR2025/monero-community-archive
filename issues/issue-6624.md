---
title: How to view the private key except the primary address
source_url: https://github.com/monero-project/monero/issues/6624
author: hitczw
assignees: []
labels: []
created_at: '2020-06-03T01:49:48+00:00'
updated_at: '2020-10-15T22:42:49+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:42:49+00:00'
---

# Original Description
I have a Monroe wallet and applied for several addresses. When I want to view the private key in the settings, it seems that I can only see the private key of the primary address. Is there any way to see the private key of other addresses in the account? My wallet is created in simple mode, and the new address is added through the "creat a new account" button

# Discussion History
## moneromooo-monero | 2020-06-03T10:55:27+00:00
I don't think there is. There's not much point in it. Do you have a use for it ?

## hitczw | 2020-06-03T11:40:21+00:00
Sometimes it takes hours to synchronize data. I want to export the private key to other wallets

## moneromooo-monero | 2020-06-03T11:44:09+00:00
How do you think knowing the subaddress secret keys might help here ?

## hitczw | 2020-06-03T12:01:32+00:00
I used to collect the Monero at my sub address. But when I want to transfer with a sub address, I find that I have to wait a long time to synchronize the data (possibly due to China's network control). I want to export the private key to other wallets, such as monerujo. There is a VPN software on my mobile phone witch can break the network control. But now that the problem is solved, I waited all morning to complete the data synchronization and transfer

## moneromooo-monero | 2020-06-03T12:08:44+00:00
This is not related to the subaddress secret key AFAICT. Do you think it is, and if so, why ?

## binaryFate | 2020-06-03T17:50:16+00:00
You cannot create a new wallet just for a specific existing subaddress of yours. You would have to export the seed and recreate the entire wallet.

Your long sync time has nothing to do with funds being sent to subaddress or not. When your wallet scan the missing blocks (which is probably what you are waiting for), it does not matter to which address the funds are going.

## fluffypony | 2020-06-03T17:53:03+00:00
Subaddresses aren't the same as an HD wallet in Bitcoin.

## rbrunner7 | 2020-06-03T20:04:58+00:00
I am not sure, but I think behind this question is a simple assumption: That a single Monero wallet has more than 1 secret key pair (spend key + view key) if there are more addresses than the main address, and/or accounts added.

This assumption is **false**. One Monero wallet always only has one such secret key pair, regardless of how many addresses / subaddresses and accounts are configured and in use. Everything gets derived from **one** secret spend key.


## UkoeHB | 2020-06-04T06:38:42+00:00
Having more subaddresses that own funds in a wallet doesn't affect scanning speed, so building a new wallet out of the subaddress keys would not improve anything afaik.

# Action History
- Created by: hitczw | 2020-06-03T01:49:48+00:00
- Closed at: 2020-10-15T22:42:49+00:00
