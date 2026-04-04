---
title: Monero Research Lab Meeting - Wed 27 August 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1261
author: Rucknium
assignees: []
labels: []
created_at: '2025-08-26T22:23:08+00:00'
updated_at: '2025-09-04T21:50:49+00:00'
type: issue
status: closed
closed_at: '2025-09-04T21:50:49+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Carrot follow-up audit](https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).

4. [Discussion: Replace Monero's hash-to-point function with the FCMP++ Upgrade](https://github.com/monero-project/research-lab/issues/142).

5.  MRL rooms moderation.

6. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).

7. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

8. CCS proposal: [kayabaNerve Finality Layer Book](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/604).

9. PoW mining pool centralization. [Monero Consensus Status](https://moneroconsensus.info/). [Bolstering PoW to be Resistant to 51% Attacks, Censorship, Selfish Mining, and Rented Hashpower](https://github.com/monero-project/research-lab/issues/136). [Mining protocol changes to combat pool centralization](https://github.com/monero-project/research-lab/issues/98).

10. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1256 

# Discussion History
## Rucknium | 2025-08-28T20:53:49+00:00
Logs
> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1261     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​rticmine:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< DataHoarder >__ Rare hi from me     

> __< v​tnerd:monero.social >__ Hi     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ Ping jeffro256     

> __< j​effro256:monero.social >__ Howdy     

> __< j​effro256:monero.social >__ thanks for the ping     

> __< r​ucknium:monero.social >__ me: Reading papers about selfish mining countermeasures and decentralized consensus protocols. Helping test rolling DNS checkpoints on testnet. Making fixes to moneroconsensus.info and moneronet.info     

> __< v​tnerd:monero.social >__ me: working on special build for dns checkpoint testing, and looking at carrot+lws stuff     

> __< j​berman:monero.social >__ me: fixed a couple bugs testing forking from current testnet (in the migration and in scanning), cleaned up the FFI (removed unwraps/asserts, used int error returns, de-duplicated some code with macros, clippy+fmt), implemented consolidated paths in the RPC for getting paths in the tree by global output id, reorganized curve trees db logic into a saner structure in prep for PR(s) <clipped message>     

> __< j​berman:monero.social >__ to the main monero repo, tested kayaba's latest prove/verify optimizations (good results!!)     

> __< tevador >__ me: researching selfish mining countermeasures (Hi)     

> __< j​berman:monero.social >__ Repeating from NWLB: good news for the stressnet: kayabanerve implemented linear prove() times, dropping 128-input tx construction down from 5m30s to ~1m!! Huge     

> __< j​effro256:monero.social >__ me: initiated communication about Carrot follow-up review by Cypherstack, updated FCMP++ benchmark tool for all the latest FCMP++ changes (github.com/jeffro256/clsag_vs_fcmppp_bench/), working on supporting high input counts in benchmark tool, working on patches in Monero core repo, re-reviewing the de-dup PR by rbrunner7, reviewed several PRs in seraphis-migration, did a write-up<clipped messag     

> __< j​effro256:monero.social >__  for an upcoming vuln disclosure, helped prepare v0.18.4.2 release. The de-dup PR does a great job at naturally excluding nodes from the known spy node list, which is great! https://github.com/monero-project/monero/pull/9939/#issuecomment-3228779989     

> __< a​rticmine:monero.social >__ I updated my comments on the FCMP++ weight function. I am also working on a full write-up on Monero s calling generally.     

> __< a​rticmine:monero.social >__ I am also working on the block signing remix     

> __< k​ayabanerve:matrix.org >__ monero-oxide migration, optimizations and improvements.     

> __< r​ucknium:monero.social >__ 3) [Carrot follow-up audit](https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).     

> __< j​effro256:monero.social >__ In communication w/ Cypherstack right now, clearing up scope and such b4 a quote. Is there anything about the scope that people here think should be changed?     

> __< j​effro256:monero.social >__ Or object generally?     

> __< j​effro256:monero.social >__ Or any questions?     

> __< j​berman:monero.social >__ It LGTM     

> __< rbrunner >__ Same here - as far as I understand such stuff ...     

> __< j​effro256:monero.social >__ One broad point about the scope we could try to tackle now is adding security arguments for a quantum-resistant migration.     

> __< j​effro256:monero.social >__ The amount commitments opening should be quantum resistant, the openings for address spend pubkeys I'm less sure about. Going down that path would surely expand the scope significantly. We could also try to tackle that later     

> __< j​effro256:monero.social >__ Or we might deem it unncessary     

> __< j​berman:monero.social >__ I would lean toward NACK on that for now since we have more auditing to get through to take fcmp++ to mainnet     

> __< j​berman:monero.social >__ and Carrot     

> __< j​effro256:monero.social >__ I would generally agree, but the option is there     

> __< tevador >__ Are the reasons for the protocol tweaks specified somewhere?     

> __< j​effro256:monero.social >__ Yes, but it's scattered about in different git commits. I should write down the rationals in one place     

> __< tevador >__ Yes, I think it should be part of the scope (to verify that the goal of each change is achieved).     

> __< k​ayabanerve:matrix.org >__ I haven't reviewed this and have no comment other than deferral to jeffro     

> __< r​ucknium:monero.social >__ Any more discussion of this item?     

> __< j​effro256:monero.social >__ tevador:     

> __< j​effro256:monero.social >__ By adding the amount to the derivation of the amount blinding factor, we add ~32 bits of security to Carrot-style openings of the amount commits, which potentially allows quantum-resistant migrations in the future.     

> __< j​effro256:monero.social >__ By removing the cofactor clear, our X25519 ECDH is A) faster, and B) easier to tweak a standards conformant library to get correct results.     

> __< j​effro256:monero.social >__ By removing K_s from anchor_sp, for accounts where there are two or more main addresses (i.e. hybrid key hierarchies), you would have to calculate-and-check anchor_sp that many times (which is not secure against collisions), or disable special enotes to yourself.     

> __< j​effro256:monero.social >__ By removing K^j_v from d_e, once s_sr (the X25519 ECDH exchange in normal enotes) is derived, you no longer need the private view-incoming key or subaddress table to scan normal enotes, which simplifies the scanning code.     

> __< tevador >__ OK, I think we can move onto the next item.     

> __< j​berman:monero.social >__ Generally agree with tevador's idea that above rationale makes sense to include in scope     

