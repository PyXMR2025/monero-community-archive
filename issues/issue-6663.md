---
title: Raspberry Pi 4 B ARMv8 Monerod segfault
source_url: https://github.com/monero-project/monero/issues/6663
author: karlkashofer
assignees: []
labels: []
created_at: '2020-06-17T14:42:26+00:00'
updated_at: '2020-06-28T14:22:56+00:00'
type: issue
status: closed
closed_at: '2020-06-28T14:22:56+00:00'
---

# Original Description
Trying to get a monero daemon running on RPi 4B running aarch64

Debians arm64 binary gives "Illegal instruction (core dumped)"
According to #4452 and #2858 and #5782 this could be connected to AES instructions.
I recompiled with "cmake -d NO_AES=ON", but its still not working:

>2020-06-17 14:16:49.024 I Monero 'Nitrogen Nebula' (v0.16.0.0-unknown)
2020-06-17 14:16:49.025 I Initializing cryptonote protocol...
2020-06-17 14:16:49.025 I Cryptonote protocol initialized OK
2020-06-17 14:16:49.028 I Initializing core...
2020-06-17 14:16:49.029 I Loading blockchain from folder /mnt/monero_blockchain/lmdb ...
2020-06-17 14:16:49.031 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2020-06-17 14:17:14.689 I Monero 'Nitrogen Nebula' (v0.16.0.0-unknown)
2020-06-17 14:17:14.690 I Initializing cryptonote protocol...
2020-06-17 14:17:14.690 I Cryptonote protocol initialized OK
2020-06-17 14:17:14.693 I Initializing core...
2020-06-17 14:17:14.694 I Loading blockchain from folder /mnt/monero_blockchain/lmdb ...
2020-06-17 14:17:14.694 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2020-06-17 14:18:09.417 I Loading checkpoints
2020-06-17 14:18:10.456 I Core initialized OK
2020-06-17 14:18:10.456 I Initializing p2p server...
2020-06-17 14:18:10.545 I p2p server initialized OK
2020-06-17 14:18:10.546 I Initializing core RPC server...
2020-06-17 14:18:10.547 W The RPC server is accessible from the outside, but no RPC payment was setup. RPC access will be free for all.
2020-06-17 14:18:10.547 I Binding on 0.0.0.0 (IPv4):18081
2020-06-17 14:18:15.443 I core RPC server initialized OK on port: 18081
2020-06-17 14:18:15.443 I Starting core RPC server...
2020-06-17 14:18:15.444 I core RPC server started ok
2020-06-17 14:18:15.612 I Starting p2p net loop...
2020-06-17 14:18:16.613 I 
2020-06-17 14:18:16.615 I **********************************************************************
2020-06-17 14:18:16.615 I The daemon will start synchronizing with the network. This may take a long time to complete.
2020-06-17 14:18:16.615 I 
2020-06-17 14:18:16.616 I You can set the level of process detailization through "set_log <level|categories>" command,
2020-06-17 14:18:16.616 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-06-17 14:18:16.616 I 
2020-06-17 14:18:16.616 I Use the "help" command to see the list of available commands.
2020-06-17 14:18:16.617 I Use "help <command>" to see a command's documentation.
2020-06-17 14:18:16.617 I **********************************************************************
2020-06-17 14:18:17.648 I [MYIP:18080 OUT] Sync data returned a new top block candidate: 2121714 -> 2122641 [Your node is 927 blocks (1.3 days) behind] 
2020-06-17 14:18:17.648 I SYNCHRONIZATION started
Illegal instruction (core dumped)

If you want to try, this is my docker build file, you need 4GB swap to run it  on RPi4:
>FROM debian:bullseye
RUN echo "deb-src http://deb.debian.org/debian bullseye main" >> /etc/apt/sources.list
RUN apt-get -y update && apt-get -y build-dep monero
RUN apt-get source monero && ln -s `ls -d monero-*` monero && cd monero && cmake -DNO_AES=ON
RUN cd /monero && make && make install
CMD /usr/local/bin/monerod --data-dir /mnt/monero_blockchain/ --log-file /mnt/monero_blockchain/monerod.log --non-interactive --confirm-external-bind --restricted-rpc --rpc-bind-ip=0.0.0.0

Any idea what i could try next ?

# Discussion History
## moneromooo-monero | 2020-06-17T16:31:47+00:00
If you're sure this is about AES insns, you can try to run the env var MONERO_USE_SOFTWARE_AES=1

