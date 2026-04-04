---
title: Monero Research Lab Meeting - Wed 11 December 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1123
author: Rucknium
assignees: []
labels: []
created_at: '2024-12-10T20:58:05+00:00'
updated_at: '2024-12-20T20:50:39+00:00'
type: issue
status: closed
closed_at: '2024-12-20T20:50:39+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Discussion: preventing P2P proxy nodes](https://github.com/monero-project/research-lab/issues/126).

4. [Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography](https://github.com/monero-project/research-lab/issues/131)

5. Any other business

6. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1119 

# Discussion History
## Rucknium | 2024-12-13T19:52:20+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1123     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​rticmine:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< j​effro256:monero.social >__ Howdy     

> __< c​ast9:matrix.org >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Working on OSPEAD. I can see big changes in the real spend age distribution during the suspected spam earlier this year and in the week of the Binance delisting announcement. That suggests to me that the estimator is working properly, besides all the theoretical and simulation support for that hypothesis.     

> __< r​ucknium:monero.social >__ > But there’s way too much information to decode the Matrix. You get used to it. I…I don’t even see the code. All I see is [spam attack, delisting announcement, exchange rate volatility].     

> __< j​effro256:monero.social >__ Me: FCMP benchmarking and Carrot integration work     

> __< r​ucknium:monero.social >__ I'm stepping down from the MAGIC Monero Fund committee. All 5 seats are open in the election if anyone wants to run for it. Candidacy announcements are due December 31: https://magicgrants.org/2024/12/05/Monero-Fund-2025-Election.html     

> __< r​ucknium:monero.social >__ 3) Discussion: preventing P2P proxy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< v​tnerd:monero.social >__ hi     

> __< r​ucknium:monero.social >__ A couple people signed the ban list: https://github.com/Boog900/monero-ban-list     

> __< r​ucknium:monero.social >__ I was waiting to investigate a user-reported issue with subnet parsing on the ban list before circulating it more widely     

> __< r​ucknium:monero.social >__ sech1 just confirmed in #monero-community:monero.social  that it does work OK on a windows installation.     

> __< r​ucknium:monero.social >__ So we may be good to spread the announcement: https://gist.github.com/Rucknium/76edd249c363b9ecf2517db4fab42e88     

> __< r​ucknium:monero.social >__ And SethForPrivacy added the ban list to their monerod Docker image.     

> __< r​ucknium:monero.social >__ I'll contact MoneroNodo, too.     

> __< r​ucknium:monero.social >__ Anything else on this agenda item?     

> __< rbrunner >__ Anyway, if the Windows error is tricky and for example only occurs with some configured languages, you will only ever find out by spreading the list widely     

> __< r​ucknium:monero.social >__ Do we have any other items anyone wants to bring up before the post-quantum discussion?     

> __< r​ucknium:monero.social >__ Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography https://github.com/monero-project/research-lab/issues/131     

> __< r​ucknium:monero.social >__ SyntheticBird: ^     

> __< s​yntheticbird:monero.social >__ right on schedule     

> __< s​yntheticbird:monero.social >__ hello     

> __< s​yntheticbird:monero.social >__ sorry for being late     

> __< s​yntheticbird:monero.social >__ So yeah I made this issue because I did realize that deanonymization of monero is inevitable as everyone knows it but actually it is still coming in a few years, precious years that can be harvested now, decrypt later, or used for our users to delete their data that could link their transactions graph to a specific account/personal data     

> __< r​ucknium:monero.social >__ In my opinion, if priorities had to be chosen, I would choose to prevent counterfeiting before preventing privacy attacks.     

> __< a​rticmine:monero.social >__ There are elements of the Google announcement especially the error reduction that supports the shorter worst case timeframe     

> __< rbrunner >__ Just a little info where I stand regarding "while most optimistic scenarios expect it to happen in ~10-25 years". Personally I don't believe that. I see at least a 50/50 chance that QC will never work as feared.     

> __< r​ucknium:monero.social >__ Here's my hypothesized threat model: For the first few years of a quantum breakthrough, there will be a few computers and an adversary won't be able to attack everything all at once. To achieve meaningful de-anonymization, the adversary would have to attack a large number of Monero keys. To attack Monero through counterfeiting, the adversary has to counterfiet just once. I don't k<clipped message     

