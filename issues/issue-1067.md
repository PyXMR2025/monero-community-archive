---
title: CentOS 7 instructions update
source_url: https://github.com/xmrig/xmrig/issues/1067
author: marcel-st
assignees: []
labels:
- review later
created_at: '2019-07-22T08:57:09+00:00'
updated_at: '2020-02-09T10:39:15+00:00'
type: issue
status: closed
closed_at: '2020-02-09T10:39:15+00:00'
---

# Original Description
Hi there,

there is a package missing in the CentOS7 instructions. The second "sudo yum install" should also include the openssl-devel package.

# Discussion History
## paulpas | 2019-07-26T14:37:02+00:00
It also needs to include the command to enable the SCL environment 

scl enable devtoolset-4 bash

## marcel-st | 2019-07-26T14:52:04+00:00
@paulpas i didn't use that command and had no issues in compilation or running xmrig.

# Action History
- Created by: marcel-st | 2019-07-22T08:57:09+00:00
- Closed at: 2020-02-09T10:39:15+00:00