## tevador | 2020-06-18T18:24:03+00:00
Try starting monerod like this:

```
MONERO_RANDOMX_UMASK=2 ./monerod
```

## karlkashofer | 2020-06-18T18:58:05+00:00
MONERO_USE_SOFTWARE_AES=1
and 
MONERO_RANDOMX_UMASK=2

do not help, i still get 
>2020-06-18 18:50:40.725	I SYNCHRONIZATION started
Segmentation fault (core dumped)

I removed my old blockchain and started syncing from scratch, that is working ok till now, however, i am currently on block 1382424, i.e. before transition to RandomX.

I'll let you know what happens at block height 1978433 ...

## ndorf | 2020-06-18T20:35:22+00:00
If this happens again, you could try `layout asm` in gdb to find out which instruction caused the error.

## karlkashofer | 2020-06-24T14:31:29+00:00
OK, it synced up to ~ 2092532, then it crashes again:
>monerod    | 2020-06-24 14:27:31.914	I [xx.xx.xx.xx:18080 OUT] Sync data returned a new top block candidate: 2092532 -> 2127721 [Your node is 35189 blocks (1.6 months) behind] 
monerod    | 2020-06-24 14:27:31.914	I SYNCHRONIZATION started
monerod    | Illegal instruction (core dumped)

Upping the loglevel i get:
>monerod    | 2020-06-24 14:25:25.305	T [61.177.83.6:18080 OUT] [levin_protocol] <<-- finish_outer_call
monerod    | 2020-06-24 14:25:25.305	T [61.177.83.6:18080 OUT] [sock 22] release
monerod    | 2020-06-24 14:25:25.374	D Couldn't use largePages for RandomX VM
monerod    | Segmentation fault (core dumped)
monerod exited with code 139

Any ideas ?

## karlkashofer | 2020-06-24T15:11:31+00:00
Checking HugePages Support:
>/mnt/data/docker/monerod$ cat /sys/kernel/mm/transparent_hugepage/enabled
[always] madvise never

>/mnt/data/docker/monerod$ grep HugePages /proc/meminfo 
AnonHugePages:     18432 kB
ShmemHugePages:        0 kB
FileHugePages:         0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0

running
>sudo sysctl -w vm.nr_hugepages=126

does not change anything

## hyc | 2020-06-24T15:22:52+00:00
If you don't allocate the hugepages at boot time it's very likely you won't be able to. What does /proc/meminfo show after you run the sysctl command?

Also - the lack of hugepages is irrelevant, as far as the Illegal Instruction exception is concerned. 

## tevador | 2020-06-24T17:01:47+00:00
Large pages are not required to run RandomX. It's just a harmless warning.

The issue also doesn't seem to be caused by hardware AES since you were able to sync past block 1978433.

I have experienced random SIGILL/SIGSEGV on ARM before. It was caused by the instruction cache not getting flushed properly after JITing the RandomX code.

You can try running `MONERO_RANDOMX_UMASK=8 ./monerod` and see if it starts syncing. This will force the interpreter mode.

## karlkashofer | 2020-06-25T16:49:10+00:00
Hi !
MONERO_RANDOMX_UMASK=8 works !
What does that UMASK do ?

I notice mining is much slower now, is 2092532 the first RANDOMX block ?

>monerod    | 2020-06-25 16:39:22.669	I [81.25.55.79:18080 OUT] Sync data returned a new top block candidate: 2092532 -> 2128498 [Your node is 35966 blocks (1.6 months) behind] 
monerod    | 2020-06-25 16:39:22.670	I SYNCHRONIZATION started
monerod    | 2020-06-25 16:39:52.691	I Synced 2092552/2128499 (98%, 35947 left)
monerod    | 2020-06-25 16:40:19.458	I Synced 2092572/2128499 (98%, 35927 left)
monerod    | 2020-06-25 16:40:53.417	I Synced 2092592/2128499 (98%, 35907 left)
monerod    | 2020-06-25 16:41:13.667	I Synced 2092612/2128499 (98%, 35887 left)
monerod    | 2020-06-25 16:41:36.782	I Synced 2092632/2128500 (98%, 35868 left, 0% of total synced, estimated 13.3 hours left)
monerod    | 2020-06-25 16:41:54.425	I Synced 2092652/2128500 (98%, 35848 left)
monerod    | 2020-06-25 16:42:18.682	I Synced 2092672/2128500 (98%, 35828 left)
monerod    | 2020-06-25 16:42:33.799	I Synced 2092692/2128501 (98%, 35809 left)

