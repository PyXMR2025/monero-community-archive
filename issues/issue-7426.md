---
title: Incorrect Balance Total
source_url: https://github.com/monero-project/monero/issues/7426
author: LotannaEzenwa
assignees: []
labels: []
created_at: '2021-03-05T11:57:23+00:00'
updated_at: '2021-03-05T13:09:30+00:00'
type: issue
status: closed
closed_at: '2021-03-05T13:03:39+00:00'
---

# Original Description
Good Morning,

I am trying to verify the total monero balance on my primary and created addresss.

I created 2 addresses, and made transactions to each.

I am able to verify that these created addresses received the correct amount of monero via the monero-gui and two third party blockchain analyses. 

My wallet is also completely synced 100+ blocks past either transaction.

However, when using `balance` in the cli, and using the gui, my total balance is shown as 0.00000000. Also, using `show_transfers in` gives no transactions.

I have a Trezor wallet, and I am connected to a remote node.

Please advise.

# Discussion History
## moneromooo-monero | 2021-03-05T12:02:55+00:00
Are the GUI and CLI running on the same wallet file ? What are third party blockchain analyses ?

## LotannaEzenwa | 2021-03-05T12:05:12+00:00
Yes, GUI and CLI are running on the same wallet file. 

Third party blockchain analyses are 
https://blockchair.com
and
https://xmrchain.net

## moneromooo-monero | 2021-03-05T12:06:14+00:00
Does show_transfers show anything ?

## LotannaEzenwa | 2021-03-05T12:07:13+00:00
`show_transfers` returns nothing

## moneromooo-monero | 2021-03-05T12:09:11+00:00
Does incoming_transfers show anything ?

## LotannaEzenwa | 2021-03-05T12:12:09+00:00
"No incoming transfers"

## moneromooo-monero | 2021-03-05T12:13:48+00:00
What is the value of refresh-from-block-height in the output of "set" ?

## LotannaEzenwa | 2021-03-05T12:14:30+00:00
Value is 2289630

## moneromooo-monero | 2021-03-05T12:15:24+00:00
At what block heights did the incoming txes get mined ?

## LotannaEzenwa | 2021-03-05T12:17:23+00:00
The first was slightly after 2310000, both within 100 blocks of each other.

## moneromooo-monero | 2021-03-05T12:18:36+00:00
What does "status" show in the wallet ?

## LotannaEzenwa | 2021-03-05T12:19:13+00:00
"Refreshed 2310331/2310331, synced, daemon RPC v3.2, SSL"

## moneromooo-monero | 2021-03-05T12:20:18+00:00
Did the incoming txes go to accounts or addresses with large minor or major indices ?

## LotannaEzenwa | 2021-03-05T12:22:37+00:00
Please clarify 'large minor or major indices'.

Txns went to addresses 1 and 2 of newly generated account and wallet.

## moneromooo-monero | 2021-03-05T12:23:40+00:00
Small enough. What is the value of subaddress-lookahead in the output of "set" ?

## LotannaEzenwa | 2021-03-05T12:24:58+00:00
Ah, subaddress lookahead is "5:20"

## moneromooo-monero | 2021-03-05T12:26:10+00:00
So, to make sure I understand, the CLI shows no transactions and the GUI shows transactions on the same wallet file ?

## LotannaEzenwa | 2021-03-05T12:26:57+00:00
Yes, both show no transactions on the same wallet file.

> For sanity, I am able to generate a transaction proof in the GUI, then verify the amount received from that transaction proof in the GUI as well.

## moneromooo-monero | 2021-03-05T12:28:37+00:00
If the GUI also shows no transactions, what did you mean by: I am able to verify that these created addresses received the correct amount of monero via the monero-gui

## LotannaEzenwa | 2021-03-05T12:31:42+00:00
While the GUI itself shows no transactions, I am able to go into the advanced settings of "prove/check" and use that workflow successfully.

I received two txn ids from a sender, then used those txn id in the gui (and on third party analyses) along with my generated addresses to generate txn proofs within the GUI.

Then I used those txn proofs generated in the GUI to verify the amount sent to each address. i.e. the GUI created an alert which read something along the lines of "Address XXXXX received YY.Y Monero"

## selsta | 2021-03-05T12:33:29+00:00
Did you use different accounts? Can you restore your wallet with a different remote node? E.g. node.xmr.to 18081

## moneromooo-monero | 2021-03-05T12:33:33+00:00
And you're really sure you are looking in the right wallet (sorry) ?

## LotannaEzenwa | 2021-03-05T12:38:54+00:00
@moneromooo-monero no worries, I am sure I am looking in the right wallet. I have just reverified this process using only copy/paste (i.e. copy address 1 and 2 from within monero-gui)

@selsta How would I go about doing that?

## moneromooo-monero | 2021-03-05T13:01:07+00:00
"rescan_bc" (after setting your daemon to another, there are many asshole nodes offering public RPC, might be lying about txes, always run your own node if you want to be secure - might not be the cause here though, but it certainly looks odd)

## LotannaEzenwa | 2021-03-05T13:03:39+00:00
`rescan_bc` worked and the txns have appeared in total balance. 
Thank you both for your assistance. @moneromooo-monero @selsta 

I was using moneroworld.com's nodes, for all who may see this in the future. `node.xmr.to:18081` worked.

## selsta | 2021-03-05T13:05:45+00:00
moneroworld aggregates "trusted" nodes so I doubt that asshole nodes were the culprit here.

## moneromooo-monero | 2021-03-05T13:06:13+00:00
I thought it was anything that was listening on 18089 ?

## selsta | 2021-03-05T13:06:49+00:00
It was changed some time ago.

## LotannaEzenwa | 2021-03-05T13:09:30+00:00
I would like to edit this to say that I had tried to refresh and rescan many times, but the Trezor only just now asked if I would like to refresh after changing nodes and stopping the daemon. Not sure if that's an issue for anyone else. 

# Action History
- Created by: LotannaEzenwa | 2021-03-05T11:57:23+00:00
- Closed at: 2021-03-05T13:03:39+00:00
