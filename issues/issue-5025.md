---
title: Fuzz Tests fail to compile 2
source_url: https://github.com/monero-project/monero/issues/5025
author: dachen0
assignees: []
labels: []
created_at: '2018-12-29T02:04:54+00:00'
updated_at: '2018-12-29T02:15:43+00:00'
type: issue
status: closed
closed_at: '2018-12-29T02:15:31+00:00'
---

# Original Description
tests/fuzz/cold-outputs.cpp:85:53: error: no matching function for call to ‘tools::wallet2::import_outputs(std::vector<tools::wallet2::transfer_details>&)’
     size_t n_outputs = wallet.import_outputs(outputs);
Well, this is bad.
     size_t n_outputs = wallet.import_outputs(outputs);
                                                     ^


# Discussion History
## dachen0 | 2018-12-29T02:15:43+00:00
I broke it trying to unbreak another issue.

# Action History
- Created by: dachen0 | 2018-12-29T02:04:54+00:00
- Closed at: 2018-12-29T02:15:31+00:00
