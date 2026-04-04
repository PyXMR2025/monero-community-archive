---
title: Use the Monroe wallet node command "create"_ It takes 10 minutes to create
  a sub address. What's the problem?
source_url: https://github.com/monero-project/monero/issues/6730
author: niukouMan
assignees: []
labels: []
created_at: '2020-07-31T06:37:14+00:00'
updated_at: '2022-04-10T18:53:07+00:00'
type: issue
status: closed
closed_at: '2022-04-10T18:53:07+00:00'
---

# Original Description
Use the Monroe wallet node command "create"_ It takes 10 minutes to create a sub address. What's the problem?

# Discussion History
## selsta | 2020-07-31T11:50:49+00:00
Can you give more infos?

Which version are you using?

Which OS?

Are you using Ledger / Trezor?

What kind of hardware?

## moneromooo-monero | 2020-07-31T11:53:07+00:00
There is no create. Do you mean create_wallet, create_address, create_account ?
I assume this is RPC. Can you post the JSON you're sending ?

## niukouMan | 2020-08-03T01:30:34+00:00
Use the "Create Address" RPC command but It takes 10 minutes for the node to respond to the result

## niukouMan | 2020-08-03T01:31:27+00:00
> There is no create. Do you mean create_wallet, create_address, create_account ?
> I assume this is RPC. Can you post the JSON you're sending ?

i use the "Create Address" RPC command It takes 10 minutes for the node to respond to the result

## niukouMan | 2020-08-03T01:41:42+00:00
> Can you give more infos?
> 
> Which version are you using?
> 
> Which OS?
> 
> Are you using Ledger / Trezor?
> 
> What kind of hardware?

The operating system is Ubuntu and the XMR node is 16.0.1
Use the RPC command to call the node's "create Address" command and wait 10 minutes to respond to the result

## moneromooo-monero | 2020-08-03T12:44:24+00:00
Which account_index are you trying to create ? Is it a very large number ?

## niukouMan | 2020-08-04T01:11:04+00:00
> account_index

account_index is 0

## selsta | 2022-04-10T18:53:07+00:00
Please try the latest version.

Closing as there were no other reports about this, so could be some issue with the local system. If you continue to have this issue comment here and I can reopen the issue.

# Action History
- Created by: niukouMan | 2020-07-31T06:37:14+00:00
- Closed at: 2022-04-10T18:53:07+00:00
