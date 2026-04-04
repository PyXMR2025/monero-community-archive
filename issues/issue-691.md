---
title: simplewallet --generate-new-wallet bug
source_url: https://github.com/monero-project/monero/issues/691
author: fluffypony
assignees: []
labels:
- bug
created_at: '2016-02-29T22:28:00+00:00'
updated_at: '2016-08-26T08:32:38+00:00'
type: issue
status: closed
closed_at: '2016-08-26T08:32:38+00:00'
---

# Original Description
Per @petertodd:

> `simplewallet --generate-new-wallet` doesn't save to `<address>.wallet` like the help text says it does


# Discussion History
## bigreddmachine | 2016-03-02T19:42:25+00:00
`simplewallet --generate-new-wallet`
returns the error message
`Failed to parse arguments: the required argument for option '--generate-new-wallet' is missing`

For clarity's sake, is the bug that the help is wrong or that the default behavior is not working?

i.e. Should
`simeplewallet --generate-new-wallet`
be just as valid as
`simplewallet --generate-new-wallet arg`
or is it correct that it forces you to name the wallet?


## petertodd | 2016-03-02T20:07:54+00:00
Well, I think it'd be good if 'simeplewallet --generate-new-wallet'
created a new wallet of the form <addr>.wallet like the help text says
it does. But yeah, changing the help text would be a way to fix this
issue too.

> `simplewallet --generate-new-wallet`
> returns the error message
> `Failed to parse arguments: the required argument for option '--generate-new-wallet' is missing`
> 
> For clarity's sake, is the bug that the help is wrong or that the default behavior is not working?
> 
> i.e. Should
> `simeplewallet --generate-new-wallet`
> be just as valid as
> `simplewallet --generate-new-wallet arg`
> or is it correct that it forces you to name the wallet?
> 
> ---
> 
> Reply to this email directly or view it on GitHub:
> https://github.com/monero-project/bitmonero/issues/691#issuecomment-191393271

## 

https://petertodd.org 'peter'[:-1]@petertodd.org
000000000000000000f755631f059a7cbbefae9e2d3783197e824154dd926639


# Action History
- Created by: fluffypony | 2016-02-29T22:28:00+00:00
- Closed at: 2016-08-26T08:32:38+00:00
