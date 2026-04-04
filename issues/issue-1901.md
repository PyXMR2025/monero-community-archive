---
title: Sending Transactions - request for improvements
source_url: https://github.com/monero-project/monero-gui/issues/1901
author: kayront
assignees: []
labels: []
created_at: '2019-01-15T11:13:38+00:00'
updated_at: '2019-01-15T11:18:31+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
(breaking down #1864 as requested)

1. While in the send dialog, the user is given the choice to enter an address from the address book. The address book dialog then pops up, **but it is decontextualized, allow me to elaborate**.  We just arrived at the address book dialog from the send dialog, and immediately what do we see? **About 50% of the space in the window is dedicated to adding a new address to the book, with an optional payment id, and a description** -- these have **nothing to do** with selecting an address to send to! Therefore, **I suggest that the software detects when the address book dialog is being displayed in the case where it was called for address selection to send a transaction**, in which case the following modifications take place: **1) omit everything to do with adding a new address**, and **2) just display a list of the labels + addresses**, and rather than having to click the round button-thing and then click "send to this address", simply clicking on the address ought to be enough to a) select this address in this special mode and b) return us to the send dialog.

2. **Don't default to the subaddress label as the description in an outgoing transaction**. For example, say my mother has seen the light and now she uses Monero. Wonderful! A true miracle of technology (and persistence, in this case...)! Now I want to send her some for christmas. Naturally, she's in my address book, so after going through the somewhat convoluted process to get her address (see previous point above for my suggestions on how to improve that workflow), **the description of the transaction is "Mother"**. I think this is not a sane default - the *recipient* is Mother, and in line with suggestions made earlier in this report, that's what the History window ought to show for outgoing transactions. However, the *description* being the *label (= who is it)* of the subaddress in the address book is not a good default, I think. **Instead, after returning from the slimmed down address book window (see previous point), the send window should now be ready for input in the description field, but leave it blank by default, for the reasons explained in this point**.



# Discussion History
# Action History
- Created by: kayront | 2019-01-15T11:13:38+00:00
