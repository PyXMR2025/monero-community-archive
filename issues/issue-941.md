---
title: Monero Research Lab Meeting - Wed 06 December 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/941
author: Rucknium
assignees: []
labels: []
created_at: '2023-12-06T15:27:27+00:00'
updated_at: '2023-12-17T17:15:11+00:00'
type: issue
status: closed
closed_at: '2023-12-17T17:15:11+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: How to confirm security of Monero's multisignature protocol? Do we need mathematical security proofs, and can we get them? Info:
- [Brandon Goodell and Sarang Noether (2018) "Thring Signatures and their Applications to Spender-Ambiguous Digital Currencies"](https://www.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf)
- [Monero multi-signature patch review by Inference](https://community.rino.io/rino-multisig-pr8194-audit-20220627.pdf)
- [Rust alternative implementation](https://github.com/serai-dex/serai/blob/develop/coins/monero/src/wallet/send/multisig.rs) by @kayabaNerve

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#938 

# Discussion History
## plowsof | 2023-12-17T17:03:55+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/941     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ hello     

> __< v​tnerd:monero.social >__ Hi     

> __< h​into.janaiyo:matrix.org >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< j​effro256:monero.social >__ howdy     

> __< h​into.janaiyo:matrix.org >__ me: working on misc cuprate stuff     

> __< j​effro256:monero.social >__ finished first draft of Jamtis changes     

> __< v​tnerd:monero.social >__ Me: still on beefing up LWS tests, this time working on subaddress tests. Found 4 bugs so far, so it's been worth it.     

> __< r​ucknium:monero.social >__ me: OSPEAD. And I have new data about suspected Exodus _Mobile_ txs with nonstandard fees. Exodus released a Mobile wallet fix on November 11th: https://github.com/Rucknium/misc-research/blob/main/Monero-Nonstandard-Fees/images/Exodus-Mobile-txs-after-fix-release.png     

> __< r​ucknium:monero.social >__ I'm not sure all the txs in that category are Exodus Mobile. But the number of those txs fell a lot. In total about 5% of Monero txs were using fees in that range.     

> __< r​ucknium:monero.social >__ 3) Discussion. What do we want to discuss?     

> __< rbrunner >__ A bit surprising how widespread use of Exodus seems to be     

> __< s​gp:magicgrants.org >__ hello     

> __< r​ucknium:monero.social >__ I am not surprised.     

> __< j​effro256:monero.social >__ I wanted to discuss the threat models of using multisig now for the CCS versus giving control to one entity. Multisig is still experimental in its current state. However, does the likelihood of multisig having some vulnerability that will be leveraged by one multisig signer outweight the likelihood that a singular entity with a non-multisig wallets loses the funds in a conventiona<clipped messag     

> __< j​effro256:monero.social >__ l way (getting hacked, theft, etc)?     

> __< r​ucknium:monero.social >__ Here is luigi1111's proposal: https://github.com/monero-project/meta/issues/935#issuecomment-1841052378     

> __< r​ucknium:monero.social >__ "For a longer term solution [after March 1, 2024], I do think a community multisig could work (ideally non-experimental, of course)."     

> __< r​ucknium:monero.social >__ More people having a multisig key to the wallet means that the probability that at least one of the multisig keys is compromised by an adversary IMHO.     

> __< r​ucknium:monero.social >__ So...maybe multiply the probability of compromise by the probability that the adversary would find an exploit in the experimental multisig or sell the multisig key to someone who did develop an exploit.     

> __< h​into.janaiyo:matrix.org >__ assuming multisig is ready by march, luigi would "only" hold 3 months of CCS raised funds at the maximum     

> __< r​ucknium:monero.social >__ Isn't it hard to do multisig with an airgapped machine? That's another thing.     

> __< rbrunner >__ For me, really hard to say. I tend towards multisig from a security regarding theft point of view. But there are many other ways you can mess up something when using multisig, e.g. too many signers lose keys.     

> __< r​ucknium:monero.social >__ I like multisig for CCS, but just thinking through the threats.     

> __< rbrunner >__ Not sure whether airgappend multisig is possible at all. Would somehow surprise me, frankly.     

> __< h​into.janaiyo:matrix.org >__ i'm assuming a multisig setup would preclude the need for airgapped machines     

> __< rbrunner >__ Maybe we even don't know, because so far nobody tried that :)     

> __< j​effro256:monero.social >__ It's possible but definitely a hassle with current wallets. There's not really an app *built* for that use-case, but nothings stopping you from doing it now technically     

> __< rbrunner >__ Amazing.     

> __< plowsof >__ We should sponsor hours via the CCS (specifically for jeffro256 / tobtoht to continue working on the ux/other problems?)     

> __< j​effro256:monero.social >__ It would take twice as many trips as a normal hot/cold airgapped wallet and the messages being passed around would be much bigger     

> __< rbrunner >__ Then please clone jeffro256 so he can work on multisig and the Seraphis wallet at the same time ...     

> __< j​effro256:monero.social >__ With Seraphis though, it would be the same number of trips which is nice since you don't need to combine partial key images     

> __< j​effro256:monero.social >__ lol     

> __< v​tnerd:monero.social >__ is the expected work in the UI or the underlying multisig code? I thought there was some push to move it closer to MRL-009 ?     

> __< v​tnerd:monero.social >__ and MRL-009 has security proofs, but none for extensions that compute the viewkey     

> __< rbrunner >__ As far as I understand the situation, tobtoht intends to work on the UI/UX side only     

> __< v​tnerd:monero.social >__ thats probably not a deal-breaker (the viewkey)     

> __< t​obtoht:monero.social >__ Yes, I'm going to focus on UI/UX and make changes to the MMS, not the multisig code itself.     

> __< rbrunner >__ Replacing PyBitmessage by something modern, and make the whole UI graphical instead of command line like the MMS in the CLI wallet now     

> __< v​tnerd:monero.social >__ yes, we still dont have a great system to replace PyBitmessage     

> __< rbrunner >__ Working on the "fundamentals" of multisig would certainly be nice, but I am in the camp of the people who think the "experimental" state is "good enough" for our use case     

> __< rbrunner >__ given how dire the alternatives look, at least     

> __< t​obtoht:monero.social >__ vtnerd: I intend to replace PyBitmessage with a centralized self-hostable message relay. It is radically simple, which is why I feel it has a good chance allow us to ship _something_  sooner rather than later.     

> __< t​obtoht:monero.social >__ No PoW. No distributed storage. No extra client dependencies. No forced reliance on flaky anonymity networks.     

> __< t​obtoht:monero.social >__ Federation? Distributed storage? It increase complexity exponentially and with that development time. Not saying these aren't lofty goals but let's start with the basics here.     

> __< rbrunner >__ But there will be *some* spam protection, I guess?     

> __< v​tnerd:monero.social >__ yes, we have to get the authentication and message exchanges down first     

> __< t​obtoht:monero.social >__ rbrunner: Yes, through traditional means. Basic access control, rate-limiting, automatically closing abusive channels.     

> __< v​tnerd:monero.social >__ well this is the issue, you need an authentication system I think, otherwise anyone can jumpin and hijack the messages     

> __< rbrunner >__ That probably won't make many friends, or will it?     

> __< t​obtoht:monero.social >__ MMS already encrypts messages for each participant.     

> __< v​tnerd:monero.social >__ tobtoht: correct, but how does it even know who the participants are in the first place?     

> __< rbrunner >__ Yeah, reading messages is not the problem.     

> __< rbrunner >__ Message decrypts = it's the right participant.     

> __< v​tnerd:monero.social >__ I don't recall how the MMS is encrypted, but     

> __< rbrunner >__ Private view key     

> __< v​tnerd:monero.social >__ theres a chicken and egg problem here     

> __< v​tnerd:monero.social >__ otherwise anyone could jump-in the first round     

> __< v​tnerd:monero.social >__ after establishing all participants, yes its easier, but the first round doesn't even know participants iirc     

> __< r​ucknium:monero.social >__ For the CCS wouldn't the private view key be published publicly? Maybe an edge case, but important for the CCS.     

> __< j​effro256:monero.social >__ The way I envisioned it was that the centralized service could choose to verify thru email, PGP keys, or interactive secure channel auth like Matrix     

> __< rbrunner >__ It's the private view keys of the wallets before they go "multisig". Not the private view key of the multisig address     

> __< v​tnerd:monero.social >__ yeah I was thinking PGP myself, hopefully that isnt too hard to setup     

> __< rbrunner >__ But well, to establish all that before March 1, seems to be ... optimistic.     

> __< v​tnerd:monero.social >__ and we haven't identified who the participants are either     

> __< rbrunner >__ And well, all participants running bleeding edge master branch code instead of an official interim release ... phew     

> __< rbrunner >__ This is tempting faith     

> __< rbrunner >__ You can do 2/3 multisig "by hand", if you don't have to do too often, and *after* establishing the wallets     

> __< rbrunner >__ If you go higher, things get hairy     

> __< rbrunner >__ This is all a bit depressing ...     

> __< t​obtoht:monero.social >__ I remain optimistic     

> __< rbrunner >__ But anyway, not sure what kind of successor solutions Luigi had in mind that we could establish in a mere 2 months     

> __< rbrunner >__ Ok, nearly 3 months     

> __< h​into.janaiyo:matrix.org >__ tobtoht: how confident are you this could be ready (at least for our use cases) by march 1st 2024?     

> __< t​obtoht:monero.social >__ 80%     

> __< rbrunner >__ :)     

> __< rbrunner >__ We probably still should talk a bit about the case it won't be ready after all. Maybe not today, but soon     

> __< luigi1111 >__ It was supposed to be 3 months. It's not hard and fast. Just meant to spur discussion and changes needed for longer term solutions quickly.      

> __< luigi1111 >__ Even if multisig was in a good state now it will still take weeks to find the right signers and them to be happy with their setups      

> __< rbrunner >__ Yes, would need several rounds of training for everybody to get acquanted with multisig     

> __< rbrunner >__ Or maybe tobtoht succeeds to come up with a really good UI/UX     

> __< rbrunner >__ Or better said, user-friendly, simple and easy     

> __< t​obtoht:monero.social >__ Yes, but still, have all signers practice with a dummy CCS wallet before 'the real deal', collect feedback, integrate changes, etc     

> __< rbrunner >__ Yup     

> __< plowsof >__ Definitely , its all fun and games until several people.actualy try it      

> __< rbrunner >__ And then go on to manage funds to the tunes of tens of thousands of dollars.     

> __< rbrunner >__ "Only numbers on screen, don't get nervous" :)     

