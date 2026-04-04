---
title: '[Discussion] Description of the View-Only wallet incorrect'
source_url: https://github.com/monero-project/monero-gui/issues/1610
author: Leza89
assignees: []
labels:
- resolved
created_at: '2018-10-07T20:45:11+00:00'
updated_at: '2018-11-03T17:09:22+00:00'
type: issue
status: closed
closed_at: '2018-11-03T17:09:22+00:00'
---

# Original Description
Hey there,

 I wanted to discuss if you guys see a need to change the following description:

> `<location filename="../pages/settings/SettingsWallet.qml" line="185"/>`
> `        <source>Creates a new wallet that can only view transactions, cannot initialize transactions.`

Since a view-only wallet can initialize transactions; Just not sign them.

However my idea

> Creates a new wallet that can only view and send transactions, but cannot sign transactions.

might confuse new users.

Any ideas or do you think we should leave it as is?

# Discussion History
## stoffu | 2018-10-15T12:14:29+00:00
Agreed for the need of change. Like this maybe?

> Creates a new wallet that can only view and initiate transactions, but cannot sign transactions.


## Leza89 | 2018-10-15T19:13:08+00:00
Ah.. getting closer

What about

>Creates a new wallet that can only view and initiate transactions, but **requires a spendable wallet to sign and send** transactions.

Is that too convoluted already?

## stoffu | 2018-10-15T21:50:10+00:00
Technically, signing requires the spendable wallet, but sending (submitting) a signed transaction doesn’t. Maybe your version could cause some confusion?

## Leza89 | 2018-10-16T17:48:49+00:00
Yes that is the problem. However do you think someone new to crypto (which at this point basically is everyone) will understand the concept of signing? I'm searching for a way to phrase it that'll make it obvious.

>Creates a new wallet that can only view and initiate transactions, but requires a spendable wallet to sign transactions before sending.

## stoffu | 2018-10-16T23:01:30+00:00
Just my guess, but the phrase “sign a transaction” seems to already literally imply (without technical context) giving a clear approval to some tentative action. So your above text seems to read naturally even for new users.

Also, the concept of view-only wallet and cold signing itself already assumes some minimal level of education on the user. If the user can’t understand the description, either look elsewhere for educational material, or not use the feature. After all, the problem being addressed here seems to be the accuracy of the description, not the approachability.


## Leza89 | 2018-10-17T19:20:11+00:00
>After all, the problem being addressed here seems to be the accuracy of the description, not the approachability.

When I'm translating I always try to make it as descriptive as possible while keeping it as short as possible. I prefer a phrasing that'll explain itself in one sentence instead of making the user duckduckgo'ing for 2 minutes.

If I got you correct though, you'd say that [this](https://github.com/monero-project/monero-gui/issues/1610#issuecomment-430332666) is a good approach and you'd just omit the "before sending" part?

## stoffu | 2018-10-18T13:16:07+00:00
> If I got you correct though, you'd say that this is a good approach and you'd just omit the "before sending" part?

Yes, I'm quite OK with your last version and even with "before sending" kept.


## erciccione | 2018-11-03T17:03:06+00:00
#1703 

+resolved

# Action History
- Created by: Leza89 | 2018-10-07T20:45:11+00:00
- Closed at: 2018-11-03T17:09:22+00:00
