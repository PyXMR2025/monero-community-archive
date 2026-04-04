---
title: Fee using 12 decimal places
source_url: https://github.com/monero-project/monero/issues/1835
author: luigi1111
assignees: []
labels: []
created_at: '2017-03-03T22:33:05+00:00'
updated_at: '2017-03-31T17:11:36+00:00'
type: issue
status: closed
closed_at: '2017-03-31T17:11:36+00:00'
---

# Original Description
Calculating fee to 12 decimal places is needlessly specific, and will likely get in the way in the future if we move to different size range proof that doesn't cover the entire field. This is because the specificity of the fee is leaving change outputs for the difference. I recommend rounding up to nearest digit at either the 6th or 8th (a la Bitcoin) decimal place.

Conversely, outputs that presently have digits smaller than 10^-6 (or 8), likely due to the above, might want to drop those digits to the fee instead, but that can be left as a future change.

# Discussion History
## iamsmooth | 2017-03-26T23:53:21+00:00
This can be closed now? Not sure the PR or commit but I believe this is implemented in the new release?


## luigi1111 | 2017-03-31T17:11:35+00:00
Yes.

# Action History
- Created by: luigi1111 | 2017-03-03T22:33:05+00:00
- Closed at: 2017-03-31T17:11:36+00:00
