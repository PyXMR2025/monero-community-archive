---
title: Showing both total balance and unlocked balance is horrible for new users
source_url: https://github.com/monero-project/monero-gui/issues/2293
author: ghost
assignees: []
labels: []
created_at: '2019-07-18T12:20:12+00:00'
updated_at: '2023-06-22T09:42:09+00:00'
type: issue
status: closed
closed_at: '2019-08-13T20:00:58+00:00'
---

# Original Description
Proposal (updated! thx for all input! design also includes #2298, #2304):
![image](https://user-images.githubusercontent.com/46682965/62006390-64e0fb00-b140-11e9-9273-e6784f631273.png)
Clicking on `(Why?)` shows: 

_"For safety reasons, mainly to prevent double-spending, in Monero there's a waiting time of 10 blocks (~20 minutes) until newly received funds can be spent. In case you have to wait although you haven't received any funds within the last 10 blocks, then you certainly have sent some funds within the last 10 blocks - which also can cause a waiting time. The reason for this is that when you send for example 1 XMR, technically 5 XMR may be send but you get 4 XMR back as change - a process you may not notice at all, but technically the 4 XMR count as newly received funds and cause the same waiting time as regularly received funds."_

**Reasons:**
- This solution doesn't make Monero look complicated
- The user only is bothered with locked funds in case it is actually relevant (when he's on the `Send` page **and** funds are locked)
- It is consistent to most other crypto wallets: They won't show you 2 different balances only because some funds might not have enough confirmations yet.




# Discussion History
## rating89us | 2019-07-18T13:16:35+00:00
I agree 100%. Displaying a single balance is much better.

## sanderfoobar | 2019-07-18T13:43:15+00:00
> WHAT THE COMMUNITY THINKS IN GENERAL ABOUT MY RECOMMENDATIONS FOCUSED ON MAKING MONERO EASY FOR NEW USERS. Because I suspect veterans here don't like it too much

Could you expand on that? As active contributor I feel responsible for making sure people feel welcome whilst submitting issues - if you think this is not the case please specifically outline why so we can improve our process.

As for the proposal itself, first impression is that I like the idea.

## ghost | 2019-07-18T13:55:36+00:00
@xmrdsc My proposals just didn't get adopted (yet). Probably it was wrong from me to expect that to happen quickly. And I wonder if "appeal to new users" is considered important here or not so much. I would understand the latter, given that developer resources are limited!

Thanks for liking the proposal!

## dEBRUYNE-1 | 2019-07-18T14:12:33+00:00
@Realchacal - fwiw, selsta is working on your suggestion in #2211.

## dEBRUYNE-1 | 2019-07-18T14:16:59+00:00
>It is consistent to every other (Bitcoin) wallet: They never show you 2 different balances only because some funds might not have enough confirmations yet.

New outputs in Bitcoin aren't actually locked, i.e., you can spend them immediately. By contrast, in Monero they are actually locked for ten blocks. The ten blocks lock time is a security measure.

>You have NO clue what's going on. It is NOT self explaining

I think you are being a bit dramatic here. If there is discrepancy between total balance and unlocked balance, it is kind of obvious that part of the balance is not spendable yet. Additionally, the GUI shows that it will take x minutes for this part of the balance to become spendable again. 

> how long

The GUI shows how long it takes for them to unlock. 

That being said, I like your suggestion of showing a single balance with an appropriate warning message on the `Send` page in case of part of the balance still being locked. 

## erciccione | 2019-07-18T14:28:36+00:00
> That being said, I like your suggestion of showing a single balance with an appropriate warning message on the Send page in case of part of the balance still being locked.

+1. With the only difference that i would add a link to the guide or to somwhere else where it's explained why there is a locked balance. Just to not leave the user confused on why they cannot use all the balance.

## ghost | 2019-07-18T14:34:29+00:00
@dEBRUYNE-1 
> The GUI shows how long it takes for them to unlock.

Sorry, I didn't know! Thanks. 


## ghost | 2019-07-18T20:29:50+00:00
> +1. With the only difference that i would add a link to the guide or to somewhere else where it's explained 

Ok! I made an explanation that could be used as a popup or tooltip:

_For safety reasons, mainly to prevent double-spending, you have to wait 10 blocks (~20 minutes) until newly received funds can be spent. Please note that sending funds also may lead to such a waiting time. The reason for this is that sending funds usually involves getting back some change, which is handled in the background without you noticing it, but technically counts as newly received funds._

## GBKS | 2019-07-19T08:10:29+00:00
Here's an exploration around simplifying the balance display and keeping the information about locked amounts inside the balance card. The big message with the warning sign in the send screen just seems a bit overkill. Big alert messages should be things that are super important for users to see and act on. I'd find a subtler treatment more appropriate.

![monero-balance-cards-gbks-190718](https://user-images.githubusercontent.com/695901/61519881-488ce200-aa0d-11e9-9ae7-dbc87b573d69.png)

And yes, it has also bugged me to see two balances with the same visual weight. Always takes me a second to figure out what's what.

## ghost | 2019-07-19T10:30:29+00:00
@GBKS What you've done looks REALLY, REALLY great! But:
- The big warning sign is NOT overkill, because it's only shown in the `Send` page and only if funds are actually locked. But I'd totally agree to make the sign smaller or change the message! If you've got any proposals for that, you seem to be very talented to see what looks good!
- Showing how much is locked is not of primary interest. What's AVAILABLE is more of interest!
- The main idea was not to bother the (new) user with something strange ("locked funds") that he is not familiar with.
- In #2298 we (you and me^^) are currently discussing to overhaul the balance window anyway. That would make your proposal here obsolete.

**Conclusion:** I'm against your proposal (Sorry! I'm not saying it's bad, it's an excellent proposal! But I'm still against it for the given reasons.)

Thank you for pointing out that seeing 2 balances always needs a second look, even for veterans!


## rating89us | 2019-07-19T10:45:59+00:00
Balance card should display total balance only.
Send page should display available balance.

## ghost | 2019-08-12T09:08:22+00:00
@selsta do I close this, too, and integrate it in #2298?

## selsta | 2019-08-13T18:55:12+00:00
@Realchacal yes I’d add it to #2298.

## ghost | 2019-08-13T20:00:58+00:00
Closed and integrated in #2298.

## ghost | 2023-06-22T09:42:08+00:00
you very rich


# Action History
- Created by: ghost | 2019-07-18T12:20:12+00:00
- Closed at: 2019-08-13T20:00:58+00:00
