---
title: 'Feature: allow selection of multiple transactions to show their netted sum'
source_url: https://github.com/monero-project/monero-gui/issues/4457
author: godfuture
assignees: []
labels: []
created_at: '2025-06-12T14:13:28+00:00'
updated_at: '2025-06-13T17:36:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi guys,
many times I am using the monero desktop gui, I am missing the possibility to mark multiple transactions of my choice to see the net balance of those transactions. 

Think of multiple transactions no matter the direction and you would like to know the netted sum. Like in Exel and other comparable tools. If you mark cells all containing valid numbers, it will show you the sum (and average).

Currently I have to enter each and every transaction amount into my calculator to find out the net balance of these specific transactions. This problem is even worse, because of two reasons: 
1. Monero desktop gui does not apply the current locale of my computer. This means the dot copied to clipboard is not understood properly as my locale uses comma for decimal separator.
2. copying the transaction amount includes the unit ("XMR") which makes it even harder to simply paste the numbers into calculator.

But with this ticket implemented, we could simply mark those transactions and take a look to the bottom status bar (or somewhere else) showing its netted balance/sum. It would be useful, if CTRL and SHIFT could be used, to either mark/unmark transactions individually (CTRL) or mark a series of transactions from start to end (SHIFT) as we know it from many file explorer.

Many thanks

Win 10 x64
Monero GUI 0.18.4.0

# Discussion History
## plowsof | 2025-06-12T15:30:03+00:00
please leave feedback in #4431 

## godfuture | 2025-06-13T15:51:19+00:00
> please leave feedback in [#4431](https://github.com/monero-project/monero-gui/issues/4431)

@plowsof the other ticket is a different feature request. It is about how to display multiple recipients of the same transaction (I dont even know what this technically means to the payment. Everyone gets the amount? Or is it split? Doesn't matter...)

How can I help here? I would like to help, if I can...

## plowsof | 2025-06-13T16:22:15+00:00
Apologies, your request and #4431 are unrelated, i misread. Maybe a filter -> manual selection for sorting? checkboxes could then display next to each transaction.
- [ ] transaction 1
- [x] transaction 2
- [ ] tx 3
- [x] tx 4   

displaying total sent / received in the manual selection somewhere could be default behaviour 

## godfuture | 2025-06-13T17:36:40+00:00
> Apologies, your request and [#4431](https://github.com/monero-project/monero-gui/issues/4431) are unrelated, i misread. Maybe a filter -> manual selection for sorting? checkboxes could then display next to each transaction.
> 
>     * [ ]  transaction 1[x]  transaction 2[ ]  tx 3[x]  tx 4
> 
> 
> displaying total sent / received in the manual selection somewhere could be default behaviour

I guess my request is not about sorting, but the rest of your idea is quite nice. A tickt box to activate slection mode. Selections can be done using CRTL and SHIFT. 

In the end you helped me! ;-)

# Action History
- Created by: godfuture | 2025-06-12T14:13:28+00:00
