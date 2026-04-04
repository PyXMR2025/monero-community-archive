---
title: Change structure of the sections in en.yml that are not easily parsed by Weblate
source_url: https://github.com/monero-project/monero-site/issues/957
author: erciccione
assignees:
- erciccione
labels:
- i18n
created_at: '2020-04-28T12:57:14+00:00'
updated_at: '2020-05-15T18:44:33+00:00'
type: issue
status: closed
closed_at: '2020-05-15T18:44:33+00:00'
---

# Original Description
The structure of some sections of `en.yml` needs some changing if we want Weblate to parse everything correctly. We had a problem few weeks ago (reported by @netrik182 on `#monero-translations`) where some sections got messed up and a lot of work was necessary in order to have everything working as intended.

I already started the refactoring with #934 (the library), but other sections need to be adjusted:

- [x] The list of IRC channels: https://github.com/monero-project/monero-site/blob/master/_i18n/en.yml#L97
- [x] The press kit https://github.com/monero-project/monero-site/blob/master/_i18n/en.yml#L233

For reference, this issue was discussed and confirmed in https://github.com/WeblateOrg/weblate/issues/3796

# Discussion History
# Action History
- Created by: erciccione | 2020-04-28T12:57:14+00:00
- Closed at: 2020-05-15T18:44:33+00:00
