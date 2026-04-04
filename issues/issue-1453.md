---
title: '[BUG] if we change transaction priority it will change back to default if
  we change the tab'
source_url: https://github.com/monero-project/monero-gui/issues/1453
author: krtschmr
assignees: []
labels:
- Hacktoberfest
created_at: '2018-06-07T05:28:22+00:00'
updated_at: '2018-12-18T15:36:44+00:00'
type: issue
status: closed
closed_at: '2018-12-18T15:36:43+00:00'
---

# Original Description
- change priority
- go on receive tab
- go on send tab
- priority is back to default




# Discussion History
## pazos | 2018-06-07T15:40:53+00:00
hey, AFAIK this is the intended behaviour, not a bug. You fill the form and send a payment, next time you'll do that again. Almost all the form items are empty by default and the priority is, errrr, default too.

## krtschmr | 2018-06-07T15:52:32+00:00
@pazos 

if i fill in an address, then change the tab, then go back, the address is still in. 

i just tested, literally *everything* is persistent, except the priority. doesn't make sense. 

## cryptochangements34 | 2018-06-07T18:36:57+00:00
I agree this sounds more like a bug. It doesn't make much sense for the address, amount, payment id, etc to all be somewhat persistent while the priority always gets reset.

## pazos | 2018-06-09T19:09:39+00:00
err, in that case we can do:

1. wipe all values on page changed.  **or**
2. keep all stuff as is and add a clean button to wipe all form data manually if the payment is not sent( ie: wipe all lineEdits and set combobox index to 0)


## krtschmr | 2018-06-10T15:51:54+00:00
wipe it after a transaction was successfully send. unless it's send, keep whatever we did.

## erciccione | 2018-10-06T15:59:51+00:00
+hacktoberfest

# Action History
- Created by: krtschmr | 2018-06-07T05:28:22+00:00
- Closed at: 2018-12-18T15:36:43+00:00