> __< r​ucknium:monero.social >__ now the relative difficulty of attacking one compared to the other     

> __< rbrunner >__ Achieving error correction is certainly nice and interesting, but you still need many, many more qubits. There's the rub, IMHO.     

> __< s​yntheticbird:monero.social >__ rbrunner yes. Google have only 105 qbuits but Atom computing for example have a 1000 qubit prototype that is beraly usable because of error correction     

> __< s​yntheticbird:monero.social >__ barely*     

> __< a​rticmine:monero.social >__ If error reduction improves with the number of qubits l would be concerned     

> __< r​ucknium:monero.social >__ And preventing counterfeiting has political issues. It could be good to start the discussion now. I mean "political" as an economist would call it "distributional". Potential winners and losers. Losers could be users who don't move their coins for years, then are preventing from spending their pre-QC-resistant coins.     

> __< rbrunner >__ Well, it does in that Google breakthrough, but we are many years into QC prototypes, and still only 100 or so qubits.     

> __< j​effro256:monero.social >__ This is why Carrot should encode switch commitments now IMO     

> __< r​ucknium:monero.social >__ And possibly including a discussion of a transaprent turnstile that coins must pass through     

> __< c​haser:monero.social >__ jeffro256: absolutely.     

> __< r​ucknium:monero.social >__ jeffro256: Could you explain what steps would need to be taken to bring that to mainnet?     

> __< j​effro256:monero.social >__ Simply change the Carrot blinding factor derivation from a hash of some values X, to a hash of an el gamal commitment, which has a blinding factor as a hash of some values X     

> __< j​effro256:monero.social >__ It would be pretty simple     

> __< a​rticmine:monero.social >__ Cost?     

> __< rbrunner >__ I think you mentioned last week that the byte size growth for that is reasonable?     

> __< j​effro256:monero.social >__ The byte size growth is 0     

> __< r​ucknium:monero.social >__ But what review of the mathematics and/or code would be required?     

> __< j​effro256:monero.social >__ The scanning time would go up a couple fractions of a percent     

> __< a​rticmine:monero.social >__ So this is an example of low hanging fruit     

> __< r​ucknium:monero.social >__ Would that mean that a blockchain observer would be able to tell if a tx was made with a Carrot or legacy address? Is that already the case without switch commitments?     

> __< j​effro256:monero.social >__ I think a security proof that the blinding factor brings the same hiding properties as defined already in Carrot would be pretty straight forward since scalar-point multiplication is a 1-to-1 function if the scalar is reduced and the point is of prime order     

> __< j​effro256:monero.social >__ Then we would just double-check that the el gamal commitment is well formed     

> __< j​berman:monero.social >__ Sorry I'm late, mixed up timing. My update: continuing faster FCMP++ tree build, implementing faster torsion checking from kayabanerve's implementation     

> __< rbrunner >__ And explained in one or two sentences, what whould this buy us? Some method to "evacuate" transactions into QC resistant lands in the future?     

> __< j​effro256:monero.social >__ Exactly     

> __< rbrunner >__ And without this "stuff" that's not possible then?     

> __< j​effro256:monero.social >__ El gamal commitments have the property that they are "perfectly binding", which means that not even a quantum computer can fake opening them     

> __< r​ucknium:monero.social >__ IIRC last meeting you said that a revealed switch commitment would create transparent amounts. Is it possible to keep the amount confidential in a smooth transition to post-QC if some more math/code is developed? Is the switch commitment mostly a prep for an emergency QC breakthrough?     

> __< rbrunner >__ Ah, ok, it's about faking     

> __< j​effro256:monero.social >__ The reason we don't use them is that they are 2x bigger, and would retroactively reveal the amount to quantum computers in the future     

> __< r​ucknium:monero.social >__ Just to QC? Or to any blockchain observer if they are "activated"?     

> __< rbrunner >__ I am bit confused. If those el gamal commitments are 2 times bigger, and we start to use them, how does the bytesize of a tx not grow?     

> __< j​effro256:monero.social >__ It depends on how we do it, but confidentiality probably wouldn't work since AFAIK, range proofs on El gamal commitments rely on the hardness of the discrete log problem, which are assuming doesn't exist anymore if we're activating switch commitments     

