---
title: get_hashes() causes broken wallet cache in error case.
source_url: https://github.com/monero-project/monero/issues/1235
author: medusadigital
assignees: []
labels: []
created_at: '2016-10-18T15:45:24+00:00'
updated_at: '2016-12-08T22:40:14+00:00'
type: issue
status: closed
closed_at: '2016-12-08T22:40:14+00:00'
---

# Original Description
If get_hashes() cant run properly and has to return an error (like here https://github.com/monero-project/monero-core/issues/75), the situation is not handled proberly and can cause a corrupt wallet cache, which results in :
![genesis_missmatch](https://cloud.githubusercontent.com/assets/17108301/19485129/65c3b738-955a-11e6-9099-5834c3e1e0c3.png)


# Discussion History
## moneromooo-monero | 2016-10-18T20:28:36+00:00
I could reproduce the "GUI hangs", but whatever I did, I did not get that problem after reloading the wallet.


## medusadigital | 2016-12-08T22:40:14+00:00
can not reproduce.

--> closed

# Action History
- Created by: medusadigital | 2016-10-18T15:45:24+00:00
- Closed at: 2016-12-08T22:40:14+00:00
