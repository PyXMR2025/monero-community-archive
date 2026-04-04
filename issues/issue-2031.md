---
title: GUI freezes loading large transaction history
source_url: https://github.com/monero-project/monero-gui/issues/2031
author: woodser
assignees: []
labels: []
created_at: '2019-03-25T12:34:45+00:00'
updated_at: '2019-07-04T12:53:46+00:00'
type: issue
status: closed
closed_at: '2019-07-04T12:53:46+00:00'
---

# Original Description
Steps to reproduce:

1. Open a wallet with a large transaction history.  Here is a stagenet seed with such a history: `nagged giddy virtual bias spying arsenic fowls hexagon oars frying lava dialect copy gasp utensils muffin tattoo ritual exotic inmate kisses either sprig sunken sprig`
2. Click the History tab in the wallet.
3. The GUI freezes.

# Discussion History
## selsta | 2019-03-25T12:38:26+00:00
Thanks for reporting, this is a known issue. #2025 should improve this.

## dEBRUYNE-1 | 2019-07-03T17:30:19+00:00
As far as I know, this is resolved with the `History` page redesign (which is included in GUI v0.14.1.0). 

Thus, can you perhaps give it another shot with GUI v0.14.1.0? 

## woodser | 2019-07-04T12:53:46+00:00
This issue is resolved in GUI v0.14.1.0.  Thanks.

# Action History
- Created by: woodser | 2019-03-25T12:34:45+00:00
- Closed at: 2019-07-04T12:53:46+00:00
