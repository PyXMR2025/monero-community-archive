---
title: reddit submitted typo
source_url: https://github.com/monero-project/monero/issues/1922
author: grummerd
assignees: []
labels: []
created_at: '2017-03-25T07:44:09+00:00'
updated_at: '2017-04-04T10:12:31+00:00'
type: issue
status: closed
closed_at: '2017-04-04T10:12:31+00:00'
---

# Original Description
Minor typo in `monero-wallet-cli` command, sweep_all
-------------------------------------------------------------------------

[`/u/moneronoob12345` writes:](https://np.reddit.com/r/Monero/comments/61cs9c/typo_in_cli_wallet/)

sweep_all sweep_all [mixin] address [payment_id] - Send all unlocked balance an address

It should be:

sweep_all sweep_all [mixin] address [payment_id] - Send all unlocked balance **to** an address



# Discussion History
## grummerd | 2017-03-25T07:46:44+00:00
`monero-wallet-cli --wallet-file=[your wallet] --password=[your password] --command help`

Then look for the sweep_all command description


## darentuzi | 2017-03-25T09:32:37+00:00
pull request #1921 fixes this

# Action History
- Created by: grummerd | 2017-03-25T07:44:09+00:00
- Closed at: 2017-04-04T10:12:31+00:00