> __< j​effro256:monero.social >__ I was also thinking of a certain funding scheme (which albeit is a little less friendly for the donator), which doesn't allow the escrow to lose the funds, but doesn't give the money to the proposer without approval from the escrow. It would work like this: donator and CCS create 2/2 multisig wallet together. Donator sends funds to the 2/2 multisig wallet, then donator partially s<clipped messag     

> __< j​effro256:monero.social >__ igns a transaction to the proposers' address, then a refund address they the donator owns. If the escrow determines that a proposer completed their milestones, then they add a signature to the proposer partially signed tx, and if not, add a signature to the refund partially signed tx and broadcast     

> __< j​effro256:monero.social >__ Doesn't require interaction from proposer and doesn't require interaction from the donator after the inital setup     

> __< o​frnxmr:monero.social >__ Think of this:     

> __< o​frnxmr:monero.social >__ many projefts accept donations in crypto, such as graphene.      

> __< o​frnxmr:monero.social >__ if graphene wanted folks to partially sign tx, theyd likely lose 100% of retail donors     

> __< h​into.janaiyo:matrix.org >__ would multisig be needed? can't donators just send return address + donated tx id?     

> __< j​effro256:monero.social >__ This way escrow can't send funds to themselves     

> __< j​effro256:monero.social >__ They don't have the ability to cryptographically (assuming multisig code is secure)     

