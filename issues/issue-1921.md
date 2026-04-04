---
title: Links don't open in new tabs
source_url: https://github.com/monero-project/monero-site/issues/1921
author: konstantinosfragkoulis
assignees: []
labels:
- enhancement
created_at: '2022-01-28T08:17:03+00:00'
updated_at: '2022-12-27T10:55:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
On the website there are many links which have next to them the symbol that indicates that they will open in a new tab but they don't
![Screenshot from 2022-01-28 10-13-18](https://user-images.githubusercontent.com/92216292/151511401-71f4000c-17f2-4fcb-9cd7-b9c2534c39e1.png)
.

# Discussion History
## erciccione | 2022-01-30T10:15:27+00:00
The symbol is to warn the user that they are about to click on an external link. Meaning they will leave getmonero for an external website, it's not meant to signal that a new tab will be open.

Either way, i'm ok with #1922, which makes external links open in a new tab.

## FedericoNembrini | 2022-12-26T20:26:31+00:00
I saw that pull request #1922  has been closed, maybe I can take care of that.

From what I've read, `target="_blank"` should be added to all `<a />` that lead to sites other than this one (or rather, those to which this style `a[href^="https:"]:not([href*="getmonero.org"]`) is applied).

The resource files in the _i18n/ directory shouldn't be modified, right?

## erciccione | 2022-12-27T10:55:50+00:00
@FedericoNembrini that would be appreciated, thanks :)

>The resource files in the _i18n/ directory shouldn't be modified, right?

Only the english files should be edited (`en` folder and `en.yml`)

# Action History
- Created by: konstantinosfragkoulis | 2022-01-28T08:17:03+00:00
