---
title: Monero Research Lab Meeting - Wed 02 October 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1086
author: Rucknium
assignees: []
labels: []
created_at: '2024-10-01T21:08:26+00:00'
updated_at: '2024-10-15T17:02:15+00:00'
type: issue
status: closed
closed_at: '2024-10-15T17:02:15+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). Reviews for [Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md).

5. 10 block lock discussion: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259 , [Monero output lock analysis](https://github.com/AaronFeickert/pup-monero-lock/releases/tag/final)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1082 

# Discussion History
## Rucknium | 2024-10-04T17:21:43+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1086     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< s​gp_:monero.social >__ Hello     

> __< Chris12321 >__ Hello     

> __< l​yanaqb:matrix.org >__ hello     

> __< j​effro256:monero.social >__ howdy     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< j​berman:monero.social >__ *waves*     

> __< OliverZellic >__ Hello!     

> __< LindsayTOB >__ hi everyone!     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Analyzing node p2p logs, especially transaction broadcast timings. Mostly, things work the way that the code is supposed to work.     

> __< j​effro256:monero.social >__ me: invited some guests from the firms who would like to audit the Carrot spec! Welcome to all those that joined the MRL for that reason, and thanks for your time. I'll let you know when a good time to jump in is. Otherwise, I have been working on implementation and integration with legacy scanning and balance recovery     

> __< r​ucknium:monero.social >__ We can go directly into the FCMP++/Carrot agenda item, since I think some people in the room are waiting on that.     

> __< r​ucknium:monero.social >__ 3) Research Pre-Seraphis Full-Chain Membership Proofs. Reviews for Carrot. https://www.getmonero.org/2024/04/27/fcmps.html https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< j​berman:monero.social >__ me: continuing working on syncing the curve trees tree on the wallet side (storing minimal data necessary to sync the tree), so wallets can construct an fcmp for an owned output using the output's latest path in the tree     

> __< LunaZellic >__ Hey all, Luna from Zellic here     

> __< r​ucknium:monero.social >__ Before the meeting, kayabaNerve posted a summary of work that has been accomplished on FCMP++ research and review: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449#note_26540     

> __< r​ucknium:monero.social >__ Thanks, kayaba     

> __< r​ucknium:monero.social >__ I am going to pose a noob question about the Carrot review. (To guests: I'm an economist, not a cryptographer.) Is there anything "special" about addressing protocols, compared to other problems in the blockchain cryptography space? In other words, is it important that a reviewer have specific prior experience in reviewing and/or designing address protocols?     

> __< j​effro256:monero.social >__ I believe that kayabanerve had some details to share about his FCMP work before discussion of the Carrot audit     

> __< d​iego:cypherstack.com >__ hi     

> __< d​iego:cypherstack.com >__ apologies for being late     

> __< r​ucknium:monero.social >__ I see . Ok thanks     

> __< k​ayabanerve:matrix.org >__ Hello, sorry.     

> __< k​ayabanerve:matrix.org >__ I am here, I just had to step back for a moment.     

> __< LunaZellic >__ Welcome back :D     

> __< k​ayabanerve:matrix.org >__ I would like to go over the FCMP++ Research summary and how that's moving forward, if amenable.     

> __< j​effro256:monero.social >__ Of course     

> __< k​ayabanerve:matrix.org >__ I posted the summary above. Re: divisors, we have proofs of the technique from Veridise (reviewed), yet still haven't had the R1CS finalized/audited. We prior ran out of hours and had a small extension approved, as detailed in the posted summary.     

> __< j​effro256:monero.social >__ Rucknium: to answer your question, previous experience in auditing addressing protocols always helps, but AFAIK it shouldn't be strictly required as long as the consensus protocol requirements are well understood by the reviewers. If I am wrong, anyone feel free to correct me     

> __< k​ayabanerve:matrix.org >__ For the past few weeks, I've been discussing the rest of that scope with Veridise. The prior mentioned extension did start on a review and identified one potential issue.     

> __< k​ayabanerve:matrix.org >__ The existing security proofs are for positive integers, not elements of a finite field. That leaves us needing to expand the security proofs in that regard.     

> __< tjadenTOB >__ Rucknium having only briefly looked a the Carrot proposal, at a glance it is helpful to have some familiarity with stealth address schemes in general -- as implemented in ZCash for instance. There are certain attack vectors that come up in practice (Janus attacks, DDH oracles via timing, etc) that can break privacy / add linkability but don't     

> __< tjadenTOB >__ violate the normal existential forgery considerations of address/signature schemes     

> __< k​ayabanerve:matrix.org >__ I'd like to move forward with Veridise, who the running tally is 11k, for an additional 5k explicitly to specify taking the logarithmic derivatives (a topic brought up in CS's review) and expand the security proofs on this manner.     

> __< k​ayabanerve:matrix.org >__ That still leaves needing to formalize the protocol encoded into the R1CS, prove it, and actually encode it into the R1CS. While we do have a quote for those scopes, that part is still being discussed and clarified a bit. I'd like to propose moving forward with what makes sense now before this gets further bottlenecked.     

> __< k​ayabanerve:matrix.org >__ I'll also note a few meetings ago, I had a check written (yet never cashed) for an amount exceeding the amount I'm requesting now for further work on this from Veridise. I'm explicitly making this proposal now as it's a bit weird as I'm only proposing a partial continuance of the necessary scope, not the entire scope at this time.     

