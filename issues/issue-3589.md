---
title: transferring Monero to Ledger X Hardware Wallet
source_url: https://github.com/monero-project/monero-gui/issues/3589
author: MarkyBel
assignees: []
labels: []
created_at: '2021-06-25T22:05:12+00:00'
updated_at: '2021-06-25T23:30:37+00:00'
type: issue
status: closed
closed_at: '2021-06-25T23:30:37+00:00'
---

# Original Description
yesterday i sent my monero to my Hardware wallet that i set up but i havent recieved it. i have double checked the address, i have the most updated wallet and from my end it seems to say that is synced. is there anytning im missing? anything technical that i may have to change?

appreciate any help?

# Discussion History
## selsta | 2021-06-25T22:06:12+00:00
Can you go to Settings -> Info and post the number under "wallet restore height".

## MarkyBel | 2021-06-25T22:10:33+00:00
2389801
\

## selsta | 2021-06-25T22:12:19+00:00
Could you also share the transaction id?

Also you go to Settings -> Info and post the number under "wallet mode"?

## MarkyBel | 2021-06-25T22:20:44+00:00
why do you need the transaction id?

the wallet is in simple mode


## MarkyBel | 2021-06-25T22:21:46+00:00
there is no number under the wallet mode?

## selsta | 2021-06-25T22:23:47+00:00
> why do you need the transaction id?

I need to know the block height of the transaction. I saw it now so not necessary to post it again.

> there is no number under the wallet mode?

Yes, it was a copy paste issue I meant the value.

-----------------------

Please go to Settings -> Info, click on "(Change)" next to wallet restore height and then enter `2389000` and click on okay twice. Wait for the wallet to rescan. Please report back if that works, if not I have to give further instructions.

## MarkyBel | 2021-06-25T22:26:50+00:00
it says it will delete the recieve adress etc? is that right?


## selsta | 2021-06-25T22:27:40+00:00
yes

## MarkyBel | 2021-06-25T23:21:57+00:00
says its startring node.

thanks very much for the help?

## MarkyBel | 2021-06-25T23:27:33+00:00
i tried that but the number doesnt seem to be staying there. there is no number next to the block height


## MarkyBel | 2021-06-25T23:30:18+00:00
its worked.

thank you so so much

## selsta | 2021-06-25T23:30:37+00:00
Great :)

# Action History
- Created by: MarkyBel | 2021-06-25T22:05:12+00:00
- Closed at: 2021-06-25T23:30:37+00:00
