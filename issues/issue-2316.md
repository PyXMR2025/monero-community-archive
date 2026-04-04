---
title: Drop "Change account"
source_url: https://github.com/monero-project/monero-gui/issues/2316
author: ghost
assignees: []
labels: []
created_at: '2019-07-24T15:56:20+00:00'
updated_at: '2019-09-03T18:12:50+00:00'
type: issue
status: closed
closed_at: '2019-09-03T18:10:56+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/46682965/61848605-f20d2100-aeae-11e9-9dc0-37e86162c636.png)
Proposal: Drop marked "feature".

Rationale:
- You can access the `Account` page with just one click anyways.
- It is confusing for new users. They think: _"I just want to send money. What is this strange `(change account)` thing!? Is that a separate account for my change money!??? Oh wait, it looks like I can click on it. Do I have to do that!??? Shit, I don't know, but it must be important, otherwise it probably wouldn't be there. Gosh, why is that Monero thing so complicated!? I just wanted to send money, now I have anxiety because I could make something wrong and lose my money."_
- Using multiple accounts is optional. Why bother everyone with it on the `Send` page?



# Discussion History
## rating89us | 2019-07-28T14:39:40+00:00
In my opinion:
- Simple wallet: display "Amount ("`Name of account`")".
- Advanced wallet: display "Amount ("`Name of account`") (`change account link`)".

## ghost | 2019-07-28T15:14:24+00:00
Strongly disagree. Why do you propose to even **add** the account name? Isn't it already shown on the balance card?!

## rating89us | 2019-07-30T08:59:09+00:00
The intent here is to prevent user to inadvertently spend funds from wrong account.

When you are in Send page, you must have a clear and explicit indication informing from which account you are spending from. 

I believe the account's name in balance card is not highlighted enough.

An alternative could be that the background color of balance card changes according to selected account. So, if my Savings account is selected, my balance card would be purple, and so on...

## ghost | 2019-07-30T09:41:21+00:00
> I believe the account's name in balance card is not highlighted enough.

True! That's hopefully gonna change (#2298):
![image](https://user-images.githubusercontent.com/46682965/62118114-697eee00-b2bd-11e9-8afd-5af3d310bade.png)

> When you are in Send page, you must have a clear and explicit indication informing from which account you are spending from.

Everything in the wallet (sending / receiving / transaction history) relates to the **current** account shown in the balance card. With your logic you would have to add an account info to the `Receive` and `Transactions` page as well.

## ghost | 2019-09-03T18:10:56+00:00
Closed because #2367 is much better and includes this proposal (implicitly).

# Action History
- Created by: ghost | 2019-07-24T15:56:20+00:00
- Closed at: 2019-09-03T18:10:56+00:00
