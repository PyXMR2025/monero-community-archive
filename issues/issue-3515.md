---
title: scripts/build.openssl3.sh points to wrong URL
source_url: https://github.com/xmrig/xmrig/issues/3515
author: jfikar
assignees: []
labels:
- bug
created_at: '2024-07-24T12:53:28+00:00'
updated_at: '2025-06-16T19:39:21+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:39:21+00:00'
---

# Original Description
Hi,
when trying to build the libraries by `scripts/build_deps.sh` it fails fetching the OpenSSL library. I think the openssl.org no more hosts the source files. The URL in `scripts/build.openssl3.sh` should be changed to `https://github.com/openssl/openssl/releases/download/openssl-${OPENSSL_VERSION}/openssl-${OPENSSL_VERSION}.tar.gz`

Also note there is a new version 3.0.14.

Maybe it is just a temporary breakdown of the openssl.org?


# Discussion History
## xmrig | 2024-07-24T14:05:19+00:00
It looks like it is permanent, they have a brand new website, logo, and even domain for the library itself.
Thank you.

# Action History
- Created by: jfikar | 2024-07-24T12:53:28+00:00
- Closed at: 2025-06-16T19:39:21+00:00
