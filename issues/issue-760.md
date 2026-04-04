---
title: 'PR #756: handle bad / incorrect JSON types'
source_url: https://github.com/monero-project/monero/issues/760
author: fluffypony
assignees: []
labels:
- bug
created_at: '2016-03-25T06:27:07+00:00'
updated_at: '2016-04-02T03:03:09+00:00'
type: issue
status: closed
closed_at: '2016-04-02T03:03:09+00:00'
---

# Original Description
Per https://github.com/monero-project/bitmonero/pull/756#issuecomment-201109722 and the comment thereafter

> "Note that, RapidJSON does not automatically convert values between JSON types. If a value is a string, it is invalid to call GetInt(), for example. In debug mode it will fail an assertion. In release mode, the behavior is undefined."

Since this is unbound user input we need to sanitise and check before acting on any particular input.


# Discussion History
## moneromooo-monero | 2016-03-27T21:14:09+00:00
https://github.com/monero-project/bitmonero/pull/769


## fluffypony | 2016-04-02T03:03:09+00:00
Closed via #769


# Action History
- Created by: fluffypony | 2016-03-25T06:27:07+00:00
- Closed at: 2016-04-02T03:03:09+00:00
