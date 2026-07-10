---
title: Monero Research Lab Meeting - Wed 3 Jun 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1399
author: j-berman
assignees: []
labels: []
created_at: '2026-06-02T16:51:56+00:00'
updated_at: '2026-07-09T19:40:45+00:00'
type: issue
status: closed
closed_at: '2026-07-09T19:40:45+00:00'
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

## Rucknium | 2026-06-08T20:26:47+00:00
Logs


> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1393     

> __< rucknium >__ 1. Greetings     

> __< tevador >__ Hi     

> __< jberman >__ waves     

> __< boog900 >__ Hi     > __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1399     

> __< rucknium >__ 1. Greetings.     

> __< tevador >__ Hi     

> __< jberman >__ waves     

> __< vtnerd >__ hi     

> __< articmine >__ Hi     

> __< sgp_ >__ Hello     

> __< boog900 >__ hi     

> __< jpk68:matrix.org >__ Hello     

> __< rbrunner >__ Hello     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __*__ br-m <jbabb:cypherstack.com> waves     

> __< rbrunner >__ Polyseed support for the Wallet RPC server, the last bigger chunk     

> __< vtnerd >__ me: posted zmq-pub code that leverages cbor instead of msgpack after feedback and perf testing     

> __< syntheticbird >__ Hi     

> __< jberman >__ me: completed FCMP++ audit remediation tasks, chasing down windows GUI crashing on stressnet, PR review     

> __< vtnerd >__ and working on ssl stuff! almost forgot about that. Im going to address selstastuff and then start a pr to beta-stressnet     

> __< rucknium >__ 3. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686)     

> __< tevador >__ No notable updates from me, I'm working on Jamtis Appendix B (interactive payment protocol).     

> __< sgp_ >__ I’ll shill episode 2 of plaintext on divisors: https://youtu.be/-Ae0AUBG2Mg     

> __< UkoeHB >__ Hi, will be reviewing the jamtis-pq draft, maybe start implementing it     

> __< rucknium >__ [waiting on someone to finish typing on Matrix side]     

> __< jberman >__ (nothing from me sorry)     

> __< rucknium >__ sgp may have something to say. Or his elbow is on the keyboard.     

> __< rucknium >__ 4. Monero-PSK (https://gist.github.com/tevador/9169235b3c0c97e735f58a8c2ba92502)     

> __< tevador >__ I'm proposing to skip this agenda item unless spirobel is here.     

> __< rucknium >__ Ok. Any other comments on PSK?     

> __< jberman >__ I think spirobel just needs to clarify his ideas on that front to move that forward     

> __< rucknium >__ 5. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/)     

> __< jberman >__ v2.0 seems to be going smooth for now. Spamming hasn't kicked into gear yet     

> __< rucknium >__ My monitors for the new stressnet are up and running: https://stressnetnode1.redteam.cash/  https://stressnetnode2.redteam.cash/ https://stressnetconsensus1.redteam.cash/  https://stressnetconsensus2.redteam.cash/     

> __< jberman >__ I'm working on a windows GUI binary crash at the moment     

> __< rbrunner >__ Just curious, can you use a proper debugger there now?     

> __< jberman >__ no, I don't have a good dev env for windows     

> __< jberman >__ but I think I'm close to getting at the cause of the issue     

> __< redsh4de:matrix.org >__ rbrunner: you can capture a crash dump with prodcump and run it through WinDbg. used that to produce the crash report for the issue     

> __< brandon:cypherstack.com >__ hola     

> __< rbrunner >__ Ah, I see. That makes sense.     

> __< rucknium >__ More on stressnet?     

