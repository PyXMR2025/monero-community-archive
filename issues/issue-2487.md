---
title: 'Send page: description text doesn''t persist after colapsing it'
source_url: https://github.com/monero-project/monero-gui/issues/2487
author: rating89us
assignees: []
labels: []
created_at: '2019-11-25T01:34:18+00:00'
updated_at: '2019-12-05T06:34:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![23](https://user-images.githubusercontent.com/45968869/70209864-904ca580-1731-11ea-9e58-a78112fb301c.gif)

Related to #2488 

# Discussion History
## xiphon | 2019-11-25T05:07:36+00:00
This is intended. Collapsing description field implies removing description as well.

## rating89us | 2019-11-25T05:38:33+00:00
Sure, if the user collapses a description field containing a text, the description should not be used in this transaction.

However, if the user changes his mind and decides to use the description previously typed, the text should be there when the field is expanded again.

That is, colapsing the field should mean "don't use description" and not "don't use description  and clean description".

The intended function of collapsing description is to not add a description in the transaction. Nobody uses the "collapse function" in order to clean the description field.

# Action History
- Created by: rating89us | 2019-11-25T01:34:18+00:00
