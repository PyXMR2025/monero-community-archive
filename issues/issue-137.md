---
title: 'Idea: CKB Cell to carry block template'
source_url: https://github.com/monero-project/research-lab/issues/137
author: Schneiderei
assignees: []
labels: []
created_at: '2025-08-11T15:20:02+00:00'
updated_at: '2025-08-15T08:34:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Idea: CKB Cell to carry block template**
Idea as a proposal to establish a security anchor to support the existing PoW consensus of Monero.

Miners can read the corresponding CKB cell to safely mine on a known block mined by trusted entities. The blocks from untrusted miners must match the hashes of the blocks in the CKB cells in order to be used for mining.
All possible forms of data can be written to a CKB cell. One CKB, the layer 1 of the Nervos Network Blockchain, corresponds to one byte of data.

Goal: Maintain the proof-of-work hashrate of the known, centralized XMR pools until most of the hashrate has been mined on P2pool or another secure solution against 51% attacks has been established.

Use of the other decentralized and permissionless PoW blockchain "Nervos Network" to write the hashes of the block templates to CKB cells approximately every ten seconds.

The blocks of the largest known pools, having over 1% of the total hashrate, are used as consensus anchors. The pools marked here are currently responsible for over 75% of the hashrate.
- https://supportxmr.com/ 
- https://xmr.nanopool.org/
- https://monero.hashvault.pro/
- https://c3pool.com/
- https://p2pool.io/
- https://moneroocean.stream/
- https://pool.kryptex.com/xmr
 
These pools have earned a long history and credibility over the years. We do not want to lose the existing hashrate of these pools, even if the miners do not switch to P2pool on their own. So we use the blocks of these pools, usually generated per ten seconds, and compare these blocks. If the blocks of these known entities match, Block hash (height) can be written to a CKB cell.

 **hex string to data field** https://docs.nervos.org/docs/dapp/store-data-on-cell

https://docs.nervos.org/
https://explorer.nervos.org/charts
Average Block Time: 7.93 s
Mining Hash Rate: 281.19 PH/s

> The CKB-VM is the virtual machine that executes Scripts on the CKB. It uses the RISC-V instruction set, which is a modern, open-source architecture. This design provides a low-level access to the CPU, enabling highly efficient execution and flexibility.

> Eaglesong is a new hash function developed specifically for Nervos CKB proof-of-work, which is also suitable in other use cases in which a secure hash function is needed.

For information on **single-use seals and client-side validation techniques**, see **RGB++ Protocol**: https://docs.nervos.org/docs/tech-explanation/rgbpp
This newer technology also enables other opportunities for potential Monero consensus strengthening.

# Discussion History
## Schneiderei | 2025-08-11T21:33:14+00:00
GPT-4:

CCC connector
1. Functionality

    The CCC connector makes it possible to exchange data and information between different blockchains. This could make it easier for miners to write block information into CKB cells or read it out.
    By using the CCC connector, miners could directly access the information they need without having to develop complex interfaces or protocols.

2. advantages for miners

    **Easy integration:** Miners could access trusted block information more easily, making the validation and mining process more efficient.
    **Speed:** Block information could be accessed faster, improving miner response time and reducing the likelihood of attacks.
    **Security:** By using a standardized protocol, security risks could be minimized as communication between blockchains is clearly defined.

3. implementation

    The implementation of the CCC connector requires careful planning to ensure that data integrity and security is maintained.
    It would be important to define the specific requirements and protocols needed for the exchange of block information between Monero and Nervos Network.

## kayabaNerve | 2025-08-14T20:50:45+00:00
This is a proposal to federate Monero using the Nervos blockchain for the federation to communicate? This just removes the network's decentralization in favor of existing pools, while adding an entire other blockchain for little benefit (PoW alone would work if we simply only allow the mentioned pools to be the only miners).

## Schneiderei | 2025-08-15T08:34:18+00:00
> (PoW alone would work if we simply only allow the mentioned pools to be the only miners).

That is very true, you could simply allow the pools listed exclusively.

The idea was written down spontaneously at a time of 30+ % hashrate of a not-by-the-rules-playing miner. As a potential emergency solution, not thought through.

Thank you.

# Action History
- Created by: Schneiderei | 2025-08-11T15:20:02+00:00
