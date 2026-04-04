---
title: The "privacy level" slider doesn't convey meaningful information
source_url: https://github.com/monero-project/monero-gui/issues/142
author: antanst
assignees: []
labels:
- enhancement
- resolved
created_at: '2016-11-09T20:09:05+00:00'
updated_at: '2018-11-18T19:54:32+00:00'
type: issue
status: closed
closed_at: '2018-11-18T19:54:32+00:00'
---

# Original Description
Seasoned Monero users that know what a mixin is, have no indication of what mixin value corresponds to a specific counter location.

New Monero users don't know what to choose there and there's no information provided to help them.

May I suggest that at least the applied mixin value is shown? This way a user can at least google "mixin" to find out what it's all about, and experienced users have sufficient information.

# Discussion History
## dEBRUYNE-1 | 2016-11-09T20:25:27+00:00
FWIW, mixin is shown in the confirmation message. 


## medusadigital | 2016-11-23T15:36:48+00:00
is confirmation message good enough? personally i would prefer having it somewhere visible too, maybe even as changeable field, so the user can add their own mixing ? 

with ringCt, much higher mixing values will be possible before reaching the transaction size limit. 

or is the slider enough for "normal" users and we should close this? 

## antanst | 2016-11-23T15:43:20+00:00
Confirmation message isn't informative imho. The user doesn't know what changes when he moves the slider. A simple label below the slider that prints the active mixin should be enough I guess.

## medusadigital | 2017-08-07T20:00:29+00:00
+enhancement

would prefer to not do this via Tiptext (also because this can be turned off, and maybe will be by default)

## leafcutterant | 2018-03-06T15:11:36+00:00
Currently, the chosen "privacy level" is shown in parentheses.

![mixin](https://user-images.githubusercontent.com/7106231/37039839-b758797c-2158-11e8-9adf-dc0550368f34.png)

BUT I think it's very hard to notice that it changes with moving the slider. I suggest placing it after a semicolon and using a larger font size for the value, e.g.:

Privacy level (ringsize): **5**

(Imagine a bigger font for the "5" as markdown won't let me change that within a line.)

Also, the "Transaction cost" label on the far end of the slider is confusing. If I wouldn't know what it means, I' think the slider is a trade-off between privacy level and transaction cost. (This  would make people always use the lowest actual privacy level.) It should just somehow communicate that the transaction cost correlates with the privacy level. Maybe put it i a new line under the privacy level:

Privacy level (ringsize): **6**
Transaction cost: **~20% higher**

(I'd use a percentage here because the 1.2x notation is already used by the Tx priority and it would be just more confusing. The 100% base would always be the lowest allowed mixin.)

## erciccione | 2018-11-18T12:45:17+00:00
The slider has been removed. Closing this

+resolved

# Action History
- Created by: antanst | 2016-11-09T20:09:05+00:00
- Closed at: 2018-11-18T19:54:32+00:00
