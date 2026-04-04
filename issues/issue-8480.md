---
title: 'sweep_* command: Please add an "error" when args (index and address) are incorrectly
  placed'
source_url: https://github.com/monero-project/monero/issues/8480
author: afungible
assignees: []
labels: []
created_at: '2022-08-02T23:41:01+00:00'
updated_at: '2023-05-25T21:49:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

This is my first post on Monero. I am reporting a strange behavior that I recently found, which I likely find a bug. Let me detail as below:

Assume a wallet with 6 unspent outputs (under account Index: 0, 5 sub-addresses and 1 primary address, with balances as below:
 
```
1. 0.000000001000
2. 0.000000001000
3. 0.000000001000
4. 0.000000001000
5. 0.000000001000
6. 0.100000000000
```
Notice, 5 of the above addresses have negligible amount. Negligible, with respect to "network fee" i.e. (~0.000005 XMR).

As funds sit on transactions' unspent outputs and in principle, a single transaction should be able to aggregate and spend outputs from multiple addresses (and by extension from multiple accounts). However, in the above scenario when the balance at a "sub-address" is less than the "network fee", that output is not being spent.
 
I also validated this by splitting an output into multiple small chunks and sweeping it off my wallet. I realized later this was the exact problem as posted below, the reason the wallet is not being emptied (off dust) in spite of adding sufficient amount to the wallet to clear it up. A balance of 000000005000 XMR is not possible to be spent.
 
https://www.reddit.com/r/Monero/comments/wcaykc/sadly_my_monero_practically_lost_forever/
 
This has three potential problems going forward:
1) People donating very small amounts to an address, would forever remain unspent at that address
2) Reduces Monero supply with growing adoption
3) This can become an issue when the network fee increases in future, thus blocking out greater amounts

This is just like saying cent, nickel and dime have no value today and cannot be spent. This should not be the case for digital money.
 
Looking forward to any views.

Cheers,
aFungible


# Discussion History
## moneromooo-monero | 2022-08-03T04:54:37+00:00
set ignore-fractional-outputs 0

## afungible | 2022-08-04T09:40:28+00:00
I tried setting "ignore-fractional-outputs" to 0, and "sweep_all" to another wallet. Added more than enough for fees. Also, paid higher than the min. fees i.e. 0.00005105XMR (0.0083USD), perhaps due to combining outputs.

**My conclusion:**
Same result. Clearing up balance from (sub) address outputs that have (**balance < transfer_fee**) cannot be retrieved/used as of v0.17.3. So, perhaps the output selection algorithm needs a look.

