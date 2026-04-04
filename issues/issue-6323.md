---
title: Manually adding sub addresses to wallet
source_url: https://github.com/monero-project/monero/issues/6323
author: godfuture
assignees: []
labels: []
created_at: '2020-02-07T15:15:17+00:00'
updated_at: '2022-03-16T15:50:52+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:50:52+00:00'
---

# Original Description
I have transferred/recovered my wallet created on desktop to my Android phone. It simply worked, my main account was available on both devices...but...once you create a sub address on desktop or phone, you will not be able to see this sub address on the other device.

This could be easily solved by allowing to add the missing sub address manually.

v0.15.0.1

# Discussion History
## moneromooo-monero | 2020-02-07T16:30:46+00:00
And... it fails to ?

## ndorf | 2020-02-22T06:39:12+00:00
@godfuture subaddresses are deterministic and generated in the same order. So, if you generate one in the new wallet, it will be the same as the first one (index=1) from your old wallet.

## godfuture | 2020-02-27T21:28:59+00:00
> @godfuture subaddresses are deterministic and generated in the same order. So, if you generate one in the new wallet, it will be the same as the first one (index=1) from your old wallet.

Maybe this is not about subaddresses. I am speaking of the feature "create new address". I have compared these additional addresses on desktop and android. They are not the same. Should I rename the topic?

## moneromooo-monero | 2020-03-01T01:53:29+00:00
Yes. They're supposed to be the same. First though, double check you're really checking addresses with the same indices. 

## moneromooo-monero | 2020-03-30T13:40:27+00:00
ping

## godfuture | 2020-05-12T23:14:46+00:00
Instead of adding a new random account, I would like to specify the key myself, for the reason mentioned above. I have my wallet on both devices. As the blockchain is anyhow the same, two wallets would not really add benefit, but more complexity (coins distributed over multiple places, additional backup, more addresses).
![grafik](https://user-images.githubusercontent.com/4669278/81754688-175b3200-94b7-11ea-9188-fbb489d17d2b.png)


## moneromooo-monero | 2020-05-13T14:09:14+00:00
You can do that in the CLI by specifying the account/subaddress indices. If you mean adding *arbitrary* keys, then that's not how monero works, so no to that. Subaddresses (including accounts) are deterministic, so if you generate some in two wallet files that have the same keys, you'll get the same subaddresses in both. Not sure if that's what you were asking.


# Action History
- Created by: godfuture | 2020-02-07T15:15:17+00:00
- Closed at: 2022-03-16T15:50:52+00:00
