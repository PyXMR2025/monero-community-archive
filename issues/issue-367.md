---
title: '[beta] macOS GUI crashes while syncing wallet'
source_url: https://github.com/seraphis-migration/monero/issues/367
author: redsh4de
assignees: []
labels: []
created_at: '2026-05-09T02:10:49+00:00'
updated_at: '2026-05-10T14:44:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### Environment

- **OS:** macOS Tahoe 26.4
- **GUI:** v1.1 (beta)
- **Daemon:** v1.1 (beta)

Linux GUI works fine with the same seed & restore height (2997542), against the same remote daemon.

Issue appears to be macOS-specific.

### Behavior

The GUI crashes a few minutes in after opening a restored from seed wallet file, during FCMP++ tree sync initialization.
```
...
2026-05-09 02:05:30.317      0x16dae3000        INFO    wallet.wallet2  src/wallet/wallet2.cpp:3960     Found new pool tx: <fcf2dd186f5f7cc64631eb573852e65e2b787c8ce95da5b3e66c4c060b57ffff>
2026-05-09 02:05:30.317      0x16dae3000        INFO    wallet.wallet2  src/wallet/wallet2.cpp:3960     Found new pool tx: <46a277db260a5d5bbd5fd2d36eaf0e45804d4f8dc8bd26ffbe85e742b372ffff>
2026-05-09 02:05:30.398      0x16dae3000        INFO    wallet.wallet2  src/wallet/wallet2.cpp:3884     Initializing tree at block 2997541 with block hash <8a01bca03b85ff877187c023dc6851bedf817ddb29c394e3092ad65deb4bd1e5>
2026-05-09 02:05:30.402      0x16dae3000        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3272     Checking for reorg split point on block 2997541
2026-05-09 02:05:30.402      0x16dae3000        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3534     No reorg detected
2026-05-09 02:05:30.402      0x16dae3000        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3348     Start parsed block i to sync local hashchain: 0
2026-05-09 02:05:30.402      0x16dae3000        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3567     Processing parsed blocks, start_parsed_block_i: 0, parsed_blocks.size(): 286, start_height: 2997542, m_blockchain.size(): 2997542
2026-05-09 02:05:30.402      0x16dae3000        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3583     Starting tree sync, start_block_idx: 2997542, start_parsed_block_i: 0, prev_block_hash: <8a01bca03b85ff877187c023dc6851bedf817ddb29c394e3092ad65deb4bd1e5>
2026-05-09 02:05:30.403      0x17255f000        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3105     Requesting blocks starting on top of block hash <85c4f22e4733e1110d098f08954e76e96b8f37e38fded60b6e126b226be7874a>, n blocks synced: 2997542, init_tree_sync: 0
(GUI crash)
```
---

Trimmed GUI logs: https://pastebin.com/f9DQ90hU
Crash report: https://pastebin.com/ckZZjrvK

# Discussion History
## j-berman | 2026-05-09T03:09:43+00:00
The crashing thread is pretty surprising:

```
Thread 19 Crashed:
0   ???                           	              0x79 ???
1   monero-wallet-gui             	       0x102da99cc fcmp_pp::output_pubkey_cref(std::__1::variant<fcmp_pp::LegacyOutputPair, fcmp_pp::CarrotOutputPairV1> const&) + 72
2   monero-wallet-gui             	       0x102d9bea0 fcmp_pp::curve_trees::output_to_tuple(std::__1::variant<fcmp_pp::LegacyOutputPair, fcmp_pp::CarrotOutputPairV1> const&, bool) + 64
3   monero-wallet-gui             	       0x102da3ab8 0x102904000 + 4848312
4   monero-wallet-gui             	       0x102a1ac04 tools::threadpool::run(bool) + 604
5   libboost_thread.dylib         	       0x10487aa5c 0x104878000 + 10844
6   libsystem_pthread.dylib       	       0x186437c58 _pthread_start + 136
7   libsystem_pthread.dylib       	       0x186432c1c thread_start + 8
```

It seems like a memory issue, possibly with faulty serialization

## redsh4de | 2026-05-10T14:44:01+00:00
yeah, faulty serialization. comes down to libstdc++ (x86_64 daemon) and libc++ (ARM Mac wallet) storing `std::variant` differently - libstdc++ uses 1 byte for the variant's index, libc++ uses 4.

x86_64 daemon writes 1 byte for the index and leaves the next 3 bytes uninitialized. macOS wallet's libc++ reads all 4 as the index -> out-of-range value -> `std::visit` calls into random memory -> crash. matches the `output_pubkey_cref` frame in the trace.

I applied a local workaround on the Mac that zeroes those 3 bytes after receive in `wallet2::pull_and_parse_next_blocks`:

```cpp
const auto sanitize_variant_padding = [](fcmp_pp::UnifiedOutput &uo) {
  auto *p = reinterpret_cast<unsigned char *>(&uo);
  p[73] = p[74] = p[75] = 0;
};
for (auto &lo : init_tree_sync_data->locked_outputs)
  for (auto &uo : lo.outputs)
    sanitize_variant_padding(uo);
for (auto &uo : init_tree_sync_data->last_path.leaves)
  sanitize_variant_padding(uo);
```

i reckon this is the only `std::variant` bug because it's the only place we memcpy this type across the network - other variant usages are in-memory or go through serializers.

Replacing `std::variant` in `OutputPair` with a plain struct with a type field should fix it since both libs would lay it out identically, but maybe there's a cleaner fix

# Action History
- Created by: redsh4de | 2026-05-09T02:10:49+00:00
