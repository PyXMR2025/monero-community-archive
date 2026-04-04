---
title: Too big amounts are sent and received back for every transaction.
source_url: https://github.com/monero-project/monero/issues/2351
author: miningpoolhub
assignees: []
labels: []
created_at: '2017-08-26T09:29:16+00:00'
updated_at: '2017-08-26T16:23:10+00:00'
type: issue
status: closed
closed_at: '2017-08-26T16:23:10+00:00'
---

# Original Description
Hi
I am running monero pool.
https://monero.miningpoolhub.com

When I send 1 XMR to some address, 1000 XMR is sent and 999 XMR gets back.
I know why it works like this but I need to payout many many miners and I have to wait several minutes to confirm the change amount.
So many payouts are delayed more than a day currently.

I already asked about this issue few months ago at forum and couldn't get clear solution.
What can I do to reduce this happening?

Maybe increase/decrease mixin parameter helps?
Divide wallet?
Is there sendmany like API that supports paymentId?




# Discussion History
## moneromooo-monero | 2017-08-26T10:11:29+00:00
You can send 50 monero 20 times in one tx to yourself (make sure you have set merge-destinations to 0 first). This will break up the 1000 output.
Also set min-outputs-count and min-outputs-value to, say, 20 and 10, see the commit message for 0ad87db01f19eff22ab9c3998826b7aa943975cf for an explantion of how they work. Last, you can pay several destinations in the same tx, which means no intervening change. Payment id is per tx, so if you have two payment ids, you have to make two txes at least. Just make the payout limit higher for people with a payment id.

## miningpoolhub | 2017-08-26T13:53:41+00:00
@moneromooo-monero 
Thank you for detailed answer.
Is there any way to set min-outputs-count and min-outputs-value to simplewallet rpc?

I searched and read source code but still bit confused that there's no way to set those variables for rpc simplewallet. Those info seems like to be saved in wallet file itself but don't know how to set from outside.

------
UPDATE

I closed rpc process and opened wallet file from monero-wallet-cli. Changed variables and saved wallet file.
Seems it's working. Don't know whether it's normal approach.


## moneromooo-monero | 2017-08-26T14:44:40+00:00
Yes, you did it right.


## miningpoolhub | 2017-08-26T16:23:02+00:00
Thanks!

# Action History
- Created by: miningpoolhub | 2017-08-26T09:29:16+00:00
- Closed at: 2017-08-26T16:23:10+00:00
