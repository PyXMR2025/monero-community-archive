---
title: Monero Research Lab Meeting - Wed 04 December 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1119
author: Rucknium
assignees: []
labels: []
created_at: '2024-12-03T21:21:23+00:00'
updated_at: '2024-12-17T21:19:59+00:00'
type: issue
status: closed
closed_at: '2024-12-17T21:19:59+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Carrot audit](https://github.com/cypherstack/carrot-audit/releases/download/final/Carrot-final.pdf).

4. [Security Review - Generalized Bulletproofs](https://repo.getmonero.org/-/project/54/uploads/b2d5c8198f55d72b588f1ef138126850/GBP_Security_Review.pdf). [Brandon Goodell's comments](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449#note_27508).

5. [Proposed Cypher Stack review of "On the Use of Logarithmic Derivatives in Eagen’s Proof of Sums of Points"](https://gist.github.com/kayabaNerve/6173fa623ac0f6a9cd4269c16f3ffd48).

6. [Veridise proposed work: Formal definition of an interactive protocol and verifying the R1CS defined in the FCMP++ paper aligns](https://gist.github.com/kayabaNerve/175a00de6edd3a64458dacb4f5e481e0).

7. [Discussion: preventing P2P proxy nodes](https://github.com/monero-project/research-lab/issues/126).

8. [FCMP++ tx size and compute cost](https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898). [On MAX_INPUTS and MAX_OUTPUTS](https://gist.github.com/kayabaNerve/dbbadf1f2b0f4e04732fc5ac559745b7). [Monero FCMP MAX_INPUTS/MAX_OUTPUTS empirical analysis](https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6).

9. Any other business

10. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1116 

# Discussion History
## j-berman | 2024-12-04T02:52:47+00:00
> 4. [Proposed Cypher Stack review of "On the Use of Logarithmic Derivatives in Eagen’s Proof of Sums of Points"](https://gist.github.com/kayabaNerve/6173fa623ac0f6a9cd4269c16f3ffd48).

> 5. [Veridise proposed work: Formal definition of an interactive protocol and verifying the R1CS defined in the FCMP++ paper aligns](https://gist.github.com/kayabaNerve/175a00de6edd3a64458dacb4f5e481e0).

In advance of the meeting, I left comments on my rationale supporting both of these proposals.

## plowsof | 2024-12-06T10:06:42+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting in this room in one and half hours.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1119     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< j​effro256:monero.social >__ Howdy     

> __< a​rticmine:monero.social >__ Hi     

> __< j​berman:monero.social >__ *waves*     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ hi     

> __< c​haser:monero.social >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< v​tnerd:monero.social >__ I’ve got to fix a functional test in my monerod patches, its a pain tracking it down for some reason     

> __< r​ucknium:monero.social >__ me: Suggested spy node ban list community communication plan: https://gist.github.com/Rucknium/76edd249c363b9ecf2517db4fab42e88 boog900  . HackerOne report.     

> __< j​effro256:monero.social >__ Me: testing and improving the Carrot code     

> __< j​berman:monero.social >__ me: wrapping up FCMP++ wallet sync starting from arbitrary restore height (it's working as expected), then planning to move over to FCMP++ proof construction over the FFI     

> __< o​frnxmr:monero.social >__ Not me, but i hope that those MAX_INPUT tests check 64+ inputs     

> __< j​berman:monero.social >__ I also commented my +1 on Gooddell's GPB review linked above by @plowsof, and provided more detailed rationale in support of moving forward with Cypher Stack to review Veridise's work on logarithmic derivatives in divisors, and to move forward with Veridise on R1CS proving     

> __< plowsof >__ Thanks jberman      

> __< r​ucknium:monero.social >__ 3) Carrot audit/review: https://github.com/cypherstack/carrot-audit/releases/download/final/Carrot-final.pdf     

> __< r​ucknium:monero.social >__ jeffro256: Could you give a summary and maybe TODO list that came out of this audit/review?     

> __< j​effro256:monero.social >__ The review went well with no real crypto issues , I just need to clarify some portions of the spec     

> __< j​effro256:monero.social >__ Also there were a couple typos     

> __< j​effro256:monero.social >__ But overall I'm happy with how it went     

> __< j​effro256:monero.social >__ One change that Kayaba brought up that would actually change the crypto is doing switch commitments     

> __< r​ucknium:monero.social >__ Doesn't that require a lot of post-quantum R&D?     

> __< j​effro256:monero.social >__ Not really if we're scoping it to just commitments they're pretty well understood     

> __< j​effro256:monero.social >__ The hard part is getting some PQ security out of the onetime outputs and key images     

> __< j​effro256:monero.social >__ But that part can be done later     

> __< rbrunner >__ What would that type of commitments improve?     

> __< j​effro256:monero.social >__ Amount commitment blinding factors are transmitted as part of the sender-receiver protocol and thus need to be decided beforehand     

> __< j​effro256:monero.social >__ Rbrunner: A switch commitment allows for a commitment to be perfectly blinding and computationally binding until it "switches" to perfectly binding     

> __< j​effro256:monero.social >__ Well not really "perfectly", but still computationally  binding against a quantum computer     

> __< rbrunner >__ So they would be a step towards future PQ security?     

> __< j​effro256:monero.social >__ In higher level terms, it let's us set up a PQ-secure turnstile in the future     

> __< rbrunner >__ And using those would not invalidate the audit results just obtained?     

> __< c​haser:monero.social >__ we'd basically get post-quantum monetary soundness in exchange for losing confidentiality     

> __< r​ucknium:monero.social >__ Would it be a true turnstile or just a future prohibition on spending outputs that do not have the switch commitments, i.e. outputs produced before switch commitments were available?     

> __< j​effro256:monero.social >__ I think they would basically be a very small-scoped swap of one part of the derivation, so we would need to revalidate just that small bit of the derivation , but nothing else     

> __< j​effro256:monero.social >__ Well it wouldn't lose confidentially unless actively "switched". We wouldn't retroactively lose confidentially for enotes spent before the turnstile     

> __< c​haser:monero.social >__ yes, this is to mean what comes after the hypothetical fork that flips the switch     

> __< j​effro256:monero.social >__ It depends on the implementation, but old outputs do not use switch commitments so there wouldn't be any way to prove a quantum computer didn't open its commitment to an arbitrary value so those probably wouldn't be allowed     

> __< j​effro256:monero.social >__ Proving ownership PQ-securely will be a lot harder , but that is specific to how the wallet derives its addresses , but doesn't need to be a part of the addressing protocol     

> __< j​effro256:monero.social >__ (At the moment)     

> __< j​effro256:monero.social >__ Switch commitments *do* though, unless we were to transmit the entire blinding factor encrypted to the receiver (which RingCT did do at one point)     

> __< j​effro256:monero.social >__ However, this costs an extra 32 bytes per enote     

> __< r​ucknium:monero.social >__ Ok. This is a big decision, so maybe we can think about it and come back next meeting to discuss more.     

> __< r​ucknium:monero.social >__ 4) Security Review - Generalized Bulletproofs. Brandon Goodell's comments. https://repo.getmonero.org/-/project/54/uploads/b2d5c8198f55d72b588f1ef138126850/GBP_Security_Review.pdf  https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449#note_27508     

> __< r​ucknium:monero.social >__ jberman: What is the "tightness gaps" you mentioned?     

> __< r​ucknium:monero.social >__ As far as I can tell, everything came out fine in the GBP review.     

> __< j​berman:monero.social >__ From section 4.1: "security proofs do not merely establish     

> __< j​berman:monero.social >__ security. The proof itself contains a description of a reduction from one problem to     

> __< j​berman:monero.social >__ another, and the details of that reduction lead to a tightness gap in security. Both     

> __< j​berman:monero.social >__ [3] and [7] neglect analysis of tightness. This is a usual practice and up to     

> __< j​berman:monero.social >__ industry standards."     

> __< r​ucknium:monero.social >__ Does "reduction from one problem to another" mean that it has been proven that P ⇔ Q? That statements P and Q are equivalent?     

> __< r​ucknium:monero.social >__ The "tightness gap" makes me think that they are not proven exactly equivalent.     

> __< r​ucknium:monero.social >__ Anyway, maybe this is something I need to educate myself on. Goodell says that GBP is proven OK up to industry standards.     

> __< r​ucknium:monero.social >__ Any more comments on this?     

> __< rbrunner >__ Are they already implemented for Monero, those GBPs?     

> __< j​berman:monero.social >__ I don't know if that question is directly relevant/exactly how it relates. From the conclusion which migh help provide more color: "The tightness gaps implied by the security proofs of [7] imply a lower bound on     

> __< j​berman:monero.social >__ scheme security, and this bound weakens with each transcript rewinding. Ensuring     

> __< j​berman:monero.social >__ this lower bound exceeds cryptographic security is a conservative way to select     

> __< j​berman:monero.social >__ system parameters for future system designers. It would be nice that [7] be modified     

> __< j​berman:monero.social >__ to mention and compute tightness gaps. Due to this, security theorem statements     

> __< j​berman:monero.social >__ are most useful when stated like this: If there exists an algorithm A which runs in     

> __< j​berman:monero.social >__ time at most tA and breaks one of the security properties of scheme S with success     

> __< j​berman:monero.social >__ probability at least ϵA, then there exists an algorithm B which runs in time at most     

> __< j​berman:monero.social >__ tB and solves a famously hard problem P with success probability at least ϵB"     

> __< r​ucknium:monero.social >__ This is sort of about the total bits of security of Monero txs, maybe     

> __< j​berman:monero.social >__ GBPs are "generalized bulletproofs" and are a core component of FCMP++. Kayaba implemented GBPs in his work on FCMP++     

> __< rbrunner >__ Nice     

> __< r​ucknium:monero.social >__ 5) Proposed Cypher Stack review of "On the Use of Logarithmic Derivatives in Eagen’s Proof of Sums of Points". https://gist.github.com/kayabaNerve/6173fa623ac0f6a9cd4269c16f3ffd48     

> __< r​ucknium:monero.social >__ The review sounds good to me. Thanks for the write-up, kayabanerve     

> __< j​berman:monero.social >__ It does seem relevant in that the choice of bit-security may be affected by the tigtness gap (i.e. a "tighter" gap seems to imply a wider window for certain classes of attacks, rendering a higher bit security unnecessary? I'm may be reading that portion incorrectly)     

> __< rbrunner >__ Yes, those gists are valuable to keep the (at least for me) much welcome overview     

> __< j​berman:monero.social >__ sorry, rending a higher bit security more necessary*     

> __< rbrunner >__ That proposed review seems good to me also     

> __< j​berman:monero.social >__ Nice :)     

> __< j​berman:monero.social >__ Reiterating +1 from me too     

> __< r​ucknium:monero.social >__ Anyone else have comments on Proposed Cypher Stack review of "On the Use of Logarithmic Derivatives in Eagen’s Proof of Sums of Points"?     

> __< rbrunner >__ Does Monero help here to push forward the state of the art of crypocurrencies in general?     

> __< j​berman:monero.social >__ AFAIK Monero seems to be the most widely used application of BPs, so it would certainly make sense for Monero to push forward research into attacks / security hardening for BPs     

> __< rbrunner >__ Interesting.     

> __< r​ucknium:monero.social >__ I see loose consensus here in favor of Cypher Stack review of "On the Use of Logarithmic Derivatives in Eagen’s Proof of Sums of Points". https://gist.github.com/kayabaNerve/6173fa623ac0f6a9cd4269c16f3ffd48     

> __< r​ucknium:monero.social >__ Or maybe jeffro wants to say something     

> __< r​ucknium:monero.social >__ Maybe not. Let's move on.     

> __< r​ucknium:monero.social >__ 6) Veridise proposed work: Formal definition of an interactive protocol and verifying the R1CS defined in the FCMP++ paper aligns. https://gist.github.com/kayabaNerve/175a00de6edd3a64458dacb4f5e481e0     

> __< r​ucknium:monero.social >__ Seems good to me     

> __< j​berman:monero.social >__ +1     

> __< rbrunner >__ Yes, thankfully looks good, because we need those R1CSs - whatever they are :)     

> __< c​haser:monero.social >__ rbrunner: this is a good primer: https://learn.0xparc.org/materials/circom/additional-learning-resources/r1cs%20explainer/#context-what-is-r1cs-and-how-does-it-fit-in     

> __< rbrunner >__ Thanks, looks pretty wild :)     

> __< c​haser:monero.social >__ it is :)     

> __< j​effro256:monero.social >__ Sorry, reviewing other people's review on zk proofs is a bit over my head ;)     

> __< j​effro256:monero.social >__ Hopefully someday it won't be     

> __< r​ucknium:monero.social >__ Do we have loose consensus here in favor of this proposed work by Veridise?     

> __< rbrunner >__ +1     

> __< c​haser:monero.social >__ I find the forest of proofs and reviews a bit hard to navigate, that flow chart discussed last week would definitely help :) but I have no objection either.     

