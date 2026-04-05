---
title: 'Guide: How to implement HW devices for Carrot/FCMP++ [WIP]'
source_url: https://github.com/seraphis-migration/monero/issues/63
author: jeffro256
assignees: []
labels: []
created_at: '2025-07-02T16:56:29+00:00'
updated_at: '2025-11-18T00:40:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# How to implement hardware wallet devices for Carrot/FCMP++

**NOTE: This guide is a work-in-progress. No HW devices have been developed for Carrot/FCMP++ yet. Right now, the latest development code, under the `fcmp++-stage` branch, has the ability to move to HW devices for spending, but it is not currently implemented. Successful development of HW device code for deployment will probably require interaction with either @jeffro256 or @j-berman**. 

## FCMP++/Carrot background

[FCMP++](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86) is the planned consensus upgrade to Monero that will replace ring signatures with a membership proof that enables an anonymity set of all historical Monero transaction outputs, ever. [Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md) is a *conditionally* quantum forward secret (among other features) addressing scheme for FCMP++ that is backwards compatible with existing Monero addresses. The Carrot spec also contains a recommended key derivation scheme that enables outgoing view keys (OVKs), *unconditionally* quantum forward secret self-sends, private address generation delegation, and more.

FCMP++ is short for "Full-Chain Membership Proofs + Spend Authorization + Linkability". FCMP++ proving can be split into two parts: "membership" and "spend-auth/linkability". FCMP proofs handle membership proving, while SA/L proofs handle spend-auth/linkability proving. Hardware wallet implementers only have to implement the SA/L proving code to protect private spend keys, not the FCMP proving code. This is in notable contrast to RingCT, which require HWs more or less have to validate and/or construct the entire ring signature. If HW wallets rely on live connected devices to handle FCMPs, the enotes which are being spent is revealed to the live connected device. In practice, this shouldn't be an issue since this is known anyways in almost all cases.

## Interactive construction / cold signing approaches for transaction construction

There are generally two distinct approaches used in the Monero core repo for constructing transactions with HW devices: "interactive construction" and "cold signing".

- *Interactive construction*: the live device "drives" the HW device to generate each component of the transaction according to user's needs. The HW device accumulates the state of the currently open transaction, displaying "driving information" to the HW user (addresses, amounts, etc). When it comes time to cryptographically sign the signatures, the HW device already knows the transaction message to bind to and generates a signature as such.
- *Cold signing*: the live device forms a "transaction proposal" at once, which can be used by any entity with the corresponding account keys to deterministically re-derive the "signable transaction hash". The live device sends the HW device this transaction proposal, and the HW device responds with signatures bound to the signable transaction hash.

