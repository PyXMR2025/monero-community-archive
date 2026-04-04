---
title: Add wallet name to title bar
source_url: https://github.com/monero-project/monero-gui/issues/2325
author: ghost
assignees: []
labels: []
created_at: '2019-07-27T07:13:41+00:00'
updated_at: '2019-09-14T17:43:01+00:00'
type: issue
status: closed
closed_at: '2019-09-14T17:43:01+00:00'
---

# Original Description
[Updated! Thx @GBKS]
![image](https://user-images.githubusercontent.com/46682965/64293800-ae0d4180-cf6d-11e9-9edd-b225b2275855.png)
(Ignore changes from #2298, #2339, #2304.)

This is financial safety-critical because it's super easy to confuse wallets when the name is not shown prominently.

Alternative:
![image](https://user-images.githubusercontent.com/46682965/64327347-d1ff7000-cfcb-11e9-9f7b-f90aa9810e27.png)


# Discussion History
## rating89us | 2019-07-28T14:46:49+00:00
Where would you get the wallet's title from? From the .keys file?

## ghost | 2019-07-28T15:28:18+00:00
Sure!

## rating89us | 2019-07-28T15:42:55+00:00
That's a good idea. Window title should be "Mywallet.keys - Monero GUI"
Logo should be removed from title.

## ghost | 2019-07-28T15:58:36+00:00
- Agreed on putting the wallet name in front and dropping the logo.
- Not so sure about adding `.keys`. A normal user probably isn't aware at all that his wallet file actually is a `.keys` file. Even when opening a wallet the wallet names are presented without `.keys`.

## rating89us | 2019-07-28T16:59:08+00:00
Maybe we should start educating our users that a Monero wallet is nothing more than a .keys file. 

What about displaying .keys extension when in Advanced wallet, and don't displaying it in simple mode?

## ghost | 2019-07-28T17:16:42+00:00
> Maybe we should start educating our users that a Monero wallet is nothing more than a .keys file.

I think we can be happy enough if all users understand the basic safety concept of mnemonic seeds. We want to board millions of normal people in the future! :)

> What about displaying .keys extension when in Advanced wallet, and don't displaying it in simple mode?

Advanced users rather wouldn't need it.



## GBKS | 2019-07-30T11:54:33+00:00
How about removing "Monero" from the title bar altogether and just show the wallet name? It's not shown anyways if you disable custom decorations. The logo is still shown in the balance card on the left.

## ghost | 2019-07-30T12:55:05+00:00
@GBKS That would be awesome!!!

## dginovker | 2019-07-31T17:16:45+00:00
@GBKS I'd rather see both variations before deciding on that. To avoid clutter on small resolution monitors, I could see it working well for taskbars, but on the actual GUI bar it offers aesthetics 

## ghost | 2019-09-04T11:12:18+00:00
> I'd rather see both variations before deciding on that.

Proposal updated now showing @GBKS's variant. By far the best. (For older variants see "edited".)

## selsta | 2019-09-04T23:47:02+00:00
See #2376.

![menubar](https://user-images.githubusercontent.com/7697454/64300880-ebc69600-cf7e-11e9-8b1d-d73a8c3ab862.gif)

Also ping @dEBRUYNE-1, what do you think of not having the Monero logo in the titlebar?

## ghost | 2019-09-05T08:35:13+00:00
Very nice but **font size should be much smaller** (like the title before).

The logo adds visual complexity. In case you want the logo for clarity, this would be **more** helpful **and** simpler visually:

![image](https://user-images.githubusercontent.com/46682965/64327052-56052800-cfcb-11e9-89bd-9a5e6284ae24.png)
(2 blanks before and after the dash.)

## selsta | 2019-09-05T18:25:22+00:00
I reduced the font size from 24 to 20.

# Action History
- Created by: ghost | 2019-07-27T07:13:41+00:00
- Closed at: 2019-09-14T17:43:01+00:00
