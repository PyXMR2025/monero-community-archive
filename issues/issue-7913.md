---
title: Improve performance syncing daemon with another daemon on the same local machine
source_url: https://github.com/monero-project/monero/issues/7913
author: woodser
assignees: []
labels: []
created_at: '2021-08-31T15:56:40+00:00'
updated_at: '2021-09-22T17:14:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Syncing a daemon with latest blocks from the network is currently one of the slowest parts of using Monero.

When syncing the daemon, we should expect most time to be spent waiting on network transmission or other external factors.

However, we find that syncing one daemon from another daemon _on the same local machine_ exhibits the same slowness with very low resource utilization of the host.

This suggests daemon sync speed can be improved dramatically by better utilizing resources of the host machine.

This issue requests investigating and improving performance of syncing one daemon from another local daemon in order to improve daemon sync speed.

**Specifically requested is a list breaking down top time consumers when syncing locally, including references to related code in order to inform where optimizations are needed and focus developer effort.**

One can sync locally in order to analyze performance by starting a local blockchain with 2 daemons syncing with each other:

1. Start daemon 1: `./monerod --stagenet --no-igd --hide-my-port --data-dir node1 --p2p-bind-ip 127.0.0.1 --p2p-bind-port 48080 --rpc-bind-port 48081 --zmq-rpc-bind-port 48082 --add-exclusive-node 127.0.0.1:38080 --rpc-login superuser:abctesting123 --rpc-access-control-origins http://localhost:8080 --fixed-difficulty 10`
2. Start daemon 2: `./monerod --stagenet --no-igd --hide-my-port --data-dir node2 --p2p-bind-ip 127.0.0.1 --rpc-bind-ip 0.0.0.0 --confirm-external-bind --add-exclusive-node 127.0.0.1:48080 --rpc-login superuser:abctesting123 --rpc-access-control-origins http://localhost:8080 --fixed-difficulty 10`
3. In either daemon, mine at least several hundred blocks, e.g.: `start_mining 52aPELZwrwvVBNK4pvRZPNj4U5EEkZBsNTR2jozCLYyrhQySvYbWebTQEdt7RS9nFnRY9r88eFpt6UcsHKnVpCQDAFKu1Az 1`
4. Stop daemon 1.
5. Pop some blocks from daemon 1's blockchain, e.g.: `./monero-blockchain-import --stagenet --data-dir ./node1 --pop-blocks 100`
6. Restart daemon 1: `./monerod --stagenet --no-igd --hide-my-port --data-dir node1 --p2p-bind-ip 127.0.0.1 --p2p-bind-port 48080 --rpc-bind-port 48081 --zmq-rpc-bind-port 48082 --add-exclusive-node 127.0.0.1:38080 --rpc-login superuser:abctesting123 --rpc-access-control-origins http://localhost:8080 --fixed-difficulty 10`
7. Observe that daemon 1 syncs relatively slowly and with very low resource utilization despite all operations being local.



# Discussion History
## selsta | 2021-08-31T19:26:04+00:00
> When syncing the daemon, we should expect most time to be spent waiting on network transmission or other external factors.

As far as I know daemon sync bottleneck is usually block verification and not networking related.

## woodser | 2021-08-31T19:42:48+00:00
> As far as I know daemon sync bottleneck is usually block verification and not networking related.

Since block verification is a local operation, it should ideally consume 100% cpu if it's the bottleneck. All cpu cores are currently underutilized so there should be room for optimization as a local operation.

## selsta | 2021-08-31T19:55:34+00:00
> Since block verification is a local operation, it should ideally consume 100% cpu if it's the bottleneck.

That implies that your disk storage has instant IO speeds. Verification requires looking up older transactions / blocks so a lot of non sequential reading.  That's why SSD/NVMe speed up sync noticeably.

