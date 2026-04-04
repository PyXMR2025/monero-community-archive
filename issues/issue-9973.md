---
title: Offline transaction signing not working
source_url: https://github.com/monero-project/monero/issues/9973
author: tczee36
assignees: []
labels:
- question
created_at: '2025-07-02T00:18:16+00:00'
updated_at: '2025-08-30T18:48:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![Image](https://github.com/user-attachments/assets/df347c5b-6c31-4ec9-ae4b-341e50389701)

Following the actions on https://docs.getmonero.org/cold-storage/offline-transaction-signing/#launching-a-view-only-wallet

Offline transaction signing.

cannot get past the error 'transfer xmr-address amount-of-xmr-to-send'

unsigned_monero_tx in the current working directory never gets generated.

System: Ubuntu 24.04 LTS - latest patch

View-only wallet synced with remote node.



# Discussion History
## tczee36 | 2025-07-02T04:17:45+00:00
> Ensure the unsigned transaction is fully formed with correct network parameters, verify the offline signing tool supports the transaction type, and double-check that the private key or hardware wallet is properly configured and connected.
> 
> 

wallet was created with monero-cli, node is trusted daemon + synced mainnet.

unsigned transactions doesn't get generated, so the signing offline step never happened 

# Action History
- Created by: tczee36 | 2025-07-02T00:18:16+00:00