> __< r​ucknium:monero.social >__ How could a turnstile work with this setup, to make sure that the total supply of XMR was not affected by a hidden QC attack? Or some other method that had the same effect as a turnstile?     

> __< j​effro256:monero.social >__ rbrunner: great question. We set the blinding factor in the Pederson commitment to a hash an the el gamal commitment with the same amount value. QCs can't reverse hashes and thus for a given commitment C, and arbitary amount a, can't find blinding factor z, such that C = a H + z G and z = Hn(some el gamal commitment)     

> __< c​haser:monero.social >__ rbrunner: IMHO "evacuation" isn't the right description. IIUC what it enables is flipping a switch in a fork, which, from the moment of activation (but not any time before) prevents a potential quantum adversary from counterfeiting, but will reveal amounts of transactions made after the activation. it doesn't allow you to detect or roll back any previous counterfeiting.     

> __< j​effro256:monero.social >__ Here's a pretty decent article about switch commitments: https://docs.grin.mw/wiki/miscellaneous/switch-commitments/     

> __< j​effro256:monero.social >__ This is correct     

> __< c​haser:monero.social >__ a turnstile would in this context would mean whoever moves their coins "last" (=before the counter on the turnstile is exhausted) loses their money. you can bet the QC attacker will move first.     

> __< rbrunner >__ Hmm, if it's about transactions made after that special hardfork, why do we start to use this scheme already today?     

> __< c​haser:monero.social >__ as I currently understand, I don't think this is enforceable in good faith.     

> __< j​effro256:monero.social >__ So the turnstile would only work to verify that the new transaction output pool was funded by for inputs which 1) use el gamal commitments, and 2) actively prove on those el gamal commitments. Inflation can still occur if we allow new pre-QC outputs to be created with an immediate proof     

> __< r​ucknium:monero.social >__ The absence of move by a QC attacker means that the supply was not compromised. If the QC attacker moves first, then it's known that the supply was compromised and the system is destroyed. Better to know the system is destroyed     

> __< rbrunner >__ Is there also a good general article about those "turnstiles" somewhere? I think I am lacking in conceptual understanding here.     

> __< j​effro256:monero.social >__ rbrunner: we start today because the commitments we make today have to be constructed according to a special rule that allows us to reveal that we committed to an el gamal commitment when constructing our Pederson commitments     

> __< c​haser:monero.social >__ Rucknium: good point.     

> __< j​effro256:monero.social >__ Otherwise, there is no way to retroactively prove that inflation didn't happen     

> __< r​ucknium:monero.social >__ Zcash has them for its shielded pools. IIRC, Zcash implemented them after they realized the supply in one of their shielded pools could have been counterfeited.     

> __< rbrunner >__ That probably was a "Oh sh*it" moment ...     

> __< rbrunner >__ So that retroactive proof is the thing we are after with starting as soon as possible     

> __< r​ucknium:monero.social >__ https://electriccoin.co/blog/zcash-counterfeiting-vulnerability-successfully-remediated     

> __< j​effro256:monero.social >__ Also, a quantum computer cannot "move first" if make the commitments switch commitments, since they do not know the correct opening of the amount commitment, and it would take about (256-64)/2 bits of brute forcing to find a valid opening for *any* amount     

> __< j​effro256:monero.social >__ Well they move first and inflate the whole supply, but they couldn't compete for a specific output     

> __< j​effro256:monero.social >__ And it depends on how fast they can compute versus how fast everyone else can move their coins off     

> __< c​haser:monero.social >__ I meant "move first" as in 1) counterfeit now (before the chain is upgraded to switch commitments), then 2) go to the turnstile as soon as that becomes part of consensus.     

> __< rbrunner >__ "counterfeit now" needs a QC I would guess?     

> __< j​effro256:monero.social >__ Oh yeah, if we activate the switch after the first counterfeited output, then the turnstile is all for naught     

> __< r​ucknium:monero.social >__ rbrunner: https://electriccoin.co/blog/turnstile-enforcement-against-counterfeiting/     

> __< rbrunner >__ Thanks!     

> __< rbrunner >__ And as *now* there are no working QC to counterfeit, we are still ready in time?     

