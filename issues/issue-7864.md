---
title: Private smart contracts
source_url: https://github.com/monero-project/monero/issues/7864
author: 9mido
assignees: []
labels: []
created_at: '2021-08-16T04:33:49+00:00'
updated_at: '2022-12-18T09:22:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
https://en.wikipedia.org/wiki/Homomorphic_encryption

https://eprint.iacr.org/2021/133.pdf

https://eprint.iacr.org/2019/191.pdf

Create private smart contracts using the computational power of the interested parties in any given transaction. Instead of the nodes executing some shady smart contract code, it would be the parties involved (their computers) executing the smart contract. Since the nodes would not execute the smart contracts, there would be no need for gas. Oracles come to mind. 

Parties agree to make transactions conditioned by some smart contract code, and it's their business, the network only waits until it's fully confirmed by all involved parties, then it confirms the transaction. The mempool would grow most likely.

Every contract would need to have its own address.

If there is no agreement or cheating between parties, then there is no transaction. For example, let's say you and me trust an oracle's provider. What that oracle says is accepted as truth by all parties. This oracles provider would be paid a small fee. It's mission is just to verify an information and say true/false. This third party executes the contract code. And it requires one more signature to be a valid transaction (2 of 3). Once any of the parties accept what the oracle said is true signs, it's done. The parties execute the contract as well, to that end. This can be done on bitcoin, but making it private would be ideal.

Imagine we make a bet for who wins a race. There is a company that verifies the result and pays the bettors. This company "approves" (signs) transactions that match the result in real life. That company that verifies the results of the race is an oracle who says what is true and reflects that reality on the blockchain. This oracle verifies the race results and does so on the blockchain.

This process would not look at the miners and instead it would be a second layer. It would not be PoS, it would instead be someone running a program on their server, and a monero node. Their program simply signs transactions, that are broadcast on the monero blockchain. The key is to make the whole thing private without compromising identities. 

Bitcoin will eventually have smart contracts with the taproot update. Maybe monero could follow bitcoin's approach but make it more private.

# Discussion History
## zh54tg234f | 2022-12-18T09:20:22+00:00
There are indeed many use cases for private and opt in public smart contracts. 
The ecosystem would grow and options arise, so mostly legit DEX / liability loans etc and some scams.

# Action History
- Created by: 9mido | 2021-08-16T04:33:49+00:00