> __< j​effro256:monero.social >__ With limited information , I say +1     

> __< j​berman:monero.social >__ I've been working on this spread sheet: https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/     

> __< c​haser:monero.social >__ jberman this is awesome. thank you. additional respect for using CryptPad.     

> __< rbrunner >__ Quite a number of lines towards the end, but those are mostly or even all code audits, right?     

> __< j​berman:monero.social >__ :)     

> __< j​berman:monero.social >__ Almost all code audits except "Gadgets formal verification"     

> __< rbrunner >__ Thus quite straightforward     

> __< r​ucknium:monero.social >__ I see loose consensus in favor of Veridise proposed work: Formal definition of an interactive protocol and verifying the R1CS defined in the FCMP++ paper aligns. https://gist.github.com/kayabaNerve/175a00de6edd3a64458dacb4f5e481e0     

> __< r​ucknium:monero.social >__ 7) Discussion: preventing P2P proxy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< rbrunner >__ So with those "gadgets" the "crypto" will be complete.     

> __< r​ucknium:monero.social >__ I wrote a draft post to urge node operators to enable boog900 's ban list: https://gist.github.com/Rucknium/76edd249c363b9ecf2517db4fab42e88     

> __< r​ucknium:monero.social >__ Note that the draft says "The Monero Research Lab (MRL) has decided to recommend that all Monero node operators enable a ban list of suspected spy node IP addresses."     