You can see examples of "interactive construction" in the Monero codebase [here](https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/device/device_ledger.hpp#L252-L286) and [here](https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/device/device_ledger.cpp#L1436-L2358). Trezor also supports interactive construction for MLSAG and CLSAG transactions. You can see examples of "cold signing" in the Monero codebase [here](https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/device_trezor/device_trezor.cpp#L509-L691). At the time of writing, Ledger does not support a cold signing interface for RingCT transactions.

There are some pros and cons to each approach, but IMO, the only real pro for interactive construction is that small, iterative changes to the transaction format are easier to handle. Beyond that, cold signing can be designed to be stateless, which makes new large changes easier, easier to understand from a beginner, easier to verify soundness/correctness, and its flow is reusable for hot/cold wallet setups, which leads to less code duplication. Interactive construction also sometimes leads to difficulty for HW developers being able to re-derive transaction information correctly. See this [Ledger issue](https://github.com/LedgerHQ/app-monero/issues/66) open for over 5 years. _Because of this, the FCMP++/Carrot integration uses the cold signing approach towards HW transaction construction._

## FCMP++/Carrot HW interface architecture

Unlike the current `hw::device` interface (see [here](https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/device/device.hpp#L87)), the Carrot/FCMP++ HW device interface aims to be as modular as possible. For every single supported persistent private key, there is a distinct & compact interface. And  there is also a separate interface for generating signatures for transaction proposals.

### Scanning / address generation interfaces

- *view-balance secret* $s_{vb}$: https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/carrot_core/device.h#L140-L165
- *view-incoming key* $k_v$: https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/carrot_core/device.h#L104-L138
- *generate-address secret* $s_{ga}$: https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/carrot_core/device.h#L167-L181
- *generate-image key* $k_{gi}$, $k_s$: https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/carrot_core/device.h#L183-L194

However, if your flavor of HW does not need to support on-device refresh & address generation, then these implementations can largely be ignored in favor of exporting them to the live device. The one exception is the *generate-image key* device, assuming that the HW device maintains support for pre-Carrot addresses. Internally, this will use the private spend-key, which must remain on the HW. 

These key/secret-based interfaces are designed mainly to hide that specific key/secret, but not *derivations* using those keys. In other words, there is currently no analogue to `hw::device::conceal_derivation()` (see [here](https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/device/device.hpp#L174)) in the Carrot/FCMP++ HW device architecture. See [this comment](https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/carrot_core/device.h#L48-L58) for more details on this decision.

### Compound device interfaces

Some higher-level device interfaces can be composed from other smaller devices. For example, the `key_image_device` (see [here](https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/carrot_impl/key_image_device.h#L42-L50)) is a device which takes an "opening hint" (described below) and derives the key image for that enote. A composed implementation is provided [here](https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/carrot_impl/key_image_device_composed.h#L43-L58). Here you can see that this composed devices takes in 3 abstract devices: a "generate-image key device", a "hybrid hierarchy address device", a "view-balance secret device" (optional), and a "view-incoming key device" (optional). Generally, it is not required that the HW override these compound devices, as long as generation of account secrets and transaction components adheres to the standard. They are mainly there to provide ease-of-use to the live code.

### Transaction construction interface

#### `CarrotTransactionProposalV1`

https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/carrot_impl/tx_proposal.h#L59-L91

The `CarrotTransactionProposalv1` struct is the primary message used for communicating human-meaningful and computer-meaningful information about a transaction-to-be. Using just this struct plus account keys, one can derive the signable transaction hash for SA/L proofs: https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/carrot_impl/tx_builder_outputs.cpp#L129-L155

A HW wallet can also display destination address and amount information from the `normal_payment_proposals` and `selfsend_payment_proposals` fields so that human users can confirm transaction details.

The `input_proposals` field contains a list of "output opening hints". An output opening hint is information which allows a device with the private spend key with calculate $x, y$ such that $O = x G + y T$, where $O$ is some output public key. The knowledge of this relationship allows the HW device to sign a SA/L proof. Likewise, an output opening hint also informs a HW how to calculate the key image of $O$: $L = x * H_p(O)$, used in balance recovery.

#### `spend_device` 

https://github.com/seraphis-migration/monero/blob/f7e174c996c732f9b5cd5e39945aa566a0ddaadf/src/carrot_impl/spend_device.h#L44-L56

This device interface will be the main interface that HW devices must implement. It will contain a single function which takes in a `CarrotTransactionProposalv1`, "rerandomized outputs", and returns a set of SA/L proofs and the key images corresponding to the given inputs. It is the HW device's job to make sure the human user confirms the details of the `CarrotTransactionProposalv1` before performing the cryptographic operation of creating a SA/L proof. You can see how SA/L proofs are constructed from `CarrotTransactionProposalv1`s and in-memory private spend-keys in the `src/carrot_impl/tx_builder_inputs.cpp` file. Specifically for non-Carrot-keyed accounts (every user right now), this is the primary function: https://github.com/seraphis-migration/monero/blob/983106342f8265dc096505e952826809a219a532/src/carrot_impl/tx_builder_inputs.cpp#L179-L209

The base cryptographic code for SA/L proving can be found in @kayabaNerve's FCMP++ Rust crypto repository: https://github.com/kayabaNerve/fcmp-plus-plus/blob/cebfb4bdff0c34ead77ba3f1d4e5610e934c581f/networks/monero/ringct/fcmp%2B%2B/src/sal/mod.rs#L202-L253

As I understand it now, Ledger, Trezor, and Keystone wallets use C toolchains. As such, the proving code may have to be re-written in C. To my knowledge, there is not yet a C implementation for FCMP++ SA/L proving. Thankfully, SA/L proofs only uses arithmetic on Ed25519, unlike the FCMPs, which need arithmetic on Helios/Selene fields and points.

## Hybrid Legacy/Carrot key hierarchies

At some point, a HW implementer may want to support Carrot-keyed accounts to enable its [features](https://github.com/jeffro256/carrot/blob/master/carrot.md#22-new-wallets-only). However, a HW implementer might not want to force users to re-generate seeds and discard old addresses. A HW implementer also may not want their users to have to do double the scan work for balance recovery. In this case, they can opt for supporting a hybrid key hierarchy. If a HW's derivation path from seed to private spend key to private view key is amenable, then a HW can re-use the "legacy" view-incoming key, but generate new Carrot account secrets and addresses. These new addresses will support the OVKs, amongst other features. The old addresses will still be scannable, with the same amount of CPU effort, so no funds will be lost. The result of a good hybrid key hierarchy is that users will experience an (almost) seamless transaction to Carrot key hierarchy features for their *new* (not existing) addresses without having to lift a finger.

## Relationship Diagram

Hopefully, the following diagram can give a better overall picture of the device architecture. The "primitive" devices interfaces, representing operations on one piece of key material, are marked as diamonds. "Compound" device interfaces and implementations are marked with the document shape.

<img width="1661" height="1071" alt="Image" src="https://github.com/user-attachments/assets/bcdf9652-53fe-4c58-821c-6667feb42c13" />

In general, for the feature sets that a hardware device is targeting, it will need to implement the "primitive" device interfaces and the `spend_device` interface.

# Discussion History
# Action History
- Created by: jeffro256 | 2025-07-02T16:56:29+00:00