> __< r​ucknium:monero.social >__ kayabanerve: I'm ok with that, but what is the contingency plan if the attempt to repair the proof fails?     

> __< k​ayabanerve:matrix.org >__ I also do see Alp is here and this is the first they're hearing of my intent to downscope our discussions from the existing quote. Hi, very sorry if this a bit blindsiding to you, I just wanted consensus from the community that the more incremental approach is an acceptable proposal before I came to y'all with this.     

> __< j​effro256:monero.social >__ I'm also fine with that, but would we also have another player (maybe CS again) review the new security proofs afterwards?     

> __< LunaZellic >__ BTW as a procedural matter, I'm having issues joining this room on Matrix (thus the fallback to IRC here), and monero.social homeserver registration seems disabled. I was able to join the lounge channel but not this one; am I missing an invite?     

> __< k​ayabanerve:matrix.org >__ Rucknium: The proofs should work out. The main concern is if they work out with ideal performance.     

> __< k​ayabanerve:matrix.org >__ Without divisors, a scalarmul is 512 multiplicative constraints with a reusable prior 256 multiplicative constraint bit decomposition.     

> __< j​effro256:monero.social >__ LunaZellic: type out the username in the chat and I'll invite you. Sorry we've been having spam issues recently     

> __< LunaZellic >__ ephemeral2:matrix.org, thank you!     

> __< k​ayabanerve:matrix.org >__ With divisors, and no need for a bit constraining, it's 7. 1/110th the constraints.     

> __< e​phemeral2:matrix.org >__ Thank you!     

> __< a​lpbassa:matrix.org >__ No worries, I agree that a more incremental approach would be meaningful!     

> __< j​effro256:monero.social >__ Of course! Sorry about the friction     

