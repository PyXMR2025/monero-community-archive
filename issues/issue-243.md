---
title: Client DoS due to large DH parameter (CVE-2018-0732)
source_url: https://github.com/monero-project/meta/issues/243
author: anonimal
assignees: []
labels: []
created_at: '2018-06-12T21:16:22+00:00'
updated_at: '2018-10-16T21:24:43+00:00'
type: issue
status: closed
closed_at: '2018-10-16T21:24:24+00:00'
---

# Original Description
Regarding our usage of libunbound, this is a very narrow attack vector unless there are some naughty DNS servers. This affects our static release builds.

https://www.openssl.org/news/secadv/20180612.txt

>Due to the low severity of this issue we are not issuing a new release of
OpenSSL 1.1.0 or 1.0.2 at this time. The fix will be included in OpenSSL 1.1.0i
and OpenSSL 1.0.2p when they become available. The fix is also available in
commit ea7abeeab (for 1.1.0) and commit 3984ef0b7 (for 1.0.2) in the OpenSSL git
repository.

Neither 1.1.0i or 1.0.2p are available yet, but 1.1.1 should be available soon [tm].

This issue should be resolved along with https://github.com/monero-project/meta/issues/208.

# Discussion History
## anonimal | 2018-09-08T23:25:19+00:00
[1.1.0i was released August 14th](https://www.openssl.org/news/openssl-1.1.0-notes.html). The static release binaries should be built against the latest version of openssl.

## anonimal | 2018-10-16T21:24:24+00:00
Should be resolved in the v0.13 series.

# Action History
- Created by: anonimal | 2018-06-12T21:16:22+00:00
- Closed at: 2018-10-16T21:24:24+00:00
