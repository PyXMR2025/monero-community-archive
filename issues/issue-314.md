---
title: compile error libunbound "multiple definition of SHA512"
source_url: https://github.com/monero-project/monero/issues/314
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-06-08T04:49:02+00:00'
updated_at: '2015-06-11T03:13:32+00:00'
type: issue
status: closed
closed_at: '2015-06-11T03:12:59+00:00'
---

# Original Description
so I set up a new virtual machine, and compiled with make release-static to avoid the berkelyDB. got this

http://imgur.com/4v56aCC

sorry for the image link. Was having a real pain trying to copy from the VM.


# Discussion History
## Gingeropolous | 2015-06-11T03:13:31+00:00
turns out it was because i didn't use the new make command make static-release-64. ( facepalm )


# Action History
- Created by: Gingeropolous | 2015-06-08T04:49:02+00:00
- Closed at: 2015-06-11T03:12:59+00:00
