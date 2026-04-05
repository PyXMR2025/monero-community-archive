---
title: 'Guide: How to play with Carrot/FCMP++ on a local testnet'
source_url: https://github.com/seraphis-migration/monero/issues/47
author: jeffro256
assignees: []
labels: []
created_at: '2025-05-16T22:16:46+00:00'
updated_at: '2025-06-13T17:13:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# How to play with Carrot/FCMP++ on a local testnet

## Compiling daemon, CLI wallet, & RPC wallet

1. Install normal Monero dependencies ([source](https://github.com/monero-project/monero?tab=readme-ov-file#dependencies))
 
2. Install Rust toolchain from https://rustup.rs/
 
3. Add `seraphis-migration` as a remote
 
If you already have a local monero repository:
```
git remote add seraphis-migration https://github.com/seraphis-migration/monero
```
Otherwise:
```
git clone https://github.com/seraphis-migration/monero
cd monero
```

4. Checkout the `fcmp++-stage` branch: `git checkout fcmp++-stage`

Make sure to check for updates here!

5. Update git submodules: `git submodule update --init`

6. Modify the testnet hardfork table by applying the following diff:

```diff
diff --git a/src/hardforks/hardforks.cpp b/src/hardforks/hardforks.cpp
index 571ba3818..faf24e733 100644
--- a/src/hardforks/hardforks.cpp
+++ b/src/hardforks/hardforks.cpp
@@ -78,28 +78,24 @@ const size_t num_mainnet_hard_forks = sizeof(mainnet_hard_forks) / sizeof(mainne
 const uint64_t mainnet_hard_fork_version_1_till = 1009826;
 
 const hardfork_t testnet_hard_forks[] = {
-  // version 1 from the start of the blockchain
-  { 1, 1, 0, 1341378000 },
-
-  // version 2 starts from block 624634, which is on or around the 23rd of November, 2015. Fork time finalised on 2015-11-20. No fork voting occurs for the v2 fork.
-  { 2, 624634, 0, 1445355000 },
-
-  // versions 3-5 were passed in rapid succession from September 18th, 2016
-  { 3, 800500, 0, 1472415034 },
-  { 4, 801219, 0, 1472415035 },
-  { 5, 802660, 0, 1472415036 + 86400*180 }, // add 5 months on testnet to shut the update warning up since there's a large gap to v6
-
-  { 6, 971400, 0, 1501709789 },
-  { 7, 1057027, 0, 1512211236 },
-  { 8, 1057058, 0, 1533211200 },
-  { 9, 1057778, 0, 1533297600 },
-  { 10, 1154318, 0, 1550153694 },
-  { 11, 1155038, 0, 1550225678 },
-  { 12, 1308737, 0, 1569582000 },
-  { 13, 1543939, 0, 1599069376 },
-  { 14, 1544659, 0, 1599069377 },
-  { 15, 1982800, 0, 1652727000 },
-  { 16, 1983520, 0, 1652813400 },
+  {  1,    1, 0, 1747401000 },
+  {  2,  200, 0, 1747402000 },
+  {  3,  300, 0, 1747403000 },
+  {  4,  400, 0, 1747404000 },
+  {  5,  500, 0, 1747405000 },
+  {  6,  600, 0, 1747406000 },
+  {  7,  700, 0, 1747407000 },
+  {  8,  800, 0, 1747408000 },
+  {  9,  900, 0, 1747409000 },
+  { 10, 1000, 0, 1747410000 },
+  { 11, 1100, 0, 1747411000 },
+  { 12, 1200, 0, 1747412000 },
+  { 13, 1300, 0, 1747413000 },
+  { 14, 1400, 0, 1747414000 },
+  { 15, 1500, 0, 1747415000 },
+  { 16, 1600, 0, 1747416000 },
+  { 17, 1700, 0, 1747417000 },
+  { 18, 1800, 0, 1747418000 },
 };
 const size_t num_testnet_hard_forks = sizeof(testnet_hard_forks) / sizeof(testnet_hard_forks[0]);
 const uint64_t testnet_hard_fork_version_1_till = 624633;
```

7. Choose a build type: `debug` or `release`. `debug` builds are many, many times slower than `release`, particularly when constructing transactions, but provide better debugging information when exceptions are thrown. If unsure, it can be a good idea to select `release` until you run into an issue, then switch to `debug`. Set an environmental variable for this decision:

`BUILD_TYPE=release` or `BUILD_TYPE=debug`

8. Compile: `make -j${nproc} $BUILD_TYPE`

9. If on Linux, the binaries can be found in the directory `./build/Linux/fcmp++-stage/$BUILD_TYPE/bin`

## Compiling GUI wallet

1. Install Monero GUI dependencies, mainly just the normal Monero dependencies plus Qt ([source](https://github.com/monero-project/monero-gui?tab=readme-ov-file#compiling-the-monero-gui-from-source))

2. Clone the `monero-gui` repo:
 
```
git clone --recursive https://github.com/monero-project/monero-gui
cd monero-gui
```

3.  Switch to the internal `monero` submodule: `cd monero`

4. Repeat steps 3-7 of "Compiling daemon, CLI wallet, & RPC wallet"

5. Switch to `monero-gui` root dir: `cd ..`

6. Compile with an `fcmp++-stage` submodule: `make -j${nproc} MANUAL_SUBMODULES=1 DEV_MODE=1 $BUILD_TYPE`

7. Binaries can be found in the `build` directory

## Running daemons

1. Set env variables for where `monerod` data should go: `MONERO_DIR=...`

2. Make that directory: `mkdir -p "$MONERO_DIR"`

3. Run daemon 1

```
./build/Linux/fcmp++-stage/$BUILD_TYPE/bin/monerod --testnet --fixed-difficulty 10 --no-igd --p2p-bind-port 18282 --rpc-bind-port 18182 --zmq-rpc-bind-port 18382 --zmq-pub tcp://127.0.0.1:18482 --non-interactive --disable-dns-checkpoints --check-updates disabled --rpc-ssl disabled --data-dir "$MONERO_DIR/monerod1" --log-level 2 --rpc-max-connections-per-private-ip 100 --rpc-max-connections 100 --add-exclusive-node 127.0.0.1:18283
```

4. Run daemon 2

```
./build/Linux/fcmp++-stage/$BUILD_TYPE/bin/monerod --testnet --fixed-difficulty 10 --no-igd --p2p-bind-port 18283 --rpc-bind-port 18183 --zmq-rpc-bind-port 18383 --zmq-pub tcp://127.0.0.1:18483 --non-interactive --disable-dns-checkpoints --check-updates disabled --rpc-ssl disabled --data-dir "$MONERO_DIR/monerod2" --log-level 2 --rpc-max-connections-per-private-ip 100 --rpc-max-connections 100 --add-exclusive-node 127.0.0.1:18282
```

As you can see in the hardfork table above, the block index for where each fork starts is 100 * X, where X is the fork number. The one exception is v1 which always starts at block index 1. So to activate FCMP++/Carrot (fork v17), you need to mine up to block 1700. With a fixed difficulty of 10 in the above CLI options, mining with multiple threads on my old-ish laptop takes less than a minute to reach 1800 (where pre-FCMP++ txs are disallowed). If you are *not* using a fixed difficulty, then it should take ~60 hours to reach that height (2 min/blk * 1800 blks / 60 min/hour). For a private testnet, I recommend fixed difficulty ;). If these fork values don't work for your private testnet, you can always adjust them to your liking.

## Using CLI/RPC/GUI wallet

You can run use these like normally, just remember to provide the `--testnet` flag for CLI and RPC. For GUI, select the "testnet" network type from the drop-down menu in "advanced settings". The daemon port should be either 18182 or 18183.

## Inspecting Carrot/FCMP++ transactions/blocks

The [onion blockchain explorer](https://github.com/moneroexamples/onion-monero-blockchain-explorer) has yet been updated for Carrot/FCMP++, so to inspect transactions and blocks, you can use the [`get_transactions`](https://docs.getmonero.org/rpc-library/monerod-rpc/#get_transactions) or [`get_block`](https://docs.getmonero.org/rpc-library/monerod-rpc/#get_block) RPC calls, respectively. The linked documentation provides example usage if you want a quick copy-and-paste usage. 


# Discussion History
## plowsof | 2025-06-13T07:18:46+00:00
have i missed a step? or must we mine up to a certain number of blocks first?

```
2025-06-13 07:08:26.321 I [127.0.0.1:58684 INC] calling /sendrawtransaction
2025-06-13 07:08:26.325 E Bulletproofs are not allowed before v8
2025-06-13 07:08:26.325 I transaction <eaaa794fa6216bc3cbc74a85a2b54b895b5fab656a9c3714312d9f11523f35e1> failed non-input consensus rule checks
2025-06-13 07:08:26.326 W [on_send_raw_tx]: tx verification failed: invalid output
```


## jeffro256 | 2025-06-13T17:07:04+00:00
> or must we mine up to a certain number of blocks first?

Yes. To reach fork vX, mine up to block index X * 100. So to get to v17, mine up to block index 1700. You can see the values in the hardfork table diff above. I'll add this information to the guide for clarity.

# Action History
- Created by: jeffro256 | 2025-05-16T22:16:46+00:00