> __< k​ayabanerve:matrix.org >__ If we need to introduce bit constraints for the field elements to satisfy the positive integer bound (if we can't relax that bound), we'd add the reusable bit decomposition. Divisors would only be 33% the size, not 1%, of the traditional method.     

> __< k​ayabanerve:matrix.org >__ (The fact it's reusable only matters if we want to reuse the scalars. Most scalars we don't reuse so it doesn't benefit us)     

> __< r​ucknium:monero.social >__ Do you have an estimate for what percentage larger that falback would make the input proof/tx?     

> __< k​ayabanerve:matrix.org >__ If we can relax the bound and maintain performance, presumably CS would do review again. If we prove it with additional constraints, the additional performance is of such value I'd encourage contracting CS to do their own attempt on this topic, yet that's a separate discussion.     

> __< a​lpbassa:matrix.org >__ I believe that the issue about finite field elements vs integers will most likely not cause a too serious issue, but would probably require some of the soundness proofs to be re-adjusted. In the worst case it can be salvaged resturcturing and adding additional contraints (hopefully not too many).     

> __< k​ayabanerve:matrix.org >__ After we have the technique so improved, we'll still have a scope of work for the protocol encoded and the R1CS encoding. I just don't want to continue delaying any progress while the considerations there finalize. I've already deferred to the next meeting for the prior... three meetings?     

> __< r​ucknium:monero.social >__ I have seen myself and jeffro256  support kayabanerve 's proposal on an incremental extension on the divisor proof. Are there more opinions in the room?     

> __< rbrunner >__ At least I see nothing that speaks against it ...     

> __< k​ayabanerve:matrix.org >__ Size wouldn't be impacted. Performance would be. It'd increase the path size (which may notably impact wallet bandwidth for anyone without wallet trees) and probably impact proof verification time 2-3x.     

> __< j​effro256:monero.social >__ And Veridise doing it makes sense here obv since they freshly worked on it. Just for fun, who noticed the issue initially?     

> __< j​berman:monero.social >__ I +1 this approach as well     

> __< r​ucknium:monero.social >__ I see. Thank you. So many meanings of "size" ;)     

> __< k​ayabanerve:matrix.org >__ Alp, thank you for expressing your support for this timeline (which you're only just now hearing of 😅) and iterating your confidence :)     

> __< k​ayabanerve:matrix.org >__ jeffro256: Alp noted the issue in the few hours of R1CS review already done.     

> __< k​ayabanerve:matrix.org >__ Rucknium: circuit size impacts proof size and proof time. Proof size is negligible as doubling the circuit size only adds 64 bytes to the proof.     

> __< r​ucknium:monero.social >__ We already had some support for incremental extension of around this budget at a previous meeting IIRC.     

> __< k​ayabanerve:matrix.org >__ I also have more on the fcmp++ dev side but I'm happy to step back for jeffro256 and the fine collection of auditors they brought in person now that I've said my piece on audits.     

> __< r​ucknium:monero.social >__ I think we have loose consensus on this proposal. We can move on to the next topic since we have lots to cover ("I'd like to move forward with Veridise, who the running tally is 11k, for an additional 5k explicitly to specify taking the logarithmic derivatives (a topic brought up in CS's review) and expand the security proofs on this manner.")     

> __< r​ucknium:monero.social >__ Thanks, guests, for your patience :)     

> __< e​phemeral2:matrix.org >__ No, thank you!     

> __< j​effro256:monero.social >__ Alright! Yeah I'll invite the guests to introduce themselves one by one, and give a quick elevator pitch if desired ;). Also anyone should ask questions if they have any     

> __< e​phemeral2:matrix.org >__ Okay!     

> __< j​effro256:monero.social >__ Thanks for your patience     

> __< j​effro256:monero.social >__ Luna, would you like to go?     

> __< e​phemeral2:matrix.org >__ Hi all, my name is Luna, and I'm the co-founder and CEO of Zellic. I've brought along with me some of my colleagues on the IRC side and we're proposing for the proof and audit of Carrot.     

> __< e​phemeral2:matrix.org >__ (still typing)     

> __< v​tnerd:monero.social >__ Forgot to today was Wed, sorry I'm late     

> __< r​ucknium:monero.social >__ jeffro256: Do we have a formal statement of the scope of work? Sorry if I missed it.     

> __< e​phemeral2:matrix.org >__ We have extensive background auditing privacy-focused cryptocurrency projects. We audited Singularity, which is essentially a Zcash clone (a dark pool). In our audit of Penumbra (Zcash-esque, we found several critical soundness bugs. We've also audited NEBRA (zk proof aggregation in gnark) and in the process we actually found two vulnerabilities in the gnark's extension of Groth16<clipped message>     

> __< e​phemeral2:matrix.org >__  that we reported and got fixed (CVE-2024-45039, CVE-2024-45040)     

> __< e​phemeral2:matrix.org >__ Our audit of Singularity: https://reports.zellic.io/publications/singularity      

> __< e​phemeral2:matrix.org >__ PDF: https://github.com/Zellic/publications/blob/master/Singularity%20-%20Zellic%20Audit%20Report.pdf     

> __< e​phemeral2:matrix.org >__ Penumbra audit: https://github.com/Zellic/publications/blob/master/Penumbra%20-%20Zellic%20Audit%20Report.pdf     

> __< j​effro256:monero.social >__ Yes scope of worked for the Carrot audit is this document: https://github.com/jeffro256/carrot/blob/master/carrot.md. For all the firms, I requested general review of security of the specification and security proofs of all the properties listed in the "security properties" section 9.     

> __< e​phemeral2:matrix.org >__ As for myself, I'm a former vulnerability researcher, and me and my cofounder founded perfect blue, which was the top-ranked CTF team in the world in 2020, 2021, and 2023 per CTFtime.     

> __< e​phemeral2:matrix.org >__ I'm also a huge believer and evangelist in Monero myself and have been using and spending Monero since 2017 when I was in high school!     

> __< e​phemeral2:matrix.org >__ so I have an emotional connection to this proposal myself haha     

> __< s​gp_:monero.social >__ Nice to meet you Luna!     

> __< e​phemeral2:matrix.org >__ As for myself, I'm a former vulnerability researcher, and me and my cofounder also founded perfect blue, which was the top-ranked CTF team in the world in 2020, 2021, and 2023 per CTFtime.     

> __< e​phemeral2:matrix.org >__ I'm also a huge believer and evangelist in Monero myself and have been using and spending Monero since 2017 when I was in high school!     

> __< e​phemeral2:matrix.org >__ </spiel done>     

> __< e​phemeral2:matrix.org >__ Thanks sgp_!     

> __< j​effro256:monero.social >__ Thanks, Luna! Anyone have any questions for Luna / Zellic ?     

> __< e​phemeral2:matrix.org >__ \</spiel>     

> __< e​phemeral2:matrix.org >__ Thanks sgp\_!     

> __< e​phemeral2:matrix.org >__ (Also, here is the link to the report for the issues we found with Gnark: https://www.zellic.io/blog/gnark-bug-groth16-commitments/)     

> __< e​phemeral2:matrix.org >__ I wanted to ask, have the members of the MRL already seen our proposal or is it mainly just jeffro256 so far?     

> __< r​ucknium:monero.social >__ LunaZellic: Do you have a specific person or person in Zellic who would likely lead the review of Carrot? Or is that not something that's decided yet?     

> __< e​phemeral2:matrix.org >__ It will be Malte Leip, the author of the Gnark advisory linked above.     

> __< r​ucknium:monero.social >__ person(s)     

> __< e​phemeral2:matrix.org >__ The second peer reviewer will be Mohit Sharma.     

> __< j​effro256:monero.social >__ I have compiled a summary of proposals and shared it with a few members. If anyone would like the PDFs as well, please let me know.     

> __< j​effro256:monero.social >__ Okay, if there aren't any more questions, would QuarksLabs like to jump in?     

> __< l​yanaqb:matrix.org >__ Hi all, Quarkslab team is here  ! We prepared a text to outline our offer     

> __< l​yanaqb:matrix.org >__ # Why us      

> __< l​yanaqb:matrix.org >__ Quarkslab's team already performed a cryptographic & security assessment of the Bulletproof protocol to be used by the Monero open-source cryptocurrency (XMR) and RandomX new proof-of-work algorithm. Our team is substantial and composed of 3 PhDs, 2 master degrees in security, and 1 master degree in mathematics.     

> __< l​yanaqb:matrix.org >__ https://dblp.org/pid/44/1487.html     

> __< l​yanaqb:matrix.org >__ https://dblp.org/pid/214/8633.html     

> __< l​yanaqb:matrix.org >__ https://dblp.org/pid/177/2271.html     

> __< l​yanaqb:matrix.org >__ # References     

> __< l​yanaqb:matrix.org >__ - https://github.com/tari-project/bulletproofs-plus/blob/main/docs/quarkslab-audit/report.pdf     

> __< l​yanaqb:matrix.org >__ - https://blog.quarkslab.com/resources/2021-12-08_litecoin/21-08-872-REP.pdf     

> __< l​yanaqb:matrix.org >__ - https://blog.quarkslab.com/audit-of-the-mimblewimble-integration-inside-litecoin.html     

> __< l​yanaqb:matrix.org >__ # Audit Methodology Proposed     

> __< l​yanaqb:matrix.org >__ ## Discovery  (3d)     

> __< l​yanaqb:matrix.org >__ 3 days of discovery of:      

> __< l​yanaqb:matrix.org >__     - Adversary model for each proof     

> __< l​yanaqb:matrix.org >__     - Carrot construction     

> __< l​yanaqb:matrix.org >__     - Curve trees     

> __< l​yanaqb:matrix.org >__     - SoA: Original scheme + subaddress     

> __< l​yanaqb:matrix.org >__     - Janus attack (and other existing ones)     

> __< l​yanaqb:matrix.org >__ ## Proofs (~15d)     

> __< l​yanaqb:matrix.org >__ - Balance Recovery (~6d)     

> __< l​yanaqb:matrix.org >__ - Unlinkability (~2.5d)     

> __< l​yanaqb:matrix.org >__ # Timing     

> __< l​yanaqb:matrix.org >__ End November / December to start and execute is ok for us     

> __< l​yanaqb:matrix.org >__ Available for questions !     

> __< j​effro256:monero.social >__ Thank you, lyanaqb     

> __< j​effro256:monero.social >__ Does Cypherstack want to hop in?     

> __< s​gp_:monero.social >__ Yes, thank you!     

> __< d​iego:cypherstack.com >__ We'll do the work. In exchange for Monero.     

> __< j​effro256:monero.social >__ Let me know if I'm moving too fast, by the way, I just want to make sure to respect the guests' time     

> __< d​iego:cypherstack.com >__ Brandon Goodell is with us now (surae), and we're on-boarding three more cryptographers that will be reviewing the work as well.     

> __< r​ucknium:monero.social >__ lyanaqb: Same question to you. Do you have a specific person(s) on your team who would likely be the lead(s) on this review?     

> __< d​iego:cypherstack.com >__ Surae will be the primary overseer, with the bulk of the work and proving done by Freeman Slaughter (not a pseudonym), one of our new cryptographers.     

> __< rbrunner >__ :)     

> __< l​yanaqb:matrix.org >__ It will be one of the 3 Phd and an other one will be the reviewer for the quality process.     

> __< l​yanaqb:matrix.org >__ It will be one of the 3 PhD and an other one will be the reviewer for the quality process.     

> __< j​effro256:monero.social >__ Diego, thanks for the input. Following up on timing information, is the turnaround time still estimated to be 3-4 months?     

> __< d​iego:cypherstack.com >__ I'm also happy to take further questions.     

> __< d​iego:cypherstack.com >__ No. Things have cleared up significantly since then. MRL taking their time meant we got to clear a lot of work off of our plate.     

> __< d​iego:cypherstack.com >__ 3 weeks more likely.     

> __< j​effro256:monero.social >__ Alright, good to hear.     

> __< j​effro256:monero.social >__ Guests from Trail of Bits here?     

> __< LindsayTOB >__ Hi all - thanks for having us at your meeting! I’m Lindsay, sales manager at Trail of Bits - a software security research and development firm in Cyber security with specialized expertise in blockchain, cryptographic, and application security reviews.     

> __< LindsayTOB >__ I’m joined by Tjaden, a senior security engineer on our cryptography team, as well as Chris, our principal sales engineer.     

> __< LindsayTOB >__ We’re proposing a 4 engineer-week cryptographic design review of the Carrot (Cryptonote Address on Rerandomizable-RingCT-Output Transactions) specification, which includes Janus attack resistance. This work would be completed by 2 cryptographers over 2 calendar weeks. We currently have availably to begin work this month!      

> __< LindsayTOB >__ Please see notable similar reviews include: - Zcash: https://github.com/trailofbits/publications/blob/master/reviews/Zcash.pdf -Stealth addresses: https://github.com/trailofbits/publications/blob/master/reviews/2023-02-ryanshea-practicalstealthaddresses-securityreview.pdf (Stealth address scheme for ethereum-based privacy coin - found a number of de-anonymization issues.      

> __< LindsayTOB >__ Public examples of our cryptographic design reviews to see work and deliverable we’ll produce include: -Discord https://github.com/trailofbits/publications/blob/master/reviews/2024-08-discord-dave-protocol-designreview.pdf Ockam: https://github.com/trailofbits/publications/blob/master/reviews/2023-11-ockam-designreview.pdf     

> __< LindsayTOB >__ Happy to answer any questions!     

> __< s​gp_:monero.social >__ Nice to see you again Lindsay (Justin from MAGIC Grants here). Thanks for your proposal     

> __< LindsayTOB >__ We're glad to be here, Justin - great to be in touch again!     

> __< rbrunner >__ The field of companies doing such reviews seems to be bigger than I would have estimated, interesting     

> __< r​ucknium:monero.social >__ Lindsay, do you have an idea of who in your company may be the lead(s) on a review of Carrot?     

> __< e​phemeral2:matrix.org >__ I was assuming everyone had copies or summaries of the proposals; should I share our timeline / availability info here for convenience?     

> __< e​phemeral2:matrix.org >__ Seeing as the other proposers have so far in this channel. This is our first time proposing for Monero, so getting the hang of it still.     

> __< LindsayTOB >__ The project team is chosen based on each engineer’s skill set and availability, so it may vary. We have a few cryptographers in mind, but it will likely be Jim Miller, engineering director of our cryptography team, Filipe Casal, Principal Security Engineer, Fredrik Dahlgren, Principal Security Engineer, and/or Tjaden Hess, Senior Security Engineer     

> __< j​effro256:monero.social >__ Yes, feel free to attach any info that you would like to share more openly!     

> __< r​ucknium:monero.social >__ You can share what you wish. I think jeffro256  was cautious about what to share since some firms want to keep some details non-public. I guess for competitive reasons.     

> __< r​ucknium:monero.social >__ Thanks, Lindsay     

> __< j​effro256:monero.social >__ Note that this room is not normally invite-only as has publicly available logs     

> __< j​effro256:monero.social >__ Note that this room is not normally invite-only and has publicly available logs     

> __< r​ucknium:monero.social >__ Yes this room is logged: https://libera.monerologs.net/monero-research-lab     

> __< j​effro256:monero.social >__ This should've been mentioned in the emails / Slack chats but it probably good to reiterate     

> __< j​effro256:monero.social >__ And yes, thank you, Lindsay. Finally, I welcome Ben and Alp from Veridise to join in at the moment if desired.     

> __< b​en_sepanski:matrix.org >__ Hi all! My name is Ben, I am the CSO at Veridise     

> __< b​en_sepanski:matrix.org >__ Veridise is a security firm that works across the blockchain tech stack, but is especially well-known for our work in ZK-circuits and in-house expertise in building and applying automated security analyses in tandem with manual reviews. We have worked with projects like the Manta Network, o1js, Linea, Succinct, and RiscZero to secure their circuits, including both extensive review<clipped messag     

> __< b​en_sepanski:matrix.org >__ s for cryptographic vulnerabilities as well as common ZK or logical errors. We worked with Monero earlier this year to help ascertain the security of a new dlog-commitments. This effort was led by Alp Bassa , who would also be leading the work on the carrot protocol     

> __< r​ucknium:monero.social >__ Monero is a community-based project, has no CEO, no premine, etc. as many of you know. R&D decisions are subject to community scrutiny :)     

> __< b​en_sepanski:matrix.org >__ Alp joined Veridise in 2022 after spending over a decade as a mathematics professor in academia. Alp has extensively published in number theory, algebraic geometry, cryptography and coding theory. He holds a double major in computer science and mathematics and earned his PhD from the University of Duisburg-Essen. After postdoctoral positions in the Number Theory Group at the Écol<clipped messag     

> __< b​en_sepanski:matrix.org >__ e Polytechnique Fédérale de Lausanne (EPFL), the Cryptology Research Group lead by Ronald Cramer at the CWI-Amsterdam and the Coding Theory and Cryptography Group at NTU Singapore, he joined the faculty at Sabanci and Bogazici Universities in Istanbul. At Veridise, Alp works at the intersection of research and in-house tool development. He also participates in security audits, e<clipped messag     

> __< b​en_sepanski:matrix.org >__ specially those requiring a deep understanding of mathematics and cryptography.     

> __< b​en_sepanski:matrix.org >__ We'd be happy to answer any questions about the proposal! Timeline-wise, we are expecting it to take around four weeks, and can start by in the next one to two weeks     

> __< b​en_sepanski:matrix.org >__ We'd be happy to answer any questions about the proposal! Timeline-wise, we are expecting it to take around four weeks, and can start in the next one to two weeks     

> __< r​ucknium:monero.social >__ I should say "community input and scrutiny"     

> __< d​iego:cypherstack.com >__ all of you smarties should join forces with us and we can make an ultra super mega powerful privacy protocol :D     

> __< r​ucknium:monero.social >__ Ah, but competition is good. Diego wanting to form a monopoly :P     

> __< s​yntheticbird:monero.social >__ *smarties* are candy.     

> __< d​iego:cypherstack.com >__ I meant for Monero >:(     

> __< e​phemeral2:matrix.org >__ Ack. Zellic:     

> __< e​phemeral2:matrix.org >__ - Work will be conducted over a 4 calendar-week period     

> __< e​phemeral2:matrix.org >__ - Availability starts around the beginning of November, to the beginning of December at the latest     

> __< e​phemeral2:matrix.org >__ - Our estimate is 3 engineer-weeks of effort for the proofs and peer review, and we're also providing MRL the option for 1 additional engineer-week as an extension if it is needed.     

> __< e​phemeral2:matrix.org >__ One thing we want to note for the group is that the amount of time proof writing takes can vary and isn't always 100% predictable. Sometimes properties turn out to be very straightforward and easy to prove. Other times, it may turn out harder than expected or the property doesn't actually hold (i.e. a proof is impossible), and we need to instead switch to proving a variant.     

> __< e​phemeral2:matrix.org >__ This is tricky from a project management standpoint, and to mitigate, we'll be in constant communication with MRL as we make progress. This would mean progress updates and asking for priorities/direction from MRL. This is so MRL gets the best value out of the time as possible.     

> __< e​phemeral2:matrix.org >__ We think 4 engineer-weeks is a safe amount of time to get it all done; 2 is maybe possible if everything turns out to be really easy to prove. We think 3 weeks + option for 1 week extension is a good middle ground here that saves MRL budget. So that's our overall rationale     

> __< r​ucknium:monero.social >__ jeffro256: What is the approximate labor time needed to implement Carrot in code? I am just thinking about which of our racehorses here (FCMP++ R&D, coding, Carrot R&D and coding) may finish last as we think about hard fork activation timing.     

> __< e​phemeral2:matrix.org >__ (our understanding is that this is essentially being funded by community members and not a foundation of sorts, so cost saving is important)     

> __< j​effro256:monero.social >__ So many wonderful people here. Thank you for attending and for your input ;). Any technical questions for specific guests?     

> __< r​ucknium:monero.social >__ In other words, how urgent is Carrot review?     

> __< r​ucknium:monero.social >__ Does kayabanerve have any questions?     

> __< j​effro256:monero.social >__ I would greatly prefer it not to slow down the FCMP++ upgrade, and it shouldn't. In the worst case, we can release FCMP++ and keep the same addressing protocol code we have now and bring Carrot in a few months after. That shouldn't happen, but it is what it is. Even if Carrot is on time, hardware wallets might take a while to catch up so we should be open to allowing non-Carrot tx<clipped messag     

> __< j​effro256:monero.social >__ s for a few months IMO     

> __< j​effro256:monero.social >__ The implementation is basically done, but the integration and inclusion with legacy wallet code is a bit trickier. I predict integration to be ready for review by EoY     

> __< j​effro256:monero.social >__ Which should be before FCMP++ hard fork activation     

> __< k​ayabanerve:matrix.org >__ Carrot can be implemented prior to review if we assume review will pass, but we need review prior to deployment.     

> __< k​ayabanerve:matrix.org >__ We also need review done 1-2 months before we ship it for deployment in case more work is needed.     

> __< k​ayabanerve:matrix.org >__ So ideally by EOY but arguably as late as February.     

> __< k​ayabanerve:matrix.org >__ I support a CCS now if jeffro is ready now.     

> __< r​ucknium:monero.social >__ "a CCS now" You mean a contract with a firm, now, right? We don't need a separate CCS, right?     

> __< r​ucknium:monero.social >__ (CCS = Community Crowdfunding System)     

> __< r​ucknium:monero.social >__ I think probably we can decide on this at next week's meeting. A lot of things to consider, but interested people should be able to consider them before next meeting IMHO.     

> __< j​effro256:monero.social >__ By the way Diego Salazar, ben_sepanski, Alp Bassa LunaZellic lyanaqb , LindsayTOB, feel free to leave whenever, or stay as long as you'd like. Thank you all for your consideration and patience! All of you are excellent candidates and we are lucky to have your time.     

> __< e​phemeral2:matrix.org >__ Thank you, jeffro256! Will commercials / price be discussed here or will that be a topic of separate discussion?     

> __< j​effro256:monero.social >__ Concrete prices won't be discussed in this meeting, except amongst a few members or with explicit approval from you     

> __< l​yanaqb:matrix.org >__ Quarkslab Team was very happy to present our proposal! Great end of session and talk soon !     

> __< j​effro256:monero.social >__ Thank you lyanaqb and QuarksLabs!     

> __< j​berman:monero.social >__ Thank you all, excellent candidates     

> __< d​iego:cypherstack.com >__ We at CS have a separate thing from all of this as an add-on item to the agenda for whenever this one is done.     

> __< e​phemeral2:matrix.org >__ All right. Thank you very much for the opportunity to present. It was a great meeting that was exceptionally well-run, and talk again soon!     

> __< LindsayTOB >__ Thanks again for having us! Trail of Bits is excited and eager to work with Monero to help the security of Carrot!     

> __< r​ucknium:monero.social >__ Diego Salazar: At this meeting? You can bring it up now.     

> __< j​effro256:monero.social >__ Rather, I should say, concrete prices won't be discussed in the meeting, period. It will be discussed outside this meeting, unless you explicitly give consent to share *within* this meeting     

> __< d​iego:cypherstack.com >__ Neat.     

> __< j​effro256:monero.social >__ Thank you, Luna and Lindsay! Have a great day     

> __< a​lpbassa:matrix.org >__ Thank you! Was nice meeting everyone. Have a nice meeting.     

> __< b​en_sepanski:matrix.org >__ Thanks all!     

> __< s​yntheticbird:monero.social >__ Who exactly that is part of MRL will lead the price negotiation off-meeting?     

> __< d​iego:cypherstack.com >__ In the next couple of weeks we at Cypher Stack will be releasing a paper on churning. It's obviously Monero-focused, but it applies to any small-anonymity set coins. The paper is pretty extensive. In conjunction, we've released a Monero churn tool. https://github.com/cypherstack/moneromixer     

> __< ChrisTOB >__ Thank you all!     

> __< d​iego:cypherstack.com >__ We'll also be releasing the code for how we ran simulations for part of the churn paper.     

> __< rbrunner >__ MoneroMixer is a cool name, but will probably rise quite a few eyebrows :)     