> __< r​ucknium:monero.social >__ 4) [Discussion: Replace Monero's hash-to-point function with the FCMP++ Upgrade](https://github.com/monero-project/research-lab/issues/142).     

> __< k​ayabanerve:matrix.org >__ We rely on the hash to point to be a collision resistant hash function to resolve the burning bug. The current HtP isn't a good CRH. We can add a new HtP in ~10 lines. jeffro256: volunteered to update the codebase so all CARROT outputs, already a new type, define their key image generator via a HtP. The FCMP++ upgrade makes it trivial to update the HtP. I've discussed this as a po<clipped message     

> __< tevador >__ I wrote my opinion on github. I don't think that the change is worth it. The security benefit is questionable.     

> __< k​ayabanerve:matrix.org >__ tential change for over a year. I just finally did the work to review our existing HtP and confirm it _should_ be replaced.     

> __< k​ayabanerve:matrix.org >__ tevador has prior advocated against the change due to the marginal increase in security. I'll note that while there's an explicit marginal benefit, the hash function also has implicit bias I'm not sure has ever been formally bounded.     

> __< k​ayabanerve:matrix.org >__ Even the unbiased version I'm proposing is bounded to 10/sqrt(q), so ~123 bis of security to my understanding.  That raises the question of how much worse the current version is.     

> __< j​effro256:monero.social >__ As to whether the security is worth it, I leave that to people smarter than me. However, if there is a valid argument for the increase in security, I am willing to update all my relevant code to handle that change.     

> __< k​ayabanerve:matrix.org >__ We can also make more than 10 lines of edits (100 lines?) To become standards compliant, as we *almost* are compliant with what became the standard, and optimize the resulting function by ~20-40% (but this isn't a performance critical fn after FCMP++). The main benefit is anyone who _uses_ Monero _without_ using the Monero C++ would be able to write a key image generator function <clipped message     

> __< k​ayabanerve:matrix.org >__ without writing bespoke elliptic curve arithmetic (due to any impl of the standard being relevant).     

> __< k​ayabanerve:matrix.org >__ If we define the security of our protocol as the security of the weakest component, I wouldn't be surprised if this HtP was _technically_ it.     

> __< tevador >__ It will be far more than 10 lines of code. Just the fact that RCT and FCMP transactions will coexist for some time will need to be coded for.     

> __< DataHoarder >__ my opinion, ^ I have been bitten by the bespoke ec math for hash to point specifically, otherwise I was able to make everything else using generic libraries     

> __< j​berman:monero.social >__ From my view: the benefit seems pretty small, and the change seems pretty small as well. It adds some complexity to manage as tevador notes     

> __< k​ayabanerve:matrix.org >__ The unbiased hash to point function is ~10 lines tevador     

> __< k​ayabanerve:matrix.org >__ The _call sites_ will be more, hence why the old RingCT code remains as-is and we use the separation _already introduced for CARROT outputs_ for the new HtP.     

> __< k​ayabanerve:matrix.org >__ We already have to delineate old outputs from CARROT outputs. cc jeffro256     

> __< j​berman:monero.social >__ FWIW in tree building we do already have an indicator determined by whether or not an output is Carrot or not (if Carrot, then consensus already made sure the output does not have torsion)     

> __< j​berman:monero.social >__ So it wouldn't be such a major change to introduce in there     

> __< k​ayabanerve:matrix.org >__ Even if it is just a few bits or just half a bit, we shouldn't sacrifice them for naught. The moment we realize any cryptography, we realize losses in our security. Our job should always be to minimize those.     

> __< k​ayabanerve:matrix.org >__ Else, these will add up and add up, and we'll end up with a protocol whose practical bound is lower than desired.     

> __< j​berman:monero.social >__ On the flip side, if someone wants to write a Monero wallet that can deal with older txs pre-FCMP++, I figure they would still need the old hash to point implemented too     

> __< tevador >__ Since the biased function is based on Elligator, its security might have been already studied. Could be worth looking into it more.     

> __< k​ayabanerve:matrix.org >__ It has, and the recommendation for an unbiased version when you need a CRH is from that research.     

> __< k​ayabanerve:matrix.org >__ Also, the 10 / sqrt(q) bound for calling it twice and summing the result is from an Elligator author.     

> __< tevador >__ You wrote above: "the hash function also has implicit bias I'm not sure has ever been formally bounded"     

> __< k​ayabanerve:matrix.org >__ It depends on the exact curve parameters due to the reduction from the order of the field the curve is defined over to the order of the curve.     

> __< k​ayabanerve:matrix.org >__ You'd need research specific to Curve25519, which may scrape by due to how small the primes are after the leading bit?     

> __< j​effro256:monero.social >__ FWIW, working with Carrot outputs in the Carrot libs already don't use much of the higher-level key image helper functions that the current code uses, because those are meant for univariate key images and the API would have to be modified     

> __< k​ayabanerve:matrix.org >__ But that research has been largely forsaken AFAICT because there's other reasons for bias leading people to simply invoke it twice for am unbiased variant, and formalize the bias on that instead     

> __< tevador >__ It's pretty likely that the bias is exactly 1 bit since it covers half of the curve.     

> __< k​ayabanerve:matrix.org >__ But you're right, I may have missed a prior formalized bound for single-invocation Elligator over Curve25519     

> __< k​ayabanerve:matrix.org >__ tevador: I'm pretty sure some resulting points appear more frequently due to the difference in orders.     

> __< tevador >__ It's possible.     

> __< k​ayabanerve:matrix.org >__ It's part of the commentary from Hamburg when the IRTF standardized hash to points.     

> __< k​ayabanerve:matrix.org >__ That's the 'implicit, unformalized' bias I'm gesturing at.     

> __< k​ayabanerve:matrix.org >__ But again, Curve25519 moduli are favorable _and_ the torsion clear may also be beneficial?     

> __< k​ayabanerve:matrix.org >__ It's just a such a mess we can either research it or fix it, and it's the perfect time to fix it.     

> __< tevador >__ I think we should investigate and also model worst case attacks. I think even if you can find a collision in Hp, I don't think it implies you can burn an ouput.     

> __< k​ayabanerve:matrix.org >__ See jberman, jeffro256 noting we have the perfect spots to deal with this.     

> __< k​ayabanerve:matrix.org >__ It does because if you have the outgoing view key.     

> __< k​ayabanerve:matrix.org >__ You can create two outputs with the same discrete logarithm for their key image, and then you solely need a key image generator collision to perform a burn.     

> __< tevador >__ For RCT it does not imply burning an output. I'm not very familiar with Carrot.     

> __< k​ayabanerve:matrix.org >__ It's an FCMP++ comment, not a CARROT comment. You're right for RingCT.     

> __< tevador >__ If FCMP is more vulnerable than RCT, the update can make more sense.     

> __< k​ayabanerve:matrix.org >__ FCMP++ allows users to publish what _were_ RingCT private spend keys and are _now_ FCMP++ outgoing view keys for _newly created wallets_.     

> __< k​ayabanerve:matrix.org >__ The only reason that's safe is because the key image generator is a CRH binding to the outgoing view key _and_ the private spend key.     

> __< k​ayabanerve:matrix.org >__ See the difficulties Seraphis had with the burning bug, leading Seraphis to define the outgoing view key as a point _and_ a scalar whose ratio formed the linking tag.     

> __< tevador >__ ^ I don't think this was mentioned in your proposal on github. That's a pretty strong point.     

> __< k​ayabanerve:matrix.org >__ I did say we require it to be a CRH to stop the burning bug 😅     

> __< k​ayabanerve:matrix.org >__ But I'm sorry I didn't provide sufficient context/background on that     

> __< j​effro256:monero.social >__ Although it might be that if people scan CARROT enotes honestly, they can always avoid a burn even if the hash-to-point is not coliision resistant since it would always be the case that x!=x' for some O = x G + y T and O' = x' G + y' T if O!=O'.     

> __< k​ayabanerve:matrix.org >__ I don't believe so since they only have to be able to scan one of them, not both.     

> __< j​effro256:monero.social >__ Yes, and the other one is guaranteed to have the same one-time address EC point. Assuming the receiver is scanning honestly (and thus recomputes the one-time address as a function of their spend pubkey), only the receiver should know the discrete logarithm of that point, so the other can't spend it     

> __< k​ayabanerve:matrix.org >__ IMO, this has sufficient feasibility and acknowledgement to move forward, at least within the scope of this meeting which is 50m in over only a few topics.     

> __< k​ayabanerve:matrix.org >__ jeffro256: No, they aren't.     

> __< k​ayabanerve:matrix.org >__ They're guaranteed to have the same key image discrete logarithm and the same key image generator.     

> __< k​ayabanerve:matrix.org >__ The whole ides is two different one-time addresses can share a key image if the CRH property of the HtP is broken.     

> __< k​ayabanerve:matrix.org >__ They're allowed to have distinct `y` values.     

> __< r​ucknium:monero.social >__ Discussion can continue in the GitHub issue and next meeting. Thanks.     

> __< r​ucknium:monero.social >__ 5) MRL rooms moderation.     

> __< r​ucknium:monero.social >__ SyntheticBird: You suggested this item.     

> __< s​yntheticbird:monero.social >__ Hi     

> __< s​yntheticbird:monero.social >__ Yes     

> __< k​ayabanerve:matrix.org >__ Now, is CARROT sufficient to convert the problem from finding a collision to second preimage, which would remain secure? Maybe. Even if, we shouldn't place that bound on CARROT.     

> __< o​frnxmr:monero.social >__ Too much spam & trolling in lounge, not enough kicks or mutes     

> __< k​ayabanerve:matrix.org >__ A member here has sent nothing of value, insulted me for days, and arguably even made a threat.     

> __< s​yntheticbird:monero.social >__ I have a few complaints regarding the current moderation of the research channel. It comes to no surprise i think that the quality of discussions have degraded in the recent qubic events. What would before be reserved to #monero is now disrupting monero lounge, rarely monero lab. I would like to discuss if there is a possibility to increase moderators in these zones. The discussio<clipped me     

> __< s​yntheticbird:monero.social >__ ns are not constructive, arguments repetetive and often turns into shilling fight whenever a random or a bot comes in to stir the pot.     

> __< c​aptaincanaryllc:matrix.org >__ more moderation would be welcome     

> __< s​yntheticbird:monero.social >__ If the increase in moderator is not justified then I would ask the moderators to be more strict     

> __< r​ucknium:monero.social >__ Conversations should move according to the procedure: #MRL (heaven) -> #MRL-Lounge (purgatory) -> #Monero-Beef (hell).     

> __< j​effro256:monero.social >__ I think that CARROT converts the problem of finding the same x to also finding a collision on the hash-to-scalar, but I'll think about it some more. Though I do agree that it's a bit sketchy for CARROT to have that bound     

> __< o​frnxmr:monero.social >__ I dont even think beef is necessary for a lot of this, not that lounge is purgatory. some of these topics arent "off topic" but are time sinks and distractions     

> __< s​yntheticbird:monero.social >__ Yeah ngl, interestingband case is kind of annoying. He have a beef with the people with permissioned which either ignore him or maybe do not want to appear like mod abusing. But he has passed the point of being constructive     

> __< tevador >__ I'm not sure how moderation can work with the relays, at least from the IRC side. But I agree that this room should be more strictly moderated.     

> __< r​ucknium:monero.social >__ "Stir the pot" and "producing more heat than light" should be avoided in all MRL rooms, observed voluntarily on the part of participants, if possible.     

> __< c​aptaincanaryllc:matrix.org >__ some pretty lazy attempts at manipulation/subversion happening in lounge on regular basis since qubic     

> __< s​yntheticbird:monero.social >__ Rucknium: I totally agree and in the fact no moderator intervene when this is obviously the case.     

> __< c​aptaincanaryllc:matrix.org >__ even to the point of harassing devs just to waste time     

> __< DataHoarder >__ I have been trying to sync up the new bridge to deploy it soon, probably starting with specific monero rooms first. It can make moderation from Matrix side easier, as each user on IRC will appear distinct     

> __< r​ucknium:monero.social >__ A scientific tone is appreciated.     

> __< o​frnxmr:monero.social >__ And worse, long term members (..and mods) are dragged into it and make it worse     

> __< s​yntheticbird:monero.social >__ It's not just a matter of ban but also telling people to stop the false discussion because its disrupting other to introduce another useful talk     

> __< DataHoarder >__ Mapping of bans/kicks on each side is a feature that it has, although not widely tested (and relay on irc side would need at least half-op rights)     

> __< o​frnxmr:monero.social >__ I think lounge should be related to work, and people working     

> __< o​frnxmr:monero.social >__ Not AMA     

> __< DataHoarder >__ This is in response of your ask about relays, tevador      

> __< tevador >__ DataHoarder: thanks     

> __< c​aptaincanaryllc:matrix.org >__ I think that any kind of hyperbole in that channel seems detrimental     

> __< DataHoarder >__ monero.social Matrix gods allow, this should finish syncing up today (it's up to the 25th of July now, it has been syncing up from 2024 events)     

> __< r​ucknium:monero.social >__ DataHoarder has been MVP recently 🎉     

> __< s​yntheticbird:monero.social >__ DataHoarder, very excited to see the new bridge operational     

> __< r​ucknium:monero.social >__ (Not minimum viable product, but most valuable player)     

> __< DataHoarder >__ I was MVP 20+ years ago :)     

> __< o​frnxmr:monero.social >__ Can i be the lowercase mvp?     

> __< DataHoarder >__ People find their way in these channels and usually get asked to move elsewhere for specific discussions, but some just ... continue     

> __< s​yntheticbird:monero.social >__ I think first things we could try get a rough consensus on is whether new moderators are necessary     

> __< DataHoarder >__ after that, a mute or enforcement could be necessary to prevent channel spam     

> __< r​ucknium:monero.social >__ Any more to say on this item?     

> __< o​frnxmr:monero.social >__ diego  cc     

> __< s​yntheticbird:monero.social >__ Rucknium: i think i'm good, the discussion can happen later.     

> __< p​lowsof:matrix.org >__ isn't Rucknium mod here and in lounge yet?     

> __< c​haser:monero.social >__ keeping out Qubic sock puppets and concern trolls IMHO is paramount, otherwise valuable discussions and valuable contributors will be turned away from participation. the current admins seem to be MIA. I wouldn't mind having more of them.     

> __< o​frnxmr:monero.social >__ No     

> __< r​ucknium:monero.social >__ I'm not mod of any room. I was mod of -beef 😢     

> __< s​yntheticbird:monero.social >__ Butcherium     

> __< o​frnxmr:monero.social >__ You are 😆     

> __< r​ucknium:monero.social >__ I prefer not to have mod powers because mod powers involves you in controvery unnecessarily, but if it's for the collective good, then I can get mod powers.     

> __< r​ucknium:monero.social >__ The collective good has spoken, it seems.     

> __< p​lowsof:matrix.org >__ you moderate meetings here, lounge can be handled by banhammer     

> __< o​frnxmr:monero.social >__ lounge can be handled by ruck     

> __< r​ucknium:monero.social >__ [Note to IRC side: I am admin now in Matrix MRL room]     

> __< o​frnxmr:monero.social >__ I'd volunteer, but yknow how that goes     

> __< s​yntheticbird:monero.social >__ if he wishes so tho     

> __< r​ucknium:monero.social >__ 6) [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).     

