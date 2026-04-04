---
title: Empty balance doesn't need to show all 12 decimal places
source_url: https://github.com/monero-project/monero-gui/issues/563
author: ghost
assignees: []
labels:
- resolved
created_at: '2017-03-18T18:01:19+00:00'
updated_at: '2018-11-18T18:27:33+00:00'
type: issue
status: closed
closed_at: '2018-11-18T18:27:33+00:00'
---

# Original Description
From a design level, it only adds confusion to a new person looking at the GUI. For an empty wallet balance, it's better to have it read 0.0 instead of 0.000000000000.

Once there's a balance below the first decimal place, of course it's good to show the entire balance to the current decimal place (eg: 0.000023 could include six numbers after the decimal point).

# Discussion History
## erciccione | 2018-11-18T13:12:39+00:00
This is still valid, but looks like nobody cared to change it. so, closing. Can be reopen if somebody change their mind.

+resolved

# Action History
- Created by: ghost | 2017-03-18T18:01:19+00:00
- Closed at: 2018-11-18T18:27:33+00:00