> __< d​iego:cypherstack.com >__ Monero Butter Maker     

> __< d​iego:cypherstack.com >__ will change name     

> __< d​iego:cypherstack.com >__ you know...cuz you churn butter     

> __< d​iego:cypherstack.com >__ I'm here all week, folks     

> __< s​yntheticbird:monero.social >__ I almost laughed. almost     

> __< r​ucknium:monero.social >__ Very interesting. Looking forward to reading it     

> __< d​iego:cypherstack.com >__ Not even a slight exhale from the nose?     

> __< d​iego:cypherstack.com >__ Yeah it was a preannouncement, I guess.     

> __< s​yntheticbird:monero.social >__ i did     

> __< rbrunner >__ Interesting that it did take until now until somebody sat down and built something like that.     

> __< d​iego:cypherstack.com >__ Slight spoiler: churns are only somewhat helpful     

> __< d​iego:cypherstack.com >__ but I think that's been suspected for some time     

> __< r​ucknium:monero.social >__ AFAIK, a churner has been built at least twice before now.     

> __< r​ucknium:monero.social >__ But with no theoretical backing     

> __< d​iego:cypherstack.com >__ But with FCMPs right around the corner hopefully it won't matter that much     

> __< j​effro256:monero.social >__ I'm open to sharing it with people that have been in the MRL a while, I just don't want to leak financial details to the public in an *easily-accessible* way     