> __< d​iego:cypherstack.com >__ Lel     

> __< o​frnxmr:monero.social >__ articmine updated comment today     

> __< k​ayabanerve:matrix.org >__ Rucknium: I prefer turkey     

> __< j​berman:monero.social >__ I'm still not understanding why the disincentive should be so strong for 128-in versus 16x 8-in     

> __< s​yntheticbird:monero.social >__ chain bloat     

> __< ArticMine >__ My thought on this is that we can separate the weight that is due to proofs from the rest of the transaction weight and then apply a function so that after the quadratic penalty the fee tracks verification time more closely     

> __< o​frnxmr:monero.social >__ chain bloat is easier with lower input txs     

> __< o​frnxmr:monero.social >__ https://github.com/seraphis-migration/monero/issues/44#issuecomment-3228882784     

> __< s​yntheticbird:monero.social >__ mea culpa i thought the opposite     

> __< o​frnxmr:monero.social >__ 1 and 2 input txs are the longest verification and highest size     

> __< ArticMine >__ if one want to maximize spam with mined transaction the smallest weight is optimal      

> __< ArticMine >__ sinnce this is where the penalty is lowest     

> __< ArticMine >__ So there is a case to counterbalance this by favoring large transactions     

> __< j​berman:monero.social >__ I'm not sure I fully follow, Artic are you proposing to update the original proposal with new forumlas?     

> __< o​frnxmr:monero.social >__ 2c: If fees are set linearly per-input, higher input txs end up paying more per byte than lower input     

> __< ArticMine >__ If we want the fees to be close to linear with verification time then we will have to apply a weight formula to favor large transactions     

> __< ArticMine >__ So if this is the wish of the community then yes     

> __< ArticMine >__ My main concern here is that the transactions be economic to mine     

> __< j​berman:monero.social >__ linear would mean that it is roughly comparable cost to construct 16x 8-in's compared to 1x 128-in, not to make one more favorable than the other     

> __< ArticMine >__ Yes     

> __< k​ayabanerve:matrix.org >__ I think we should set an 8-in/4-out limit and not _have_ large transactions.     

> __< j​berman:monero.social >__ (although I think there is a stronger argument for 16x 8-in's to cost more)     

> __< ArticMine >__ This needs a square root weight formula on the proof part of the weight     

> __< k​ayabanerve:matrix.org >__ Alternatively, a linear weight sounds fine without favoring either side. If anything, I'd call for large TXs to pay notably more than smaller TXs to provide an economic incentive for people to move to small TXs, as we may require in the future.     

> __< ArticMine >__ My point is we can tune the weight formula to what ever is desired     

> __< DataHoarder >__ P2Pool coinbase outputs :)     

