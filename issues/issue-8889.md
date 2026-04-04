---
title: Bus error upon starting monerod on termux android 32-bit
source_url: https://github.com/monero-project/monero/issues/8889
author: k4r4b3y
assignees: []
labels:
- arm
- reproduction needed
- more info needed
created_at: '2023-06-02T13:51:56+00:00'
updated_at: '2025-08-26T16:26:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am trying to run a monero node on my android. The hardware is Samsung Galaxy J7 Pro (SM-J730F). I installed Termux from Fdroid. With in termux, I check the system architecture:
```
[u0_a197@localhost]:~ % uname -m
armv8l
[u0_a197@localhost]:~ %
```
Accordingly, I download the `monero-android-armv7-v0.18.2.2.tar.bz2` package, and use the monerod in it:
```
[u0_a197@localhost]:~ % ./monero-cli/monero-cli/monerod --config-file monero-cli/config/config.txt
2023-06-02 13:41:40.619 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-06-02 13:41:40.619 I Initializing cryptonote protocol...
2023-06-02 13:41:40.619 I Cryptonote protocol initialized OK
2023-06-02 13:41:40.622 I Initializing core...
2023-06-02 13:41:40.623 I Loading blockchain from folder /data/data/com.termux/files/home/storage/external-1/bitmonero/lmdb ...
2023-06-02 13:41:40.722 I Loading checkpoints
2023-06-02 13:41:40.722 I Core initialized OK
2023-06-02 13:41:40.722 I Initializing p2p server...
2023-06-02 13:41:40.724 I p2p server initialized OK
2023-06-02 13:41:40.725 I Initializing core RPC server...
2023-06-02 13:41:40.725 I Binding on 127.0.0.1 (IPv4):18081
2023-06-02 13:41:40.727 I core RPC server initialized OK on port: 18081
2023-06-02 13:41:40.728 I Initializing restricted RPC server...
2023-06-02 13:41:40.728 I Binding on 0.0.0.0 (IPv4):18089
2023-06-02 13:41:50.068 I restricted RPC server initialized OK on port: 18089
2023-06-02 13:41:50.068 I Starting core RPC server...
2023-06-02 13:41:50.069 I core RPC server started ok
2023-06-02 13:41:50.070 I Starting restricted RPC server...
2023-06-02 13:41:50.070 I restricted RPC server started ok
2023-06-02 13:41:50.071 I Starting p2p net loop...
2023-06-02 13:41:51.073 I
2023-06-02 13:41:51.073 I **********************************************************************
2023-06-02 13:41:51.073 I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-06-02 13:41:51.074 I
2023-06-02 13:41:51.074 I You can set the level of process detailization through "set_log <level|categories>" command,
2023-06-02 13:41:51.074 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-06-02 13:41:51.074 I
2023-06-02 13:41:51.074 I Use the "help" command to see the list of available commands.
2023-06-02 13:41:51.074 I Use "help <command>" to see a command's documentation.
2023-06-02 13:41:51.075 I **********************************************************************
zsh: bus error  ./monero-cli/monero-cli/monerod --config-file monero-cli/config/config.txt
[u0_a197@localhost]:~ % 
```

Is there a way to resolve this?

# Discussion History
## hyc | 2023-06-02T14:06:32+00:00
An armv8l system should be using 64bit binaries.

## k4r4b3y | 2023-06-02T14:09:50+00:00
I remember trying 64-bit binaries first. And they didn't work. But let me try again, and come back with some logs.


## k4r4b3y | 2023-06-02T18:18:29+00:00
@hyc I am getting "no such file or directory" error:

```
[u0_a187@localhost]:~ % tar jxvf androidarm8
monero-aarch64-linux-android-v0.18.2.2/
monero-aarch64-linux-android-v0.18.2.2/ANONYMITY_NETWORKS.md
monero-aarch64-linux-android-v0.18.2.2/LICENSE
monero-aarch64-linux-android-v0.18.2.2/monero-blockchain-ancestry
monero-aarch64-linux-android-v0.18.2.2/monero-blockchain-depth
monero-aarch64-linux-android-v0.18.2.2/monero-blockchain-export
monero-aarch64-linux-android-v0.18.2.2/monero-blockchain-import
monero-aarch64-linux-android-v0.18.2.2/monero-blockchain-mark-spent-outputs
monero-aarch64-linux-android-v0.18.2.2/monero-blockchain-prune
monero-aarch64-linux-android-v0.18.2.2/monero-blockchain-prune-known-spent-data
monero-aarch64-linux-android-v0.18.2.2/monero-blockchain-stats
monero-aarch64-linux-android-v0.18.2.2/monero-blockchain-usage
monero-aarch64-linux-android-v0.18.2.2/monerod
monero-aarch64-linux-android-v0.18.2.2/monero-gen-ssl-cert
monero-aarch64-linux-android-v0.18.2.2/monero-gen-trusted-multisig
monero-aarch64-linux-android-v0.18.2.2/monero-wallet-cli
monero-aarch64-linux-android-v0.18.2.2/monero-wallet-rpc
monero-aarch64-linux-android-v0.18.2.2/README.md
[u0_a187@localhost]:~ % cd monero-aarch64-linux-android-v0.18.2.2
[u0_a187@localhost]:~/monero-aarch64-linux-android-v0.18.2.2 % l
total 260M
drwx------  2 u0_a187 u0_a187 4.0K Apr  3 03:53 .
drwx------ 16 u0_a187 u0_a187 4.0K Jun  2 21:13 ..
-rw-------  1 u0_a187 u0_a187 9.9K Apr  3 03:53 ANONYMITY_NETWORKS.md
-rw-------  1 u0_a187 u0_a187 2.7K Apr  3 03:53 LICENSE
-rw-------  1 u0_a187 u0_a187  46K Apr  3 03:53 README.md
-rwx------  1 u0_a187 u0_a187  18M Apr  3 03:53 monero-blockchain-ancestry
-rwx------  1 u0_a187 u0_a187  17M Apr  3 03:53 monero-blockchain-depth
-rwx------  1 u0_a187 u0_a187  17M Apr  3 03:53 monero-blockchain-export
-rwx------  1 u0_a187 u0_a187  17M Apr  3 03:53 monero-blockchain-import
-rwx------  1 u0_a187 u0_a187  13M Apr  3 03:53 monero-blockchain-mark-spent-outputs
-rwx------  1 u0_a187 u0_a187  17M Apr  3 03:53 monero-blockchain-prune
-rwx------  1 u0_a187 u0_a187  17M Apr  3 03:53 monero-blockchain-prune-known-spent-data
-rwx------  1 u0_a187 u0_a187  17M Apr  3 03:53 monero-blockchain-stats
-rwx------  1 u0_a187 u0_a187  17M Apr  3 03:53 monero-blockchain-usage
-rwx------  1 u0_a187 u0_a187  13M Apr  3 03:53 monero-gen-ssl-cert
-rwx------  1 u0_a187 u0_a187  25M Apr  3 03:53 monero-gen-trusted-multisig
-rwx------  1 u0_a187 u0_a187  26M Apr  3 03:53 monero-wallet-cli
-rwx------  1 u0_a187 u0_a187  26M Apr  3 03:53 monero-wallet-rpc
-rwx------  1 u0_a187 u0_a187  28M Apr  3 03:53 monerod
[u0_a187@localhost]:~/monero-aarch64-linux-android-v0.18.2.2 % ./monerod
zsh: no such file or directory: ./monerod
zsh: exit 127   ./monerod
[u0_a187@localhost]:~/monero-aarch64-linux-android-v0.18.2.2 % file ./monerod
./monerod: ELF 64-bit LSB shared object, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /system/bin/linker64, with debug_info, not stripped
[u0_a187@localhost]:~/monero-aarch64-linux-android-v0.18.2.2 %
```

File not found, error is quite confusing as I can see the file is right there in the same folder as my current working directory..

## selsta | 2023-06-06T01:06:49+00:00
Does `/system/bin/linker64` exist on your system? Are you using the latest version of termux?

## k4r4b3y | 2023-06-06T13:43:40+00:00
@selsta I am on Termux v0.118.0 installed from fdroid. This is currently the latest version.

>Does `/system/bin/linker64` exist on your system?

Under `$PREFIX/bin` there is only a binary named `clang-linker-wrapper`. How else can I check for the existence of `linker64` ?