> __< j​berman:monero.social >__ @rbrunner yep, we're approaching the finish line for theoretical vetting of FCMP++     

> __< r​ucknium:monero.social >__ Is that accurate? Does MRL make that recommendation? Discuss.     

> __< rbrunner >__ Seems to me evidence is good enough, and potential harm big enough, to indeed speak out such a recommendation. We don't go overboard here, if you ask me.     

> __< r​ucknium:monero.social >__ I hope this can be released in a week or so. It would also need some Monero devs and researchers to PGP-sign the ban list and to ask SethForPrivacy to add the ban list to his monerod Docker template.     

> __< r​ucknium:monero.social >__ Anyone should feel free to suggest edits by making a comment on the gist     

> __< rbrunner >__ "MRL has decided to ask node operators to block these IP addresses voluntarily instead of by default." For what it's worth, that seems important to me.     

> __< c​haser:monero.social >__ IMHO looks sane, and the best that can be done to mitigate the problem at present.     

> __< j​effro256:monero.social >__ Do you have a deterministic method / piece of code that can re-find these proxies, and would you be willing to do a semi-closed source release to those who you want to the sign the banlist ?     

> __< r​ucknium:monero.social >__ rbrunner: Should I put that higher in the post?     

> __< r​ucknium:monero.social >__ jeffro256: That is a question for boog900     

