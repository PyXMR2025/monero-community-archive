---
title: 'Privacy Issue: Unneccesarry merging of coins makes users more traceable (broken
  change management)'
source_url: https://github.com/monero-project/monero/issues/9350
author: AlwaysCompile
assignees: []
labels:
- low priority
- discussion
created_at: '2024-06-03T17:24:44+00:00'
updated_at: '2024-06-05T11:54:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I noticed a bug that affects almost all wallets (as they seem to use wallet2.cpp). Essentially, Monero fund segregation / "coin control" is based on address (frozen, thaw, etc). From my research fund segregation is very important in Monero due to it's low anonymity set and the improbability of repeated merged outputs from unrelated parties. _Segregated funds should never merge together_

The issue is that **Monero sends all change to the same address**. This creates a merging nightmare because all those outputs will eventually be merged together. It might be 20 transactions from now, but when they are it creates a goldmine of probability heuristic info for chain analysis companies. It not only is bad from a privacy standpoint, but it is simply a bug from Monero's concept of coin control.

**The Problem**
Let's pretend that Addr0 is where all change is sent. User segregates Addr1 and Addr2 via the built-in coin-control (freeze, thaw, etc). As user spends Addr1 it's change is put in Addr0. Later, as the user spends Addr2, it's change is _also put in Addr0_. It creates a conundrum for the user. If they didn't also freeze Addr0 then outputs would have been merged long ago. However, even if they did, they will have a lot of balance in Addr0 which has _no option but to be merged together_ at which point their privacy is broken.

There are two possibilities here:

1. Either change handling is bugged 
2. Freeze / thaw (aka coin control) implementation is bugged and needs to be based on the output level and NOT address level (similar to feather wallet).

IMO, change handling is what is bugged because address-level coin control is far more intuitive and proper for the user. Output-level coin control introduces dusting attacks on the user unless they review all outputs in wallet before every spend. Address-level coin control does not have this issue.

The goal of output is that _privacy context_ should not change. Spent inputs belonging to one context should create change outputs that also belong to the same context. When privacy context is violated, user privacy is violated.
 
**The Solution**
I am not a programmer, so I cannot comment for sure, but I asked my programmer friend and he said that indeed the Monero code does mishandle change outputs. I do not understand the details, but I paste the corrected code he offered me and maybe it will be of help.

Basically, in two places in wallet2.cpp the following is called:

`change_dts.addr = get_subaddress({subaddr_account, 0});
change_dts.is_subaddress = subaddr_account != 0;
splitted_dsts.push_back(change_dts);`

**This code is problematic for two reasons:**

1. It forces all change into the same address thus giving them the same "privacy context"
2. It does not respect the passed transfer context already passed to the functions

**Here is the corrected code:**

`const cryptonote::subaddress_index input_subaddr = m_transfers[selected_transfers[0]].m_subaddr_index;
change_dts.addr = get_subaddress(input_subaddr);
change_dts.is_subaddress = input_subaddr.is_zero() == false;`

**Why is this a solution?**

It preserves the privacy context of the change. Change will never go into a different privacy context. This is an agnostic way because it uses the list of unspent outputs available to the transaction to derive the proper change address that will not violate the privacy context.

The result is that coin control (freeze / thaw) actually has value. If you keep two addresses frozen / thawed you can guarantee the outputs from the transactions they generate will never be merged later down the road. It also enables frozen / thawed to have use on the primary address. Currently, you cannot really freeze the primary address as soon your entire balance will end up in that address due to improper change handling and the result is you will have an unspendable wallet (until you thaw and merge everything to create a privacy nightmare).





# Discussion History
## selsta | 2024-06-03T17:29:18+00:00
> Freeze / thaw (aka coin control) implementation is bugged and needs to be based on the output level and NOT address level (similar to feather wallet).

Maybe I'm misunderstanding something but freeze / thaw is on an output level, not address level. The commands ask you for a key image, not an address.

## selsta | 2024-06-03T17:45:36+00:00
What you are suggesting is similar to using subaccounts, change outputs won't be merged between different accounts.

## AlwaysCompile | 2024-06-03T17:55:20+00:00
You are right that freeze / thaw is based on keyimage I didn't really analyze it because output-level coin control is inherently broken due to dust attacking. Even though I used that terminology I actually meant the internal spending control used by wallet2.cpp. This is primary based on subaddress index. You can see this in the wallet RPC:

> subaddr_indices - array of unsigned int; (Optional) Transfer from this set of subaddresses. (Defaults to empty - all indices)

And in the wallet2.cpp various transaction handling:

> std::vector<wallet2::pending_tx> wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry> dsts, const size_t fake_outs_count, const uint64_t unlock_time, uint32_t priority, const std::vector<uint8_t>& extra, uint32_t subaddr_account, std::set<uint32_t> subaddr_indices, const unique_index_container& subtract_fee_from_outputs)

Notice, subaddr_indices is what is primary used to limit output selection. Though freezing / thawing will further limit it if an individual output is frozen even if the subaddr index is passed.

However, **that is still means built-in coin control is broken** because as previously pointed out if you cannot reliably control spendign _per-address_ then you open yourself up for a **dust-merge attack**. Basically, anyone can send dust to multiple addresses and see if they merge. This cannot happen when using subaddress level coin control as the dust retains the privacy context of the address.

However, with output-level coin control this can happen unless the user reviews all newly created outputs and then freezes them properly every time. When limiting outputs by subaddress this step is not necessary.

So, my question is, **why not handle change in a more elegant manner so that per-address privacy context preservation is possible?**

## selsta | 2024-06-03T18:23:47+00:00
> So, my question is, why not handle change in a more elegant manner so that per-address privacy context preservation is possible?

Did you try to use accounts instead of subaddresses? That should result in the behaviour you are asking for.

# Action History
- Created by: AlwaysCompile | 2024-06-03T17:24:44+00:00
