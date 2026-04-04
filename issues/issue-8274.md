---
title: eternal loading wallet...(rpc)
source_url: https://github.com/monero-project/monero/issues/8274
author: dmitrykrylov18
assignees: []
labels: []
created_at: '2022-04-21T00:27:14+00:00'
updated_at: '2022-05-29T15:31:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi. I start monero-wallet-rpc with command ./monero-wallet-rpc --daemon-address 127.0.0.1:18081 --rpc-bind-port 28082 --generate-from-json crypto.json --daemon-login daemon-user:daemon-pass (after monerod --rpc-login daemon-user:daemon-pass --detach). But the last log is "Monero 'Oxygen Orion' (v0.17.3.0-release)
Logging to ./monero-wallet-rpc.log
2022-04-21 00:12:06.780 W Loading wallet...". why the wallet don t continue staring? thank you in advance
![telegram-cloud-photo-size-2-5404579330102770969-y](https://user-images.githubusercontent.com/41378307/164345660-c3e43774-d46d-4f11-9501-89dd545317bb.jpg)
![telegram-cloud-document-2-5404579329646533656](https://user-images.githubusercontent.com/41378307/164345703-67ce1db6-0c23-44d8-92de-85c33cdb5841.jpg)


# Discussion History
## selsta | 2022-04-22T16:16:04+00:00
Can you start with `--log-level 2`?

# Action History
- Created by: dmitrykrylov18 | 2022-04-21T00:27:14+00:00
