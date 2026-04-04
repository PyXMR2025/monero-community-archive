---
title: get_output_histogram unlocked flag logic scenarios
source_url: https://github.com/monero-project/monero/issues/6871
author: VanGrx
assignees: []
labels: []
created_at: '2020-10-08T13:34:42+00:00'
updated_at: '2020-10-26T15:27:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In get_output_histogram function, if unlocked flag is turned on, the code goes to the following part:

        const tx_out_index toi = get_output_tx_and_index(amount, num_elems - 1);
        const uint64_t height = get_tx_block_height(toi.first);
        if (height + CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE <= blockchain_height)
          break;
        --num_elems;

But, in case the tx is locked for more than CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE, daemon will return locked output.

A solution would be something like this:

        const tx_out_index toi = get_output_tx_and_index(amount, num_elems - 1, output_type);
        const uint64_t height = get_tx_block_height(toi.first);
        const uint64_t unlock_time = get_tx_unlock_time(toi.first);
        if (blockchain_height - 1 + CRYPTONOTE_LOCKED_TX_ALLOWED_DELTA_BLOCKS >= unlock_time && height + CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE <= blockchain_height)
          break;
        --num_elems;

or to add is_tx_spendtime_unlocked function inside the lmdb and check if output is unlocked there.

Also, not sure if the logic `if (unlocked || recent_cutoff > 0)` should be split to 2 ifs?



# Discussion History
## moneromooo-monero | 2020-10-08T21:01:07+00:00
That would allow someone to make an output that's locked forever and complete screw up everyone's rings, no ?

## VanGrx | 2020-10-09T11:41:18+00:00
Let's say we have 3 types of tx outputs:

unlocked, locked, non_spendable

If we get histogram the way it is, we get


`uuuuuullllllnnnnn`
 `-----------^`
`outputs until here`

But if we select outputs from u and l, there is a chance we will not have enough for mixin if too much l outputs are selected. If we add check for locked then histogram will return

`uuuuuullllllnnnnn`
 `-----^`
`outputs until here`

This is actually special scenario for miners tx because they are locked for

CRYPTONOTE_MINED_MONEY_UNLOCK_WINDOW            60

Now that I think about that, there is also this scenario 

`uuuluuululluuullnnnnn`

where histogram will return smaller number of outputs, but they still can be selected. Maybe a better approach instead of my first comment should be to add a check if output is a mining transaction and if height of tx is less than `blockchain_heigh - CRYPTONOTE_MINED_MONEY_UNLOCK_WINDOW`.

This way, we remove mined tx outputs for sure, and as wallet is selecting 1.5x of needed mixins, if it gets too much locked txs, by retrying user should send tx with new random outputs selected.

 Do You agree with this? Hope I explained scenario and a potential fix.

## moneromooo-monero | 2020-10-10T22:18:06+00:00
What distinction are you making between locked and non_spendable ?

## VanGrx | 2020-10-11T11:09:29+00:00
Yes. Sorry. 
Locked means output unlock height is still not reached.
Non_spendable is when CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE for that output has not passed. 

## moneromooo-monero | 2020-10-11T13:42:55+00:00
So what is your suggestion here ? As far I as understand, you want to stop at the first locked output, rather than the first output that is within CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE of the tip. Is that correct ?

## VanGrx | 2020-10-11T20:40:40+00:00
So, the code logic right now goes like this:

Start from the LAST output in total and if current output is within CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE range, reduce num_outputs by one. When we get the first output that is not within CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE, we exit the loop, and we return num_outputs that can be spent in the wallet. However, this is including locked outputs(can be locked by user giving bigger locked period) and miner tx outputs that need more block period to be unlocked.

My proposition is to extend the loop until CRYPTONOTE_MINED_MONEY_UNLOCK_WINDOW range is exited. This way, miner tx outputs will not be selected and we evade case when too much miner tx outputs are selected for mixin and we cannot create a transaction.

## moneromooo-monero | 2020-10-12T15:57:24+00:00
That will make people who spend their outputs before 60 blocks essentially have no ring signatures.

## VanGrx | 2020-10-13T17:55:06+00:00
But as I understand, this function is returning only number of outputs that can be selected and wallet is selecting from that number the ones for ring signatures. By this change, only number of outputs is reduced. 

I understand Your concerns, so logic can be expanded to go after CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE and continue until first unlocked output. This way, if there are a lot of miner outputs and locked txs for selection, they will be removed from possible outputs. Do You think this logic is better?

## moneromooo-monero | 2020-10-14T12:01:07+00:00
It will require loads of traffic from the daemon, and lots more work. Instead of a number, you send N flags, N close to the number of outputs. The daemon also has to scan all outputs to see which are locked, rather than just the few last dozens.


## VanGrx | 2020-10-20T11:47:10+00:00
Yes, I agree that that will be a proper solution and it is too much load on the dameon, but going until the first unlocked found can improve the current logic and it will not increase the load. You will still have some locked outputs, yes, but wallet is selecting 1.5x of the number he needs for mixin. With selection until first unlocked output, we can decrease number of outputs that are returned. For example:

`uuuluuululluuulllllnnnnn`

current implementation will go until the most right l.

`uuuluuululluuulllllnnnnn`
`------------------^`
 Improved will go until the most right u.

`uuuluuululluuulllllnnnnn`
`-------------^`

 so the wallet will not consider any of the locked outputs on the right. The number of outputs will be without n and without l that are on the left side until the first unlocked that can be used.  

## moneromooo-monero | 2020-10-22T01:48:26+00:00
OK, I see that what you suggest will not change much daemon load or RPC traffic.
It might skew the distribution of fake outs, though I doubt it will be by very much since this version is not vulnerable to one long locked output.
Now, what benefits would the change bring ?

## VanGrx | 2020-10-26T15:26:53+00:00
> It might skew the distribution of fake outs

Not sure, as selecting these outputs for distribution will return locked outputs that would not be used at the end. Right?

>  Now, what benefits would the change bring ?

More stable wallet and tx creation, as now there is a situation when too much outputs that are selected are locked and wallet cannot create a transaction as not enough outputs for mixins are returned.

# Action History
- Created by: VanGrx | 2020-10-08T13:34:42+00:00
