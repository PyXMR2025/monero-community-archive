---
title: Proving reserve at a past block
source_url: https://github.com/monero-project/monero/issues/5603
author: moneromooo-monero
assignees: []
labels: []
created_at: '2019-06-02T19:29:18+00:00'
updated_at: '2019-06-02T19:33:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Reserve proof checks spentness as of the check. This prevents proving balance at a particular date (eg, at a tax boundary date). There is no easy way to get from a key image to a spent height currently, it'd need a db update.

# Discussion History
# Action History
- Created by: moneromooo-monero | 2019-06-02T19:29:18+00:00
