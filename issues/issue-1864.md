---
title: Multiple suggestions for GUI improvement
source_url: https://github.com/monero-project/monero-gui/issues/1864
author: kayront
assignees: []
labels:
- invalid
created_at: '2018-12-26T12:50:52+00:00'
updated_at: '2019-01-11T23:18:26+00:00'
type: issue
status: closed
closed_at: '2019-01-11T23:18:26+00:00'
---

# Original Description
Recently I've had to get a bit more familiar with the GUI because of a tutorial that I've been working on.

This experience has left me with some suggestions to give.

# Default action upon launching GUI when a wallet already exists

After going through a successful wallet creation, closing the program and starting it again immediately prompts for the password of the wallet that was opened before the program was previously closed.

While this is not an unreasonable default, what comes next could, in my opinion, be improved.

The only options available at this point are to either input the password and click Ok, or Cancel.

Clicking Cancel brings the UI back to the language selection screen, and only after that can the user select whether to create a wallet, open an existing one, etcetera.

Let's focus on opening an existing one. I clicked that, and now there's a file dialog that defaults to the home directory, rather than the directory where monero saves wallets to disk.

On this subject, here's what I think could be improved:

  - Present the option to open any recently opened wallets, straight from the initial password dialog (could be a collapsible that reads "Open recent..").

  - If not the above, then at the very least the following: remember the language selection and avoid going back to that screen (but have a back button to go back there if needed), and jump straight to the second screen where creating/opening/restoring a wallet is possible - **and on the file dialog that follows, default to the directory where wallets are saved** - anything else is confusing for newbies, not everyone nontechnical understands directory structures.

# Transaction History Improvements

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

# Address Book Improvements

1. **See point nr 1 on the next section for an idea on how to improve the send tx workflow when we're selecting an address from the address book**.

2. (see below)

![](https://i.ibb.co/9pMv7C3/monero-improve.png)

That button is in the way. With the window maximized it's not in the way, but in the default size that's how it looks. How about getting rid of it altogether, showing only the first 5 or so characters of the address, then 5 more in the middle, then the last 5, and with the gained space (perhaps make the font a tad smaller too) just have the buttons to send/copy/delete instead?

3. In the address book window, the *description*, could probably be renamed to *Contact*. At the very least, keeping "Description" as it is already, there could be subscript to the tune of something like "A person, institution or a purpose which this address uniquely identifies", something to that extent.

# Sending Transaction Improvements

1. While in the send dialog, the user is given the choice to enter an address from the address book. The address book dialog then pops up, **but it is decontextualized, allow me to elaborate**.  We just arrived at the address book dialog from the send dialog, and immediately what do we see? **About 50% of the space in the window is dedicated to adding a new address to the book, with an optional payment id, and a description** -- these have **nothing to do** with selecting an address to send to! Therefore, **I suggest that the software detects when the address book dialog is being displayed in the case where it was called for address selection to send a transaction**, in which case the following modifications take place: **1) omit everything to do with adding a new address**, and **2) just display a list of the labels + addresses**, and rather than having to click the round button-thing and then click "send to this address", simply clicking on the address ought to be enough to a) select this address in this special mode and b) return us to the send dialog.

2. **Don't default to the subaddress label as the description in an outgoing transaction**. For example, say my mother has seen the light and now she uses Monero. Wonderful! A true miracle of technology (and persistence, in this case...)! Now I want to send her some for christmas. Naturally, she's in my address book, so after going through the somewhat convoluted process to get her address (see previous point above for my suggestions on how to improve that workflow), **the description of the transaction is "Mother"**. I think this is not a sane default - the *recipient* is Mother, and in line with suggestions made earlier in this report, that's what the History window ought to show for outgoing transactions. However, the *description* being the *label (= who is it)* of the subaddress in the address book is not a good default, I think. **Instead, after returning from the slimmed down address book window (see previous point), the send window should now be ready for input in the description field, but leave it blank by default, for the reasons explained in this point**.

# More advanced features for the future

Monero aims to be digital cash for everyone, anywhere and everywhere.

With this in mind, I think we should ask ourselves what kind of features from standard online bank interfaces that could be transposed into Monero make sense to implement.

What immediately jumps to mind is **personal finance applications**, such as:

- Ability to export transactions (+ descriptions, recipients, etc) in common formats, such as CSV.

- Historical data (graphs) about wallet balance.

- Ability to tag transactions - contacts (address book) and (our own) addresses - according to categories and subcategories, add filtering options for these in search, and based on this categorization, have the option to display bar and piecharts about the data, enabling the user to visually get answers to such varied questions as:

  - Which projects are generating the most income?

  - Where is my XMR going?

  - How much XMR do I have left every month after paying my bills and receiving my income (cash flow)?

  - What have been my biggest purchases this year?

  - In the last 3 months, what were the top 5 categories of expenses?

  .. and so on.

- Income vs Expenses charts.

- etc.

# Accounts support

Having used accounts in *simplewallet* since their inception, I can without a doubt say that **this is one of the most important features that Monero offers** (above base layer privacy).

Account support makes managing personal finance for those with the knowledge to do so an absolute delight, and it would be wonderful to see support for accounts in the GUI, so that people who aren't so inclined to use a console could benefit as well.

# Discussion History
## sanderfoobar | 2019-01-11T23:12:18+00:00
As discussed on IRC, best to open 4 separate issues which makes discussing & solving specific issues more streamlined.

+invalid

# Action History
- Created by: kayront | 2018-12-26T12:50:52+00:00
- Closed at: 2019-01-11T23:18:26+00:00
