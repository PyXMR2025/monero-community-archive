---
title: Not all language fields are updated after selecting a new language with flag
  icon
source_url: https://github.com/monero-project/monero-gui/issues/2004
author: rating89us
assignees: []
labels:
- bug
- resolved
created_at: '2019-03-11T10:02:36+00:00'
updated_at: '2019-04-27T00:45:36+00:00'
type: issue
status: closed
closed_at: '2019-04-27T00:45:36+00:00'
---

# Original Description
If you select a new language on flag icon, almost all fields are updated to the new language, but some aren't.

# Discussion History
## dEBRUYNE-1 | 2019-03-11T11:35:24+00:00
This may simply be due to incomplete translations. Pinging @erciccione. 

## rating89us | 2019-03-11T11:37:38+00:00
No, this is happening when I change from my native language back to english (which is wallet's default).

## dEBRUYNE-1 | 2019-03-11T15:58:57+00:00
Interesting, definitely a bug then. 

+bug

## mmbyday | 2019-03-13T01:58:34+00:00
@rating89us  Without knowing exactly what fields you're referring to, I submitted PR #2016 that might fix some of the issues you're seeing. HTH. Please let us know if this fixes it. Thanks.

## sanderfoobar | 2019-04-10T02:52:04+00:00
@rating89us Does this still happen on the latest release?

## rating89us | 2019-04-17T11:00:08+00:00
Sorry, I can't test it now. 

## GBKS | 2019-04-18T09:23:35+00:00
This issue came up in user testing on March 27. Right on the initial welcome screen, the button labels don't update then you pick a different language. So "Language" stays "Language", and "Continue" stays "Continue", even if you pick German or something else. That caused users to think the language selector was broken. Totally understandable if some things don't translate because of missing Strings, but would be cool to fix this particular issue so it doesn't feel broken.

## selsta | 2019-04-18T09:26:58+00:00
This should be solved since #2088.

## erciccione | 2019-04-18T09:54:35+00:00
My build fails, so i cannot test this, but as selsta says, it should be solved. Maybe @xmrdsc will have a second to check if it's solved.

## selsta | 2019-04-27T00:37:28+00:00
+resolved

# Action History
- Created by: rating89us | 2019-03-11T10:02:36+00:00
- Closed at: 2019-04-27T00:45:36+00:00
