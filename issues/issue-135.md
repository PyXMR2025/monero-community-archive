---
title: simplewallet starts refresh at wrong block
source_url: https://github.com/monero-project/monero/issues/135
author: iamsmooth
assignees: []
labels: []
created_at: '2014-09-13T03:15:31+00:00'
updated_at: '2016-01-25T17:54:38+00:00'
type: issue
status: closed
closed_at: '2016-01-25T17:54:38+00:00'
---

# Original Description
Upon refresh there is a message in simplewallet.log that the first block received is already known. Likely off-by-one error.

2014-Sep-12 23:02:45.767691 Starting refresh...
**2014-Sep-12 23:02:45.810703 Block is already in blockchain: 4c0917d3f62781d39ab67e0f21c1397a4f706424c206ec3bea96b44a4bf5ea81**
2014-Sep-12 23:02:45.812681 Processed block: <f7eca35848ba7203b6cd08481bdec4eead26daf24b49cef50c4b57c5114479d3>, height 215209, 2(2/0)ms
2014-Sep-12 23:02:45.913911 Processed block: <99eb11332ccf81d6e4bb01b135b62327e0d9c9e150af6a08e6ecb073abc22aed>, height 215210, 71(1/70)ms


# Discussion History
## fluffypony | 2016-01-25T17:54:38+00:00
Appears to be resolved


# Action History
- Created by: iamsmooth | 2014-09-13T03:15:31+00:00
- Closed at: 2016-01-25T17:54:38+00:00
