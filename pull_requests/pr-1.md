---
title: Initial tx history
source_url: https://github.com/seraphis-migration/monero/pull/1
author: DangerousFreedom1984
assignees: []
labels: []
created_at: '2023-06-06T20:15:48+00:00'
updated_at: '2023-10-25T20:56:45+00:00'
type: pull_request
status: closed
closed_at: '2023-10-25T20:56:45+00:00'
merged_at: null
---

# Original Description
(Still a draft as it needs a review, clean-up and it is failing the checks as it depends on @jeffro256's basic_wallet2 PR)

This PR contains the following:

#### Creation of Transaction History Component:
- It allows to efficiently look at transaction records by searching the txid of sent txs.
- The transaction records contains:
    - the key_images of sent enotes (so the enote_records can be easily recovered from the enote_store).
    - the JamtisPaymentProposals so the enote_ephemeral_private_key and destination addresses can be recovered.
- Created (de)serialization functions to the components of the class so they can be imported/exported.

#### Creation of Legacy knowledge proofs from the wallet side:
- Removed the node connection/wallet_keys and cache dependence using jeffro's lib (wallet2_basic)
- Created a demonstrator for the legacy_spend_proof and in_proof using jberman's scanner. 
- Unit_tests to fully test those functions may need to be implemented.

#### Creation of Seraphis knowledge proofs from the wallet side:
- All the seraphis knowledge proofs (except enote_unspent_proof as the practical side needs to be more explored (nodes and bc connection)) with unit tests
- Serialization is using base58 as do the legacy.

#### Creation of the show enotes functions to provide useful visualization of enotes and to be able to create the knowledge proofs:
- The idea is to filter the enotes by its spend/origin status and sort them by block/timestamp
- The filters and sorting can be easily fine tuned allowing many combinations to show/get the wanted enotes. 
- Wrote a demonstrator for that

### It creates/modifies the files:

#### encrypt_file.h (Temporary)
- Used to encrypt/decrypt and save/load SpTransactionStoreV1 to a file

#### legacy_knowledge_proofs.h
- Two ways of creating the legacy proofs are presented. 1) Using the wallet2_basic library from jeffro. 2) After re-scanning the blockchain and storing owned enotes in a seraphis form (using jberman demonstrator for example).
I prefer the first one since it allows to recover the tx_key necessary for tx_proof_out. [Here]() is a discussion about it.
- Unit_tests or functional tests still needs to be done (once we define the way to go)

#### sp_knowledge_proofs.h
- These functions should be really close to what the wallet CLI would call when asking for a proof.
- Added option to insert filename (which I think that is missing in current wallet) instead of overwriting existing proofs of same type.

#### serialization_types.h

- Make/Recover serializable structs used in the wallet (transaction_history, knowledge_proofs, ...)

#### transaction_history.h

- Contains SpTransactionStoreV1 which contains map by tx_id to TransactionRecordV1.
- TransactionRecordV1 contains 1) key_images of spent enotes in a tx (so almost all the information about the tx can be retrieved looking at the corresponding enote at the EnoteStore) and 2) JamtisPaymentProposals (so all other information like destination and enote_ephemeral_privkey can be retrieved).
- Functions to load (import) /save (export) TxHistory
- Functions to add entries to TxHistory from a transaction
- Functions to get enotes from a tx or last txs

#### show_enotes.h

- A series of filters and comparators to show enotes (and all its info) to users.
- Filters could be used to show transfers like today's command `show_transfers`.
- I believe all the information of an enote or transaction could be retrieved using the EnoteStore and TransactionHistory classes (and also some wallet information like the network which the wallet was opened).

#### transaction_utils.h

- Useful functions for transactions (like going from `JamtisDestination` to the string address (xmra1...))


----
#### New tasks and opened issues:
- How to store wallet data on files? Which functions to use? Separate key_container from the rest?
- How to implement knowledge proofs for hardware wallet devices (e.g., trezor)
- Implementation of mutex for thread safe access to enote_store, tx_store and keys (should be done one level above these functions, whenever the wallet call them)
- Decide how to show messages to user (same library as wallet2?)
- Decide which legacy knowledge scheme we want to move forward with
- Find a way to fully test the knowledge proofs (both legacy and seraphis) due to issues to the node connection. Create something similar to functional_tests?



# Discussion History
## UkoeHB | 2023-06-06T22:01:59+00:00
Can you do a proofreading pass on this PR for whitespace inconsistencies? This file is 2-space indentation, while other files in seraphis_wallet are 4-space indentation...

## DangerousFreedom1984 | 2023-06-07T08:10:10+00:00
Ok. I tried to create a [.clang-format file](https://github.com/DangerousFreedom1984/seraphis_lib/commit/69a0fdd8c41e0b318a619f95fed6972e4681a5f9) that mimics Seraphis style for those using VSCodium/VSCode. It should be better now. Though these specific files (encrypt_file.*) won't exist in the future probably. Also created another PR for that.

## rbrunner7 | 2023-06-07T16:42:59+00:00
See also here: https://github.com/seraphis-migration/strategy/wiki/Seraphis-Wallet-Coding-Conventions

## rbrunner7 | 2023-06-09T12:01:01+00:00
`ser_SpTransactionStoreV1` is a quite strange name.

It starts with a lowercase letter which looks quite strange to me.

It mixes two naming styles, using underscores to separate words, and camel case.

In the Seraphis library only few words within names are abbreviated, but here we have `ser` instead of `Serialized`.

I checked the "Serialization demo" files in the Seraphis library, and much to my surprise, that `ser_` prefix was used by @UkoeHB there. Still, with the naming in the library usually so systematic and well thought-out, I wonder whether this `ser_` is merely there because so far that code is only that, a **demo**.

## rbrunner7 | 2023-06-09T12:04:20+00:00
Usually those `FIELD` lines get indented 1 level, and that seems only logical to me: Technically `BEGIN_SERIALIZE_OBJECT()` expands to a method, and those `FIELD`s to statements within that method.

## UkoeHB | 2023-06-09T20:01:59+00:00
The `ser_` prefix is intentional as a kind of 'modifier. The rest of the name is a copy-paste of the original struct name.

## UkoeHB | 2023-06-09T20:02:56+00:00
Indenting does not improve readability here.

# Action History
- Created by: DangerousFreedom1984 | 2023-06-06T20:15:48+00:00
- Closed at: 2023-10-25T20:56:45+00:00