> __< rbrunner >__ Seems like a good finishing sentence to me. That's a good spot IMHO     

> __< b​oog900:monero.social >__ Yes I'll PM you     

> __< j​effro256:monero.social >__ I understand that the methodology should remain semi-private since we don't want the adversary to adapt their methods, but I personally would like to know why I would be signing a banlist, even if I don't release the details to the public     

> __< rbrunner >__ Makes sense.     

> __< j​berman:monero.social >__ Speaking just for myself I don't personally want to take an explicit role in advocating for banning specific IP's. The approach seems reasonable generally to me though     

> __< j​berman:monero.social >__ I also haven't gotten the chance to dig deeper into @boog900 's findings, but it passes my initial smell test. Would encourage anyone who wants to dig deeper / sign off to PM @boog900 as well     

> __< s​yntheticbird:monero.social >__ now is the time to give each people a different method so that if one is patched we know who is the maul     

> __< j​effro256:monero.social >__ One legit use case for a proxy node tho that jberman brought up was running a node at home but not revealing to the world where your home is     

> __< b​oog900:monero.social >__ These nodes do not proxy all messages they handle handshakes themselves     

> __< rbrunner >__ Well, we don't have something against the occassional single proxy node, right?     

> __< rbrunner >__ Just to whole packs of them ...     

> __< b​oog900:monero.social >__ Or intercept and insert their own data     

> __< a​rticmine:monero.social >__ This may be related to the video I reviewed on MoneroTopia     

> __< r​ucknium:monero.social >__ The Chainalysis one? It might     

> __< a​rticmine:monero.social >__ Yes that one     

