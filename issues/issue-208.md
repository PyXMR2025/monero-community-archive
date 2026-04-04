---
title: Cache timing vulnerability in RSA Key Generation (CVE-2018-0737)
source_url: https://github.com/monero-project/meta/issues/208
author: anonimal
assignees: []
labels: []
created_at: '2018-04-17T08:02:10+00:00'
updated_at: '2018-10-16T21:24:34+00:00'
type: issue
status: closed
closed_at: '2018-10-16T21:24:34+00:00'
---

# Original Description
This is for our static release builds, regarding our usage of libunbound (RSA/SHA1 [required](https://tools.ietf.org/html/rfc6944) for DNSSEC). RSA also needed for epee(?), and more(?) (? = can @moneromooo-monero or @hyc or others confirm?):

https://www.openssl.org/news/secadv/20180416.txt

>Due to the low severity of this issue we are not issuing a new release of
OpenSSL 1.1.0 or 1.0.2 at this time. The fix will be included in OpenSSL 1.1.0i
and OpenSSL 1.0.2p when they become available.

If the next point release is not *before* they release 1.1.0i / 1.0.2p, then we should release a monero point release with those applicable versions once they are released.

# Discussion History
## hyc | 2018-04-17T09:04:02+00:00
Only libunbound had any particular OpenSSL requirement.

## fluffypony | 2018-04-17T09:12:35+00:00
Yes - only needed for libunbound

## anonimal | 2018-09-08T23:25:40+00:00
[1.1.0i was released August 14th](https://www.openssl.org/news/openssl-1.1.0-notes.html). The static release binaries should be built against the latest version of openssl.

## anonimal | 2018-10-16T21:24:34+00:00
Should be resolved in the v0.13 series.

# Action History
- Created by: anonimal | 2018-04-17T08:02:10+00:00
- Closed at: 2018-10-16T21:24:34+00:00
