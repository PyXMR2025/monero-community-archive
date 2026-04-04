---
title: fix CMakeLists.txt to add -lpthread, did not compile boost 1.55
source_url: https://github.com/monero-project/monero/pull/1
author: vertoe
assignees: []
labels: []
created_at: '2014-05-05T18:00:46+00:00'
updated_at: '2014-09-02T00:05:14+00:00'
type: pull_request
status: merged
closed_at: '2014-05-06T00:14:41+00:00'
merged_at: '2014-05-06T00:14:41+00:00'
---

# Original Description
had a couple of compile errors and wasnt able to compile it until i added `LDFLAGS=-lpthread`


# Discussion History
# Action History
- Created by: vertoe | 2014-05-05T18:00:46+00:00
- Merged at: 2014-05-06T00:14:41+00:00
