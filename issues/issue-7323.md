---
title: monerod.exe stops syncing while mining
source_url: https://github.com/monero-project/monero/issues/7323
author: mrwhy-orig
assignees: []
labels: []
created_at: '2021-01-18T10:35:52+00:00'
updated_at: '2022-07-19T19:57:06+00:00'
type: issue
status: closed
closed_at: '2022-07-19T19:57:06+00:00'
---

# Original Description
monerod.exe version 0.17.1.9-release

I encountered the phenomen, that the daemon stops syncing while mining. The daemon runs on a windows 10 vm with 3 cores assigned, 2 are mining. It is a full node as i'm planning to mine with other computers in my network. 

At the moment, i check the status occasionally with the status command. As soon as I'm issueing the command the daemon starts to sync again. But there is no sign of stopping sync. 

I'm using the following flags:

monerod.exe --rpc-restricted-bind-ip x.x.x.x --rpc-restricted-bind-port 18089 --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18081 --confirm-external-bind --public-node --rpc-payment-address 4xxxx --rpc-payment-credits 250 --rpc-payment-difficulty 1000



# Discussion History
## selsta | 2022-02-19T00:45:26+00:00
While I don't think it makes sense to mine in a VM, do you have any logs? For testing reasons please also remove everything related to `rpc-payment`.

## selsta | 2022-07-19T19:57:06+00:00
Closing this as we didn't get a second report about this and the original author didn't reply.

# Action History
- Created by: mrwhy-orig | 2021-01-18T10:35:52+00:00
- Closed at: 2022-07-19T19:57:06+00:00
