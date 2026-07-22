---
title: Relative locks with FCMP++
source_url: https://github.com/monero-project/research-lab/issues/161
author: tevador
assignees: []
labels: []
created_at: '2026-07-15T16:57:50+00:00'
updated_at: '2026-07-22T17:24:56+00:00'
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

Note that Monero already enforces a relative 10-block lock. For FCMP++, it means the tree root <code>R</code> used for the membership proof must be at least 10 blocks old. This proposal adds the option to make the lock longer than 10 blocks.

**This proposal completely changes the way locked transactions work after the FCMP++ hard fork. The lock is not applied to the transaction outputs. It's applied to transaction inclusion in the blockchain. Locked transactions cannot even enter the mempool until they unlock.**

## Hiding locks with a ring signature

My original proposal was to use `unlock_time = 1` to publicly declare a time-locked transaction, which would be enforced at the consensus layer by checking that the age of the tree root `R` is older than a week.

@UkoeHB suggested a more private solution based on a ring signature on the root hash comitment. Let <code>R<sub>h</code> be the FCMP tree root at height `h` and `ref` be the explicit transaction reference height (the earliest height the transaction is mineable).

The protocol will support a few possible lock times, for example:

| <code>i</code> | Approx. lock duration | <code>R<sub>i</sub></code> |
|---------------|-------------|------------------------------|
|    `0`        | 20 minutes  | <code>R<sub>ref-10</code>
|    `1`        | 3 hours     | <code>R<sub>ref-90</code>
|    `2`        | 1 day       | <code>R<sub>ref-720</code>
|    `3`        | 1 week      | <code>R<sub>ref-5040</code>
|    `4`        | 8 weeks     | <code>R<sub>ref-40320</code>
|    `5`        | 1 year      | <code>R<sub>ref-262800</code>
|    `6`        | 8 years     | <code>R<sub>ref-2102400</code>

Each transaction will include an additional commitment <code>L = j H + x G</code> with j equal to one of the i values from the table above (i.e. 0 <= j <= 6). The value j = 0 corresponds to the default 10-block lock. The commitment `L` is signed by the spend authorization proof.

The FCMP++ proof outputs a tree root commitment <code>R = R<sub>j</sub> + y G</code> where <code>R<sub>j</sub></code> is one of the <code>R<sub>i</sub></code> values from the table.

We then define the ring <code>(L - i H, R - R<sub>i</sub>)</code> for each `i = 0..6`. Note that the prover will know the opening of exactly the j-th pair from the ring. This can be proven with a standard ring signature. The approximate size of a 7-ring signature is 256 bytes, which is relatively small compared to the size of the FCMP++ proof.

The purpose of this construction is for the pre-signed commitment `L` to force a relative lock without publicly revealing that the transaction was pre-signed and time-locked.

## Payment channel protocol sketch

Here is a sketch of a trustless payment channel protocol that required a relative lock on a pre-signed transaction. The payment channel is bidirectional between Alice and Bob. Transactions fees are ignored for clarity.

### Opening the channel

The channel is opened by Alice and Bob jointly signing 4 transactions: **Fund**, **CloseA**, **CloseB** and **Recover**. The **Fund** transaction is immediately submitted to the network. Alice keeps **CloseA** and **Recover** as her offline transactions and Bob keeps **CloseB** and **Recover** as his offline transactions.

The channel opening process is:

1. Alice and Bob agree on the initial channel balances.
1. Alice and Bob agree on a 2-of-2 stealth address <code>K<sup>fund</sup></code>.
1. Alice and Bob agree on a 2-of-2 stealth address <code>K<sup>close</sup><sub>0</sub></code>.
1. Alice and Bob jointly sign the initial **Recover** transaction, which spends from <code>K<sup>close</sup><sub>0</sub></code> to Alice's and Bob's private addresses according to the correct channel balances. The **Recover** transaction is time-locked relative to the preceding **Close** transaction.
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
1. Alice and Bob jointly sign the N-state **Recover** transaction, which spends from <code>K<sup>close</sup><sub>N</sub></code> to Alice's and Bob's private address according to the correct channel balances. The **Recover** transaction is time-locked relative to the preceding **Close** transaction.
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
| collaborative close | Alice and Bob jointly close the channel | **Fund**, **Withdraw** |
| undisputed force close | one party forces the channel to close | **Fund**, **Close**, **Recover** (time-locked) |
| disputed force close | one party forces the channel to close with incorrect state | **Fund**, **Close**, **Punish** |

#### Collaborative close

The happy path is if Alice and Bob both agree to close the channel. In that case, they jointly sign a new **Withdraw** transaction, which spends from <code>K<sup>fund</sup></code> to Alice's and Bob's private addresses according to the final channel balances.

#### Undisputed force close

If Bob is unresponsive, Alice can force the channel to close by publishing the **CloseA(N)** transaction. She then has to wait for 24 hours and then publish the **Recover(N)** transaction, which will distribute the funds in the channel according to the final state.

Note that this is the only case when a time-locked transaction with appears on the chain.

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