> __< rucknium >__ 6. FCMP++ integration audit (https://github.com/seraphis-migration/monero/issues/294)     

> __< jberman >__ Reminder context: Trail of Bits completed phase 1, minus a task item. We're working internally on managing that task item (would prefer to kick discussion of this til next week)      

> __< jberman >__ I also haven't had a good chance to deeply review Cypher Stack's audit (much appreciated for that work, thank you guys again)     

> __< jberman >__ But what has been reviewed so far has all "passed" so to speak. Neither ToB nor Cypherstack found issues beyond informational so far     

> __< rucknium >__ Zcash just patched a critical counterfeiting bug via hard fork: https://forum.zcashcommunity.com/t/orchard-vulnerability-successfully-remediated/55976#p-248390-technical-details-5  . It looks like it was a problem with a code loop, not a problem with the mathematical theory. That shows how important the code integration audit is :)     

> __< jberman >__ By next week, I'll try to have all code prepped for phase 2 as well so that can move forward     

> __< rucknium >__ Zcash has a safety net. They have a turnstile that prevents counterfeiting supply from increasing the total supply in the transparent pool. Monero does not have that. Thanks to selsta for pointing out the Zcash developments.     

> __< jberman >__ FWIW the equivalent bug would actually not be in the scope of this code integration audit, and it would still be something on the Rust side in kayabanerve:matrix.org 's FCMP++ lib. And that side is getting (and has gotten) audited rigorously     

> __< brandon:cypherstack.com >__ uhm, i'm not sure if i would say our implementation audit at cypher stack is "passing"     

> __< brandon:cypherstack.com >__ we raised an issue about the view-all key      

> __< brandon:cypherstack.com >__ i'm not sure if this is the best time to bring it up     

> __< brandon:cypherstack.com >__ but we are concerned for a few reasons     

> __< brandon:cypherstack.com >__ namely, the view-all key advertised in the CARROT spec is not a view-all key. it's an opt-in view key     

> __< rucknium >__ brandon:cypherstack.com: Sure. Go ahead and bring it up.     

> __< jberman >__ That was unrelated to phase 1 of the integration audit     

> __< fireine:matrix.org >__ brandon:cypherstack.com: Indeed, I wouldn't have lobbied for this if it was trivial.     

> __< brandon:cypherstack.com >__ so, for the folks listening, there is a way to construct a transaction to a wallet, which you've given the view key access to an auditor, but for which the auditor does not see the incoming transaction     

> __< brandon:cypherstack.com >__ this is similar to sending money to a wallet the auditor does not know about     

> __< brandon:cypherstack.com >__ however, it is distinct     

> __< rucknium >__ Maybe I am not fully understanding, but I find this ironic because some community members were worried that the Carrot view key would give "viewers" too much information. Now, is this new finding a feature or a bug?     

> __< brandon:cypherstack.com >__ an auditor with your view key may see some outgoing transactions to yourself, but not incoming transactions, and conclude you have a negative balance     

> __< freeman:cypherstack.com >__ And I think it can do things that just sending money to a new wallet cannot      

> __< brandon:cypherstack.com >__ i view this as a bug, unconditionally, in the sense that the key was advertised as a view-all key, but it is not.     

> __< fireine:matrix.org >__ brandon:cypherstack.com: bc it is.     

> __< fireine:matrix.org >__ the bug is buggy     

> __< freeman:cypherstack.com >__ Cuz it is lol     

> __< brandon:cypherstack.com >__ whether this practically impacts the security surface is a different question, because someone could always send money to a wallet the auditor doesn't know about     

> __< rbrunner >__ Otherwise everything runs perfectly ok with those "hide from view-all key holder" transactions?     

> __< rucknium >__ Is jeffro256:monero.social  present?     

> __< jpk68:matrix.org >__ Just throwing this out there: this could actually be nice to have, if it can work that way. None of the benefits with regards to hardware wallets/LWS seem to be removed, meanwhile it could also reduce FUD around mandatory key-sharing and whatnot     

> __< brandon:cypherstack.com >__ rbrunner: we haven't identified other broken parts yet, but we suspect that the same problem may just appear in multiple spots in carrot, soi it may be that there are many ways to do this     

> __< brandon:cypherstack.com >__ there is a simple fix which is to include a verifiable random function (VRF) proof that a certain piece of randomness was computed verifiably randomly, one for each transaction output     

> __< brandon:cypherstack.com >__ this would inflate FCMP transaction sizes, but would guarantee that view-all keys are view-all     

> __< brandon:cypherstack.com >__ jpk68:matrix.org: this is a common attitude, but here's my concern     

> __< rbrunner >__ Ok, but probably otherwise no other disadvantages? E.g. perfect restore from seed with such transactions received, right?     

> __< brandon:cypherstack.com >__ advertising view access but not actually having it may piss off exchanges who are trying to comply with kyc/aml, and this may lead to them deciding that monero is no longer compliance-friendly. which is incorrect, because the new view keys are less broken than the current view keys lol     

> __< kayabanerve:matrix.org >__ ... wouldn't that imply they sent to a different wallet, just one with overlapping other keys?     

> __< brandon:cypherstack.com >__ rbrunner: yeah we think so     

> __< kayabanerve:matrix.org >__ Like, same internal view key, different view key     

> __< rbrunner >__ Interesting.     

> __< brandon:cypherstack.com >__ no, it just means they didn't use ScalarDerive on something appropriately, instead picking a random number     

> __< brandon:cypherstack.com >__ same wallet keys     

> __< rbrunner >__ I agree that's a bug, not a feature. People who don't want view-all keys existing shall use the old 2-key wallet format ...     

> __< rbrunner >__ With or without holes     

> __< jbabb:cypherstack.com >__ jberman: as a sort of pedantic point of order, I want to underline this as well     

> __< jbabb:cypherstack.com >__ that what Freeman and surae are discussing is outside of the scope of the phase 1 integration audit except insofar as that Freeman found it while reviewing the underlying math while we were doing integration audit phase 1     

> __< fireine:matrix.org >__ rbrunner: which is what was stated.     

> __< fireine:matrix.org >__ perhaps you underestimate us lol     

> __< rbrunner >__ Was there a "Carrot the crypto and the math" audit that overlooked this?     

> __< kayabanerve:matrix.org >__ So if the sender creates an unscannable TX, but the opening is communicated out-of-band, then...?     

> __< rbrunner >__ By another party, I mean     

> __< jpk68:matrix.org >__ > <brandon:cypherstack.com> advertising view access but not actually having it may piss off exchanges who are trying to comply with kyc/aml, and this may lead to them deciding that monero is no longer compliance-friendly. which is incorrect, because the new view keys are less broken than the current view keys lol     

> __< jpk68:matrix.org >__ Understandable, and clearly the "marketing" around Carrot would need to change to match what it actually does. But does this imply that making Monero compliance-friendly (or at least perceived to be) is part of the objective here? I don't really agree with that, if it's the case     

> __< jpk68:matrix.org >__ To be clear, I am not against Carrot in any way     

> __< freeman:cypherstack.com >__ I did a CARROT audit in the past, but explicitly searching for vulnerabilities wasn't in-scope, so I don't feel too bad     

> __< freeman:cypherstack.com >__ Better late than never, amirite.....? 😅     

> __< kayabanerve:matrix.org >__ I'm still unclear on this scenario which causes the auditor to perceive a negative balance     

> __< brandon:cypherstack.com >__ kayabanerve:matrix.org: same thing happens. the interesting thing here is that with the fcmp view keys (as-is), auditors actually have a chance to collect evidence of wrongdoing (if your apparent balance goes negative, for example) so in a way, the detectability in the case that a malicious user is not being very carefu [... too long, see https://mrelay.p2pool.observer/e/3MnDwIkLX215UC1Q ]     

> __< brandon:cypherstack.com >__ kayabanerve:matrix.org: you have 100 xmr     

> __< brandon:cypherstack.com >__ you send 100 xmr less fees to yourself     

> __< jberman >__ The objective of the key isn't compliance friendliness. It's primarily to improve UX for cold/hot wallets, hw wallets, and multisig. So this wouldn't deviate from the primary goal imo      

> __< brandon:cypherstack.com >__ you randomly sample your own key data so that the transaction can't be scanned by someone with the view key     

> __< brandon:cypherstack.com >__ auditor sees you lose 100 xmr but not gain it again     

> __< rbrunner >__ jpk68: view-all keys do not only "please auditors". It has other solid uses. E.g. checking your paper wallet balance is still there without any danger     

> __< brandon:cypherstack.com >__ but you sent it to the same wallet it came from     

> __< kayabanerve:matrix.org >__ Sure. That isn't a bug in CARROT.     

> __< freeman:cypherstack.com >__ But I wonder if exactly this could be abused. I show an auditor "look, I have a negative balance, so I'm deserving of golden parachute funds!!" when actually I'm just hiding them (or something like this)     

> __< brandon:cypherstack.com >__ jberman: okay, if that's the case, then it's a matter of being careful to clarify this. this is not how monero view access has been advertised, for the most part, going back to the cryptonote whitepaper     

> __< rbrunner >__ I don't understand. Won't even the dumbest auditors see that there is no such thing like a negative balance with a cryptocurrency wallet?     

> __< rbrunner >__ If everything works correctly, that is     

> __< kayabanerve:matrix.org >__ The ability for senders to not send you an output via CARROT, but the ability for you to manually import non-CARROT outputs and spend them in ways which interact with CARROT, is bs understandably outside the scope of CARROT.     

> __< kayabanerve:matrix.org >__ If you have to manually import an opening, so does the auditor, is straightforward enough.     

> __< kayabanerve:matrix.org >__ manually importing an opening is effectively operating a distinct wallet though     

> __< brandon:cypherstack.com >__ if the view keys are just for convenience for wallets and UX, then the problem is auditors using the view keys for auditing instead of wallets using them for backend convenience (or whatever)     

> __< kayabanerve:matrix.org >__ There is no solution to prove your view key is for all of your wallets without linking to an identity     

> __< kayabanerve:matrix.org >__ Except the view keys do identify all coins that wallet received. Your proposal requires a wallet with distinct rules to receive the coins with.     

> __< brandon:cypherstack.com >__ kayabanerve:matrix.org: absolutely correct     

> __< brandon:cypherstack.com >__ the severity of this problem is ... debatable. there's nuance.     

> __< kayabanerve:matrix.org >__ You're then noting manual importing can fuck with CARROT accounting, sure, but the bug isn't with the view key itself.     

> __< brandon:cypherstack.com >__ kayabanerve:matrix.org: uhm no     

> __< jpk68:matrix.org >__ rbrunner: Of course, and that's part of my argument. In my opinion, a huge part of the tangible benefit provided by Carrot is the ability to have so-called "view-all" keys, allowing for safer balance-checking without the need for the spend keys. I am sure this possibility for hiding transactions will not be part of core wallet [... too long, see https://mrelay.p2pool.observer/e/xsrXwIkLR2tBT2ky ]     

> __< brandon:cypherstack.com >__ i can opt out of the vie accesss, and it's advertised as view all     

> __< brandon:cypherstack.com >__ not true with a VRF deciding random transaction data     

> __< kayabanerve:matrix.org >__ You can create a different wallet     

> __< jpk68:matrix.org >__ A concern of mine, though, is transparency of General Fund wallets with this, along with similar things     

> __< brandon:cypherstack.com >__ kayabanerve:matrix.org: no one ever claimed that creating a new wallet wouldn't evade auditors     

> __< kayabanerve:matrix.org >__ view-all for a wallet does not mean view all for every wallet under this entity     

> __< jpk68:matrix.org >__ Though it wouldn't be any worse than how it is currently     

> __< brandon:cypherstack.com >__ carrot claims that view-all is view-all, and it isn't     

> __< jbabb:cypherstack.com >__ where this may come in handy is to keep in mind downstream for applications like swaps etc that are built on shared wallets using view keys as one method of accounting     

> __< brandon:cypherstack.com >__ kayabanerve:matrix.org: view all also does not mean "optional"     

> __< brandon:cypherstack.com >__ jpk68:matrix.org: yeah, i don't think it is worse than the current state of things     

> __< jbabb:cypherstack.com >__ jbabb:cypherstack.com: just to be more aware of the ways malicious counterparties can fudge the books for shared wallets     

> __< brandon:cypherstack.com >__ but that's my knee jerk     

> __< kayabanerve:matrix.org >__ It is because you're proposing a non-carrot wallet and therefore a distinct wallet     

> __< brandon:cypherstack.com >__ kayabanerve:matrix.org: no i'm proposing an actor who is semi-honest can fail to satisfy the claimed properties     

> __< jpk68:matrix.org >__ How much would the fix impact scaling and transaction sizes?     

> __< kayabanerve:matrix.org >__ A CARROT view key omitting outputs to a non-CARROT wallet isn't a bug in CARROT     

> __< brandon:cypherstack.com >__ if the claimed properties are different, then claim teh correct properties     

> __< kayabanerve:matrix.org >__ Which properties though?     

> __< rbrunner >__ Just making sure I understand it on a high conceptual level: The "invisible to view-all key" transactions can't go the normal way through the blockchain?     

> __< brandon:cypherstack.com >__ "view ALL"     

> __< brandon:cypherstack.com >__ i'm done arguing. if the community thinks this isn't a security problem and monero gets delisted for not being compliance friendly, that's not my decision.     

> __< kayabanerve:matrix.org >__ I, from what I've read, believe you're claiming CARROT view keys not being inclusive to other wallets is an issue. I'd disagree with that premise     

> __< ofrnxmr >__ Translation: CARROT wallet has 100xmr in it, but auditor with view-all key see's less-than 100xmr = view-all is falsely advertised     

> __< kayabanerve:matrix.org >__ But, AFAICT, your exceptional case is an output to a distinct wallet??     

> __< ofrnxmr >__ no, output to the same wallet     

> __< ofrnxmr >__ . > <brandon:cypherstack.com> but you sent it to the same wallet it came from     

> __< kayabanerve:matrix.org >__ That means your reading of "view all" means all wallets, not just this wallet, AIUI?     

> __< kayabanerve:matrix.org >__ except it explicitly isn't scannable by the wallet ofrnxmr     

> __< jpk68:matrix.org >__ brandon:cypherstack.com: Monero is delisted from almost everything already     

> __< jbabb:cypherstack.com >__ rbrunner: yes they can.  monero-wallet-cli detects "evil" spends made this way that are self-spends or a send-to-self see it as being sent to an outside address even though they still own it     

> __< jbabb:cypherstack.com >__ we save the secret needed in a sort of notebook on the side.  it requires custom software but passes consensus and gets confirmed     

> __< kayabanerve:matrix.org >__ so it can't be to the same wallet AIUI     

> __< sgp_ >__ Is there a clear written summary of the conditions this may apply to? We need to fully understand that to know if it’s an issue or something we can say we don’t care about     

> __< kayabanerve:matrix.org >__ So outputs to _different wallets_ manually migrated in aren't in-scope is the claim jbabb:cypherstack.com: ?     

> __< rbrunner >__ That all sounds pretty weird. Maybe we talk past each other at least in part, and don't fully understand brandon's argument ...     

> __< ofrnxmr >__ Well, if someone can swipe the funds from your paper wallet, and your view-all key doesnt notice, id say this isnt desirable behavior     

> __< rbrunner >__ Uh, *that's* not on the table, right?     

> __< sgp_ >__ ofrnxmr: Is that the case though?     

> __< sgp_ >__ It doesn’t sound like it?     

> __< jbabb:cypherstack.com >__ kayabanerve:matrix.org: I'm not sure I understand the question sorry.  tbh I agree that it isn't really a problem yet--it may indicate a weakness in the protocol that mathematicians exploit somehow in the future--but so far it's not really a problem with CARROT as we do enough different that it's some evil sort of carrot anyways     

> __< jbabb:cypherstack.com >__ and I think this is outside of the scope of this agenda item and also unrelated to fireine's agenda item completely     

> __< ofrnxmr >__ Or rather, i guess the case is that you can have funds on the paper wallet and hide them     

> __< rbrunner >__ You could construct a paper that appears empty when looked at with a view-all key but isn't really, however, if I understand correctly     

> __< rucknium >__ ofrnxmr: AFAIK, you as the wallet holder would have to deliberately set up those conditions. And you still see funds leaving the wallet, if I understand correctly. You just don't see funds entering.     

> __< jberman >__ ofrnxmr: AIUI you have to have created a custom wallet with custom software to create a distinct view-all key      

> __< kayabanerve:matrix.org >__ missing credits, not missing debits, afaiui     

> __< ofrnxmr >__ Yeah, sorry. Got mixed up for a sec     

> __< sgp_ >__ And does it require knowledge of the private spend key to create these “hidden” credits?     

> __< diego:cypherstack.com >__ jberman: if the argument for something not being a problem is that there is currently no software that supports it, that's a bad argument     

> __< jberman >__ As I get it, it's a view-all key that requires trust that the view-all key holder created a well formed view-all key. And you can detect if they didn't if they spend funds     

> __< kayabanerve:matrix.org >__ Same jberman, in which case this is saying view-al keys aren't view ALL because they don't cover other wallets even though other wallets' outputs have to be manually migrated in?     

> __< rbrunner >__ I don't think we reached already a point where we can confidently judge whether it's a problem, and if yes how big IMHO     

> __< kayabanerve:matrix.org >__ but we can't say a view key ever works for all wallets     

> __< kayabanerve:matrix.org >__ jberman: *while reusing some keys from the original wallet     

> __< kayabanerve:matrix.org >__ (AFAIUI)     

> __< rbrunner >__ jberman: That makes sense as an explanation - if it's correct     

> __< kayabanerve:matrix.org >__ So the view-all key doesn't view distinct wallets which may overlap?     

> __< kayabanerve:matrix.org >__ (with _some_ keys)     

> __< sgp_ >__ I’m concerned about the possibility (if this even applies!) of users causing headaches to exchanges by depositing funds that don’t appear in their incoming balances, tracked by view all key. But does that scenario apply here?     

> __< diego:cypherstack.com >__ it's really not that deep guys. CARROT is being marketed as having a view key wherein you can see all the funds coming in and out. It's not that. Either decide that's not a problem and adjust the verbiage on CARROT description, or fix the problem so the description is accurate. There's no in-between or trying to halfway change the verbiage.      

> __< kayabanerve:matrix.org >__ I think the sender has to the distinct wallet, though Brandon left before we're clear     

> __< jbabb:cypherstack.com >__ kayabanerve:matrix.org: as far as I understand, yes     

> __< rucknium >__ Do we know how much larger the txs would be with the fix? The verifiable random function.     

> __< kayabanerve:matrix.org >__ diego:cypherstack.com: AIUI, it requires sending to a distinct wallet, and we lack clarity.     

> __< jberman >__ No shot this is getting fixed with increased tx sizes     

> __< kayabanerve:matrix.org >__ If this requires sending to a distinct wallet, as jbabb:cypherstack.com: just agreed, then it is arguing about the view key not covering _distinct wallets_     

> __< kayabanerve:matrix.org >__ That's why we're discussing this so     

> __< jberman >__ I think argument is going to be over accurately describing the key's properties     

> __< articmine >__ jberman: What is the increase in tx size? Is this known?     

> __< kayabanerve:matrix.org >__ If the claim is the view key doesn't show TXs not sent to the CARROT wallet with consistent keys, I don't see any issue.     

> __< boog900 >__ If this bug can only be dine with the wallets spend key then I don't think it is an issue, otherwise I do.     

> __< kayabanerve:matrix.org >__ If the claim is 'ghost debits', where a wallet can spend funds it doesn't actually have, that's an issue but only with the debit system AFAICT, trivially solved via checking key images, I'd assume     

> __< kayabanerve:matrix.org >__ diego:cypherstack.com: Can CS please provide a clear writeup at some point so we may properly discuss this?     

> __< jbabb:cypherstack.com >__ kayabanerve:matrix.org: Here's the conjecture:     

> __< jbabb:cypherstack.com >__ Assume:     

> __< jbabb:cypherstack.com >__ * Alice is an honest sender,     

> __< jbabb:cypherstack.com >__ * Mallory is a dishonest user with a new-hierarchy wallet,     

> __< jbabb:cypherstack.com >__ * Vera is an auditor,[... more lines follow, see https://mrelay.p2pool.observer/e/7LGbwYkLdjNDYVhZ ]     

> __< diego:cypherstack.com >__ kayabanerve:matrix.org: done ^     

> __< fireine:matrix.org >__ diego:cypherstack.com: Cool.     

> __< rbrunner >__ I am really curious how this will play out.     

> __< rbrunner >__ And if there is a real problem I will shout "See! This is all much too complex" :)     

> __< fireine:matrix.org >__ rbrunner: it's chaotic but presumably solvable      

> __< rbrunner >__ I don't doubt, e.g. with more complexity, right, like that "random function whatever" :)     

> __< jbabb:cypherstack.com >__ as far as I understand it, this means that this custom approach does not track the CARROT specification     

> __< rbrunner >__ I am only joking about 30% or so, don't misunderstand     

> __< kayabanerve:matrix.org >__ Mallory sends to a distinct wallet, in effect. Vera's auditing is correct for the wallet Vera has access to AFAICT in that it resolves as 0?     

> __< kayabanerve:matrix.org >__ Also, the write-up has typos AFAICT. (iii) should be a second credit, not a second debit?     

> __< jbabb:cypherstack.com >__ well... except insofar as that you can trick a CARROT-specification-following-wallet into thinking it has less than it really does.  that a boat accident happened     

> __< boog900 >__ Ok so Mallory does this to her own wallet ...      

> __< kayabanerve:matrix.org >__ Sending 10 XMR to a different wallet, where the auditor observes the spend but not the receipt, is fundamental     

> __< kayabanerve:matrix.org >__ jbabb:cypherstack.com: except it's to a different wallet     

> __< rbrunner >__ Well, if we claim we built a system where you have to follow Carrot to transact, but you can cheat and operate Carrot+/- in stealth, that's an exploit, no?     

> __< boog900 >__ kayabanerve:matrix.org: They would see the spend though right?     

> __< boog900 >__ like its not really a different wallet      

> __< kayabanerve:matrix.org >__ Mallory, in effect, derives a bespoke wallet and sends to it. Why _should_ the view key for the original wallet apply?     

> __< kayabanerve:matrix.org >__ How is this not     

> __< kayabanerve:matrix.org >__ "If people don't use CARROT, CARROT stops applying"?     

> __< boog900 >__ kayabanerve:matrix.org: Its an issue becuase the keys would still see the spend      

> __< jbabb:cypherstack.com >__ boog900: and you can send it back and they regain control     

> __< boog900 >__ boog900: but not see it incoming      

> __< kayabanerve:matrix.org >__ boog900: The spend is detected and is to a non-CARROT wallet, therefore distinct     

> __< boog900 >__ right?     

> __< boog900 >__ kayabanerve:matrix.org: no if you were to then spend that again      

> __< boog900 >__ they view all key would see that right?     

> __< jbabb:cypherstack.com >__ that, I would have to check.     

> __< boog900 >__ so it sees the spend of the first but not the incoming and the spend of the second      

> __< boog900 >__ right?     

> __< kayabanerve:matrix.org >__ In the exact write-up above, it isn't spendable again AFAICT     

> __< jbabb:cypherstack.com >__ boog900: yes, you can send to self and they detect the spend but not where it went     

> __< jbabb:cypherstack.com >__ then if the evil mallory chooses in the future to spend to self back into the CARROT wallet they would detect the incoming funds and regain control     

> __< fireine:matrix.org >__ Mallory is not breaking any cryptographic primitive. She is exploiting the fact that CARROT's view-all scanning relies on outputs being constructed according to the protocol's derivation scheme (ScalarDerive).     

> __< fireine:matrix.org >__ perhaps this statement is naive tho      

> __< ofrnxmr >__ kayabanerve:matrix.org: At all? So its burned?     

> __< boog900 >__ jbabb:cypherstack.com: what?     

> __< jbabb:cypherstack.com >__ I'm sorry, I https://matrix.to/#/!toFcRZtpaiwiyapgVO:matrix.org/$XcV7c2sC_wAkQUyhGKs0TfzZDIi_EMNU3Wa2Ku7S7Fc fireine's comments to Freeman's work, but they aren't really related.  I saw "View-All Evasion" and jumped to the conclusion that they had independently discovered something related, but I don't see how they are related after review     

> __< kayabanerve:matrix.org >__ *send to self's distinct wallet though, which is a key distinction, jbabb:cypherstack.com:     

> __< boog900 >__ kayabanerve:matrix.org: yes but thats what I got from above      

> __< fireine:matrix.org >__ jbabb:cypherstack.com: cant we use a zkzk proof that ScalarDerive was followed     

> __< fireine:matrix.org >__ i should have optimized everything before pushing that commit. by bad lol     

> __< kayabanerve:matrix.org >__ An overlapping spend key does not change the view key is distinct     

> __< fireine:matrix.org >__ also we should document that view-all tracks honestly-constructed flows only.     

> __< fireine:matrix.org >__ maybe at the MRL meeting agenda     

> __< kayabanerve:matrix.org >__ fireine:matrix.org: We don't need any additional proof if the issue is the owner may have multiple wallets and may only share _some_'s view keys     

> __< fireine:matrix.org >__ kayabanerve:matrix.org: can U say more?     

> __< UkoeHB >__ 'View all' is implicitly 'view all enotes sent/received within the carrot spec'. It does not include out-of-spec receives. Not sure how an auditor would see negative balance for spent enotes whose key images he doesn't know and can't verify. Non-compliant enotes would need to be 'isolated' into essentially a wallet-within-a-wallet, otherwise audits would fail when looking at txs containing key images of unknown      

> __< UkoeHB >__ providence.     

> __< boog900 >__ jbabb:cypherstack.com: so they don't see the spend of the bad output?     

> __< fireine:matrix.org >__ kayabanerve:matrix.org: like a toy model or smth     

> __< boog900 >__ if this is the case then it is just the same as sending to another wallet lol      

> __< kayabanerve:matrix.org >__ I'm saying, AFAICT, the posited issue is a view-all key is scoped to wallet, not person, where a person may have multiple wallets. That's fundamental, not an issue needing a fix, AFAICT     

> __< jbabb:cypherstack.com >__ boog900: ok, then we're back to: sorry, I don't know and have to check.     

> __< jbabb:cypherstack.com >__ boog900: I agree it's effectively this at this point.  but I Am Not A Cryptographer     

> __< tevador >__ I agree with kayabanerve and UkoeHB. The "view-all" key does not claim to see payments that don't follow the Carrot specs.     

> __< rbrunner >__ Hmmm ... maybe we see the birth of a new protocol, like "Tomatoe" or whatever, and the issue is maybe not more that you can serve two protocols at the same time with a single wallet?     

> __< rbrunner >__ *not more than     

> __< boog900 >__ People were talking about negative balances earlier      

> __< boog900 >__ so surly it still sees the spend      

> __< kayabanerve:matrix.org >__ if the auditor did, I'd agree that's a bug, but the fix is just checking debits against scanned credits to remove such 'ghost debits' > <boog900> so they don't see the spend of the bad output?     

> __< jpk68:matrix.org >__ From a usability perspective, I am inclined to believe that, IF a wallet can receive 'hidden' enotes without the owner doing this on purpose, AND this only applies to incoming transactions, it is a bug rather than a feature. Just throwing this out there; I am also not a cryptographer (obviously)     

> __< tevador >__ And I don't think you can ever detect negative balance in the wallet even if you miss payments because the wallet balance only reduces if an enote known to be owned by the wallet is spent.     

> __< kayabanerve:matrix.org >__ rbrunner: If a CARROT View key does not scan a Tomatoe output, does that mean the view key isn't a view key?     

> __< fireine:matrix.org >__ jbabb:cypherstack.com: Even if you were, it’s not like you’d actually be doing anything. At least you’re putting the time in lol     

> __< jpk68:matrix.org >__ However, I am strongly of the opinion that no compromises should be made for so-called "compliance", full stop.     

> __< kayabanerve:matrix.org >__ jpk68:matrix.org: The owner has to collude with an alternative wallet as far as we can tel.     

> __< ofrnxmr >__ jpk68:matrix.org: A knife can be used to cut a steak, a rope, or a person. Cant stop someone from using the tool for compliance     

> __< ofrnxmr >__ So its either we dont allow knives, or we accept that some people might use them to hurt people     

> __< jpk68:matrix.org >__ kayabanerve:matrix.org: As in, if I am a regular person using Skylight Wallet with my self-hosted LWS server, people cannot send "hidden" enotes that cannot be seen from my LWS client without me making this possible on my part?     

> __< UkoeHB >__ tevador: I suppose you could inflate apparent balance using selfsends constructed as normal enotes. But a deep enough audit would question the providence of those enotes.     

> __< kayabanerve:matrix.org >__ jbabb:cypherstack.com: You reacted with a thumbs down, but how is Mallory's alt derivation of K_o'prime _not_ a theoretical Tomatoe process?     

> __< jpk68:matrix.org >__ ofrnxmr: Yes, my point is just that design decisions should not be made to purposefully allow for increased compliance, as that is not the purpose of Monero.     

> __< kayabanerve:matrix.org >__ CARROT view keys don't work for receives via Tomatoe, a non-CARROT process, even if Tomatoe reuses some keys AFAICT.      

> __< jbabb:cypherstack.com >__ I meant: "does that mean the view key isn't a view key?" No.  Right? > <kayabanerve:matrix.org> If a CARROT View key does not scan a Tomatoe output, does that mean the view key isn't a view key?     

> __< fireine:matrix.org >__ my understanding is that view-all only guarantees visibility of enotes constructed according to CARROT spec; non-compliant outputs inherently fall outside this scope and to prevent audit contamination, wallets must enforce strict domain isolation, never mixing compliant and non-compliant inputs in a single transaction.     

> __< kayabanerve:matrix.org >__ Oh, sorry lol     

> __< tevador >__ UkoeHB: the view-all wallet will detect the key image on the selfsend and deduct balance correctly.     

> __< boog900 >__ I don't think we can make progress without more info      

> __< rbrunner >__ +1     

> __< kayabanerve:matrix.org >__ Okay, but then the issue is why this is considered such a bug by brandon:cypherstack.com: and diego:cypherstack.com: , as we feel we must be missing something, somewhere.     

> __< jbabb:cypherstack.com >__ I was trying to scroll up--someone else put it much better up above--if the claim is that we came up with fcmp++ and carrot was the only way to use it and thus all fcmp++ txs get "compliant!" view-all keys, well, we can use fcmp++ apparently without a lawful good carrot, is all     

> __< fireine:matrix.org >__ jpk68:matrix.org: +1     

> __< UkoeHB >__ tevador: oh true, you can't cycle it.     

> __< kayabanerve:matrix.org >__ CARROT is not protocol-enforced and any entity may have multiple wallets, sure     

> __< ofrnxmr >__ jpk68:matrix.org: I agree that if this only effects compliance theater, then i dont care lmao     

> __< fireine:matrix.org >__ kayabanerve:matrix.org: bc it is a bug. and the bug is buggy for many reasons     

> __< kayabanerve:matrix.org >__ The view-all key is still view-all within the scope of the CARROT wallet though     

> __< kayabanerve:matrix.org >__ fireine:matrix.org: No one has posited a way to send to the same wallet without it being viewed. What exactly do you think the bug is?     

> __< rucknium >__ I would be worried about this issue if it could affect protocols like atomic swaps and escrow. Could it?     

> __< kayabanerve:matrix.org >__ Do you have a way to send to a CARROT wallet in a way the view key cannot detect?     

> __< fireine:matrix.org >__ kayabanerve:matrix.org: I'll be putting the data in soon.     

> __< jbabb:cypherstack.com >__ rucknium: it's something to be aware of and advise all people working on atomic swap, multisig, or other protocols with shared wallets in ways that their counterparties can be dishonest so as to guard against, yes     

> __< rbrunner >__ With my little knowledge I can imagine problems if people use a different, non-Carrot protocol where nevertheless *some* txs made are visible to Carrot, and some not     

> __< fireine:matrix.org >__ kayabanerve:matrix.org: in short - after skimming through the spec think wallet owner must have control over output construction     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: If I send 1 XMR to the hash of "Rucknium", I can claim I sent 1 XMR to you. You'd check your wallet and not notice.People who do bespoke wallet protocols require mutual support. There shouldn't be concern re: atomic swaps.     

> __< jbabb:cypherstack.com >__ if you build an app ("smart contract", whatever) on top of monero that uses a shared wallet in some step or uses view keys as some security feature, yes     

> __< ofrnxmr >__ jbabb:cypherstack.com: Dont think so, as the swap wallet (as is) only needs to detect incoming funds and xmr is the second mover ?     

> __< fireine:matrix.org >__ jbabb:cypherstack.com: won't the crazy people try injecting NFTs     

> __< fireine:matrix.org >__ into the smart contract     

> __< freeman:cypherstack.com >__ More research needs to be done, of course, but my fear is this has ramifications deeper than just using a new wallet     

> __< fireine:matrix.org >__ freeman:cypherstack.com: doing it now     

> __< jpk68:matrix.org >__ jpk68:matrix.org: ^ I apologize for asking again, but I feel like this is very relevant from a usability perspective     

> __< kayabanerve:matrix.org >__ jbabb:cypherstack.com: Except these outputs to 'guard against' aren't to that wallet, they're to a distinct wallet. Guardimg against TXs to other wallets isn't sensical unless an explicit relation exists of note. That's why I'm pushing for clarity or correction.     

> __< jbabb:cypherstack.com >__ you have to have the spend key to do this > <jpk68:matrix.org> From a usability perspective, I am inclined to believe that, IF a wallet can receive 'hidden' enotes without the owner doing this on purpose, AND this only applies to incoming transactions, it is a bug rather than a feature. Just throwing this out there; I am also not a cryptographer (obviously)     

> __< fireine:matrix.org >__ rucknium:monero.social cross-cutting into your previous post regarding smart contracting / NFT's on monero     

> __< fireine:matrix.org >__ https://www.reddit.com/r/Monero/comments/12kv5m0/empirical_privacy_impact_of_mordinals_monero_nfts/     

> __< jpk68:matrix.org >__ jbabb:cypherstack.com: Okay, so it would only be the owner of the wallet doing this on purpose. Others cannot send "invisible" enotes.     

> __< rucknium >__ People have already injected NFTs into the Monero block chain and called them Mordinals. tx_extra length was limited by a relay rule to prevent it.     

> __< rucknium >__ fireine:matrix.org: Right.     

> __< fireine:matrix.org >__ rucknium: i already credited U     

> __< kayabanerve:matrix.org >__ jpk68:matrix.org: People can always send 'you' outputs you can't see. People can't send you XMR via CARROT in a way you can't detect though.     

> __< kayabanerve:matrix.org >__ I sent you 1 XMR right now jpk68:matrix.org: . To scan it, just solve for my private key.     

> __< tevador >__ There is no way to send an enote to a Carrot wallet in a way that an (unmodified) ViewAll tier doesn't detect it but an (unmodified) Master tier does. When sending an enotes not constructed according to the Carrot specs, the payment never actually arrives in the wallet.     

> __< rucknium >__ Has this conversation run its course for the time being? I will put it on next meeting's agenda.     

> __< kayabanerve:matrix.org >__ Oh no, 1 XMR I sent to you in a bespoke way you can't scan/spend 😱     

> __< kayabanerve:matrix.org >__ I think tevador summarized it best, yeah     

> __< tevador >__ So far, I think the "issue" is just a nitpick on the naming of "ViewAll", which actually can't view arbitrarily botched enotes.     

> __< jbabb:cypherstack.com >__ Monero doesn't yet force compliance with view-all keys on the protocol level is about the gist of the finding as I understand it?     

> __< fireine:matrix.org >__ jbabb:cypherstack.com: Why?     

> __< jbabb:cypherstack.com >__ or that CARROT isn't enforced?     

> __< jpk68:matrix.org >__ jbabb:cypherstack.com: Even if this Carrot thing wasn't an issue, can you not still use legacy wallets after the hardfork?     

> __< boog900 >__ jbabb:cypherstack.com: you can't, if I understand the issue correctly, I can just make a new wallet to do the same thing: send XMR to myself without a view key seeing it.     

> __< fireine:matrix.org >__ rucknium: Indeed, this deserves more active dialogue and think it might make sense to place at next meeting agenda.     

> __< rucknium >__ 7. CCS proposal: ProbeLab P2P Network Metrics Proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667)     

> __< articmine >__ boog900: This is also my thought     

> __< yiannisbot:matrix.org >__ 👋 Hi everyone!      

> __< fireine:matrix.org >__ articmine: this should be formally verified.     

> __< fireine:matrix.org >__ bc it's quite the assumption     

> __< boog900 >__ its pretty much what it says here^ > <jbabb:cypherstack.com> Assume:     

> __< fireine:matrix.org >__ boog900: not yet formally verified.     

> __< tevador >__ I vote to NOT place "ViewAll issue" on the next meetings agenda unless a clear write-up with examples is publicly provided in advance of the meeting.     

> __< fireine:matrix.org >__ tevador: well, it's almost complete     

> __< fireine:matrix.org >__ what about next meeting?     

> __< fireine:matrix.org >__ assuming we put the data in      

> __< fireine:matrix.org >__ and you'll get toy models, not examples     

> __< yiannisbot:matrix.org >__ rucknium: Hi everyone, here to answer any questions regarding the proposal. I hope people had the time to look through the updated proposal, although I didn't see any new comments in the issue.     

> __< rucknium >__ yiannisbot:matrix.org: Hi. Thanks. I think there was a misunderstanding about terminology. I said before that the Dandelion++ paper ignored unreachable nodes. You said in your revised proposal that they ignored spy nodes. Just change that to unreachable nodes. Spy nodes are very reachable. Being reached is their main purpose :)     

