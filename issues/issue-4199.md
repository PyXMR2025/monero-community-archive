---
title: transactions with many inputs fail with Trezor Model T without any hints in
  the UI
source_url: https://github.com/monero-project/monero-gui/issues/4199
author: thestinger
assignees: []
labels: []
created_at: '2023-07-18T04:27:31+00:00'
updated_at: '2023-07-18T18:46:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Trying to send a transaction using a large number of inputs doesn't work. The Trezor Model T displays the wrong transaction amount and fails to produce a valid transaction to send. I'm trying to work around it by setting a lower transaction amount and consolidating to a temporary account in the same wallet, but it's painful. The software should know the maximum limits and should support working around it. Should I be using the CLI software instead?

# Discussion History
## thestinger | 2023-07-18T04:43:54+00:00
I'm managing to get this done by doing a quick manual binary search for the maximum amount that I can send in a transaction, which is gradually getting smaller since it seems to use the larger inputs first. I'm not at all an expert on how it works under the hood, but I was able to guess what was wrong and work around it. Someone else might have thought their funds were lost.

## thestinger | 2023-07-18T05:11:56+00:00
This seems to be the same issue, but it would be nice if the UI helped with it and could do coin control of some kind to split it up into small batches without trial and error.

https://github.com/monero-project/monero/issues/8290

## selsta | 2023-07-18T11:32:32+00:00
How is it failing? The exact same error code 99 from the linked issue?

## thestinger | 2023-07-18T18:19:59+00:00
There were multiple kinds of failures. I started out trying to transfer all the money (send max) and the Trezor only displayed a much smaller amount as what I was trying to send. I approved that to see what would happen and the wallet rejected it as invalid with an error. It seems as if the Trezor was only trying to handle a subset of the inputs since it was more than happy to attempt signing it. That happened many times. I had to pick smaller amounts to send in order to get it to use a smaller number of inputs. This was far from precise since some of the transactions ended up with many inputs and some with very few because increasing it by 1 XMR would add too many and I didn't feel like doing a finer grained search.

I only saw a similar error to that code 99 error when I reached the end and needed to send all the leftover inputs. I did see that error right near the end before a final few transactions dealt with all the non-dust inputs.

## selsta | 2023-07-18T18:23:46+00:00
Is your wallet full of mining outputs?

## thestinger | 2023-07-18T18:46:49+00:00
No, it was a donation wallet which received hundreds of mostly small donations over several years. I needed to send the money to a new hardware wallet and initially tried to do that with a single transaction. It ended up having to be done with dozens of transactions, which is a worthwhile sacrifice to use a hardware wallet but manually splitting it up was a major annoyance and it could have been done a lot more efficiently if the software calculated the max amount it could send with each transaction instead of me having to keep manually lowering it by an arbitrary amount until it worked. Until near the end, the Trezor would show a smaller amount than what I had entered if it wasn't going to work so it was a lot faster than actually having to try signing each transaction before seeing if it was going to work. When I was nearly done, I started getting that error code 99 instead, often part of the way through the transaction which made it much more annoying.

# Action History
- Created by: thestinger | 2023-07-18T04:27:31+00:00