![image](https://user-images.githubusercontent.com/108204668/182823636-77bebf91-49c1-4e5f-bd2b-683fe35dd9e4.png)



## afungible | 2022-08-04T11:57:56+00:00
Log attached with --log-level 2:
[__unspent_op_wallet.log](https://github.com/monero-project/monero/files/9259410/__unspent_op_wallet.log)

This time, I added a greater balance to the account and repeated the steps. Same end result.

Last Line in log 767, after sweeping the account:
Balance: 0.**000001900240**, unlocked balance: 0.000001900240

I hope this would suffice.



## moneromooo-monero | 2022-08-04T12:25:20+00:00
Can you please run again with this patch ? Apply by saving to, eg, /tmp/wallet.diff, then run: patch -p1 < /tmp/wallet.diff

It'll log data about each output at log level 0, from which we can see why some outputs aren't being used.

```
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index 195763949..9aad1272b 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -10483,9 +10483,12 @@ std::vector<wallet2::pending_tx> wallet2::create_transactions_all(uint64_t below
 
   // gather all dust and non-dust outputs of specified subaddress (if any) and below specified threshold (if any)
   bool fund_found = false;
+MGINFO("create_transactions_all: checking " << m_transfers.size() << " outputs, major " << subaddr_account << ", " << subaddr_indices.size() << " minors, " << use_rct << " " << below << " " << m_ignore_fractional_outputs << " " << fractional_threshold);
+for (uint32_t m: subaddr_indices) MGINFO("  minor " << m);
   for (size_t i = 0; i < m_transfers.size(); ++i)
   {
     const transfer_details& td = m_transfers[i];
+MGINFO("" << i << ": " << td.amount() << " " << td.m_frozen << " " << td.m_key_image_partial << " " << td.is_rct() << " " << is_transfer_unlocked(td) << " " << td.m_subaddr_index.major << " " << is_spent(td, false) << " " << td.m_subaddr_index.major << ":" << td.m_subaddr_index.minor << " " << is_valid_decomposed_amount(td.amount()));
     if (m_ignore_fractional_outputs && td.amount() < fractional_threshold)
     {
       MDEBUG("Ignoring output " << i << " of amount " << print_money(td.amount()) << " which is below threshold " << print_money(fractional_threshold));
```

## afungible | 2022-08-04T15:22:21+00:00
I included your patch, compiled and below is the detailed log:
[patch_debug_unspent_op_wallet.log](https://github.com/monero-project/monero/files/9260979/patch_debug_unspent_op_wallet.log)

Transfer successful. Balance left: 0.000001900240 XMR

**May have found another issue:**
Also, "prior to above transfer" and while operating on the "very same unlocked outputs", I could not use sweep_account OR sweep_all, in spite of everything being the same. I tried "transfer <addr>" cancelled the operation and then sweep "started working". I found this very strange, but I might have just found another issue. So, log attached for it below:

[transfer_not_possible.log](https://github.com/monero-project/monero/files/9260893/transfer_not_possible.log)

It basically showed:
wanted 0.000007700001, found 0.000000000060, fee 0.000007700000
Tries to spend from subaddress: 6
found_money < needed_money. THROW EXCEPTION: error::not_enough_unlocked_money

whereas, it should have showed:
wanted 0.000005670001, found 0.000800000000, fee 0.000005670000
Actually, spends from subaddress:8
and is able to spend it.

You can confirm that in both cases account had (unlocked) balance greater than 000800000000 ready to be moved.


## moneromooo-monero | 2022-08-04T15:26:02+00:00
The log is not a log, it seems to point to this bug's url.

## moneromooo-monero | 2022-08-04T15:26:48+00:00
nvm, the link changed it's good now.

## afungible | 2022-08-04T15:26:54+00:00
Just updated. Please check again.

## afungible | 2022-08-04T16:30:36+00:00
**At the start of test:**
balance (all accounts): 0.000701900240, unlocked: 0.000701900240
(balance will cover fees)

Attempted "sweep_all" twice, first time failed, second time succeeded.

**1st attempt:**
sweep_all <addr> index=0,1,2,3,4,5,6,7,8
Line of interest: 293 (Exception: tools::error::not_enough_unlocked_money)

**2nd attempt:**
sweep_all <addr> index=0,1,2,3,4,5,6,7,8
Line of interest: 1133 (Transaction successfully sent)
Balance: 0.000001900240

No difference in result. Dust balance is still stuck in wallet.
[sweep_all_all_indices.log](https://github.com/monero-project/monero/files/9261562/sweep_all_all_indices.log)


In addition to the reported issue, I am curious as to why we would receive error on the first attempt?


## moneromooo-monero | 2022-08-04T16:37:42+00:00
From the log, it looks like it's ignoring the index= settings.

## moneromooo-monero | 2022-08-04T16:38:26+00:00
It's trying to spend from different indices, 5 and 8. Not enough money in 5.

## moneromooo-monero | 2022-08-04T16:39:53+00:00
Ooh, I see a "index=all" override, away from the normal parsing.

## moneromooo-monero | 2022-08-04T17:27:03+00:00
I setup a test case here, and I do get my minors properly taken into account. Can you share the exact command you used (placeholder for address is fine) ? Your post just has " sweep_all index=0,1,2,3,4,5,6,7,8" which is not a valid command. I used "sweep_all index=0,1,2,3 44nfYswDeX8AokAekad5jCirL8XRuqEg2D54HUd4VPmwHix5SM6iFdTd2RM9HVXUV5VpBiUWzjuXcQjxgK8im6tETN4YYG5", and my logs show 4 minors, rather than 0 like in your log.

## afungible | 2022-08-04T17:42:13+00:00
Sorry, since the address was long I skipped it. I used the following:

`sweep_all 86AKubqhJnMXrU8B9tSL6QgvjHtUzHs61BDPZDGk9gW2HKKrqWzjBPyXz3Ksbi8eVdN623pAnxKgM5hicYVRjPUYA6Kwhue index=0,1,2,3,4,5,6,7,8`

## moneromooo-monero | 2022-08-04T17:48:31+00:00
index= goes first.

## afungible | 2022-08-04T17:53:15+00:00
Perhaps, under _sweep_all_ command usage, it could be nice to have a usage example for users, like:

`sweep_all index=0,1,2,3,4,5,6,7,8 86AKubqhJnMXrU8B9tSL6QgvjHtUzHs61BDPZDGk9gW2HKKrqWzjBPyXz3Ksbi8eVdN623pAnxKgM5hicYVRjPUYA6Kwhue
`
Can avoid any confusion or at least if the args are not in correct order, it could complain.

Let me top up my wallet and get this right :) brb

## afungible | 2022-08-04T18:24:58+00:00
Indeed, it worked out this time. It was the format of the args.

```
[wallet 4AW1gK]: balance
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000701900240, unlocked balance: 0.000701900240
[wallet 4AW1gK]: sweep_all index=0,1,2,3,4,5,6,7,8 86AKubqhJnMXrU8B9tSL6QgvjHtUzHs61BDPZDGk9gW2HKKrqWzjBPyXz3Ksbi8eVdN623pAnxKgM5hicYVRjPUYA6Kwhue
Wallet password: 

Transaction 1/1:
Spending from address index 0
Spending from address index 5
Spending from address index 6
Spending from address index 8
WARNING: Outputs of multiple addresses are being used together, which might potentially compromise your privacy.

Warning: Some input keys being spent are from blocks that are temporally very close, which can break the anonymity of ring signatures. Make sure this is intentional!
Sweeping 0.000701900240 for a total fee of 0.000028460000.  Is this okay?  (Y/Yes/N/No): Y
Transaction successfully submitted, transaction <cd6335dba272d90c2a6c1b4f877a1865ce44665a112735a962043bb2f0178993>
You can check its status by using the `show_transfers` command.
[wallet 4AW1gK]: balance
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000
```

```
[wallet 4AW1gK]: incoming_transfers available
No incoming available transfers
```
The fee was relatively high (0.00002846), I guess that is because of the tx-size, as many outputs are being combined for this?
Anyhow. The wallet is clean now and learnt where I went wrong. Thanks a lot @moneromooo-monero 


## moneromooo-monero | 2022-08-04T18:29:41+00:00
Yes, the feel is proportional to tx size (technically weight, but in this case it's the same).
So it's just down to the not very intuitive spending from just one subaddress by default, and the lack of message if the index= is at the end then. Good, and thanks for the prompt testing.

## afungible | 2022-08-04T18:44:43+00:00
Thanks for your prompt follow up as well. Is it good to have this PR open to have a better description for sweep_all & sweep_account and a usage example for commands? Might help others, should they fall victim to a similar situation ;)

Now that we know what its down to, think we are good.
 

## moneromooo-monero | 2022-08-04T18:51:36+00:00
Sure. It can serve as "please add an error when switching the args" issue if you change the title.

## afungible | 2022-08-04T19:09:11+00:00
Done. Thanks.

## afungible | 2022-12-24T18:23:08+00:00
@moneromooo-monero I need to unfortunately revisit this issue. "sweep_all" isn't working for me with this sample wallet, on v0.18.1.0-release

![image](https://user-images.githubusercontent.com/108204668/209447333-bacf40d8-2d58-49df-a3a4-11ab7019a22c.png)

I am providing this **sample wallet** (only with the intention of ease of reproduction of given issue).

SEED:
imagine corrode gemstone rigid soapy jargon rabbits anvil
desk yoyo inorganic lobster deodorant acquire soccer arises
summon honked gymnast opposite dusted layout talent threaten dusted

PS: Need to top up a small fee (e.g. 0.0001 XMR) to try to sweep all of the sub-addresses 0,1, 2. Which one may notice, don't work.
 
One could also check "show_transfers" to see that transfer outs with sweep didn't lead to the intended result. The balance in the three outputs remain stuck.
 
![image](https://user-images.githubusercontent.com/108204668/209512294-31059b99-aed4-41a1-a8dc-a8833c452154.png)


## afungible | 2022-12-26T19:18:13+00:00
`set ignore-fractional-outputs 0` is the answer, to be able to sweep all outputs which are lower than fee. Thanks @moneromooo-monero 

Might others find this helpful at any time, placing the output.

![image](https://user-images.githubusercontent.com/108204668/209577802-ec35c819-45cb-4bfb-a178-0b4529b51d7c.png)



## plowsof | 2022-12-26T20:15:21+00:00
duplicate of #8405 

## silverpill | 2023-05-25T21:49:39+00:00
>set ignore-fractional-outputs 0

Is there a way to set this parameter with JSON-RPC API?

# Action History
- Created by: afungible | 2022-08-02T23:41:01+00:00
