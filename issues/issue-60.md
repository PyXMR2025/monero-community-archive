---
title: Transaction proofs (InProofV1 and OutProofV1) have incomplete Schnorr challenges
source_url: https://github.com/monero-project/research-lab/issues/60
author: SarangNoether
assignees: []
labels: []
created_at: '2020-01-30T16:54:26+00:00'
updated_at: '2020-02-10T20:17:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It's possible to generate proofs for incoming and outgoing transactions of knowledge of either the transaction private key or the recipient private view key, using two-component Schnorr proofs. However, the challenge used in the proof [generation](https://github.com/monero-project/monero/blob/master/src/crypto/crypto.cpp#L323) and [verification](https://github.com/monero-project/monero/blob/master/src/crypto/crypto.cpp#L395) functions does not include all public proof parameters.

# Discussion History
## UkoeHB | 2020-01-31T20:44:04+00:00
EDIT: (moved to new issue)

## SarangNoether | 2020-01-31T20:46:05+00:00
This would almost certainly be separate functionality from the existing proof functions.

## SarangNoether | 2020-01-31T20:47:48+00:00
This issue specifically deals with the existing challenge construction, which is incomplete.

## UkoeHB | 2020-01-31T20:49:48+00:00
Ah, I can make a separate issue then. Thought this was about 'proofs about tx info' in general.

## SarangNoether | 2020-01-31T20:52:09+00:00
No worries. I'd prefer to keep it separate, to track the fix.

## SarangNoether | 2020-02-10T20:17:57+00:00
Addressed in https://github.com/monero-project/monero/pull/6329.

# Action History
- Created by: SarangNoether | 2020-01-30T16:54:26+00:00