Very cool.

## tevador | 2020-06-25T17:11:27+00:00
> I notice mining is much slower now, is 2092532 the first RANDOMX block ?

No. The first RandomX block was 1978433. `MONERO_RANDOMX_UMASK=8` forces the interpreter mode, which is about 10x slower than the compiled mode.

Also I don't think the name of the issue is correct. Your previous segfault was on a different block height AFAICS. Or does it always crash on 2092532? If yes, it could be related to the particular program that the block was mined with.

## karlkashofer | 2020-06-25T17:33:14+00:00
You are correct about the title, it seems to crash on different blocks, i just took the number from the log but that does not seem to be the current block. Will change the title asap.

Hmm, when i remove MONERO_RANDOMX_UMASK=8 it crashes again.

>.size()=10000, m_start_height=2095231, m_total_height=2128530
2020-06-25 17:29:24.033	I [195.154.233.74:18080 OUT] [0] state: received chain in state synchronizing
2020-06-25 17:29:24.034	D [195.154.233.74:18080 OUT] first block hash <06e4bc309a829cfb3f3b9fe9c4fcf73cc421cc20d51a4a6f32a71bca3f1ad294>, last <64835e3e7eb07ef0fae3e8f0bdcd1d82246e9b9719b1531fdb43b0e87f363ab0>
2020-06-25 17:29:24.037	T Blockchain::get_current_blockchain_height
2020-06-25 17:29:24.038	T BlockchainLMDB::height
2020-06-25 17:29:24.038	T BlockchainLMDB::block_rtxn_start
2020-06-25 17:29:24.038	T mdb_txn_safe: destructor
2020-06-25 17:29:24.038	T Blockchain::get_current_blockchain_height
2020-06-25 17:29:24.038	T BlockchainLMDB::height
2020-06-25 17:29:24.038	T BlockchainLMDB::block_rtxn_start
2020-06-25 17:29:24.038	T mdb_txn_safe: destructor
2020-06-25 17:29:24.038	D get_next_needed_pruning_stripe: want height 2095252 (2095232 from blockchain, 2095252 from block queue), stripe 8 (5/8 on it and 0 on 1, 0 others) -> 1 (+1), current peers 115 104 115 115 110 110 
2020-06-25 17:29:24.038	T BlockchainLMDB::get_blockchain_pruning_seed
2020-06-25 17:29:24.038	T BlockchainLMDB::block_rtxn_start
2020-06-25 17:29:24.038	T mdb_txn_safe: destructor
2020-06-25 17:29:24.038	T Blockchain::have_block
2020-06-25 17:29:25.614	D Couldn't use largePages for RandomX VM
Segmentation fault (core dumped)

So, will it have to run in this slow interpreter mode forever ?

Also, is there documentation of Monero environment variables somewhere ?

## karlkashofer | 2020-06-26T08:05:28+00:00
Ok, so with MONERO_RANDOMX_UMASK=8 i was now able to successfully sync up to now.

Still, it seems compiled mode is not working on Armv8. 
Is that a concern? Should we try to find the root cause? Or is there no need?


## tevador | 2020-06-26T08:29:25+00:00
> Still, it seems compiled mode is not working on Armv8.

I have a Raspberry Pi 3B and compiled mode works for me just fine. AFAIK you are the first one reporting this issue. It's possible that the chip in your Raspberry is faulty.

## karlkashofer | 2020-06-26T09:24:59+00:00
Hmm, how did you produce the arm64 monerod binary ? 

I use the one from Debian bullseye, but i have also done a native compile on the RPi4 from debian sources. Both have the same problem. Maybe a compiler flag ?

Could you send me your binary ?

## tevador | 2020-06-26T19:54:56+00:00
I'm not running monerod on my raspberry, but I did quite extensive testing using the RandomX benchmark. You can build it from source here: https://github.com/tevador/RandomX

You can test it with: `./randomx-benchmark --verify --auto` - this will calculate 1000 hashes and print the result.

If the basic tests doesn't crash, you can try `./randomx-benchmark --verify --auto --threads 4 --nonces 100000`, which should be a good stress test.

## karlkashofer | 2020-06-26T21:26:43+00:00
Hmm, verify seems to work, mining does not work here, "Ungültiger Maschinenbefehl" is "Illegal instruction":

karl@rpi4-20200622:~$ ./randomx-benchmark --verify --auto 
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - light memory mode (256 MiB)
 - JIT compiled mode 
 - software AES mode
 - small pages mode
