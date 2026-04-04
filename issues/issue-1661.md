---
title: Non-translatable strings
source_url: https://github.com/monero-project/monero-gui/issues/1661
author: snaggen
assignees: []
labels:
- resolved
created_at: '2018-10-16T08:09:50+00:00'
updated_at: '2018-11-18T12:54:22+00:00'
type: issue
status: closed
closed_at: '2018-11-18T12:54:22+00:00'
---

# Original Description
I looked at the latest GUI and looked for untranslated strings using the Swedish translation that should be complete. I then found some un translated strings, that were not available in the monero-core_sv.ts file. That gave me the following non-translatable strings.

On the Send page:
Automatic (in the transaction priority dropdown).

On the Recieve page it lists adresses, I have an entry saying
`#0  Primary address <adress>`
Where the text "Primary address" is not translatable

On the History page: 
The entries in the sort dropdown is not translatable.
In each entry "Sent", "To", "Transaction ID" is not translatable.

On the Advanced -> Sign/Verify page, these strings are not translatable
"Message from file"
"Verify message"


# Discussion History
## erciccione | 2018-10-16T10:47:12+00:00
Thanks @snaggen , the absence of a code freeze make hard to have all strings synced for release. Will fix this asap

## erciccione | 2018-10-16T11:48:36+00:00
#1664 should fix this

## erciccione | 2018-11-18T12:38:55+00:00
+resolved

# Action History
- Created by: snaggen | 2018-10-16T08:09:50+00:00
- Closed at: 2018-11-18T12:54:22+00:00