> __< o​frnxmr:monero.social >__ Why should my wallet bloat the chain by splitting my tx into 16 instead of just sending the damn thing     

> __< k​ayabanerve:matrix.org >__ ofrnxmr: Transaction uniformity.     

> __< DataHoarder >__ those tend to be plenty, and small, which with this change would make using p2pool more expensive than a centralized pool due to even higher fees     

> __< k​ayabanerve:matrix.org >__ And again, this may become a hard requirement in the future. We want people to get prepared now with solutions now.     

> __< k​ayabanerve:matrix.org >__ I have been told no to 8/4 and I think you all are horrible people who hate privacy and don't understood anything /s     

> __< s​yntheticbird:monero.social >__ me but unironically     

> __< o​frnxmr:monero.social >__ Tx uniformity would be a fixed 1 or 2 input tx, not 8 4 2 1     

> __< ArticMine >__ So i propose we separate the proof parts of the total weight from the rest of the transaction weight, then I can provide options for consideration     

> __< k​ayabanerve:matrix.org >__ On a legitimate note, if we have an end goal of uniformity, we will decrease from 128 in. I understand we aren't doing so now. We should still nudge people towards less and less inputs per TX.     

> __< k​ayabanerve:matrix.org >__ 8 in/4 out is a valid uniformity target ofrnxmr     

> __< k​ayabanerve:matrix.org >__ Dummy inputs/dummy outputs     

> __< j​berman:monero.social >__ > I intend to break out membership proof size and verify time into 2 additional columns     

> __< j​berman:monero.social >__ I can do this today     

> __< o​frnxmr:monero.social >__ my input count on ringct has privacy issues (cospends). What issues for fcmp?     

> __< k​ayabanerve:matrix.org >__ 4/3 is a minimum established by CARROT.     

> __< o​frnxmr:monero.social >__ ..afaict, uniformity doesnt add privacy w/o knowledge linking the inputs together     

> __< o​frnxmr:monero.social >__ And with fcmp, its my understanding that the history of the inputs arent linkable to their origins     

> __< c​haser:monero.social >__ I (non-sarcastically) agree reducing the number of in/out combinations is a legitimate and viable way toward tx uniformity, and would nudge people toward that even without universal dummies and IVC     

> __< k​ayabanerve:matrix.org >__ ofrnxmr: More inputs signifies you're an exchange or service provider.     

> __< o​frnxmr:monero.social >__ no it doesnt     

> __< k​ayabanerve:matrix.org >__ It's a long-term goal for all TXs to be indistinguishable, which would include fixed input/output count.     

> __< r​ucknium:monero.social >__ Number of inputs in a FCMP tx probably only gives information to the tx recipient, not an external blockchain observer.     

> __< c​haser:monero.social >__ ofrnxmr: it still betrays a lower bound on how many enotes you own in that wallet     

> __< k​ayabanerve:matrix.org >__ With statistical likelihood? Yes. A new user who just joined the network won't have 128 inputs on day one.     

> __< o​frnxmr:monero.social >__ I can have 128 x 10$ inputs and be spending $1000     

> __< k​ayabanerve:matrix.org >__ It leaks how many TXs the creator of the TX was involved with.     

> __< ArticMine >__ A very important point. If we have minimums with 4in then the reference transaction weight will have to be changed      

> __< ArticMine >__ and very likely the minimum penalty free zone     

> __< k​ayabanerve:matrix.org >__ So I do want to encourage Monero down that path, but obviously, we can't jump down to the end of 8/4.     

> __< k​ayabanerve:matrix.org >__ So an economic incentive for fewer inputs may be a good first step.     

> __< o​frnxmr:monero.social >__ i think this is a non-issue, and disagree that there should be incentive to blocat the chain for pseudo privacy     

> __< o​frnxmr:monero.social >__ Its not an economic incentive for node runners to store more data for less money     

> __< ArticMine >__ In other words if the minimum transaction weight is going to be say between 10000 bytes and 20000 bytes then ZM will meed to increase to 2000000 bytes     

> __< k​ayabanerve:matrix.org >__ Also, we're limiting inputs to 128 with FCMP++, and I'd support limiting to 64 in the future as well.     

> __< k​ayabanerve:matrix.org >__ Taking steps.     

> __< j​effro256:monero.social >__ ArticMine: that 4/3 is a minimum bound for a maximum limit rule. Txs can still have 1-3 ins     

> __< tevador >__ Is dummy input support planned for FCMP? Proposed here: https://github.com/monero-project/research-lab/issues/96#issuecomment-2104091836     

> __< k​ayabanerve:matrix.org >__ Not planned.     

> __< j​berman:monero.social >__ not at the moment no     

> __< ArticMine >__ ... but will they be the same weight as 4in?     

> __< k​ayabanerve:matrix.org >__ But it'd work and wouldn't be the most difficult, nor the most costly :) You did good tevador     

> __< j​effro256:monero.social >__ Although I think it's really more like 3/2, but it depends on how you count it     

> __< j​effro256:monero.social >__ ArticMine: depends on how we end up defining weight. Byte size? No. Should it be the same weight? Almost certainly noyt     

> __< k​ayabanerve:matrix.org >__ TL;DR IMO, long-term goal of uniformity. TX cost should respect byte size _and_ verification cost, as the Bulletproof clawback does. We can step towards uniformity by additionally penalizing large TXs so that it's cheaper to do small TXs instead.     

> __< o​frnxmr:monero.social >__ Low input txs***     

> __< k​ayabanerve:matrix.org >__ We don't have to agree on uniformity as a goal now. We can start just by discussing if weight should be linear to size and time, or just size, or what     

> __< o​frnxmr:monero.social >__ Those are larger per input, so not "small"     

> __< k​ayabanerve:matrix.org >__ I can sidetrack us with a penalty on large TXs later     

> __< j​berman:monero.social >__ Back-tracking a bit, my opinion on weights assuming we maintain the current plan to support up to 128 inputs: I think a formula with linearly increasing weight will probably be simplest and easiest to justify. But will review artic's updates to the proposal, and will break out membership proof size and verification times     

> __< ArticMine >__ What i do need is typical transaction weights for the bulk of the transactions currently 2in     

> __< ArticMine >__ if these are replace by 3in or 4in     

> __< tevador >__ What would be the size of 4/3?     

> __< ArticMine >__ that is what I need to knnpw     

> __< o​frnxmr:monero.social >__ This is smooth brained, but again: charging a fixed amount _per input_ ends up more costly _per byte_ for higher input txs, with no obvious penalty to the user     

> __< o​frnxmr:monero.social >__ kayaba     

> __< j​berman:monero.social >__ Here is a table with all FCMP++/Carrot tx sizes and verification times, for all input and output combinations: https://github.com/seraphis-migration/monero/issues/44#issuecomment-3150754862     

> __< ArticMine >__ my understanding is between 10000 and 20000 bytes     

> __< ArticMine >__ for 4in     

> __< tevador >__ The table says 10462     

> __< k​ayabanerve:matrix.org >__ I'd be fine with byte size + fixed amount per input to be respective of verification time. That doesn't encourage making smaller TXs though. Larger TXs are still favored due to their smaller overall byte size.     

> __< ArticMine >__ 4in are still below 13000 bytes     

> __< j​effro256:monero.social >__ Byte size for Carrot 4-in is 10240-12216     

> __< k​ayabanerve:matrix.org >__ But I'd be fine with it. I'm not trying to force in my policies on uniformity today. I've conceded it's a long-term goal at best. I thought an economic penalty may be a decent first step.     

> __< tevador >__ A (nearly) fixed tx size would remove a lot of the issues with fee scaling.     

> __< ArticMine >__ So most likely changing TR to 15000 bytes and ZM to 1500000 bytes would work     

> __< ArticMine >__ it is a very simple change      

> __< ArticMine >__ on my part     

> __< o​frnxmr:monero.social >__ Miners get paid more per byte but less per verification time. Users dont see any difference     