Initializing ...
Memory initialized in 2.29795 s
Initializing 1 virtual machine(s) ...
Running benchmark (1000 nonces) ...
Calculated result: 10b649a3f15c7c7f88277812f2e74b337a0f20ce909af09199cccb960771cfa1
Reference result:  10b649a3f15c7c7f88277812f2e74b337a0f20ce909af09199cccb960771cfa1
Performance: 80.7858 ms per hash
karl@rpi4-20200622:~$
****************************************************
karl@rpi4-20200622:~$ ./randomx-benchmark --verify --auto --threads 4 --nonces 1000
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - light memory mode (256 MiB)
 - JIT compiled mode 
 - software AES mode
 - small pages mode
Initializing ...
Memory initialized in 2.29395 s
Initializing 4 virtual machine(s) ...
Running benchmark (1000 nonces) ...
Calculated result: 10b649a3f15c7c7f88277812f2e74b337a0f20ce909af09199cccb960771cfa1
Reference result:  10b649a3f15c7c7f88277812f2e74b337a0f20ce909af09199cccb960771cfa1
Performance: 24.9544 ms per hash
karl@rpi4-20200622:~$
****************************************************
karl@rpi4-20200622:~$ ./randomx-benchmark --mine --jit --threads 4 --init 4
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - full memory mode (2080 MiB)
 - JIT compiled mode 
 - hardware AES mode
 - small pages mode
Initializing (4 threads) ...
Memory initialized in 31.5856 s
Initializing 4 virtual machine(s) ...
Ungültiger Maschinenbefehl
karl@rpi4-20200622:~$
****************************************************
karl@rpi4-20200622:~$ ./randomx-benchmark --mine --threads 4 --init 4
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - full memory mode (2080 MiB)
 - interpreted mode
 - hardware AES mode
 - small pages mode
Initializing (4 threads) ...
WARNING: You are using the interpreter mode. Use --jit for optimal performance.
Memory initialized in 487.612 s
Initializing 4 virtual machine(s) ...
Ungültiger Maschinenbefehl
karl@rpi4-20200622:~$
****************************************************
karl@rpi4-20200622:~$ ./randomx-benchmark --mine --jit --secure --threads 4 --init 4
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - full memory mode (2080 MiB)
 - JIT compiled mode (secure)
 - hardware AES mode
 - small pages mode
Initializing (4 threads) ...
Memory initialized in 31.561 s
Initializing 4 virtual machine(s) ...
Ungültiger Maschinenbefehl
karl@rpi4-20200622:~$
****************************************************
karl@rpi4-20200622:$ uname -a
Linux rpi4-20200622 5.7.0-rc5-arm64 #1 SMP Debian 5.7~rc5-1~exp1 (2020-05-10) aarch64 GNU/Linux
****************************************************
different pi:
****************************************************
karl@rpi4-20200516:~$ ./randomx-benchmark --mine --jit --threads 4 --init 4
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - full memory mode (2080 MiB)
 - JIT compiled mode 
 - hardware AES mode
 - small pages mode
Initializing (4 threads) ...
Memory initialized in 59.2033 s
Initializing 4 virtual machine(s) ...
Ungültiger Maschinenbefehl
****************************************************
karl@rpi4-20200516:~$  ./randomx-benchmark --verify --auto 
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - light memory mode (256 MiB)
 - JIT compiled mode 
 - software AES mode
 - small pages mode
Initializing ...
Memory initialized in 2.66804 s
Initializing 1 virtual machine(s) ...
Running benchmark (1000 nonces) ...
Calculated result: 10b649a3f15c7c7f88277812f2e74b337a0f20ce909af09199cccb960771cfa1
Reference result:  10b649a3f15c7c7f88277812f2e74b337a0f20ce909af09199cccb960771cfa1
Performance: 110.247 ms per hash
karl@rpi4-20200516:~$ 

## tevador | 2020-06-26T22:11:28+00:00
> * hardware AES mode

You are using the wrong command for mining. You have to either use `--softAes` or `--auto` because the raspberry pi doesn't have hardware AES.

Also I recommend running the test with a lot more than the default 1000 nonces. Try `--nonces 100000`.

## karlkashofer | 2020-06-26T23:12:52+00:00
You are right, RandomX works in verify and mine mode on arm8 Rpi4:

karl@rpi4-20200622:~$ time ./randomx-benchmark --verify --auto --threads 4 --init 4 --nonces 100000
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - light memory mode (256 MiB)
 - JIT compiled mode 
 - software AES mode
 - small pages mode
