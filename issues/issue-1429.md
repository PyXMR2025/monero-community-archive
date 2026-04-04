---
title: No hash or PGP signiture available for the source tar ball on Release section
source_url: https://github.com/monero-project/monero/issues/1429
author: good-guy-greg
assignees: []
labels:
- invalid
created_at: '2016-12-10T21:51:48+00:00'
updated_at: '2017-09-07T12:24:25+00:00'
type: issue
status: closed
closed_at: '2017-09-07T12:24:25+00:00'
---

# Original Description
On the [release section](https://github.com/monero-project/monero/releases), there aren't any checksum hashes available for v0.10.0.zip and v0.10.0.tar.gz source files. Please add them, and even better, add a PGP signed file. 

# Discussion History
## ghost | 2016-12-13T21:53:35+00:00
@fluffypony is this still an issue with 0.10.1?

## moneromooo-monero | 2017-01-15T12:30:50+00:00
Looks like it.
If you want the source though, it's best to get it from github, then you can check all signatures.
For other files, there's a GPG signed file at https://getmonero.org/downloads/hashes.txt

## moneromooo-monero | 2017-08-12T20:10:36+00:00
Still the case for 0.10.3.1, for the record.

## moneromooo-monero | 2017-09-07T12:20:42+00:00
The source tarball is apparently an automatic github thing, and so having a signature on it would not be too useful, since it'd be signing a tarball made by a third party. So I guess I'll close this. Use git if you want the source, checkout the release tag, and check signatures there.

+invalid

# Action History
- Created by: good-guy-greg | 2016-12-10T21:51:48+00:00
- Closed at: 2017-09-07T12:24:25+00:00
