---
title: Add possibility to activate language files before using them
source_url: https://github.com/monero-project/monero/issues/5753
author: erciccione
assignees: []
labels: []
created_at: '2019-07-15T10:57:55+00:00'
updated_at: '2019-08-22T15:59:37+00:00'
type: issue
status: closed
closed_at: '2019-08-22T15:59:37+00:00'
---

# Original Description
Right now if a language is added to `/translations` it gets automatically picked by the CLI. This is problematic because most of the time translators submit just a partial translation and if that gets automatically picked we would end up with a new language file containing a partial translation.

Would be better to be able to activate languages, so that even if they are commited to the repo (and uploaded in `/translations`) we can choose the right time to make them available in the wallet. This will give us more control over the language files and make the integration with Weblate not painful.

As discussed with @moneromooo-monero, probably the best approach is to create a list of languages in a file which can be activated when needed. Something similar to what we already do [with the GUI](https://github.com/monero-project/monero-gui/blob/master/lang/languages.xml).

# Discussion History
## erciccione | 2019-07-16T11:53:18+00:00
self-reminder: after this is resolved, commit unpushed translated strings of the unactivated languages from Pootle.

## moneromooo-monero | 2019-07-16T19:26:20+00:00
https://github.com/monero-project/monero/pull/5757

## erciccione | 2019-08-22T15:59:37+00:00
Resolved

# Action History
- Created by: erciccione | 2019-07-15T10:57:55+00:00
- Closed at: 2019-08-22T15:59:37+00:00
