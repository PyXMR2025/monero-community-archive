---
title: '[Request/Question] import_multisig_info shouldn''t flush the previous import
  of M/N info?'
source_url: https://github.com/monero-project/monero/issues/4846
author: anonimal
assignees: []
labels: []
created_at: '2018-11-13T17:04:27+00:00'
updated_at: '2018-11-13T17:09:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If wallet A imports `export_multisig_info` from wallet B and C by using `import_multisig_info` more than once, and not on the same line like `import_multisig_info B C`, then B will be flushed and only C will be kept.

After some collaboration with @moneromooo-monero, this issue has been opened at the request of @moneromooo-monero.

# Discussion History
# Action History
- Created by: anonimal | 2018-11-13T17:04:27+00:00
