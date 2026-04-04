---
title: Move versioning to 1.0 upon inclusion of Seraphis protocol
source_url: https://github.com/monero-project/meta/issues/721
author: ghost
assignees: []
labels: []
created_at: '2022-07-20T15:56:25+00:00'
updated_at: '2024-01-25T22:31:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
For most of cryptohistory, projects have tended to keep versioning at zero in order to communicate the rough and experimental condition of the underlying code. For example, here's Hal Finney sharing Satoshi's original **version 0.1** Bitcoin binaries on Bitcointalk.org: https://bitcointalk.org/index.php?topic=68121.0

While this was probably a decent approach back in the day as it succinctly communicated the experimental nature of blockchain software, thirteen years later blockchain theory is quite stable and the zero versioning is far less necessary. Perhaps it has its use for a new project, but this is less applicable for a somewhat mature project like Monero. One might even argue that, at this point of Monero's timeline, the 0 versioning as a communicator of instability has almost become almost a tired joke (eg: "We're still waiting for that stable release!"). It is important to ask if the project might ever move to version 1, and if it did, what sort of circumstance or event might justify this change. 

It seems that moving to Monero v1.0 would involve one of two circumstances: either (1) Monero's codebase is finally declared mature/polished/complete, or (2) Monero has such a significant upgrade to its underlying code as to use the new versioning to indicate the significance of this change.

Option 1: the community reaching a consensus around the "readiness" of Monero's code, seems already long overdue or _de facto_ unreachable. As [already discussed](https://github.com/monero-project/meta/issues/316) many times, the goal of offering people private digital money is a neverending process. As the technical abilities of adversarial parties continue to improve, and underlying technologies (eg: [zk-SNARKs](https://github.com/monero-project/research-lab/issues/100)) develop and improve, Monero has always been pushing itself to improve in tandem. This endless improvement somewhat indicates that the software will never be 100% "complete", or that Monero is already mature and polished enough to warrant non-zero versioning.

Option 2: version 1.0 indicating a significant change or upgrade within Monero's code, seems the better opportunity, and Seraphis seems a major enough upgrade to warrant this new change. As outlined well [elsewhere](https://localmonero.co/knowledge/seraphis-for-monero), the Seraphis protocol increases the ringsize by an order of magnitude (eg: to possibly 128 ring members from today's 16) as well as offering a whole host of much needed additional upgrades (eg: a view key that actually functions as advertised). Using the Seraphis release as an excuse to move to v1.0 would help communicate the significance of this potential upgrade to the wider public.