> __< c​haser:monero.social >__ as I love this specific blog for from Zcash/ECC so much, I have to point out that their claim to be able to somehow detect whether inflation took place before the fix is wholly unproven and they refused to show any proof of it.     

> __< rbrunner >__ Really :)     

> __< r​ucknium:monero.social >__ > If a counterfeiting compromise generated illegitimate ZEC within a shielded value pool and more ZEC exited the pool than entered, then the publicly tracked value pool total would become negative.     

> __< c​haser:monero.social >__ rbrunner: there is no way to know, and maybe there will never be. all we can do is move ASAP.     

> __< r​ucknium:monero.social >__ For Monero, this would be if more XMR tried to crossed the turnstile than the legitimate supply, the turnstile would prevent that.     

> __< rbrunner >__ chaser: Yeah, if it's not prohibitively expensive     

> __< rbrunner >__ Which right now doesn't look so, if I understand jeffro256 correctly     

> __< r​ucknium:monero.social >__ And the attempt should show that someone did counterfeit XMR somehow. But the turnstile would prevent more than the legitimate supply from existing on the other side of the turnstile. Legitimate XMR by users who did not move "in time" would be lost to those users     

> __< c​haser:monero.social >__ Rucknium: true, but that's only if/when enough people wake up and start to move coins and the attacker is smart. my comment concerned this part, about present analysis: "The Zcash Company studied the blockchain for evidence of exploitation: An attack might leave a specific kind of footprint. We found no such footprint."     

> __< rbrunner >__ Well, if you counterfeit, why not millions of coins at once?     

> __< rbrunner >__ In a few transactions or so     

> __< c​haser:monero.social >__ rbrunner: to not kill your golden goose.     

> __< rbrunner >__ Counting on everybody being able to scam staying resonable?     

> __< rbrunner >__ "Some people just want to see the world burn" comes to mind     

> __< s​yntheticbird:monero.social >__ unironically the reason cold war didn't transformed into ww3     

> __< rbrunner >__ Yes, but access to atomic bombs was pretty limited. With QCs available that may not be the case.     

> __< r​ucknium:monero.social >__ In the context we are discussing, you need a quantum computer, not just knowledge of a math exploit.     

> __< v​tnerd:monero.social >__ any privacy concerns related to the turnstile? I guess its better than having no technique for confirming inflation, but the problem is that in the end all you can do is block people at the turnstile or declare monero dead     

> __< rbrunner >__ If we can get those switch commitments in in a year's time or so, I can take the risk / probability of QCs appearing in that short timeframe     

> __< c​haser:monero.social >__ rbrunner: world burners exist, and a single one could blow up such a potential balance. I can't prove or disprove it, only say that a situation where that doesn't happen is possible.     

> __< rbrunner >__ I see     

> __< c​haser:monero.social >__ vtnerd: assuming FCMP++, the specific amounts could still reveal identifying info.     

> __< r​ucknium:monero.social >__ AFAIK, with a turnstile an observer would see that a specific turnstile tx had a certain XMR amount, but without rings, there is very little info for an adversary to get about the tx graph or any info before or after the turnstile     

> __< v​tnerd:monero.social >__ thats what I mean, you have to reveal at the turnstile, no?     

> __< j​effro256:monero.social >__ Realistically, we would probably have to downgrade the privacy of turnstile transactions to that of BTC (with stelath addresses): so no amount privacy and no sender privacy. This is because our current FCMP++ unspentness and ownership proofs rely on the DLOG problem, so we will need new sender proofs basically     

> __< s​gp_:monero.social >__ There are serious privacy risks, but when compared to the alternative of a possibly counterfeit supply, the risks might be outweighed by the advantages. Zcash made the decision that the advantages of the turnstile were worth it. For Monero, sacrificing privacy will be even greater risk     

> __< s​gp_:monero.social >__ A turnstile is arguably an emergency option     

> __< c​haser:monero.social >__ vtnerd: you could gain some limited obscurity via multiple inputs, if you have them in the specific account you're transacting from.     

> __< rbrunner >__ That is kind of nice, because as I mentioned I don't really "believe" in QCs yet ...     

> __< v​tnerd:monero.social >__ they’ve primarily been a “money hole” so far     

