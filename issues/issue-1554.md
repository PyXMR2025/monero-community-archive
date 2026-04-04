---
title: Automate monitoring of critical OpenSSL updates for static binary releases
source_url: https://github.com/monero-project/monero/issues/1554
author: anonimal
assignees: []
labels: []
created_at: '2017-01-10T05:01:34+00:00'
updated_at: '2017-01-24T01:38:21+00:00'
type: issue
status: closed
closed_at: '2017-01-24T01:38:21+00:00'
---

# Original Description
### This is cross-posted with https://github.com/monero-project/meta/issues/38
### I'm posting here because there are more eyes and maybe someone would like the opportunity to get involved
-------------------
For the static builds on the website: `monerod` uses libunbound which in turn uses OpenSSL statically. `kovri` uses cpp-netlib which in turn uses OpenSSL statically (now that the static builds are ready).

This is a problem for the website binaries in terms of keeping up with critical OpenSSL updates. We should somehow decide who takes care of what, and how, and preferably the process would be as automated as possible.

This idea was originally going to be only for kovri until just now when I noticed the capacity of monerod's libunbound usage.

-------------------

With that said, I think this responsibility would be best managed by a trusted regular developer. Ideas are welcome!

# Discussion History
## anonimal | 2017-01-24T01:38:21+00:00
See https://github.com/monero-project/meta/issues/38#issuecomment-274675158

# Action History
- Created by: anonimal | 2017-01-10T05:01:34+00:00
- Closed at: 2017-01-24T01:38:21+00:00
