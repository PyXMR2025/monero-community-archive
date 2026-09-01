---
title: 'Node incentives vs. tail emission: is "self-interest is enough" a deliberate
  design bet, or has it been researched?'
source_url: https://github.com/monero-project/research-lab/issues/162
author: Bpivat
assignees: []
labels: []
created_at: '2026-08-24T18:16:21+00:00'
updated_at: '2026-08-31T17:38:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm setting up a pruned full node (not mining) on a small always-on machine, for the standard reasons: sovereign verification of my own transactions, contributing to network decentralization, not depending on a remote node.

Reading the tail emission documentation, the stated purpose is explicit: pay miners forever because mining is the costly, hard-to-fake resource that secures block production — without payment, hashrate (and thus security) would drop. That reasoning is clear and makes sense to me.

What I can't find anywhere — official docs, Moneropedia, this repo's history — is the equivalent reasoning for full nodes. The implicit answer seems to be "node operators are compensated by self-interest, not by the protocol," which is coherent, but I've never seen it stated and defended as a deliberate design decision — only assumed by omission.

Three concrete questions:

Is "self-interest, not protocol payment" a conscious economic model MRL has actually reasoned through and endorsed (as opposed to proof-of-work security), or is it inherited from Bitcoin's assumptions without being independently re-examined for Monero's specific threat model?
Is the obvious objection — that unpaid node-running pushes non-technical users toward a handful of remote nodes, re-centralizing exactly what full nodes are meant to prevent — considered a real risk, or judged negligible? Is there any data (node count over time, remote-node usage share) that settles this either way?
Has a node-incentive design ever been seriously modeled for Monero (in the spirit of the fee-market or tail-emission-size discussions in this repo, e.g. #150, #152) and rejected — and if so, on what grounds? Sybil-resistance is the obvious blocker, but I'd like to know if that's actually the argument that killed it, or just the assumed one.

I'm not asking because I expect a node to get "paid" — I understand it isn't a scarce/costly resource the way hashrate is, and payment-per-node is trivially Sybil-able. I'm asking because the asymmetry (miners paid forever, node operators never) is publicly justified on one side of the pair but not the other, and I'd like to know whether that's a settled, examined position or an inherited assumption nobody's revisited.

# Discussion History
## viktor4096 | 2026-08-29T05:20:38+00:00
If it's specifically for full nodes:

Each pruned node belongs to a bucket. Every node in a single bucket with have deterministically pruned the same data. So, when the pruned data is needed, the node reaches out to other nodes that will have the data.

So, even with all pruned nodes, it shouldn't be an issue for the whole network to have all the blockchain data. However, it would require having enough pruned nodes spread throughout the network.

As for getting paid for hosting a node, there was pay-for-RPC feature but it's deprecated now as it was not popular + difficult to implement for wallets (iirc, only the official wallets supported it).

## fluffypony | 2026-08-29T09:01:36+00:00
> Is "self-interest, not protocol payment" a conscious economic model MRL has actually reasoned through and endorsed

It’s been discussed at length. The challenge is that you ultimately end up with something that can trivially be gamed (eg. imagine a swarm of Sybil nodes that merely proxy requests back to “real” nodes, incurring no data storage costs while passing any “proof of node” test you throw at it)...or you end up with something centralised (eg. Tor dirauth).

Even if you have something significantly complex and multi-homed, you’ll struggle with things like proof of service (a node gets paid for relaying a tx, but you have to trust it actually does relay it), and you just create a heap of attack vectors for sophisticated threat actors.

The reason you run a full node is simple: you run it for you, to validate your transactions. You don’t run it for anyone else. Helping other people on the network is a side-effect, not the purpose.

## Bpivat | 2026-08-30T08:52:40+00:00
Thanks to both of you — this is exactly the kind of answer I was after.

@fluffypony — that settles the main question for me: the asymmetry is a deliberate, examined position, not an inherited Bitcoin assumption, and Sybil-resistance is the actual blocker rather than a hand-wave. The "gameable proxy swarm on one side, Tor-dirauth-style centralisation on the other" framing is the crux, and the proof-of-service problem (paying for relay you can't verify) is a cleaner statement of it than I'd managed myself. The "you run it for you, helping others is a side-effect" point lands too.

One follow-up: you say it's been discussed at length. Is any of that discussion written down somewhere I could cite — an MRL meeting log, an IRC/Matrix thread, an old issue — rather than folklore? Not because I doubt it, but because "self-interest, not protocol payment" being a documented, defended decision (vs. an assumption by omission) was the whole gap I ran into, and a linkable trace would close it for the next person who goes looking.

@viktor4096 — the pruned-node bucket explanation is helpful, and the pay-for-RPC precedent is precisely the kind of concrete "tried and dropped" data point I was hoping existed. Do you happen to know if there's anything measured on the other half of my second question — node count over time, or the share of wallets hitting remote nodes vs. their own? Even rough figures would help gauge whether the recentralisation risk is materialising in practice or staying theoretical.

Either way, thanks — happy to have this on the record.

## fluffypony | 2026-08-30T09:32:38+00:00
> One follow-up: you say it's been discussed at length. Is any of that discussion written down somewhere I could cite — an MRL meeting log, an IRC/Matrix thread, an old issue — rather than folklore? Not because I doubt it, but because "self-interest, not protocol payment" being a documented, defended decision (vs. an assumption by omission) was the whole gap I ran into, and a linkable trace would close it for the next person who goes looking.

I don't believe there's anything canonical I can point to - a lot of this stuff is buried in IRC logs over the last 10 years. I think this GitHub issue is a good canonical point of reference, and I'm sure other MRL members can weigh in as and when they have additional thoughts about this.

## Bpivat | 2026-08-30T09:52:50+00:00
Following up on my second question — whether the recentralisation concern is materialising in practice or staying theoretical — I went looking for public data. Putting it here so the trace is on the record, and happy to be corrected by anyone with better numbers.

The most rigorous recent snapshot I found is ProbeLab's network crawl (24 Feb 2026)[[1](https://probelab.io/blog/peering-into-privacy-a-deep-dive-into-the-monero-network-topology/)]. A few figures stand out for this thread:

- Of the ~16–17k reachable nodes, **81.6% were spy nodes** (13,420) — and all of them traced back to a single AS (Spruce Creek Networks). Stripping those out leaves only **~2,944 "legitimate" nodes**. So the honest network is an order of magnitude smaller than the raw count suggests — worth flagging any time a headline node number gets cited.
- **8.1% pruned vs 91.9% full**, which lines up with @viktor4096's bucket point: pruned nodes are a small minority, so their even distribution matters more, not less.
- Only **5.4% of nodes expose a public RPC** (883 reachable providers). That's the concrete pressure point for my second question: every wallet on a remote node is leaning on fewer than 900 public endpoints — and, per the surveillance angle below, an unknown share of those are hostile.

On that surveillance angle specifically, it's already a documented concern in-repo: monero-project/meta#1079 ("The Public Remote Node Problem")[[2](https://github.com/monero-project/meta/issues/1079)] lays out the exact mechanism — a party can run a public remote node and correlate connecting users' IPs with the txs they push (Chainalysis is named). So the "unpaid node-running pushes non-technical users toward a handful of remote nodes" objection isn't hypothetical; it has a named threat model and a small, partly-adversarial serving set.

There's also an academic preprint (arXiv 2509.10214, summarised by TRM Labs[[3](https://www.trmlabs.com/resources/blog/monero-in-2025-persistent-use-and-emerging-network-layer-insights)]) reporting ~14–15% of reachable peers with non-standard behaviour, consistent with the spy-node picture.

Honest caveat: these are **snapshots**, not a clean time series. I couldn't find a reliable "honest node count over time" curve — the raw public counters are themselves distorted by the spy-node flooding, which makes the *trajectory* question genuinely hard to answer. So: strong evidence on the *current* state of (re)centralisation, weak evidence on the trend.

Net, for the record: the asymmetry @fluffypony described — you run a node for yourself, helping others is a side-effect — isn't just a clean design position; the data suggests the failure mode it implies (few public serving nodes, some adversarial) is visibly present today. If anything that strengthens the "run your own" conclusion rather than reopening the "pay the nodes" one — the proof-of-service problem still sits squarely in the way of the latter.

[1]: https://probelab.io/blog/peering-into-privacy-a-deep-dive-into-the-monero-network-topology/
[2]: https://github.com/monero-project/meta/issues/1079
[3]: https://www.trmlabs.com/resources/blog/monero-in-2025-persistent-use-and-emerging-network-layer-insights

## Rucknium | 2026-08-31T17:36:26+00:00
Please disclose AI LLM use when posting issues here.

I maintain https://xmrnetscan.redteam.cash/ , which has a (mostly) uninterrupted reachable node count for the last year. My counts differ from ProbeLab's because  I count nodes that are on different ports, but on the same IP address, as a single node. The spy node metric only counts nodes that have a specific spy node response behavior. Lately, it looks like some spy nodes without the spy node fingerprint have appeared and disappeared on the network a few times.

Both my number and ProbeLab's number only count the reachable nodes, i.e. nodes that have open ports. Unreachable nodes may outnumber reachable nodes by 5-to-1 or 10-to-1. You can get a rough idea by checking the inbound connection count of a reachable node that you operate. Input `status` in the `monerod` console. I usually see inbound counts above one hundred. Nodes' default number of outbound connections is 12. So subtract 12 from the number of your inbound connections (you subtract the average number of reachable nodes' outbound connections connecting to your node), then divide that number by 12. That's approximately how many unreachable nodes are on the network, assuming all nodes use the default 12 outbound connections.

AFAIK, the incentives to running a node haven't been modeled rigorously. It's hard because there are too many unknowns and unknowables. Usually, you would approach research like this by starting with a [willingness to pay](https://en.wikipedia.org/wiki/Willingness_to_pay) survey of the market participants. Getting a representative sample of Monero users to answer a survey like that is going to be very difficult. If you want to see some pretty rigorous modeling on the adversary side, see my ["Subnet Deduplication for Monero Node Peer Selection"](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf), especially Section 4. My suggestion in the paper was implemented in the node code: https://github.com/monero-project/monero/pull/9939

# Action History
- Created by: Bpivat | 2026-08-24T18:16:21+00:00
