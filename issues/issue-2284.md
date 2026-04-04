---
title: Not able to connect to Trezor T when there is model One connected
source_url: https://github.com/monero-project/monero-gui/issues/2284
author: bosomt
assignees: []
labels:
- resolved
created_at: '2019-07-16T08:54:05+00:00'
updated_at: '2019-07-16T11:54:44+00:00'
type: issue
status: closed
closed_at: '2019-07-16T11:54:44+00:00'
---

# Original Description
Not able to connect to Trezor T when there is model One connected.
When T1 disconnected = works fine

![image](https://user-images.githubusercontent.com/31506317/61280279-e12a2480-a7b7-11e9-838f-f0fc254845e1.png)

2019-07-16 08:53:38.439	E Get public address exception: Trezor returned failure: code=1, message=Unknown message
2019-07-16 08:53:38.440	E Cannot get a device address


# Discussion History
## ph4r05 | 2019-07-16T11:51:43+00:00
@bosomt thanks for the report!

This should be fixed by PR https://github.com/monero-project/monero/pull/5476 which was merged to the monero-core in commit https://github.com/monero-project/monero/commit/08ab0cbddab9e8c7b0151ac235793602766e3a8e, on 2nd May 2019, but the current monero-gui uses the monero-core from the commit https://github.com/monero-project/monero/commit/581994b61c9b8b530629b2dbc2e7ddd3b30b12b4, 24th April 2019.

Once the monero-core version in the GUI is bumped to the current monero-core, this issue should be solved.

## selsta | 2019-07-16T11:52:49+00:00
+resolved

# Action History
- Created by: bosomt | 2019-07-16T08:54:05+00:00
- Closed at: 2019-07-16T11:54:44+00:00