> __< rbrunner >__ But maybe with a less solid, well, scientific basis?     

> __< d​iego:cypherstack.com >__ but, not to dog on you guys on MRL, work can sometimes go slow, and work can sometimes go fast.     

> __< j​effro256:monero.social >__ yeppp     

> __< d​iego:cypherstack.com >__ So since the exact release time of FCMPs is unknown, we thought it'd be good to have some things available to the public while we wait for the FCMP goodness     

> __< s​yntheticbird:monero.social >__ Can I assist to the negotiation? I haven't contributed in the MRL but I'm highly interested into learning the process.     

> __< d​iego:cypherstack.com >__ Because, all of our findings on the usefulness of churn go out the window with FCMPs. As in, the tests and heuristics that would apply to current Monero don't apply after FCMPs go live. Which is kind of a 'no duh, that's why we're moving over' thing, I guess. :P     

> __< rbrunner >__ Will negotiations proceed with all companies until a definite offer is on the table, or will the field get narrowed down first?     

> __< k​ayabanerve:matrix.org >__ Rucknium: No, a CCS. The Research CCS isn't scoped to Carrot.     

> __< r​ucknium:monero.social >__ Ok. That changes the timeline     

> __< k​ayabanerve:matrix.org >__ Even if there wasn't that procedural issue, I was not involved with the Carrot process and would need to be cc'd on and review those discussions to personally endorse. There's also some question of how much that stretches the Research CCS since it's 25% done (good) but we haven't started audits (bad).     

