---
title: 'Discussion: the path forward '
source_url: https://github.com/monero-project/monero-docs/issues/5
author: plowsof
assignees: []
labels: []
created_at: '2024-07-27T11:13:19+00:00'
updated_at: '2024-07-28T07:32:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
i assume this will be put into #1

these seem to be our options:
- starting with Just the docs + monerodocs original files. for reference, monero-docs master branch looks like https://md.monerodevs.org/ 
- update the original monerodocs front/backend to their latest versions : for reference: https://md.monerodevs.org/ is a preview of https://github.com/plowsof/md/tree/latest_mkdocs_test
    - the original monerodocs has calls to googleapi's for fonts, this is not the case with the updated version that uses the [privacy plugin](https://squidfunk.github.io/mkdocs-material/plugins/privacy/)
    - git-committers plugin to display contributors at the bottom / and also last revision date (compatible with localisation) e.g. this [cryptography related page](https://md.monerodevs.org/cryptography/asymmetric/introduction/). We can accept contribs from anyone * or commit external contribs using appropriate author name * e.g. MAGIC can submit PR's under a specific account

all of the above is flexible / not been decided on*

# Discussion History
## jermanuts | 2024-07-27T16:50:10+00:00
https://getmonero.dev/ is more up-to-date docs

## nahuhh | 2024-07-27T17:25:12+00:00
.dev has some updates to it, but also some unnecessary (imo) changes. Its adapted for justthedocs, which has issues with no-js

## dan-is-not-the-man | 2024-07-28T00:31:42+00:00
I would stick to mkdocs material as it has better plugins and is designed for documentation. As ofrn said no js breaks the drop down menus for justfordocs and also majority of the work has been done already. Also i'm not sure it has localization. With mkdocs material there is  [plugins](https://squidfunk.github.io/mkdocs-material/plugins/):

- [localization](https://github.com/ultrabug/mkdocs-static-i18n)

- [Building Site Offline ](https://squidfunk.github.io/mkdocs-material/plugins/offline/?h=offline)

# Action History
- Created by: plowsof | 2024-07-27T11:13:19+00:00