Initializing ...
Memory initialized in 2.22104 s
Initializing 4 virtual machine(s) ...
Running benchmark (100000 nonces) ...
Calculated result: f35a269c763e9ef175708a5099c2c30ea25f6cb26fe79b0049d96846f5fbfd47
Performance: 23.6283 ms per hash

real	39m25,094s
user	154m38,689s
sys	0m9,325s
karl@rpi4-20200622:~$
************************************************************************************************
karl@rpi4-20200622:~$ ./randomx-benchmark --mine --auto
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - full memory mode (2080 MiB)
 - JIT compiled mode 
 - software AES mode
 - small pages mode
Initializing (4 threads) ...
Memory initialized in 33.7921 s
Initializing 1 virtual machine(s) ...
Running benchmark (1000 nonces) ...
Calculated result: 10b649a3f15c7c7f88277812f2e74b337a0f20ce909af09199cccb960771cfa1
Reference result:  10b649a3f15c7c7f88277812f2e74b337a0f20ce909af09199cccb960771cfa1
Performance: 43.3783 hashes per second

Which gets us back to the question why is my monerod crashing in compile mode ?


## tevador | 2020-06-27T12:19:52+00:00
Can you rerun the benchmark with the `--secure` option? Monerod uses it, but it's disabled by default in the benchmark.

Run:
`./randomx-benchmark --verify --auto --secure --threads 4 --init 4 --nonces 100000`

If this crashes, then we know it's caused by the secure option. It can be disabled with `MONERO_RANDOMX_UMASK=16`.

## karlkashofer | 2020-06-27T13:10:54+00:00
Seems to work:

karl@rpi4-20200622:~$ ./randomx-benchmark --verify --auto --secure --threads 4 --init 4 --nonces 100000
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - light memory mode (256 MiB)
 - JIT compiled mode (secure)
 - software AES mode
 - small pages mode
Initializing ...
Memory initialized in 2.42567 s
Initializing 4 virtual machine(s) ...
Running benchmark (100000 nonces) ...
Calculated result: f35a269c763e9ef175708a5099c2c30ea25f6cb26fe79b0049d96846f5fbfd47
Performance: 24.8803 ms per hash



## tevador | 2020-06-27T13:23:04+00:00
Then I'm out of ideas. Can you check with `gdb` where exactly monerod crashes? `bt` should show the stack trace and `disassemble $pc-40,$pc+40` will show the code around the instruction where it crashed.