> __< j​effro256:monero.social >__ Is ZM the penalty free minimum ? I don't know how I feel about increasing that...     

> __< ArticMine >__ Miners get paid per byte of weight      

> __< ArticMine >__ Yes XM is the penalty free minimum     

> __< ArticMine >__ ZM     

> __< ArticMine >__ My question is: do we have consensus for 4in as a standard     

> __< ArticMine >__ If so i can implement the scaling changes     

> __< o​frnxmr:monero.social >__ No     

> __< j​effro256:monero.social >__ Miners ostensibly don't care about transaction verification time unless it affects the speed of their block propagation. Ideally, each transaction in their mined block is already in honest nodes' mempools already     

> __< j​effro256:monero.social >__ I don't think 4-in should be a standard IMO, IIRC <1% of current Monero txs are 4-in     

> __< k​ayabanerve:matrix.org >__ jberman has asked I submit the optimized Field25519 impact which impacts verification time via a patch (not waiting for upstream to merge) and to get numbers accurate to the final target. I'll try to do so shortly after this.     

> __< k​ayabanerve:matrix.org >__ TL;DR Numbers are still variable and may change by ~20% by tomorrow on this point alone.     

> __< k​ayabanerve:matrix.org >__ jeffro256: 3 isn't a power of 2, and we can't do 2 in unless in < out :C     

> __< j​effro256:monero.social >__ fair point     

> __< ArticMine >__ So if I understand correcty 4in is the minimu?     

> __< k​ayabanerve:matrix.org >__ A 3-in is effectively entirely as costly as 4-in, on proof size and verification time. It saves the 32 bytes in the key image store, and ~1kb for the signatures + the commitments we can't assume are zero (but still pay the verification cost on).     

> __< k​ayabanerve:matrix.org >__ Long-term goal: less input TXs.     

> __< k​ayabanerve:matrix.org >__ IMO, for now: TX weight linearly respective to size and time, potentially penalizing larger TXs in a way encouraging smaller TXs instead.     

> __< k​ayabanerve:matrix.org >__ Instead of forcing people to write better code, we can have them save money if they write better code.     

> __< o​frnxmr:monero.social >__ at the cost of my ssd storage .. and bandwidth     

> __< j​effro256:monero.social >__ ArticMine: 4 is the minimum value we should set the *maximum limit* rule to, not the minimum input count. In other words, we should never add a rule which limits the input count to less than 4. But txs with <4 ins can exist     

> __< j​effro256:monero.social >__ And will exist, probably continuing to be the majority of txs like it is today     

> __< o​frnxmr:monero.social >__ As a miner, i earn more if i store less data = logic is backwords     

> __< o​frnxmr:monero.social >__ Backwards*     

> __< j​effro256:monero.social >__ In other other words, 4-in transactions need to be able to exist     

> __< ArticMine >__ I understand that tx with less than 4 can exist but they will have the same or similar weight as 4 in. If so then I must change the scaling paramenters     

> __< o​frnxmr:monero.social >__ Penalizing large in with higher fees means miners are incentivized to prefer large in txs     

> __< j​effro256:monero.social >__ No they should not have a similar weight as a 4-in IMO     

> __< j​berman:monero.social >__ I think easiest to justify / achieve consensus on would be: linear increasing weights, clamping to higher powers of 2 to incentivize powers of 2     

> __< k​ayabanerve:matrix.org >__ (Though Monero TXs are so cheap right now that may not matter 😅)     

> __< k​ayabanerve:matrix.org >__ ofrnxmr: that requires users make large input TXs for miners to have that option, and users won't be incentivized to.     

> __< j​effro256:monero.social >__ I agree with jberman. Now the question is: linear with respect to the input count itself, or linear with respect to the proof size of that many inputs?     

> __< k​ayabanerve:matrix.org >__ I don't think miners are a relevant part of the puzzle here.     

> __< k​ayabanerve:matrix.org >__ If there's a congested mempool, the existing fee market handles all.     

> __< o​frnxmr:monero.social >__ not if i make my own block templates ..     

> __< r​ucknium:monero.social >__ IMHO, it could be a good idea to pin tx fee levels to network hashpower. Hashpower follows the purchasing power of 1 XMR closely. Or, closely enough.     

> __< ArticMine >__ What matter is the weight of the bulk of the transactions currently 2in or less? So are the proposed FCMP++ 2in weights going to hold     

> __< o​frnxmr:monero.social >__ thats pinning to usd     

> __< k​ayabanerve:matrix.org >__ I would say linear to TX size and linear to inputs. Two separate terms in the equation jeffro256     

> __< k​ayabanerve:matrix.org >__ Model space and time     

> __< r​ucknium:monero.social >__ That could end all the discussions of "what if XMR purchasing power increases suddenly" for good.     

> __< k​ayabanerve:matrix.org >__ ofrnxmr: Even with your own block template, you can't make higher paying TXs appear out of thin air.     

> __< r​ucknium:monero.social >__ It's pinning to purchasing power of a CPU.     

> __< j​effro256:monero.social >__ kayabanerve:  Not necessarily. What we want to avoid is people adding transactions into the mempool which miners aren't incentivized to mine so they stick around. This can happen when the penalty free zone is saturated     

> __< a​rticmine:monero.social >__ Correct     

> __< r​ucknium:monero.social >__ and/or a kilowatt hour of electricity.     

> __< o​frnxmr:monero.social >__ Yes you can. Mine empty blocks until ppl raise their fees     

> __< r​ucknium:monero.social >__ You need a mining cartel to do that     

> __< r​ucknium:monero.social >__ Let's continue the agenda     

> __< ArticMine >__ We need to use node relay to block not economic transactions     

> __< r​ucknium:monero.social >__ See "Monopoly without a monopolist" paper     

> __< k​ayabanerve:matrix.org >__ ofrnxmr: that attack always exists     

