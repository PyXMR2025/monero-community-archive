---
title: DNSSEC DS record out of date in dns_utils.cpp
source_url: https://github.com/monero-project/monero/issues/8474
author: OrvilleRed
assignees: []
labels: []
created_at: '2022-07-30T07:26:04+00:00'
updated_at: '2022-08-23T03:50:29+00:00'
type: issue
status: closed
closed_at: '2022-08-23T03:50:29+00:00'
---

# Original Description
I believe the DS on the first line here is outdated (since 2019):

https://github.com/monero-project/monero/blob/b6a029f222abada36c7bc6c65899a4ac969d7dee/src/common/dns_utils.cpp#L105-L106

You can confirm this by using [get_trust_anchor.py](https://raw.githubusercontent.com/iana-org/get-trust-anchor/master/get_trust_anchor.py) or looking at [root-anchors.xml](https://data.iana.org/root-anchors/root-anchors.xml)

_Originally posted by @sanderfoobar in https://github.com/monero-project/monero/issues/8452#issuecomment-1196066179_

# Discussion History
## OrvilleRed | 2022-07-30T07:26:57+00:00
I can confirm @sanderfoobar 's observation. Seems like this should be tracked separately.

# Action History
- Created by: OrvilleRed | 2022-07-30T07:26:04+00:00
- Closed at: 2022-08-23T03:50:29+00:00