In summary, while it's wonderful to see the recent release of Monero's [v0.18 'Flourine Fermi'](https://www.getmonero.org/2022/07/19/monero-0.18.0.0-released.html), the first major software release for the project in almost two years, its v0.18 versioning begins to feel a bit unnecessary. I would like to invite feedback toward using the next major software release (eg: v0.19, and likely to be Seraphis) as an opportunity to move away from the v0 versioning that has served the project well from its humble beginnings, but is no longer as helpful these eight years later.

# Discussion History
## hyc | 2022-07-20T16:53:52+00:00
Sounds ill advised, even at this point. Setting version 1.0 signals that we don't anticipate any more changes of significant magnitude, which I don't believe is true. We still have major questions to resolve regarding use of anonymity networks and securing the p2p protocol, as an example.

## ghost | 2022-07-20T22:21:28+00:00
> Setting version 1.0 signals that we don't anticipate any more changes of significant magnitude, which I don't believe is true.

I'm not sure setting a full version does indicate no further major changes. That seems what further versions could mean (eg v2.0). 

> We still have major questions to resolve regarding use of anonymity networks and securing the p2p protocol, as an example.

But what's to say that there will not be further major additions identified once these have been added? That's the problem with Option 1. Or, perhaps more to the point hyc, do you truly believe we will reach a point in Monero where all major questions are resolved?

## hyc | 2022-07-21T01:52:03+00:00
On 2nd thought, after seeing old tickets being closed out today, sure why not. Since all wallets need to be recreated, it's definitely a major enough change. We could also rename ".bitmonero" to ".monero" while we're at it.

## jtgrassie | 2022-07-21T03:49:19+00:00
> We could also rename ".bitmonero" to ".monero" while we're at it.

Things like this I feel are higher priority, especially as the years roll by. We can't assume new users will know about the very early days of Monero when they go looking for ".monero".

On moving beyond version 0, I suppose it's better to make the move at some point (pardon the pun). There's an argument though that keeping it at 0.M.P may remind people it's still somewhat experimental and / or caution should be exercised. Moving to v1 at the inclusion of something like Seraphis is case in point, a somewhat experimental, bleeding edge release.

## erciccione | 2022-07-21T07:16:43+00:00
Personally, i see the 10 blocks lock as the biggest problem of the Monero network. Its impact on UX is huge and it's hard to consider Monero a fully working currency as long as people have to wait 20 minutes between receiving and sending their coins. I would be inclined to move to v1 after this crucial usability problem is resolved.

Related issues:

- https://github.com/monero-project/research-lab/issues/95
- https://github.com/monero-project/research-lab/issues/102

## fluffypony | 2022-07-21T11:18:04+00:00
> On 2nd thought, after seeing old tickets being closed out today, sure why not. Since all wallets need to be recreated, it's definitely a major enough change. We could also rename ".bitmonero" to ".monero" while we're at it.

We could create a list of v1.0 deliverables, and then switch to [Semantic Versioning](https://semver.org) thereafter? I certainly would be more comfortable with the constrained versioning of SemVer, as opposed to the current rather hand-wavey "major-version-is-a-fork-but-only-sometimes" situation we have now.

## vtnerd | 2022-07-22T15:43:32+00:00
@fluffypony

With semantic versioning, I assume you meant at the hardfork level (as opposed to HTTP-RPC or P2P layer)? So a major version change indicates a hard-fork, whereas a minor version change indicates big changes where upgrading is not required. 

There would be at least a more consistent pattern to the release numbers, and it somewhat side-steps the arbitrary bumping that the Linux kernel seems to be doing (which irritates me for some reason).

## vtnerd | 2022-07-22T15:46:07+00:00
BTW - I'm interested in this topic because I decided to "mirror" version numbers for `monero-lws`. So I've been wondering how this would play out because it meant that the third number in `monero-lws` is the only indicator for internal changes (whereas the first two indicate external changes in `monero`). It's a small thing but annoying as people are already confused on how to build `monero-lws` sometimes.

## comminutus | 2024-01-24T23:43:22+00:00
Upon Seraphis, I think it'd make sense to version it as v19.0.0 to avoid confusion.  Some may get the idea that v1.0 or variations (v1.0.0) are older than v0.18.3.1 for example.  v19.0.0 would solve that problem and get the project onto a standardized SemVer style versioning.

## iamamyth | 2024-01-25T19:38:50+00:00
I think you're confusing the concept of semantic versioning with its common, practical form: The concept requires the versioning scheme to define and follow fixed semantic rules; in practice, many applications do this as major.minor.patch. The current versioning scheme may, in fact, have perfectly reasonable, definable semantics; if so, switching to major.minor.patch (a clear departure from the prior form) would actually *break* semantic versioning at the conceptual level. On the other hand, the current semantics could be ill-defined, in which case a proposal to define them clearly, and stick with that definition, may be reasonable.

## comminutus | 2024-01-25T20:10:02+00:00
@iamamyth I totally agree.  In the current semantics then, how is each component of the version defined?

## iamamyth | 2024-01-25T22:31:00+00:00
I'm not sure there are very clear semantics (other than perhaps zero means "be careful"); I didn't originate this scheme, so I wouldn't be the right one to ask. But, since you asked, the most accurate way I could describe the current scheme would be: milestone.major.minor.patch. Per the comments on this issue, one could argue the milestones are somewhat arbitrary, but it's not exactly difficult to strip off "milestone" and compare major.minor.patch if the project contributors accept some common meaning of major (for example, "requires hardfork" as vtnerd proposed).

# Action History
- Created by: ghost | 2022-07-20T15:56:25+00:00
