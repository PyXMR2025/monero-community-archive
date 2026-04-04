---
title: 'Cuprate Meeting #34 - Tuesday, 2024-12-17, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1122
author: moo900
assignees: []
labels: []
created_at: '2024-12-10T18:44:26+00:00'
updated_at: '2024-12-17T19:20:20+00:00'
type: issue
status: closed
closed_at: '2024-12-17T19:11:00+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Any other business

Previous meeting with logs: #1118

# Discussion History
## moo900 | 2024-12-17T19:10:59+00:00
## Meeting logs
```
boog900: !meeting 
```
```
boog900: meeting time: https://github.com/monero-project/meta/issues/1122
```
```
boog900: 1) Greetings
```
```
syntheticbird: Hello
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
boog900: me: I haven't spent much time on Cuprate the last week, I'm back now though and will PR a temporary fix for heed's `get_range` in a couple hours
```
```
hinto: me:

- Implemented an `Entry` API for `cuprate_database`: https://github.com/Cuprate/cuprate/pull/358
- Finished at least a draft for all RPC handler functions yesterday, will be ready for review hopefully within 2 weeks: https://github.com/Cuprate/cuprate/pull/355
- Created a testing harness for `monerod` <-> `cuprated` compatibility: https://github.com/Cuprate/cuprate/pull/357
```
```
hinto: <image>
```
```
hinto: I forget how moo handles non-text messages so for the record that is a gif of the testing harness processing all blocks
```
```
syntheticbird: High quality asciinema GIF?
```
```
syntheticbird: In my cuprate chat
```
```
syntheticbird:  * In my cuprate chat?
```
```
syntheticbird: wonderful
```
```
boog900: yeah that does look nice
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: I really need to update the website
```
```
syntheticbird: and link the docs
```
```
syntheticbird: Oh also my first and last test of cuprated in init branch resulted in an halt and slow performance. I actually think it was caused by my disk setup. I'm gonna retest very soon and measure it then make a nice gnuplot out of it
```
```
syntheticbird: I'll wait for the get_range fix
```
```
hinto: I mentioned this in another meeting but I have plans for RPC input/output compatibility testing (which I think I will add to this testing harness).

I don't think it's actually as complicated as I thought it would be, something like this could work:

/// represents a `monerod/cuprated` RPC request type.
trait RpcRequest {
    /// the expected response type, potentially only being a subset of the fields.
    type SubsetOfResponse: PartialEq;

    /// create a 'base' request.
    fn base() -> Self;

    /// permutate the base request into all (or practically) possible requests.
    // e.g. `{"height":0}`, `{"height":1}`, etc
    fn all_possible_inputs_for_rpc_request(self) -> Vec<Self>;

    /// send the request, get the response.
    ///
    /// `monerod` and `cuprated` are both expected to be fully synced.
    fn get(self, node: Node) -> Self::SubsetOfResponse;
}

enum Node {
    Monerod,
    Cuprated,
}

// all RPC requests.
let all_rpc_requests: Vec<dyn RpcRequest> = todo!();

// for each request...
for base in all_rpc_requests {
    // create all possible inputs...
    let requests = all_possible_inputs_for_rpc_request(base);

    // for each input permutation...
    for r in requests {
        // assert (a potential subset of) `monerod` and `cuprated`'s response fields match in value.
        let monerod_response = r.get(Node::Monerod);
        let cuprated_response = r.get(Node::Cuprated);
        assert_eq!(
            monerod_response.subset_of_response(),
            cuprated_response.subset_of_response(),
        );
    }
}
```
```
hinto: Basically, for each request, create all (practical) inputs and assert (at least a subset) of `monerod` and `cuprated`'s output values are the same
```
```
syntheticbird: literally atheris library
```
```
syntheticbird: that will be great
```
```
syntheticbird: the snippet looks simple and sane to me
```
```
hinto: The caveat is that these tests take forever because of `monerod`'s RPC throughput, due to a few things but this almost decade old line definitely does not help: https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/src/daemon/rpc.h#L75
```
```
hinto: I'm currently using a custom `monerod` because the verifier threadpool can verify blocks an order of magnitude faster than they can be fetched from a release `monerod`
```
```
hinto: tewinget strikes again with a long lasting yet myopic decision
```
```
syntheticbird: > <@hinto:monero.social> tewinget strikes again with a long lasting yet myopic decision

lmfao
```
```
hinto: boog900: do you have any thoughts on how RandomX's full memory mode would be integrated into `cuprated`?
```
```
boog900: monerod uses and env variable, I think ideally it should be part of the config   
```
```
boog900:  * monerod uses an env variable, I think ideally it should be part of the config   
```
```
boog900: it shouldn't be too hard to do I think
```
```
hinto: I meant the re-initialization of the dataset every 2048 blocks, I'm not sure how `monerod/xmrig` do it actually, I would assume they don't it on the spot
```
```
boog900: ah well we already have most of the code for that: https://github.com/Cuprate/cuprate/blob/main/consensus/context/src/rx_vms.rs
```
```
boog900: just need to add a dataset field here I would've thought: https://github.com/Cuprate/cuprate/blob/7b8756fa80e386fb04173d8220c15c86bf9f9888/consensus/context/src/rx_vms.rs#L36
```
```
hinto: This is a bottleneck because the verifying threadpool (at least, a larger one) can verify 2048 blocks faster than creating the dataset
```
```
hinto: Does that code pre-create the dataset? I thought about adding some pipelining to prepare it before the next batch comes around but it's a bit more complicated to impl
```
```
hinto: Pre-create as in, before the next seed hash comes, a full-memory VM with that seed is already ready
```
```
syntheticbird: I love pipelining
```
```
boog900: yes it creates it as soon as the seed block is seen (64 blocks before it activates): https://github.com/Cuprate/cuprate/blob/7b8756fa80e386fb04173d8220c15c86bf9f9888/consensus/context/src/rx_vms.rs#L226 although it immediately waits for its creation 
```
```
boog900: it's created on the next call for vms: https://github.com/Cuprate/cuprate/blob/7b8756fa80e386fb04173d8220c15c86bf9f9888/consensus/context/src/rx_vms.rs#L187
```
```
hinto: Is there a mechanism for old VMs to be dropped? Full memory mode will use a lot of memory if a VM for each seed is held
```
```
boog900: yeah we hold 2 VMs at a time, monerod will only hold 1 full VM though, if full VMs are enabled
```
```
hinto: do you know how xmrig does it?
```
```
boog900: nope
```
```
syntheticbird: I've a question before the end of the hour
```
```
boog900: go ahead
```
```
syntheticbird: what's your stance on GPU usage for Bulletproof(+) ? Vulkan is a well established API, and have computation layers. This has been brought in MRL at some point and I think it could be beneficial
```
```
syntheticbird: There are other APIs obviously
```
```
syntheticbird: But main point is if Cuprate could see an optional GPU acceleration support
```
```
boog900: I wouldn't want it to be the only option, but if it gives a significant performance boost and is audited, then I don't see why it shouldn't be included.
```
```
boog900: anything else anyone wants to discuss?
```
```
boog900: I think we can end here
```
```
boog900: thanks everyone! 
```
```
hinto: thanks
```

# Action History
- Created by: moo900 | 2024-12-10T18:44:26+00:00
- Closed at: 2024-12-17T19:11:00+00:00