> __< a​rticmine:monero.social >__ The idea there was to trick unsuspecting wallets to connect to the spy none in order to collect the wallet IPs     

> __< a​rticmine:monero.social >__ Node     

> __< r​ucknium:monero.social >__ Boog900's findings are more about the P2P network privacy. IIRC the Chainalysis representative complained that Dandelion++ made their job harder. Maybe they are trying to have a strategy to weaken D++     

> __< a​rticmine:monero.social >__ Yes I understand, weaken D++ by collecting wallet IPs     

> __< a​rticmine:monero.social >__ My concern here is that a BS company does not change to use proxy IPs to do this     

> __< c​haser:monero.social >__ they can definitely weaken the effects of D++ by running loads of spy nodes, can't they?     

> __< a​rticmine:monero.social >__ Have to use     

> __< j​berman:monero.social >__ IIRC Chainanal was running malicious nodes hosted at community trusted domains that had prior expired and Chainanl picked up the domains. So it wasn't that they were running proxies on tons of IP's, rather that they controlled community trusted domains     

> __< r​ucknium:monero.social >__ chaser: Yes     

> __< j​berman:monero.social >__ Whereas the discussion here is relevant to running tons of spy proxy nodes across many different IP's, which Chainanal may also be doing, but it's not known who's doing that AFAIK     

> __< a​rticmine:monero.social >__ Yes they can., but detecting proxy nodes does not address this     

> __< r​ucknium:monero.social >__ chaser: The effect of the suspected spy nodes on the privacy provided by D++ is estimated here under "Empirical privacy impact": https://github.com/monero-project/research-lab/issues/126#issuecomment-2460261864     

> __< p​reland:monero.social >__ Making sure I remember this correctly: if you use your own node for transactions, this makes the Chainalysis attack not an issue for you, correct?     

> __< r​ucknium:monero.social >__ preland: The _remote node_ attack would not affect you, but your own node could still be connecting to peer spy nodes, which weakens D++. To avoid connecting to them, run the ban list.     

> __< j​berman:monero.social >__ ^+1     

> __< o​frnxmr:monero.social >__ tx-proxy     

> __< b​oog900:monero.social >__ I think Chainalysis were black-holing txs, if you look at the video by the IP addresses in observations there are small symbols, sadly he never hovered over any long enough for the help text to pop up with a description of what they mean, at least I didn't see it.     

> __< b​oog900:monero.social >__ The 4 symbols I have seen are: a speaker, cross, 3 lines, question mark.     

> __< b​oog900:monero.social >__ The only one I have a little bit of confidence on is the 3 lines, I think it means stem, like the tx was sent in a stem message. At 32:00 if you look at all outputs with IPs with that symbol the time till it was seen a second time is extremely high, it makes me think these txs were blackholed.     

> __< a​rticmine:monero.social >__ I believe the real issue is the behavior of the proxy node as opposed to the node being a peproxy     

> __< o​frnxmr:monero.social >__ anonymous-inbound     

> __< j​berman:monero.social >__ +1 to @ofrnxmr 's point also. Using tor/i2p via tx-proxy is another way to avoid a spy proxy node from correlating your node's IP to your txs     

> __< o​frnxmr:monero.social >__ NAT nodes are easier to blackhole, because you cant connect to them 🙃. Using anonymous-inbound and tx-proxy throw in variables that make it a guessing game     

> __< r​ucknium:monero.social >__ Yes, but there is an unresolved issue with the real IP address of a Monero node onion service being discovered. I can't link to it right now since moneroresaerch.info is giving an error 😬     

> __< a​rticmine:monero.social >__ So we have nodes that accept wallets. Connections but do not open outbound connections     

> __< o​frnxmr:monero.social >__ When you relay via tx-proxy, it doesnt share your onion address     

> __< o​frnxmr:monero.social >__ So even if you associate me ip to onion (my onion starts with ofrnxmr btw), you dont know my tx-proxy's txes     

> __< b​oog900:monero.social >__ your node will insert it at the end of a peer list message IIRC     

> __< o​frnxmr:monero.social >__ At the end ? 💀     

> __< r​ucknium:monero.social >__ Here it is: Shi et al. (2024) "Deanonymizing Transactions Originating from Monero Tor Hidden Service Nodes" https://dl.acm.org/doi/abs/10.1145/3589335.3651487     