> __< j​effro256:monero.social >__ rbrunner: that's a good question. I think we can narrow it down some first     

> __< d​iego:cypherstack.com >__ Given that I gave my price in Monero, you guys would be getting a steal now :D     

> __< j​effro256:monero.social >__ I don't know if there will be "negotiations" in the sense that we try to advocate for a lower price based on the offers of others, but we'll see     

> __< s​yntheticbird:monero.social >__ understood     

> __< r​ucknium:monero.social >__ Technically there are two more agenda items, (1) Stressnet and (2) The 10 block lock. AFAIK, there is not much to discuss about stressnet (except my spamming wallets ran out of money and I needed to replenish them).  On the ten block lock, I don't plan to do more research on it in the short term. Maybe someone else has something to discuss on those items.     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone!     

> __< j​effro256:monero.social >__ To follow up on previous discussions about including Janus resistance in the scope of properties for which we want security proofs, I advocate that we do include it. The difference in quotes to include Janus resistance was 25%-33%, which is reasonable. Also, I've had a few people ask me about Janus attacks and my general feeling is that the general Monero audience doesn't yet enti<clipped messag     

> __< j​effro256:monero.social >__ rely understand how Janus attacks works, which makes user-side mitigations hard. This should be an argument in favor of prioritizing it IMO     