> __< r​ucknium:monero.social >__ 7)  [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< o​frnxmr:monero.social >__ i think would be nice to have kayabas tx creation speedups in for stressnet     

> __< ArticMine >__ I have to attend another meeting     

> __< j​berman:monero.social >__ re: alpha stressnet, just 1 more blocker PR needed     

> __< o​frnxmr:monero.social >__ ty artic     

> __< r​ucknium:monero.social >__ ofrnxmr: Did you try much with the Monero Research Computing Cluster?     

> __< j​berman:monero.social >__ I don't think it needs to be a blocker, we can merge it in after launch/people can run it if they want even without a merge     

> __< o​frnxmr:monero.social >__ No, i synced up a couple nodes but havent started spamming from there yet     

> __< r​ucknium:monero.social >__ A very "tidy" setup would be to have a docker container or something with a node, a monero-wllet-rpc, the spam script, and a unique wlalet in each.     

> __< j​effro256:monero.social >__ I took a deeper dive into 0xfffc 's 9494 PR, and I'm satisified with it. I'm currently reviewing PR #81 in seraphis-migration. I think we could start planning a launch date     

> __< k​ayabanerve:matrix.org >__ The Monero FCMP++ branch has a PR from me moving from j-bermam/fcmp-plus-plus (a fork of kayabaNerve/fcmp-plus-plus) to monero-oxide/monero-oxide#fcmp++ which now hosts the FCMP++ libraries.     

> __< r​ucknium:monero.social >__ Junior in MRC has plenty of storage for lots of stressnet nodes, but Senior doesn't. Maybe some storage could be moved there.     

> __< j​berman:monero.social >__ I would propose launch date 7 days after merging #81     

> __< o​frnxmr:monero.social >__ Except w/o docker     

> __< j​effro256:monero.social >__ This could be done, but IDK if deterministic builds for GUIX and Rust are ready yet, so users would have to just trust a single person     

> __< k​ayabanerve:matrix.org >__ The monero-oxide/monero-oxide#fcmp++ code has most of the optimizations I've made recently. I also proposed a faster verifier, but it's on a branch and will not be included as it'd need to be audited (or at least heavily reviewed) to be merged.     

> __< r​ucknium:monero.social >__ I don't like docker either. Any way to do dockerless docker? :P     

> __< k​ayabanerve:matrix.org >__ It's 15-20% faster for 128-input TXs though.     

> __< k​ayabanerve:matrix.org >__ (8% for 64, and rather negligible after)     

> __< r​ucknium:monero.social >__ Last time on stressnet the spamming monero-wallet-rpc instances could not stay connected to nodes easily. So I did one node per rpc instance IIRC.     

> __< k​ayabanerve:matrix.org >__ monero-oxide/monero-oxide#fcmp++ does target Rust 1.69 for the relevant libraries, as we need for cross-compilation and Guix. cc tobtoht     

> __< o​frnxmr:monero.social >__ Thats due to the 100mb txpool     

> __< o​frnxmr:monero.social >__ Restricted-rpc works     

> __< k​ayabanerve:matrix.org >__ I'll also try to submit the patch for the Field25519 arithmetic tonight for jberman's benches, but I see no reason we can't also include it in stressnet.     

> __< r​ucknium:monero.social >__ jberman 's proposal "I would propose launch date 7 days after merging #81" sounds fine to me.     

> __< j​effro256:monero.social >__ I plan to hop back on reviewing #81 when I'm done with reviewing the peer dedup PR     

> __< r​ucknium:monero.social >__ jeffro256: I removed the spy nodes agenda item for this meeting. Should it be put back in, or can it be skipped today?     

> __< r​ucknium:monero.social >__ I noticed your new comments on the peer subnet deduplication PR     

> __< o​frnxmr:monero.social >__ Just the one thinf about dns blocklist     

> __< r​ucknium:monero.social >__ Any more discussion on alpha stressnet planning?     

> __< o​frnxmr:monero.social >__ Consensus to update blocklist to remove a couple old ones and add active subnet(s)?     

> __< j​berman:monero.social >__ "Any more discussion on alpha stressnet planning?" -> nothing from me     

> __< r​ucknium:monero.social >__ ofrnxmr: This one? https://github.com/monero-project/meta/issues/1242     

> __< o​frnxmr:monero.social >__ Yeah     

> __< j​effro256:monero.social >__ It can be skipped IMO     

> __< r​ucknium:monero.social >__ Maybe more thumbs can be upped on https://github.com/monero-project/meta/issues/1242     

> __< r​ucknium:monero.social >__ 8) CCS proposal: [kayabaNerve Finality Layer Book](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/604).     

> __< r​ucknium:monero.social >__ What are the advantages and disadvantages of a finality layer compared to rolling N-block (e.g. 10) checkpoints, where nodes refuse to re-org to a new alt-chain deeper than N blocks?     

> __< k​ayabanerve:matrix.org >__ The fact one can have formally-proven safety in an asynchronous model and one immediately fails even in the synchronous model?     

> __< a​tomfried:matrix.org >__ I still dont realy know a good, decetnralized, fair and secure way of selecting the validators.     

> __< k​ayabanerve:matrix.org >__ If Qubic achieves a 10-block reorg, which IIRC they've demonstrated multiple 9-block reorgs, suggesting they could, it'd immediately netsplit off all new nodes.     

> __< k​ayabanerve:matrix.org >__ (any nodes not online at the time of reorg)     

> __< r​ucknium:monero.social >__ Are you aware of any scholarship on N-block rolling checkpoints?     

> __< r​ucknium:monero.social >__ An easy fix is to have deterministic tiebreaking at N block re-orgs.     

> __< r​ucknium:monero.social >__ Deterministic tiebreaking has been studied in many papers.     

> __< k​ayabanerve:matrix.org >__ Until the 'didn't reorg' group achieved a chain with more work, if they ever did, but then the nodes which followed Qubic's chain won't reorganize back.     

> __< r​ucknium:monero.social >__ (Instead of first-seen rules)     

> __< o​frnxmr:monero.social >__ theyd have to maintain the longest chain, else the offline nodes will eventually be reorged onto the "honest" chain     

> __< k​ayabanerve:matrix.org >__ We're at a point where we have to replace 10 with 20, if we were to discuss not reorganizing past N IMO.     

> __< k​ayabanerve:matrix.org >__ (cc Rucknium for actual statistics on this)     

> __< k​ayabanerve:matrix.org >__ And all of this, IMO, implies PoW has been shown to be insufficient for the Monero network as it stands.     

> __< k​ayabanerve:matrix.org >__ While there are proposed improvements, I'm not convinced they do any better than marginal.     

> __< b​oog900:monero.social >__ to get back to the real chain they would need to do a reorg bigger than 10 blocks, right?     

> __< r​ucknium:monero.social >__ Are you referring to my analysis here? https://github.com/monero-project/research-lab/issues/102#issuecomment-2402750881     

> __< k​ayabanerve:matrix.org >__ A proper finality layer would also presumably remove the 10-block lock.     

> __< tevador >__ A deterministic tie break won't fix chain splits. The attacker will instead publish an 11-block reorg + 1 block on top of the honest chain simultaneously.     

> __< b​oog900:monero.social >__ oh the offline nodes     

> __< k​ayabanerve:matrix.org >__ ofrnxmr: No because they won't reorg off Qubic's due to the same max reorg rule.     

> __< o​frnxmr:monero.social >__ Depends on how long the lead was maintained     

> __< k​ayabanerve:matrix.org >__ Rucknium: Probably. The question would be since Qubic exists, with the attacks they've demonstrated, what reorg is now sufficiently improbable?     

> __< k​ayabanerve:matrix.org >__ And is there one with their proximity to 51%, even if it's just occasionally ~30-40% over a 8 hour period?     

> __< r​ucknium:monero.social >__ tevador: So attack the honest chain and attacking chain simultaneously? Yes, I suppose that could work in the attacker's favor to cause a netsplit.     

> __< k​ayabanerve:matrix.org >__ Do we wish to move to a (8 * 60 / 2)-block lock, recommended confirmations, and max reorg depth?     

> __< tevador >__ Anything with a max reorg depth is not PoW anymore.     

> __< b​awdyanarchist:matrix.org >__ kayabanerve: How much of a factor do you think, is the inclusion of time as an independent variable in consensus, a major factor in a finality layer? Dont most PoS systems use time slots?     

> __< o​frnxmr:monero.social >__ isnt the main reason 10+ block reorgs are an issue, due to invalidating decoys     

> __< k​ayabanerve:matrix.org >__ A proper finality layer solves this. A finality layer can replace the 10-block lock. The risk of a finality layer is the finality layer stalling, performing censorship, though that'd enable a social slash, or equivocating. I believe all of those can be made less problematic than PoW today.     

> __< r​ucknium:monero.social >__ According to what I'm reading by Roughgarden, the less synchronous you become, the more permissioned the validation must be.     

> __< c​haser:monero.social >__ tevador: indeed     

> __< k​ayabanerve:matrix.org >__ *much* less     

> __< DataHoarder >__ 21:00:11 <k​ayabanerve:matrix.org> If Qubic achieves a 10-block reorg, which IIRC they've demonstrated multiple 9-block reorgs, suggesting they could, it'd immediately netsplit off all new nodes.     

> __< DataHoarder >__ They have been able to get +14 ahead     

> __< k​ayabanerve:matrix.org >__ And the amount of discussions DNS checkpoints have gotten, which would be centralized, solely justify my position IMO.     

> __< DataHoarder >__ they released when monero got 9 deep     

> __< o​frnxmr:monero.social >__ tevador we already (effectively) have a max reorg depth of a few thousand blocks     

> __< k​ayabanerve:matrix.org >__ BawdyAnarchist: My proposal is asynchronous BFT which doesn't have bounds on time.     

> __< g​onbat.zano:zano.org >__ >  they've demonstrated multiple 9-block reorgs     

> __< g​onbat.zano:zano.org >__ kayabanerve They also had the capacity to do 16 blocks and decided not to, according to DataHoarder's research     

> __< tevador >__ ofrnxmr: technicality     

> __< r​ucknium:monero.social >__ kayabanerve: What do you want to accomplish with this agenda item? General countermeasures to a malicious mining pool is next.     

> __< k​ayabanerve:matrix.org >__ Can I have my CCS merged and can the community agree PoW isn't a fundamental tenant of Monero, security and decentralization is? 😅     

