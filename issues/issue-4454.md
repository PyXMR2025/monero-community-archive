---
title: startup page
source_url: https://github.com/monero-project/monero-gui/issues/4454
author: melaxon
assignees: []
labels: []
created_at: '2025-06-05T17:27:28+00:00'
updated_at: '2025-06-26T16:14:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The start up page seems to be little bit strange on Linux Lite (see screenshot). Not sure is it a bug or a feature. Anyway on MAC OS it looks normal

![Image](https://github.com/user-attachments/assets/768ff54f-fe86-4bdd-ae75-fed56507c9c0)

 

# Discussion History
## selsta | 2025-06-26T16:14:53+00:00
It's likely a graphics driver issue. Can you start monero-wallet-gui with `QMLSCENE_DEVICE=softwarecontext` env var set and test if the issue still applies?

# Action History
- Created by: melaxon | 2025-06-05T17:27:28+00:00
