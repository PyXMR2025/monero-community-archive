---
title: Hide wallet balance from initial view
source_url: https://github.com/monero-project/monero-gui/issues/693
author: BoscoMurray
assignees: []
labels:
- feature
- resolved
created_at: '2017-04-24T19:22:43+00:00'
updated_at: '2018-12-14T19:18:26+00:00'
type: issue
status: closed
closed_at: '2018-12-14T19:18:26+00:00'
---

# Original Description
When using Monero Core in a public place it is easy for 3rd parties to see a wallet balance if they can see the laptop screen.
In order to preserve users private information, it might be good if a wallet balance was not immediately on display when the wallet is opened. It could perhaps become visible with a mouse-over the area that currently shows the wallet balance, or some other method could be used to reveal it.
Users can then freely open a wallet, transact and view transaction history without needing to clearly display a wallet balance.

# Discussion History
## jonathancross | 2017-04-26T10:57:36+00:00
I like this idea.  It might help to reinforce the notion that "Monero prioritizes privacy" and make it clear to new users they are in control.

I made a few quick mocks to get the conversation started.

Hidden balance:
![2017-04-26_balance-hidden](https://cloud.githubusercontent.com/assets/5115470/25430996/0a65fcf6-2a7f-11e7-9a48-8d39f5ceba7a.png)

Shown balance:
![2017-04-26_balance-shown](https://cloud.githubusercontent.com/assets/5115470/25431003/0e8a2140-2a7f-11e7-937d-fdf62b01ba16.png)

We should make it brainless to show the balance: user can click on the icon, "Balance" text label, the actual placeholder dots, lock icon, etc.

We should discuss what the initial state should be (_hidden_ or _shown_) and if that requires a new setting for configuring the default (some users may not want the balance to be hidden by default).  Making it "sticky" (saved between wallet sessions) would probably avoid us having to add a new setting.

Thoughts / feedback?

## mariodian | 2017-05-09T12:13:48+00:00
Good idea. I would even go so far to remove the giant "MONERO" logotype at the top left corner. It may draw too much uneeded attention.

Btw nice mockups. I like the user-configurable idea.

## jonathancross | 2017-05-13T10:51:45+00:00
Let's keep this feature request focused on **hiding the wallet balance** and wait for more feedback from other project contributors.

> remove the giant "MONERO" logo...

Personally, I think this is going too far as it is needed for branding and just to make it clear what app you are using.  It might be considered in the _distant_ future, but I think there are many other things we would want to focus on first.  Anyhow, such requests should be discussed elsewhere. :-)



## BoscoMurray | 2017-05-13T11:06:45+00:00
I like your mockups, jonathancross, and the idea to switch the balance display on/off is better than my initial mouseover suggestion I think.

I'm not sure about the sticky feature. Say you forget to hide the balance before closing a wallet, then open the wallet again in a public place, you'll be scrambling to hide the balance. A "hide by default" option in Settings might be better. How about also a popup that appears the first time you hide your balance that asks the user, "Hide by default?".

By default a visible balance is probably OK, since new wallets will contain zero coins. Users who want to make their balance hidden from view (because they go out their way for utmost privacy) are likely to use and know the wallet, hence will set it as they like before using in a public place.

Are the settings for wallets stored with each wallet seperately, or will these settings be global?

## QuickBASIC | 2017-05-30T06:01:21+00:00
If a user is truly that paranoid or in a public space there's nothing stopping them from doing the transaction on monerod in a terminal window.

## dEBRUYNE-1 | 2017-08-09T13:25:51+00:00
+feature

## jonathancross | 2017-08-11T20:13:44+00:00
> Are the settings for wallets stored with each wallet seperately, or will these settings be global?

Such questions show why even small changes can turn into a lot of dev time, user confusion, etc.  I would suggest they be at the app level (meaning global for all wallets) as they are an expression of user-preference.

Anyhow, this looks like a very low priority in the grand scheme of things.

## sanderfoobar | 2018-12-13T18:33:37+00:00
Implemented since #1802 

+resolved

## dEBRUYNE-1 | 2018-12-14T19:10:02+00:00
+resolved

# Action History
- Created by: BoscoMurray | 2017-04-24T19:22:43+00:00
- Closed at: 2018-12-14T19:18:26+00:00