## selsta | 2023-06-06T13:51:32+00:00
Which Android version are you using? Is it a custom ROM?

https://android.googlesource.com/platform/bionic/+/2aebf5429bb1241a3298b5b642d38f73124c2026/HACKING.txt

According to this `/system/bin/linker64` should exist on all 64bit Android systems.

## selsta | 2023-06-06T13:58:13+00:00
`/system/bin` is not the same as `$PREFIX/bin`, though I'm not sure if you can even access that with Termux.

## k4r4b3y | 2023-06-06T13:58:24+00:00
>Which Android version are you using? Is it a custom ROM?

The hardware is Galaxy J7 Pro (SM-J730F) running Android 9. It is not a custom ROM. It runs whatever Samsung distributes it with.

>According to this /system/bin/linker64 should exist on all 64bit Android systems.

My bad with my previous reply. I now have cd'ed into `/system/bin` dir. `ls -la linker*` command returns a binary named `linker`. 

## selsta | 2023-06-06T14:00:36+00:00
It seems like you are running a 32bit version of Android with a 64bit CPU.

## k4r4b3y | 2023-06-06T14:01:32+00:00
@selsta that is my impression, too. And thus I have tried installing the androidarm7 in my OP.

## MarcusNewman | 2023-06-07T04:58:08+00:00
I noticed the armv7 tar says arm but the armv8 tar says aarch64 Linux. Are those the right files?