## karlkashofer | 2020-06-27T17:09:05+00:00
root@ed91bb20dc8a:/# monerod  --data-dir /mnt/monero_blockchain/ --log-file /mnt/monero_blockchain/monerod.log --non-interactive --confirm-external-bind --restricted-rpc --rpc-bind-ip=0.0.0.0 
2020-06-27 17:05:38.406	I Monero 'Nitrogen Nebula' (v0.16.0.0-unknown)
2020-06-27 17:05:38.406	I Initializing cryptonote protocol...
2020-06-27 17:05:38.406	I Cryptonote protocol initialized OK
2020-06-27 17:05:38.408	I Initializing core...
2020-06-27 17:05:38.408	I Loading blockchain from folder /mnt/monero_blockchain/lmdb ...
2020-06-27 17:05:38.618	I Loading checkpoints
2020-06-27 17:05:38.620	I Core initialized OK
2020-06-27 17:05:38.620	I Initializing p2p server...
2020-06-27 17:05:38.639	I p2p server initialized OK
2020-06-27 17:05:38.639	I Initializing core RPC server...
2020-06-27 17:05:38.640	W The RPC server is accessible from the outside, but no RPC payment was setup. RPC access will be free for all.
2020-06-27 17:05:38.640	I Binding on 0.0.0.0 (IPv4):18081
2020-06-27 17:05:39.345	I core RPC server initialized OK on port: 18081
2020-06-27 17:05:39.345	I Starting core RPC server...
2020-06-27 17:05:39.345	I core RPC server started ok
2020-06-27 17:05:39.349	I Starting p2p net loop...
2020-06-27 17:05:40.350	I 
2020-06-27 17:05:40.350	I **********************************************************************
2020-06-27 17:05:40.351	I The daemon will start synchronizing with the network. This may take a long time to complete.
2020-06-27 17:05:40.351	I 
2020-06-27 17:05:40.351	I You can set the level of process detailization through "set_log <level|categories>" command,
2020-06-27 17:05:40.351	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-06-27 17:05:40.351	I 
2020-06-27 17:05:40.351	I Use the "help" command to see the list of available commands.
2020-06-27 17:05:40.351	I Use "help <command>" to see a command's documentation.
2020-06-27 17:05:40.352	I **********************************************************************
2020-06-27 17:05:41.132	I [52.195.11.169:18080 OUT] Sync data returned a new top block candidate: 2129993 -> 2129996 [Your node is 3 blocks (6.0 minutes) behind] 
2020-06-27 17:05:41.132	I SYNCHRONIZATION started
Segmentation fault (core dumped)
root@ed91bb20dc8a:/# which monerod
/usr/bin/monerod
root@ed91bb20dc8a:/# gdb /usr/bin/monerod /usr/bin/com
comm     compose  
root@ed91bb20dc8a:/# gdb /usr/bin/monerod /usr/bin/com
comm     compose  
root@ed91bb20dc8a:/# gdb /usr/bin/monerod core        
GNU gdb (Debian 9.2-1) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "aarch64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /usr/bin/monerod...
(No debugging symbols found in /usr/bin/monerod)
[New LWP 262]
[New LWP 246]
[New LWP 243]
[New LWP 253]
[New LWP 244]
[New LWP 264]
[New LWP 247]
[New LWP 251]
[New LWP 248]
[New LWP 263]
[New LWP 260]
[New LWP 249]
[New LWP 256]
[New LWP 245]
[New LWP 254]
[New LWP 252]
[New LWP 250]
[New LWP 257]
[New LWP 259]
[New LWP 258]
[New LWP 255]
[New LWP 261]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
Core was generated by `monerod --data-dir /mnt/monero_blockchain/ --log-file /mnt/monero_blockchain/mo'.
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x0000ffe824447424 in ?? ()
[Current thread is 1 (Thread 0xffe7fabfaf50 (LWP 262))]
(gdb) bt
#0  0x0000ffe824447424 in ?? ()
Backtrace stopped: Cannot access memory at address 0x9e0d9dc1cff8ea7f
(gdb) disassemble $pc-40,$pc+40
Dump of assembler code from 0xffe8244473fc to 0xffe82444744c:
   0x0000ffe8244473fc:	adr	x27, 0xffe824539bb4
   0x0000ffe824447400:	.inst	0x8bb9a86c ; undefined
   0x0000ffe824447404:	bl	0xffe8203ac7c0
   0x0000ffe824447408:	.inst	0xe05151ee ; undefined
   0x0000ffe82444740c:	ldr	s21, 0xffe8244aaec0
   0x0000ffe824447410:	.inst	0x028b90cf ; undefined
   0x0000ffe824447414:	.inst	0x53567669 ; undefined
   0x0000ffe824447418:	.inst	0x1a1eed42 ; undefined
   0x0000ffe82444741c:	eor	xzr, x29, x5, lsl #42
   0x0000ffe824447420:	stp	w6, w25, [x6], #-132
=> 0x0000ffe824447424:	.inst	0xbb156a26 ; undefined
   0x0000ffe824447428:	.inst	0x59f8d65e ; undefined
   0x0000ffe82444742c:	cbz	x1, 0xffe8244d2110
   0x0000ffe824447430:	adr	x12, 0xffe8243c21c8
   0x0000ffe824447434:	orr	x4, x17, #0x7ffff00
   0x0000ffe824447438:	bl	0xffe8231cb87c
   0x0000ffe82444743c:	.inst	0x60740537 ; undefined
   0x0000ffe824447440:	sub	w2, w14, #0x962, lsl #12
   0x0000ffe824447444:	.inst	0xa69376bf ; undefined
   0x0000ffe824447448:	stp	d25, d0, [x16, #112]
End of assembler dump.
(gdb) 


## tevador | 2020-06-27T17:22:03+00:00
It looks like it's executing garbage data. I will summon @SChernykh since he is the author of the ARMv8 JIT compiler.

## SChernykh | 2020-06-27T17:30:38+00:00
@karlkashofer Did you build monerod yourself? And randomx-benchmark? Or was it all official binaries? I remember we had garbage code in RandomX on ARMv8 with certain compiler/linker versions...

## karlkashofer | 2020-06-27T17:42:48+00:00
monerod is the arm64 binary from debian bullseye, randomx-benchmark was downloaded from https://github.com/tevador/RandomX/releases, all tests were done in docker containers

## SChernykh | 2020-06-27T17:46:19+00:00
randomx-benchmark works with JIT for you, hmm... I have RPi3 B+. I don't run monerod there, but mining works. Can you try to compile randomx-benchmark? If your binary still works with JIT, you have a good chance to get working monerod if you compile it yourself.

## karlkashofer | 2020-06-27T18:29:12+00:00
Scanning dependencies of target randomx-tests
[ 97%] Building CXX object CMakeFiles/randomx-tests.dir/src/tests/tests.cpp.o
[100%] Linking CXX executable randomx-tests
[100%] Built target randomx-tests
root@ed91bb20dc8a:/build/RandomX/build# ls
CMakeCache.txt	Makefile	     librandomx.a	randomx-codegen
CMakeFiles	cmake_install.cmake  randomx-benchmark	randomx-tests
root@ed91bb20dc8a:/build/RandomX/build# ./randomx-benchmark --verify --auto --secure --threads 4 --init 4 --nonces 10000 
RandomX benchmark v1.1.7
 - Argon2 implementation: reference
 - light memory mode (256 MiB)
 - JIT compiled mode (secure)
 - software AES mode
 - small pages mode
Initializing ...
Memory initialized in 2.35389 s
Initializing 4 virtual machine(s) ...
Running benchmark (10000 nonces) ...
Calculated result: aac101905c037428abc2b21e5a5dbf4a520c38a400448c288113b84728bffb54
Performance: 24.0257 ms per hash
root@ed91bb20dc8a:/build/RandomX/build# 

seems to work OK

## karlkashofer | 2020-06-27T20:35:25+00:00
>echo "deb-src http://deb.debian.org/debian bullseye main" >> /etc/apt/sources.list
apt-get -y update && apt-get -y build-dep monero
apt-get source monero && ln -s `ls -d monero-*` monero && cd monero && cmake .
make
.......
>[ 95%] Built target blockchain_prune_known_spent_data
Scanning dependencies of target blockchain_depth
[ 95%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_depth.dir/blockchain_depth.cpp.o
[ 96%] Linking CXX executable ../../bin/monero-blockchain-depth
[ 96%] Built target blockchain_depth
Scanning dependencies of target blockchain_import
[ 97%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_import.dir/blockchain_import.cpp.o
[ 97%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_import.dir/bootstrap_file.cpp.o
[ 98%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_import.dir/blocksdat_file.cpp.o
[ 98%] Linking CXX executable ../../bin/monero-blockchain-import
[ 98%] Built target blockchain_import
Scanning dependencies of target blockchain_usage
[ 98%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_usage.dir/blockchain_usage.cpp.o
[100%] Linking CXX executable ../../bin/monero-blockchain-usage
[100%] Built target blockchain_usage
root@ed91bb20dc8a:/monero# bin/monerod  --data-dir /mnt/monero_blockchain/ --log-file /mnt/monero_blockchain/monerod.log --non-interactive --confirm-external-bind --restricted-rpc --rpc-bind-ip=0.0.0.0
2020-06-27 20:32:06.346	I Monero 'Nitrogen Nebula' (v0.16.0.0-unknown)
2020-06-27 20:32:06.347	I Initializing cryptonote protocol...
2020-06-27 20:32:06.347	I Cryptonote protocol initialized OK
2020-06-27 20:32:06.349	I Initializing core...
2020-06-27 20:32:06.351	I Loading blockchain from folder /mnt/monero_blockchain/lmdb ...
2020-06-27 20:32:13.514	I Loading checkpoints
2020-06-27 20:32:13.673	I Core initialized OK
2020-06-27 20:32:13.673	I Initializing p2p server...
2020-06-27 20:32:13.695	I p2p server initialized OK
2020-06-27 20:32:13.695	I Initializing core RPC server...
2020-06-27 20:32:13.696	W The RPC server is accessible from the outside, but no RPC payment was setup. RPC access will be free for all.
2020-06-27 20:32:13.696	I Binding on 0.0.0.0 (IPv4):18081
2020-06-27 20:32:17.137	I core RPC server initialized OK on port: 18081
2020-06-27 20:32:17.138	I Starting core RPC server...
2020-06-27 20:32:17.138	I core RPC server started ok
2020-06-27 20:32:17.147	I Starting p2p net loop...
2020-06-27 20:32:18.147	I 
2020-06-27 20:32:18.148	I **********************************************************************
2020-06-27 20:32:18.148	I The daemon will start synchronizing with the network. This may take a long time to complete.
2020-06-27 20:32:18.148	I 
2020-06-27 20:32:18.148	I You can set the level of process detailization through "set_log <level|categories>" command,
2020-06-27 20:32:18.150	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-06-27 20:32:18.150	I 
2020-06-27 20:32:18.150	I Use the "help" command to see the list of available commands.
2020-06-27 20:32:18.150	I Use "help <command>" to see a command's documentation.
2020-06-27 20:32:18.150	I **********************************************************************
2020-06-27 20:32:18.921	I [52.195.11.169:18080 OUT] Sync data returned a new top block candidate: 2129993 -> 2130085 [Your node is 92 blocks (3.1 hours) behind] 
2020-06-27 20:32:18.921	I SYNCHRONIZATION started
Illegal instruction (core dumped)
root@ed91bb20dc8a:~/monero# 

so, monerod built from debian sources crashes.

## karlkashofer | 2020-06-27T22:53:57+00:00
The plot thickens:

>root@ed91bb20dc8a:~/monero-git/monero# build/Linux/release-v0.16/release/bin/monerod --data-dir /mnt/monero_blockchain/ --log-file /mnt/monero_blockchain/monerod.log --non-interactive --confirm-external-bind --restricted-rpc --rpc-bind-ip=0.0.0.0
2020-06-27 22:48:42.737	I Monero 'Nitrogen Nebula' (v0.16.0.1-release)
2020-06-27 22:48:42.737	I Initializing cryptonote protocol...
2020-06-27 22:48:42.737	I Cryptonote protocol initialized OK
2020-06-27 22:48:42.739	I Initializing core...
2020-06-27 22:48:42.739	I Loading blockchain from folder /mnt/monero_blockchain/lmdb ...
2020-06-27 22:48:49.793	I Loading checkpoints
2020-06-27 22:48:49.953	I Core initialized OK
2020-06-27 22:48:49.953	I Initializing p2p server...
2020-06-27 22:48:49.977	I p2p server initialized OK
2020-06-27 22:48:49.978	I Initializing core RPC server...
2020-06-27 22:48:49.979	I Binding on 0.0.0.0 (IPv4):18081
2020-06-27 22:48:52.179	I core RPC server initialized OK on port: 18081
2020-06-27 22:48:52.180	I Starting core RPC server...
2020-06-27 22:48:52.180	I core RPC server started ok
2020-06-27 22:48:52.187	I Starting p2p net loop...
2020-06-27 22:48:53.187	I 
2020-06-27 22:48:53.188	I **********************************************************************
2020-06-27 22:48:53.188	I The daemon will start synchronizing with the network. This may take a long time to complete.
2020-06-27 22:48:53.188	I 
2020-06-27 22:48:53.188	I You can set the level of process detailization through "set_log <level|categories>" command,
2020-06-27 22:48:53.188	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-06-27 22:48:53.188	I 
2020-06-27 22:48:53.189	I Use the "help" command to see the list of available commands.
2020-06-27 22:48:53.189	I Use "help <command>" to see a command's documentation.
2020-06-27 22:48:53.189	I **********************************************************************
2020-06-27 22:48:53.989	I [52.195.11.169:18080 OUT] Sync data returned a new top block candidate: 2129993 -> 2130128 [Your node is 135 blocks (4.5 hours) behind] 
2020-06-27 22:48:53.990	I SYNCHRONIZATION started
2020-06-27 22:49:19.038	I Synced 2130013/2130128 (99%, 115 left)
2020-06-27 22:49:34.470	I Synced 2130033/2130128 (99%, 95 left)
^C2020-06-27 22:49:38.387	I p2p net loop stopped
2020-06-27 22:49:38.393	I Stopping core RPC server...
2020-06-27 22:49:38.394	I Node stopped.
2020-06-27 22:49:38.395	I Deinitializing core RPC server...
2020-06-27 22:49:38.396	I Deinitializing p2p...
2020-06-27 22:49:38.433	I Deinitializing core...
2020-06-27 22:49:39.610	I Stopping cryptonote protocol...
2020-06-27 22:49:39.611	I Cryptonote protocol stopped successfully

Compiling from git works ! So it seems the debian packagr is broken.

It seems git has a newer version than debian, v0.16.0.1-release instead of v0.16.0.0-unknown
Where there any randomX specific changes in that version ?

I will ping the debian maintainers to update.

# Action History
- Created by: karlkashofer | 2020-06-17T14:42:26+00:00
- Closed at: 2020-06-28T14:22:56+00:00