> __< fireine:matrix.org >__ tevador: By the way, how is voting done at MRL? Surely not on chain?     

> __< rucknium >__ I think the proposal looks good in its revised form. The exploratory research is risky, but that is usually the case with research. I mean risky in terms of uncertainty about the outcome.     

> __< yiannisbot:matrix.org >__ rucknium: 😅 Of course, apologies. Wrong phrasing. I'll change that.      

> __< fireine:matrix.org >__ because that would be stupid      

> __< rucknium >__ I would change moneronet.info to https://xmrnetscan.redteam.cash/ in the proposal.     

> __< ofrnxmr >__ fireine:matrix.org: Please dont post the same thing repeatedly and edit your messages. each edit comes through as a new message and spams irc and the meeting logs     

> __< fireine:matrix.org >__ tevador: freeman:cypherstack.com jbabb:cypherstack.com i'll place the data for such write-up at the repo and if there's anything useful feel free to harvest - this deserves a place at the agenda at some point.     

> __< fireine:matrix.org >__ ofrnxmr: governance isn't spam. even if you hate it.     

> __< jpk68:matrix.org >__ That's not the point     

> __< fireine:matrix.org >__ it is.     

> __< ofrnxmr >__ fireine:matrix.org: EACH EDIT IS SPAM     

> __< fireine:matrix.org >__ voting is non-trivial     

