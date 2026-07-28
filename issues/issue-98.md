---
title: Mining protocol changes to combat pool centralization
source_url: https://github.com/monero-project/research-lab/issues/98
author: tevador
assignees: []
labels: []
created_at: '2022-02-16T19:53:13+00:00'
updated_at: '2025-09-15T14:20:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero mining has been [centralized to 2-3 large pools](https://miningpoolstats.stream/monero) for a long time (recently, the largest pool even briefly exceeded 50% of the hashrate). This unhealthy situation is not going to get fixed by itself. It needs a protocol-level solution.

I don't think we should implement [radical changes against pool mining like Wownero did](https://git.wownero.com/wownero/wownero/pulls/369), but I'm proposing a relatively small change to make pooled mining more difficult.

The [RandomX dataset](https://github.com/tevador/RandomX/blob/master/doc/specs.md#7-dataset) is constructed from a 256-MiB cache. This cache is expanded from a 32-byte block ID using Argon2 every 2048 blocks (~3 days).

I'm proposing the following changes:

* Construct the cache by selecting random parts of the blockchain instead of using Argon2.
* Reseed the cache every 64 blocks instead of every 2048 blocks.

The portion of the blockchain that can be used is roughly ~10 GiB (everything except of prunable data - ring signatures and range proofs). The parts that are used to construct the cache could be selected pseudorandomly based on the seed block ID.

The effect of this change on the network nodes would be negligible. They already have all the data needed to construct the cache.

However, this would greatly increase the bandwidth requirements for centralized pools and their miners. Miners would either have to run their own nodes or pools would have to provide the 256 MiB cache to every miner every 2 hours. Interestingly, both of these solutions have roughly the same bandwidth requirements of ~3 GB/day (compared to ~1 MB/day that miners use currently),

If miners are forced to run their own nodes, they can find it more convenient to mine on p2pool rather than using a centralized pool.

# Discussion History
## rottenwheel | 2022-02-23T08:26:38+00:00
For what it is worth, I fully support this proposal to mitigate pool centralization. Anything that helps us boost the overall full node count, is a net positive towards decentralization; if to that we add the fact that the sometimes crazy network hashrate swings are mitigated to prevent any given pool from attaining more than 51% of total network hashrate, that is just the icing on the cake.

Keen to hear others' feedback and discuss it further. Take my support at face value.

## mad-ben | 2022-02-24T21:43:52+00:00
Sounds like a good idea.

## trasherdk | 2022-02-25T01:47:12+00:00
It would probably kill off quite a few botnet's plus all those who don't feel like maintaining a 2 node mining setup.

I wonder how much hashrate that amounts to.

## SamsungGalaxyPlayer | 2022-02-28T16:16:46+00:00
I want to push p2pool use, though I would prefer to see guides for p2pool improve further before something like this is implemented. To point a miner at a mining pool, all one needs to do is find a pool and run a program.

I notably would like a reliable program where 1 click/command would set up the p2pool server and mine (and set up a monero node or use a different one), so that the UX is exactly the same as running a mining program alone. I would like this as both a separate program and in the GUI.

Many users find Monero because it is easy to mine. Should we add roadblocks in the way of that, I want to make sure they are appropriately addressed. Monero should remain one of the most accessible mining routes for novices.

## Gingeropolous | 2022-05-09T23:25:40+00:00
@SamsungGalaxyPlayer , it seems that the GUI implementation of p2pool has happened.

> Many users find Monero because it is easy to mine. Should we add roadblocks in the way of that, I want to make sure they are appropriately addressed.

Monero will still be easy to mine. Mining pools would still exist. They would just have higher fees to compensate for the higher data usage. 

And yeah, I'm a fan of this proposal. I've always been a fan of this boolberry-type thing. I think they called it wild-keccak? 

awesome awesome.

## MoneroOcean | 2022-05-11T03:28:14+00:00
I guess pools will enforce stricter policy on proxy usage to minimize effect of this change (if I understood everything correctly here of course). 

## Gingeropolous | 2022-05-12T13:54:18+00:00
this was discussed at a recent MRL, well, mostly after the meeting. It seems the bandwidth costs for pools are negligible, so this would really just be a nuisance for larger pools and end up preventing smaller pools from surviving. 

## Gingeropolous | 2022-05-13T16:10:26+00:00
the estimate is that minexmr pulls in like $12k. So if they have to spend ~10k in bandwidith, they'll just raise their fee to 1.5% and pull in $18k in fees. 

also, i would imagine digital ocean is on the high end for bandwidth costs

https://www.leaseweb.com/dedicated-servers/high-bandwidth-server#NL

additionally, the larger pools could somehow enforce or encourage use of proxies. 

maybe its enough? 

## kaldren | 2022-06-13T08:27:46+00:00
I hope this goes through. The only issue with Monero right now is the power minexmr has.

## tevador | 2022-07-14T21:26:42+00:00


I have implemented a proof-of-concept blockchain data selector. It turns out that selecting random blockchain data is more complicated than I thought when writing this proposal.

Firstly, we should clarify the performance targets. If we want to limit the cache lifespan to just 64 blocks, the generation time must definitely be under 1 second. Since a RandomX hash in light mode takes about 15 ms to calculate, a cache generation time of 1000 ms amortized over 64 blocks would be adding additional 15-16 ms, doubling the PoW cost of the initial blockchain download (IBD). Since the cost of IBD is dominated by non-PoW calculations, this might still be acceptable. The good news is that it would not affect the PoW costs of block verification for a synchronized node.

Looking at the [blockchain database scheme](https://github.com/monero-project/monero/blob/master/src/blockchain_db/lmdb/db_lmdb.cpp#L182-L214), I came to the conclusion that only two tables can be used: `blocks` and `txs_pruned`. The rest are either lookup tables or tables containing data that is not the same for all network nodes. Additionally, `blocks` and `txs_pruned` both use a sequential integer key, which makes it easy to select data at random.

To make the I/O cost of selecting data as favorable as possible, the data is read mostly sequentially in batches of 64 blocks or 64*N transactions, where `N` on average equals the mean number of transactions per block. Most of the database accesses use the `MDB_NEXT` cursor operation, with an occasional `MDB_SET` operation at the start of each batch. Block IDs and transaction IDs are selected pseudorandomly from the set starting with the genesis block and ending with the seed block. The seed block hash is used to seed the PRNG. The selection algorithm has a small bounded bias towards selecting data from recent blocks to make it unlikey that a cache can be constructed with stale blockchain data.

I tested several different selection techniques and different sets of parameters, but the method I just described seems to be close to optimal from a performance standpoint, while still providing significant randomization.

To further boost performance, the cache can be split into several segments and each segment can be initialized independently by a different thread. This can speed up the cache construction significantly when using an NVMe SSD to store the blockchain.

Finally, here are the performance numbers. I used a blockchain database that was obtained by running a node with `--prune-blockchain` and syncing the blockchain. All tests are for the worst-case scenario of a cold disk cache.

|storage hardware|1 thread|8 threads|
|----------------|--------|---------|
|NVMe SSD        | 15s    | 2.4s    |
|7200 RPM HDD    | 11min 30s | 13min 27s |

None of the hardware configurations came close to the 1 second performance target. The HDD numbers are especially brutal. But why is it so slow? We are only reading ~256 MB from the disk, aren't we?

Actually, the total amount of data read from the disk is over 2 GB! This is due to the way the data is stored in the LMDB database file. Normally, the data from all tables is interleaved as the database grows, which leads to significant fragmentation of the `blocks` and `txs_pruned` tables.

We can confirm this theory by using the command `./monero-blockchain-prune --copy-pruned-database`. This builds a copy of the pruned database with the data from each db table moved together.

With this "defragmented" database file, the performance is much better:

|storage hardware|1 thread|8 threads|
|----------------|--------|---------|
|NVMe SSD        | 3s    | 0.5s    |
|7200 RPM HDD    | 51s | 57s |

So the only configuration that can meet the initial performance target is using an NVMe SSD, 8 threads and a defragmented database file. These are not realistic conditions for a typical network node.

The conclusion is that without having a dedicated database file just for the cache selector (which would increase the required disk space to run a pruned node by ~25%), this proposal is probably not viable.

## tevador | 2022-07-16T15:22:01+00:00
After some discussion with @hyc on IRC, it seems that the low performance of the data selector is not caused by the database file fragmentation per se. The problem might be due to a mismatch between the LMDB page size and the page size of the storage device.

LMDB uses a page size equal to the virtual memory page, which is 4K on most systems. However, modern SSDs use larger pages of 8K-64K depending on the type of flash memory. Since the page is the smallest unit an SSD can read, a request to read a 4K LMDB page will actually load 8 pages into memory. The other 7 pages will most likely contain data from other tables, which results in the "read amplification" effect that I observed with the original blockchain database.

To confirm this theory, I applied the following patch to LMDB to increase the page size to 32K:

```diff
diff --git a/external/db_drivers/liblmdb/mdb.c b/external/db_drivers/liblmdb/mdb.c
index bf60c7013..d41c08d79 100644
--- a/external/db_drivers/liblmdb/mdb.c
+++ b/external/db_drivers/liblmdb/mdb.c
@@ -362,7 +362,7 @@ typedef HANDLE mdb_mutex_t, mdb_mutexref_t;
 #define        MDB_FDATASYNC(fd)       (!FlushFileBuffers(fd))
 #define        MDB_MSYNC(addr,len,flags)       (!FlushViewOfFile(addr,len))
 #define        ErrCode()       GetLastError()
-#define GET_PAGESIZE(x) {SYSTEM_INFO si; GetSystemInfo(&si); (x) = si.dwPageSize;}
+#define GET_PAGESIZE(x) ((x) = 32768)
 #define        close(fd)       (CloseHandle(fd) ? 0 : -1)
 #define        munmap(ptr,len) UnmapViewOfFile(ptr)
 #ifdef PROCESS_QUERY_LIMITED_INFORMATION
@@ -468,7 +468,7 @@ typedef pthread_mutex_t *mdb_mutexref_t;
         *      This is the basic size that the platform's memory manager uses, and is
         *      fundamental to the use of memory-mapped files.
         */
-#define        GET_PAGESIZE(x) ((x) = sysconf(_SC_PAGE_SIZE))
+#define        GET_PAGESIZE(x) ((x) = 32768)
 #endif

 #define        Z       MDB_FMT_Z       /**< printf/scanf format modifier for size_t */

```

I synced the blockchain again from the network and ran the same benchmarks as before:

|storage hardware|1 thread|8 threads|
|----------------|--------|---------|
|NVMe SSD        | 2.7s    | 0.44s    |
|7200 RPM HDD    | 2 min 13s | 2min 18s |

The performance of the SSD matches the results with the defragmented database, so I estimate that the hardware page size is 32K. However, I cannot explain why the HDD also got faster (HDDs usually use a sector size of 4K).

## minexmr2 | 2022-10-10T06:46:25+00:00
Hi! I propose a different and  (I hope) much more effective approach to defeat Monero mining centralization problem. I believe the mining protocol changes make a bad impact on the honest miners, while large centralized pools will find workaround cheap enough, given their money resources.

As you remember, when the largest centralized Monero mining pool called MineXMR.com disappeared, it did recommend for all the miners to migrate to decentralized p2pool.

Nevertheless today we observe exactly the same picture when MineXMR pool was in the scene: centralized Nanopool or SupportXMR pool get/share the place of MineXMR (nearly 1GH/s) in the overall pools' hashrate table (just see https://miningpoolstats.stream/monero). Decentralized p2pool grows a little bit and still under 200MH/s.

I was observing that sad picture for a while, and finally... I have implemented MineXMR2 pool:

https://minexmr2.com

MineXMR2 is completely open-source old-school Monero mining pool, resembling its predecessor MineXMR. No registration, no spying cookies, no personal data collection (even email).

Meanwhile MineXMR2 is a brand new in its idea to use decentralized p2pool as a hashrate-liquidity provider.

Indeed, MineXMR2 implementation (https://github.com/minexmr2/minexmr2, https://gitlab.com/minexmr/minexmr2) is based on https://github.com/jtgrassie/monero-pool. But I have rewritten/add more than 50% of code to redirect all the miners' hashrate to the internal p2pool instance. As a result, MineXMR2 performs all the PPLNS billing and make payout in useful 0.01XMR chunks, while p2pool does generate all the jobs for miners, and receives typical p2pool "dust" payouts in 0.0003-0.0005XMR chunks.

Thus, MineXMR2 seems to be centralized pool in some aspects, but actually its hashrate is completely redirected and contributed to decentralized p2pool. All the newbies that want to support p2pool can connect to MineXMR2 and get power of p2pool immediately, without having to build, deploy and maintain their own p2pool instance.

I ask you to popularize this open source solution amid all the pool owners, as they CAN use my open source pool implementation utilizing decentralized p2pool.

Also I believe there are methods how can I prove MineXMR2 is indeed running open source code. Please give me the links on how to establish and deploy that evidence. Currently one can check stratum protocol outputs to be the same as for p2pool v2.3.

P.S. I am NOT affiliated in any way with MineXMR pool's onwer. I am completely different person, known in bitcointalk.org as florida.haunted for many years.

## tevador | 2022-10-10T07:17:48+00:00
@minexmr2 

Your "solution" doesn't remove the pool operator's ability to use the pool hashrate for malicious purposes. So it doesn't actually solve anything.

## minexmr2 | 2022-10-10T14:54:49+00:00
> @minexmr2
> 
> Your "solution" doesn't remove the pool operator's ability to use the pool hashrate for malicious purposes. So it doesn't actually solve anything.

I believe there are methods how can I prove MineXMR2 is indeed running open source code. Please give me the links on how to establish and deploy that evidence. Currently one can check stratum protocol outputs to be the same as for p2pool v2.3.

## tevador | 2022-10-10T16:39:33+00:00
> prove MineXMR2 is indeed running open source code

Such a proof would be of little value. Since the pool admin is in control of the server, they can deploy malicious code at any time to hijack the miners connected to the pool. All centralized pools have this problem. Some mitigations might be possible in mining software to check that the block template given by the pool references the tip of the public chain.

## wowario | 2023-01-15T19:36:48+00:00
Hi @tevador

Do you have the proof-of-concept available somewhere? Wownero might give this a try for the next fork

## tevador | 2025-08-09T13:20:35+00:00
> It seems the bandwidth costs for pools are negligible

Here are some calculations from 2025.

Cloud data egress price starts at ~$0.01/GB ([DigitalOcean](https://docs.digitalocean.com/platform/billing/bandwidth/#droplets), but the pricing appears to be similar with other providers).

The pool bandwidth per miner connection would be ~3 GB/day, which would cost ~$0.03.

Assuming $300/XMR, 1% pool fee and network hashrate of 5 GH/s, the pool's daily revenue per miner is `c*R`, where `c = 2.6e-7 $/(H/s)` and `R` is the miner's hashrate. Considering the above costs, any miner with less than about 116 KH/s is costing the pool more money in bandwidth than the revenue from fees.

Since typical mining rigs rarely exceed 116 KH/s (except maybe some high end dual AMD Epyc machines) there are 3 ways how centralized pools could survive:

1. They would need to significantly raise their fees. At least a 6% fee would be needed to justify an average AMD Ryzen rig connecting to the pool. This would make p2pool a much more attractive alternative with zero fees.

2. They would refuse to bear the bandwidth cost and ask each miner to run their own node and an internal network for their multiple mining rigs. The amount of work and infrastructure needed for each miner would be similar to just using p2pool.

3. They would come up with some other method, e.g. a custom p2p network to distribute the data to miners. I can't imagine any solution significantly simpler than just using p2pool.

## Slixe | 2025-08-09T16:35:44+00:00
> > It seems the bandwidth costs for pools are negligible
> 
> Here are some calculations from 2025.
> 
> Cloud data egress price starts at ~$0.01/GB ([DigitalOcean](https://docs.digitalocean.com/platform/billing/bandwidth/#droplets), but the pricing appears to be similar with other providers).
> 
> The pool bandwidth per miner connection would be ~3 GB/day, which would cost ~$0.03.
> 
> Assuming $300/XMR, 1% pool fee and network hashrate of 5 GH/s, the pool's daily revenue per miner is `c*R`, where `c = 2.6e-7 $/(H/s)` and `R` is the miner's hashrate. Considering the above costs, any miner with less than about 116 KH/s is costing the pool more money in bandwidth than the revenue from fees.
> 
> Since typical mining rigs rarely exceed 116 KH/s (except maybe some high end dual AMD Epyc machines) there are 3 ways how centralized pools could survive:
> 
> 1. They would need to significantly raise their fees. At least a 6% fee would be needed to justify an average AMD Ryzen rig connecting to the pool. This would make p2pool a much more attractive alternative with zero fees.
> 2. They would refuse to bear the bandwidth cost and ask each miner to run their own node and an internal network for their multiple mining rigs. The amount of work and infrastructure needed for each miner would be similar to just using p2pool.
> 3. They would come up with some other method, e.g. a custom p2p network to distribute the data to miners. I can't imagine any solution significantly simpler than just using p2pool.

I'm not a fan of this, because this would actually create a centralization of pools to be only set on specific providers / datacenters / regions where such price is included and unlimited (OVH in Europe for example is completely included)

Also, this would be against one of the main reason of why pools exists: allow a small miner to actually have an average daily income by joining a pool, if they can't reach the minimal hashrate required, they will never solo mine, and thus they will just abandon the idea of mining Monero

## tevador | 2025-08-09T18:29:41+00:00
> Also, this would be against one of the main reason of why pools exists: allow a small miner to actually have an average daily income by joining a pool, if they can't reach the minimal hashrate required, they will never solo mine, and thus they will just abandon the idea of mining Monero

Small miners could still mine at p2pool, which would be unaffected by the bandwidth limitations. That's the point.

## plowsof | 2025-08-09T19:21:52+00:00
>OVH in Europe for example is completely included)

Unlimited bandwidth or unmetered bandwidth? Theres always a speed cap after certain amounts. I think you'll find there already is centralisation around cheap well performing servers, naturally. 

## tevador | 2025-08-09T19:45:46+00:00
Yes, it seems there is a hidden limit after which they reduce the speed significantly:

> OVHcloud reserves the right to restrict the VPS Service bandwidth to 1 Mbps (1 Megabit per second) until the end
of the current billing period in cases of excessive use by the Client.

## iamamyth | 2025-08-10T16:44:53+00:00
Like electricity, bandwidth obeys fundamental, physical limits. Eventually, those limits constrain the actions of economic actors. A cloud provider might adopt a resource-wasting policy in the short term (in fact, resource wasting models seem quite common in the current age), but eventually, will fold under the weight of that decision. I have seen smaller, niche providers offer a wide range of bandwidth prices over the last decade (much lower than the large cloud players), but eventually, they either go bankrupt or alter their pricing structure to impose a marginal cost on bandwidth. And, even "free" bandwidth runs up against per-machine physical limits, so ends up spilling over into compute costs (considering only compute, a single machine could in theory host a very large number of pool clients, but practically would have terrible performance characteristics because it would saturate the NIC, requiring multiple NICs and a mechanism for distributing traffic across them).

So, I don't think it matters whether a current provider offers unlimited, "free" bandwidth. And, though a bandwidth cost estimation might play a role in deciding the reseeding frequency, I suggest modeling costs based on prices offered by high-capacity, bandwidth-centered entities, such as CDNs.

## tevador | 2025-08-11T16:16:46+00:00
PoC code here: https://github.com/tevador/bc_selector

I think the performance issues are surmountable.

With 32 stripes (`--threads 32`), the cache can be built in about 4 seconds on an SSD with a quad core CPU and with a cold disk cache. With a hot disk cache, it takes <0.2 seconds.

HDD performance is much worse, taking about 10 minutes.

It's possible that some tweaks can be done to LMDB to improve the HDD performance to a usable level. @hyc can you take a look?

## hyc | 2025-08-11T16:44:19+00:00
OK, will take a look at your PoC.

## SamsungGalaxyPlayer | 2025-08-11T21:41:21+00:00
I think the most realistic outcome from this proposal is that small miners will be strongly disincentivized from participating in the network. Which is potentially fine, I just want to make sure this is called out.

Mining pools can continue to exist and cater to larger miners. For example, one realistic pool fee mechanism might be a minimum h/s to qualify for any rewards or to mine at all (so in effect a 100% fee on the first X h/s), then a more normal fee of ~1% on hashes over that. That would have limited harm on large miners but would kill small miners who would normally benefit the most from a centralized pool.

If we assume that mining pools switch to a dual-scale fee structure, then we need to carefully assign the mining costs. They would look something like this:

Bandwidth
- P2Pool: paid by miner (potentially no cost to miner)
- Pool: paid by pool, possibly 100% of fee assigned to miner

Node storage costs
- P2Pool: paid by miner
- Pool: paid by pool (only one needed total, not 1 per miner; cost per miner approaches zero)

Fees
- P2Pool: None
- Pool: Whatever the pool sets (e.g. 1%)

For miners, the savings of not needing to run a node can still exceed the mining pool fees. The formula is:

P2Pool Advantage = Cost of User Bandwidth - Fees for Pool Bandwidth - Cost to Run Node + Pool Fees

In summary, this proposal *reduces* the competitiveness of the following:
- Small miners who aren't using P2Pool
- Miners on a metered internet connection
- Mining pools (less competitive, but still competitive if they react accordingly)

It increases the competitiveness, at least in relative terms, of the following:
- Existing P2Pool miners
- Miners who don't pay for bandwidth (they can mine with P2Pool to avoid incurring a pool's share of these fees)

## MoneroOcean | 2025-08-11T22:24:37+00:00
There should also be changes in miners to either support building the RX cache from a local node or preloading the RX cache from the pool, because in practice it’s difficult to upload a 256 MB file to 100 miners simultaneously in under a minute on typical VPS providers.

## tevador | 2025-08-12T04:39:42+00:00
> because in practice it’s difficult to upload a 256 MB file to 100 miners simultaneously in under a minute on typical VPS providers.

There will be a 10-block delay between the seed block and the RandomX epoch change. In practice, if pools want a 95%+ chance to upload the data to their miners in time, they have about a 10 minute window for it. This will exacerbate the bandwidth constraints for pools because most of the bandwidth will be used in 10 minute windows every 2 hours.

Uploading 256 MiB to 100 miners in 10 minutes requires a stable uplink of ~360 Mbps.

> one realistic pool fee mechanism might be a minimum h/s to qualify for any rewards

Pools will need some mechanism to prevent miners below te minimum hashrate from even connecting to the pool. Otherwise a 1 KH/s hobby miner can still connect to the pool and the pool will be losing money even with a 100% fee. It's a also a DoS vector against centralized pools. A "miner" can connect, download the 256 MiB cache and then just disconnect. I think centralized pools will need to implement some PoW hashrate proof for miners to qualify for the cache download, if the cache distribution is done by the pool.

> P2Pool Advantage = Cost of User Bandwidth - Fees for Pool Bandwidth - Cost to Run Node + Pool Fees

This should be:

P2Pool Advantage = Cost of User Bandwidth **+** Fees for Pool Bandwidth - Cost to Run Node + Pool Fees

The only cost of mining at P2Pool is running a node. This proposal does not introduce any additional bandwidth cost to P2Pool users.

The current P2Pool advantage is: Pool Fees - Cost to Run Node. Since (Cost of User Bandwidth + Fees for Pool Bandwidth) is always positive, this will incentivize the use of P2Pool.

It's clear that the pool fees are not enough themselves to attract users to P2Pool as we have seen over the past years, with P2Pool staying around 5% of the network hashrate.

Additionally, this proposal has a good potential to disrupt the hashrate rental market, which would be a strongly positive outcome for network security. Hashrate rental services are much less likely to support a special pool protocol just for Monero.

## MoneroOcean | 2025-08-12T04:52:15+00:00
For our pool, I will likely disable XMR mining by default unless the miner can signal that it can generate the RX cache from its own blockchain (likely via the MO version of XMRig if the vanilla one will not support it). All other RX/0 miners will be switched to Tari RX/0. This approach should minimize disruption for miners and provide them with a gradual path to upgrade to XMR RX/0 mining.

By the way, is there any confidence that this change would actually mitigate the current selfish mining issue? I’m assuming the renewed interest in this proposal is related to that. If most of the selfish mining hashrate originates from a single datacenter, this method would not impact them as significantly as it would other Monero pools.

## One-horse-wagon | 2025-08-14T15:11:24+00:00
For small miners, setting up with P2Pool is not as easy as with other pools.  So, a number get discouraged and stay with the other pools.  However, in the three years since this proposal has come out, artificial intelligence (AI) has greatly improved.  IMO, AI will have an impact on increasing the number of small miners using P2Pool because it provides the needed help in the initial set-up.

I am very much in favor of tevador's proposal as it appears to be a viable way forward for Monero, especially with the blossoming of AI.

## tevador | 2025-08-16T16:13:51+00:00
I think the performance issues have been largely resolved by [increasing the LMDB page size](https://github.com/tevador/bc_selector/pull/3). This change is backwards compatible with existing blockchain files (although they will not benefit from the speed up).

With a page size of 16K (instead of the default 4K), the PoC can construct the cache in ~1 second on an SSD and in ~3 minutes on an HDD.

For nodes syncing on a spinning disk, it would add roughly 8 days of sync time per year of blocks. For nodes syncing on an SSD, it would add roughly 1 hour of sync time per year of blocks. These are worst-case estimates assuming the node can do nothing else while the RandomX cache is being constructed.

The HDD performance could be improved by further increasing the page size, but this would have to be optional as there are drawbacks for SSDs.

## hnougher | 2025-08-17T03:02:55+00:00
Distributing a 256MB static file without load on the pool is relatively easy with slightly customised mining software.
Considering someone malicious will not care how they do it, I have thought of these options:

Method 1: Use CDN, like Cloudflare HTTP cache.
Method 2: Use Torrent technology for P2P distribution (with or without trackers).

Both of these put minimal load on the centralised pool bandwidth, not much more than the load on client bandwidth.
It even works in really well with HTTP caching proxies, or many nodes on one subnet for local P2P.

The only deterrent for clients and botnet is if the client Internet connection has a data limit.

## tevador | 2025-08-17T08:49:46+00:00
> Distributing a 256MB static file

It's not static. It changes every 64 blocks.

> Cloudflare HTTP cache

Cloudflare HTTP cache is only for storing website files (html, css, js etc.). Large binary files are explicitly forbidden in their ToS.

Yes, it's possible to use a CDN, but not without paying for bandwidth.

## sneurlax | 2025-08-18T23:22:08+00:00
This seems like it would lead to more centralization, no?  I don't see how requiring miners to dedicate more resources to the task will decentralize mining.

Is this going to be easy to re-implement or integrate in independent codebases and codebases in other languages, using, for example, data we know all nodes must retain?  Or will this lock us into monero-project/monero itself even longer, further centralizing the Monero ecosystem and locking it into one working implementation?



## tevador | 2025-08-19T04:29:48+00:00
> This seems like it would lead to more centralization, no? I don't see how requiring miners to dedicate more resources to the task will decentralize mining.

Only centralized pools will be hit with the additional requirements. P2Pool and solo miners already have the data that will be required for mining. This should actually promote decentralization.

The status quo leads to centralization, with hashrate concentrating the top 2-3 pools, so something has to be done.

> Is this going to be easy to re-implement or integrate in independent codebases and codebases in other languages, using, for example, data we know all nodes must retain? Or will this lock us into monero-project/monero itself even longer, further centralizing the Monero ecosystem and locking it into one working implementation?

This proposal is using raw blockchain data, which have the same format in all languages and implementations. Only non-prunable data is used, so running a pruned node is sufficient.


## nahuhh | 2025-08-19T14:00:11+00:00
> P2Pool and solo miners already have the data that will be required for mining.

AIUI, a large portion of p2pool miners are using remote nodes

## tevador | 2025-08-19T16:13:57+00:00
> a large portion of p2pool miners are using remote nodes

Can you specify what counts as a remote node? Does this refer to all cases when monerod is running on a different machine than the mining software? That does not necessarily mean there would be any bandwidth penalty.

## nahuhh | 2025-08-19T16:42:31+00:00
Remote in this case, would be referring to solutions like gupax where p2pool connects to monero nodes run by community members on several VPS

## tevador | 2025-08-19T17:23:40+00:00
Yes, this particular case would be affected in the same way as a centralized pool, with the VPS operator having to pay for the bandwidth consumed by their miners.

A small number of miners connecting to a VPS should probably still be fine (the bandwidth requirements are around 100 GB/miner/month).

A typical setup which would not be affected would be a dedicated machine running monerod and several mining rigs connecting to it from the local network.

## nahuhh | 2025-08-19T17:32:39+00:00
How would this effect

1. Run monerod and p2pool on the vps
2. Connect home miners to p2pool on the vps?

Do the home miners incur bandwidth costs, or is the 3gb/day between monerod->p2pool?
If the latter, what would prevent pools from running atop p2pool?

## tevador | 2025-08-19T17:45:11+00:00
The bandwidth is between monerod and whoever needs to calculate PoW hashes. This is typically the mining software, but p2pool software also calculates PoW hashes (to validate shares), so it also needs the data.

The only way to avoid the bandwidth penalty would be to run a node locally. I was under the assumption that all p2pool miners already did this, so thanks for the clarification.

## One-horse-wagon | 2025-08-21T13:24:14+00:00
I don't think there should be a concern about miners that don't run a node locally.  It would not be a big step for the the dedicated Monero miners to start one up and they would gladly do so if the protocol called for it.  For the really small miners, some would do it and others not.  In the process of tightening up the mining process, there will be some initial loss of miners which can't be avoided.  But if the new protocol discourages rogue and crooked miners, it needs to be implemented.

And let's be realistic.   It doesn't take much to maintain a full local node.   

## nahuhh | 2025-08-21T13:32:13+00:00
> But if the new protocol discourages rogue and crooked miners, it needs to be implemented.
>
> And let's be realistic. It doesn't take much to maintain a full local node.


Right, but imo an entity like qubic likely has no problem either running nodes or covering the bandwidth. I feel that this solves an old problem (botnets), but by doing so, would strengthen todays problem - selfish mining by a publuc entity. 51% etc would be easier _today_ if we dropped botnets w/o first addressing the attack

## PPPDUD | 2025-08-27T22:21:06+00:00
> > P2Pool and solo miners already have the data that will be required for mining.
> 
> AIUI, a large portion of p2pool miners are using remote nodes

Most of those miners originate from botnets, so encouraging local node hosting would dramatically decrease the viability of cryptomining malware. I think that the vast majority of people who would install a cryptominer by mistake would be quite alarmed by ~100GB of space suddenly becoming unavailable.

## PPPDUD | 2025-08-27T22:22:38+00:00
> How would this effect
> 
> 1. Run monerod and p2pool on the vps
> 2. Connect home miners to p2pool on the vps?
> 

Why would you pay for a VPS to run a node if you can run the mining software at home?

If you can't afford a 500GB external hard drive, you probably can't afford a good computer anyway.

## breadvsrice | 2025-08-31T03:06:40+00:00
Can't we just implement someway to reward miners for their work as part of the P2P node-node implementation? The only reason people join mining pools is to have a better chance of getting something vs nothing. If there was some implementation to reward miners for solving a lower difficulty or separate puzzle, without breaking the blockchain, nobody would join a pool. Maybe a lower-difficulty solution gets added to the transaction pool somehow, idk...it would need to be pulled into a block though, but still...?

## tevador | 2025-08-31T10:17:25+00:00
> Can't we just implement someway to reward miners for their work as part of the P2P node-node implementation? The only reason people join mining pools is to have a better chance of getting something vs nothing. If there was some implementation to reward miners for solving a lower difficulty or separate puzzle, without breaking the blockchain, nobody would join a pool. Maybe a lower-difficulty solution gets added to the transaction pool somehow, idk...it would need to be pulled into a block though, but still...?

You are basically describing P2Pool. Lower difficulty solutions get added to the P2Pool blockchain and are eligible for Monero rewards once a block is found.

## lmb | 2025-09-15T14:20:07+00:00
> Cloudflare HTTP cache is only for storing website files (html, css, js etc.). Large binary files are explicitly forbidden in their ToS.
> 
> Yes, it's possible to use a CDN, but not without paying for bandwidth.

People regularly abuse providers like Cloudflare to run illegal streaming websites. Bandwidth at this scale is approximately free to large providers which has implications for how much resources they expend to fight abuse. Looking at ToS is not useful: they exist as a post facto justification for terminating service when the abuse gets too egregious. (Source: used to work as such a place.)

# Action History
- Created by: tevador | 2022-02-16T19:53:13+00:00