## k4r4b3y | 2023-06-07T08:53:15+00:00
@MarcusNewman I confirm your observation. Extracting the androidarm8 file results in `monero-aarch64-linux-android-v0.18.2.2`. However, I believe this is still OK, as androidarm8 are basically 64-bit CPU stuff and thus should be compatible with termux running on an (expected) 64-bit OS (as I was trying in my post: https://github.com/monero-project/monero/issues/8889#issuecomment-1574135307 ). So I don't think there is an error on my part there. 

## selsta | 2023-06-07T10:28:47+00:00
> I noticed the armv7 tar says arm but the armv8 tar says aarch64 Linux. Are those the right files?

Yes.

>However, I believe this is still OK, as androidarm8 are basically 64-bit CPU stuff and thus should be compatible with termux running on an (expected) 64-bit OS (as I was trying in my post: https://github.com/monero-project/monero/issues/8889#issuecomment-1574135307 ).

Can you clarify here? Didn't you say you run a 32bit OS in a previous comment?

## k4r4b3y | 2023-06-07T10:31:11+00:00
>Can you clarify here? Didn't you say you run a 32bit OS in a previous comment?

Yes I run a 32bit OS. However as @hyc has said in his comment, "I should be running 64-bit binaries for monerod", and then, I went ahead and re-tried the androidarm8 binaries. That's what I was talking about there.

## selsta | 2023-06-07T13:39:19+00:00
Can you start with --log-level 4 and share the output?

## k4r4b3y | 2023-06-07T18:35:46+00:00
@selsta here it is:
```
~/monero-cli/monero-cli $ ./monerod --config-file /data/data/com.termux/files/home/storage/shared/crypto/monero-cli/config/config.txt --log-level 4
2023-06-07 18:28:01.869 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-06-07 18:28:01.870 I Moving from main() into the daemonize now.
2023-06-07 18:28:01.870 I Initializing cryptonote protocol...
2023-06-07 18:28:01.870 I Cryptonote protocol initialized OK
2023-06-07 18:28:01.873 T Blockchain::Blockchain
2023-06-07 18:28:01.874 I Initializing core...
2023-06-07 18:28:01.875 T BlockchainLMDB::BlockchainLMDB
2023-06-07 18:28:01.876 T BlockchainLMDB::get_db_name
2023-06-07 18:28:01.876 I Loading blockchain from folder /data/data/com.termux/files/home/storage/external-1/bitmonero/lmdb ...
2023-06-07 18:28:01.876 D option: fast
2023-06-07 18:28:01.876 D option: async
2023-06-07 18:28:01.877 D option: 1000000
2023-06-07 18:28:01.877 T BlockchainLMDB::open
2023-06-07 18:28:01.878 T BlockchainLMDB::need_resize
2023-06-07 18:28:01.878 D DB map size:     2147483648
2023-06-07 18:28:01.878 D Space used:      81920
2023-06-07 18:28:01.878 D Space remaining: 2147401728
2023-06-07 18:28:01.878 D Size threshold:  0
2023-06-07 18:28:01.879 D Percent used: 0.0038  Percent threshold: 90.0000
2023-06-07 18:28:01.879 D Setting m_height to: 1
2023-06-07 18:28:01.879 T mdb_txn_safe: destructor
2023-06-07 18:28:01.879 T Blockchain::init
2023-06-07 18:28:01.879 T BlockchainLMDB::height
2023-06-07 18:28:01.879 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:01.880 T mdb_txn_safe: destructor
2023-06-07 18:28:01.880 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:01.880 T mdb_txn_safe: destructor
2023-06-07 18:28:01.880 T BlockchainLMDB::height
2023-06-07 18:28:01.880 T BlockchainLMDB::height
2023-06-07 18:28:01.880 T BlockchainLMDB::get_block_blob_from_height
2023-06-07 18:28:01.880 T BlockchainLMDB::height
2023-06-07 18:28:01.881 T BlockchainLMDB::height
2023-06-07 18:28:01.881 T BlockchainLMDB::get_hard_fork_version
2023-06-07 18:28:01.881 T BlockchainLMDB::height
2023-06-07 18:28:01.881 T BlockchainLMDB::block_rtxn_stop
2023-06-07 18:28:01.882 D init done
2023-06-07 18:28:01.882 T BlockchainLMDB::height
2023-06-07 18:28:01.882 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:01.882 T mdb_txn_safe: destructor
2023-06-07 18:28:01.882 T BlockchainLMDB::fixup
2023-06-07 18:28:01.882 T BlockchainLMDB::set_batch_transactions
2023-06-07 18:28:01.882 I batch transaction mode already enabled, but asked to enable batch mode
2023-06-07 18:28:01.883 I batch transactions enabled
2023-06-07 18:28:01.883 T BlockchainLMDB::batch_start
2023-06-07 18:28:01.883 T BlockchainLMDB::check_and_resize_for_batch
2023-06-07 18:28:01.883 T [check_and_resize_for_batch] checking DB size
2023-06-07 18:28:01.883 T BlockchainLMDB::need_resize
2023-06-07 18:28:01.883 D DB map size:     2147483648
2023-06-07 18:28:01.883 D Space used:      81920
2023-06-07 18:28:01.883 D Space remaining: 2147401728
2023-06-07 18:28:01.883 D Size threshold:  0
2023-06-07 18:28:01.884 D Percent used: 0.0038  Percent threshold: 90.0000
2023-06-07 18:28:01.884 T batch transaction: begin
2023-06-07 18:28:01.884 T BlockchainLMDB::get_block_hash_from_height
2023-06-07 18:28:01.884 T BlockchainLMDB::height
2023-06-07 18:28:01.884 T BlockchainLMDB::height
2023-06-07 18:28:01.884 T BlockchainLMDB::batch_stop
2023-06-07 18:28:01.884 T batch transaction: committing...
2023-06-07 18:28:01.884 T mdb_txn_safe: destructor
2023-06-07 18:28:01.884 T batch transaction: end
2023-06-07 18:28:01.885 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:01.885 T mdb_txn_safe: destructor
2023-06-07 18:28:01.885 T BlockchainLMDB::get_top_block_timestamp
2023-06-07 18:28:01.885 T BlockchainLMDB::height
2023-06-07 18:28:01.885 T BlockchainLMDB::get_block_timestamp
2023-06-07 18:28:01.885 I Loading precomputed blocks (356356 bytes)
2023-06-07 18:28:01.886 I precomputed blocks hash: <2c95b5af1f3ee41893ae0c585fd59207a40f28ed4addbaad64a46a39b82955e7>, expected 2c95b5af1f3ee41893ae0c585fd59207a40f28ed4addbaad64a46a39b82955e7
2023-06-07 18:28:01.886 T BlockchainLMDB::height
2023-06-07 18:28:02.059 I 5568 block hashes loaded
2023-06-07 18:28:02.059 T BlockchainLMDB::get_txpool_tx_count
2023-06-07 18:28:02.060 T BlockchainLMDB::for_all_txpool_txes
2023-06-07 18:28:02.060 T BlockchainLMDB::height
2023-06-07 18:28:02.060 T Blockchain initialized. last block: 0, d3337.h7.m39.s8 time ago, current difficulty: Blockchain::get_difficulty_for_next_block
2023-06-07 18:28:02.060 T BlockchainLMDB::height
2023-06-07 18:28:02.060 T Blockchain::get_tail_id
2023-06-07 18:28:02.060 T BlockchainLMDB::top_block_hash
2023-06-07 18:28:02.060 T BlockchainLMDB::height
2023-06-07 18:28:02.060 T BlockchainLMDB::get_block_hash_from_height
2023-06-07 18:28:02.060 T Blockchain::get_tail_id
2023-06-07 18:28:02.061 T BlockchainLMDB::top_block_hash
2023-06-07 18:28:02.061 T BlockchainLMDB::height
2023-06-07 18:28:02.061 T BlockchainLMDB::get_block_hash_from_height
2023-06-07 18:28:02.061 I 1
2023-06-07 18:28:02.061 T BlockchainLMDB::block_rtxn_stop
2023-06-07 18:28:02.061 T BlockchainLMDB::top_block_hash
2023-06-07 18:28:02.061 T BlockchainLMDB::height
2023-06-07 18:28:02.061 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:02.061 T mdb_txn_safe: destructor
2023-06-07 18:28:02.061 T BlockchainLMDB::get_block_hash_from_height
2023-06-07 18:28:02.061 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:02.062 T mdb_txn_safe: destructor
2023-06-07 18:28:02.062 T BlockchainLMDB::get_top_block
2023-06-07 18:28:02.062 T BlockchainLMDB::height
2023-06-07 18:28:02.062 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:02.062 T mdb_txn_safe: destructor
2023-06-07 18:28:02.062 T BlockchainLMDB::get_block_blob_from_height
2023-06-07 18:28:02.062 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:02.062 T mdb_txn_safe: destructor
2023-06-07 18:28:02.062 T BlockchainLMDB::height
2023-06-07 18:28:02.062 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:02.062 T mdb_txn_safe: destructor
2023-06-07 18:28:02.063 T BlockchainLMDB::block_wtxn_start
2023-06-07 18:28:02.063 T Blockchain::update_next_cumulative_weight_limit
2023-06-07 18:28:02.063 T BlockchainLMDB::height
2023-06-07 18:28:02.063 T Blockchain::get_last_n_blocks_weights
2023-06-07 18:28:02.064 T BlockchainLMDB::height
2023-06-07 18:28:02.064 T BlockchainLMDB::get_block_info_64bit_fields
2023-06-07 18:28:02.064 T BlockchainLMDB::height
2023-06-07 18:28:02.064 T BlockchainLMDB::add_max_block_size
2023-06-07 18:28:02.064 T BlockchainLMDB::block_wtxn_stop
2023-06-07 18:28:02.064 T mdb_txn_safe: destructor
2023-06-07 18:28:02.064 T BlockchainLMDB::for_all_txpool_txes
2023-06-07 18:28:02.064 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:02.065 T mdb_txn_safe: destructor
2023-06-07 18:28:02.065 T BlockchainLMDB::for_all_txpool_txes
2023-06-07 18:28:02.065 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:02.065 T mdb_txn_safe: destructor
2023-06-07 18:28:02.065 I Validating txpool contents for v1
2023-06-07 18:28:02.065 T BlockchainLMDB::batch_start
2023-06-07 18:28:02.066 T BlockchainLMDB::check_and_resize_for_batch
2023-06-07 18:28:02.066 T [check_and_resize_for_batch] checking DB size
2023-06-07 18:28:02.066 T BlockchainLMDB::need_resize
2023-06-07 18:28:02.066 D DB map size:     2147483648
2023-06-07 18:28:02.066 D Space used:      81920
2023-06-07 18:28:02.066 D Space remaining: 2147401728
2023-06-07 18:28:02.066 D Size threshold:  0
2023-06-07 18:28:02.066 D Percent used: 0.0038  Percent threshold: 90.0000
2023-06-07 18:28:02.066 T batch transaction: begin
2023-06-07 18:28:02.066 T BlockchainLMDB::for_all_txpool_txes
2023-06-07 18:28:02.066 T BlockchainLMDB::batch_stop
2023-06-07 18:28:02.067 T batch transaction: committing...
2023-06-07 18:28:02.067 T mdb_txn_safe: destructor
2023-06-07 18:28:02.067 T batch transaction: end
2023-06-07 18:28:02.067 I Loading checkpoints
2023-06-07 18:28:02.067 T BlockchainLMDB::drop_alt_blocks
2023-06-07 18:28:02.067 T mdb_txn_safe: destructor
2023-06-07 18:28:02.067 T BlockchainLMDB::get_blockchain_pruning_seed
2023-06-07 18:28:02.067 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:02.067 T mdb_txn_safe: destructor
2023-06-07 18:28:02.067 T BlockchainLMDB::prune_worker
2023-06-07 18:28:02.068 I Pruning blockchain...
2023-06-07 18:28:02.068 T BlockchainLMDB::height
2023-06-07 18:28:02.068 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:02.068 T mdb_txn_safe: destructor
2023-06-07 18:28:02.068 I Pruned blockchain in 0 ms: 0 MB (0 MB) pruned in 0 records (0/1 4096 byte pages), 0/0 pruned records
2023-06-07 18:28:02.068 T mdb_txn_safe: destructor
2023-06-07 18:28:02.068 I Core initialized OK
2023-06-07 18:28:02.068 I Initializing p2p server...
2023-06-07 18:28:02.069 T Blockchain::get_current_blockchain_height
2023-06-07 18:28:02.070 T BlockchainLMDB::height
2023-06-07 18:28:02.070 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:02.070 T mdb_txn_safe: destructor
2023-06-07 18:28:02.070 D Found 0 out connections having height >= 1
2023-06-07 18:28:02.071 I Setting LIMIT: 1.04858e+06 kbps
2023-06-07 18:28:02.072 I Set limit-up to 1048576 kB/s
2023-06-07 18:28:02.072 I Setting LIMIT: 1.04858e+06 kbps
2023-06-07 18:28:02.072 I Setting LIMIT: 1.04858e+06 kbps
2023-06-07 18:28:02.072 I Set limit-down to 1048576 kB/s
2023-06-07 18:28:02.073 I Set server type to: 2 from name: P2P, prefix_name = P2P
2023-06-07 18:28:02.073 I Binding (IPv4) on 0.0.0.0:18080
2023-06-07 18:28:02.073 D start accept (IPv4)
2023-06-07 18:28:02.074 D Spawned connection #0 to 0.0.0.0 currently we have sockets count:1
2023-06-07 18:28:02.075 I Net service bound (IPv4) to 0.0.0.0:18080
2023-06-07 18:28:02.075 I p2p server initialized OK
2023-06-07 18:28:02.075 I Initializing core RPC server...
2023-06-07 18:28:02.075 I Set server type to: 1 from name: RPC, prefix_name = RPC
2023-06-07 18:28:02.076 I Binding on 127.0.0.1 (IPv4):18081
2023-06-07 18:28:02.077 D start accept (IPv4)
2023-06-07 18:28:02.078 D Spawned connection #0 to 0.0.0.0 currently we have sockets count:1
2023-06-07 18:28:02.078 I core RPC server initialized OK on port: 18081
2023-06-07 18:28:02.078 I Initializing restricted RPC server...
2023-06-07 18:28:02.078 I Set server type to: 1 from name: RPC, prefix_name = RPC
2023-06-07 18:28:02.079 W The RPC server is accessible from the outside, but no RPC payment was setup. RPC access will be free for all.
2023-06-07 18:28:02.079 I Binding on 0.0.0.0 (IPv4):18089
2023-06-07 18:28:02.080 I Generating SSL certificate
2023-06-07 18:28:09.429 D start accept (IPv4)
2023-06-07 18:28:09.429 D Spawned connection #0 to 0.0.0.0 currently we have sockets count:1
2023-06-07 18:28:09.429 I restricted RPC server initialized OK on port: 18089
2023-06-07 18:28:09.429 I Starting core RPC server...
2023-06-07 18:28:09.430 I Run net_service loop( 2 threads)...
2023-06-07 18:28:09.430 D Run server thread name: RPC
2023-06-07 18:28:09.430 D Run server thread name: RPC
2023-06-07 18:28:09.431 D Reiniting OK.
2023-06-07 18:28:09.431 I core RPC server started ok
2023-06-07 18:28:09.431 I Starting restricted RPC server...
2023-06-07 18:28:09.431 I Run net_service loop( 2 threads)...
2023-06-07 18:28:09.431 D Run server thread name: RPC
2023-06-07 18:28:09.431 D Run server thread name: RPC
2023-06-07 18:28:09.431 D Reiniting OK.
2023-06-07 18:28:09.431 I restricted RPC server started ok
2023-06-07 18:28:09.433 I ZMQ server disabled
2023-06-07 18:28:09.433 I Starting p2p net loop...
2023-06-07 18:28:09.433 I Run net_service loop( 10 threads)...
2023-06-07 18:28:09.433 D Thread monitor number of peers - start
2023-06-07 18:28:09.433 D Starting new Dandelion++ epoch: stem
2023-06-07 18:28:09.434 D Run server thread name: P2P
2023-06-07 18:28:09.434 D Run server thread name: P2P
2023-06-07 18:28:09.434 D Run server thread name: P2P
2023-06-07 18:28:09.435 D Run server thread name: P2P
2023-06-07 18:28:09.435 D Run server thread name: P2P
2023-06-07 18:28:09.435 D Run server thread name: P2P
2023-06-07 18:28:09.435 D Run server thread name: P2P
2023-06-07 18:28:09.435 D Run server thread name: P2P
2023-06-07 18:28:09.436 D Run server thread name: P2P
2023-06-07 18:28:09.436 D Run server thread name: P2P
2023-06-07 18:28:09.436 D JOINING all threads
2023-06-07 18:28:10.434 D STARTED PEERLIST IDLE HANDSHAKE
2023-06-07 18:28:10.436 T Checking for idle peers...
2023-06-07 18:28:10.436 T Blockchain::get_current_blockchain_height
2023-06-07 18:28:10.436 T BlockchainLMDB::height
2023-06-07 18:28:10.437 D FINISHED PEERLIST IDLE HANDSHAKE
2023-06-07 18:28:10.437 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:10.437 T mdb_txn_safe: destructor
2023-06-07 18:28:10.438 T Checking for outgoing syncing peers...
2023-06-07 18:28:10.438 D dns_threads[0] created for: seeds.moneroseeds.se
2023-06-07 18:28:10.439 I
2023-06-07 18:28:10.439 I **********************************************************************
2023-06-07 18:28:10.439 I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-06-07 18:28:10.440 I
2023-06-07 18:28:10.440 I You can set the level of process detailization through "set_log <level|categories>" command,
2023-06-07 18:28:10.440 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-06-07 18:28:10.441 I
2023-06-07 18:28:10.441 I Use the "help" command to see the list of available commands.
2023-06-07 18:28:10.441 I Use "help <command>" to see a command's documentation.
2023-06-07 18:28:10.441 I **********************************************************************
2023-06-07 18:28:10.442 T BlockchainLMDB::batch_start
2023-06-07 18:28:10.442 T BlockchainLMDB::check_and_resize_for_batch
2023-06-07 18:28:10.442 T [check_and_resize_for_batch] checking DB size
2023-06-07 18:28:10.443 T BlockchainLMDB::need_resize
2023-06-07 18:28:10.443 D DB map size:     2147483648
2023-06-07 18:28:10.443 D dns_threads[2] created for: seeds.moneroseeds.ch
2023-06-07 18:28:10.444 D dns_threads[1] created for: seeds.moneroseeds.ae.org
2023-06-07 18:28:10.444 D dns_threads created, now waiting for completion or timeout of 20000ms
2023-06-07 18:28:10.445 I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5
2023-06-07 18:28:10.445 D Space used:      81920
2023-06-07 18:28:10.446 D Space remaining: 2147401728
2023-06-07 18:28:10.446 I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D
2023-06-07 18:28:10.446 D Performing DNSSEC TXT record query for updates.moneropulse.org
2023-06-07 18:28:10.447 D Size threshold:  0
2023-06-07 18:28:10.447 D dns_threads[3] created for: seeds.moneroseeds.li
2023-06-07 18:28:10.448 D Percent used: 0.0038  Percent threshold: 90.0000
2023-06-07 18:28:10.448 T batch transaction: begin
2023-06-07 18:28:10.448 T BlockchainLMDB::get_txpool_tx_count
2023-06-07 18:28:10.449 T BlockchainLMDB::for_all_txpool_txes
2023-06-07 18:28:10.449 T BlockchainLMDB::batch_abort
2023-06-07 18:28:10.449 T mdb_txn_safe: abort()
2023-06-07 18:28:10.449 T mdb_txn_safe: destructor
2023-06-07 18:28:10.450 T batch transaction: aborted
2023-06-07 18:28:10.450 T BlockchainLMDB::for_all_txpool_txes
2023-06-07 18:28:10.451 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:10.451 T mdb_txn_safe: destructor
2023-06-07 18:28:11.374 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.375 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.375 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.375 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.376 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.376 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.376 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.376 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.377 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.377 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.377 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.378 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.378 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.378 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.379 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.379 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.379 I Found TXT record for updates.moneropulse.org
2023-06-07 18:28:11.380 D Performing DNSSEC A record query for seeds.moneroseeds.se
2023-06-07 18:28:11.380 D Performing DNSSEC A record query for seeds.moneroseeds.li
2023-06-07 18:28:11.380 D Performing DNSSEC A record query for seeds.moneroseeds.ae.org
2023-06-07 18:28:11.381 D Performing DNSSEC A record query for seeds.moneroseeds.ch
2023-06-07 18:28:11.968 D dns_threads[2] DNS resolve done
2023-06-07 18:28:11.968 I dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2023-06-07 18:28:11.980 D dns_threads[0] DNS resolve done
2023-06-07 18:28:11.980 I dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2023-06-07 18:28:12.069 D dns_threads[1] DNS resolve done
2023-06-07 18:28:12.069 I dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2023-06-07 18:28:12.072 D dns_threads[3] DNS resolve done
2023-06-07 18:28:12.073 I dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2023-06-07 18:28:12.073 D DNS lookup for seeds.moneroseeds.se: 0 results
2023-06-07 18:28:12.073 D DNS lookup for seeds.moneroseeds.ae.org: 0 results
2023-06-07 18:28:12.074 D DNS lookup for seeds.moneroseeds.ch: 0 results
2023-06-07 18:28:12.074 D DNS lookup for seeds.moneroseeds.li: 0 results
2023-06-07 18:28:12.074 I DNS seed node lookup either timed out or failed, falling back to defaults
2023-06-07 18:28:12.074 D Seed node: 176.9.0.187:18080
2023-06-07 18:28:12.074 D Seed node: 192.99.8.110:18080
2023-06-07 18:28:12.074 D Seed node: 37.187.74.171:18080
2023-06-07 18:28:12.074 D Seed node: 51.79.173.165:18080
2023-06-07 18:28:12.074 D Seed node: 66.85.74.134:18080
2023-06-07 18:28:12.075 D Seed node: 88.198.163.90:18080
2023-06-07 18:28:12.075 D Seed node: 88.99.173.38:18080
2023-06-07 18:28:12.075 D Number of seed nodes: 7
2023-06-07 18:28:12.075 D Connecting to 192.99.8.110:18080(peer_type=1, last_seen: never)...
2023-06-07 18:28:12.075 D Spawned connection #1 to 0.0.0.0 currently we have sockets count:2
2023-06-07 18:28:12.075 D connections_ size now 1
2023-06-07 18:28:12.076 D Trying to connect to 192.99.8.110:18080, bind_ip = 0.0.0.0
2023-06-07 18:28:12.231 T Connected success to 192.99.8.110:18080
2023-06-07 18:28:12.233 T New connection from host 192.99.8.110: 0
2023-06-07 18:28:12.234 I [192.99.8.110:18080 57963a24-9452-449e-a21e-d3dff7704b65 OUT] NEW CONNECTION
2023-06-07 18:28:12.234 T Moving counter buffer by 1 second 0 < 1587 (last time 0)
2023-06-07 18:28:12.234 T dbg <<< global-IN: speed is A=       0 vs Max=1.07374e+09  so sleep: D=      -1 sec E=       0 (Enow=       1) M=1.07374e+09 W=       1 R=1.07374e+09 Wgood      11 History: [0 0 0 0 0 0 0 0 0 0 ] m_last_sample_time= 1587.87
2023-06-07 18:28:12.234 D  connection type 2 10.22.106.241:54355 <--> 192.99.8.110:18080 (via 192.99.8.110:18080)
2023-06-07 18:28:12.234 T Blockchain::get_tail_id
2023-06-07 18:28:12.234 T BlockchainLMDB::top_block_hash
2023-06-07 18:28:12.234 T BlockchainLMDB::height
2023-06-07 18:28:12.235 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:12.235 T mdb_txn_safe: destructor
2023-06-07 18:28:12.235 T BlockchainLMDB::get_block_hash_from_height
2023-06-07 18:28:12.235 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:12.235 T mdb_txn_safe: destructor
2023-06-07 18:28:12.235 T BlockchainLMDB::get_block_cumulative_difficulty  height: 0
2023-06-07 18:28:12.235 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:12.235 T mdb_txn_safe: destructor
2023-06-07 18:28:12.235 T BlockchainLMDB::get_blockchain_pruning_seed
2023-06-07 18:28:12.235 T BlockchainLMDB::block_rtxn_start
2023-06-07 18:28:12.236 T mdb_txn_safe: destructor
2023-06-07 18:28:12.236 T [192.99.8.110:18080 OUT] [levin_protocol] -->> start_outer_call
2023-06-07 18:28:12.236 T Moving counter buffer by 1 second 0 < 1587 (last time 0)
2023-06-07 18:28:12.236 T dbg >>> global-OUT: speed is A=       0 vs Max=1.07374e+09  so sleep: D=      -1 sec E=       0 (Enow=     313) M=1.07374e+09 W=       1 R=1.07374e+09 Wgood      11 History: [0 0 0 0 0 0 0 0 0 0 ] m_last_sample_time= 1587.87
2023-06-07 18:28:12.237 I [192.99.8.110:18080 OUT] 280 bytes sent for category command-1001 initiated by us
2023-06-07 18:28:12.237 T Moving counter buffer by 1 second 0 < 1587 (last time 0)
2023-06-07 18:28:12.237 D [192.99.8.110:18080 OUT] LEVIN_PACKET_SENT. [len=280, flags1, r?=?, cmd = 1001, ver=1
2023-06-07 18:28:12.238 T Throttle throttle_speed_out: packet of ~313b  (from 313 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [313 0 0 0 0 0 0 0 0 0 ]
2023-06-07 18:28:12.238 T [192.99.8.110:18080 OUT] [levin_protocol] -->> start_outer_call
2023-06-07 18:28:12.238 T Throttle >>> global-OUT: packet of ~313b  (from 313 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=1048576 KiB/sec  [313 0 0 0 0 0 0 0 0 0 ]
2023-06-07 18:28:12.238 D [192.99.8.110:18080 OUT] anvoke_handler, timeout: 5000
2023-06-07 18:28:12.238 T [192.99.8.110:18080 OUT] [levin_protocol] <<-- finish_outer_call
2023-06-07 18:28:12.392 T Moving counter buffer by 1 second 0 < 1588 (last time 0)
2023-06-07 18:28:12.393 T Throttle throttle_speed_in: packet of ~4104b  (from 4104 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [4104 0 0 0 0 0 0 0 0 0 ]
2023-06-07 18:28:12.394 T Moving counter buffer by 1 second 1587 < 1588 (last time 1587.87)
2023-06-07 18:28:12.394 T Throttle <<< global-IN: packet of ~4104b  (from 4104 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=1048576 KiB/sec  [4104 0 0 0 0 0 0 0 0 0 ]
2023-06-07 18:28:12.395 D [192.99.8.110:18080 OUT] LEVIN_PACKET partial msg received. len=4104, current total 4071/15990 (25.4597%)
2023-06-07 18:28:12.396 T dbg <<< global-IN: speed is A=    4104 vs Max=1.07374e+09  so sleep: D=-0.999996 sec E=    4104 (Enow=    4105) M=1.07374e+09 W=       1 R=1.07374e+09 Wgood      11 History: [4104 0 0 0 0 0 0 0 0 0 ] m_last_sample_time= 1588.03
2023-06-07 18:28:12.397 T Throttle throttle_speed_in: packet of ~8192b  (from 8192 b) Speed AVG=   4[w=1]    4[w=1] /  Limit=16 KiB/sec  [12296 0 0 0 0 0 0 0 0 0 ]
2023-06-07 18:28:12.397 T Throttle <<< global-IN: packet of ~8192b  (from 8192 b) Speed AVG=   4[w=1]    4[w=1] /  Limit=1048576 KiB/sec  [12296 0 0 0 0 0 0 0 0 0 ]
2023-06-07 18:28:12.398 D [192.99.8.110:18080 OUT] LEVIN_PACKET partial msg received. len=8192, current total 12263/15990 (76.6917%)
2023-06-07 18:28:12.399 T dbg <<< global-IN: speed is A=   12296 vs Max=1.07374e+09  so sleep: D=-0.999989 sec E=   12296 (Enow=   12297) M=1.07374e+09 W=       1 R=1.07373e+09 Wgood      11 History: [12296 0 0 0 0 0 0 0 0 0 ] m_last_sample_time= 1588.04
2023-06-07 18:28:12.399 T Throttle throttle_speed_in: packet of ~1384b  (from 1384 b) Speed AVG=  12[w=1]   12[w=1] /  Limit=16 KiB/sec  [13680 0 0 0 0 0 0 0 0 0 ]
2023-06-07 18:28:12.400 T Throttle <<< global-IN: packet of ~1384b  (from 1384 b) Speed AVG=  12[w=1]   12[w=1] /  Limit=1048576 KiB/sec  [13680 0 0 0 0 0 0 0 0 0 ]
2023-06-07 18:28:12.401 D [192.99.8.110:18080 OUT] LEVIN_PACKET partial msg received. len=1384, current total 13647/15990 (85.3471%)
2023-06-07 18:28:12.401 T dbg <<< global-IN: speed is A=   13680 vs Max=1.07374e+09  so sleep: D=-0.999987 sec E=   13680 (Enow=   13681) M=1.07374e+09 W=       1 R=1.07373e+09 Wgood      11 History: [13680 0 0 0 0 0 0 0 0 0 ] m_last_sample_time= 1588.04
2023-06-07 18:28:12.434 T [192.99.8.110:18080 OUT] [levin_protocol] -->> start_outer_call
2023-06-07 18:28:12.435 T [192.99.8.110:18080 OUT] [levin_protocol] <<-- finish_outer_call
2023-06-07 18:28:12.453 T [192.99.8.110:18080 OUT] [levin_protocol] -->> start_outer_call
2023-06-07 18:28:12.453 T [192.99.8.110:18080 OUT] [levin_protocol] <<-- finish_outer_call
2023-06-07 18:28:12.549 T Throttle throttle_speed_in: packet of ~2343b  (from 2343 b) Speed AVG=  13[w=1]   13[w=1] /  Limit=16 KiB/sec  [16023 0 0 0 0 0 0 0 0 0 ]
2023-06-07 18:28:12.549 T Throttle <<< global-IN: packet of ~2343b  (from 2343 b) Speed AVG=  13[w=1]   13[w=1] /  Limit=1048576 KiB/sec  [16023 0 0 0 0 0 0 0 0 0 ]
2023-06-07 18:28:12.550 D [192.99.8.110:18080 OUT] LEVIN_PACKET_RECEIVED. [len=15990, flags2, r?=?, cmd = 1001, v=1
2023-06-07 18:28:12.564 I [192.99.8.110:18080 OUT] 15990 bytes received for category command-1001 initiated by us
2023-06-07 18:28:12.565 D [192.99.8.110:18080 OUT] REMOTE PEERLIST: remote peerlist size=250
2023-06-07 18:28:12.575 T [192.99.8.110:18080 OUT] REMOTE PEERLIST:
2023-06-07 18:28:12.575 T cbf98a5cfdaafdc3      94.130.238.10:18080     rpc port -     rpc credits per hash -   pruning seed 185        last_seen: never
2023-06-07 18:28:12.575 T 593d0d68fdf4cfc7      68.183.223.191:18080    rpc port -     rpc credits per hash -   pruning seed 187        last_seen: never
2023-06-07 18:28:12.576 T f7252944de33d898      [::ffff:84.250.90.66]:18080     rpc port -      rpc credits per hash -  pruning seed 0  last_seen: never
2023-06-07 18:28:12.576 T 55ca28a8a6b738e1      [::ffff:95.217.131.84]:18080    rpc port 18089  rpc credits per hash -  pruning seed 183        last_seen: never
2023-06-07 18:28:12.576 T b519f48a6bcfc0bc      46.125.42.58:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.576 T 4092048177a5cf7b      87.92.254.131:18080     rpc port -     rpc credits per hash -   pruning seed 187        last_seen: never
2023-06-07 18:28:12.577 T b60560d1efe536ce      217.79.184.72:18080     rpc port 18081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.577 T e47b6b10df123794      70.34.196.93:18080      rpc port 18089 rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.577 T a8712ded69fb115a      95.208.0.249:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.577 T cec8450514f01706      165.22.12.133:18080     rpc port 18089 rpc credits per hash -   pruning seed 184        last_seen: never
2023-06-07 18:28:12.578 T 62d3b9b4c98860d1      5.255.102.92:18080      rpc port 18089 rpc credits per hash -   pruning seed 184        last_seen: never
2023-06-07 18:28:12.578 T ec74a01bb09dc36e      167.114.18.32:18080     rpc port 18081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.578 T cd42617c2fa17aec      71.166.54.112:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.578 T 425d2f56429b0a27      77.68.74.244:18080      rpc port 18089 rpc credits per hash -   pruning seed 184        last_seen: never
2023-06-07 18:28:12.579 T 060dc8ef5e578628      188.142.225.196:18080   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.579 T ddc30bbabb76d0ed      158.160.38.38:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.579 T 6e3a6f508e1e1bdd      75.71.22.109:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.579 T 28aac2a15c3c2088      82.64.127.107:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.580 T a1ab7846951b1e33      37.187.142.2:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.580 T 241c1205e98c60ba      207.66.71.46:18080      rpc port 18089 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.580 T 06e944085818d1de      80.241.217.144:18080    rpc port 18089 rpc credits per hash 1677721     pruning seed 187        last_seen: never
2023-06-07 18:28:12.580 T 9bcd917f1efbdc46      108.5.207.201:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.581 T cf9519d84ad02985      149.106.159.148:18080   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.581 T 80e22e500c56e3df      103.253.26.19:8081      rpc port 2121  rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.581 T a7cf6bae470587db      115.64.11.64:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.581 T af4de61c58ce7e0f      24.113.197.89:18080     rpc port -     rpc credits per hash -   pruning seed 187        last_seen: never
2023-06-07 18:28:12.582 T 157a60b97d413617      104.202.251.69:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.582 T 32b15dc92dd196e4      199.85.209.60:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.582 T 4e4ae5a405c18f22      151.74.201.59:18080     rpc port 18089 rpc credits per hash 1677721     pruning seed 0  last_seen: never
2023-06-07 18:28:12.582 T fd33d4d967b4488a      80.7.132.249:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.583 T 7569c208f56128a0      184.88.4.232:18080      rpc port 18089 rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.583 T 7124aa32092cfbf0      201.186.40.77:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.583 T 96b5dc7ec10088a8      208.167.255.10:18080    rpc port 18089 rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.583 T d17eea581a901444      85.240.250.137:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.584 T 7ed9085e906b7a99      128.75.115.105:18080    rpc port -     rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.584 T fa8d820eae5d8a4a      83.171.109.141:18080    rpc port -     rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.584 T f7d46af1e910ddf2      98.29.204.31:18080      rpc port 18082 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.584 T e3b2584dfda955eb      83.59.254.107:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.585 T 5fd8606dfe4954bc      67.14.213.202:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.585 T f9e580952b878621      136.33.180.203:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.585 T 1886c2441aa30e6a      34.71.217.137:18080     rpc port 18081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.585 T e9f2520d4fc6ec8a      64.118.118.186:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.586 T 36fcf675fea314cb      129.213.149.151:18080   rpc port -     rpc credits per hash -   pruning seed 185        last_seen: never
2023-06-07 18:28:12.586 T 8341afdd42a41209      155.4.55.87:18080       rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.586 T b2ee1bc42bbe156d      86.137.138.119:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.586 T a0f65c7e15172718      47.35.1.37:18080        rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.586 T 41bf78d7ac9845aa      140.141.169.97:18080    rpc port -     rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.587 T ff049a18c7ed5f02      132.145.233.128:18080   rpc port -     rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.587 T 64838375e4bd935e      75.179.35.59:18080      rpc port -     rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.587 T f8ef67cfa7f44768      100.0.31.209:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.587 T 0fb5026271753ec0      137.220.57.217:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.588 T 2f9e885ac9a92225      70.53.194.180:18080     rpc port -     rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.588 T 0fa8673973abd5ad      188.40.109.160:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.588 T 469521e32b9b8222      167.71.223.72:18080     rpc port 18089 rpc credits per hash -   pruning seed 184        last_seen: never
2023-06-07 18:28:12.588 T 9f9e71bc66ee025a      125.168.80.60:18080     rpc port 18089 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.589 T 5ea7b76995abcdbf      96.43.139.226:18080     rpc port 18089 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.589 T 62dbb8f10196a937      84.248.67.214:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.589 T 3105c893a5f75bf8      73.131.180.58:18080     rpc port -     rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.589 T d3a2838c90e419fd      66.42.82.58:18080       rpc port 18089 rpc credits per hash -   pruning seed 187        last_seen: never
2023-06-07 18:28:12.590 T ee14813d12b650ca      90.224.177.219:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.590 T 5426be22bc650cbe      195.159.204.93:18080    rpc port 18089 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.590 T 8ff5e33f67219597      [::ffff:67.149.203.65]:18080    rpc port -      rpc credits per hash -  pruning seed 180        last_seen: never
2023-06-07 18:28:12.590 T a3522195df14b2d5      45.87.106.43:18080      rpc port -     rpc credits per hash -   pruning seed 187        last_seen: never
2023-06-07 18:28:12.591 T 2685e21f01192719      176.150.35.61:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.591 T d4e59e77554f0e68      84.255.235.77:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.591 T f1d25c95760e35c3      99.254.47.76:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.591 T 5f49eed78358c680      203.12.10.15:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.592 T 0ec51f4dcfbdb749      146.198.48.221:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.592 T 36e82a876686db7e      76.172.85.211:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.592 T 3083e34f538681e3      136.56.58.26:18080      rpc port 18089 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.593 T 93c8255c9044730f      2.97.182.100:18080      rpc port -     rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.593 T 21389063ea7165cb      143.244.166.15:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.593 T 52e36695c9cd7dd9      146.19.75.24:18080      rpc port 18089 rpc credits per hash -   pruning seed 184        last_seen: never
2023-06-07 18:28:12.593 T ffd45e8c3237fed1      85.50.3.223:18080       rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.594 T b5d46c4560618866      195.213.118.163:18080   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.594 T f5b5f08ca84abc4d      51.158.145.141:18080    rpc port 18089 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.594 T 1af2c10f43086d86      92.224.183.202:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.594 T ebbcf04657a616f4      96.10.28.146:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.594 T dbe0b2841976f3a4      108.162.141.48:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.595 T 76d51a6e09d0267a      65.19.73.221:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.595 T 2fdc3fe8ef5de886      61.245.153.149:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.595 T 7c1bae67f1855125      185.33.135.174:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.595 T f51795e1c0bb3f3b      201.253.22.240:18080    rpc port 18089 rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.596 T 494864e91ade656f      82.65.122.63:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.596 T bb1fe3e61dc46a60      46.32.144.131:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.596 T bdd4cbff7621d479      80.245.226.69:18080     rpc port 18089 rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.596 T 4792db6e97e609f3      88.19.45.146:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.596 T 9f0a534cb36deda3      85.166.102.119:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.597 T fd59f3c39ccef1d1      94.112.168.129:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.597 T 47f7f7a960d88d30      107.2.7.237:18080       rpc port -     rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.597 T 5a9690f5ecc51ee5      173.217.250.65:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.597 T 01b07380797e5a85      75.9.75.39:18080        rpc port 18081 rpc credits per hash -   pruning seed 185        last_seen: never
2023-06-07 18:28:12.597 T f2929fa9d4b24a07      87.95.187.114:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.598 T c44fa02fb29902e3      82.66.157.214:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.598 T efa3a81bd860fc7e      51.75.146.174:34917     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.598 T 428ffc7538934080      172.93.47.73:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.598 T c8e636fc82eeffaa      84.193.137.221:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.598 T cebba92605fc5a2c      185.213.174.70:18080    rpc port 18081 rpc credits per hash -   pruning seed 187        last_seen: never
2023-06-07 18:28:12.599 T 0188cc09e100524c      34.168.192.46:18080     rpc port -     rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.599 T 432d982833eef7f5      155.4.158.111:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.599 T 49ec104e8f9af42e      135.23.202.13:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.599 T c4429e9c8c3318e2      76.95.117.26:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.599 T b1c08e83736fbe72      70.35.142.2:18080       rpc port 18089 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.600 T 4d68a33abbaad12f      37.187.6.241:18080      rpc port 18089 rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.600 T 9ef1202a2b7d88bd      96.60.221.119:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.600 T f5bf2fe884cb3979      86.9.11.38:18080        rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.600 T 2309843d75ebd2d8      76.155.38.147:18080     rpc port 18081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.601 T 3e3d30f609f73461      173.182.135.72:18080    rpc port -     rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.601 T 264b7521725a60f6      213.47.117.245:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.601 T c43e223b102b2565      184.190.222.70:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.601 T 2c110ae3b8ddf29d      74.207.226.156:18080    rpc port 18081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.601 T 7dfa98756fb40a95      24.11.138.179:18080     rpc port -     rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.602 T 55bd6115b291ac84      81.243.84.163:18080     rpc port -     rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.602 T 1d701218148feee5      51.91.128.184:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.602 T feb6dbf62ef06dbb      134.19.105.210:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.603 T 599218b47ce42a90      80.211.115.63:18080     rpc port -     rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.603 T 752f385c6a8742f6      51.38.53.106:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.603 T 6cd87f492f191eda      165.232.181.14:18080    rpc port 18089 rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.603 T 44076a0f4cd7e5f0      86.210.235.164:18080    rpc port -     rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.604 T de5dec7345f9380d      65.21.194.248:18080     rpc port 18089 rpc credits per hash -   pruning seed 185        last_seen: never
2023-06-07 18:28:12.604 T 704ce253ac6a4cd1      85.17.71.209:18080      rpc port 18089 rpc credits per hash -   pruning seed 184        last_seen: never
2023-06-07 18:28:12.604 T 011943d3f18e5368      169.150.196.17:55937    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.604 T 709457c7c16fa9e2      174.91.217.168:18080    rpc port -     rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.604 T 8c3ab29ec1a2bf42      34.27.33.7:18080        rpc port 18081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.605 T 3749d2aaaf31384e      86.28.158.41:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.605 T d6916eab12c09491      185.100.87.116:18080    rpc port -     rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.605 T 4161a78019f56904      138.199.60.30:59566     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.605 T 135863866abc512e      69.195.136.125:18080    rpc port -     rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.606 T 9173cd6cda40a23a      95.217.143.113:18080    rpc port 18089 rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.606 T fc9e4838aca8c7b6      188.157.113.212:18080   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.606 T 2fb67ce3f19e333b      51.15.18.243:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.607 T 17022e6da0b37ed7      149.28.88.208:18080     rpc port -     rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.607 T ed114bf93f636501      95.217.227.254:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.607 T 54d17ffcaf48fc57      162.55.183.179:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.607 T 665de97bc434afc2      24.66.225.40:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.608 T a88bb64d4acbc983      103.244.204.38:18080    rpc port -     rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.608 T dc8e4f71e1017f77      98.161.155.107:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.608 T 56c660b8d9a05aea      173.249.8.236:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.608 T bab749411ca6b1bb      84.74.137.139:18080     rpc port 18089 rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.609 T c392bbbc65db695c      37.187.27.193:18080     rpc port 18089 rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.609 T 0d273636e0595193      77.185.167.82:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.609 T 5190101f3940cc4f      23.113.152.136:18089    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.609 T da384c0b0a6dabd0      188.214.133.150:18080   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.610 T 58fc54137b8d852b      124.197.59.88:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.610 T 4000f27efdad26f5      195.191.218.196:18080   rpc port -     rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.610 T f6b57dcc4ecffbae      75.119.130.101:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.610 T a939bdb9c78f38fa      89.189.18.93:18080      rpc port -     rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.611 T 0f85905daf218c5e      81.149.209.24:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.611 T 7aa472d3592a3f52      185.10.68.215:18080     rpc port 18081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.611 T f8f4ed34e77b6d34      51.38.52.123:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.611 T 0b265d62c0db66e3      78.17.254.100:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.612 T c3962c2ed8c04daa      15.235.54.153:18080     rpc port -     rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.612 T 42ecacb8c84407e9      145.239.64.167:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.612 T 72a2fb7b1efa4caf      46.188.39.143:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.613 T 640c33def269547b      76.158.184.136:18080    rpc port -     rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.613 T ad3bfa40b8317987      109.152.99.102:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.613 T 67a8ec3a53af3792      80.208.229.77:18080     rpc port -     rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.614 T 3de7ff389136085b      103.3.79.106:18080      rpc port 18089 rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.614 T 6ffb8c1196034c68      148.251.194.151:18080   rpc port 18081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.614 T 98721eadc06b596d      89.22.123.62:18080      rpc port 18089 rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.614 T b10819e25c87fa9b      111.221.45.48:8080      rpc port 8089  rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.615 T c5958759630fbb5b      221.216.137.172:18089   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.615 T c264b4bc5012c01b      73.108.235.112:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.615 T d3c3dc57f017e7f6      185.69.55.193:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.615 T 9f549f05d3c166e9      65.27.203.87:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.615 T 3ee30347d9601ce6      154.5.2.41:18080        rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.615 T 2f124da502b75d01      144.172.126.144:18080   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.616 T 6634345dccc4c566      67.213.106.68:18080     rpc port 18089 rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.616 T 074e2702813d1598      5.12.75.199:18080       rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.616 T a70dff3ad77e4e85      180.150.9.143:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.616 T 1d1d2637b8cc8050      31.170.22.26:56110      rpc port -     rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.616 T 9e2d0e7a61c4d660      174.45.155.143:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.617 T 66da6b8efc9057bb      111.221.46.126:8080     rpc port 8089  rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.617 T 533a88553718600f      38.105.209.54:18080     rpc port 18089 rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.617 T 8bf83959fc4c267b      172.92.102.115:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.617 T 28e4e68f80bbe352      46.223.100.146:18080    rpc port -     rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.617 T feb16e42c78b322b      34.79.30.122:18089      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.618 T f4ce4bf8829c4748      45.132.245.124:18080    rpc port 18089 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.618 T be6b756560232d64      23.88.103.9:18080       rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.618 T 273d4d316682fafa      86.25.169.24:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.618 T 341b0d94c81b7d89      67.182.236.209:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.618 T a6ddf896230ab51c      109.238.11.161:18080    rpc port 18089 rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.618 T cbc8e0b4f5086fae      95.216.16.112:18080     rpc port 18089 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.619 T afbc812d65e0c0a0      49.12.86.248:18080      rpc port -     rpc credits per hash -   pruning seed 187        last_seen: never
2023-06-07 18:28:12.619 T 5529b9ed7fc70af9      128.199.4.77:18080      rpc port 18081 rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.619 T 3f66f6d481fbb3ec      82.129.73.17:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.619 T e3ad32f64cff83da      82.69.12.29:18080       rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.619 T 3b3a93e25bf97d47      208.102.110.203:18080   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.620 T d2875c67aa9fcfa9      5.181.25.98:18080       rpc port 18089 rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.620 T 455442aa80825951      188.235.1.208:48090     rpc port -     rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.620 T 179949b278df7057      172.73.115.193:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.620 T f1c7e62b4f8385f4      90.188.251.36:18080     rpc port 18081 rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.620 T a8c9020aa38b1f99      50.93.62.221:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.621 T 2451c84bd421e053      92.58.28.124:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.621 T 55efbc74d8938772      88.129.56.212:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.621 T a996e20a6053b2b6      98.225.91.191:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.621 T 6122f9afa63da9a4      71.181.243.239:18080    rpc port 18089 rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.621 T 787f6d8371105d47      90.1.177.105:18089      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.621 T 42b3cc14f4fa0cb6      136.49.188.247:18080    rpc port 18081 rpc credits per hash -   pruning seed 184        last_seen: never
2023-06-07 18:28:12.622 T dacf4feed155540c      192.181.251.35:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.622 T 89f8aab570754316      75.119.128.216:18080    rpc port 18081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.622 T 611a0a46f6c56f5a      176.126.87.119:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.622 T f8a7d8c66fe49a5b      222.166.93.54:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.623 T fe61e8ac1ecf3349      97.113.36.65:18080      rpc port 18089 rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.623 T c29bf4db435102d1      85.70.179.198:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.623 T 1ecbed9899efedc5      75.163.28.196:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.623 T 0e656f9b75606eba      63.209.33.111:18080     rpc port -     rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.623 T bb8ea6274399a1cc      80.48.82.70:18080       rpc port -     rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.623 T d68fc4b4220af9a1      46.227.136.66:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.624 T 12299d7ad9efd9a1      109.102.21.121:18080    rpc port 18089 rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.624 T 179866b14768dc59      97.127.0.31:18080       rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.624 T d0bd6db97a92da40      141.239.159.95:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.624 T b6d2a84595ef18ee      34.204.170.119:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.624 T b6e4472080e72e0a      188.117.249.62:18080    rpc port 18089 rpc credits per hash -   pruning seed 184        last_seen: never
2023-06-07 18:28:12.625 T 0ea57ed690b9d1b3      104.248.153.100:18080   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.625 T 702edfcb60fba600      89.58.47.13:18080       rpc port 18081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.625 T f4597ed9aaed5e63      95.31.5.255:18089       rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.625 T f7252944de33d898      84.250.90.66:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.625 T 0dff0942f41e1ca6      125.240.203.89:18080    rpc port -     rpc credits per hash -   pruning seed 184        last_seen: never
2023-06-07 18:28:12.626 T 3501b887cd0e43a2      162.19.139.184:46917    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.626 T d6d32ebacdbefe71      142.132.131.248:18080   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.626 T 5cc405d4ad9dcfa3      144.76.29.30:18080      rpc port -     rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.626 T c052181e5abd824e      79.142.69.160:36384     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.626 T 267c8e50195e3bf6      181.27.75.202:18080     rpc port 18089 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.627 T e645df773253ab8c      [::ffff:185.202.239.65]:18080   rpc port -      rpc credits per hash -  pruning seed 0  last_seen: never
2023-06-07 18:28:12.627 T 471b10fab442ecf4      71.247.228.201:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.627 T 65f6d450fe69f4f7      51.175.149.51:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.627 T 4970673fa5f17263      95.211.194.15:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.627 T 8a33ccb4aa16b0e6      174.107.212.68:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.627 T ca1555a8b9190583      73.195.110.38:18080     rpc port 18089 rpc credits per hash -   pruning seed 187        last_seen: never
2023-06-07 18:28:12.628 T 77360630019498ba      93.71.61.57:18080       rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.628 T fbf0abf7cc11c336      149.202.66.153:18080    rpc port -     rpc credits per hash -   pruning seed 187        last_seen: never
2023-06-07 18:28:12.628 T 3ad48a292d8803e8      67.176.69.73:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.628 T 4abd1600e45e255e      213.239.217.126:18080   rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.628 T b76d5ba4db008023      92.4.166.248:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.629 T d54613da054bf7fb      212.159.68.3:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.629 T 1af939fec55359eb      130.61.201.251:18080    rpc port -     rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.629 T 78d602711762c74a      82.165.111.242:18080    rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.629 T 9780564efffd4530      192.18.141.11:18080     rpc port 18089 rpc credits per hash -   pruning seed 180        last_seen: never
2023-06-07 18:28:12.629 T d5e0fd21921fbb00      153.156.198.248:18080   rpc port -     rpc credits per hash -   pruning seed 183        last_seen: never
2023-06-07 18:28:12.630 T ff2930c1776c496c      92.119.178.3:54039      rpc port 28081 rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.630 T c9f4e9aeeca7b901      24.60.31.36:18080       rpc port -     rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.630 T 33ef46590ae9a2e3      45.56.123.216:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.630 T 656d29897543d5b9      207.255.102.210:18080   rpc port -     rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.630 T 9a2f3ea0e524077a      185.19.31.153:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.631 T 23cd12901adb64f7      37.120.165.105:18080    rpc port 18089 rpc credits per hash -   pruning seed 182        last_seen: never
2023-06-07 18:28:12.631 T 4804640527593ad8      165.227.4.64:18080      rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
2023-06-07 18:28:12.631 T ea93bacf1323eb8c      173.81.87.19:18080      rpc port -     rpc credits per hash -   pruning seed 186        last_seen: never
2023-06-07 18:28:12.631 T 3d1c8583e6afc170      80.133.106.212:18080    rpc port -     rpc credits per hash -   pruning seed 181        last_seen: never
2023-06-07 18:28:12.631 T 5dcdcb0194e34c83      50.70.160.193:18080     rpc port -     rpc credits per hash -   pruning seed 0  last_seen: never
Bus error
```


## selsta | 2023-06-07T18:38:57+00:00
Please also share the config.

## k4r4b3y | 2023-06-07T18:41:24+00:00
Here's the config:
```
# Data directory (blockchain db and indices)
data-dir=/data/data/com.termux/files/home/storage/external-1/bitmonero

# Log file
log-file=/dev/null
max-log-file-size=0           # Prevent monerod from creating log files

#Peer ban list
#ban-list=/data/data/com.termux/files/home/storage/shared/crypto/monero-cli/config/block.txt

# block-sync-size=50
prune-blockchain=1            # 1 to prune

# P2P (seeding) binds
p2p-bind-ip=0.0.0.0           # Bind to all interfaces. Default is local 127.0.0.1
p2p-bind-port=18080           # Bind to default port

# Restricted RPC binds (allow restricted access)
# Uncomment below for access to the node from LAN/WAN. May require port forwarding for WAN access
rpc-restricted-bind-ip=0.0.0.0
rpc-restricted-bind-port=18089

# Unrestricted RPC binds
rpc-bind-ip=127.0.0.1         # Bind to local interface. Default = 127.0.0.1
rpc-bind-port=18081           # Default = 18081
#confirm-external-bind=1      # Open node (confirm). Required if binding outside of localhost
#restricted-rpc=1             # Prevent unsafe RPC calls.

# Services
rpc-ssl=autodetect
no-zmq=1
no-igd=1                            # Disable UPnP port mapping
db-sync-mode=fast:async:1000000     # Switch to db-sync-mode=safe for slow but more reliable db writes

# Emergency checkpoints set by MoneroPulse operators will be enforced to workaround potential consensus bugs
# Check https://monerodocs.org/infrastructure/monero-pulse/ for explanation and trade-offs
#enforce-dns-checkpointing=1
disable-dns-checkpoints=1
enable-dns-blocklist=1


# Connection Limits
out-peers=32              # This will enable much faster sync and tx awareness; the default 8 is suboptimal nowadays
in-peers=32               # The default is unlimited; we prefer to put a cap on this
limit-rate-up=1048576     # 1048576 kB/s == 1GB/s; a raise from default 2048 kB/s; contribute more to p2p network
limit-rate-down=1048576   # 1048576 kB/s == 1GB/s; a raise from default 8192 kB/s; allow for faster initial sync
```

## selsta | 2023-06-08T22:28:10+00:00
I unfortunately don't have any suggestions currently, I don't see anything interesting in the config and logs. Based on what I have heard from others it's unclear if 32-bit Android binaries even work, almost everyone who runs a node on their phone uses 64-bit.

## k4r4b3y | 2023-06-09T10:05:13+00:00
Thanks for looking at the logs and the config selsta. It is sad that there is ambiguity around whether 32-bit android binaries work or not, as there are lots of phones out there that have 32-bit OS'es running on them. It would be good if people would be able to use those old phones sitting in their drawers as a monero node.

# Action History
- Created by: k4r4b3y | 2023-06-02T13:51:56+00:00
