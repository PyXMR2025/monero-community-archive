---
title: Relocate monerod registries from [HKCU\SOFTWARE\monero-project\monero-core]
  to [HKLM\SOFTWARE\monero-project\monero] or monero.conf
source_url: https://github.com/monero-project/monero/issues/7083
author: mattmill30
assignees: []
labels: []
created_at: '2020-12-05T19:06:14+00:00'
updated_at: '2021-01-09T01:38:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In order to support multi-user workstations, monerod should be installed as a service and offer an API for configuring settings, which are either held in HKLM (rather than HKCU) or in a monero/bitmonero config file.

# Discussion History
## moneromooo-monero | 2021-01-09T01:38:41+00:00
That seems to be related to the GUI. Please file to the GUI repo: https://github.com/monero-project/monero-core

# Action History
- Created by: mattmill30 | 2020-12-05T19:06:14+00:00
