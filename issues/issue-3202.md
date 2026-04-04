---
title: Add sweep_all_mixable command
source_url: https://github.com/monero-project/monero/issues/3202
author: dEBRUYNE-1
assignees: []
labels:
- feature
created_at: '2018-01-29T12:19:54+00:00'
updated_at: '2021-08-13T06:42:06+00:00'
type: issue
status: closed
closed_at: '2021-08-13T06:42:06+00:00'
---

# Original Description
Currently the sweep_all button will try to include unmixable outputs as well. It'll subsequently fail because those unmixable outputs don't have sufficient ring partners. Now, typically one can make unmixable outputs mixable with the `sweep_unmixable` command. However, in some cases these unmixable outputs can't pay for themselves (per moneromooo, note that some tiny mixable outputs may also not be able to pay for themselves), which then creates a potential problem for the `sweep_all` command. Therefore, it might be beneficial if we had a `sweep_all_mixable` command too that only sweeps mixable outputs. 

# Discussion History
## dEBRUYNE-1 | 2018-01-29T12:20:00+00:00
+feature

## mizuki-hikaru | 2018-04-22T02:31:34+00:00
Gave this an attempt at pull request https://github.com/monero-project/monero/pull/3680 . It uses a function that extracts mixables that is already written in `wallet2.cpp`, however I'm not sure this function is actually doing what is intended. Can anyone review this? ^_^

## stoffu | 2018-05-04T08:31:29+00:00
Isn't it strange in the first place that `sweep_all` tries to send both mixable and unmixable outputs, when the tx is required to have a minimum ring size (so trying to send unmixable outputs will always fail)?

## selsta | 2021-08-13T06:42:06+00:00
Should be resolved with #3991

# Action History
- Created by: dEBRUYNE-1 | 2018-01-29T12:19:54+00:00
- Closed at: 2021-08-13T06:42:06+00:00