> __< r​ucknium:monero.social >__ I like it. Getting more creative, at least.     

> __< h​into.janaiyo:matrix.org >__ ahhh i see - either back to donator or to proposer     

> __< plowsof >__ I donate 100% then i spend the output after ?      

> __< plowsof >__ 1 week later? Day before milestone completed?     

> __< j​effro256:monero.social >__ Well you wouldn't necessary make it mandatory, but have it be the option  for those so inclines ig     

> __< j​effro256:monero.social >__ Donator couldn't spend output without approval from CCS since its a 2/2 multisig wallet     

> __< r​ucknium:monero.social >__ BCH has a special wallet + webpage setup for Flipstarters to create partially signed AnyoneCanPay txs for crowdfunding. Works differently because the threshold for sending to the worker is just that the funding goal amount is reached. It's not a multisig (I think).     

> __< plowsof >__ Sounds similar to BCH's collective funding method which wont(?) Be possible with seraphis (but could be?) Rucknium knows more about that     

> __< r​ucknium:monero.social >__ I brought up Flipstarter because it has a "smooth enough" special interaction between a wallet (Electron Cash) and a web page. IIRC they improved the UX recently so you don't need a special wallet plugin, but they had it before.     

> __< plowsof >__ Interesting jeffro256     

> __< o​frnxmr:monero.social >__ thats a lot of wallets     