> __< rucknium >__ MRL has "votes" sparingly because MRL members are not really defined. If someone has strong objections to something, then MRL tries to talk it out. Then an ad-hoc voting process may be followed if consensus is very difficult to reach. Last year there was a decision that took months.     

> __< fireine:matrix.org >__ ofrnxmr: at your opinion.     

> __< fireine:matrix.org >__ this isnt a blockchain. its matrix. but in general i agree     

> __< jbabb:cypherstack.com >__ fireine, what ofrn means is that when you edit your message, it sends the whole message again on irc.     

> __< fireine:matrix.org >__ rucknium: makes sense.     

> __< fireine:matrix.org >__ jbabb:cypherstack.com: I see. I don't usually use matrix. thanks for letting me know      

> __< fireine:matrix.org >__ signal only usually.     

> __< jbabb:cypherstack.com >__ also, fireine, please, we're on another agenda item.  please wait for your next agenda item when that comes up; see the github issue referenced at the very beginning of the meeting     

> __< fireine:matrix.org >__ jbabb:cypherstack.com: sure     

> __< fireine:matrix.org >__ timezone mismatch. thought we still had ten minutes til active dialogue.     

> __< rucknium >__ ofrnxmr:monero.social, boog900:monero.social : Do you have comments on ProbeLab's proposal now that you have had time to digest the revisions?     

