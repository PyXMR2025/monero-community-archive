---
title: Add conversion price in CSV export when option is enabled
source_url: https://github.com/monero-project/monero-gui/issues/1917
author: SamsungGalaxyPlayer
assignees: []
labels:
- feature
created_at: '2019-01-27T18:21:10+00:00'
updated_at: '2022-09-05T20:46:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Related to #1897 and #1714.

The CSV export option should include a column with the approximate historical conversion price for the selected currency if the pricing/fiat conversion is enabled.

Perhaps a warning should be added when clicking the export transactions button if the currency conversion is on, saying this leaks metadata. Add an options in the screen to 1) export anyway, 2) export safely, 3) cancel.

This feature is useful for accounting purposes, since it allows users to optionally find the approximate value in another currency at the time the transaction took place. If this was done manually, it would take a lot of time for many transactions.

# Discussion History
## sanderfoobar | 2019-01-28T13:26:10+00:00
+feature

## akshatakulkarni25 | 2022-09-05T07:01:26+00:00
Hello. I am Akshata Kulkarni. I am interested in working on this issue. Is this issue still open to work on??It would be my first issue. Could you also please guide through this issue.Thanks

## selsta | 2022-09-05T20:46:24+00:00
A data source is required for historical price.

# Action History
- Created by: SamsungGalaxyPlayer | 2019-01-27T18:21:10+00:00