> __< h​into.janaiyo:matrix.org >__ although escrow wouldn't be able to divert funds, they can still 1. deadlock forever 2. lose the keys, right?     

> __< o​frnxmr:monero.social >__ and a lot of seeds for (someone) to have the keys for     

> __< j​effro256:monero.social >__ Yeah a wallet plugin which makes an ephemeral 2/2 multisig wallet (perhaps with `monero-javascript`) could make the UX actually really smooth     

> __< o​frnxmr:monero.social >__ hintos #2 is what im getting at     

> __< r​ucknium:monero.social >__ The escrow agent can loose the keys, but you can have multiple escrow agents with the same key. There is less security risk in this setup. The multiple agents would also have to have the partially signed txs.     

> __< r​ucknium:monero.social >__ lose*     

> __< h​into.janaiyo:matrix.org >__ this scheme + some deadman switch to auto send funds after a period of time would be interesting     

> __< j​effro256:monero.social >__ yes escrow could choose to deadlock funds or lose the keys still, but now there isn't a financial incentive to hack the wallet or "steal" coins. Since it is not possible to steal coins, the escrow can focus more on making the keys redundant     

> __< j​effro256:monero.social >__ With a normal wallet, the more redundant you make the keys, the larger your attack surface is to get hacked     

> __< o​frnxmr:monero.social >__ I see no reason to burden a donor with creating wallets or any speciak anything     

> __< o​frnxmr:monero.social >__ They need only send funds. The rest is our problem     

> __< j​effro256:monero.social >__ But now the effects of someone else having knowledge of the keys is minimized     

> __< o​frnxmr:monero.social >__ Dont need a refund address, dont need to sign anything     

> __< o​frnxmr:monero.social >__ Just deposit and walk away     

> __< h​into.janaiyo:matrix.org >__ i think we're re-inventing smart contracts :)     

> __< o​frnxmr:monero.social >__ Yei     

> __< j​effro256:monero.social >__ Ostensibly they would actually be more inclined to donate if they knew the funds were safer and weren't going to be diverted to some hacker     

> __< o​frnxmr:monero.social >__ and their opsec is to be trusted?     

> __< j​effro256:monero.social >__ Whose opsec ?     

> __< o​frnxmr:monero.social >__ The donators, who partially signed the tx already     

> __< j​effro256:monero.social >__ They don't need ongoing OPSEC models, they just need to fund the wallet, partially sign, then shred everything and forget about it     

> __< r​ucknium:monero.social >__ This would not allow repurposing CCS funds, of course. Just return to sender.     

> __< j​effro256:monero.social >__ They're already custodying their own funds, so if they screw themselves out of funds, that would happen anyways     

> __< r​ucknium:monero.social >__ Repurposing if the original worker decided to stop working     

> __< o​frnxmr:monero.social >__ red taping the donation process is backwards to me     

> __< a​ck-j:matrix.org >__ Not sure if this was brought up yet but since we’re talking about CCS. A 2696 xmr donation was just made to the monero general fund. It could have been the CCS theif returning most of the funds     

> __< o​frnxmr:monero.social >__ The problem is: were playing with peanuts and accept this as the norm     

> __< r​ucknium:monero.social >__ We can officially end the meeting here. Feel free to continue. Thanks for trying to fix multisig everyone.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-12-06T15:27:27+00:00
- Closed at: 2023-12-17T17:15:11+00:00
