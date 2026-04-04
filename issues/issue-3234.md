---
title: instructions page -- macos src build needs libsodium brew install
source_url: https://github.com/monero-project/monero-gui/issues/3234
author: rednaxus
assignees: []
labels: []
created_at: '2020-11-13T19:52:09+00:00'
updated_at: '2021-01-21T03:43:05+00:00'
type: issue
status: closed
closed_at: '2021-01-21T03:43:05+00:00'
---

# Original Description
the instructions only have this as dependencies

brew install boost hidapi zmq libpgm miniupnpc ldns expat libunwind-headers protobuf libgcrypt

add libsodium



# Discussion History
## selsta | 2020-11-23T23:01:28+00:00
Is it required? We don’t use it for our Mac CI, though it could be preinstalled on CI.

https://github.com/monero-project/monero-gui/blob/master/.github/workflows/build.yml#L13

## rednaxus | 2020-11-23T23:58:52+00:00
I had to add it... and my machine is pretty developer beefed up and up to date with latest Catalina, so I don't think it is pre-installed

# Action History
- Created by: rednaxus | 2020-11-13T19:52:09+00:00
- Closed at: 2021-01-21T03:43:05+00:00
