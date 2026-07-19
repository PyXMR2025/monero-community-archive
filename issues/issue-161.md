---
title: Repurposing `unlock_time` for relative locks with FCMP++
source_url: https://github.com/monero-project/research-lab/issues/161
author: tevador
assignees: []
labels: []
created_at: '2026-07-15T16:57:50+00:00'
updated_at: '2026-07-17T10:32:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The legacy `unlock_time` field in Monero is [being deprecated](https://www.getmonero.org/2026/05/10/deprecating-unlock-time.html). It's planned that the next hard fork will enforce a value of 0 in all transactions.

The arguments against `unlock_time` are:

1. It's not actually useful for any decentralized protocol (payment channels, atomic swaps).
2. It's a DoS vector on the FCMP++ tree.
3. It creates anonymity puddles.
4. There have been issues with merchants receiving maliciously locked payments.

## Relative locks

Relative locks are useful for a variety of decentralized protocols. Notably, payment channels are notoriously hard to design for Monero. The simplest payment channel protocol only requires adaptor signatures and relative locks. Adaptor signatures are already possible with FCMP++ (and the separate membership proof further facilitates pre-signed transactions). The only missing feature is a simple relative lock.

Note that Monero already enforces a relative 10-block lock. For FCMP++, it means the `anchor_height` (the height of the FCMP++ tree root used for the membership proof) must be at least 10 blocks less than `block_height` (the height where the transaction is confirmed).

A simple yet useful relative lock could be introduced by allowing `unlock_time` to be equal to `0` or `1` as follows:

| `unlock_time` | Lock type | `block_height - anchor_height` | Lock time |
|---------------|-----------|--------------------------------|-----------|
|    `0`        | no lock   |   `>= 10`                      | 20 minutes|
|    `1`        | relative lock | `>= 720`                   | 24 hours  |

To avoid anonymity puddles, only a single relative lock value is allowed, which is sufficient for the required use cases (e.g. payment channel close dispute). The 24h lock time is just an example. The exact lock duration is up for discussion. Longer lock times (up to 1 week) might offer better UX for payment channel disputes.

To avoid leaking the fact that the transaction was time-locked, wallets could randomly set `unlock_time` to `1` when spending an output older than the lock time with a small probability. The leakage would be limited to the fact that the age of the spent output was at least 24 hours.

**To avoid confusion: This proposal completely changes the way `unlock_time` works after the FCMP++ hard fork. The lock is not applied to the transaction outputs. It's applied to transaction inclusion in the blockchain. Locked transactions cannot even enter the mempool until they unlock.**

## Payment channel protocol sketch

Here is a sketch of a trustless payment channel protocol. The payment channel is bidirectional between Alice and Bob. Transactions fees are ignored for clarity.

### Opening the channel

The channel is opened by Alice and Bob jointly signing 4 transactions: **Fund**, **CloseA**, **CloseB** and **Recover**. The **Fund** transaction is immediately submitted to the network. Alice keeps **CloseA** and **Recover** as her offline transactions and Bob keeps **CloseB** and **Recover** as his offline transactions.

The channel opening process is:

1. Alice and Bob agree on the initial channel balances.
1. Alice and Bob agree on a 2-of-2 stealth address <code>K<sup>fund</sup></code>.
1. Alice and Bob agree on a 2-of-2 stealth address <code>K<sup>close</sup><sub>0</sub></code>.
1. Alice and Bob jointly sign the initial **Recover** transaction, which spends from <code>K<sup>close</sup><sub>0</sub></code> to Alice's and Bob's private addresses according to the correct channel balances. The **Recover** transaction has `unlock_time = 1`, so it's time-locked relative to the preceding **Close** transaction.
1. Alice generates a key pair and shares the public key <code>T<sup>A</sup><sub>0</sub></code> with Bob.
1. Bob generates a key pair and shares the public key <code>T<sup>B</sup><sub>0</sub></code> with Alice.
1. Alice signs her half of the **CloseB** transaction, which spends the entire channel balance from <code>K<sup>fund</sup></code> to <code>K<sup>close</sup><sub>0</sub></code>. Alice uses <code>R + T<sup>B</sup><sub>0</sub></code> as the signature nonce. This creates an adaptor signature only Bob can complete.
1. Bob signs his half of the **CloseA** transaction, which spends the entire channel balance from <code>K<sup>fund</sup></code> to <code>K<sup>close</sup><sub>0</sub></code>. Bob uses <code>R + T<sup>A</sup><sub>0</sub></code> as the signature nonce. This creates an adaptor signature only Alice can complete.
1. Finally, Alice and Bob jointly sign the **Fund** transaction, which spends their private inputs into the stealth address <code>K<sup>fund</sup></code>.

The channel opening is complete when the **Fund** transaction is confirmed on the Monero network.

```
              [Fund]
                |
     ___________|_____________
     |                       |
     v                       V
[CloseA(0)]             [CloseB(0)]
     |                       |
     |_______________________|
                |
                v
     [Recover(0)(time-locked)]
```

### Channel state update

The channel transitions from state N-1 to state N (with new channel balances for Alice and Bob) as follows:

1. Alice and Bob agree on new channel balances.
1. Alice and Bob agree on a 2-of-2 stealth address <code>K<sup>close</sup><sub>N</sub></code>.
1. Alice and Bob jointly sign the N-state **Recover** transaction, which spends from <code>K<sup>close</sup><sub>N</sub></code> to Alice's and Bob's private address according to the correct channel balances. The **Recover** transaction has `unlock_time = 1`, so it's time-locked relative to the preceding **Close** transaction.
1. Alice generates a key pair and shares the public key <code>T<sup>A</sup><sub>N</sub></code> with Bob.
1. Bob generates a key pair and shares the public key <code>T<sup>B</sup><sub>N</sub></code> with Alice.
1. Alice signs her half of the N-state **CloseB** transaction, which spends the entire channel balance from <code>K<sup>fund</sup></code> to <code>K<sup>close</sup><sub>N</sub></code>. Alice uses <code>R + T<sup>B</sup><sub>N</sub></code> as the signature nonce. This creates an adaptor signature only Bob can complete.
1. Bob signs his half of the **CloseA** transaction, which spends the entire channel balance from <code>K<sup>fund</sup></code> to <code>K<sup>close</sup><sub>N</sub></code>. Bob uses <code>R + T<sup>A</sup><sub>N</sub></code> as the signature nonce. This creates an adaptor signature only Alice can complete.
1. Alice signs her half of the N-state **PunishA** transaction, which spends the entire channel balance from <code>K<sup>close</sup><sub>N-1</sub></code> to Bob's private address. Alice uses <code>R + T<sup>A</sup><sub>N-1</sub></code> as the signature nonce, but omits <code>t<sup>A</sup><sub>N-1</sub></code> from the signature response, which makes the signature invalid.
1. Bob signs his half of the N-state **PunishB** transaction, which spends the entire channel balance from <code>K<sup>close</sup><sub>N-1</sub></code> to Alice's private address. Bob uses <code>R + T<sup>B</sup><sub>N-1</sub></code> as the signature nonce, but omits <code>t<sup>B</sup><sub>N-1</sub></code> from the signature response, which makes the signature invalid.

The new transaction graph looks like this:

```
               [Fund]
                 |
      ___________|_____________
      |                       |
      v                       V
[CloseA(N-1)]           [CloseB(N-1)]
     |                       |
     |_______________________|
                |
                |
                -> [Recover(N-1)(time-locked)]
                |
                |
                -> [PunishA(N)]
                |
                |
                -> [PunishB(N)]


              [Fund]
                |
     ___________|_____________
     |                       |
     v                       V
[CloseA(N)]             [CloseB(N)]
     |                       |
     |_______________________|
                |
                v
     [Recover(N)(time-locked)]
```


### Closing the channel

| Type       | Description | On-chain transactions           |
|------------|-------------|---------------------------------|
| collaborative close | Alice and Bob jointly close the channel | **Fund** (unlock_time=0), **Withdraw** (unlock_time=0) |
| undisputed force close | one party forces the channel to close | **Fund** (unlock_time=0), **Close** (unlock_time=0), **Recover** (unlock_time=1) |
| disputed force close | one party forces the channel to close with incorrect state | **Fund** (unlock_time=0), **Close** (unlock_time=0), **Punish** (unlock_time=0) |

#### Collaborative close

The happy path is if Alice and Bob both agree to close the channel. In that case, they jointly sign a new **Withdraw** transaction, which spends from <code>K<sup>fund</sup></code> to Alice's and Bob's private addresses according to the final channel balances.

#### Undisputed force close

If Bob is unresponsive, Alice can force the channel to close by publishing the **CloseA(N)** transaction. She then has to wait for 24 hours and then publish the **Recover(N)** transaction, which will distribute the funds in the channel according to the final state.

Note that this is the only case when a time-locked transaction with `unlock_time = 1` appears on the chain.

#### Disputed force close

Alice can try to maliciously close the channel with an old state by publishing **CloseA(i)** with `i < N`.

When **CloseA(i)** appears on the chain, Bob can recover <code>t<sup>A</sup><sub>i</sub></code> from the valid transaction signature (using the adaptor saved in step `i+1`). This allows Bob to complete the signature of the **PunishA(i+1)** transaction. Since the **Punish** transaction is not locked, Bob can front-run Alice's **Recover** transaction and punish Alice by taking the entire channel balance.

# Discussion History
## UkoeHB | 2026-07-15T17:15:29+00:00
> To avoid leaking the fact that the transaction was time-locked, wallets could randomly set unlock_time to 1 when spending an output older than the lock time with a small probability. The leakage would be limited to the fact that the age of the spent output was at least 24 hours.

`unlock_time` applies to new enotes, not spending old ones. Wallets can't be randomly locking funds on send.

## tevador | 2026-07-15T17:19:41+00:00
@UkoeHB I think you misunderstood. The repurposed lock is only applied to off-chain transactions. Locked transactions cannot be submitted to the mempool.

The wallet knows the age of the inputs it's spending. If that age is >720 blocks, setting `unlock_time = 1` is easy, the wallet will only use a different FCMP root hash for the membership proof.

## tevador | 2026-07-16T05:31:45+00:00
I added a payment channel protocol sketch that uses the proposed relative lock mechanism.

# Action History
- Created by: tevador | 2026-07-15T16:57:50+00:00
