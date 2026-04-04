---
title: Transaction History - request for improvements
source_url: https://github.com/monero-project/monero-gui/issues/1899
author: kayront
assignees: []
labels: []
created_at: '2019-01-15T11:12:16+00:00'
updated_at: '2019-01-20T21:56:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
(breaking down #1864 as requested)

1. On a new wallet, I sent a small amount to test, and even though the transaction was in the txpool, it didn't show up in the history. This may or may not be a standalone issue, see below.

2. Even after obtaining 2 confirmations, and the top-left corner of the screen correctly displaying the balance, nothing would still show in the History. **I then re-selected today's date on that page, and lo and behold, the transaction showed up**.

3. When receiving transactions, **there is zero mention of which subaddress** it was sent to. **This is a very serious omission in my opinion, and here's why**. As payment ids are becoming a thing of the past, it becomes necessary to have *some way* of differentiating between incoming transactions. Say you are a freelancer and getting paid in Monero, since payment ids are not an option, subaddresses are the way to go - **but there is no visual indication whatsoever of which subaddress we received funds to, and thus, we cannot determine who has paid us!**

![](https://i.ibb.co/ZBvWY6c/monero-improve.png)

See above for what I believe is a better display; in short:

  - For receiving (incoming tx), display the target subaddress label (if any, otherwise display as (Unknown), and maybe make it visible with a different color) - this is a subaddress we have to someone, and thus we can label it as someone, a company, or something more abstract like just "donations"; **the "truncated descr** refers to the tx description we can add for an incoming transaction, **this feature is missing too!**

  - For sending (outbound tx), **if the recipient is in our address book, rather than displaying the address, display the address label ("Mother" in the example) instead, and together with it display a truncated version of the tx description (if any), so that it is **immediately visible just from scanning the tx history if we know what we're looking for**.

4. **There are no filtering options whatsoever** for:

  - Only showing transactions **sent to** a contact (address book) (important)
  - Only showing transactions **received from** a contact (address book). (important)
  - Showing transactions below or above a certain amount (important)
  - Showing transactions to unlabeled subaddresses. (less important)

5. Immediately after sending a transaction, it will show in history (CTRL+H) as "unknown recipient". Minor one, but could it right away show the address, or label if it is part of our address book?

# Discussion History
## selsta | 2019-01-20T21:56:59+00:00
> On a new wallet, I sent a small amount to test, and even though the transaction was in the txpool, it didn't show up in the history. This may or may not be a standalone issue, see below.

I can confirm this bug but I haven’t found out what causes it yet.

> When receiving transactions, there is zero mention of which subaddress it was sent to.

#1873 improves this.


# Action History
- Created by: kayront | 2019-01-15T11:12:16+00:00
