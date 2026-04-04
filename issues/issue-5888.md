---
title: Separate wallet2 core wallet functionality from networking, persistence, and
  other application-specific dependencies
source_url: https://github.com/monero-project/monero/issues/5888
author: woodser
assignees: []
labels: []
created_at: '2019-09-06T19:42:34+00:00'
updated_at: '2021-03-25T14:42:59+00:00'
type: issue
status: closed
closed_at: '2021-03-25T14:42:59+00:00'
---

# Original Description
This issue documents the task of separating core wallet functionality in wallet2 from application-specific dependencies.  For example, wallet2 currently uses specific dependencies to request network data and persist wallet files to disk, but those dependencies cannot run in a web browser which must make network requests and persist data on behalf of the C++ runtime.  Similar limitations exist in bindings to/from other languages and environments.  In order to access Monero Core's wallet software in those environments, application-specific dependencies need to be separated from core wallet functionality.

This issue has been discussed in #monero-dev irc and has general support with the first step being a pure or "algebraic" refactor of wallet2's current state.

# Discussion History
# Action History
- Created by: woodser | 2019-09-06T19:42:34+00:00
- Closed at: 2021-03-25T14:42:59+00:00
