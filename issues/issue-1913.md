---
title: 'Feature request: set fee per transaction in the transfer command'
source_url: https://github.com/monero-project/monero/issues/1913
author: assylias
assignees: []
labels: []
created_at: '2017-03-23T14:29:07+00:00'
updated_at: '2017-04-10T22:19:44+00:00'
type: issue
status: closed
closed_at: '2017-04-10T22:19:44+00:00'
---

# Original Description
At the moment, to set the fee of a specific transaction, one needs to alter a global setting.

It would probably be more intuitive and user-friendly to allow users to set the fee per transaction in the transfer command.

So instead of current spec of:

    transfer [<mixin_count>] <address> <amount> [<payment_id>] <address_2> <amount_2>

It could become:

    transfer [<fee>] [<mixin_count>] <address> <amount> [<payment_id>] <address_2> <amount_2>

That should not create any collisions with the other parameters if fee is one of `default/unimportant/normal/elevated/priority`.

The new command would read, in the most common situation:

    transfer elevated XXXXXXX_address_XXXXXXXX 1

# Discussion History
# Action History
- Created by: assylias | 2017-03-23T14:29:07+00:00
- Closed at: 2017-04-10T22:19:44+00:00
