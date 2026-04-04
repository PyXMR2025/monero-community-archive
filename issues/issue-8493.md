---
title: make_multisig returns unhelpful error message on bad input to multisig_info
source_url: https://github.com/monero-project/monero/issues/8493
author: woodser
assignees: []
labels: []
created_at: '2022-08-10T14:13:02+00:00'
updated_at: '2023-10-26T01:35:06+00:00'
type: issue
status: closed
closed_at: '2023-10-26T01:35:06+00:00'
---

# Original Description
Calling `make_multisig` with bad `multisig_info` (e.g. ["asd", "dsa"]) returns a strange error message: "basic_string".

This issue requests improving the error message.

# Discussion History
# Action History
- Created by: woodser | 2022-08-10T14:13:02+00:00
- Closed at: 2023-10-26T01:35:06+00:00