## UkoeHB | 2026-07-21T00:22:08+00:00
> Re: privacy

Setting aside perf, would it be possible to sign a ring signature on the FCMP++ root hash? Where it's a dual-layer ring, one layer is the commitments to zero of root hashes and the other is commitments to zero of multiples `m` of `H`. The relative lock `L` is a commitment to one multiple of `H`, and you sign in the ring sig on `L - mH = xG` (and include `L` in the SAL proof message). The root hash ring members are selected from pre-defined block depths (10 blocks, 1 day of blocks, 1 week of blocks, etc.) relative to the indicated signing block (at >= 10 block depth).

The question in my mind is whether FCMP++ proofs could be constructed relative to a *commitment* to the root hash, rather than the root hash directly.

## UkoeHB | 2026-07-21T00:53:04+00:00
> When CloseA(i) appears on the chain, Bob can recover tAi from the valid transaction signature (using the adaptor saved in step i+1). This allows Bob to complete the signature of the PunishA(i+1) transaction. Since the Punish transaction is not locked, Bob can front-run Alice's Recover transaction and punish Alice by taking the entire channel balance.

This is the interesting bit.

We were discussing in MRL whether `unlock_time` could achieve this. My idea that *almost* works (but you are right, does not):
- Pair **Close** variants with **DummyLock**. **DummyLock** spends a tiny amount from `K^fund`, has a timelock, and outputs a zero-amount enote.
- Write **Recover** txs so they spend from **DummyLock**'s output. This way **DummyLock** must be submitted along with **Close** variants if you want to recover.

The problem is current timelocks are based on a specific blockheight, not relative (as in this proposal), so if the channel is old enough **Recover** can always be submitted immediately after an old **Close**.

## tevador | 2026-07-21T06:11:28+00:00
> Setting aside perf, would it be possible to sign a ring signature on the FCMP++ root hash? Where it's a dual-layer ring, one layer is the commitments to zero of root hashes and the other is commitments to zero of multiples `m` of `H`. The relative lock `L` is a commitment to one multiple of `H`, and you sign in the ring sig on `L - mH = xG` (and include `L` in the SAL proof message). The root hash ring members are selected from pre-defined block depths (10 blocks, 1 day of blocks, 1 week of blocks, etc.) relative to the indicated signing block (at >= 10 block depth).
>

I think that would work and would completely hide the fact that a transaction was time-locked. However, it would require significant changes to the FCMP circuit, which is not something we'd want to do at this stage (code already written, audits in progress etc.).

The FCMP proof could use an artificial root <code>R' = a R<sub>10</sub> + b R<sub>720</sub> + c R<sub>5040</sub> + x<sub>1</sub> G</code>, where `a, b, c` are `0` or `1` and `a + b + c = 1`. The pre-signed lock commitment would be <code>L = a H<sub>1</sub> + b H<sub>2</sub> + c H<sub>3</sub> + x<sub>2</sub> G</code> for some generators <code>H<sub>1</sub>, H<sub>2</sub>, H<sub>3</sub></code>. The circuit would prove the knowledge of <code>a, b, c, x<sub>1</sub>, x<sub>2</sub></code> with the public witnesses <code>R', L, R<sub>10</sub>, R<sub>720</sub>, R<sub>5040</sub></code>, where <code>R<sub>x</sub></code> is the tree root `x` blocks ago.

CC @kayabaNerve



## kayabaNerve | 2026-07-21T14:22:56+00:00
Having yet to read the issue in its entirety,

The FCMP as-is already outputs a Pedersen commitment to the tree root. It's outside of the circuit that we unblind it and reveal the underlying root. By modifying the library, but not the circuit, it should be fine to then pipe into a ring signature.

One may also allow the user to declare the tree roots (subject to the standard validity criteria), where these become the top layer of the tree proven against. This wouldn't require modifying any of the FCMP code at all, with caveat the trees would be expected to have consistent length. There also wouldn't be a need to require only one root has a non-zero coefficient so long as we're fine publicly declaring the _candidate_ roots.

I'll try to read the issue in full and give a more specific response later.

## tevador | 2026-07-21T16:08:41+00:00
> The FCMP as-is already outputs a Pedersen commitment to the tree root.

Thanks, I wasn't aware. The solution proposed by @UkoeHB with a two-layer ring signature should work without changes then. If we allow 5-6 possible lock times, which should be plenty, I'm estimating that the transaction size would increase by about 300 bytes. I think the cost of this change would be quite low, which makes for a strong case in support of implementing relative locks this way on top of FCMP++.

## UkoeHB | 2026-07-21T23:11:58+00:00
Wanted to point out that side-effects from state changes (e.g. a real-world exchange) must not occur until after a state change is fully finalized and validated. Otherwise there are race conditions that let one participant close the previous state without penalty (e.g. initialize a payment, receive the good, then back out without completing the payment state change by submitting close on the previous state but without threat of punishment).

