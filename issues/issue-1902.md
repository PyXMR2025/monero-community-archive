---
title: Add Personal Finance Management tools the wallet
source_url: https://github.com/monero-project/monero-gui/issues/1902
author: kayront
assignees: []
labels: []
created_at: '2019-01-15T11:14:37+00:00'
updated_at: '2019-02-08T14:11:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
(breaking down #1864 as requested)


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

# Discussion History
## sanderfoobar | 2019-02-08T14:11:07+00:00
Thanks for the suggestion(s). Recently, the GUI added support for exporting transaction history to CSV. I would argue that most points you are suggesting can be solved using third-party software, using the CSV as input.

From your suggestions I think the following points are eligible:

- Historical data (graphs) about wallet balance
- Income vs Expenses charts
- Ability to tag transactions on category

The rest should really be picked up with other software.

# Action History
- Created by: kayront | 2019-01-15T11:14:37+00:00
