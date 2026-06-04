---
title: Monero Research Lab Meeting - Wed 3 Jun 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1399
author: j-berman
assignees: []
labels: []
created_at: '2026-06-02T16:51:56+00:00'
updated_at: '2026-06-02T19:42:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686.

4. [Monero-PSK](https://gist.github.com/tevador/9169235b3c0c97e735f58a8c2ba92502).

5. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

6. [FCMP++ integration audit](https://github.com/seraphis-migration/monero/issues/294).

7. [CCS proposal: ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).

8. [Potential ring signature findings](https://github.com/monero-project/meta/issues/1399#issuecomment-4604934837).

9. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

https://github.com/monero-project/meta/issues/1395

# Discussion History
## SyntheticBird45 | 2026-06-02T16:57:49+00:00
Rename the greetings chapter into "Glory to Rucknium" please.

## uwaterl00 | 2026-06-02T17:10:38+00:00
We would like to propose general dialogue (agenda item) regarding linkable ring signatures and the leaking of probabilistic information. Specifically, if one signs a linkable ring signature for one ring (org A) and another linkable ring signature for a different ring (org B), the resulting linking tag reveals that both signatures were produced by the same signer. If the signer is the only overlapping participant across both rings, this linkage can effectively deanonymize the signer’s identity.

Relevant implementation context can be found here:
https://github.com/firoorg/crucible/blob/main/lessons-from-monerochan/lessons-from-monerochan/LessonViewAllEvasion.lean
If access to the repository or additional data for the view-all evasion code is needed, please reach out to reuben@firo.org for repo access.

## j-berman | 2026-06-02T17:34:52+00:00
@uwaterl00 I get "Page not found" errors when clicking those links

## uwaterl00 | 2026-06-02T18:32:11+00:00
@j-berman you'd need repo access from reuben@firo.org

alternatively Fieckert / Freeman could send you the repo as they already have access.

## tevador | 2026-06-02T19:39:03+00:00
> We would like to propose general dialogue (agenda item) regarding linkable ring signatures and the leaking of probabilistic information. Specifically, if one signs a linkable ring signature for one ring (org A) and another linkable ring signature for a different ring (org B), the resulting linking tag reveals that both signatures were produced by the same signer. If the signer is the only overlapping participant across both rings, this linkage can effectively deanonymize the signer’s identity.

Isn't this a well-known issue of RingCT? See for example [This getmonero blog post from 2018](https://www.getmonero.org/2018/02/11/PoW-change-and-key-reuse.html) and scroll down to the Key reuse section.


## uwaterl00 | 2026-06-02T19:42:52+00:00
Indeed, probabilistic information leakage is a known issue. But at this point, dialogue related to view-all evasion code might be non-trivial and presumably worthy of placing at the agenda. C++

# Action History
- Created by: j-berman | 2026-06-02T16:51:56+00:00
