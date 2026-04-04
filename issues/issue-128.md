---
title: Support fee bumping
source_url: https://github.com/monero-project/research-lab/issues/128
author: kayabaNerve
assignees: []
labels: []
created_at: '2024-11-28T20:01:17+00:00'
updated_at: '2025-08-04T13:08:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If a transaction is defined as a set of outputs and the associated wallet data, we don't have to sign the fee. Either the correct fee is specified or the transaction won't balance.

The inputs also don't have to refer to each other. Agreement on the first input is necessary to define an input context to prevent the burning bug, but the entire list isn't necessary unless we require sorted inputs. Even then, insertion of a new input only requires it have a higher ordinality key image than the first input.

If anyone can attach a new input, they can bump the fee. This requires either:
A) Input proofs not be done in aggregate
B) Usage of an IVC scheme so anyone can fold in an additional input's proof (though this would require the additional input be last in the list)

# Discussion History
## kayabaNerve | 2024-11-28T20:04:21+00:00
The input's amount commitment would need to have zero randomness which would make it obvious the transaction was bumped. Anyone would be able to bump any TX however.

## UkoeHB | 2024-11-28T20:17:00+00:00
This should be fine so long as no additional outputs are added to the tx. Input proofs need to sign the full output set.

## kayabaNerve | 2025-08-04T12:49:29+00:00
If we move to a non-key-binding Schnorr signature for our balance proof, bump inputs could have a non-zero randomness as they'd solely add to the existing response the randomness they contribute.

We just have the mess of the weaker binding, though the mined bumped TX would be indistinguishable from any other (except if we require the appended input have the highest ordinality key image, then the distribution of key images may be distinct?).

## kayabaNerve | 2025-08-04T13:08:41+00:00
We only require input SAL proofs not be done in aggregate. The membership proofs can still be aggregated (a performance requirement) so long as whoever bumps the fee knows the outputs spent and re-randomizations used.

# Action History
- Created by: kayabaNerve | 2024-11-28T20:01:17+00:00