> __< rbrunner >__ A realistically priced emergency option that we might never need. What is there not to like?     

> __< r​ucknium:monero.social >__ jeffro256: Is that a downgrade to the privacy of the "one" entry turnstile tx, or all txs after the turnstile, i.e. all post-QC-secure txs?     

> __< rbrunner >__ Better than starting to use "post-QC-crypto" that verifies 10 times slower and blows up transaction size 10 times     

> __< j​effro256:monero.social >__ Just the turnstile transactions     

> __< rbrunner >__ At least with current "state of the art"     

> __< r​ucknium:monero.social >__ Yes, switch commitments seem like a good compromise. IIRC, MRL has discussed them years ago, too.     

> __< s​gp_:monero.social >__ Yes, the idea was circulating years and years ago, though never acted upon     

> __< rbrunner >__ And then we already had quite spectacular breaches of some of those post QC themes mere months after they were proposed. Slendid.     

> __< rbrunner >__ *post QC schemes     

> __< rbrunner >__ The cure might be worse than the desease here :)     

> __< rbrunner >__ I get that those el gamal commitments are well understood and rock solid. They do what they claim, so to say?     

> __< s​yntheticbird:monero.social >__ rbrunner Nist standardized algorithms seems to be in good course at the moment     

> __< rbrunner >__ Yeah, I was remembering some candidates flopping, not the victors     

> __< r​ucknium:monero.social >__ Before we end, I'll announce that I don't intend to post an MRL agenda or chair a meeting for Wednesday, December 25. But people can choose to meet if they want :)     

> __< c​haser:monero.social >__ rbrunner: yes, this is why Bernstein has been advocating for some king of hybrid (encapsulated?) approach to fend off the risk of new primitives, but I'm not sure how much progress was made into that direction.     

> __< r​ucknium:monero.social >__ escapethe3ra: ^     

> __< c​haser:monero.social >__ *kind     

> __< j​effro256:monero.social >__ I will say that NIST/NSA has a history of pushing unsafe crypto specifically to weaken real-world systems. We should always keep this in the back of heads when considering post-quantum cryptography hype     

> __< rbrunner >__ Well said. And it's so terribly early with all that stuff, if we go for something there, you can be sure we will look like dinasaurs after some better stuff appears     

> __< c​haser:monero.social >__ I'm arguably nowhere to be able to judge the NIST post-quantum standardization process professionally myself, but the fact that Daniel Bernstein found it concerning does concern me, given that half of our current asymmetric crypto came from him.     

> __< v​tnerd:monero.social >__ lol you put one backdoor in random number generator algorithm, and suddenly no one trusts you ever again. What a fail     

> __< s​yntheticbird:monero.social >__ I agree, I just assume this uncertainty is what put many reviews from independent researchers upon the NIST standardization process.     

> __< a​rticmine:monero.social >__ Do we have a rough idea of the cost of the post quantum cryptography in terms of tx size and verification time?     

> __< c​haser:monero.social >__ ArticMine: may be outdated, but yes: https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a#5-post-quantum-signature-algorithms     

