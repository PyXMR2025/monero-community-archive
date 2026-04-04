---
title: Link to translate.getmonero.org is dead, how to fix translation?
source_url: https://github.com/monero-project/monero-site/issues/2308
author: slrslr
assignees: []
labels:
- 🧰 back end
created_at: '2024-06-18T18:51:29+00:00'
updated_at: '2026-01-27T11:30:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
At https://github.com/monero-project/monero-site?tab=readme-ov-file#translation is a link to https://translate.getmonero.org which fails to load (Bad gateway Cloudflare error).

# Discussion History
## plowsof | 2024-06-19T11:37:41+00:00
thanks, back end admin is aware, It's an on-going issue for over a year now. It seemed to have been resolved recently but then back offline. Im currently on-boarding myself for actually pulling in changes from weblate and getting them live on site, spent the last several days setting up some automated workflows and such. ill soon be ready to actually work with an 'online weblate'. we can keep this issue open until that happens. 

Stability of the machine its running on / availability of back admin admin (volunteer) to fix things has been our main issue. The Tor project for example pays weblate to handle that. Hosted weblate is available starting at 37eur/month. If we can't get weblate online then we have to consider this option.

## plowsof | 2024-07-04T08:31:08+00:00
@xmrscott has stepped forward to undertake the role of translations coordinator. i have made progress with updating current translations https://github.com/plowsof/monero-site/pull/28 and will handle reviews/conflicts to add in the new stuff from weblate to give them a head start where possible. leaving the remaining issue: an online / stable weblate instance. Digilol has shown interest in this handling that for core. 

## jermanuts | 2024-12-05T23:33:53+00:00
@plowsof any update? If no one is willing to fix Weblate then why not pay Weblate to do it for you?

## jorgesumle | 2025-07-03T09:45:23+00:00
I think that links to the broken Weblate instance should be removed until you solve this issue. They can be found in the header of the site, in the README, etc.

## plowsof | 2026-01-27T00:24:52+00:00
https://translate.monerodevs.org for https://beta.monerodevs.org 

## jermanuts | 2026-01-27T10:26:37+00:00
https://beta.monerodevs.org/ will be the upcoming monero redesign website, will be then on getmonero.org, you can contribute to translation on https://translate.monerodevs.org/

## jorgesumle | 2026-01-27T10:38:40+00:00
> https://beta.monerodevs.org/ will be the upcoming monero redesign website, will be then on getmonero.org, you can contribute to translation on https://translate.monerodevs.org/

I can't start a new language translation there. Right now there are only three languages available and you can't suggest a new one.

## redsh4de | 2026-01-27T11:30:00+00:00
> > https://beta.monerodevs.org/ will be the upcoming monero redesign website, will be then on getmonero.org, you can contribute to translation on https://translate.monerodevs.org/
> 
> I can't start a new language translation there. Right now there are only three languages available and you can't suggest a new one.

Should be possible now, project was set to Protected

# Action History
- Created by: slrslr | 2024-06-18T18:51:29+00:00
