---
title: Esperanto seed option not used in GUI
source_url: https://github.com/monero-project/monero-gui/issues/1131
author: apertamono
assignees: []
labels: []
created_at: '2018-02-20T22:56:57+00:00'
updated_at: '2018-03-14T11:54:35+00:00'
type: issue
status: closed
closed_at: '2018-03-14T11:54:34+00:00'
---

# Original Description
In languages.xml, the wallet_language parameter for Esperanto is still set to English, although there is a mnemonic seed word list in Esperanto now. I assume this parameter refers to the mnemonic seed language, since it's localized for other languages like Russian and Japanese that have localized seeds but not a localized CLI and daemon.

`        <language display_name="Esperanto" locale="eo" wallet_language="English" flag="/lang/flags/esperanto.png" qs="none"/>
`
in https://github.com/monero-project/monero-gui/blob/master/lang/languages.xml

I don't feel comfortable changing this myself in an important file. I'm not sure if anything else needs to be changed in order to enable selecting Esperanto. But I would like to see Moneristoj actually use the word list I compiled.


# Discussion History
## glv2 | 2018-02-21T10:02:03+00:00
There is no other line to change to use the Esperanto word list when the Esperanto locale is used.

So you just have to make a pull request changing the line
```<language display_name="Esperanto" locale="eo" wallet_language="English" flag="/lang/flags/esperanto.png" qs="none"/>```
to
```<language display_name="Esperanto" locale="eo" wallet_language="Esperanto" flag="/lang/flags/esperanto.png" qs="none"/>```
and new wallet generation will use the right word list.


## apertamono | 2018-03-02T16:20:19+00:00
Thanks, that's surprisingly easy! 

Complication: I accidentally made another commit in my forked master branch. I'll make a pull request for this issue after sorting that out.

## apertamono | 2018-03-14T11:54:34+00:00
PR #1154 merged.

# Action History
- Created by: apertamono | 2018-02-20T22:56:57+00:00
- Closed at: 2018-03-14T11:54:34+00:00
