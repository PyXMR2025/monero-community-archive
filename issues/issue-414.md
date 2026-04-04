---
title: Provide better tutorials / info on cli tools
source_url: https://github.com/monero-project/monero-site/issues/414
author: jonathancross
assignees: []
labels: []
created_at: '2017-09-23T02:08:48+00:00'
updated_at: '2020-04-07T09:33:35+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:33:34+00:00'
---

# Original Description
RE: https://github.com/monero-project/monero/issues/985

We should provide better documentation and examples of cli tools, options and how to use.
I'm assuming this would go here : https://getmonero.org/resources/user-guides/ but maybe there is a better location?  Something like "How to use monero in a terminal" with very basic examples and linking off to details about configuration of `monerod`, `monero-wallet-cli` options, etc.


# Discussion History
## QuickBASIC | 2017-09-23T02:11:01+00:00
> I'm assuming this would go here : 

The README for monero-site has directions for adding a user guide. If you feel so inclined, follow those directions.

## mattcode55 | 2017-09-23T08:09:33+00:00
There's a guide for the wallet cli at https://getmonero.org/resources/user-guides/monero-wallet-cli.html

## jonathancross | 2017-10-11T14:58:01+00:00
Makes sense.  I'll look into it setting up locally and making the change myself.

## QuickBASIC | 2017-10-11T15:23:30+00:00
Awesome. From the way you phrased the issue it sounded like you intended on fixing it yourself. Make sure you use issue keywords 'fixes #blah' in a commit message or PR to close the issue when it gets merged.

## erciccione | 2017-10-22T12:02:51+00:00
+improvement

## jacklenox | 2018-01-09T13:08:40+00:00
Having recently been through this, I'd be happy to try to help here. Are we talking about literally just setting the daemon going and opening up the wallet?

## jonathancross | 2018-01-19T18:43:27+00:00
@jacklenox Contributions welcome! I kinda dropped the ball and got distracted with other things.

Idea is just to add examples and explanations for common use cases here: https://getmonero.org/resources/user-guides/

The [monero-wallet-cl](https://getmonero.org/resources/user-guides/monero-wallet-cli.html)i example is great, would be nice to have a similar document for the daemon.  Here are a few ideas:

* How to securely allow remote connections (and considerations)
* How to only allow rpc from localhost
* username / password considerations (eg: can't use `#` in the password or it is interpreted as a comment and will strip all characters after that in the bitmonero.conf)
* _some_ commandline arguments work inside `bitmonero.conf`, others do not. A few example that don't:
  * `no-igd`
  * `confirm-external-bind`
  * `restricted-rpc`
  * `rpc-bind-ip` - works, but cannot be specified more than once


## erciccione | 2020-04-07T09:33:34+00:00
This issue is old and was discussed and closed on gitlab. Please reopen if you feel it's still relevant.

# Action History
- Created by: jonathancross | 2017-09-23T02:08:48+00:00
- Closed at: 2020-04-07T09:33:34+00:00
