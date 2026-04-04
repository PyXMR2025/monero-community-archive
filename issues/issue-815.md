---
title: Monero Research Lab Meeting - Wed 22 March 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/815
author: Rucknium
assignees: []
labels: []
created_at: '2023-03-22T00:27:02+00:00'
updated_at: '2023-03-28T21:17:28+00:00'
type: issue
status: closed
closed_at: '2023-03-28T21:17:28+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: [Consider removing the tx_extra field](https://github.com/monero-project/monero/issues/6668).

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100).

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#811 

# Discussion History
## plowsof | 2023-03-23T15:11:12+00:00
Logs 
```
17:04:35 <Rucknium[m]> I will wing it. Meeting time! https://github.com/monero-project/meta/issues/815

17:04:41 <Rucknium[m]> Say hi everyone

17:04:45 <Rucknium[m]> Hi

17:04:49 <rbrunner> Hello

17:04:59 <xmrack[m]> Hey

17:05:05 <dangerousfreedom> Hello

17:05:05 <jeffro256[m]> Howdy

17:05:33 <Rucknium[m]> Updates: What is everyone working on?

17:05:36 <hinto[m]> hello

17:07:06 <Rucknium[m]> me: have preliminary script to collect all RingCT rings. So far I have used it to check
how the P2Pool payout efficiency upgrade has improved effective ring size: https://github.com/Rucknium/misc-
research/tree/main/Monero-Effective-Ring-Size

17:07:38 <Rucknium[m]> This can be used to check the effect of Mordinals/NFTs on effective ring size if and
when I parse tx_extra for Mordinals' designated tag

17:08:03 <xmrack[m]> I’ve been working on adding k-anonymity to the monero block explorer to give users more
privacy.

17:08:40 <Rucknium[m]> isthmus has closed his work-in-progress CCS to help with computational speedup of
OSPEAD due to not enough labour bandwidth. I am seeking other forms of help now.

17:08:51 <dangerousfreedom> I'm working on the transaction_history for the seraphis_wallet which will be a
layer above the "seraphis_engine".

17:09:07 <xmrack[m]> I have it working for blocks at the moment but need to add a range search to Lmdb to
allow for transaction hashes. Hyc is helping me with that

17:09:16 <blankpage[m]> What is k-anonymity?

17:10:01 <xmrack[m]> I explain here https://github.com/moneroexamples/onion-monero-blockchain-
explorer/issues/284

17:10:21 <blankpage[m]> Thanks

17:11:02 <UkoeHB> ah crap got distracted, hi

17:11:38 <Rucknium[m]> The deadline for MoneroKon submissions is April 3rd: https://cfp.monerokon.com/2023/cfp

17:11:41 <xmrack[m]> Tl:dr instead of a user requesting a single tx hash which the block explorer can
confidently assume belongs to the requesting ip address. They will provide the first 5 characters of the hash
and the explorer will return all possible k matches. Hence, k-anonymity

17:12:31 <atomfried[m]> i just started looking into the new rangeproof a bit and try to understand it

17:12:36 <ArticMine> hi

17:12:41 <plowsof11> hi

17:13:46 <rbrunner> To use that, I will just need some HTML with a form and the necessary JavaScript to issue
to that newly k-anonymity capable block explorer?

17:13:58 <plowsof11> Rucknium: (diego is here on hand for when bp++ peer review funding is to be discussed)

17:14:10 <DiegoSalazar[m]> ye

17:14:19 <UkoeHB> my update: did a refactor of the seraphis scanning framework to better support async
backends, right now working on integrating checkpoint caches into the seraphis enote store

17:14:30 <blankpage[m]> Do any other XMR block explorers have k-anonymity? This seems like a great privacy
improvement for the general user

17:14:45 <Rucknium[m]> plowsof: IMHO, we should discuss that first since tx_extra is potentially unlimited
discussion: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358

17:14:57 <xmrack[m]> rbrunner: yea javascript will be needed, unfortunately, to filter all the data returned

17:15:28 <xmrack[m]> It should be super straightforward from the frontend perspective

17:15:52 <Alex|LocalMonero> xmrack[m]: What about the compact filters approach that Neutrino uses?

17:16:23 <rbrunner> I see, thanks

17:16:28 <UkoeHB> plowsof11: it looks like the bp++ paper is still not updated

17:16:37 <Rucknium[m]> xmrack: IMHO, timing is still an issue with 5-character hash prefix.

17:16:44 <plowsof11> after 3+ months wait - the bp++ paper has not been updated, and my lines of communication
with the author have dried up. correct UkoeHB

17:17:25 <atomfried[m]> depending on how "Range Proofs with Constant Size and Trustless Setup" performs, we
could maybe skip bp++ and just use this instead?

17:17:45 <UkoeHB> plowsof11 I thought blockstream hired him, maybe worth reaching out

17:17:52 <Rucknium[m]> You would only get about one tx per week with 5 character prefix I think. Most people
look up recent txs

17:18:23 <UkoeHB> atomfried[m]: it sounds like that new paper is missing a proper security model

17:18:47 <Rucknium[m]> I suggested that we return to the CCS after 3 months if there was no paper update. It
has been three months

17:18:54 <UkoeHB> ah

17:19:20 <atomfried[m]> UkoeHB: yes, thats not included in the paper, maybe it was not in the paper due to a
pagelimit

17:19:49 <xmrack[m]> Rucknium: timing data should have no effect on this. All data is sent to the client, then
the client loops through the data and pulls out the block/tx they want

17:20:14 <blankpage[m]> The authors of the constant size rangeproofs (needs a shorter name!) will be at the
meeting next week yes?

17:21:17 <xmrack[m]> The 5 character prefix is subject to change. I need to run benchmarks to see what
acceptable bandwidth looks like

17:21:27 <plowsof11> move bp++ peer review to funding as is vote? or

17:21:27 <Rucknium[m]> blankpage: Good point. Maybe the next step will be clearer once we discuss that paper
with the authors

17:21:59 <blankpage[m]> For example we could ask "do you have a security model?"

17:22:14 <xmrack[m]> blankpage: yes they mentioned they were busy today but will be here to answer questions
next week

17:22:17 <rbrunner> Do we know how far vtnerd is with their BP++ implementation already?

17:22:43 <ofrnxmr[m]> move bp++ peer review to funding as is vote? or wait for next week after constand sized
range proofs meetings?

17:23:23 <rbrunner> Paper authors sort of vanishing make me a bit nervious ...

17:24:13 <blankpage[m]> Or the CCS is rewritten as "research, implement & audit next generation range proofs"
so that it covers b++ and/or the new thing

17:24:13 <ofrnxmr[m]> (Putting up for funding leaves time to raise the money so we are ready when/if. Can
always repurpose the funds for alternative solution)

17:24:24 <plowsof11> i think its a simple case of : he is now employed / busy on other things, i can make a
last attempt to contact blockstream before next weeks meeting?

17:25:28 <Rucknium[m]> Blockstream's focus is BTC. They probably don't particularly want to help Monero FWIW

17:25:53 <plowsof11> i have this feeling too

17:26:00 <ofrnxmr[m]> blankpage:  sounds good to me - anybody against?

17:26:39 <blankpage[m]> xmrack I guess the consideration is whether the block explorer has a powerful
heuristic by guessing that the intended query is the most recent of the returned set of k.

17:26:42 <rbrunner> Don't have clear and focussed CCS a better resonance than such "this or maybe this"?

17:26:44 <Rucknium[m]> I would not be in favor of a CCS that is so vague on what the task is and who would
accomplish it

17:27:41 <rbrunner> Usually it does not take long to fund a CCS, I would say. We probably won't bump against a
wait of, say, a month or so.

17:28:06 <blankpage[m]> Considering the "open ended" nature of this stuff, is MAGIC maybe a better fit?

17:28:46 <rbrunner> Well, it's only open ended if we don't bring with us the patience to wait until we have a
clear direction :)

17:29:04 <Alex|LocalMonero> xmrack: the problem you're trying to solve is known as "private information
retrieval", or PIR, and it's been around for a while. You need homomorphic encryption to make a block explorer
that truly knows nothing about what the client is asking for. Such an explorer exists for Bitcoin in an
experimental state: https://btc.usespiral.com/ I know the developers and can get you in touch with them so
that you can make a similar

17:29:04 <Alex|LocalMonero> one for XMR.

17:29:25 <blankpage[m]> Blockstream uses rangeproofs BTW for confidential amounts on their "liquid network".
Idk if they are jumping into this new rangeproof though.

17:29:32 <ofrnxmr[m]> rbrunner:  has nothing to do with patience

17:29:33 <xmrack[m]> blankpage: ahhhh I see, I thought you meant side channel timing data like packet times.
Guess newest heuristic could be true especially singe I will need to scan the mempool. I will work with
Rucknium to figure it out

17:29:39 <Alex|LocalMonero> It uses lattice-based cryptography.

17:29:46 <xmrack[m]> *since

17:30:09 <plowsof11> rewrite the ccs = back to the drawing table for quotes from multiple companies

17:30:21 <ofrnxmr[m]> So for now plowsof @plowsof:matrix.org:  sounds like do nothing

17:30:36 <xmrack[m]> Alex | LocalMonero | AgoraDesk: sounds interesting

17:30:46 <atomfried[m]> Alex|LocalMonero: could this also work for light wallets?

17:31:25 <Alex|LocalMonero> atomfried[m]: Probably but it's way more complex due to homomorphic encryption
constraints.

17:31:27 <Rucknium[m]> IMHO, more programmer-cryptographers like koe and kayabanerve should give opinions
about what to do about the BP++ paper

17:31:40 <Rucknium[m]> And wait for the new rangeproof paper authors next week

17:32:25 <Alex|LocalMonero> xmrack[m]: https://eprint.iacr.org/2022/368

17:32:34 <kayabanerve[m]> 👋

17:33:07 <Alex|LocalMonero> Homomorphic encryption allows you to perform operations on encrypted data without
decrypting it. Such as checking an address for txs.

17:33:21 <kayabanerve[m]> Just finished reading up

17:33:36 <Alex|LocalMonero> The downside is that its very space-inefficient nowadays.

17:33:42 <plowsof11> sounds good, we can TBD next week, thanks for attending Diego Salazar

17:33:50 <DiegoSalazar[m]> ye

17:33:52 <Rucknium[m]> Homomorphic encryption is quite bleeding edge AFAIK...meaning users may get cut

17:33:59 <kayabanerve[m]> BP++ is beyond me. I can't encourage deployment without review from people its not.

17:34:57 <Alex|LocalMonero> Rucknium[m]: PIR block explorers are probably the least dangerous production
battleground to test this tech out.

17:34:57 <kayabanerve[m]> My one candidate is sarang. I would hold off until this constant time proof has an
initial eval. That means source access + benchmarking + a security proof.

17:35:13 <Rucknium[m]> Alex | LocalMonero | AgoraDesk: You're probably right.

17:35:18 <kayabanerve[m]> Currently, I believe the authors didn't make a CSRP sec proof. I have heard
commentary the applicability is a bit... Hand waved.

17:35:44 <kayabanerve[m]> I look forward to hearing more from the authors on the matter. They didn't respond
to me, yet someone else. I believe they'll be here next week?

17:35:46 <Alex|LocalMonero> xmrack: https://github.com/ahenzinger/simplepir is currently the fastest PIR
server I know.

17:35:50 <Rucknium[m]> I don't think BP++ has a security proof either. Does it?

17:36:23 <kayabanerve[m]> If CSRP doesn't have a sec proof, I'd move forward with BP++.

17:36:56 <kayabanerve[m]> I believe ++ has a proof, yet also a TODO somewhere in the paper?

17:37:27 <kayabanerve[m]> I don't believe that TODO is relevant to us but I can double check now.

17:38:05 <UkoeHB> yeah might as well stop waiting on BP++

17:38:06 <kayabanerve[m]> TBC, without a publication for and proof of CSRP, it's interesting but a non
starter.

17:38:55 <kayabanerve[m]> I'm willing to wait a week to hear back from the CSRP authors, as I do believe
they're interested in attending next week's meeting...

17:39:20 <Rucknium[m]> kayabanerve: Thanks for your input

17:40:19 <plowsof11> the peer review is step 1 of <many> , entire project is being delayed imo

17:40:52 <kayabanerve[m]> BP++, 8.1, proving and verification time is incomplete. 9, proofs, is not.

17:44:27 <kayabanerve[m]> xmrack: Are they trying to attend the meeting next week?

17:44:45 <xmrack[m]> Yes

17:45:15 <kayabanerve[m]> Just triple checking :)

17:45:29 <kayabanerve[m]> I'd call to hold off on any decisions until after then.

17:45:43 <kayabanerve[m]> But BP++ should be moved forward with.

17:46:09 <Rucknium[m]> kayabanerve: "moved forward with"?

17:46:15 <kayabanerve[m]> And while I don't want to force a topic change, I do have a question for tevador of
larger interest.

17:46:44 <kayabanerve[m]> Rucknium: There's no reason to hold off on it currently, other than potential
greater interest in this constant sized proof.

17:47:02 <DataHoarder> xmrack[m]: Ideas for doing k-anonymity client side without JS, use fragment hash CSS
styling of page via targeting https://stackoverflow.com/questions/36552784/change-the-style-of-an-element-if-
the-fragment-identifier-hash-in-the-url-refe but the hard part would be sending the user to the proper page
(maybe abuse max length on fields) JavaScript

17:47:02 <DataHoarder> could be needed to redirect user to results page, but not on the filtering part. Maybe
good for linking to the page by other places

17:47:13 <kayabanerve[m]> If the CSRP becomes a non-factor, we should conduct peer review on it.

17:48:12 <Rucknium[m]> kayabanerve: Go ahead and change topics

17:49:37 <kayabanerve[m]> tevador: I don't believe an indirect curve cycle is possible due to the fact we need
to do an ECC op *and* membership. Do you have any thoughts on this?

17:50:36 <kayabanerve[m]> To be clear, the proof needs to substract the blinding factor, then prove the
unblinded point is a member. tevador found an efficient indirect cycle, letting us stay on Ed25519, but the
indirect cycle *can't* do ECC ops unless it rebuilds a calculator on the arithmetic level.

17:50:44 <kayabanerve[m]> *binary level

17:50:50 <kayabanerve[m]> Completely infeasible

17:51:50 <kayabanerve[m]> So that means we'd need to do ECC ops on the tower, and then use that unblinded
point on the cycle. I'm unsure we can efficiently do that since we have to maintain ZK.

17:52:26 <kayabanerve[m]> We can trivially prove the ECC op on the tower, get the output point, and move that
to the cycle. It just wouldn't be ZK.

17:53:13 <kayabanerve[m]> ... It may be possible with a Pedersen commitment? And then we'd have to prove two
EC ops on the tower and open the commitment in the cycle?

17:54:05 <kayabanerve[m]> Anyways. I wanted to get tevador's thoughts in this and if I wasn't missing
anything, move the discussion back to switching curves, despite the potential avoidance noted by tevador.

18:01:03 <kayabanerve[m]> ... Doesn't seem like we'll get a response this meeting 😅 My thoughts/updates on the
SNARK design discussion have been made available. I don't have anything else to say as part of it right now :)
Thanks for the opportunity Rucknium:

18:03:06 <Rucknium[m]> Meeting is over :)


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-03-22T00:27:02+00:00
- Closed at: 2023-03-28T21:17:28+00:00
