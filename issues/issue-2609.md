---
title: Passing -D ARCH=default with ./build.sh
source_url: https://github.com/monero-project/monero-gui/issues/2609
author: kpcyrd
assignees: []
labels: []
created_at: '2019-12-16T00:32:25+00:00'
updated_at: '2020-01-22T22:22:08+00:00'
type: issue
status: closed
closed_at: '2020-01-22T22:22:08+00:00'
---

# Original Description
We're currently shipping monero-gui in Arch Linux, which means the binary is built on a cpu that may be different from the cpu the binary is going to be executed on. To avoid AVX2 issues in monerod we pass `-D ARCH=default` to cmake.

cmake is called by `get_libwallet_api.sh` which is called by `build.sh`, which we use, but it seems there's no way to make `get_libwallet_api.sh` to pass `-D ARCH=default` without patching it. Being able to control this with a environment variable would be great. Advice also very welcome.

# Discussion History
## xiphon | 2019-12-16T10:31:11+00:00
Added `ARCH` environment variable support, would you like to test it? #2615 

# Action History
- Created by: kpcyrd | 2019-12-16T00:32:25+00:00
- Closed at: 2020-01-22T22:22:08+00:00
