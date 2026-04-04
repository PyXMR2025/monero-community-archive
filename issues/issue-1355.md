---
title: Monero Research Lab Meeting - Wed 18 March 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1355
author: Rucknium
assignees: []
labels: []
created_at: '2026-03-18T16:27:28+00:00'
updated_at: '2026-04-01T15:10:21+00:00'
type: issue
status: closed
closed_at: '2026-04-01T15:10:21+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [FCMP code integration audit overview](https://github.com/seraphis-migration/monero/issues/294).

4. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/issues/166).

5. [CCS proposal: I2P SAMv3 support](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/650).

6. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1352 

# Discussion History
## plowsof | 2026-03-25T10:06:08+00:00
Logs 
    
    
> **\<rucknium\>** Meeting time! https://github.com/monero-project/meta/issues/1355     
    
> **\<rucknium\>** 1. Greetings.     
    
> **\<vtnerd\>** Hi     
    
> **\<gingeropolous\>** (kinda here)     
    
> **\<jberman\>** waves     
    
> **\<iamnew117:matrix.org\>** hello guys i am new like learning codebase and about monero so i can contribute in future     
    
> **\<rucknium\>** Welcome, @iamnew117:matrix.org     
    
> **\<iamnew117:matrix.org\>** thanks     
    
> **\<rucknium\>** 2. Updates. What is everyone working on?     
    
> **\<UkoeHB\>** Hi     
    
> **\<jpk68:matrix.org\>** Hello     
    
> **\<vtnerd\>** Worked on various monerod bug fixes, all of which are posted now. Also worked on getting lws documentation into shape, with a new soft launch of monerolws.com     
    
> **\<vtnerd\>** Still needs works though     
    
> **\<UkoeHB\>** Me: studying carrot.     
    
> **\<jberman\>** Fleshed out more detailed Audit Goals for phases 1a-1b of the FCMP++ integration audit in response to questions raised by Cypher Stack and points raised by koe: https://github.com/seraphis-migration/monero/issues/294 , working on fixing a "hang on exit" bug in monerod caused by my connection patches PR reported by ofrnxmr     
    
> **\<rbrunner\>** A bit late: Hello!     
    
> **\<rucknium\>** @jpk68:matrix.org: I added your I2P proposal to the agenda, at the end.     
    
> **\<jpk68:matrix.org\>** Rucknium: Thanks :)     
    
> **\<rucknium\>** 3. FCMP code integration audit overview (https://github.com/seraphis-migration/monero/issues/294).     
    
> **\<jberman\>** In communication with Cypher Stack on the audit, as noted above fleshed out more detailed Audit Goals for Phases 1a-1b     
    
> **\<rucknium\>** Anything about the edits worth discussing here?     
    
> **\<jberman\>** I'd say the more interesting edits include 1) the bullet on the "Unbiased key image generator", fleshing out a goal to audit both our rationale in using a new hash-to-point function in the first place, as well as the implementation / soundness of the new hash-to-point fn     
    
> **\<jberman\>** both koe and Cypher Stack raised questions /suggestions on that item that I think that fleshed out goal should hopefully adequately address     
    
> **\<jberman\>** 2. I added a bullet to verify that all detectable received outputs should essentially be able to enter the curve tree merkle tree, otherwise someone would be able to construct an output that your wallet detects as a receive that you can't spend (see the section "Converting outputs to tuples in prep for insertion to the curve tree merkle tree")     
    
> **\<jeffro256\>** Sorry I'm late, timezone change threw me off     
    
> **\<jberman\>** 3. I added more concrete bullets on auditing the Rust FFI     
    
> **\<jberman\>** 4. As per Cypher Stack suggestion, I moved hash_grow and point_to_cycle_scalar to "Audit 2: Curve Tree Building", since those items more directly correspond to building the tree     
    
> **\<jberman\>** 5. I included a catch-all statement that the goal of the audit is to answer the question "Is the linked PR fit for use in Monero?" and that any insights that would help answer that question are appreciated, even if not explicitly mentioned in the "Audit Goals" for each PR     
    
> **\<jberman\>** Above are main highlights of the changes     
    
> **\<rucknium\>** Thanks, @jberman:monero.social  for all your work on the audit scoping and thanks to Cypherstack and UkoeHB  for initial review of the scope.     
    
> **\<rucknium\>** Anything else on this topic?     
    
> **\<jberman\>** Nothing from me     
    
> **\<rucknium\>** 4. FCMP beta stressnet (https://github.com/seraphis-migration/monero/issues/166).     
    
> **\<jberman\>** The main blocker on beta includes changes to the Rust FCMP++ lib (most significant are the changes to GBP in response to Cypher Stack's audit). I would like to give it 1 more week before exploring alternative routes to unblock that item     
    
> **\<jeffro256\>** That was the one question I had     
    
> **\<jeffro256\>** Is that being worked on rn?     
    
> **\<jberman\>** Waiting on kayaba's availability     
    
> **\<rucknium\>** Anything else on stressnet?     
    
> **\<jberman\>** Nothing from me     
    
> **\<rucknium\>** 5. CCS proposal: I2P SAMv3 support (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/650).     
    
> **\<rucknium\>** This ^ was discussed late last meeting: https://libera.monerologs.net/monero-research-lab/20260311#c661062-c661214     
    
> **\<jpk68:matrix.org\>** Happy to answer any questions/concerns regarding this proposal :)     
    
> **\<rucknium\>** I'll ping @vtnerd:monero.social     
    
> **\<rucknium\>** @jpk68:matrix.org: You have to copy the new commit version to the PR text in the CCS. It doesn't appear automatically.     
    
> **\<vtnerd\>** I'm in support after what I saw in i2p code. They could arguably improve socks to be more kike tor, but there's resistance to that for reasons not clear to me     
    
> **\<rbrunner\>** That goes solidly above my head, but I start to worry a bit about how many things we do *not* do "because sybil attacks". Really no solution in sight for that? Might unblock quite some things     
    
> **\<rucknium\>** Copy https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/650/diffs to https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/650     
    
> **\<vtnerd\>** Tor automatically creates a new circuit per hidden service, i2p may not     
    
> **\<vtnerd\>** *over socks     
    
> **\<jpk68:matrix.org\>** @rucknium: Looking at that right now... unless I missed something, I believe I did that already (?)     
    
> **\<rucknium\>** Ah, I may have had a wrong version loaded     
    
> **\<jpk68:matrix.org\>** It is worth noting that I intend on changing/removing the last milestone of the CCS; this was suggested by vtnerd     
    
> **\<jpk68:matrix.org\>** I am waiting on an email response from I2P devs about this, and will change it if they are in agreement     
    
> **\<rucknium\>** rbrunner: Sybil attack seems to be an unsolved problem in computer science. Big tech solves it with Captchas and personal identity info collection AFAIK.     
    
> **\<rbrunner\>** Ah, ok.     
    
> **\<rbrunner\>** So it's not only dragging us down at least     
    
> **\<rucknium\>** More discussion of this item?     
    
> **\<rucknium\>** We can end the meeting here. Thanks everyone.     

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2026-03-18T16:27:28+00:00
- Closed at: 2026-04-01T15:10:21+00:00