> __< j​effro256:monero.social >__ Yes, given that the XMR/fiat price has had some pretty substantial action, would you like to amend the quoted XMR price before a formal decision?     

> __< d​iego:cypherstack.com >__ What'd I quote? 125?     

> __< d​iego:cypherstack.com >__ Sure. Updated quote to 126 XMR.     

> __< j​effro256:monero.social >__ Duly noted :)     

> __< k​ayabanerve:matrix.org >__ Oh. I had a brief dev update. I believe I've finished making divisors constant time. boog900: really helped with the complexity of one segment. I do believe I have better benchmarks on the topic now.     

> __< j​effro256:monero.social >__ Does anyone have any observations about specific auditors based on the information provided by the guests, pros or cons?     

> __< k​ayabanerve:matrix.org >__ I'm now continuing work on cleaning the dataflow of the proof (not the internal gadgets/functions) to make that proper. Then I'll add support for the multi-input case (within a single proof).     

> __< j​effro256:monero.social >__ Awesome! Great to hear     

> __< k​ayabanerve:matrix.org >__ I'd appreciate and advocate for Janus inclusion in Carrot.     

> __< r​ucknium:monero.social >__ I liked when firms gave specific relevant examples of past work.     

> __< s​yntheticbird:monero.social >__ when I see some of them I kneel.     

> __< s​yntheticbird:monero.social >__ when I see some of them I kneel 🧎‍♂    

> __< r​ucknium:monero.social >__ I am thinking about firms that have already participated in FCMP++ review vs. those that have not. It is "good" when a firm already knows FCMP++ because they can apply what they know. It is "good" when a firm has not looked at FCMP++ yet since they could spot something with fresh eyes that previous reviewers missed.     

> __< s​yntheticbird:monero.social >__ I guess we can't take two of them at the same time? not enough money ?     

> __< j​effro256:monero.social >__ If it makes sense, we *could* do what we did with FCMP++: have one firm create proofs and the other review the proofs     

