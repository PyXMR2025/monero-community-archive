---
title: 'OSS-Fuzz Failing to Build Since 09/23/2024  '
source_url: https://github.com/monero-project/monero/issues/9699
author: ACK-J
assignees: []
labels: []
created_at: '2025-01-13T21:24:33+00:00'
updated_at: '2025-01-16T04:28:33+00:00'
type: issue
status: closed
closed_at: '2025-01-16T04:28:33+00:00'
---

# Original Description
According to the following site tracking Google's OSS-Fuzz project, monero has not been fuzzed since September 2024 due to the build process failing. 
https://introspector.oss-fuzz.com/project-profile?project=monero

Here is the build log with the errors
https://oss-fuzz-build-logs.storage.googleapis.com/log-d9f01732-2381-4a86-9cb7-0de8daef137b.txt

This appears to be due to the following link returning a 404
https://boostorg.jfrog.io/artifactory/main/release/1.84.0/source/boost_1_84_0.tar.gz

# Discussion History
## ACK-J | 2025-01-13T21:25:37+00:00
Maybe merging the PR associated with this issue would help as well
https://github.com/monero-project/monero/issues/7230

## selsta | 2025-01-14T12:00:33+00:00
https://github.com/google/oss-fuzz/commit/70c202e3b77261154382101e045fb13955334ffe should fix it, but I can't submit the PR due to lack of Google account required to sign the CLA.

## selsta | 2025-01-16T04:28:33+00:00
Resolved in https://github.com/google/oss-fuzz/pull/12936

# Action History
- Created by: ACK-J | 2025-01-13T21:24:33+00:00
- Closed at: 2025-01-16T04:28:33+00:00
