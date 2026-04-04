---
title: 'Setup Wizard :: Auto donation behavior'
source_url: https://github.com/monero-project/monero-gui/issues/79
author: M5M400
assignees: []
labels: []
created_at: '2016-10-20T13:03:33+00:00'
updated_at: '2016-11-13T17:59:14+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:59:14+00:00'
---

# Original Description
1) It is possible to leave the auto donation percentage empty and still activate auto donation via the checkbox:

![screenshot from 2016-10-20 14-12-05](https://cloud.githubusercontent.com/assets/22886679/19560708/bfbdc608-96d5-11e6-9c8c-5cb6c43148cf.png)
![screenshot from 2016-10-20 14-12-30](https://cloud.githubusercontent.com/assets/22886679/19560713/c561da40-96d5-11e6-9387-c839328184a3.png)

2) after messing around with empty auto donation field, I deleted the wallet folder and restarted the gui. In the setup wizard the default value for auto donation is no longer "50", but "-2147483648", which can also be confirmed in the next screen:

![screenshot from 2016-10-20 14-22-38](https://cloud.githubusercontent.com/assets/22886679/19560830/4901c40a-96d6-11e6-8435-2dfeecf97b42.png)
![screenshot from 2016-10-20 14-57-43](https://cloud.githubusercontent.com/assets/22886679/19560846/58394344-96d6-11e6-9753-a664c498f079.png)


# Discussion History
## medusadigital | 2016-10-26T22:43:26+00:00
the whole feature is not completed yet, see https://github.com/monero-project/monero-core/issues/29

we should think about disabling the whole wizzard page, since smart mining is also not implemented.


## Jaqueeee | 2016-10-30T20:21:52+00:00
disabled this page in https://github.com/monero-project/monero-core/pull/93


## medusadigital | 2016-11-06T09:13:43+00:00
can be closed


## fluffypony | 2016-11-13T17:59:14+00:00
Closing as fixed


# Action History
- Created by: M5M400 | 2016-10-20T13:03:33+00:00
- Closed at: 2016-11-13T17:59:14+00:00