> __< a​rticmine:monero.social >__ Can we focus on the node behaviour itself as opposed to whether it is behind a proxy?     

> __< o​frnxmr:monero.social >__ Sounds like unintended behaviors. Whats the point of hiding the addr$ss via "unknown tor host", if the host is known via being the last onion on the peerlist 🥲     

> __< o​frnxmr:monero.social >__ Artic, are you asking about the spy node behavior?     

> __< a​rticmine:monero.social >__ Yea     

> __< v​tnerd:monero.social >__ yikes, I really botched that then.     

> __< a​rticmine:monero.social >__ Yea     

> __< a​rticmine:monero.social >__ Yes     

> __< v​tnerd:monero.social >__ knowing the hidden service doesn’t automatically get you the IP address, at least, but some Tor node knows the correlation     

> __< r​ucknium:monero.social >__ ArticMine: Ideally, a Monero node should be able to determine if its peer is a single node or if it is part of a network of proxied nodes. The network of proxied nodes means that the spy node operator pays a lower cost in storage, RAM, and CPU.     

> __< v​tnerd:monero.social >__ this should’ve been an a GI Issue; I don’t recall seeing it before     

> __< v​tnerd:monero.social >__ another point - if you use —tx-proxy without —anonmous-inbound you get the privacy back, but aren’t helping the network of relays     

> __< r​ucknium:monero.social >__ There's a paper about how to check if something is a real single node or not, but requires a lot of protocol changes, found by boog900 : JHeo, Ramachandran, and Jurdak (2023) "PPoS : Practical Proof of Storage for Blockchain Full Nodes" https://ieeexplore.ieee.org/document/10174897     

> __< v​tnerd:monero.social >__ we can randomize the list, but there’s a timestamp too that could be problematic     

> __< r​ucknium:monero.social >__ Do we want to discuss `MAX_INPUTS`/`MAX_OUTPUTS` again or do we want to end the meeting here and postpone that discussion until we get more CPU benchmarks?     

> __< j​effro256:monero.social >__ The latter IMO     

> __< a​rticmine:monero.social >__ Yes but the real issue here is the spying. I just don't see the deterrence in just detecting proxies     

> __< a​rticmine:monero.social >__ I mean the BS company will just pass the additional cost to government     

> __< j​effro256:monero.social >__ if you can detect proxies, then you can ban them from D++ stems     

> __< r​ucknium:monero.social >__ AFAIK, the only deterrence that D++ has is to make it economically costly for an adversary to spy. It's a permissionless network after all.     

> __< r​ucknium:monero.social >__ This is the end of the meeting. We can continue discussing P2P network privacy, of course :)     

> __< c​haser:monero.social >__ mitigating that would probably require a different network-layer mixing method     

> __< c​haser:monero.social >__ and potentially non-trivial PoW for participation     

> __< j​berman:monero.social >__ @vtnerd here's the relevant code for sending a node's IP to outgoing connections at the end of the peerlist: https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/src/p2p/net_node.inl#L2475-L2501     

> __< r​ucknium:monero.social >__ chaser: I would agree. The Dandelion++ protocol limits the spying effectiveness to roughly the theoretical minimum. The theoretical minimum is a function of the share of spy nodes on the network.     

> __< j​effro256:monero.social >__ Thanks everyone !     

> __< j​berman:monero.social >__ @moneromoo brought up this exact issue on my PR and I completely forgot to look into it more :/ https://github.com/monero-project/monero/pull/8324#issuecomment-1125108872     

> __< r​ucknium:monero.social >__ I summarize the D++ protocol's resistance to spy nodes in the GitHub issue I linked above.     

> __< r​ucknium:monero.social >__ https://github.com/monero-project/research-lab/issues/126#issuecomment-2460261864     

> __< r​ucknium:monero.social >__ If an adversary has enough malicious nodes, he/she can also try to launch eclipse and network partitioning attacks, which are distinct from spying.     

> __< v​tnerd:monero.social >__ @jberman yes, I know what needs to be fixed, just a little disappointed I missed this first time     

> __< s​yntheticbird:monero.social >__ he/she? Artificial intelligence don't have gender     

> __< v​tnerd:monero.social >__ oh wow, just read that moo comment. a shame this wasn’t fixed earlier     

> __< o​frnxmr:monero.social >__ For any spy's that kept logs: i was joking. my onion doesnt start with "ofrnxmr" 🫠     

