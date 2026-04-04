---
title: 'Research meeting: 13 May 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/462
author: SarangNoether
assignees: []
labels: []
created_at: '2020-05-09T17:33:27+00:00'
updated_at: '2020-05-13T17:51:19+00:00'
type: issue
status: closed
closed_at: '2020-05-13T17:51:19+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 13 May 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## Mitchellpkt | 2020-05-13T16:37:16+00:00
Updated proposal to researching post-quantum strategies for Monero: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/142

Incorporated community feedback to focus on the audit and writeups to disseminate information. The research results will initially be articulated/documented along the lines of:
> Monero's [component] is vulnerable to [impact] by a hypothetical adversary that can leverage [algorithm]. In general, the solution must meet [requirements]. Current relevant methods include [cryptosystem] which would require [migration process] and has [tradeoffs] that would prevent implementation until [device bandwidth/resource threshold] is widely available.

Throughout this entire project, the community will receive updates during the weekly #monero-research-lab meetings, and key deliverables from this research will be freely published in several forms:

1. **User-friendly writeup**: This community-facing writeup will provide an approachable explanation of how hypothetical quantum computers may impact Monero, and possible future mitigations. The writeup should minimize FUD and provide the context that these vulnerabilities apply to almost all cryptocurrencies (not only Monero).
2. **Technical documentation**: An MRL position paper to distill key information for (current and future) researchers and developers. The writeup should formally describe vulnerabilities, and highlight potential strategies and solutions, noting their tradeoffs. Code snippets may be included if appropriate for pedagogical purposes or clarity.
3. **Non-technical 1-pager**: An ELI5 / TL;DR summary will be provided for journalists, Monero Outreach, etc. This blurb will discuss risks and myths with no technical jargon, with key takeaways that a broad audience will appreciate.

Results and updates will be also disseminated via Twitter threads, Reddit posts, etc, and we would love to share key takeaways through the Breaking Monero series.

