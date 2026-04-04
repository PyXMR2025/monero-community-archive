---
title: All funds lost!
source_url: https://github.com/monero-project/monero-gui/issues/3336
author: stephlo76
assignees: []
labels: []
created_at: '2021-02-11T21:14:39+00:00'
updated_at: '2021-02-11T22:00:25+00:00'
type: issue
status: closed
closed_at: '2021-02-11T21:52:41+00:00'
---

# Original Description
I again had trouble with failed transactions so I followed the advice from last time (https://github.com/monero-project/monero-gui/issues/3272) and changed the node to 78.47.80.55 and clicked Settings->Info->Change Wallet restore height. Now, all my funds are lost! Balance is 0.000 and also the transaction history is lost. I tried to set the node back to the old value with no change. How can I get my money back?

# Discussion History
## selsta | 2021-02-11T21:16:30+00:00
What is the value of "Wallet restore height" in Settings -> Info?

Did you wait for it to restore fully?

## stephlo76 | 2021-02-11T21:17:48+00:00
2294736 is the value. It is fully restored. 
![Bildschirmfoto vom 2021-02-11 22-15-55](https://user-images.githubusercontent.com/37303377/107699851-f5e1dd80-6cb6-11eb-940c-b53c2d2c242b.png)


## selsta | 2021-02-11T21:19:27+00:00
The value is only from 4 blocks ago. That explains why your funds aren't showing up.

Did you change the value when clicking on "(Change)"?

When was the first time you received funds into this wallet?

## stephlo76 | 2021-02-11T21:20:31+00:00
No, I left the value unchanged ad just clicked OK. Shall I update the value to 2294740 now? First utime I received funds was maybe a month ago.

## selsta | 2021-02-11T21:22:44+00:00
No, don't change it to 229470. You have to change it before you first received a transaction.

Try 2250000 and then wait for it to sync.

## stephlo76 | 2021-02-11T21:30:24+00:00
That saved my account, thanks!! Now I tried to repeat the failed transaction and got 
Couldn't send the money: transaction <0370a7704965b6c64be482043be3b81d27f115e1fa9065f4f732db5dc82e9614> was rejected by daemon with status: <error>. Reason: double spend, invalid input
What might be the reason for that?

## selsta | 2021-02-11T21:31:41+00:00
Is this the same node you used the first time? If yes, is it a remote node or your own?

If it is the same try to use a different node.

## stephlo76 | 2021-02-11T21:41:59+00:00
That worked (...well, still waiting for confirmation...), thanks a lot! Will I have to get used to changing the node each time I use Monero? That is a little cumbersome...

## selsta | 2021-02-11T21:42:48+00:00
No. Which node did you use previously?

## stephlo76 | 2021-02-11T21:50:46+00:00
Bitcoin with Electrum; never had any problems. With Monero, each time something strange happens

## selsta | 2021-02-11T21:52:41+00:00
Closing as the issue seems resolved.

## stephlo76 | 2021-02-11T21:53:46+00:00
Ah, which node. First I used node.supportxmr.com, then  got problems and had to change to 88.198.199.23 That one gave problems today; now I use 78.47.80.55

## selsta | 2021-02-11T22:00:25+00:00
> 88.198.199.23

That’s my node, and it seems to have had connection problems. I fixed it now.

# Action History
- Created by: stephlo76 | 2021-02-11T21:14:39+00:00
- Closed at: 2021-02-11T21:52:41+00:00