> __< c​haser:monero.social >__ (unrelated easter egg: the gist says "last active last week", and I'm not sure what that means, given that tevador has been away for months, and no comments have been posted under it recently either)     

> __< r​ucknium:monero.social >__ Maybe someone starred it in the last week     

> __< s​yntheticbird:monero.social >__ I wasn't planning on asking the question but I was asking myself, is tevador ok? I haven't seen activity of him since a while     

> __< j​berman:monero.social >__ Fwiw I would be for switch commitments in Carrot v1, I think it's a sound strategy toward mitigating the worst outcome of hidden inflation at low cost     

> __< c​haser:monero.social >__ SyntheticBird: I don't know, and I don't know anyone who claims to know. personally, makes me worried something's up with them.     

> __< j​berman:monero.social >__ Hoping tevador is ok too. I think he's been afk for long periods of time in the past too     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< c​haser:monero.social >__ thank you all!     

> __< a​rticmine:monero.social >__ Thanks     

> __< s​yntheticbird:monero.social >__ thanks     

> __< j​effro256:monero.social >__ Okay I will begin the Carrot modifications now, should only take a couple days     

> __< j​effro256:monero.social >__ We can rollback if it's not popular     

> __< rbrunner >__ What I find the most worrysome about all that QC stuff is this: Many people seem to be damned sure about the capabilities that they will have     

> __< rbrunner >__ How can you be sure? QCs cannot crack hashes? How do you know? Are you sure they won't have very different capabilities that people now see in their crystal balls?     

> __< rbrunner >__ Can you *prove* in any way that this universe allows no "computer" whatsoever to crack hashes?     

> __< rbrunner >__ Because of information loss maybe?     

> __< sech1 >__ you can't reverse a hash (find THE data that was hashed), but you can find A data that gives the same hash     

> __< sech1 >__ but if you have some extra information (i.e. the data was a readable text of a certain length), and unlimited compute power, then you can probably find it     

> __< j​effro256:monero.social >__ That's actually an open question in mathematics in general. Us humans have come up with this notion called a "random oracle", an entity which returns a perfectly random, chaotic, yet deterministic answer when given an input. This is what hash functions are designed to emulate. We can prove that a lot of cryptography is safe if these entities exist, but no one has yet been able to <clipped messag     

> __< j​effro256:monero.social >__ prove that you can actually model a random oracle as a hash function     

> __< rbrunner >__ You mean you just iterate through many many collisions     

> __< j​effro256:monero.social >__ On the other hand, no one has been able to formulate a place to begin to break random oracles. This isn't the case with elliptic curves, RSA, etc. There is already an algorithm which can do it, given that you can throw some part of the computation at a magical physics phenomenon and get quick answers. It's called Shor's algorithm     

> __< j​effro256:monero.social >__ So while we don't know for sure what QCs can or can't do since we haven't made them yet at a practical level, we are pretty certain if this "noise" / "error correction" issue goes away, then a QC can use Shor's algorithm to break elliptic curves     

> __< j​effro256:monero.social >__ But there's no known mathematical pathway to attack hash functions in general, though     

> __< rbrunner >__ So we don't have yet a hypothetical "If QCs can do that then hashes are broken", with only the uncertainty left whether they will or will not be able     

> __< rbrunner >__ Nobody has any idea there yet - other than sech1's bruteforcing of as many collisions as necessary, at least in simple cases     

> __< rbrunner >__ A QC being able to represent so many states simultaniously that they can represent *all* possible byte sequences up to a particular length, and hash them all in parallel ...     

> __< rbrunner >__ Just brainstorming now :)     

> __< s​yntheticbird:monero.social >__ Isn't groover's algorithm representing a threat against hashes security level <192 ?     

> __< s​yntheticbird:monero.social >__ Iirc it roughly divide the security level by to     

> __< s​yntheticbird:monero.social >__ Iirc it roughly divide the security level by two     

> __< s​yntheticbird:monero.social >__ Oh I think i'm being confused with symmetric ciphers actually     

> __< k​ayabanerve:matrix.org >__ djb claims the cube root complexity claim isn't accurate in practice: https://cr.yp.to/hash/collisioncost-20090517.pdf     

> __< k​ayabanerve:matrix.org >__ I leave no comment on if it'd still be beneficial to be so conversative or of there's more modern research restoring it.     

> __< 0​xfffc:monero.social >__ FWIW djb is extremely reliable source.     

> __< k​ayabanerve:matrix.org >__ Rucknium: This isn't specifically to you, but you noted on the topic here.     

> __< k​ayabanerve:matrix.org >__ I completely disagree. I'd prefer complete destruction of Monero as an economic unit before we had a critical privacy issue.     

> __< k​ayabanerve:matrix.org >__ The project is worthless either way. I'd rather maintain our promise of privacy and not publish everyone's transaction history.     

> __< k​ayabanerve:matrix.org >__ Switch commitments are a voluntary transition with consent of the owner.     

> __< k​ayabanerve:matrix.org >__ I am fine with a turnstile for the PQ migration though.     

> __< e​scapethe3ra:matrix.org >__ thanks for the ping, noted; I assume you'll be chairing the 18th correct?     

> __< r​ucknium:monero.social >__ escapethe3ra: Yes     



# Action History
- Created by: Rucknium | 2024-12-10T20:58:05+00:00
- Closed at: 2024-12-20T20:50:39+00:00
