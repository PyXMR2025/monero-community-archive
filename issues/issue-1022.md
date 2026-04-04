---
title: Monero Research Lab Meeting - Wed 12 June 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1022
author: Rucknium
assignees: []
labels: []
created_at: '2024-06-11T22:28:10+00:00'
updated_at: '2024-06-21T19:23:51+00:00'
type: issue
status: closed
closed_at: '2024-06-21T19:23:51+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

5. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1020

# Discussion History
## Rucknium | 2024-06-12T23:53:31+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1022     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< x​mrack:monero.social >__ Hi     

> __< a​rticmine:monero.social >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< v​tnerd:monero.social >__ Hi     

> __< spackle >__ hello     

> __< rbrunner >__ Hello     

> __< j​effro256:monero.social >__ Howdy     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< j​berman:monero.social >__ Continuing fcmp tree work, continuing the trim algorithm     

> __< s​yntheticbird:monero.social >__ Hi     

> __< x​mrack:monero.social >__ Starting work on stressnet     

> __< s​yntheticbird:monero.social >__ I've been working on a proposal for traffic pattern obfuscation and mitigation against automated firewall active probing. Tho I have received concern over the complexity of such mitigation than I'm trying to address     

> __< v​tnerd:monero.social >__ Me: still stress testing the LWS remote scan feature, and found some bugs in the process     

> __< a​rticmine:monero.social >__ Continuing work on scaling after my presentation at MoneroKon     

> __< r​ucknium:monero.social >__ me: Helping set up the stressnet. Started on a simple Shiny app for visualizing the fee/ring size tradeoff for black marble defense, suggested by xmrack . I made by MoneroKon presentation "Hard Data on Banking the Unbanked", but I submitted it way too late, so it will be a presentation for Monerotopia in November 😅     

> __< spackle >__ misc. stressnet tasks     

> __< r​ucknium:monero.social >__ xmrack: Do we have Emanuele here?     

> __< r​ucknium:monero.social >__ Thanks for contacting them     

> __< x​mrack:monero.social >__ Im not sure. I could ping him over email     

> __< r​ucknium:monero.social >__ I didn't see any new people joining the Matrix room. If he shows up later in the meeting, we can have the agenda item then     

> __< r​ucknium:monero.social >__ 3) Stress testing `monerod` https://github.com/monero-project/monero/issues/9348     

> __< spackle >__ The stressnet release is published: https://github.com/spackle-xmr/monero/releases/tag/v250.18.3.3.1     

> __< spackle >__ Everything is running smoothly with 9 nodes at the last count, and flooding wallets are prepared. Public announcement is set for tomorrow; stressing begins 15:00 UTC June 19th. In short, the stage has been set.     

> __< x​mrack:monero.social >__ Rucknium: did you want to share the Shiny app or are you working on it more?     

> __< r​ucknium:monero.social >__ We have a stressnet block explorer running: http://explorer.stressnet.net:8081     

> __< r​ucknium:monero.social >__ xmrack: Not sure. I may share in the next agenda item     

> __< rbrunner >__ Fantastic progress.     

> __< s​yntheticbird:monero.social >__ Have the stressnet nodes already caused system crash or memory exhaustion yet on some host ?     

> __< r​ucknium:monero.social >__ The SSL cert for https will be added soon. We have an onion hidden service too: http://xmrstrss5d6fii5mku5glfxp3g73unofae2yh4cndfxgvbexbifhguyd.onion/     

> __< r​ucknium:monero.social >__ You can see in the block explorer that we are not stressing the network right now     

> __< spackle >__ I have observed excessive memory use on a test machine, up to 71.7GB for one instance of monerod     

> __< r​ucknium:monero.social >__ spackle had very high RAM usage on the node that was receiving the spam for the wallet, recently     

> __< spackle >__ The machine had 128GB RAM available, so no OOM crash occurred.     

> __< r​ucknium:monero.social >__ I mean spam _from_ the wallet     

> __< r​ucknium:monero.social >__ Anyone is welcome to join the stressnet. It may take more than 24 hours for initial sync. Here are instructions: https://github.com/spackle-xmr/monero/blob/master/README.md     

> __< j​effro256:monero.social >__ Me: finishing first draft of Jamtis-RCT library     

> __< r​ucknium:monero.social >__ Right now I am working on saving and displaying ephemeral data for the stressnet like txpool size, RAM and CPPU usage, peer connection data, etc.     

