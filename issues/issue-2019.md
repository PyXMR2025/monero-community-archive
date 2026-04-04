---
title: set min-output-count 10 & set min-output-value 30 unrecognized command
source_url: https://github.com/monero-project/monero/issues/2019
author: ocminer
assignees: []
labels: []
created_at: '2017-05-08T23:20:10+00:00'
updated_at: '2017-08-07T17:42:16+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:42:16+00:00'
---

# Original Description
while using wallet-cli and trying to set those options I get:

[wallet XXXXXX]: set min-output-value 30
Error: set: unrecognized argument(s)

And it doesn't seem to be possible to set those values to the wallet-rpc as well

# Discussion History
## iDunk5400 | 2017-05-09T00:12:52+00:00
Try `set min-outputs-value 30`.

## stoffu | 2017-05-09T03:08:40+00:00
Typo fixed in #2021 

## ocminer | 2017-05-09T06:37:41+00:00
Thanks, output**s** works fine !

## moneromooo-monero | 2017-08-07T17:40:13+00:00
+resolved

# Action History
- Created by: ocminer | 2017-05-08T23:20:10+00:00
- Closed at: 2017-08-07T17:42:16+00:00