## SarangNoether | 2020-05-13T17:51:19+00:00
    [2020-05-13 13:00:03] <sarang> First, GREETINGS
    [2020-05-13 13:00:08] <sarang> Hi
    [2020-05-13 13:00:59] <binaryFate> hello!
    [2020-05-13 13:01:01] ⇐ Inge- quit (~inge@17-231-47-212.rev.cloud.scaleway.com): Ping timeout: 246 seconds
    [2020-05-13 13:01:14] <Isthmus> Heyo
    [2020-05-13 13:01:30] <h4sh3d[m]> Hello
    [2020-05-13 13:01:53] → Inge- joined (~inge@17-231-47-212.rev.cloud.scaleway.com)
    [2020-05-13 13:02:11] <ArticMine> Hi
    [2020-05-13 13:02:54] <sarang> Next up is ROUNDTABLE
    [2020-05-13 13:02:55] <rehrar> hi
    [2020-05-13 13:03:05] <sarang> Does anyone have research of interest to share with the group?
    [2020-05-13 13:03:15] <sarang> I know Isthmus just mentioned something before we started
    [2020-05-13 13:03:55] <Isthmus> Hey everybody. I incorporated y'all's feedback on the research proposal (thanks for your input), updated version here: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/142
    [2020-05-13 13:04:00] <Isthmus> Most of the changes are in the Roadmap section
    [2020-05-13 13:04:51] <Isthmus> For phase 1 we've switched to a very formal enumeration of adversary capabilities and Monero features of interest, and will document possible issues and solutions along the lines of:
    [2020-05-13 13:04:58] <Isthmus> "Monero's [component] is vulnerable to [impact] by a hypothetical adversary that can leverage [algorithm]. In general, the solution must meet [requirements]. Current relevant methods include [cryptosystem] which would require [migration process] and has [tradeoffs] that would prevent implementation until [device bandwidth/resource threshold] is widely available."
    [2020-05-13 13:05:10] <Isthmus> Throughout this entire project, the community will receive updates during the weekly #monero-research-lab meetings. During phase 3 however, several specific documents (the key deliverables from this research) will be freely published:
    [2020-05-13 13:05:15] <Isthmus> 1. User-friendly writeup: This community-facing writeup will provide an approachable explanation of how hypothetical quantum computers may impact Monero, and possible future mitigations. The writeup should minimize FUD and provide the context that these vulnerabilities apply to almost all cryptocurrencies (not only Monero).
    [2020-05-13 13:05:21] <Isthmus> 2. Technical documentation: An MRL position paper to distill key information for (current and future) researchers and developers. The writeup should formally describe vulnerabilities, and highlight potential strategies and solutions, noting their tradeoffs. Code snippets may be included if appropriate for pedagogical purposes or clarity.
    [2020-05-13 13:05:26] <Isthmus> 3. Non-technical 1-pager: An ELI5 / TL;DR summary will be provided for journalists, Monero Outreach, etc. This blurb will discuss risks and myths with no technical jargon, with key takeaways that a broad audience will appreciate.
    [2020-05-13 13:05:32] <Isthmus> Results and updates will be also disseminated via Twitter threads, Reddit posts, and Breaking Monero videos. :- )
    [2020-05-13 13:05:56] <Isthmus> (ends notes)
    [2020-05-13 13:06:09] <Isthmus> Oh, I'll X-post the proposal to Reddit today
    [2020-05-13 13:06:20] <sarang> I like the change in scope, particularly focusing on communicating the current state of the protocol
    [2020-05-13 13:06:51] <sarang> Moving away from specific things like implementations and proofs-of-concept for changes seems wise, especially considering that the state of the art will change
    [2020-05-13 13:07:15] <Isthmus> ^ yep
    [2020-05-13 13:07:15] <Isthmus> It's important to note that many current post-quantum cryptography candidates require large proofs and significant computational resources, and will thus not be suitable for immediate deployment. For this reason, understanding broad strategies and their tradeoff will be more useful than specific implementations. Thankfully, consumer device capabilities increase over time, and researchers continue to
    [2020-05-13 13:07:15] <Isthmus> discover new faster/smaller proving systems, so these practical barriers are temporary.
    [2020-05-13 13:08:45] <sarang> Were there any questions for Isthmus about this proposal? (Comments could also be made on the proposal itself to reach a wider audience)
    [2020-05-13 13:09:13] <rehrar> nop
    [2020-05-13 13:09:52] <sarang> OK, does anyone else wish to share research of interest?
    [2020-05-13 13:10:19] <sarang> If not, I have a few items to share
    [2020-05-13 13:10:39] <h4sh3d[m]> Yes, I have something
    [2020-05-13 13:10:55] <h4sh3d[m]> Earlier someone posted this: https://gist.github.com/RubenSomsen/8853a66a64825716f51b409be528355f
    [2020-05-13 13:11:17] <sarang> Ah yes, the atomic swap idea
    [2020-05-13 13:11:45] <h4sh3d[m]> I had a closer look. The interesting part is the usage of ECDSA adaptor signature
    [2020-05-13 13:12:12] <sarang> Avoids the use of hash preimage proofs IIRC?
    [2020-05-13 13:12:19] <sarang> (I have yet to examine it in detail)
    [2020-05-13 13:12:46] <h4sh3d[m]> Yes, the protocol is very close what I already shared here
    [2020-05-13 13:13:37] <h4sh3d[m]> But with the idea of using a cross group dl-proof with an ECDSA adaptor signature might work
    [2020-05-13 13:13:59] <sarang> At the very least, a cross-group DL equivalence proof is very straightforward
    [2020-05-13 13:14:08] <sarang> and exists today
    [2020-05-13 13:14:43] <h4sh3d[m]> Yes, that's why it's interesting =)
    [2020-05-13 13:14:51] <h4sh3d[m]> The new part for me is this: https://lists.linuxfoundation.org/pipermail/lightning-dev/2019-November/002316.html
    [2020-05-13 13:15:11] <sarang> Is that link related to the gist?
    [2020-05-13 13:15:41] <Isthmus> Very cool
    [2020-05-13 13:15:59] <sarang> Ah, the link is from the gist
    [2020-05-13 13:16:00] <h4sh3d[m]> Yes, it's the first link "single signer ECDSA adaptor signatures" in the Gist
    [2020-05-13 13:16:05] <sarang> got it
    [2020-05-13 13:16:27] <sarang> I'm excited to work it out in detail!
    [2020-05-13 13:17:57] <h4sh3d[m]> With this, we can put one half of the monero key as the adaptor `Y` (or the other half depending if the swap succeed or not)
    [2020-05-13 13:18:30] ⇐ heatsinkid quit (~heatsinki@gateway/tor-sasl/heatsinkid): Remote host closed the connection
    [2020-05-13 13:19:05] <h4sh3d[m]> I'd be happy to work on this too. As zkao mentioned it earlier we are thinking about a proposal if it make sense
    [2020-05-13 13:19:29] <sarang> Having more eyes on ideas like this is definitely a good thing
    [2020-05-13 13:20:17] <sarang> Thanks for sharing this h4sh3d[m] (and zkao earlier as well!)
    [2020-05-13 13:20:32] <sarang> Were there any questions for h4sh3d[m] ?
    [2020-05-13 13:20:36] <h4sh3d[m]> Cool, I'll continue posting my findings here in the next days.
    [2020-05-13 13:20:41] <sarang> Thanks, please do
    [2020-05-13 13:21:34] <sarang> I wanted to finish up some work on next-gen transaction protocols, so I wrote up a proof-of-concept C++ implementation of Arcturus: https://github.com/SarangNoether/monero/tree/arcturus
    [2020-05-13 13:21:45] → heatsinkid joined (~heatsinki@gateway/tor-sasl/heatsinkid)
    [2020-05-13 13:21:51] <rehrar> weeeeee!!!!
    [2020-05-13 13:21:59] <sarang> The usual disclaimer that it has not undergone any kind of review, and should be considered unsafe for production use
    [2020-05-13 13:22:09] <sarang> However, I got timing data from it
    [2020-05-13 13:22:34] <sarang> I had to rewrite the performance tests for Triptych, MLSAG, and CLSAG for better comparison since Arcturus integrates balance checking directly into the proof (and the others do not)
    [2020-05-13 13:23:09] <sarang> The results, which I'll paste in just a sec, show that transaction input/output structure plays a role in the overall timing results
    [2020-05-13 13:24:15] <sarang> Here is data for 1-in-2-out transactions: https://usercontent.irccloud-cdn.com/file/KZxENlzN/timing-1-2.png
    [2020-05-13 13:24:36] <sarang> Here is data for 2-in-2-out transactions: https://usercontent.irccloud-cdn.com/file/Ww2hDEbo/timing-2-2.png
    [2020-05-13 13:24:56] <sarang> These account for the total verification time for signature/proof verification and balance checks
    [2020-05-13 13:25:06] <sarang> but does not include range proof verification (that's the same for all protocols)
    [2020-05-13 13:25:54] <sarang> You can get the same data by choosing the appropriate performance test parameters on my `clsag-device` branch (for MLSAG _and_ CLSAG), `triptych` branch (for Triptych), and `arcturus` branch (for Arcturus)
    [2020-05-13 13:27:02] <sarang> The grey lines are centered at the 11-MLSAG point to show the current timing
    [2020-05-13 13:27:52] <binaryFate> it looks super close to Triptych, any hunch how it would look like for more-inputs and/or more-outputs?
    [2020-05-13 13:28:33] <sarang> At higher ring sizes, Triptych and Arcturus should stay very close, as the balance check component becomes less relevant overall
    [2020-05-13 13:29:26] <sarang> The difference mainly arises from whether the balance check group operations are separated (in Triptych) or included in a single multiscalar multiscalar operation with the rest of the proof (in Arcturus)
    [2020-05-13 13:29:40] <sarang> and that difference goes away at higher ring sizes
    [2020-05-13 13:29:48] <sarang> The real benefit is in transaction size
    [2020-05-13 13:30:13] <sarang> I thought I already had Arcturus included in plot data, but it turns out I don't... I'll work that out right after the meeting and post it here
    [2020-05-13 13:32:35] <sarang> Unrelated to this, I'm coordinating a statement of work for the CLSAG audit with OSTIF and Teserakt, the audit firm that the audit workgroup recommended
    [2020-05-13 13:34:43] <sarang> Were there any other questions for me on these topics?
    [2020-05-13 13:34:48] <moneromooo> Oooooh ^_^
    [2020-05-13 13:35:00] → lederstrumpf joined (lederstrum@gateway/shell/matrix.org/x-ebhqmmiiojtdocdx)
    [2020-05-13 13:38:03] <sarang> Does anyone else have topics to discuss for the roundtable, before we move on?
    [2020-05-13 13:38:24] <Isthmus> Hmm, I just remembered a showerthought to generate seashell avatars based on transforming heterogeneously-structured transaction metadata into a signature string, and then running that through surae's visual hash function...
    [2020-05-13 13:38:27] <Isthmus> I'll try to prototype it this weekend so I can share examples next week (kind of hard to describe abstractly)
    [2020-05-13 13:39:46] <sarang> Oh man, I remember that seashell work! It's been a while
    [2020-05-13 13:40:51] <Isthmus> Yeah, that's a throwback. I forked Surae's repo back in 2018 and turned it into a notebook, but never connected it to Monero input data. https://github.com/Mitchellpkt/seashells/blob/master/seashells_notebook.ipynb
    [2020-05-13 13:41:47] <sarang> I suppose we can move on to ACTION ITEMS and finish up the meeting if there isn't anything else to discuss
    [2020-05-13 13:41:49] <selsta> I wish we could display seashells in CLI wallet.
    [2020-05-13 13:42:56] <sarang> I'll be incorporating some changes to my in-memory key encryption PR, looking into that swap proposal in greater detail, and updating the Arcturus security model for conference submission
    [2020-05-13 13:43:09] <sarang> Anyone else?
    [2020-05-13 13:45:08] <h4sh3d[m]> I'll study more in details adaptor for ECDSA and rewrite the concerned parts of the atomic swap paper.
    [2020-05-13 13:45:31] <sarang> You mean updating your original write-up?
    [2020-05-13 13:45:38] <h4sh3d[m]> yes
    [2020-05-13 13:45:43] <sarang> Excellent
    [2020-05-13 13:48:56] <sarang> All right, I suppose we can adjourn; thanks to everyone for participating!
    [2020-05-13 13:49:03] <sarang> Logs will be posted shortly to the agenda issue


# Action History
- Created by: SarangNoether | 2020-05-09T17:33:27+00:00
- Closed at: 2020-05-13T17:51:19+00:00
