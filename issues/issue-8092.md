---
title: release-v0.17 branch fails to build in gitian MacOS
source_url: https://github.com/monero-project/monero/issues/8092
author: hyc
assignees: []
labels: []
created_at: '2021-11-29T07:59:58+00:00'
updated_at: '2022-02-18T23:27:34+00:00'
type: issue
status: closed
closed_at: '2022-02-18T23:27:34+00:00'
---

# Original Description
PR #7691 is missing from the release branch, so cmake is ignoring the CXX_STANDARD settings, causing various targets like easylogging and qrcodegen to fail to compile. That feature was introduced in CMake 3.1, and the `cmake_minimum_required(2.8.7)` makes these CXX_STANDARD settings get ignored.

# Discussion History
# Action History
- Created by: hyc | 2021-11-29T07:59:58+00:00
- Closed at: 2022-02-18T23:27:34+00:00