> __< vtnerd >__ my only comment was to re-iterate what someone else said: “he Dandelion++ paper assumes that spy nodes do not play a role and therefore ignores them in the analysis.” -> I assume this was meant to be unreachable nodes?     

> __< vtnerd >__ spy nodes were definitely a part of their analysis iirc     

> __< fireine:matrix.org >__ vtnerd: what is a reasonable definition for a "spy node"     

> __< boog900 >__ rucknium: I think it's ok      

> __< yiannisbot:matrix.org >__ vtnerd: Yes, definitely, apologies, this was my fault.      

> __< vtnerd >__ yeah which is minor because I guessed based on context it was a typo     

> __< boog900 >__ fireine:matrix.org: A node trying to link IPs to txs.     

> __< fireine:matrix.org >__ boog900: what if the node operating a "spy" service without its knowledge. how can we identify or tag them as a "spy node"     

> __< fireine:matrix.org >__ meaning the service running on such node is linking IPs to txns and not the runtime itself     

> __< rucknium >__ They would have to know. Spying is deliberate and involves active aggregation of information.     

> __< fireine:matrix.org >__ rucknium: what if it's mythos, for example     

> __< fireine:matrix.org >__ or an adversarial ai     

> __< rucknium >__ The main model of spy nodes is explained in the D++ paper. One moment.     

> __< rucknium >__ https://moneroresearch.info/122 Fanti, G., Venkatakrishnan, S. B., Bakshi, S., Denby, B., Bhargava, S., & Miller, A., et al. (2018). Dandelion++: Lightweight Cryptocurrency Networking with Formal Anonymity Guarantees. Proc. ACM Meas. Anal. Comput. Syst. 2(2).       

> __< fireine:matrix.org >__ https://www.cnbc.com/2026/06/01/anthropic-eu-ai-mythos-access-advanced-model.html     

> __< rucknium >__ I think the ProbeLab proposal is ready to go to #monero-community:monero.social     

> __< fireine:matrix.org >__ I think anthropic peeps are mostly weird. so laugh at their models too. but still. something to consider     

> __< rucknium >__ Any more comments on this item?     

> __< jpk68:matrix.org >__ fireine:matrix.org: Whether or not it's run by an AI is completely irrelevant. A spy node is a spy node     

> __< rucknium >__ 8.  Potential ring signature findings (https://github.com/monero-project/meta/issues/1399#issuecomment-4604934837)     

> __< jbabb:cypherstack.com >__ nothing from CS on this.     

> __< rucknium >__ tevador: "I vote to NOT place "ViewAll issue" on the next meetings agenda unless a clear write-up with examples is publicly provided in advance of the meeting." That sounds good to me. I will put it on the agenda if a write-up is provided.     

> __< fireine:matrix.org >__ jpk68:matrix.org: A spy is a person who secretly collects information for a government, organization, military, or other group. An ai isn't a prson     

> __< fireine:matrix.org >__ rucknium: I vote to have it placed at the agenda bc the issue is a trivially obvious one.     

> __< fireine:matrix.org >__ and shouldn't need a write up bc it is obvious     

> __< fireine:matrix.org >__ but will provide this regardless     

> __< boog900 >__ why does it matter? > <fireine:matrix.org> A spy is a person who secretly collects information for a government, organization, military, or other group. An ai isn't a prson     

> __< fireine:matrix.org >__ boog900: it doesn't. just wanted a reasonable definition so i can look into it :)     

> __< boog900 >__ just a discussion to waste time      

> __< rucknium >__ Thanks. It seemed during the ViewAll discussion today that there were some details that a write-up would clarify. It would help discussion.     

> __< boog900 >__ boog900: ^     

> __< fireine:matrix.org >__ boog900: for you perhaps.     

> __< fireine:matrix.org >__ i'd argue dealing with curves is itself a waste of time.     

> __< fireine:matrix.org >__ yet here we are     

> __< fireine:matrix.org >__ rucknium: i'll work on that.     

> __< rucknium >__ rucknium: fireine:matrix.org: I think you wanted to put this ^ item on the agenda. Could you start the discussion?     

> __< fireine:matrix.org >__ rucknium: Indeed, but don't think I'm authorized to make these projections yet so will tie in freeman:cypherstack.com     

> __< jbabb:cypherstack.com >__ as far as I can tell, fireine's findings are unrelated to Freeman's and the ones we were all discussing earlier     

> __< jbabb:cypherstack.com >__ they seem to be premised on the reuse of one time use keys     

> __< fireine:matrix.org >__ jbabb:cypherstack.com: based on ideas from freeman:cypherstack.com     

> __< jbabb:cypherstack.com >__ I have to apologize.  I saw "View-All Evasion" mentioned and assumed that we were all discussing the same thing and so related two unrelated concepts.     

> __< fireine:matrix.org >__ jbabb:cypherstack.com: Well, the data exists but hasn't yet been pushed. I'll get to that.     

> __< yiannisbot:matrix.org >__ What are next steps here rucknium:monero.social ? > <rucknium> I think the ProbeLab proposal is ready to go to #monero-community:monero.social     

> __< boog900 >__ jbabb:cypherstack.com: IIRC wallet2 has a ring cache to prevent this issue right?     

> __< jberman >__ yes it does, non issue     

> __< freeman:cypherstack.com >__ This linkability issue is separate, and solved with opt-in linkability. I have a PQ paper solving it that will be published around August, but I don’t think it’s a problem in this setting     

> __< freeman:cypherstack.com >__ Since in cryptocurrencies, the point is to catch key reuse, it’s fine     

> __< fireine:matrix.org >__ jberman: have you read the pq paper     

> __< rucknium >__ yiannisbot:matrix.org: yiannisbot:matrix.org: I think plowsof would put it on the next Community Workgroup meeting for approval at that stage, then go to funding required. I think plowsof's role may have changed a little recently, however. plowsof:matrix.org , what do you think?     

> __< freeman:cypherstack.com >__ Though, it means those cryptocurrencies are married to their hash function. If a large family of collisions were found tomorrow, it would cause problems with linking tags     

> __< freeman:cypherstack.com >__ But that hasn’t happened yet, so whatever     

> __< rucknium >__ A few published papers have analyzed key reuse on Monero hard forks. Any Monero hard forkers are supposed to implement key image reuse mitigation to prevent privacy issues.     

> __< plowsof:matrix.org >__ ofrnxmr has been organising the community meetings as of late but that sounds like a plan      

> __< ofrnxmr >__ rucknium: If all looks good here, then it can bbe merged before the next meeting     

> __< jberman >__ fireine:matrix.org: have I read a paper that will be published in August?     

> __< fireine:matrix.org >__ Mitigations ≠ Specifications     

> __< fireine:matrix.org >__ jberman: jbabb:cypherstack.com: pushed a draft here im not trolling U     

> __< fireine:matrix.org >__ for GRYMOIRE     

> __< yiannisbot:matrix.org >__ ofrnxmr: Cool, thanks. When does that meeting take place? Is that a public meeting where we're supposed to be present?      

> __< fireine:matrix.org >__ so assumed maybe it was shared     

> __< rucknium >__ https://moneroresearch.info/45 Wijaya, D. A., Liu, J. K., Steinfeld, R., Liu, D., & Yu, J. 2019, On The Unforkability of Monero. Paper presented at Proceedings of the 2019 ACM Asia Conference on Computer and Communications Security.     

> __< freeman:cypherstack.com >__ rucknium: My research is mostly interested in linkable ring signatures where the linking tag is formed from a different primitive than taking a hash digest. So it’s generally applicable, but imo NOT an issue here     

> __< rucknium >__ https://moneroresearch.info/39 Vijayakumaran, S. 2023, Analysis of CryptoNote Transaction Graphs using the Dulmage-Mendelsohn Decomposition. Paper presented at 5th Conference on Advances in Financial Technologies (AFT 2023).       

> __< freeman:cypherstack.com >__ e.g.: syndrome computation or MinRank     

> __< fireine:matrix.org >__ doesn't eliminate the need to understand and formally document the baseline risk. > <freeman:cypherstack.com> This linkability issue is separate, and solved with opt-in linkability. I have a PQ paper solving it that will be published around August, but I don’t think it’s a problem in this setting     

> __< fireine:matrix.org >__ The point is that accidental key reuse should be caught and prevented, not that reuse should be publicly linkable. If a wallet generates duplicate one-time keys by mistake, that's a catastrophic privacy failure. Making it detectable doesn't prevent it.     

> __< fireine:matrix.org >__ Both the View-All isolation requirement and one-time key reuse prevention point to the same architectural imperative: robust privacy and auditing in Monero depend on comprehensive wallet-level specification and enforcement, not just cryptographic properties alone.     

> __< boog900 >__ Thanks chatGPT     

> __< boog900 >__ > The point is that accidental key reuse should be caught and prevented     

> __< boog900 >__ We do     

> __< boog900 >__ That's what the ring cache is.      

> __< fireine:matrix.org >__ freeman:cypherstack.com: Does the hash-based linking tag in Monero's current implementation create linkability risks that wallet mitigations inadequately address? If no, prove it. If yes, our formalization is necessary     

> __< fireine:matrix.org >__ boog900: I don't run GPT. I use a Lambda instance when necessary.     

> __< fireine:matrix.org >__ different model     

> __< fireine:matrix.org >__ H100.     

> __< freeman:cypherstack.com >__ Thanks for sharing those papers rucknium:monero.social, will read now     

> __< rucknium >__ No problem. I think there may be a third paper out there, but I'm not sure.     

> __< rucknium >__ The relevant part of the second paper is "secondly using data from four hard forks of Monero in addition to the main Monero chain." I have successfully run the code from the second paper if you need any pointers on that.     

> __< fireine:matrix.org >__ rucknium: https://scholar.googleblog.com/2025/11/scholar-labs-ai-powered-scholar-search.html     

> __< fireine:matrix.org >__ rucknium: Very interesting.     

> __< fireine:matrix.org >__ is this code public?     

> __< rucknium >__ Yes     

> __< rucknium >__ With very good documentation, too.     

> __< rucknium >__ https://www.respectedsir.com/cna  https://github.com/avras/cryptonote-analysis     

> __< fireine:matrix.org >__ rucknium: can u pls link     

> __< fireine:matrix.org >__ oh IIT!     

> __< fireine:matrix.org >__ https://eprint.iacr.org/2021/760     

> __< fireine:matrix.org >__ THX!     

> __< rucknium >__ Is there more to discuss in this agenda item for now?     

> __< fireine:matrix.org >__ boog900: To be brutally honest and to straighten the record - lots of the zkzk community assumes I am some borg like entity. You are not the only one. I have been at academia since before OpenAI even existed and doing quite well for myself unassisted, might I add ; - )     

