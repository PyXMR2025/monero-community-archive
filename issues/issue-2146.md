---
title: 'translations: it+es are using nodo-remoto '
source_url: https://github.com/monero-project/monero-site/issues/2146
author: plowsof
assignees: []
labels:
- i18n
created_at: '2023-04-07T12:36:50+00:00'
updated_at: '2023-04-20T12:35:44+00:00'
type: issue
status: closed
closed_at: '2023-04-20T12:35:43+00:00'
---

# Original Description
jorgesumle reported on matrix the term "nodo-remoto" appears as "@nodo-remoto" with no link at https://www.getmonero.org/es/downloads/index.html

After a quick look, it is just not translated / the term not yet appended https://github.com/monero-project/monero-site/blob/6cd7e19300e17847b80d33091b3cb333af7a2a46/_i18n/es/resources/moneropedia/weblate/remote-node.po#L28

Issue 2 is that the Italian files also want to use nodo-remoto :
https://github.com/monero-project/monero-site/blob/6cd7e19300e17847b80d33091b3cb333af7a2a46/_i18n/it.yml#L231
https://github.com/monero-project/monero-site/blob/6cd7e19300e17847b80d33091b3cb333af7a2a46/_i18n/it.yml#L263

Italian po file does not have a translation either (but nodo-remoto appears more in Spanish files, not sure who should use what)
https://github.com/monero-project/monero-site/blob/6cd7e19300e17847b80d33091b3cb333af7a2a46/_i18n/it/resources/moneropedia/weblate/remote-node.po#L28

edit* of course i am assuming that 2 languages can not use the same definition.

# Discussion History
## erciccione | 2023-04-13T08:22:30+00:00
Sharing the same definitions is not a problem, since languages are self-contained. The only issue seem to be that `@nodo-remoto` appears instead of the link, but that's expected until the terms are translated. This is the case for all pages still untranslated that contain links to moneropedia entries.

## plowsof | 2023-04-20T12:35:43+00:00
thanks, my only concern was for the 'clash'. closing

# Action History
- Created by: plowsof | 2023-04-07T12:36:50+00:00
- Closed at: 2023-04-20T12:35:43+00:00
