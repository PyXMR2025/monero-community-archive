---
title: 'simplewallet: When rpc-bind-port is specified, password-file does not work'
source_url: https://github.com/monero-project/monero/issues/722
author: Aerbax
assignees: []
labels: []
created_at: '2016-03-14T01:31:54+00:00'
updated_at: '2016-03-20T18:58:22+00:00'
type: issue
status: closed
closed_at: '2016-03-20T18:58:22+00:00'
---

# Original Description
When making simplewallet non-interactive via the rpc-bind-ip and rpc-bind-port, --password-file will not read the appropriate file.  However, --password does - but that exposes the password in plain text when the process tree is inspected.

Just specifying rpc-bind-ip is fine...the password file is read appropriately.  When rpc-bind-port is added, the password-file is not read and simplewallet gives the error: "ERROR /DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:2561 Wallet password not set."

I am running "Monero 'Hydrogen Helix' (v0.9.1.0-release)" on x64 on Debian.  The binaries are those on the getmonero website.


# Discussion History
## jwinterm | 2016-03-14T01:43:50+00:00
Confirmed same behavior on Windows 10 using same release here.


## moneromooo-monero | 2016-03-19T22:23:45+00:00
https://github.com/monero-project/bitmonero/pull/734


# Action History
- Created by: Aerbax | 2016-03-14T01:31:54+00:00
- Closed at: 2016-03-20T18:58:22+00:00
