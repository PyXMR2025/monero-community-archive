---
title: Accounts as tabs
source_url: https://github.com/monero-project/monero-gui/issues/2367
author: ghost
assignees: []
labels: []
created_at: '2019-09-01T05:44:17+00:00'
updated_at: '2019-11-14T10:52:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![image](https://user-images.githubusercontent.com/46682965/64435998-c4c5ac80-d0c3-11e9-8c39-8f9b17597f30.png)

![image](https://user-images.githubusercontent.com/46682965/65489263-0f5c6c80-deab-11e9-9a19-9a29181804ee.png)

Alternative (more intuitive since the `Accounts` page itself isn't shown as tab):
![image](https://user-images.githubusercontent.com/46682965/68850438-53623580-06d4-11ea-8102-95aed4d4915f.png)


- Thx @GBKS, @selsta, @Electricsheep01 for ideas/ inspiration.
- Shown design also includes #2298, #2304, #2339, #2325, #2312.
- [Poll](https://www.reddit.com/r/Monero/comments/cxesm4/poll_to_find_out_if_the_monero_gui_should_be/) results: "Are you using multiple accounts?" **33%** YES | **66%** NO





# Discussion History
## kayront | 2019-09-01T08:21:17+00:00
I really like this.

Monero is nearly uniquely positioned to offer the accounts functionality because of on-chain privacy being on by default. I've made use of the accounts feature in the cli for a long time, and wouldn't have it otherwise: it's personal finance 101 to keep stuff separate.

I really like the work you guys have been doing, the wallet looks better and better. I'm very appreciative of the fact that we have people like you working on the project.

## realindiahotel | 2019-09-01T10:52:57+00:00
Sexy

## potatoisfood | 2019-09-01T20:16:25+00:00
 
Some GUI updates


1 Lets get rid of the left hand side menu’s sub-buttons.
Send button has one sub-button. Address Book.
Receive button has one sub-button. Merchant.
Advanced button has four sub-buttons. Mining, Prove/check, Shared RingDB and Sign/verify.

Settings button has no sub-buttons in the menu. Instead the buttons are at the top edge of the Settings page. Lets do it this way with Send and Advanced buttons. So sub-buttons to the top edge of each page. And they should be exactly like buttons on Settings page. Horizontally at the top edge of the page.

Receive buttons Merchant sub-button has so different functionality than rest of the wallet, that it could look very different than the other buttons and could be located somewhere bottom edge of the Receive page.


2 We could combine the Advanced and the Settings buttons in to one button. That could be called just Settings button. At the top edge of the settings page there would be located horizontally Wallet, Interface, Node, Log, Info, Mining, Prove/check, Shared RingDB and Sign/verify buttons. They could be in one or two rows depending how much there is space. And they really should look like they look now at the Settings page, and be horizontally, because the look so good.


3 The Setting button's written word Settings could be replaced by a cogwheel symbol. Once there is, for a written word, a widely know symbol, it should be used. And remember, less text, more intuitive. The cogwheel symbol could be located at the bottom left corner of the wallet.

It would be great to show for a friend or for a noob GUI wallet and say, hey this all you need to know to use wallet, Account, Send and Receive.

## ghost | 2019-09-02T05:09:30+00:00
@potatoisfood: Sorry but your comment is mostly off-topic for this issue.

## 1blockologist | 2019-09-04T23:14:28+00:00
I would prefer the GUI allows for multiple wallets to be opened instead of simply elevating multiple subaddresses.

The tabs should be for different wallets being scanned.

This would allow for more consistent real world accounting purposes, while continuing to promote single use addresses.

"trading" and "retirement" as only a single distinct subaddress instead of a separate wallet is promoting address re-use which is not a privacy feature.

## selsta | 2019-09-04T23:30:06+00:00
> trading" and "retirement" as only a single distinct subaddress instead of a separate wallet is promoting address re-use which is not a privacy feature.

Accounts can create as many subaddresses as they want. They promote address re-use the same way as a different wallet file would.

> I would prefer the GUI allows for multiple wallets to be opened instead of simply elevating multiple subaddresses.

The GUI isn’t built to support multiple wallets so this would require large architectural changes.

> The tabs should be for different wallets being scanned.

This performs way worse than accounts.

> This would allow for more consistent real world accounting purposes, while continuing to promote single use addresses.

Can you explain why “more consistent real world accounting purposes”? Having to save multiple seeds is a worse UX than having multiple accounts in a single seed.

## 1blockologist | 2019-09-04T23:58:19+00:00
@Realchacal 

> The tabs represent different accounts, not different subaddresses!

your mockup shows them as one in the same? the 'retirement' tab and the 'trading tab'  are also address and subaddress 1 and 2 respectively.

perhaps I am missing something. in your list of accounts, the column says "first address" of each account. does that mean that there is a tree of subaddresses that the current GUI does not show?

## ghost | 2019-09-05T01:08:48+00:00
@1blockologist On the `Accounts` page the current GUI shows only the first subaddress of each account. But every account has many more subaddresses, which you find on the `Receive` page of each account. This basic concept isn't changed with this proposal.

But I see the problem. Showing addresses on the `Accounts` page can cause misconceptions like:
- "Ah, in Monero an account is an address!"
- "Ah, every account has exactly one address!"
- "Ah, every account has one account number!"

To fight such misconceptions, I just updated the captions:
![image](https://user-images.githubusercontent.com/46682965/64336335-fadc3100-cfdc-11e9-9a4f-2576ac219d4d.png)

## 1blockologist | 2019-09-05T01:12:11+00:00
@Realchacal ah I just looked! Thanks for helping me understand that, very amazing!

I don't think this concept is adequately conveyed by either of the GUIs, or the team and this affects the UX critiques and possibilities

I'll mull it over

# Action History
- Created by: ghost | 2019-09-01T05:44:17+00:00
