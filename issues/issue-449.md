---
title: '`wallet2::get_transfers()` should obsolete `include_all` overload'
source_url: https://github.com/seraphis-migration/monero/issues/449
author: jeffro256
assignees: []
labels: []
created_at: '2026-07-29T06:30:22+00:00'
updated_at: '2026-08-05T05:36:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
AFAICT the `include_all=true` overload of `wallet2::get_transfers()` isn't used anywhere, except in the helper static function `::get_transfers()`, implicitly. However, all the uses of this helper function don't require `include_all=true`. I propose removing the `include_all` parameter and have the behavior default to the current `include_all=false` behavior. It would reduce the diff against master. 

# Discussion History
## j-berman | 2026-08-05T02:11:04+00:00
Sgtm. It can easily be brought back if some caller wants to see the 0 amount enotes in their wallet in the future

## jeffro256 | 2026-08-05T05:36:04+00:00
Okay, I will probably add this to https://github.com/monero-project/monero/pull/10995

# Action History
- Created by: jeffro256 | 2026-07-29T06:30:22+00:00
