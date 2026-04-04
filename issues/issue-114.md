---
title: Floating point is used to represent values
source_url: https://github.com/monero-project/monero-gui/issues/114
author: moneromooo-monero
assignees: []
labels: []
created_at: '2016-11-05T22:51:03+00:00'
updated_at: '2016-11-13T17:58:36+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:58:36+00:00'
---

# Original Description
Try sending 0.0000000015 monero. The GUI thinks it's zero.
Large integers need to be used internally, and store atomic units.

# Discussion History
## moneromooo-monero | 2016-11-06T12:35:44+00:00
https://github.com/monero-project/monero-core/pull/118

Filtering still uses floating point, not sure how much of a liability this is


## fluffypony | 2016-11-13T17:58:36+00:00
Closing as fixed


# Action History
- Created by: moneromooo-monero | 2016-11-05T22:51:03+00:00
- Closed at: 2016-11-13T17:58:36+00:00