> __< o​frnxmr:monero.social >__ Pow is a fundamental tenant of monero IMO     

> __< r​ucknium:monero.social >__ Can we not use comma splices? :P     

> __< c​haser:monero.social >__ kayabanerve: "A proper finality layer solves this..." comment: the finality layer would offer a strong economic incentive against it being stalled/being coopted/censorious. it's not a high-probability event. equivocations (slashing stake for provable misbehavior) can be quasi-automated within the consensus rules.     

> __< tevador >__ 1) CCS merged - maybe, 2) There will likely be stiff opposition to PoS.     

> __< r​ucknium:monero.social >__ At least consensus on no-comma-splices.     

> __< k​ayabanerve:matrix.org >__ We can't say "we declare pos" and move to a finality layer over night. I want the idea to be fairly treated. I believe there's more than sufficient justification to move forward with research and a proposal.     

> __< tevador >__ I think there is a case for the CCS to be merged. If people donate the required amount, the research should be done.     

> __< k​ayabanerve:matrix.org >__ chaser It solves it within its bounds. The only solution a max reorg depth is is within the bound 'no miner can attempt more than a 10 block reorg'.     

> __< k​ayabanerve:matrix.org >__ That's such a disastrous bound, which has already failed, any solution premised on it is a failure.     

> __< k​ayabanerve:matrix.org >__ But you're right a finality layer is only a solution to a bounded problem (n = 3f + 1).     

> __< r​ucknium:monero.social >__ Finality layer doesn't solve short-chain selfish mining, does it? And it doesn't solve empty block attacks, but you hinted it might. Or how would it?     

> __< k​ayabanerve:matrix.org >__ Sorry. In a fully synchronous network, you can assume no nodes are offline and all nodes receive the honest blockchain before any alt is published.     

> __< r​ucknium:monero.social >__ Is that an amendment to your statement about N-block rolling checkpoints?     

> __< k​ayabanerve:matrix.org >__ It can if it finalizes the honest chain before the selfishly mined chain is publish, preventing re-org'ing to itm     

> __< k​ayabanerve:matrix.org >__ It doesn't solve a miner producinga empty blocks.     

> __< c​haser:monero.social >__ kayabanerve: to clarify, I added the comment because I think the majority of the opposition to the finality layer is rooted in people not having an understanding of proof-of-stake consensus mechanics and nomenclature     

> __< k​ayabanerve:matrix.org >__ A sufficiently low latency finality layer, on an optimal network, would mean 1% of hash power earns 1% of blocks (again, in an ideal world).     

> __< tevador >__ Depending on the speed of finalization, selfish mining might still be possible.     

> __< r​ucknium:monero.social >__ Then you need it explain it. Lots of terms have not been explained. I mean, I would prefer if terms were explained.     

> __< r​ucknium:monero.social >__ Or offer a reference, which kayabanerve  declined to provide when I requested :P     

> __< k​ayabanerve:matrix.org >__ Rucknium: Yes. A N-block rolling checkpoint works if you have no offline nodes and propagation is instant.     

> __< k​ayabanerve:matrix.org >__ Who here has 100% uptime on their node?     

> __< k​ayabanerve:matrix.org >__ Does everyone?     

> __< s​yntheticbird:monero.social >__ I do     

> __< s​yntheticbird:monero.social >__ I have triple digit uptime it's not a myth guy     

> __< k​ayabanerve:matrix.org >__ Sorry, what reference did I decline to provide?     

> __< p​rivacyx:monero.social >__ I 100% uptime     

> __< k​ayabanerve:matrix.org >__ Are you talking about the reference of my proposed book? I believe I offered to provide that as soon as my CCS is merged and I actually do the work :p     

> __< r​ucknium:monero.social >__ You can check empirical update in the last month of many nodes here: https://xmr.ditatompel.com/remote-nodes     

> __< b​oog900:monero.social >__ the propagation being instant is the bigger problem than uptime     

> __< k​ayabanerve:matrix.org >__ I agree there's confusion and a lack of understanding. That's why my CCS exists.     

> __< c​haser:monero.social >__ Rucknium: a finality layer could serve as a foundation for force-inclusion of transactions in blocks, which would actually prevent empty-block attacks.     

> __< b​oog900:monero.social >__ I can live with offline nodes potentially following the bad chain although its not something I like     

> __< k​ayabanerve:matrix.org >__ Also because I'm tired of explaining things in lounge for the umpteenth time.     

> __< b​oog900:monero.social >__ I can't live with nodes online being split be a reorg right at the boundary     

> __< b​oog900:monero.social >__ by*     

> __< r​ucknium:monero.social >__ I think a high-hashpower attacker can even get around the force-inclusion of txs by broadcasting high-fee txs and mining them itself.     

> __< k​ayabanerve:matrix.org >__ Hence why a comment I left is in order to prevent censorship, we have to burn TX fees (at least partially) 😅     

> __< c​haser:monero.social >__ Rucknium: also, a finality layer, where a block is finalized, I believe treats any length of reorgs the same, short or long.     

> __< k​ayabanerve:matrix.org >__ This is something I've already noted.     

> __< o​frnxmr:monero.social >__ wouldnt this just be offset by the block reward     

> __< c​haser:monero.social >__ Rucknium, kayabanerve: that's true.     

> __< o​frnxmr:monero.social >__ We already "burn" some block reward     

> __< k​ayabanerve:matrix.org >__ According to ArticMine, the penalty already is an effective burn.     

> __< r​ucknium:monero.social >__ Aha, here is what I was referring to: https://libera.monerologs.net/monero-research-lounge/20250813#c557210     

> __< r​ucknium:monero.social >__ > kayabanerve: Any recommended introductory texts on blockchain finality layers?     

> __< r​ucknium:monero.social >__ More comments on this item?     

> __< c​haser:monero.social >__ burning more of the fees in exchange for making empty-block attacks less feasible sounds like a good trade.     

> __< r​ucknium:monero.social >__ AFAIK, fee burning would reduce the security budget, so there is a tradeoff.     

> __< b​oog900:monero.social >__ I'm not sure I agree, you can still fill blocks up quite high without hitting the penalty. With FCMP it will go up even more.     

> __< b​oog900:monero.social >__ just increase fees to cover the drop in proportion going to the miner?     

> __< r​ucknium:monero.social >__ boog900: Do you have some elasticity estimates 👀     

> __< b​oog900:monero.social >__ I think fees could probably do with increasing anyway     

> __< r​ucknium:monero.social >__ The elasticity of tx volume with respect to tx fee     

