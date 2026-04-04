---
title: Add "Remember language" option
source_url: https://github.com/monero-project/monero-gui/issues/1225
author: leafcutterant
assignees: []
labels:
- resolved
created_at: '2018-03-31T05:22:51+00:00'
updated_at: '2019-03-13T07:45:38+00:00'
type: issue
status: closed
closed_at: '2019-03-13T07:45:38+00:00'
---

# Original Description
There is no point in showing the language selector every time a new wallet is opened. Once a user chooses a language, they will probably stick with it (and even in the rare cases when multiple people use the same OS account on the same machine, they will be probably of the same language).

My suggestion:
* Add a `☑ Remember language` tick box to the language selector screen. If a language is selected after ticking this, Monero from there on will skip the language selector and go to the New/Restore/Open screen whenever a new wallet should be opened,
* Add a `Change language ` button to the bottom left corner of the New/Restore/Open screen in case someone changes their mind or a new user with a different language accesses the application. Display the flag icon of the present language next to the button so that it's obvious it leads to the language selector even if the new user doesn't speak the presently selected language.

# Discussion History
## tficharmers | 2018-04-20T08:18:53+00:00
I like this. Should there also be a 'Change language' option in the 'Advanced' tab/page?

By the way, here are the [proposed designs for the setup screens](https://raw.githubusercontent.com/GBKS/monero-wallet-design/master/screens/desktop-dark/onboarding-overview.png).

## leafcutterant | 2018-04-21T12:32:42+00:00
I think a 'Change language' option in the 'Advanced' tab won't do any harm, so yes, sure.

The new designs look cool!

## mmbyday | 2019-03-13T02:24:48+00:00
+resolved
by wizard redesign.

## dEBRUYNE-1 | 2019-03-13T07:26:10+00:00
+resolved

# Action History
- Created by: leafcutterant | 2018-03-31T05:22:51+00:00
- Closed at: 2019-03-13T07:45:38+00:00
