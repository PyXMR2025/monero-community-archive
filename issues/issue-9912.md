---
title: '[Discussion] New Release schedule and Git workflow'
source_url: https://github.com/monero-project/monero/issues/9912
author: SyntheticBird45
assignees: []
labels: []
created_at: '2025-04-24T13:31:45+00:00'
updated_at: '2025-04-25T18:05:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Discussion started here: https://libera.monerologs.net/monero-dev/20250423#c519886

## Why

- 22 august 2024: [hackerone.com/reports/2677306](https://hackerone.com/reports/2677306)
> Spamming highly nested JSON RPC requests cause node to disconnect from p2p network

Fix PR: https://github.com/monero-project/monero/pull/9459

- 1 september 2024: [hackerone.com/reports/2693786](https://hackerone.com/reports/2693786)
> A peer can remotely fill the pending block queue to an extremely high size, with blocks that will never leave the queue.

Fix PR: https://github.com/monero-project/monero/pull/9582 (extrapolated from report discussion and present on to-do list but i'm unsure)

- 21 november 2024: [hackerone.com/reports/2858802](https://hackerone.com/reports/2858802)
> low-level p2p ping + tcp flooding leads to a remote crash in monerod

Fix PR: https://github.com/monero-project/monero/pull/9459

- 23 december 2024: [hackerone.com/reports/2912194](https://hackerone.com/reports/2912194)
> Remote memory exhaustion in Epee RPC stack under zero Receive Window

Fix PR: https://github.com/monero-project/monero/pull/9765

(A discussion about the current state of the code is recommended but not the topic of this discussion)

All these vulnerabilities are at least of high-severity if not critical depending on the score system you want to use. They have all without exception seen their fix shipped in more than 90 days. With the highest gap of 7 months and a half between report and release. (Which also coincide with the period between 18.3.4 and 18.4.0)

### February

In February, Monero network has been attacked through one of these vulnerability and [the fix have quickly been merged into master](https://github.com/monero-project/monero/commit/257db6dff257bc9f60641b16d199ffde252655b2). From this point to a proper release, two months have elapsed and the history of this delay can be explained by looking at the todo list:

https://github.com/monero-project/monero/issues/9758

### The release delay

What caused this delay?

- Vulnerability fixes were blend into important feature additions, they have caused regressions or delays:
https://github.com/monero-project/monero/pull/9740 -> https://github.com/monero-project/monero/pull/9844
https://github.com/monero-project/monero/pull/9459#issuecomment-2677282415 -> https://github.com/monero-project/monero/pull/9820
https://github.com/monero-project/monero/pull/9765 -> https://github.com/monero-project/monero/issues/9758#issuecomment-2725680036
- CI issues:
https://github.com/monero-project/monero/issues/9755 | https://github.com/monero-project/monero/issues/9755
- Miscellaneous bug fixes discovered in-between
https://github.com/monero-project/monero/pull/9861
https://github.com/monero-project/monero/pull/9805

### Bottlenecks

- For almost any important changes, reviewers have to review two PRs (release and master)
- Some of the PRs that have caused these regressions were opened since a long time and were only merged for proper testing just before the targeted release timeline.

### Other issues

- Breaking changes were not properly communicated to ecosystem (There is still to this date, no appropriate message in changelog about RPC limit)

## What

In order to reduce chances of regression, make testing and reviews easier and increase frequency of releases, @tobtoht have proposed the following git workflow (other workflow has been discussed on IRC):

**Releases** are targeted **every 3 to 6 months**

There will be a `master` branch, a `vA.B.0` *release* branch, a `hf-vA+1.0.0` *hardfork* branch (name TBD)

### Branch roles

`master` is the branch welcoming any PRs (excluding hardfork related or breaking ones), this include feature additions, bug fixes, ci improvements, code cleaning, etc... **Any PR merged into master is assumed to be ready to be shipped for release**, If a PR is not meant to be shipped immediately, or is known to cause a breakage, then it should be gate keep in its own branch until the times come, or redirected towards another branch for breaking works. 

`hf-vA+1.0.0` is a branch kept in sync with master that contain hard fork related PRs (FCMP++/Carrot) and potentially other breaking changes like toolchains.

`vA.B.0` is the *release* branch from which release are tagged, compiled and shipped. It only live at most 6 months and should only welcome bug or compilation fixes. Meaning every changes in the *release* branch is meant for a patch version release (18.4.0->18.4.1). In an ideal world, it should only be created, tagged for release and nothing else. If we ever have to ship bug/vulnerability/compilation fixes, the corresponding PRs will be backported to this branch, quickly tested (as we would have already assumed stability through testing of master) and compiled for new patch release (unless its just compilation).

### Release process

When the time of a release has come:
1. If needed, merge long-living feature branches like `hf-vA+1.0.0`.
2. Proceed to extensive testing (usual compilation, syncing on all platforms, treat urgent issues).
3. Merge into master fixes for bug discovered during testing.
4. Once stability of master is asserted, create `vA.B+1.0` branch from `master`.
5. Tag `vA.B+1.0` and release it.
6. Abandon `vA.B.0` branch

Rendez-vous at next release.

### Patch release process

1. Cherry-pick required commits from `master` and make a PR for `vA.B.0 (similar to https://github.com/monero-project/monero/pull/7997)
2. Proceed to testing `vA.B.0`
3. Tag and release `Monero vA.B.C+1`

### Long-living features

Heavy feature addition needs to be kept into its appropriate branch in the repository until it is ready to be shipped.

### Pros:

- We no longer have to lie to our self about *release* branch being bug fix only but not really. Features are guaranteed to be included every 3-6 months. No more "we don't have timeline for master so lets backport this feature into release".
- Except for backporting critical bug fixes or CI fixes into *release*, no more `[Release]` version of PRs (which are usually the most slow to review and always have delays between the two)
- Testing patch releases will be much safer since the set of changes will be minimized.
- No more difference of C++ standards.
- Not necessarily due to the layout, but increasing the frequency of release and therefore testing make bisecting regression much faster


# Discussion History
## SyntheticBird45 | 2025-04-24T13:36:37+00:00
Just to be clear: There is no one to blame about the the delay in resolving these reports, what happened was mechanical chain of consequences that led to this situation. This issue is meant for discussing what can be improved.

## tobtoht | 2025-04-24T14:32:25+00:00
(Reposting my comments from Matrix)

I'm not sure if we necessarily need a hard fork branch. If we need to review it in parts, we could do that out of tree. It's unclear how and who would keep the branch "in sync with master". I don't like the idea of giving devs write access to feature branches under `monero-project/monero`.

To give an example from our neighbors: Bitcoin did most of the review for its Autotools → CMake migration out of tree (https://github.com/hebasto/bitcoin/pull/18). Once ready, all changes were submitted in a single PR to master (https://github.com/bitcoin/bitcoin/pull/30454) which then prompted additional review and testing. 

This is similar to what we're doing with the `fcmp++-staging` branch on the `seraphis-migration/monero` repo. (https://github.com/seraphis-migration/monero/pulls).

Keeps things de-cluttered during the development phase. For the sake of visibility and avoid the risk of losing discussion, we could create `monero-project/monero-hf-staging` where we give select devs write access (as a replacement for `seraphis-migration`).

# Action History
- Created by: SyntheticBird45 | 2025-04-24T13:31:45+00:00
