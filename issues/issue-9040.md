---
title: Protobuf Now Mandatory
source_url: https://github.com/monero-project/monero/issues/9040
author: vtnerd
assignees: []
labels:
- discussion
created_at: '2023-10-27T00:25:21+00:00'
updated_at: '2025-12-28T23:37:54+00:00'
type: issue
status: closed
closed_at: '2025-12-28T23:37:54+00:00'
---

# Original Description
Protobuf is listed as an optional dependency, but is now required by default after recent changes for Trezor. Either the README needs updating, or a fix for the dependency needs to be found.

# Discussion History
## selsta | 2023-10-27T00:26:45+00:00
Trezor is still optional so the CMake has to be fixed, will take a look at it.

## vtnerd | 2023-10-27T00:27:31+00:00
I think its just that it defaults to on (looking at a fix myself).

## vtnerd | 2023-10-27T00:30:39+00:00
@selsta got owned by the CMakeCache again.

[This variable](https://github.com/monero-project/monero/blob/master/cmake/CheckTrezor.cmake#L9) defaults to compile Trezor in, which then triggers a requirement for Protobuf. Whereas previously, no explicit opt-out was required.

It seems like this could be flipped to default off, requiring users to opt-in, but we may need to tag the Trezor/Protobuf team on this.

## selsta | 2023-10-27T00:33:12+00:00
I think the behaviour should be changed so that if protobuf isn't installed it should print a warning that Trezor compilation is skipped, not fail. Only if USE_DEVICE_TREZOR_MANDATORY is enabled it should fail.

Keeping USE_DEVICE_TREZOR on by default should be fine as long as it doesn't cause the compilation to fail.

## selsta | 2025-12-28T23:37:48+00:00
As far as I remember, this was fixed.

# Action History
- Created by: vtnerd | 2023-10-27T00:25:21+00:00
- Closed at: 2025-12-28T23:37:54+00:00
