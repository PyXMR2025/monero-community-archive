---
title: bug with output 18446744.073285602033 XMR
source_url: https://github.com/monero-project/monero-gui/issues/4694
author: DedovKonstantin
assignees: []
labels: []
created_at: '2026-09-04T12:30:38+00:00'
updated_at: '2026-09-07T17:26:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
<img width="1365" height="725" alt="Image" src="https://github.com/user-attachments/assets/2fdcf2c9-1d88-4e31-827b-3084a5b68a25" />

This is wallet from book "Mastering Monero". I see 2 outputs with 18M XMR. What is it?

SEED:
lamb hexagon aces acquire twang bluntly argue when unafraid awning academy nail threaten sailor palace selfish cadets click sickness juggled border thumbs remedy ridges border

DATE:
2026.08.06

# Discussion History
## selsta | 2026-09-04T13:57:17+00:00
Try restoring it from restore height 1.

## DedovKonstantin | 2026-09-04T14:15:37+00:00
> Try restoring it from restore height 1.

This is that (from height 0).

## selsta | 2026-09-07T17:25:54+00:00
One or multiple outputs were missed during wallet scan. This can either be due to wrong restore height, an issue with the subaddres lookahead, or a node issue.

# Action History
- Created by: DedovKonstantin | 2026-09-04T12:30:38+00:00