> __< fireine:matrix.org >__ rucknium: No more dialogue to field at my end, thank U     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< ofrnxmr >__ thanks ruck     

> __< gingeropolous >__ huzaah!     

> __< syntheticbird >__ and me who thought I was unhinged, fireine:matrix.org make me look like a sane person     

> __< fireine:matrix.org >__ syntheticbird: if you think I'm insane — just wait til you meet the NEAR cryptograthors     

> __< intr:unredacted.org >__ yeah this is among the most chaotic MRLs I've personally witnessed     

> __< fireine:matrix.org >__ intr:unredacted.org: I think whats at the agenda is solvable tho     

> __< fireine:matrix.org >__ To straigten the record — we still need to deliver the probability density function to the core development team...? What is the current status of this?     

> __< fireine:matrix.org >__ ofrnxmr:monero.social^     

> __< jpk68:matrix.org >__ yiannisbot:matrix.org: https://github.com/monero-project/meta/issues     

> __< rucknium >__ fireine:matrix.org: Are you talking about OSPEAD? I was investigating the safety of having multiple decoy distributions being used at the same time, as would happen with a non-mandatory rollout. I tried many different ways to attack privacy and it did seem safe. But effort has switched to deploying FCMP, which would eliminate the decoy distribution problem.     

> __< rucknium >__ Initially it was assumed that OSPEAD would be deployed with a mandatory rollout, e.g. as part of a hard fork with Seraphis, but the FCMP advances changed that.     

> __< fireine:matrix.org >__ rucknium: Vacuously yes. I have not yet extensively evaluated the monero codebase but am taking active steps to do so as we speak and will put the data in regarding a complete pq spec before the end of the week. If there's anything that's non-trivial, I'm sure it'll find it's way into the chats in a way that doesn't spam everyone (not our intent).     

> __< fireine:matrix.org >__ the data will be pushed to https://github.com/firoorg/crucible/tree/main/lessons-from-monerochan/fieckert-working-group-pq-spec     

> __< fireine:matrix.org >__ I'm sure freeman:cypherstack.com will see it at some point and share if iff it's non-trivial.     

> __< fireine:matrix.org >__ I can't expect prof menezes to audit all of our stuff bc he is super busy and has already kindly done this for us before for a different project. so will try and self-filter what is and isn't trivial by just pushing privately for now.     

> __< fireine:matrix.org >__ admittedly hilarious — but also obviously a serious issue     

> __< fireine:matrix.org >__ https://arxiv.org/abs/2606.03811     

> __< fireine:matrix.org >__ Our results demonstrate that self-sustaining AI-driven cyber-threats are no longer theoretical. We must prepare for autonomous generative adversaries     

> __< syntheticbird >__ sir, this is a wendy's     

> __< fireine:matrix.org >__ > <jbabb:cypherstack.com> Assume:     

> __< fireine:matrix.org >__ I've presumably solved the conjecture and it's been validated at Reuben's internal repo. My analysis appears to confirm that a wallet owner can evade CARROT's view-all auditing by constructing non-compliant self-send outputs outside the ScalarDerive derivation path, but this represents an inherent limitation of view-key-based  [... too long, see https://mrelay.p2pool.observer/e/oZGgyIkLemR0WTBy ]     

> __< fireine:matrix.org >__ https://github.com/firoorg/crucible/blob/main/lessons-from-monerochan/fieckert-working-group-pq-spec/conjecture.md     

> __< fireine:matrix.org >__ to be precise, the markdown presumably validates that the conjecture is "true"     

> __< fireine:matrix.org >__ I'm not mathematically sophisticated yet so it needs to be screened for bullshit. But I put the data in.     

> __< fireine:matrix.org >__ it's trivial bc we don't give a fuck about compliance. but if we did. it's a serious thing. that being said it is indeed still a bug.     

> __< fireine:matrix.org >__ at my opinion.     

> __< fireine:matrix.org >__ jbabb:cypherstack.com: pls do not waste your time until I've added comments. will be up before end of day EST.     

> __< selsta >__ It might be better to discuss these things in a private message, otherwise you are talking about a document no one can access.     

> __< fireine:matrix.org >__ selsta: monero stakeholders can indeed access it.     

> __< fireine:matrix.org >__ monero core / affiliates.     

> __< fireine:matrix.org >__ including fieckert.     

> __< jbabb:cypherstack.com >__ I can't access it     

> __< jbabb:cypherstack.com >__ but I'm not a stakeholder really :)     

> __< fireine:matrix.org >__ jbabb:cypherstack.com: reuben:firo.org:     

> __< fireine:matrix.org >__ selsta: xmr is a private ecosystem. or at least, that's what it was designed to be. private cash lol. can't hate me for requesting privacy when it's a core part of what I see as the ethos     

> __< fireine:matrix.org >__ selsta: just ping reuben:firo.org     

> __< fireine:matrix.org >__ fieckert articulated that it doesnt always make sense to share at research chats. and so i wont     

> __< fireine:matrix.org >__ he was core.     

> __< selsta >__ This channel is for open research. I don't want access to the document, but it goes against the spirit of the channel. If you don't wan to share it here that's fine, but then also no need to talk about it in here.     

> __< fireine:matrix.org >__ selsta: you're going against the spirit of the monero private ecosystem      

> __< fireine:matrix.org >__ privacy is non-trivial     

> __< fireine:matrix.org >__ like sharing a view key     

> __< fireine:matrix.org >__ ignoring fieckert would be stupid.     

> __< jpk68:matrix.org >__ At least spell his name right :P     

> __< fireine:matrix.org >__ *dialogue he has injected at the past regarding this     

> __< fireine:matrix.org >__ jpk68:matrix.org: top cryptographers and mathematicians make typos all the time. just putting the data in. typos are trivial. but I will try and spell Aaron's name correcly     

> __< plowsof:matrix.org >__ top whatevers need to stop being so full on and spamming      

> __< fireine:matrix.org >__ plowsof:matrix.org: pq isn't spam.     

> __< plowsof:matrix.org >__ could you at least role play the researcher role properly and create an open document for people to review and share thoughts on at a meeting     

> __< fireine:matrix.org >__ plowsof:matrix.org: role play?     

> __< fireine:matrix.org >__ respectfully, LMAO     

> __< fireine:matrix.org >__ bitcoin primitive OG's have endorsed my work     

> __< fireine:matrix.org >__ I'm not a crankpot     

> __< fireine:matrix.org >__ even if you want me to be      

> __< plowsof:matrix.org >__ yeah stop spamming      

> __< fireine:matrix.org >__ it's not spam. it's pq dialogue     

> __< fireine:matrix.org >__ and if it's ignored bad things will happen     

> __< fireine:matrix.org >__ I'll push the data to reuben:firo.org 's repo and if anyone with access think's it is non-trivial, it'll likely be shared. I'll end my dialogue here, thank you     

> __< fireine:matrix.org >__ Unfortunately, quantum computers / logical qubits are real.     

> __< fireine:matrix.org >__ take care.     

> __< plowsof:matrix.org >__ i know who satoshi is, doesnt give me the right to spam my stream of consciousness here      

> __< fireine:matrix.org >__ plowsof:matrix.org: prof. menezes built the primitives he used to create your beloved btc. and he endorsed our work. but ok.     

> __< fireine:matrix.org >__ send satoshi our regards lol     

> __< fireine:matrix.org >__ take care     

> __< jpk68:matrix.org >__ std::consciousness_stream x << "random jargon";     

> __< jpk68:matrix.org >__ mrl_messages = x.str();     

> __< jpk68:matrix.org >__ Wait, that's the wrong syntax :((     

> __< jpk68:matrix.org >__ Ruined the joke     

> __< boog900 >__ > top cryptographers and mathematicians make typos all the time     

> __< plowsof:matrix.org >__ "And the silence is deafening  / You're absolutely right"     

> __< fireine:matrix.org >__ jpk68:matrix.org: is this an insult?     

> __< boog900 >__ Nah its a really nice compliment     

> __< fireine:matrix.org >__ boog900: they do. at least at the context of computation, optimization | actual invariant theory      

> __< fireine:matrix.org >__ boog900: i had similar thoughts when menezes endorsed our work and pushed other faculty to do the same. hopefully the bullshit we push isn't comparatively retarded     

> __< fireine:matrix.org >__ anyways, I'll stop "spamming" the chats and get back to work.     




> __< UkoeHB >__ Hi     

> __< jpk68:matrix.org >__ Hello     

> __< rbrunner >__ Hello     

> __< vtnerd >__ Hi      

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< jeffro256 >__ Howdy      

> __< jberman >__ Beta stressnet debugging and working with jeffro256 on resolving a beta net specific consensus issue     

> __< jeffro256 >__ ^ Same      

> __< rucknium >__ me: Keeping stressnet stressed and monitored. Reviewing monerosim version 0.1.0     

> __< rbrunner >__ Still Polyseed in the Monero core software     

> __< vtnerd >__ Me: updating various prs in monerod and lws. Moving back to looking at serialization limits and block size again shortly      

> __< rucknium >__ 3. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686).     