> __< r​ucknium:monero.social >__ 9) PoW mining pool centralization. [Monero Consensus Status](https://moneroconsensus.info/). [Bolstering PoW to be Resistant to 51% Attacks, Censorship, Selfish Mining, and Rented Hashpower](https://github.com/monero-project/research-lab/issues/136). [Mining protocol changes to combat pool centralization](https://github.com/monero-project/research-lab/issues/98).     

> __< tevador >__ Raising tx fees is the best way to disincentivize empty blocks.     

> __< tevador >__ My contribution to this agenda item: https://github.com/monero-project/research-lab/issues/144     

> __< r​ucknium:monero.social >__ We have a new. Right. New issue from tevador on Publish or Perish     

> __< tevador >__ Based on my research, this would be the most efficient PoW-only solution.     

> __< r​ucknium:monero.social >__ A later paper by the same authors suggested PoP wasn't very good.     

> __< r​ucknium:monero.social >__ One of the papers you cite, "Laying Down the Common Metrics"     

> __< tevador >__ My referenced paper [6] measured the performance of PoP and it performed the best out of all soft forking solutions.     

> __< r​ucknium:monero.social >__ The profitablility threshold for a selfish miner, according to that later paper, is .25     

> __< r​ucknium:monero.social >__ Table II     

> __< r​ucknium:monero.social >__ Zhang & Preneel (2019) "Lay down the common metrics: Evaluating proof-of-work consensus protocols’ security." https://doi.org/10.1109/SP.2019.00086     

> __< tevador >__ Profitability threshold is only part of the story.     

> __< r​ucknium:monero.social >__ I looked closely at proportional reward splitting. It does a lot better than the others, but requires a hard fork and faster PoW verification, as you note.     

> __< b​awdyanarchist:matrix.org >__ Rucknium: Relative performance depended alot on assumed γ value (percent of honest HP mining on the attacker's chain). PoP outperformed NC up to 0.4     

> __< tevador >__ See Fig. 2, PoP performs well. Outperformed only by NC with gamma = 0, which is unrealistic.     

> __< r​ucknium:monero.social >__ You mean when gamma is zero, Nakamoto Consensus outperforms PoP up to 0.4, right?     

> __< tevador >__ ^ Correct.     

> __< tevador >__ But gamma is never zero.     

> __< r​ucknium:monero.social >__ Well, I have a paper that says selfish mining can be defeated up to selfish mining hashpower = 0.5     

> __< r​ucknium:monero.social >__ Not sure how reliable this paper is     

> __< r​ucknium:monero.social >__ Ghoreishi & Meybodi (2024) "New intelligent defense systems to reduce the risks of Selfish Mining and Double-Spending attacks using Learning Automata" https://arxiv.org/abs/2307.00529     

> __< r​ucknium:monero.social >__ Also doesn't require a hard fork. Only change in miner strategy.     

> __< r​ucknium:monero.social >__ Let me post my short thoughts:     

> __< r​ucknium:monero.social >__ Ghoreishi & Meybodi (2024) "New intelligent defense systems to reduce the risks of Selfish Mining and Double-Spending attacks using Learning Automata" https://arxiv.org/abs/2307.00529 seems to suggest an automatic way for honest miners to build on honest blocks when a selfish miner is active. It says that it can completely eliminate the selfish miner's profit advantage when the se<clipped message     

> __< r​ucknium:monero.social >__ lfish miner has less than 50% of hashpower (this claim makes me skeptical). Part of the procedure uses block time stamps, which _we_ assume are actually spoofable, within some limits. I don't know how well their system works without honest time stamps. They cite a paper from 2014 about non-spoofable block time stamps, but I haven't looked at that paper.     

> __< tevador >__ I'll read it, but I'm skeptical.     

> __< tevador >__ I read that 2014 paper.     

> __< r​ucknium:monero.social >__ The non-spoofable timestamp paper is.. Right [4] One Weird Trick to Stop Selfish Miners: Fresh Bitcoins, A Solution for the Honest Miner. https://eprint.iacr.org/2014/007     

> __< tevador >__ It's very very impractical.     

> __< tevador >__ It needs a trusted authority which generates unspoofable timestamps.     

> __< tevador >__ PoP, on the other hand, only needs to measure the relative arrival of competing blocks, so it has zero requiremnts on clock synchronization or timestamp accuracy.     

> __< r​ucknium:monero.social >__ I'll read the PoP paper.     

> __< b​awdyanarchist:matrix.org >__ I'm working on a nodejs simulation to compare various honest/selfish strategies. Can add an arbitrary number of pools, set their strategies and HP, and also attempts to simulate probablistic network latency with tunable input constants.     

> __< tevador >__ ^ cool, I need to simulate some proposals     

> __< tevador >__ It would be nice to double check the numbers from the PoP paper.     

> __< b​awdyanarchist:matrix.org >__ I think I'm about 80% of the way to an alpha release. Hoping to post a first rev before next week.     

> __< r​ucknium:monero.social >__ BawdyAnarchist: Try to look at the Markov Decision Process (MDP) methodology of "Lay down the common metrics" and Aumayr et al. (2025) "Optimal Reward Allocation via Proportional Splitting" https://arxiv.org/abs/2503.10185     

> __< r​ucknium:monero.social >__ It seems like MDP can require lots of CPU and RAM, but MRL has that if needed.     

> __< r​ucknium:monero.social >__ In addition to the papers already mentioned I read (half of) Lewis-Pye & Roughgarden (2024) "Permissionless Consensus" https://arxiv.org/abs/2304.14701     

> __< r​ucknium:monero.social >__ Mostly these are impossibility results at a high level. I am also getting some terms precisely defined.     

> __< r​ucknium:monero.social >__ tevador: Is a higher rate of hashpower sampling completely infeasible? I wonder how much CPU time will be spent on a typical block's FCMP verification compared to one RandomX PoW     

> __< r​ucknium:monero.social >__ Aumayr et al. (2025) "Optimal Reward Allocation via Proportional Splitting" is supposed to get the profitability threshold to 0.38, but it does require more PoW hashes per block.     

> __< r​ucknium:monero.social >__ BawdyAnarchist: AFAIK, the papers with MDP methodology did not publish their code. Maybe try to email the authors. Maybe there is off-the-shelf code for MDP that can be adopted to the scenarios.     

> __< b​awdyanarchist:matrix.org >__ I'll see what I can find.     

> __< r​ucknium:monero.social >__ More comments on this agenda item?     

> __< tevador >__ My proposal has a block time of 60 s, so it already doubles the PoW cost.     

> __< r​ucknium:monero.social >__ The second one, "Hard-forking proposal"     

> __< tevador >__ Yes.     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< tevador >__ PoW is more sensitive to performance than tx verificaion. For example, SPV-style wallets only verify PoW.     

> __< tevador >__ So I don't think PoW cost of >1 second per block would be great. That would become 10 seconds on a raspberry pi.     

> __< a​ck-j:matrix.org >__ I have a concern with the proposed finality layer or POS switch largely surrounding coin distribution. Monero’s emission curve was extremely aggressive and IMHO a blemish on the protocol as it favored the few early adopters too greatly. This combined with early mining software being sabotaged to reduce efficiency leads one to wonder what the distribution of coins actually looks <clipped message>     

> __< a​ck-j:matrix.org >__ like. There’s nothing we can do about that now but switching to POS knowing this seems insane to me. I currently support tevadors proposals to stay with POW, increase fees and research creative solutions to selfish mining.      

> __< a​ck-j:matrix.org >__ I support kayabanerve CCS proposal but I’d like these concerns addressed in the book.     

> __< moneromooo >__ FWIW it is an apparently common misconception. The bad miner only caused an skewed distribution vs hash rate for the first few weeks (assuming the CN people mined it). No extra monero was generated. So AFAIK the high bound on this is very small by now.     

> __< moneromooo >__ So using it to claim PoS would be insane is ill informed at best. There are other much more persuasive arguments to be made.     

> __< nioc >__ and 11 years since that happened, plenty of time for them to sell     

> __< nioc >__ sorry, didn't realize the channel I was in      

> __< a​ck-j:matrix.org >__ Thanks moo, good to know. I wasn’t around back then and have only heard stories.     

> __< a​ck-j:matrix.org >__ My first point still stands     

> __< r​ucknium:monero.social >__ The distribution of the coins being completely unknown _is_ a security worry, IMHO. AFAIK, the only thing that can really be known is that X coins haven't been spent since RingCT was introduced ( jeffro256  produced the numbers on that IIRC) and any of the few public valid reserve proofs that exist. Even public view keys aren't very reliable because they don't show outbound spends.     

> __< r​ucknium:monero.social >__ A transparent blockchain would give hints about who owns certain piles of coins.     

> __< j​effro256:monero.social >__ ~9% of funds in pre-RingCT outputs have not yet been spent     

> __< o​frnxmr:monero.social >__ So like 70% of the supply? :P     

> __< j​effro256:monero.social >__ The remaining enotes have been spent, but that doesn't necessarily mean that they've changed hands. They could have just been churned into RingCT enotes owned by the same people     

> __< o​frnxmr:monero.social >__ Do you know how many xmr = 9% of pre-ringct?     

> __< r​ucknium:monero.social >__ For a point of comparison (BTC and BCH spent outputs 2017 - 2022), see my analysis: https://rucknium.me/posts/pre-fork-btc-bch-spending/     

> __< d​gently:catgirl.cloud >__ People that wanted increased privacy did indeed send to themselves     



# Action History
- Created by: Rucknium | 2025-08-26T22:23:08+00:00
- Closed at: 2025-09-04T21:50:49+00:00
