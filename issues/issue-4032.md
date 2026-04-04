---
title: Fee estimate not updating
source_url: https://github.com/monero-project/monero-gui/issues/4032
author: plowsof
assignees: []
labels: []
created_at: '2022-09-18T21:44:25+00:00'
updated_at: '2022-12-11T00:39:47+00:00'
type: issue
status: closed
closed_at: '2022-12-11T00:39:47+00:00'
---

# Original Description
Reported by reddit user Br0kenRabbitTV. On the pre-send screen, there is a fee estimate which does not update when you scroll through slow/fast/fastest. (it displays correctly on the confirmation screen) But they state this was not always the case... 

[fee-estimate.webm](https://user-images.githubusercontent.com/77655812/190929069-b5ad25e0-51fd-4d4d-9171-5083a85772ef.webm)

Is this true? should the value here update? did it ever update? or is this a feature request?

# Discussion History
## selsta | 2022-09-18T22:42:39+00:00
https://github.com/monero-project/monero/blob/master/src/wallet/api/wallet.cpp#L1767 does not take the priority into account.

## selsta | 2022-10-13T01:38:45+00:00
https://github.com/monero-project/monero/pull/8610

# Action History
- Created by: plowsof | 2022-09-18T21:44:25+00:00
- Closed at: 2022-12-11T00:39:47+00:00