> __< a​rticmine:monero.social >__ From issue 126 the outbound connection behavior combined with accepting wallet connections are characteristic of the malicious nodes     

> __< a​rticmine:monero.social >__ I mean the proxy approach is reasonable as long as it does not inadvertently target legitimate proxy use for privacy purposes     

> __< a​rticmine:monero.social >__ In any case a back and forth between the community and the adversary on this could easily set up the adversary for a significant legal failure here in Canada over privacy law violations     

> __< r​ucknium:monero.social >__ https://moneroresearch.info/ is back up. It was the runaway mysql log issue again.     

> __< 0​xfffc:monero.social >__ Apologies everyone. I totally forgot/missed this meeting.      

> __< 0​xfffc:monero.social >__ Anyway, my update was mostly working on general wallet-rpc issues. #9601 and other small fixes. ( although small, but should introduce good speed up in many cases )     

> __< 0​xfffc:monero.social >__ I read the discussion. I have a question about blackhole nodes. What is the wallet response? I am a wallet. I send a transaction. My transaction gets blackholed on its way ( and never gets to fluff ). What do I do? wait and resend to same node?      

> __< 0​xfffc:monero.social >__ Because IIUC, blackholing is going to introduce another security issue. If I have 20% of nodes as spy node, I set the rule to blackhole any transaction unless you get it from the wallet. Then my surveillance capability is going to get a boost.      

> __< 0​xfffc:monero.social >__ Scenario 1:      

> __< 0​xfffc:monero.social >__ Wallet generates tx -> node 1 -(stem)- > node 2 (blackhole).      

> __< 0​xfffc:monero.social >__ Wallet waits x seconds.      

> __< 0​xfffc:monero.social >__ Wallet generates tx again, changes the node -> node 2 ( now this node has more information ), and passes the transaction.     

> __< r​ucknium:monero.social >__ In scenario 1, the honest `node 1` will broadcast the tx in fluff mode after the embargo timeout fires, so it still gets spread through the network without the wallet user doing anything.     

> __< 0​xfffc:monero.social >__ oh thanks. now it made sense. I forgot that all the nodes (on stem path) do the fluff after few seconds. So not big of a deal.     

> __< r​ucknium:monero.social >__ Still, IMHO, the black-holing node 2 gets some info from this. Because ordinarily node 2 doesn't know that the immediately preceding node in the stem was the actual origin.     

> __< r​ucknium:monero.social >__ But if node 2 black-holes the tx, then they can run a statistical model about how many nodes may have participated in the stem phase (because with more nodes participating in the stem phase, the first timeout will be reached sooner).     

> __< 0​xfffc:monero.social >__ Yes. it basically breaks the very purpose of stem. But still not as bad as I thought for a moment.     

