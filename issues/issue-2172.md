---
title: String gets picked for translations, but there isn't anything to translate
  and results empty
source_url: https://github.com/monero-project/monero-gui/issues/2172
author: erciccione
assignees: []
labels: []
created_at: '2019-05-20T11:24:04+00:00'
updated_at: '2020-06-15T06:24:23+00:00'
type: issue
status: closed
closed_at: '2020-06-15T06:24:23+00:00'
---

# Original Description
For some reason [line 91 in Transfers.qml](https://github.com/monero-project/monero-gui/blob/master/pages/Transfer.qml#L91) gets picked as translatable. The problem is that it's not a translatable string and it will be shown as empty to translators.

See on Pootle:
![pootle-empty-string](https://user-images.githubusercontent.com/28106476/58017803-661ef780-7b01-11e9-9043-c0e26c3583f9.png)

If checked manually with QTlinguist, it's labelled as *context comment*: 
![empty-string-linguist](https://user-images.githubusercontent.com/28106476/58017818-6fa85f80-7b01-11e9-9560-6e7c1898dfa3.png)

The problem is still there after pulling master and refreshing the language files. Moving the comment outside the function didn't help.

# Discussion History
## selsta | 2019-05-30T01:21:20+00:00
`// @TODO: ...` is used in various places, I don’t see any reason for it getting picked up as a context comment here :/

## selsta | 2020-06-14T22:37:54+00:00
@erciccione Is this still happening?

## erciccione | 2020-06-15T06:24:23+00:00
No, i forgot to close the issue :)

# Action History
- Created by: erciccione | 2019-05-20T11:24:04+00:00
- Closed at: 2020-06-15T06:24:23+00:00