> __< r​ucknium:monero.social >__ Thanks again to selsta and plowsof for helping with the release binaries workflow on GitHub.     

> __< a​rticmine:monero.social >__ When considering CPU usage is this per thread?     

> __< r​ucknium:monero.social >__ I have just made code to save the CPU and MEM output of `top` for monerod     

> __< r​ucknium:monero.social >__ Maybe there is a way to get more detail.     

> __< r​ucknium:monero.social >__ AFAIK we will set log levels and categories for different nodes to capture some types of data, too. We don't know exactly what will be useful. 0xfffc  will help decide that.     

> __< a​rticmine:monero.social >__ It is a good start. Thread count and CPU specs will be very helpful.     

> __< s​yntheticbird:monero.social >__ Rucknium tho harder you'll likely find more and accurate informations in `/proc/PID` directory     

> __< r​ucknium:monero.social >__ Thanks. I will try to get info from there.     

> __< r​ucknium:monero.social >__ More comments or questions on stressnet?     

> __< r​ucknium:monero.social >__ 4) Potential measures against a black marble attack. https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ I have an extremely basic Shiny app that reproduces the table and plot from my paper: https://black-marble-defense-params.redteam.cash/     

> __< a​rticmine:monero.social >__ My one comment on this is that the next changes to scaling will likely include a reduction of the ML surge factor from 50 to 16. When combined with the full ratio of the current penalty free zone this effectively places hard and soft limits on black marble.     

> __< r​ucknium:monero.social >__ The paper is https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-optimal-fee-ring-size.pdf     

> __< r​ucknium:monero.social >__ You can change the parameters in the Shiny app. Then the server will recompute the plot and add the solution to the table.     

> __< x​mrack:monero.social >__ I need to leave but emanuele is having issues making a monero.social account. He’s actively trying to join     

> __< j​effro256:monero.social >__ What kind of issues ?     

> __< c​haser:monero.social >__ this is very useful, thanks!     

> __< j​effro256:monero.social >__ ArticMine: do you have a formal analysis of how decreasing the surge factor limits how much damage a short term attacker can do with black marble flooding? I know the general idea is that reducing the surge factor to something comparable to the ring size will make "drive by" black marbling less effective     

> __< r​ucknium:monero.social >__ I am going to add the two other solution types I discussed last meeting and add explanatory text     

> __< a​rticmine:monero.social >__ I can do this     

> __< j​effro256:monero.social >__ Nice! It would be nice to see actual numbers, especially for full decoy removal     

> __< r​ucknium:monero.social >__ Maybe we can combine my analysis with the surge factor analysis     

> __< a​rticmine:monero.social >__ Yes     

> __< r​ucknium:monero.social >__ I think we got emsczkp     

> __< r​ucknium:monero.social >__ Ok we will finish discussion of this agenda item, then put emsczkp  next     

> __< s​yntheticbird:monero.social >__ be aware emsczkp is on matrix.org     

> __< s​omeoneelse495495:matrix.org >__ emsczkp Please follow meetings on monerologs.net. There are federation issues between monero.social and matrix.org. You'll likely be unable to see messages from the meeting in real time     

> __< r​ucknium:monero.social >__ Ok. He will have to look at https://libera.monerologs.net/monero-research-lab/20240612     

> __< e​msczkp:matrix.org >__ Ok thanks, i will try     

> __< j​effro256:monero.social >__ Welcome     

> __< r​ucknium:monero.social >__ Dan Miller: Any progress figuring out what the federation issues with matrix.org are?     

> __< s​omeoneelse495495:matrix.org >__ Sorry this is a reccurent issue. Be sure participants do see your messages tho     

> __< s​omeoneelse495495:matrix.org >__ Sorry this is a reccurent issue. You can be sure participants do see your messages tho     

> __< r​ucknium:monero.social >__ is kayabanerve  / kayabanerve  here?     

> __< r​ucknium:monero.social >__ emsczkp: Welcome! Could you introduce yourself, explain your recent work, and your interest in improving the Monero protocol?     

> __< e​msczkp:matrix.org >__ so I write in this chat and view the replies here monerologs.net?     

> __< s​omeoneelse495495:matrix.org >__ Yes     

> __< s​omeoneelse495495:matrix.org >__ Don't forget to resfresh monerologs.net     

> __< e​msczkp:matrix.org >__ thanks you all, I will introduce my self and explain my research objectives     