## UkoeHB | 2026-07-22T05:07:43+00:00
I think you can hostage a channel by receiving a punish but refusing to send your own punish. If the partner tries to close + recover with the previous state, the attacker can just punish and take the funds. The partner may not want to close with the current state e.g. because the current state is a transfer of funds from them to the attacker but they did not receive the goods of an exchange yet. If favorable, the attacker can close + recover the current state. This is a pretty standard problem for 2-of-2 with no arbitrator, solvable with a reputation system (implicit or constructed) or using 2-of-3 with current-state punish txs signable by arbitrator and built before participant punish txs are made.

It's likely that 2-of-3 would be mandatory for high value[+] transactions (mainchain has the same issue/solution and maybe 'take it there' for high value; but that would make channels more limited). No idea how LN/etc. handle this.

The current state update design favors the recipient of money transfers. An alternate arrangement that favors the recipient of goods (which may be less desirable, since vendors are more sensitive to reputation):
- LONG timeline Recover that pays out previous state but ties to current state Close
- Close
- Punish
- ...transaction...
- Recover

## tevador | 2026-07-22T06:36:04+00:00
> The partner may not want to close with the current state e.g. because the current state is a transfer of funds from them to the attacker but they did not receive the goods of an exchange yet.

The party receiving funds should sign Punish first. If the other party then refuses to sign, closing with the new state is favorable.

## UkoeHB | 2026-07-22T07:05:41+00:00
Don't think punish order matters.
- Fund-receiver misbehaves: ignore punish step entirely, just close-recover with the new favorable state before it's time to complete their side of the bargain.
- Fund-sender misbehaves: this guy wants to close the previous state after receiving goods, but can't because good-sending is always *after* they send a Punish (regardless of order).

## tevador | 2026-07-22T07:08:15+00:00
> I think you can hostage a channel by receiving a punish but refusing to send your own punish. If the partner tries to close + recover with the previous state, the attacker can just punish and take the funds. The partner may not want to close with the current state e.g. because the current state is a transfer of funds from them to the attacker but they did not receive the goods of an exchange yet. If favorable, the attacker can close + recover the current state.

I think overall it's a non-issue. The important fact is that a channel state update is atomic. The transfer of funds either occurs or does not occur. There is no way to make a crypto <-> physical goods transfer atomic.

Let me rephrase the "issue" with a traditional L1 payment:

*I think you can hostage a payment by waiting for the other party to send their transaction and then walking away. The payment is a transfer of funds from them to the attacker but they did not receive the goods of an exchange yet. If favorable, the attacker can run away with the money.*

> This is a pretty standard problem for 2-of-2 with no arbitrator, solvable with a reputation system (implicit or constructed) or using 2-of-3 with current-state punish txs signable by arbitrator and built before participant punish txs are made.

An arbitrator introduces a trust assumption. If both parties trust the arbitrator, there is no point in having a payment channel. The arbitrator can simply act as a bank via a 2-of-3 shared output. The main point of this proposal is to facilitate a payment channel protocol that doesn't rely on a trusted 3rd party.


## UkoeHB | 2026-07-22T16:34:38+00:00
> The main point of this proposal is to facilitate a payment channel protocol that doesn't rely on a trusted 3rd party.

I thought other major benefits were scaling and tx speed/throughput. High-speed, high-value, arbitrated payment channels may be valuable in the long run. Not saying it needs to be implemented, just considered as a potential solution/extension that could be implemented at some distant point. I don't *think* arbitrators need to be involved in state updates, they just provide material to set up the 2-of-3s then show up if there is a dispute (very rare).

## UkoeHB | 2026-07-22T16:37:30+00:00
> The party receiving funds should sign Punish first. If the other party then refuses to sign, closing with the new state is favorable.

I'll retract my dismissal. This is valuable if the receiving party becomes unresponsive (but is not misbehaving) after signing their Punish. The sending party can safely close the prior state without becoming disadvantaged. The only problem occurs with receiver-unresponsiveness after both have signed punish but before the receiver completed their ancillary transfer (the same as in the malicious-receiver case).

## tevador | 2026-07-22T16:59:36+00:00
> I thought other major benefits were scaling and tx speed/throughput.

Those are general benefits of payment channels. This proposal is about relative time-locks. There are payment channel proposals for Monero that don't need relative time-locks (e.g. Grease), but I think trustless payment channels are significantly better.

A payment channel protocol with a trusted third party (Charlie) is very simple:

### Opening a channel

Alice and Bob create a 2-of-3 Monero wallet using Charlie's public key as the third member. They then send their initial channel balances.

### Channel state update

Alice and Bob simply note that change in their balances. No cryptographic operations are needed.

### Collaborative close

If Alice and Bob both agree on their respective balances, they can simply sign a transaction to transfer funds from the channel to their own wallets.

### Disputed close

If Alice and Bob disagree, they can present their case to Charlie, who will take one side and sign the recovery transaction with them.

## UkoeHB | 2026-07-22T17:24:56+00:00
Ok yeah that makes sense.

Unrelated: this proposal should include sub-protocols for adding and removing funds (or comments that reconstructing the channel is required).

# Action History
- Created by: tevador | 2026-07-15T16:57:50+00:00
