---
title: 'Send page: impossible to paste into the amount inputbox'
source_url: https://github.com/monero-project/monero-gui/issues/3661
author: l29ah
assignees: []
labels: []
created_at: '2021-08-07T20:39:05+00:00'
updated_at: '2021-09-16T21:47:21+00:00'
type: issue
status: closed
closed_at: '2021-08-08T02:32:06+00:00'
---

# Original Description
Both with right-click->paste and ctrl-v. Pasting in the address box works. Version 0.17.2.0 on Gentoo GNU/Linux here.

# Discussion History
## selsta | 2021-08-08T00:37:02+00:00
Can't reproduce. Can you post the number you have attempted to paste?

## l29ah | 2021-08-08T00:43:33+00:00
10.6049880561322
Oh, apparently it checks the data before allowing it to be pasted and silently discards it when it doesn't like it. That's a shame.

## selsta | 2021-08-08T02:31:28+00:00
Yes, that's not a valid amount.

## selsta | 2021-08-08T02:32:06+00:00
Closing as pasting into the amount box works as long as the amount is valid.

## l29ah | 2021-08-08T10:03:44+00:00
Certainly a valid amount, reopen plz.

## l29ah | 2021-08-08T10:05:13+00:00
Is user supposed to remember, count and trim how much digits after the dot is meaningful in Monero?

## selsta | 2021-08-08T11:54:16+00:00
Monero supports 12 decimal digits. Your example number has 13. Silently dropping digits after pasting would be worse than not pasting it at all.

The only thing that can improved would be an error message.

## l29ah | 2021-09-07T14:35:34+00:00
For the record, Electrum does the right thing in this case, trimming the length of the pasted amount. Certainly better than not pasting it at all.

## chaserene | 2021-09-16T21:45:26+00:00
> Silently dropping digits after pasting would be worse than not pasting it at all.

@selsta why? this argument would be valid if it mattered financially, e.g. 10s of dollars of difference after trimming, but XMR is safely far from that. I agree with @l29ah, the amount should be trimmed, you can't expect novice users (=a goal demographic of the GUI wallet) to realize why pasting doesn't work, or remember how many decimals the protocol supports. especially since defining the amount in fiat is not yet possible, so you can pretty much expect they will try to paste a value from a calculator app when paying an amount fixed in fiat, and those divisions tend to yield a lot of decimals.

# Action History
- Created by: l29ah | 2021-08-07T20:39:05+00:00
- Closed at: 2021-08-08T02:32:06+00:00
