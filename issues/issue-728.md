---
title: '[Feature request] Seed for CLI wallets generated from keys / Error for MyMonero
  seed'
source_url: https://github.com/monero-project/monero-gui/issues/728
author: ghost
assignees: []
labels: []
created_at: '2017-05-13T22:38:23+00:00'
updated_at: '2017-05-30T19:50:04+00:00'
type: issue
status: closed
closed_at: '2017-05-30T19:50:04+00:00'
---

# Original Description
Unless I'm mistaken, the GUI shows a blank seed for wallets generated from keys. However, the CLI will display a seed for wallets generated from keys if the spend/view keys are from the CLI, but *not* from MyMonero. See this discussion: https://www.reddit.com/r/Monero/comments/6azzii/why_dont_wallets_restored_with_viewspend_keys/

So theoretically we could display a seed for wallets restored from keys if the keys are from the CLI.

Similarly, we should show an error specific to MyMonero. The seed box could show something like "Restored wallet version does not allow backup seeds. If you wish to have a backup seed then create a fresh wallet."

# Discussion History
# Action History
- Created by: ghost | 2017-05-13T22:38:23+00:00
- Closed at: 2017-05-30T19:50:04+00:00
