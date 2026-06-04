---
title: Undefined behavior when decompression fails during ECDH
source_url: https://github.com/seraphis-migration/monero/issues/409
author: j-berman
assignees: []
labels: []
created_at: '2026-06-01T19:39:17+00:00'
updated_at: '2026-06-01T22:24:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If [these ECDH derivations fail](https://github.com/seraphis-migration/monero/blob/ff35f66f1f707264efaac370a395de249753a0ce/src/wallet/scanning_tools.cpp#L421-L446) (and they can fail if decompressing the pub key fails), behavior is undefined.

wallet2 currently sets the result derivation to identity in that case ([source](https://github.com/monero-project/monero/blob/f7e7d1da68a4a3f2a3c850349a6c0b1a5f74dfaa/src/wallet/wallet2.cpp#L2385-L2399)).

I don't have a strong opinion on a better solution here, but maybe it would be simplest to match wallet2's behavior here to simplify avoiding fingerprints (e.g. `monero-wallet` currently does the same as wallet2, so maintaining that behavior may simplify matching the behavior when integrating Carrot). A wallet that supports FCMP++/Carrot will already be fingerprinted as such when it's released, so there is no getting around that fingerprint.

Worth mentioning: when merging Carrot upstream, it would probably be good to do a comprehensive pass-through to see if the scanning impl matches wallet2's. There can be tricky edges to deal with (e.g. [pub tx key handling](https://github.com/UkoeHB/monero/issues/27), [payment ID handling](https://github.com/serai-dex/serai/pull/514)).

# Discussion History
## j-berman | 2026-06-01T19:48:01+00:00
Actually, we probably need to match wallet2's behavior here at least for legacy receives. Because wallet2 could identify these outputs as receives before, and such outputs would be spendable.

FWIW, we received a vuln report for this behavior in wallet2 that I personally think is not worth changing in wallet2 / not a vuln. The vuln report indicated that such an output would be detectable as a receive by anyone with the receiver's address. I don't think it's a vuln because it requires sender to do something malicious (use malformed tx pub key), and the sender can already use some publicly known randomness and we can't stop that to achieve the same thing.

# Action History
- Created by: j-berman | 2026-06-01T19:39:17+00:00