> __< tevador >__ I have no updates, I'm still going with AC1024 as discussed in the last meeting. I can answer questions if needed.     

> __< syntheticbird >__ Hi     

> __< rucknium >__ I thought more about having an interactive address option. I think some merchants have problems with non-interactive txs. Or you could say that they are accustomed to the "pull" procedure of digital fiat payments, but cryptocurrency txs are "push". In previous research, I found this set of complaints about accepting cryptocurr [... too long, see https://mrelay.p2pool.observer/e/nIrw_oQLU1NOeXQ5 ]     

> __< rucknium >__ Just some thoughts on UX. Or DX (developer experience) maybe.     

> __< rucknium >__ ^ AFAIK, that site blocks Tor. And I cannot get archive.org to work right now :(     

> __< tevador >__ I think that interactive transactions could be an option, but not the only option. There are use cases for non-interactive transfers.      

> __< rucknium >__ That reminds me that the Tor Project is running a cryptocurrency donation campaign for some internet privacy tools, including ones that are useful for research. I used OnionShare to collect user-submitted monerod logs, for example. The donation link appears in the blank page of the newest version of Tor Browser: https://internetfreedom.torproject.org/     

> __< rucknium >__ They accept XMR. Donations are being matched by Cake Wallet and Zcash Community Grants, plus some smaller donors.     

> __< rucknium >__ tevador: I agree. Not the only option. I just wanted to say that an optional interactive protocol could have some UX/DX advantages.     

> __< tevador >__ Yes, I'm still planning to include an interactive protocol in the appendix of Jamtis.     

> __< rucknium >__ 👍     

> __< tevador >__ In response to spirobel, for point 2, you cannot just pretend that passively posted donation addresses don't exist. They do and we are not going to discontinue that use case.     

> __< tevador >__ This is a response to: https://libera.monerologs.net/monero-research-lab/20260519#c677589     

> __< rucknium >__ Here was point 2: > <spirobel:kernal.eu> tevador: https://libera.monerologs.net/monero-research-lab/20260518#c677439     

> __< rucknium >__ > 2.the one-to-many "donation address" use case:     

> __< rucknium >__ > for this case the status quo is that we have systems like kuno, ccs, xmrchat.     

> __< rucknium >__ > there is a need for the group to see a donation counter go up.[... more lines follow, see https://mrelay.p2pool.observer/e/rcqJ_4QLX0kyemE4 ]     

> __< sgp_ >__ I agree passive donation addresses are important     

> __< rucknium >__ More discussion about PQ addressing?     

> __< rucknium >__ 4. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< rucknium >__ This week we got above the 5MB block size ceiling, as predicted. To 6MB blocks :)     

> __< rucknium >__ https://stressnetnode1.redteam.cash/     

> __< rucknium >__ I also set up an alt chain visualizer because we needed it this week: https://stressnetconsensus1.redteam.cash/ https://stressnetconsensus2.redteam.cash/     

> __< rucknium >__ The same app code as for mainnet, adjusted a little for stressnet.     

> __< jberman >__ Modifying the long term window in the dynamic scaling algo to kick in at 2 weeks instead of the current 100k block window unfortunately triggered a consensus issue that's leading to a number of syncing problems / chain splits. After some rounds trying to resolve the issue cleanly, it seems the most efficient option on the table to proceed is to essentially restart the stressnet     

> __< jeffro256 >__ After a lot of discussion with j-berman, I think that it is decided that we are going to rollback the stressnet for the beta v2.0 release due to the grossness of the consensus break. I am going to put out a PR which clears the blockchain if using a previous version of the beta stressnet, merge in the LTM window cache size fix, [... too long, see https://mrelay.p2pool.observer/e/jeyo_4QLam01TTAy ]     

> __< rucknium >__ That sounds fine to me     

> __< rbrunner >__ So more or less one off-by-one bug, and stressnet broke down? Really shows the importance of code reviews :)     

> __< spirobel:kernal.eu >__ tevador: just to clarify: i am not for discontinuing the use case. its just that if someone wants this functionality, they have to continue to scan the whole chain. also again: my suggestion is non interactive.      

> __< jberman >__ It's worth noting this isn't an issue that would have affected mainnet, nor an issue with the updated scaling implementation proposed for FCMP++. It was strictly an issue with the stressnet specific change that would only affect stressnet to decrease the LT window so the chain could grow faster and get stressed faster on stressnet     

> __< rbrunner >__ Somehow missed that crucial detail, thanks for clarifying!     

> __< spirobel:kernal.eu >__ regarding the PQ addressing small addition: it would be good to have it as a separate document from jamtis and it shouldnt take up most of the space regarding addressing design choices. the discussion should be more focused on ux problems in the real world and how we can reduce scan time.  > <rucknium> More discussion about PQ addressing?     

> __< rucknium >__ The intended use of the new stressnet node is to just swap the old monerod out and start running the new one without deleting the old stressnet blockchain?     

> __< jberman >__ Ya basically just a smooth path for people upgrading to not have to manage deleting their db manually     

> __< rucknium >__ That would skip the long testnet sync from scratch :)     

> __< rbrunner >__ So basically one big reorg back to start of stressnet?     

> __< rbrunner >__ Dropping blocks like crazy :)     

> __< jberman >__ Ah sorry, I misinterpreted your message. No, it would actually delete the old stressent db, so it would re-sync from scratch     

> __< jberman >__ Unfortunately popping blocks needs an overhaul to be faster than just re-syncing     

> __< rbrunner >__ ... on testnet     

> __< jpk68:matrix.org >__ spirobel:kernal.eu: Why shift the focus even further away from the non-interactive side of the protocol? This seems like a needlessly large UX change with no apparent benefit     

> __< jeffro256 >__ For reference , my stressnet node wasn't even able to pop 100 blocks per hour on my older desktop computer, so we figured it would be literally faster to just clear the entire DB and re-sync from scratch     

> __< rucknium >__ pop blocks is very useful, but not when blocks are large.     

> __< rucknium >__ IIRC, BTC doesn't have an easy-to-use pop_blocks command.     

> __< rbrunner >__ That somehow sounds strange. I remember dropping blocks quickly. Really that much of a difference if they are large? Or maybe slower since FCMP?     

> __< rbrunner >__ (dropping blocks quite in general, years ago)     

> __< spirobel:kernal.eu >__ jpk68:matrix.org: i clarified earlier my approach is non interactive. further context: https://xcancel.com/spirobel/status/2020868563532382583#m and two more MRL messages ...      

> __< jeffro256 >__ Yeah, it's not a FCMP++-specific issue, but FCMP++ really doesn't help for popping blocks: https://github.com/monero-project/monero/issues/10207     

> __< jeffro256 >__ Especially when each block is >6MB     

> __< rbrunner >__ Ah, I see, I was dropping manually using one of the extra tools beside monerod     

> __< rbrunner >__ Which of course didn't put anything back into the pool     

> __< spirobel:kernal.eu >__ jpk68:matrix.org: https://mrelay.p2pool.observer/e/gIrIw4QLRzMzb2VC maybe i should turn this whole thing into a gist ... just to be clear i dont like interactive protocols ... where both parties have to be online at the same time.      

> __< rbrunner >__ monero-blockchain-export     

> __< rbrunner >__ --pop-blocks     

> __< rucknium >__ At one point, there were 9 orphaned blocks produced for the same block height. Was that caused directly be the consensus bug? It was a sight to behold.     

> __< jeffro256 >__ lol probably      

> __< rucknium >__ Did we have progress on the other stressnet issues?     

> __< rucknium >__ https://mrelay.p2pool.observer/m/monero.social/gYZDLUYFleUqMRKiFOSBRoOD.png (consensus-breakdown.png)     