> __< e​msczkp:matrix.org >__ I am PhD and I conducted reaserch in zero-knowledge proofs (ZKPs). In particular, I started with argument systems like Bulletproofs (BP). I experimented with BP in the public blockchain protocols, so i delved the BP as well as other trustless ZKP. From my experiments, i highlighted that BP's Inner-Product Argument (IPA) subroutine is expensive in computational terms. So i'm trying<clipped message>     

> __< e​msczkp:matrix.org >__  to reduce the computational costs of the IPA. To this end, I landed on the theory of Compressed Sigma-Protocols and tried to reconcile this theory with the IPA. My last conference shows improvements in proving and verifying costs as well as proved security in standard DLOG assumption. Now, i would like to extend this research direction in a Journal, also considering  recent advan<clipped message>     

> __< e​msczkp:matrix.org >__ cement is the field with BP+ and BP++     

> __< r​ucknium:monero.social >__ Wonderful     

> __< a​rticmine:monero.social >__ I have a question. How would this research impact the proposed FCMP in Monero.?     

> __< a​rticmine:monero.social >__ Full Chain Membership Proofs     

> __< r​ucknium:monero.social >__ The abstract of https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=221 says that the proving and verification time reduces to 1/2 of the original time, with your reearch     

> __< a​rticmine:monero.social >__ I am very excited about reductions in transaction size and verification time     

> __< e​msczkp:matrix.org >__ thank you for the question, what is FCMP exactly ?     

> __< k​ayabanerve:monero.social >__ full-chain membership proofs     

> __< r​ucknium:monero.social >__ FCMP is an adaption of Curve Trees to Monero, AFAIK     

> __< r​ucknium:monero.social >__ Basically using nested Bullletproofs to form the anonymity set of Monero instead of ring signatures     

> __< rbrunner >__ They have something like BP somewhere inside, yes? GBP or how they are called.     

> __< k​ayabanerve:monero.social >__ sorry, that was replying to emsczkp. My messages are out of order so I'm unsure that was in context     

> __< e​msczkp:matrix.org >__ The Inner-product argument is used in the Monero range proof/membership proof system, in the original BP version     

> __< j​effro256:monero.social >__ In practice for FCMPs, we were planning on using another variant of bulletproofs called "Generalized Bulletproofs" : https://github.com/simonkamp/curve-trees/blob/main/bulletproofs/generalized-bulletproofs.md     

> __< r​ucknium:monero.social >__ How much of the total BP verification time is spent on the IPA?     

> __< e​msczkp:matrix.org >__ by improving the inner-product argument, the overall system will benefit     

> __< k​ayabanerve:monero.social >__ 1) jeffro256: Please link to Aaron's specification and proofs, it's more comprehensive.     

> __< k​ayabanerve:monero.social >__ 2) We need an IPA which enables an arithmetic circuit proof which can open Pedersen Vector Commitments.     

> __< k​ayabanerve:monero.social >__ If any new IPA is proposed, if it's pure multiplicative constraints and lincombs, or even also PCs, that's insufficient unless it's ~10x faster.     

> __< k​ayabanerve:monero.social >__ I'd have to check the numbers exactly. The divisors work does get us close to efficient enough to consider a binary tree (optimal if without PVCs), yet then we'd add another few KB to the proof.     

> __< k​ayabanerve:monero.social >__ I'm opening the PDF now, I just wanted to be clear on context. if this is a 1:1 with the BP IPA statement, offering the same AC proof construction over it, I'd be quite interested.     

> __< e​msczkp:matrix.org >__ I just saw the GBP which is based on R1CS, I had no knowledge of it. We could see if my approach is applicable in the folding argument.     

> __< k​ayabanerve:monero.social >__ This seems equivalent to the BP+ IPA statement, which places the inner-product in the exponent. I'd assume we can apply the BP AC over it? I'd have to spend a few more minutes checking?     

> __< k​ayabanerve:monero.social >__ But re: range proofs, which currently use BP+, this work would presumably inherit the BP+ range proof construction (if this doesn't posit its own range proof -> IPA conversion) if it maintains the ZK property.     

> __< k​ayabanerve:monero.social >__ please, correct me if I'm wrong. I'm just starting to read through this and am stating my initial thoughts.     

> __< k​ayabanerve:monero.social >__ *This is also SHVZK.     

> __< r​ucknium:monero.social >__ xmrack said you were interesting if research funding is available. "Yes", but the process can be unconventional. There are two main ones: The Community Crowdfunding System: https://ccs.getmonero.org/ and the MAGIC Monero Fund: https://monerofund.org/     

> __< k​ayabanerve:monero.social >__ emsczkp: Can you clarify the numbers re: exponentiations? Bulletproofs doing 2n exponentiations is referring to how each round does point scalings for the intermediates?     

> __< k​ayabanerve:monero.social >__ Or are you referring to scalar exponentiations, the powers of y/z and so on?     

> __< r​ucknium:monero.social >__ We can end the official meeting time here and discussion can continue :)     

