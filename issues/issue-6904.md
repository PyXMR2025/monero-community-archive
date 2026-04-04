---
title: ' Unknown CMake command "monero_crypto_autodetect".'
source_url: https://github.com/monero-project/monero/issues/6904
author: ghdqh1515
assignees: []
labels: []
created_at: '2020-10-18T03:29:49+00:00'
updated_at: '2021-08-15T02:46:14+00:00'
type: issue
status: closed
closed_at: '2021-08-15T02:46:14+00:00'
---

# Original Description
$make
Error after execution
Can't build due to error
 Unknown CMake command "monero_crypto_autodetect".




# Discussion History
## moneromooo-monero | 2020-10-18T15:50:52+00:00
What platform ? What cmake version ? In what directory are you running make ? Any other error before that ?

## mikegeoffrey | 2020-10-19T09:20:47+00:00
All the external subdirs are empty in the v0.17.1.1 tar.gz release, so the monero_crypto_autodetect can't be found as it's in function.cmake file in the supercop subdir. Same for a lot of the other dirs, just empty.

## selsta | 2020-10-19T09:35:12+00:00
Github auto generates the source tarball without submodules. This is out of our control. Please use git to clone recursively.

# Action History
- Created by: ghdqh1515 | 2020-10-18T03:29:49+00:00
- Closed at: 2021-08-15T02:46:14+00:00
