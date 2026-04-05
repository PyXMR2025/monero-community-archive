---
title: '[seraphis_wallet]: key container'
source_url: https://github.com/seraphis-migration/monero/pull/5
author: ghostway0
assignees: []
labels: []
created_at: '2023-09-04T16:16:15+00:00'
updated_at: '2024-01-19T12:52:05+00:00'
type: pull_request
status: closed
closed_at: '2024-01-19T12:52:05+00:00'
merged_at: null
---

# Original Description
This is the key container class, its core finished, but some functionality is missing:
 - [ ] human readable representations
 - [ ] (optional) minimize time un-encrypted with KeyGuard (I have its implementation on an older commit locally I think)
 - [ ] and some more stuff that I don't necessarily remember now
 - [ ] more descriptive commits split by responsibility 
This PR includes:
- The key container
- A basic clang-format
- encrypted file for both key maps and also blobs (could be modified to use std::enable_if if wanted) and two basic tests
- encrypt/decrypt methods for jamtis_mock_keys (not necessarily up to standard)

# Discussion History
## DangerousFreedom1984 | 2023-09-06T12:21:00+00:00
I opened a PR with the .clang-format file as close as I could get to the seraphis_lib. Please use/modify that file when formatting.
I believe you can remove this file from the PR.

## DangerousFreedom1984 | 2023-09-06T12:43:45+00:00
Can you explain the main uses of these functions? Would that be used to store the keys on disk? If so, I believe we should not only use chacha but also argon2 (instead of the cn_fast_hash).

## DangerousFreedom1984 | 2023-09-06T12:52:22+00:00
1) Can you say a bit more about the security of the key container?
2) Since all private keys are crypto::secret_key = epee::mlocked<tools::scrubbed<ec_scalar>>, you are considering that they won't be swapped into memory, right? 
3) Is there any other caution that we should take?
4) What is the idea of the KeyGuard?

## ghostway0 | 2023-09-07T18:00:54+00:00
sure, will do that. thanks

## ghostway0 | 2023-09-07T18:01:56+00:00
yes they are
I don't have an opinion on that (not qualified), is this be a meeting type issue or can we just ask someone?

## ghostway0 | 2023-09-07T18:07:22+00:00
1. there's not much, I asked serhack and the only thing he told me was basically to encrypt stuff, iirc. also, I don't like these serialization structs because they are creating more copies of the keys (which then you should ask, should serialization be restricted to be done only encrypted?)
2. yep
3. we should ask, I didn't get any more responses
4. KeyGuard is there to minimize the time where the key container is left decrypted, the same way lock_guard handles things. when you pass a KeyGuard and it is copied, the ref count increases. when it reaches 0, the key container is encrypted again

## jeffro256 | 2023-09-07T20:06:49+00:00
As a general design decision, we probably shouldn't be making production code depend upon mock code. 

## rbrunner7 | 2023-09-10T07:50:45+00:00
This looks like a job for somebody to pick up: Write a class that is meant to be definit / permanent and replace this mock-only class, right? Maybe all that is needed is an exact one-to-one copy of that code, but in another file in another Seraphis-related folder.

Not sure whether this file crept into other, already existing parts of the Seraphis lib, and would need replacement there somehow as well.

## rbrunner7 | 2023-09-10T07:52:33+00:00
If I remember correctly this is just the way it works today. Can anybody point to some discussion where people argue something is in need of change or improvement here?

# Action History
- Created by: ghostway0 | 2023-09-04T16:16:15+00:00
- Closed at: 2024-01-19T12:52:05+00:00