> __< e​msczkp:matrix.org >__ The statement of the Compressed Sigma-IPA is 1:1 with the BP's IPA     

> __< e​msczkp:matrix.org >__ It can be combined well with the AC proofs     

> __< k​ayabanerve:monero.social >__ The statement just prior to section 4, marked `(1)` is not. It places the c in the exponent.     

> __< k​ayabanerve:monero.social >__ Argh. I'm stupid.     

> __< k​ayabanerve:monero.social >__ Sorry, you're right. You follow describing c in the exponent and Bulletproofs immediately makes the same mutation.     

> __< k​ayabanerve:monero.social >__ That's my misunderstanding and my bad, sorry again.     

> __< k​ayabanerve:monero.social >__ *Also, you work clarifies itself as not necessarily SHVZK, which I assume means this IPA should not be considered so. Sorry, another misreading of mine. My head is two places right now.     

> __< k​ayabanerve:monero.social >__ Apologies again for the misremembering/poor initial skim. This would be usable as a replacement for the BP IPA, if correct, and facilitate faster FCMPs/range proofs (if correct there as well). My current question is on the "exponentiations" (point scalings or scalar exponentiations).     

> __< e​msczkp:matrix.org >__ In the efficiency analysis, for exponentiations i mean the multi-exponentiation for computing the new generators G and H in each folding round     

> __< k​ayabanerve:monero.social >__ Right. Bulletproofs doesn't actually incur that.     

> __< k​ayabanerve:monero.social >__ You can delay the entire multiexponentation to the end *if the verifier*.     

> __< e​msczkp:matrix.org >__ inversions are related to the operations for computing the folded vectors A and B     

> __< k​ayabanerve:monero.social >__ The per-round aspect is exclusively prover/notational.     

> __< k​ayabanerve:monero.social >__ That does still leave a faster prover, faster verifier re: no inversions, The communication is the same?     

> __< e​msczkp:matrix.org >__ we could delay also the entire multi-exp in a single multi-exp in the verifier , but this is not shown in the paper     

> __< k​ayabanerve:monero.social >__ I presumed so and wasn't trying to claim BP potentially faster, solely note the performance claims don't hold for the verifier.     

> __< k​ayabanerve:monero.social >__ (if one optimizes their impl, the claims do hold as-notated)     

> __< e​msczkp:matrix.org >__ The security of the Compressed Sigma-IPA is based on the multi-round special soundness notion, which implies the WEE     

> __< j​effro256:monero.social >__ WEE?     

> __< k​ayabanerve:monero.social >__ I actually am interested in this. I'd be happy to replace the proof in FCMPs and see how they do comparatively. If performance does end up non-negligible, we could discuss review.     

> __< k​ayabanerve:monero.social >__ witness extended emulation     

> __< e​msczkp:matrix.org >__ communication is still the same as in BP     

> __< k​ayabanerve:monero.social >__ To be extremely honest, saving... 22 inversions? Will probably end up as negligible. The faster prover time, while pleasant, isn't dominated by the IPA proof AFAIK. My guess is our usage of divisors does.     

> __< k​ayabanerve:monero.social >__ If this does end up a ms or so faster (~10%), I would love to ask for Aaron's feedback and consider schedule availability though.     

> __< k​ayabanerve:monero.social >__ Er, sorry. ~30 inversions.     

> __< e​msczkp:matrix.org >__ I will go more in detail also in FCMP because it sounds interesting to me... sorry guys but now i have to leave     

> __< e​msczkp:matrix.org >__ Thank you all for your time, i'm truly grateful to be able to contribute to monero     

> __< k​ayabanerve:monero.social >__ I do appreciate improvements and apologize if that's blunt. I am happy to consider this further on my end re: FCMPs :)     

> __< k​ayabanerve:monero.social >__ Re: range proofs, it'd add 32 bytes and may decrease verification time a bit, which BP+ also did. That may eke out a victory, especially in a batch verification content...    

# Action History
- Created by: Rucknium | 2024-06-11T22:28:10+00:00
- Closed at: 2024-06-21T19:23:51+00:00
