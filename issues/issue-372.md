---
title: Build no longer bzip2 but still has bz2 extension.
source_url: https://github.com/monero-project/meta/issues/372
author: MicahZoltu
assignees: []
labels: []
created_at: '2019-07-18T07:51:25+00:00'
updated_at: '2020-03-09T21:41:42+00:00'
type: issue
status: closed
closed_at: '2020-03-09T21:41:42+00:00'
---

# Original Description
https://downloads.getmonero.org/linux64 redirects to https://dlsrc.getmonero.org/cli/monero-linux-x64-v0.14.1.0.tar.bz2.  However, the file at that location is _not_ a bzip2 file like the file extension suggests.  Instead, it is a gzipped file.  Trying to extract it with `tar --extract --bzip2 --file=monero-linux-x64-v0.14.1.0.tar.bz2` will fail with `tar` telling you that the file is not a bzip2 file.  Extracting with `--gzip` however will work.

# Discussion History
## dEBRUYNE-1 | 2019-07-18T08:36:41+00:00
This should be fixed in the upcoming v0.14.1.1 release. 

## erciccione | 2019-07-18T09:43:47+00:00
This is a duplicate of monero-project/monero#5730.

Also please see the [issue on GitLab](repo.getmonero.org/monero-project/monero-site/issues/964)

## jonathancross | 2019-07-18T21:39:09+00:00
Hi all, I submitted a PR to fix this issue: https://github.com/monero-project/monero/pull/5764 - reviews welcome. :-)

## jonathancross | 2019-09-04T14:49:24+00:00
Now that monero-project/monero#5764 is merged, the next release should be bzip2.

# Action History
- Created by: MicahZoltu | 2019-07-18T07:51:25+00:00
- Closed at: 2020-03-09T21:41:42+00:00