> __< 0​xfffc:monero.social >__ The interesting case is when you have X % of nodes on the network. ( Let's say 30% of the nodes on the network are spy node and doing blackholing. That is the interesting case to think about ).     

> __< 0​xfffc:monero.social >__ For example. Let's think my scenario 1. If node 2 is blackholing. and after embargo timeout node 1 will fluff. Then considering you are running 30% of the nodes on the network. There is chance you know which nodes that tx is originated from.     

> __< b​oog900:monero.social >__ between all the stems that got the tx before it was blackholed the one to fluff should be random     

> __< b​oog900:monero.social >__ so ideally you shouldn't know if the one to fluff was the initiator     

> __< r​ucknium:monero.social >__ I'm not completely sure about this, but I think there's an impossibility proposition here. You can either:     

> __< r​ucknium:monero.social >__ (1) Set embargo timers so that which node is first to broadcast does not give much information about the true origin node, but how many nodes participated in the stem phase can be estimated by maximum likelihood estimation of how many `n` i.i.d. random variables are in `y = min{x_1, x_2,...,x_n}` where `y` is the actual observed time of the fluff broadcast. This timer could be hig<clipped message     

> __< r​ucknium:monero.social >__ h-variance/mean exponential, for example. Or     

> __< r​ucknium:monero.social >__ (2) Set embargo timers so that which node is first to broadcast does give information about the true origin node, but how many nodes participated in the stem phase is hard to estimate. This timer would be a low-variance random variable or even a fixed constant.     

> __< r​ucknium:monero.social >__ But you cannot get the best of both worlds of (1) and (2).     

> __< r​ucknium:monero.social >__ Of course, in case (1) if you estimate that only a single node participated in the stem phase, then you would guess which node was the actual tx originator.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

continued:
```
23:45:11 <m-relay> <a​rticmine:monero.social> The point of this BS attack is to get the IP address of the wallet and correllate it to the public TX information. This effectively bypasses D++. entirely.
23:47:31 <m-relay> <a​rticmine:monero.social> I am thinking in another direction entirely. Instead of blacklisting the malicious nodes to other nodes, blacklist the malicious nodes to the wallets.
23:49:41 <m-relay> <a​rticmine:monero.social> We create a blacklist of "suspicious" nodes and wallets following the blacklist will not connect to the "suspicions" nodes.
23:51:55 <m-relay> <a​rticmine:monero.social> We will have to be careful here in that those signing the blacklist should be in jurisdictions with strong anti SLAPP laws.
23:52:44 <m-relay> <b​oog900:monero.social> these are P2P nodes, they are (presumably) trying to find the IP of the first node in the stem route, the origin node. D++ is only used for P2P, not by wallets, currently at least. They don't announce RPC ports for wallets to use, although some do have active RPC servers.
23:54:10 <m-relay> <a​rticmine:monero.social> What we are doing here is giving the BS companies their own medicine back
23:55:35 <m-relay> <a​rticmine:monero.social> ... and Chainalysis has used any SLAPP in New York in their defense
23:55:56 <m-relay> <a​rticmine:monero.social> anti SLAPP
00:02:39 <m-relay> <a​rticmine:monero.social> They are after the IP of the wallet. This is from the video
00:03:45 <m-relay> <a​rticmine:monero.social> Chainalysis video
00:05:33 <m-relay> <a​rticmine:monero.social> Ok if they are not announcing  RPC ports this is totally different from the video
00:08:09 <m-relay> <b​oog900:monero.social> These nodes aren't necessarily Chainalysis, also in the Chainalysis video they were collecting nodes IPs & wallet IPs. Every IP they got that didn't have `RPC: ` by them was a node IP.
00:08:33 <m-relay> <b​oog900:monero.social> which was the majority
00:13:25 <m-relay> <b​oog900:monero.social> If anyone has any ideas on the symbols from the Chainalysis video it could give us more info: https://libera.monerologs.net/monero-research-lab/20241204#c467866
00:55:01 <m-relay> <a​rticmine:monero.social> On a different but impacted topic l was going to recommend increasing the grace period for changes in the median for the calculation of fees. This is currently set at 10 blocks. It is used for the enforcement of minimum node relay fees.
00:55:01 <m-relay> <a​rticmine:monero.social> The grace period is the time between transaction creation and transaction relay. This is to prevent a transaction from not being relayed because the median has changed between transaction creation and transaction relay.
00:56:16 <m-relay> <a​rticmine:monero.social> I am looking at a minimum of 60 blocks
00:57:26 <m-relay> <a​rticmine:monero.social> D++ makes this change necessary, even more if we add delay times
```

## shermand100 | 2024-12-12T12:23:26+00:00
For added context on the 'spy node' subject as a UK located user I wrote a little script on my PiNodeXMR node that found the matches below across currently connected, white list and gray list IP's when compared to the:
https://raw.githubusercontent.com/Boog900/monero-ban-list/refs/heads/main/ban_list.txt on the 11/12/2024

![Spy node saturation](https://github.com/user-attachments/assets/4defdfdc-61b4-4d35-8741-82577489b6fb)

Script for PiNodeXMR: https://raw.githubusercontent.com/shermand100/PiNodeXMR/refs/heads/master/BanListCompare.sh


## Rucknium | 2024-12-12T13:15:13+00:00
@shermand100: Good job! The suspected spy nodes do not initiate connections. They accept outbound connections from honest nodes. Outbound connections are the "privacy-sensitive" connection type as far as Dandelion++ is concerned. By default, nodes only establish 12 outbound connections. The privacy risk is determined by the percentage of outbound connections that are to spy nodes at the time that your node first relays your transaction. See my comment here: https://github.com/monero-project/research-lab/issues/126#issuecomment-2460261864

## Rucknium | 2024-12-13T21:56:41+00:00
@shermand100 Please take further discussion about the spy node ban list to https://github.com/monero-project/meta/issues/1124
Thanks :)

# Action History
- Created by: Rucknium | 2024-12-03T21:21:23+00:00
- Closed at: 2024-12-17T21:19:59+00:00
