---
title: Monero Research Lab Meeting - Wed 13 November 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1109
author: Rucknium
assignees: []
labels: []
created_at: '2024-11-12T20:29:59+00:00'
updated_at: '2024-12-03T21:12:33+00:00'
type: issue
status: closed
closed_at: '2024-12-03T21:12:33+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

4. [FCMP++ tx size and compute cost](https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898) and [MAX_INPUTS/MAX_OUTPUTS](https://github.com/monero-project/research-lab/issues/100#issuecomment-2433524326)

5. Making transaction weight a function of number of inputs, outputs, and `tx_extra` length instead of number of bytes.

6. [Discussion: preventing P2P proxy nodes](https://github.com/monero-project/research-lab/issues/126).

7. [Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time`](https://github.com/monero-project/research-lab/issues/125)

8. Any other business

9. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1105 

# Discussion History
## Rucknium | 2024-11-14T19:07:29+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1109     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< j​berman:monero.social >__ *waves*     

> __< b​oog900:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< 0​xfffc:monero.social >__ hi everyone, not gonna able to attend the meeting. worked on few minor tasks, did few reviews. the main thing I am working right now (as I am typing this ), is debugging #9362     

> __< r​ucknium:monero.social >__ me: I worked on some spy node analysis. I finished my presentation for the Monerotopia conference: "Hard Data on Banking the Unbanked through Cryptocurrency". It is scheduled to be at 17:45 UTC on Friday, November 15: https://monerotopia.com/schedule/     

> __< r​ucknium:monero.social >__ At the presentation I will reveal a possibly first-ever estimate of the total value of goods and services purchased online using cryptocurrency in the EU in 2022, based on survey data collected by the EU central bank :D     

> __< rbrunner >__ Sounds interesting     

> __< r​ucknium:monero.social >__ 3) FCMP++ tx size and compute cost and MAX_INPUTS/MAX_OUTPUTS https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898 https://github.com/monero-project/research-lab/issues/100#issuecomment-2433524326     

> __< r​ucknium:monero.social >__ kayabaNerve said he won't be here at the meeting. I don't have anything to add on this right now. Anyone else?     

> __< j​berman:monero.social >__ me: shared a ccs update, main highlight being I implemented building the fcmp++ curve tree locally in wallet2, it makes overall sync 2-2.5x slower (initial impl was 5-6x slower), and has room for improvement still: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/491#note_27183     

> __< r​ucknium:monero.social >__ 4) Making transaction weight a function of number of inputs, outputs, and `tx_extra` length instead of number of bytes.     

> __< r​ucknium:monero.social >__ kayabaNerve asked this to be on the agenda, but he's not here right now 🥹     

> __< r​ucknium:monero.social >__ But this is something I've suggested. It is really hard to get alternative implementations of Monero wallets to match wallet2's fee behavior. Fees being based on bytes makes it hard because Monero txs can be a little different in size even if they "do" the exact same thing, i.e. spend the same number of inputs to the same number of outputs.     

> __< r​ucknium:monero.social >__ That reduces tx uniformity.     

> __< r​ucknium:monero.social >__ The tx weight computation is already partway to this proposal because there is a weight clawback based on the number of outputs. The verification time of bulletproof outputs is nonlinear in the number of outputs. That's why there is the clawback.     

> __< rbrunner >__ Hmmm, I wonder whether you can "blow up" transactions that way, with extra-heavy inputs and outputs and proofs and such, and then spam for little XMR     

> __< r​ucknium:monero.social >__ Yes I wonder that exact thing, too     

> __< r​ucknium:monero.social >__ Which is why the cryptographers would have to comment on it     

> __< r​ucknium:monero.social >__ Sort of like the BTC Ordinals situation.     

> __< rbrunner >__ My gut feeling is that a switch to that would need a very, very careful examination of this danger     

> __< rbrunner >__ Also whether our current serialization format really does not allow to put in bytes somewhere that do not disturb interpreting the data but make everything bigger     

> __< r​ucknium:monero.social >__ Yes, or just a safety limit "If tx weight goes above Z limit, then the tx pays by bytes"     

> __< rbrunner >__ Apart of course from the already mentioned cryptographic questions     

> __< rbrunner >__ Couldn't we quantize fees a bit more, so the occasional few bytes more or less of alternative implementations wouldn't matter that much?     

> __< c​haser:monero.social >__ like rounding within a certain range?     

> __< j​berman:monero.social >__ quantizing more was essentially a core idea behind koe's discrete fee selection     

> __< r​ucknium:monero.social >__ I think a side effect of the fee discretization proposal is that txs that an an "unlucky" fee/byte would stay at the back of the confirmation line when the txpool is congested     

> __< rbrunner >__ Right, there was something in koe's proposal     

> __< rbrunner >__ Is that the same however like I probably have in mind? You pay fees for blocks of, say, 50 bytes, instead of single bytes?     

> __< j​berman:monero.social >__ weighting by num inputs, outputs, and tx_extra length instead of bytes I think makes sense in practice to more accurately weigh the various components of a tx, though I'm not sure if it actually would make the problem of matching wallet2 simpler, since it introduces more rules an implementer has to figure out and match perfectly beyond just the bp clawback     

> __< r​ucknium:monero.social >__ Right now there is no mathematical function that takes as argument a Monero tx and returns the wallet2 fee for it. AFAIK.     

> __< r​ucknium:monero.social >__ With this proposal, there would be a function     

> __< r​ucknium:monero.social >__ And AFAIK, the only person who can properly implement the fees is jberman :D     

> __< r​ucknium:monero.social >__ I asked Exodus Wallet to contact jberman to get their fees exactly right, but they didn't. I'm not 100% sure that they have it exactly right, but they have it approximately right at least.     

> __< r​ucknium:monero.social >__ I can only check the approximation because there is no such mathematical function, like I said.     

> __< j​berman:monero.social >__ There is calculate_fee in wallet2 but fair there are also surrounding pieces to that function. Regardless, I think it makes sense to implement a rule to weigh by num inputs, outputs, and tx_extra size because of the disparate impact the number of the various components have on syncing the chain beyond just their number of bytes     

> __< j​berman:monero.social >__ And I also think the direction of discretizing fees is a reasonable course of action toward reducing fingerprintability     

> __< rbrunner >__ Is all the really complicated stuff like long-time median block size, penalties and such only in the calculation of the base fee per byte?     

> __< r​ucknium:monero.social >__ Yeah, the BP clawback was a step toward that. I don't know the latest numbers of FCMP++, but AFAIK, the veification time impact of FCMP++ will be larger than the tx bytes impact, compared to the status quo.     

> __< j​berman:monero.social >__ rbrunner7 yep, and that's fed to the wallet by the daemon     

> __< rbrunner >__ And still everything in the wallet is terribly difficult? :)     

> __< rbrunner >__ I wonder a bit right now, but of course I don't really doubt     

> __< rbrunner >__ You would think tx size in byte times fee per byte, done.     

> __< j​berman:monero.social >__ It's a little tricky getting priorities right and using the exact weight in the correct spot correctly     

> __< r​ucknium:monero.social >__ rbrunner: AFAIK, only the fourth (maximum) tier of the suggested fee/byte in monerod's get_fee_estimate is affected by the median block size. With the other tiers, basically wallets are expected to move up a tier in dicrete steps instead of actually increasing the tier.     

> __< j​berman:monero.social >__ And also using the correct fee mask and stuff. There's definitely a lot of room for error with the current flow     

> __< r​ucknium:monero.social >__ But the fourth tier is based on a _continuous_ computation of the median block size, so that would have to be analyzed and changed in a reasonable way if discretized fees were implemented.     

> __< rbrunner >__ Ok, it wasn't improbable from the start that something Monero related would be simple :)     

> __< r​ucknium:monero.social >__ We have p2p proxy nodes to discuss. We can discuss the fee issue more next time.     

> __< r​ucknium:monero.social >__ 5) Discussion: preventing P2P proxy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< r​ucknium:monero.social >__ I added a little function to my R package https://github.com/Rucknium/xmrpeers called `peers.ip.collect()` that shows you when your local node is connected to suspected spy nodes, plus when the "subnet saturation" of those peers is occurring. Obviously, you have to not have the banlist enabled to see when you are connected to those suspicious nodes.     

> __< v​tnerd:monero.social >__ damn, missed the meeting again, sorry :/     

> __< r​ucknium:monero.social >__ So people can check for themselves how many of their outbound peers are the suspected spy nodes, plus the subnet saturation evidence. It takes about a day of running it to see the subnet saturation clearly.     

> __< r​ucknium:monero.social >__ I posted in #monero-research-lounge:monero.social  about: LionLink Networks created a press release about the BTC spy node accusations: https://linkinglion.net/     

> __< r​ucknium:monero.social >__ > Ashburn, VA – March 26, 2024 – LionLink Networks ("LionLink") is aware of recent articles published alleging illicit behavior originating from IP addresses advertised by LionLink Networks and describing an entity known as LinkingLion. We believe the first report on this behavior to be written by the Bitcoin Developer 0xB10C....LionLink Networks categorically denies any invol<clipped message     

> __< r​ucknium:monero.social >__ vement in the activities described by the author known as 0xB10C.     

> __< r​ucknium:monero.social >__ The suspected Monero spy/proxy nodes are managed by LionLink, too.     

> __< rbrunner >__ Just define "illicit" the right way, and everything is in order     

> __< r​ucknium:monero.social >__ There was disagreement last meeting about having an opt-out setting in monerod to avoid establishing outbound connections to nodes on the suspected spy list.     

> __< r​ucknium:monero.social >__ rbrunner: Well, it is honest monerod nodes that are initiating all the connections to those IP addresses, so where is the grounds to complain? :)     

> __< rbrunner >__ Lol, right     

> __< rbrunner >__ I think with the evidence we have what they claim is only a pretty unimportant side-show     

> __< j​berman:monero.social >__ response by 0xB10C: https://b10c.me/blog/013-one-year-update-on-linkinglion/     

> __< r​ucknium:monero.social >__ Maybe a plan: Short-term: Post on Monero communication channels a suggestion to run the banlist, Medium-term: Something like ASmap: https://github.com/monero-project/monero/pull/7935, Long-term: R&D on a more universal solution like proof-of-storage, but without big downsides.     

> __< r​ucknium:monero.social >__ I have done a few preliminary simulations about how ASmap would affect network connections.     

> __< r​ucknium:monero.social >__ By the way, there were about 800 unique ASNs in my node log data from April/May 2024. For "reachable" nodes, i.e. nodes that accept incoming conenctions.     

> __< j​berman:monero.social >__ selsta does core operate the DNS blocklist (blocklist.moneropulse.* domains)?     

> __< selsta >__ yes, they pay for it     

> __< r​ucknium:monero.social >__ Really preliminary simulation results: Assume on average that reachable nodes have 120 incoming connections on average. If nodes on the network refuse to connect to a node on an ASN they are already connected to, then: Mean number of incoming txs for nodes on ASNs:     

> __< r​ucknium:monero.social >__ LionLink: 40, Hetzner: 95, Fifty rarest ASNs: 160     

> __< r​ucknium:monero.social >__ As expected, if you are on a common ASN, you get fewer incoming connections     

> __< j​berman:monero.social >__ On a short-term plan, I think it would also make sense for boog900 to share the underlying logic/approach for how the IP's are determined to be proxies with someone from core, and if deemed correct, for core to add the IP's to the DNS blocklist     

> __< selsta >__ the current issue is there is a DNS TXT record size limit for IPs     

> __< selsta >__ so we need to fix that first and put out an update     

> __< selsta >__ either by switching to a .txt fetch or by using multiple DNS endpoints     

> __< j​berman:monero.social >__ ah, just curious what's the size limit / shortfall right now (how far past the size limit would the entire list push it)?     

> __< selsta >__ it's full currently     

> __< j​berman:monero.social >__ ok     

> __< selsta >__ roug estimate 3x current list     

> __< selsta >__ rough     

> __< j​berman:monero.social >__ well, short-to-medium plan then to include as part of the DNS blocklist flow     

> __< b​oog900:monero.social >__ I have told sech1 & Rucknium (although I wouldn't expect them to publicly certify the method). I can PM you? and any other dev who wants to know is free to PM me.     

> __< r​ucknium:monero.social >__ There is Boog900's method and there is a method of counting up subnet saturation that can be done by anyone with a node. Of course, that only works on the set of IP ranges (about six) that the adversary has full control of.     

> __< r​ucknium:monero.social >__ Maybe I should have caught this when I analyzed the tx relay data for my black marble paper 😶. But I had already done a lot of different types of analysis with that, so I had to draw the line somewhere.     

> __< r​ucknium:monero.social >__ More on p2p spy/proxy nodes for now?     

> __< j​berman:monero.social >__ question for boog900 , hypothetically if you were to publicly share your code that identifies a proxy node, is your concern that they would find another hole / method of running a proxy that's harder to detect?     

> __< b​oog900:monero.social >__ Yes the issue is easy for them to fix (I think)     

> __< j​berman:monero.social >__ Reasonable     

> __< r​ucknium:monero.social >__ 6) Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time` https://github.com/monero-project/research-lab/issues/125     

> __< r​ucknium:monero.social >__ Just checking. IIRC, chaser  wanted to follow up on this by continuing the conversation in the GitHub issue. If there is nothing more to say here, we can end the meeting.     

> __< c​haser:monero.social >__ yes, I couldn't get to to that in the past week, so will do so after the meeting.     

> __< r​ucknium:monero.social >__ Meeting is over. Thanks everyone.     

> __< s​yntheticbird:monero.social >__ Delicious meeting as always     

> __< c​haser:monero.social >__ thank you all!     

> __< s​gp_:monero.social >__ Veridise completed their task to provide the log deriv spec and expand the security proofs re: negative coefficients. Their report is available here:     

> __< s​gp_:monero.social >__ https://matrix.monero.social/_matrix/media/v1/download/monero.social/AGBzpCbNZkdtnRXdtJOVmyvF     

> __< s​gp_:monero.social >__ I spoke with kayabanerve about the last bit ("An Implicit Assumption and a Potential Vulnerability"), and he says it's not an issue in practice, but it's something to keep in mind for the implementation     

> __< s​gp_:monero.social >__ I spoke with kayabanerve about the last bit ("An Implicit Assumption and a Potential Vulnerability"), and they say it's not an issue in practice, but it's something to keep in mind for the implementation     

> __< k​ayabanerve:matrix.org >__ It was a potential issue. It's now confirmed to not be a potential issue. The last line suggests something to watch out for but it doesn't occur in our case.  


# Action History
- Created by: Rucknium | 2024-11-12T20:29:59+00:00
- Closed at: 2024-12-03T21:12:33+00:00
