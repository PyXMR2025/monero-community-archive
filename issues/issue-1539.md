---
title: integrated address doesnt work with cold signing
source_url: https://github.com/monero-project/monero/issues/1539
author: Jaqueeee
assignees: []
labels: []
created_at: '2017-01-08T20:11:09+00:00'
updated_at: '2017-01-13T19:34:36+00:00'
type: issue
status: closed
closed_at: '2017-01-13T19:34:36+00:00'
---

# Original Description
When using cold signing functions (`save_transfer, sign_transfer, submit_transfer`) the short payment id is first encrypted in view only wallet and then again in cold wallet but with different tx key. The recipient will therefore get wrong payment id. 

# Discussion History
# Action History
- Created by: Jaqueeee | 2017-01-08T20:11:09+00:00
- Closed at: 2017-01-13T19:34:36+00:00
