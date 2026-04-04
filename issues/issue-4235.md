---
title: No update when latest version is 0.18.3.1?
source_url: https://github.com/monero-project/monero-gui/issues/4235
author: ghost
assignees: []
labels: []
created_at: '2023-10-26T07:10:21+00:00'
updated_at: '2023-10-26T09:53:56+00:00'
type: issue
status: closed
closed_at: '2023-10-26T09:53:24+00:00'
---

# Original Description
![image](https://github.com/monero-project/monero-gui/assets/148219987/7ec71cbc-0fcd-41d8-808b-23d563fa2038)

I also just realized the time displayed is different than my time, is this intentional?

# Discussion History
## selsta | 2023-10-26T09:53:24+00:00
We will activate the auto updater soon. For security reasons activating the auto updater requires multiple people from the core team, so it's sometimes a bit delayed. We also make sure that there are no new major bug reports.

> I also just realized the time displayed is different than my time, is this intentional?

Yes, so that it doesn't leak your timezone. It prints it at UTC+0.

# Action History
- Created by: ghost | 2023-10-26T07:10:21+00:00
- Closed at: 2023-10-26T09:53:24+00:00
