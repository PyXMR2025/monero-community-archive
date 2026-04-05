---
title: How to use "max-cpu-usage" without thread pinning for RandomX in the embedded
  config ?
source_url: https://github.com/xmrig/xmrig/issues/1869
author: ghost
assignees: []
labels: []
created_at: '2020-10-06T10:03:25+00:00'
updated_at: '2020-10-06T20:03:11+00:00'
type: issue
status: closed
closed_at: '2020-10-06T20:03:11+00:00'
---

# Original Description
I use "max-cpu-usage" in the embedded config but would like to avoid problem with newer Windows scheduler and make sure threads are unpinned like in manual setting: "rx": [-1,-1, ...],

How to do this in the embedded config while using "max-cpu-usage" setting ?

Thank you in advance!

# Discussion History
# Action History
- Created by: ghost | 2020-10-06T10:03:25+00:00
- Closed at: 2020-10-06T20:03:11+00:00
