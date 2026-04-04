---
title: '[feature] Add "offline" option for "Node" tab.'
source_url: https://github.com/monero-project/monero-gui/issues/3226
author: jonathancross
assignees: []
labels: []
created_at: '2020-11-11T17:15:19+00:00'
updated_at: '2020-12-14T16:16:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently, users must specify one of 2 options "Local node" or "Remote node":

![xmr-node-screenshot](https://user-images.githubusercontent.com/5115470/98841978-2ceeeb80-2449-11eb-98c3-305166d64267.png)


Unfortunatly neither option is appropriate for an offline system used for air-gapped signing.

Users who are offline are currently prompted with various error messages and attempts to start the daemon.

Request:
1. Make an "Offline" option available with explanation that it will have not attempt to make network connections.
2. Prevent wallet from making network connections.
3. Bottom left should indicate that user is in "Offline" mode if explicitly selected.

Rough mockup:

![image](https://user-images.githubusercontent.com/5115470/102105064-3811ae80-3e2f-11eb-9a80-9da648a6561b.png)

Related: https://github.com/monero-project/monero/issues/7013

# Discussion History
# Action History
- Created by: jonathancross | 2020-11-11T17:15:19+00:00
