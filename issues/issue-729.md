---
title: Update user guides with 0.12.0.0 GUI screenshots
source_url: https://github.com/monero-project/monero-site/issues/729
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2018-05-08T14:15:07+00:00'
updated_at: '2018-06-29T13:15:17+00:00'
type: issue
status: closed
closed_at: '2018-06-29T13:15:17+00:00'
---

# Original Description
Several guides should be updated for the latest 0.12.0.0 release.

The following need their screenshots updated:

https://getmonero.org/resources/user-guides/solo_mine_GUI.html
https://getmonero.org/resources/user-guides/remote_node_gui.html

The following need to have a section for using the GUI, including screenshots:

https://getmonero.org/resources/user-guides/view_only.html
https://getmonero.org/resources/user-guides/prove-payment.html
https://getmonero.org/resources/user-guides/restore_from_keys.html

# Discussion History
## erciccione | 2018-05-08T16:11:42+00:00
Maybe we can just point from those articles to the guide instead of create a dedicated part for the GUI? See https://github.com/monero-ecosystem/monero-GUI-guide/blob/master/monero-GUI-guide.md

+improvement

## SamsungGalaxyPlayer | 2018-05-08T16:45:24+00:00
@erciccione I suppose it depends on what sort of resource Monero should provide.

If we want to have references but use StackExchange for most things, then we can simply reference this guide.

If we want to replicate a lot of StackExchange content including common questions, I recommend we take components of the GUI guide (which is excellent btw) and include the relevant parts in these website guides.

## el00ruobuob | 2018-05-09T14:51:59+00:00
Personnaly i think we should update user-guides (in a best effort way) AND add a "more official" user-guide for the GUI, based on the gui guide which must be updated (and localized) in a short timeframe (a week or two) after a new version is released.
In this way, could we enhance the screenshots from the GUI guides? I mean, we could have "gimp layers" with the numbered bullet, so we could easily localized the screenshots. otherwize have a "screenshot toolkit" with all the things ready to be pasted on new screenshots, so everything is coherent across all languages and versions.

## el00ruobuob | 2018-05-13T15:23:12+00:00
I'll be doing the first two updates mentions by @SamsungGalaxyPlayer first.

## el00ruobuob | 2018-05-14T08:27:34+00:00
View-only is ready on my side.
I'll go with restore from keys now.

Regarding the prove payments, i'll need to run as testnet or a stagenet node and make transactions between wallets to be able to document it.

## el00ruobuob | 2018-05-14T15:55:14+00:00
There's also https://getmonero.org/resources/user-guides/restore_account.html to improve with the GUI part.
And https://getmonero.org/resources/user-guides/restore_from_keys.html should be moved to the Recovery section of user-guides, along with the "restore account" one.

## el00ruobuob | 2018-05-14T20:35:03+00:00
Done with restore from keyx on my side. I'll continue with restore account, as i only have one screenshot to change.

## el00ruobuob | 2018-05-15T11:24:17+00:00
Done with restore account. I'll try to do the prove payment update, but i cannot create a transaction on the testnet node i'm connected to (testnet.node.xmrlab.com:38081). All i've got is `Error: Can't create transaction: no connection to daemon. Please make sure daemon is running.`
Edit: Not giving up. I'm trying a self hosted testnet on one side, and a stagenet on another.

## el00ruobuob | 2018-05-16T08:43:08+00:00
I'm now private-testnet rich and stagenet rich.
Will do the screenshots and update the prove payment guide soon.

## el00ruobuob | 2018-05-16T13:36:10+00:00
Done.

## erciccione | 2018-06-25T09:57:22+00:00
Is this issue completely resolved @el00ruobuob ?

## el00ruobuob | 2018-06-28T19:27:46+00:00
Sorry i didn't see the ping.
yes. this can be closed @erciccione 

## erciccione | 2018-06-29T12:56:54+00:00
+resolved

# Action History
- Created by: SamsungGalaxyPlayer | 2018-05-08T14:15:07+00:00
- Closed at: 2018-06-29T13:15:17+00:00
