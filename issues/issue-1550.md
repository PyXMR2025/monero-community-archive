---
title: Add warning in wizard before copying the seed to clipboard
source_url: https://github.com/monero-project/monero-gui/issues/1550
author: Leza89
assignees: []
labels:
- easy
- Hacktoberfest
created_at: '2018-08-24T18:23:13+00:00'
updated_at: '2018-12-29T21:03:38+00:00'
type: issue
status: closed
closed_at: '2018-12-29T21:03:38+00:00'
---

# Original Description
While translating I came across:

<location filename="../wizard/WizardMemoTextInput.qml" line="65"/>
<source>Seed copied to clipboard</source>

I did not come across a warning however, informing the user about the potential security risk for putting the seed in plain text into the clipboard.

Please consider adding a warning like
"Coyping your seed to clipboard exposes you to the threat of malicious software recording your seed and sharing it with third parties. To be sure please write your seed down manually."

# Discussion History
## erciccione | 2018-10-06T15:51:40+00:00
+hacktoberfest

## sanderfoobar | 2018-11-18T17:00:38+00:00
+easy

# Action History
- Created by: Leza89 | 2018-08-24T18:23:13+00:00
- Closed at: 2018-12-29T21:03:38+00:00
