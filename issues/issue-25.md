---
title: Transactions larger than 24.4 kb should be split
source_url: https://github.com/monero-project/monero/issues/25
author: monero-project
assignees: []
labels:
- enhancement
created_at: '2014-06-06T14:51:43+00:00'
updated_at: '2014-07-31T08:18:17+00:00'
type: issue
status: closed
closed_at: '2014-07-31T08:18:17+00:00'
---

# Original Description
The wallet currently does not allow you to perform transfers when the generated tx is larger than 24.4 kb.

A saner behaviour would be this:
For all tx > 10 kb, attempt instead split the inputs and outputs into multiple tx of a size <10 kb specified by the user (default <5 kb).


# Discussion History
## fluffypony | 2014-07-31T08:18:17+00:00
Completed


# Action History
- Created by: monero-project | 2014-06-06T14:51:43+00:00
- Closed at: 2014-07-31T08:18:17+00:00
