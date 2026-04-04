---
title: Openssl download in Dockerfile
source_url: https://github.com/monero-project/monero/issues/6437
author: normoes
assignees: []
labels: []
created_at: '2020-04-08T10:45:34+00:00'
updated_at: '2020-04-08T11:18:53+00:00'
type: issue
status: closed
closed_at: '2020-04-08T11:18:52+00:00'
---

# Original Description
The Dockerfile in the repository uses `openssl1.1.b` . This is downloaded from https://www.openssl.org/source/openssl-1.1.1b.tar.gz.

See here: https://github.com/monero-project/monero/blob/master/Dockerfile#L61

This URL is returning `404`, because the file was moved to https://www.openssl.org/source/old/1.1.1/openssl-1.1.1b.tar.gz

This causes the build (using the Dockerfile) to break.

~~I will provide a PR for that.~~

# Discussion History
## selsta | 2020-04-08T10:46:30+00:00
Note that there are already 2 PRs open to fix this :)

## normoes | 2020-04-08T10:48:54+00:00
Less work for me ;)

## erciccione | 2020-04-08T10:58:56+00:00
Linking to those PRs for reference: #6428 #6420

## normoes | 2020-04-08T11:18:52+00:00
Closing this.

# Action History
- Created by: normoes | 2020-04-08T10:45:34+00:00
- Closed at: 2020-04-08T11:18:52+00:00
