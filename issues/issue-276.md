---
title: Decentralized Funding Solution
source_url: https://github.com/monero-project/meta/issues/276
author: anonimal
assignees: []
labels: []
created_at: '2018-09-18T08:23:45+00:00'
updated_at: '2020-06-05T15:34:57+00:00'
type: issue
status: closed
closed_at: '2020-06-05T15:34:57+00:00'
---

# Original Description
**This is a cross-post from https://gitlab.com/kovri-project/kovri-meta/issues/1**

**We intend to continue development on this issue - within that repo - in order to find a working solution soon so, please, come aboard to that repo to avoid more cross-posting. Thank you :smile:**

----------------------

The Kovri Project is currently funded entirely by the Monero Project's [Forum Funding System](https://forum.getmonero.org/). A majority of Monero Project developers and researchers are also funded by this system. The FFS is an attempt to self-regulate a crowd-funding system but suffers from at least a few fatal flaws:

- Requires a TTP of at least several core team members
  * A single TTP is inherently centralized; especially in this case where N wallets are controlled by the same entity
  * Even though the Monero Project [doesn't even follow their own Code of Conduct](https://github.com/monero-project/monero-site/pull/634), theoretically, if a contributor somehow violates the C4 despite producing 100% of the agreed upon work, the contributor can be denied payment
- Relies on approval of commentators and "the community" at large
  * The "community" can consist of random internet people with no PoS
  * As these are privacy projects, the actual community is not required to disclose TX ID
- The forum itself has been "deprecated" for possibly around a year(?) yet continues to be in use
  * It continues to suffer from a cornucopia of XSS vulnerabilities because of said "deprecation" but the forum has yet to be replaced
  * The attempt to [formalize a system](https://github.com/monero-project/meta/pull/87) has sat in PR hell for over a year and there are no other discussion of solutions in sight
- Unreliable at inconvenient times:
  * I recently sat across the table from a new prospective contributor who wanted to create her first FFS thread. She couldn't even register a new account because the forum's backend was broken for whatever reason. The solution: email fluffypony and hope he'd fix the forum soon[tm]. This is not reliable, this is not sustainable, this is not the first time I've seen issues with the forum, and when dealing with people's money the last thing you want is DoS

Note: I have more points to make, available upon request.

For the sake of longevity and decentralization, The Kovri Project must not rely *entirely* on Monero's Forum Funding System. The problem of decentralized crowdfunding is somewhat of a hot topic lately and is being tackled at the blockchain level with projects such as Lighthouse, Elix, and Fundition but various problems do exist: all are unique to their respective blockchains and involve technology that the Monero Project has refused to entertain (for example, Smart Contracts). *Note: I'm not advocating any of these solutions at this time but I'm not denying the possibility of using related technology as a solution to the problem.*

In the interim, The Kovri Project will be setting up it's own donation page and various cryptocurrency wallets as part of a new recurring revenue model. We will also be setting up a temporary FFS solution by using a git repo with a similar setup to the existing FFS, but that is another issue all together. **Neither of these solutions are decentralized** but they are a very necessary step in a sovereign direction.

Any solution to this issue will need to be *more* decentralized than the provided interim solutions. Even if partially decentralized, anything is better than completely centralized - so let's entertain as many options as possible.

Keep in mind that, for ideas like using SSSS or multi-sig to somehow secure the receiving or dispersing of funds, such schemes require N people to be alive or available to do so... So, let's keep vamping on other ideas if possible.


# Discussion History
# Action History
- Created by: anonimal | 2018-09-18T08:23:45+00:00
- Closed at: 2020-06-05T15:34:57+00:00