> __< j​effro256:monero.social >__ Is it overkill for Carrot which bears many similarities to the current addressing protocol and for which we also need implementation reviews? Maybe, maybe not     

> __< j​effro256:monero.social >__ Does anyone *object* to including a security proof for Janus resistance for up to 33% higher review costs?     

> __< j​effro256:monero.social >__ This is a thought that I have had too...     

> __< j​berman:monero.social >__ Not from me, it's worth that cost imo. the Janus attack is a pretty significant knock on subaddresses     

> __< rbrunner >__ Not me. We should do it right. We will probably live years with this addressing scheme.     

> __< r​ucknium:monero.social >__ Janus resistance proof sounds good to me :)     

> __< k​ayabanerve:matrix.org >__ I don't think FCMP++ prior matters.     

> __< rbrunner >__ I feel with syntheticbird. It's somehow breathtaking how big the field of cryptography has become in the wake of cryptocurrencies, smart contracts and such.     

> __< k​ayabanerve:matrix.org >__ Re: Carrot, we have address of a form (S, V) or (S_i, V_i) and need to generate a one-time key of O.     

> __< j​effro256:monero.social >__ I tend to agree with kayabanerve , but there are *sometimes* when the leaky abstraction of FCMP++ as presented in the Carrot spec *can* matter. For example, the privacy of collaborative transaction building in a Carrot-compatible way can be affected by how Bulletproofs are batched on the outputs     

> __< k​ayabanerve:matrix.org >__ BP structure is out of scope to Carrot     

> __< k​ayabanerve:matrix.org >__ So is the FCMP and GSP     

> __< k​ayabanerve:matrix.org >__ All that matters to Carrot is generation of an O whose x/y components are unknown to the deriver.     

> __< k​ayabanerve:matrix.org >__ (and is known to whoever has the dlogs for an address, and that the independent claims of Carrot are correct)     

> __< j​effro256:monero.social >__ But it still affects it somewhat. Since BPs+ are batched, the prover needs to know all amount commitments openings. If there was one BP+ per output, then there might be the possibility of doing collaborative transactions without knowing the amounts of the counterparties.     

> __< k​ayabanerve:matrix.org >__ Hm. It's a bit muddled due to F-S requirements but we should still be able to create a properly modular definition for the bounds expected by an addressing scheme.     

> __< k​ayabanerve:matrix.org >__ jeffro256: What in Carrot changes on this premise?     

> __< k​ayabanerve:matrix.org >__ Carrot is not a collaborative TX protocol and Carrot does detail communication of the commitment mask, but does not involve creating TXs at all per my view.     

> __< j​effro256:monero.social >__ Nothing written down in the spec currently, I'm just saying that it could have an affect on future applications     

> __< k​ayabanerve:matrix.org >__ It reads to me as if you're applying the role of Carrot to the sender when I'd argue it's primarily about the receiver.     

> __< k​ayabanerve:matrix.org >__ I fundamentally don't understand the point you're trying to raise so I'll drop it.     

> __< j​effro256:monero.social >__ As it pertains to the review as-is, prior FCMP++ knowledge probably isn't crucial     

> __< k​ayabanerve:matrix.org >__ Oh. That was the other thing. Veridise has worked on a component of the circuit. they haven't worked on the composition nor the entire circuit.     

> __< k​ayabanerve:matrix.org >__ We have a work history we can evaluate based off of. I wouldn't credit them a history on FCMP++s as relevant to this discussion.     

> __< j​effro256:monero.social >__ It's not super important so you don't have to worry about it until I think about how to reword it and bug you again ;)     

> __< j​effro256:monero.social >__ Yeah I think it's pretty uncontroversial to say that divisor work won't really be applicable to Carrot     

> __< j​effro256:monero.social >__ FCMP++ composition is the only thing somewhat directly applicable     

> __< k​ayabanerve:matrix.org >__ While uncontroversial, I'm unsure some people understand that distinction, hence why I wanted to explicitly state it.     

> __< j​effro256:monero.social >__ Didn't Cypherstack write an alternate addressing scheme for Monero which provided return addreses?     

> __< r​ucknium:monero.social >__ Salvium?     

> __< r​ucknium:monero.social >__ Diego Salazar: Do you want me to review the churning paper so that you can remove the "not peer reviewed" notice from your paper template? :D     

> __< d​iego:cypherstack.com >__ oooooooh     

> __< r​ucknium:monero.social >__ Not a double-blind review of course, but something     

> __< j​effro256:monero.social >__ Yes, that was what I was thinking of. However, it looks like old contributor knacc was the one who wrote it?     

> __< j​effro256:monero.social >__ Okay, well it's getting pretty far over. Do we want to make a decision next meeting to give some time to review details?     

> __< r​ucknium:monero.social >__ I think a decision could potentially be made next meeting.     

> __< j​effro256:monero.social >__ I've got to dip out, but thank you everyone for letting me take up such a large chunk of your time! The feedback was very helpful, and I look forward to perhaps making a decision soon     

> __< sneurlax >__ re: > <rbrunner>: MoneroMixer is a cool name, but will probably rise quite a few eyebrows :) -- sorry about that, I picked the name and have had moneromixer.com for years as a joke, suggest replacements freely haha     



# Action History
- Created by: Rucknium | 2024-10-01T21:08:26+00:00
- Closed at: 2024-10-15T17:02:15+00:00
