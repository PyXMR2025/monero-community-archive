---
title: Fork to Argon/ArgonNight
source_url: https://github.com/monero-project/monero/issues/5085
author: ClashLuke
assignees: []
labels: []
created_at: '2019-01-20T00:34:56+00:00'
updated_at: '2019-01-20T06:41:01+00:00'
type: issue
status: closed
closed_at: '2019-01-20T06:41:01+00:00'
---

# Original Description
Regarding the current hype for Argon and Monero's and Aeon's IoT friendliness.
It would certainly be possible to make a move in the direction of Argon or ArgonNight.
As of right now, the only major projected I noticed working towards this goal would be Turtlecoin.
Since I personally don't know whether this has scientific reasoning or if you were busy with other things, I will propose a change of CryptoNight (or CryptoNight-Lite in case of Aeon) to Argon2d or even ArgonNight.
An unclean reference implementation can be found in here:
https://github.com/Tax-Project/Test-Tax/blob/master/src/crypto/slow-hash.c#L862

If argon would be preferred over ArgonNight, it would certainly be possible to remove everything apart from what currently is the initialization. If you really want to have the optimal cycles per byte and don't care about ASICs, you could always go with Argon without any support such as the keccak which still is there in ArgonNight.

Advantages of Argon and ArgonNight over CryptoNight would be the following:
-- Increased IoT friendliness
-- Increased Hashrate
---- Increased Verification Speeds
---- Increased Security against (D)DoSing
-- Increased ASIC resistance
-- Easier Rebalancing of CPU Hashrate to GPU Hashrate
-- Higher Modularity and therefore a higher chance that people will tweak variables or implement slight changes to further increase ASIC resistance of the whole CryptoNote ecosystem.

Thanks for reading this proposal, and not to worry, I could implement Argon or ArgonNight into Monero, in case its decided to be the next algorithm. It is only about whether or not the community would like to see it implemented.


# Discussion History
## hyc | 2019-01-20T01:16:58+00:00
>-- Increased Hashrate
>---- Increased Verification Speeds

Hash rate is not what secures a network, energy is. This is moronic.

## ClashLuke | 2019-01-20T01:25:49+00:00
That's interesting because you actually linked the reason why I think it's important.

An increased hashrate obviously increases verification speeds. The hashrate gets increased since argon is significantly faster than CryptoNight.
Faster verifications mean higher synchronisation speeds and higher validation speeds for transactions or blocks sent by attacking nodes.

I don't see where exactly your issue is, so please elaborate further.

EDIT: Rereading your message, I get the feeling that this was a slight misunderstanding. I was referring to nodes sending invalid blocks and using those to (D)DoS the network and slow it down a lot. On the other hand you seem to be refering to the point that it doesn't matter how high you hashrate it, as long as everyone's hashrate gets multiplied with the same factor there will be no difference to the security. And I agree with this point, but that's not what I was refering to. I probably should've clarified that in my message. Thanks for pointing that out.

# Action History
- Created by: ClashLuke | 2019-01-20T00:34:56+00:00
- Closed at: 2019-01-20T06:41:01+00:00
