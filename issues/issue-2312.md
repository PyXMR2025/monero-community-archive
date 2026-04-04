---
title: 4 proposals to make the `Account` page more intuitive
source_url: https://github.com/monero-project/monero-gui/issues/2312
author: ghost
assignees: []
labels: []
created_at: '2019-07-23T14:04:06+00:00'
updated_at: '2019-09-04T08:15:55+00:00'
type: issue
status: closed
closed_at: '2019-09-04T08:15:55+00:00'
---

# Original Description
[Updated]

**1.** 
![image](https://user-images.githubusercontent.com/46682965/61712275-4486fa00-ad56-11e9-8771-28f49c830be3.png)
- "Account" can be misinterpreted as "user account" / "user profile". Calling it "Accounts" would improve that a little bit.
______________________________________________

**2.** 
![image](https://user-images.githubusercontent.com/46682965/61796230-48ce1880-ae25-11e9-8d8e-fe756131feaf.png)
- Using multiple accounts is **optional**, sending and receiving is **not**. This should be reflected by the menu order. (You wouldn't put `Advanced` at the top, right?)

______________________________________________

**3.+4.**
![image](https://user-images.githubusercontent.com/46682965/64069593-ea2e6280-cc4c-11e9-8dfa-2aa6a5c80466.png)

- What is "Balance All"?
- "Total unlocked balance" should be removed for the same reasons as in #2298.
- "Balance" in each row is bad
- Shortening the balance with `...` to replace just 2 zeros is bad
- The edit icon and the copy icon have unintuitive positions
- Showing one address per account leads to misconceptions for new users. They may think:
     - **_"Ah, in Monero an account is an address!"_**
     - **_"Ah, every account has exactly one address!"_**
     - **_"Ah, every account has one account number!"_**
Solution: Introduce a header line to explain a little bit.
- `+ Create new account` sounds like the account doesn't exist yet - but it does, it's just not shown.

![image](https://user-images.githubusercontent.com/46682965/64069643-e2bb8900-cc4d-11e9-8fee-e0ca9cf64e4c.png)
![image](https://user-images.githubusercontent.com/46682965/64069461-e3522080-cc49-11e9-9af7-5c418ba03d9e.png)







# Discussion History
## rating89us | 2019-07-23T18:41:57+00:00
I agree with all your points, except with hiding addresses of accounts. After seeing them many times, you start to remember which address refers to each account, and this improves security.

## selsta | 2019-07-23T18:48:28+00:00
I appreciate the feedback.

## ghost | 2019-07-29T09:23:01+00:00
Updated! Feedback integrated! Thx.

## selsta | 2019-08-29T21:44:51+00:00
Proposal 3. and 4. looks good, I will try to implement it.

Regarding the sidebar I will implement concept #1 from @GBKS which you can find here: https://www.reddit.com/r/Monero/comments/c23zxn/feedback_request_ideas_for_improving_how_multiple/

## ghost | 2019-08-29T22:38:31+00:00
@GBKS #1 brings tears to my eyes! (Sorry!) I totally understand his intention, but:
- "`Account` above `Wallet`" in the menu is so misleading (wrong hierarchy)! And then `Accounts` below `Wallet` adds confusion.
- the GUI gets visually **more** complex while all those normies don't even use multiple accounts

**Alternative proposal:**
![image](https://user-images.githubusercontent.com/46682965/63981128-1a93c680-cabe-11e9-96c6-de3a724f7a78.png)
(Ignore the changes from #2298, #2304, #2325, #2339.)

## selsta | 2019-08-29T22:44:41+00:00
I’ll have to think about it. What about making the whole `Account #0 Retirement Savings` area clickable and this brings you to the account page?

## ghost | 2019-08-30T08:13:07+00:00
THAT WOULD BE INCREDIBLY NICE! It simplifies visually, it doesn't bother average users who don't use multiple accounts, it reduces potential account hierarchy misinterpretation, it still allows 1-click access to `Accounts`, and it can't get any more intuitive than clicking on the account to change the account!

My only requirement would be:

- The user **somehow** must be able to see that he can click on it! Maybe change something when the mouse is hovering (text color / text underlining / rectangle around the area or something). Or show the same icon as in the menu:
   ![image](https://user-images.githubusercontent.com/46682965/64004205-14c5d180-cb0e-11e9-8fed-c36195781296.png)


## GBKS | 2019-08-30T09:08:21+00:00
Great discussion here. I agree with the detail improvements in the accounts page, but disagree about the accounts/wallet hierarchy.

Underneath wallet, we find accounts, address book (used in all items underneath account), settings (+ subitems) and advanced (+ subitems).

Underneath account, we find send, receive, and transactions.

I think it's important to be clear about this and label things appropriately. I'd also argue that generally interfaces are not more intuitive because there's less in them, but because they do a better job at explaining what's going on - so in this case I'm not concerned about the complexity. It's problematic when you're hiding a whole top-level feature underneath a pretty thin arrow in the corner of another element and rely on a hover-state for people to discover it. Obvious is better here.

I'm also not sold on the "normies don't use accounts" argument. It's a very new feature in the GUI, we don't have analytics, so we just don't know how how people want to use it (let me know if you have some info on this). Maybe people love it if we just treat it like a real, useful feature?

And a small note, I find that the grey logo looks disabled. I'd make it colored. Or maybe it can be grey while syncing, and colored when ready to transact?

Love the discussions. It's a great place when you're discussing such details, it means a lot of bigger things are in good shape.

## ghost | 2019-08-30T10:05:06+00:00
> It's problematic when you're hiding a whole top-level feature underneath a pretty thin arrow

- it's not more or less hidden than any other menu item:
![image](https://user-images.githubusercontent.com/46682965/64016228-ac371e80-cb26-11e9-8958-6e871d8add51.png)

According to your proposal we would have `Account` above `Wallet`. This is confusing because it reflects the wrong hierarchy. And as if that was not confusing enough, your proposal also has `Accounts` below `Wallet`. 

We don't need to introduce a separate section `Wallet` because the whole window already is related to the wallet, which hopefully soon will be reflected by the wallet name in the title bar (#2325):
![image](https://user-images.githubusercontent.com/46682965/64011129-6163d980-cb1b-11e9-89e8-8e584d31a244.png)

> let me know if you have some info on this

I just started a small poll:
https://www.reddit.com/r/Monero/comments/cxesm4/poll_to_find_out_if_the_monero_gui_should_be/

> And a small note, I find that the grey logo looks disabled.

It doesn't look disabled to me **but if** it looks disabled to you, it probably also looks disabled to others so we should change it!

## ghost | 2019-08-30T14:31:26+00:00
@GBKS what you're aiming at is ABSOLUTELY right! But IMO it would require a much deeper redesign like #2367.

## ghost | 2019-09-04T08:15:55+00:00
Closing this because it's bullshit compared to #2367.

# Action History
- Created by: ghost | 2019-07-23T14:04:06+00:00
- Closed at: 2019-09-04T08:15:55+00:00