## selsta | 2021-08-31T19:57:19+00:00
I'm sure things can be optimized, e.g. by using @vtnerd's ASM ECC lib (https://github.com/monero-project/supercop/tree/monero), which is currently only used for wallet scanning and not daemon sync.

## cirocosta | 2021-08-31T22:55:25+00:00
I just recorded a run of two monerod instances (compiled out of current `master` 8fde011dbeb56ab92a909710567b964186671247) with a setup pretty much the same as @woodser suggested but synced with stagenet and popping 7k blocks

using a mix of `perf` for capturing the samples an doing the first reporting

<img width="1340" alt="Screen Shot 2021-08-31 at 6 53 12 PM" src="https://user-images.githubusercontent.com/3574444/131585927-01ef0cc4-bb23-45b8-8e16-c6530ec2d7a1.png">

, then `flamegraph` and `speedscope` to visualize:

<img width="2560" alt="Screen Shot 2021-08-31 at 6 34 25 PM" src="https://user-images.githubusercontent.com/3574444/131584373-28cd9da1-873c-4ab1-9628-125be24dac5e.png">

focusing on the `[unkown]` (symbol not found):

<img width="1265" alt="Screen Shot 2021-08-31 at 6 39 36 PM" src="https://user-images.githubusercontent.com/3574444/131584849-ee7b27f4-04c7-463f-9432-d6df39aa209e.png">

it appears that the lib _might_ help but not substantially as functions like `fe_mul` don't account for all that much once we're past the checkpoints zone. 

is that right? not familiar with this part of the codebase



## selsta | 2021-08-31T22:57:07+00:00
Do you have stats for the checkpoints zone? Speeding that part up would also be interesting, as it accounts for the majority in a fresh sync.

## cirocosta | 2021-08-31T23:13:20+00:00
@selsta, just gave it a run here - starting the sync from scratch this time, we can see that most of the samples are simply `cn_slow_hash` (90% of total):

<img width="1340" alt="Screen Shot 2021-08-31 at 7 13 05 PM" src="https://user-images.githubusercontent.com/3574444/131587489-34389139-c569-4e35-b622-8fb1cea38e1f.png">

---

to generate these:

```bash
# record the samples
#
        sudo perf record -a -F 500 -g -p $pid -- sleep $RECORD_DURATION


# do some terminal-based exploration
#
        sudo perf report

# output in a way that flamegraph can consume and then generate svg
# see https://github.com/brendangregg/FlameGraph
# 
        sudo perf script >perf.script
        stackcollapse-perf.pl perf.script > ./stacks-collapsed
        cat ./stacks-collapsed | flamegraph.pl >flamegraph.svg     # (or, open `stacks-collapsed on https://www.speedscope.app/)
```

## vtnerd | 2021-08-31T23:17:52+00:00
I've already been looking at that this for a few months - I've done some recent PRs to help with data copying that occurs on both sending and receiving side of the p2p protocols. They help a bit, but as @cirocosta points out they do not constitute the majority of the time spent syncing. I think there's some improvements to be done in the "block_span" code with copying as well, but there's still that wall of cryptography.

@selsta the ECC library was not used with synchronization to reduce the possibility of a chain fork with different implementations. Perhaps it could be used only during synchronization but not after?

## selsta | 2021-08-31T23:18:50+00:00
> @selsta the ECC library was not used with synchronization to reduce the possibility of a chain fork with different implementations. Perhaps it could be used only during synchronization but not after?

Yes, that was my intention. Only use it for historical sync.

## vtnerd | 2021-08-31T23:22:07+00:00
#7803 is the outstanding work on data copying, but if you look at the numbers they aren't the dominating time for a ryzen3 desktop chip. My expectation is that CPUs with smaller caches will benefit more with that patch (less cache thrashing).

@selsta thats an intriguing thought that I will look into. The major issue is that the code is focused on wallet scanning, and will need some more functions for bulletproofs, etc.

## woodser | 2021-09-02T16:15:28+00:00
> @selsta thats an intriguing thought that I will look into. The major issue is that the code is focused on wallet scanning, and will need some more functions for bulletproofs, etc.

Throwing in my support.  Switching the ECC library for historical sync could improve sync time and UX substantially.

## boogerlad | 2021-09-22T16:45:26+00:00
> 
> 
> > Since block verification is a local operation, it should ideally consume 100% cpu if it's the bottleneck.
> 
> That implies that your disk storage has instant IO speeds. Verification requires looking up older transactions / blocks so a lot of non sequential reading. That's why SSD/NVMe speed up sync noticeably.

would 3d xpoint or a ramdrive be even faster then?

## selsta | 2021-09-22T16:46:57+00:00
The whole blockchain in RAM would speed sync up, yes. Not familiar with "3d xpoint".

## boogerlad | 2021-09-22T17:12:51+00:00
instead of NAND flash used in most SSDs, it uses a kind of phase change memory. See here: https://ark.intel.com/content/www/us/en/ark/products/123623/intel-optane-ssd-900p-series-280gb-2-5in-pcie-x4-20nm-3d-xpoint.html

I have one of those fancy SSDs and wouldn't mind running benchmarks if there are some bash scripts to do so.

How much faster would the whole blockchain in RAM be? Would the bottleneck still be i/o or would it now be the CPU?

# Action History
- Created by: woodser | 2021-08-31T15:56:40+00:00
