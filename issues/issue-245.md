---
title: Adhere to naming conventions in the UI
source_url: https://github.com/monero-project/monero-gui/issues/245
author: ghost
assignees: []
labels:
- resolved
created_at: '2016-12-07T06:20:37+00:00'
updated_at: '2018-11-18T19:18:31+00:00'
type: issue
status: closed
closed_at: '2018-11-18T19:18:31+00:00'
---

# Original Description
Working on the German translations I found some inconsistencies in the UI regarding the labels. I would like use this ticket to discuss some important terms in the UI:

**Payment vs. Transactions**

What is the difference between the two? The UI uses the two terms in different contexts:
* Payment ID
* Transaction ID
* Transaction priority
* Transaction cost
* Verify payment
* Transaction history

**(Mnemonic) Seed**

For the inexperienced user the term "Seed" or "Mnemonic Seed" leads to confusion. Instead I would suggest the term "Recovery Words" or "Recovery Phrase".

**Account vs. Wallet**

The Wizard uses the term "Account" and "Account name", whereby the term "Wallet" is also often used. Isn't it the same?

Examples (from 5 total):
* Account name
* This is my first time, I want to create a new account
* I want to recover my account from my 25 word seed

I suggest to use "Wallet" everywhere.


# Discussion History
## ghost | 2016-12-08T16:08:59+00:00
Personally, I think user friendliness is most important, so changing the GUI phrase "mnemonic seed" to "recovery seed" feels like a good decision. However, I've only been involved in cryptocurrency for less than a year, so I'm not an expert at all.

## ghost | 2016-12-23T00:26:20+00:00
You're an expert on being a newbie though, which is of course the target audience ;)

## erciccione | 2018-11-18T13:05:09+00:00
Looks that this PR didn't get much traction in the last two years and meanwhile, a lot of naming changed. If still meaningful, please open a new issue

+resolved

# Action History
- Created by: ghost | 2016-12-07T06:20:37+00:00
- Closed at: 2018-11-18T19:18:31+00:00
