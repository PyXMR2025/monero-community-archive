---
title: Language selection not skipped when wallet is closed from settings page
source_url: https://github.com/monero-project/monero-gui/issues/310
author: ClementJnc
assignees: []
labels:
- resolved
created_at: '2016-12-18T18:43:53+00:00'
updated_at: '2017-08-07T19:15:10+00:00'
type: issue
status: closed
closed_at: '2017-08-07T19:15:10+00:00'
---

# Original Description
When there is only one language accepted (as now), the GUI opens the Wizard directly to the optionsPage ("Create"/"Recover"/"Open") rather than to the welcomePage (language choice). It works also like that when the user cancels the opening of the last wallet from the pop-up window. However if the user clicks on "Close wallet" in the setting, he goes to the welcomePage instead of the optionPage I would expect.

# Discussion History
## medusadigital | 2017-04-18T09:25:50+00:00
seems solved to me now that there are more languages.

can you confirm? 

## dEBRUYNE-1 | 2017-08-07T17:41:24+00:00
+resolved

# Action History
- Created by: ClementJnc | 2016-12-18T18:43:53+00:00
- Closed at: 2017-08-07T19:15:10+00:00
