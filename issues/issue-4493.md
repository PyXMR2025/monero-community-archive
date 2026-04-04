---
title: 'Build failed on windows : error dereferencing pointer to incomplete type ''EVP_MD_CTX'''
source_url: https://github.com/monero-project/monero/issues/4493
author: RomyWeb
assignees: []
labels: []
created_at: '2018-10-03T07:43:14+00:00'
updated_at: '2018-10-03T09:21:54+00:00'
type: issue
status: closed
closed_at: '2018-10-03T09:21:54+00:00'
---

# Original Description
Hi, can't build master or release-v0.12 on windows 64.
openssl 1.1

![errormonero](https://user-images.githubusercontent.com/16287732/46396490-d7837480-c6ef-11e8-9a0b-d14c1c325f2b.PNG)

Thank you

# Discussion History
## iDunk5400 | 2018-10-03T08:33:24+00:00
`git pull`
`git submodule update`

However..., you may need to pull #4471 first. I don't think that's in release-v0.12 branch.

## RomyWeb | 2018-10-03T09:21:37+00:00
Thank you !

# Action History
- Created by: RomyWeb | 2018-10-03T07:43:14+00:00
- Closed at: 2018-10-03T09:21:54+00:00
