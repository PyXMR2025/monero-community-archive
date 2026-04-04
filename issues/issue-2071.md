---
title: Display viewkeys of the general fund / ccs
source_url: https://github.com/monero-project/monero-site/issues/2071
author: plowsof
assignees: []
labels:
- 💬 discussion
created_at: '2022-10-15T07:03:20+00:00'
updated_at: '2024-10-18T11:29:08+00:00'
type: issue
status: closed
closed_at: '2024-10-18T11:29:08+00:00'
---

# Original Description
User selenze asks ' the ccs keys may need to be displayed somewhere along with the gf and to include their view keys. ' 

```
ccs
43H2k6iDgyfNo4HzgQKF8ABALWGpRz9Ez6uexXLGFyuC32SevoaGUiKWbebSkqy5EzdkviwJ4NQwDHkxVxHceUtLBzBjoTV
645936bdbb2e13830f587351b73b226c7c107ff94e5db0e0dd19c661cd657b0a
```
General fund info found in this blog post:
https://www.getmonero.org/2021/06/24/general-fund-2020-2021-report.html

Is there an easy place to display this somewhere on site? or should it be on the ccs front end (not here) 

# Discussion History
## HardenedSteel | 2022-10-15T18:18:26+00:00
Duplticate of [Gitlab #4](https://repo.getmonero.org/monero-project/ccs-front/-/issues/4)

## plowsof | 2022-10-15T21:06:43+00:00
Thanks, so putting this somewhere on the ccs front end would make the most sense, rather than on -site. in the 'Donate to the monero project' footer? , i will leave this open for a bit in case anyone has any wildly different ideas then close as its not for -site 

## erciccione | 2022-10-20T08:26:31+00:00
If we want to add a view key, i would add it everywhere where the general fund address is displayed (beside past blog posts)

## plowsof | 2024-07-18T07:59:43+00:00
so adding the private view key under here seems enough:
https://github.com/monero-project/monero-site/blob/99fd539bea6b819ce1a3a02722d3062cf6f18fc6/get-started/contributing/index.md?plain=1#L73

further work i'd like to see: all mentions of the GF xmr/btc address will be done via a variable e.g. `site.gf_xmr` / `site.gf_btc` (instead of hardcoded) and the hashes of QR codes noted. A github CI script would confirm these during build. we sometimes have huge +100k translation PR's and an address edit here and there could be missed. (the address moneropedia entry for example has the GF address listed)

# Action History
- Created by: plowsof | 2022-10-15T07:03:20+00:00
- Closed at: 2024-10-18T11:29:08+00:00