> __< rucknium >__ ^ Here was the set of orphan blocks on https://stressnetconsensus1.redteam.cash/     

> __< rbrunner >__ Cool     

> __< rucknium >__ Can IRC side see images?     

> __< rbrunner >__ There is a link that works     

> __< rbrunner >__ (But might expire after some time, I guess)     

> __< rucknium >__ Thanks, DataHoarder[m] , for working IRC image links :)     

> __< jberman >__ Slight progress on impaired node connectivity after deep reorgs, and jeffro also made solid progress on 1) faster wallet loading when the pool is large, and 2) improved fix to unrestricted RPC when the pool is large > <rucknium> Did we have progress on the other stressnet issues?     

> __< jberman >__ The consensus issue has unfortunately taken up a solid amount of time     

> __< rucknium >__ Nice     

> __< rucknium >__ I mean nice to your first message     

> __< rucknium >__ After the meeting I will shut down my stressnet monitors while I re-sync testnet     

> __< rucknium >__ Any other discussion about stressnet?     

> __< jberman >__ Nothing from me     

> __< spirobel:kernal.eu >__ jpk68:matrix.org: the apparent benefit is that you dont have to sync wallets anymore.     

> __< rucknium >__ 5. CCS proposal: ProbeLab P2P Network Metrics Proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).     

> __< rucknium >__ yiannisbot:matrix.org said he would arrive to the meeting at 18:00 UTC. In 6 minutes.     

> __< yiannisbot:matrix.org >__ Hi everyone, I'm here :)      

> __< yiannisbot:matrix.org >__ The general feeling of the community seems to be that we skip Milestone 1 and focus on Milestone 2. We won't only count unreachable nodes, but try to find better heuristics and derive insights that would help identify spy nodes and blockchain surveillance companies. We will also spend some time to investigate if POW systems wo [... too long, see https://mrelay.p2pool.observer/e/sP21gIULNmpoZmxz ]     

> __< yiannisbot:matrix.org >__ Does that sound like a good summary? We plan to update the proposal issue to reflect these new directions. Any extra feedback is more than welcome as we try to shape up the final version.      

> __< yiannisbot:matrix.org >__ rucknium:monero.social: plowsof what's your take and suggestions for next steps?     

> __< rucknium >__ That sounds good to me. Right, I think one would use monerosim when you are ready to actually implement a feature into the monerod C++ codebase. Initial research on the viability of a PoW approach would come before that.     

> __< rucknium >__ boog900:monero.social had some recent thoughts about spy node countermeasure that he may want to post here.     

> __< yiannisbot:matrix.org >__ Exactly. So if while doing the study we come up or identify a previously proposed approach that looks attractive, we can then port it into monerosim.     

> __< rucknium >__ More comments on this item? (I see someone typing)     

> __< vtnerd >__ For #2 (unreachable nodes) you kind of have to do the work if #1 anyway? Just no fancy dashboard?     

> __< boog900 >__ I had an idea on how we could prove nodes were not making too many outbound connections but it would require something like proof of storage. If we could do that though then we might be able to allow stemming to inbound connections, which would increase the stem graph and remove the privacy leak when nodes don't allow inbound.     

> __< yiannisbot:matrix.org >__ Yeah, kind of. That's why we included it as a first item/milestone. But given M1 is not desired we'll do just what is needed to be able to get to M2.     

> __< boog900 >__ It's pretty cheap to tag on with proof of storage though     

> __< rucknium >__ To get unreachable nodes, you take a different approach. You have to passively wait for nodes to connect to you. To get reachable nodes, you can just crawl rapidly through peer lists, connecting briefly to each reachable node. To get the ratio of reachable to unreachable, of course, you would do both.     

> __< rucknium >__ Or there may be a smarter way to get unreachable node count, but I don't know of one.     

> __< vtnerd >__ the primary value of unreachable node estimation is in d++ privacy related. Is that the consensus? Because funding the research for that makes sense     

> __< yiannisbot:matrix.org >__ vtnerd: Agreed, but to me that would be the natural next step.     

> __< rucknium >__ vtnerd:monero.social: Yes     

> __< yiannisbot:matrix.org >__ boog900: That's a good approach. We'll take this into account as we revise the methodology for Milestone 2.      

> __< boog900 >__ I feel Milestone 2's scope is getting large.     

> __< rucknium >__ Paraphrasing, the D++ papers said that unreachable nodes don't play a large role in the network, so they are ignored in the analysis. We could show that unreachable nodes do play a big role in the network, at least by the number of nodes.     

> __< rucknium >__ I am trying to find the quote. They don't use the term "unreachable"     

> __< rucknium >__ Can't find it at the moment.     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< yiannisbot:matrix.org >__ Thanks. We'll be back next week with an updated proposal for Milestone 2 and hope to make progress from there.      

> __< tevador >__ spirobel: Your twitter post is too vague to properly judge the proposal. You should post a more detailed write-up, with all the keys and derivations, what constitutes an address, what is included on-chain and what must be shared off-chain.     

> __< tevador >__ I'm suspecting that in the process of writing it down, you will identify several issues.     

> __< spirobel:kernal.eu >__ tevador it is good enough to judge the core idea. no i don't think there is an issue with this. its a fairly clear idea     

> __< spirobel:kernal.eu >__ i will turn it into gist when i have more time      

> __< tevador >__ It's not clear to me. One paragraph says the sender includes an index verbatim, one paragraph says the sender increments an index and one paragraph says the sender fills part of the index with random data.     

> __< spirobel:kernal.eu >__ or write a prototype ...  do a kdf on the wallet seed and put it into the address ...  put the secret into the place where the dummy payment id is now      

> __< spirobel:kernal.eu >__ then only scan transactions that contain this secret in the dummy id      

> __< tevador >__ But that's a serious privacy regression. Any external observer can see the same pid repeating and can conclude that those two outputs are owned by the same party.     

> __< spirobel:kernal.eu >__ tevador ... yes because this works for only one tx, so after that this secret index needs to be incremented      

> __< tevador >__ That doesn't solve anything, the external observer can identify (pid, pid+1) just as easily as (pid, pid)     

> __< spirobel:kernal.eu >__ no it cant.  because after the initial transaction the channel is open and we can obviously "increment" it in away the channel observer wont know     

> __< tevador >__ Ah, so your proposal requires a secret channel between the sender and receiver. OK, in that case we don't actually need addresses, the receiver can just construct their own outputs every time.     

> __< spirobel:kernal.eu >__ and the point is: you find the channel opening ... and then you can find all others ... that where sent with this participant      

> __< spirobel:kernal.eu >__ no wallet syncing anymore      

> __< spirobel:kernal.eu >__ and just to be clear: by channel i mean this in the simplest way, just some ecdh with the viewkey in the address and just say: this is the next secret for the next transaction. then you can find it as easily as the first but the observer wont know. thats what i mean by increment      

> __< spirobel:kernal.eu >__ used the word channel because i had hedy lamarrs frequency hoping technique in mind, but its not some interactive off chain connection      

> __< spirobel:kernal.eu >__ so you can reconstruct the first secret from seed and you get all the others afterwards as the next "index" is always embedded in encrypted form in the transaction       

> __< tevador >__ Does it allow for stateless address generation? Probably not. You'd have to keep track of issued 'view keys' and never reuse the same key for two recipients (even if they don't send you anything). And you still have to scan, at least for the first transaction in every channel.     

> __< spirobel:kernal.eu >__ do subaddresses allow for stateless address generation? no we increment the subaddress index.  " never reuse the same key for two recipients " exactly what we recommend now for subaddresses ...      

> __< tevador >__ Jamtis does allow for stateless address generation.     

> __< spirobel:kernal.eu >__ and scanning for open channels: no. the expensive part is the cpu work ... and even if we were to still to do all the network fetching (which is not necessary, as this secret is similar to a txhash an "index" in the sense of a database index, so we can retrieve just what we want. its just a matter of in the case of remote node [... too long, see https://mrelay.p2pool.observer/e/zYKsgoULTVN4M0RS ]     

> __< tevador >__ It could probably work if the channel opening transaction included the original index. But at least the sender is always stateful. If they ever forget how many transactions they have sent, repeated 'view tags' will appear in the blockchain.     

> __< tevador >__ spirobel: you can't have stateless address generation that supports "index lookup" because you don't know which addresses exist.     

> __< spirobel:kernal.eu >__ yes i dont see statefulness as a big issue. wallets have to do this in practice. statefulness is cheap compared to having to scan every single transaction everyone is sending all the time      

> __< spirobel:kernal.eu >__ and also for logical reasons: if you want to compartmentalize your identity you have to make different identifiers for the people you interact with in any case      

> __< tevador >__ Stateful addresses get you issues like this: https://github.com/monero-project/monero/issues/8138     

> __< spirobel:kernal.eu >__ but that is an engineering issue. because wallet2.cpp sometimes left gaps ... in my wallet library i increment the index for every address generated      

> __< tevador >__ And how do you know the value of the index when restoring from a seed?     

> __< spirobel:kernal.eu >__ this whole lookahead thing is clunky ... also statelessness is not worth the price ... we can literally do away with scanning entirely ... which is a much practical step towards scaling than something like tachyon (which needs to update a proof constantly to be able to spend, different topic, but shows the different directions here ...)      

> __< spirobel:kernal.eu >__ "And how do you know the value of the index when restoring from a seed?" you would know how many addresses you generated ... you can easily just make 100000. just call the kdf make the  secret ask the node if there where txs for these ... just a database lookup     

> __< spirobel:kernal.eu >__ and the incremented indeces per participant only come into play if a tx was found ... if that is the case its easy ... because the info is in the tx      

> __< spirobel:kernal.eu >__ alright its getting late here I am getting sleepy. has been fun chatting with you cya      

> __< DataHoarder >__ <rucknium> Can IRC side see images? > 19:47:26 <rbrunner> There is a link that works > 19:47:58 <rbrunner> (But might expire after some time, I guess)     

> __< DataHoarder >__ the links won't expire unless the content is deleted on the matrix side     

> __< DataHoarder >__ and bridge stays up, it mainly proxies the authenticated call 1:1     




## Rucknium | 2026-07-09T19:30:46+00:00
@j-berman , please close this issue.

# Action History
- Created by: j-berman | 2026-06-02T16:51:56+00:00
- Closed at: 2026-07-09T19:40:45+00:00
