---
title: simplewallet ctrl+c close failture
source_url: https://github.com/monero-project/monero/issues/31
author: monero-project
assignees: []
labels:
- bug
created_at: '2014-06-11T14:58:25+00:00'
updated_at: '2014-06-11T15:01:00+00:00'
type: issue
status: closed
closed_at: '2014-06-11T15:01:00+00:00'
---

# Original Description
Commit 2d755b3d0eef16a0cedc4801bd7fdde894dd649d (merge from fluffypony) prevents a daemon crash relating to console input, however it creates a hang in simplewallet when attempting to ctrl+c to send sigterm. This is being actively investigated.


# Discussion History
# Action History
- Created by: monero-project | 2014-06-11T14:58:25+00:00
- Closed at: 2014-06-11T15:01:00+00:00
