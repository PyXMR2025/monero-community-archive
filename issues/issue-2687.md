---
title: 'Send page: import key images button isn''t always visible'
source_url: https://github.com/monero-project/monero-gui/issues/2687
author: rating89us
assignees: []
labels: []
created_at: '2019-12-26T18:31:33+00:00'
updated_at: '2020-02-06T02:39:41+00:00'
type: issue
status: closed
closed_at: '2020-02-06T02:39:41+00:00'
---

# Original Description
`Import key images` button should always be visible in `Send` page, otherwise users can't even know that this option exists.

Currently it is only visible when a view-only wallet is opened and the user is connected to a local node. 

When the monero-gui is not in these situations, the button should still be visible, but disabled.

This is being consistent with PR #2616:

>"A newbie observing Monero GUI wallet for the first time should learn that such a functionality exists and could be used in the future."

# Discussion History
# Action History
- Created by: rating89us | 2019-12-26T18:31:33+00:00
- Closed at: 2020-02-06T02:39:41+00:00
