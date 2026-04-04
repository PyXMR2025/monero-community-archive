---
title: Monero Research Lab Meeting - Wed 20 November 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1112
author: Rucknium
assignees: []
labels: []
created_at: '2024-11-19T20:55:54+00:00'
updated_at: '2024-12-03T21:12:27+00:00'
type: issue
status: closed
closed_at: '2024-12-03T21:12:27+00:00'
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

7. Any other business

8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1109 

# Discussion History
## Rucknium | 2024-11-21T19:38:21+00:00
Logs


> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1112     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< c​haser:monero.social >__ hello     

> __< a​rticmine:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ hi     

> __< j​effro256:monero.social >__ Howdy     

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: I put up a docs website for my `xmrpeers` R package: https://rucknium.github.io/xmrpeers/reference/index.html . The txpool archiver now stores key images, too, so it is easier to retrospectively measure intentional or unintentional double spend attempts.     

> __< v​tnerd:monero.social >__ finished up span changes in monerod, working on merging PRs in LWS, and frontend for LWS     

> __< r​ucknium:monero.social >__ My Monerotopia talk "Hard Data on Banking the Unbanked through Cryptocurrency" is up: https://vimeo.com/1029005523  https://github.com/Rucknium/presentations/blob/main/Rucknium-Monerotopia-2024-Banking-the-Unbanked.pdf . Thanks to xenumonero for voicing it. To answer the question from last time, the estimated aggregate spending on goods and services in the EU in 2022 using cryptoc<clipped message     

> __< r​ucknium:monero.social >__ urrency was €4.1 billion. (90% confidence interval: €1.7 to €6.6 billion).     

> __< a​rticmine:monero.social >__ Scaling changes to support FCMP++ One the questions I am looking at are changes in TX size when an additional layer is added to the FCMP++     

> __< r​ucknium:monero.social >__ Two CCS proposal that we have discussed are now on the Ideas page: "Audit monero-serai and monero-wallet" https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/518 and "Gingeropolous 1TB MRC upgrade" https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/516     

> __< r​ucknium:monero.social >__ Declare your thoughts with your thumbs.     

> __< j​effro256:monero.social >__ Someone brought up an interesting question at the conference: FCMP++ unifies all anonymity pools, including pre-RingCT. How much money is actually tied up in unspent pre-RingCT outputs? I believe we can actually answer this question with 0 uncertainty if take the sum of "amount*(num_outs_of_amount-num_rings_of_amount)" for each amount. This is because previously, we only allowed r<clipped messag     

> __< j​effro256:monero.social >__ ings to contain inputs of equal amount     

> __< j​effro256:monero.social >__ Can anyone see a problem with this approach? I'll work on a script today that calculates it just for fun     

> __< s​gp_:monero.social >__ Hello     

> __< j​effro256:monero.social >__ Hi sgp     

> __< j​berman:monero.social >__ *waves*     

> __< j​berman:monero.social >__ Sorry I might be a sporadically available dealing with a personal issue atm     

> __< r​ucknium:monero.social >__ jeffro256: I don't know enough about how the pre-RCT protocol works, but your idea sounds very interesting.     

> __< r​ucknium:monero.social >__ Usually my first step when building the Monero tx database is to delete pre-RingCT data :D     

> __< j​effro256:monero.social >__ Regarding the CCS proposals, since multiple researchers have need for higher compute requirements, I'm totally okay with the 1TB upgrade CCS     

> __< a​rticmine:monero.social >__ jeffro256: This should be doable with zero error. I also believe it is important to preserve the pre-ring CT block chain data and to make it easily available to the public in order to not give the blockchain surveillance companies an advantage     

> __< r​ucknium:monero.social >__ 3) FCMP++ tx size and compute cost and MAX_INPUTS/MAX_OUTPUTS     

> __< r​ucknium:monero.social >__  https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898 https://github.com/monero-project/research-lab/issues/100#issuecomment-2433524326     

> __< r​ucknium:monero.social >__ Is kayabanerve  available for this agenda item?     

> __< r​ucknium:monero.social >__ Anyone else have thoughts about introducing a MAX_INPUTS limit and/or changes to the current MAX_OUTPUTS limit, with the FCMP++ hard fork activation?     

> __< c​haser:monero.social >__ I'm generally in favor of any of the limits (except 2/2) in order to increase tx uniformity     

> __< s​gp_:monero.social >__ I defer to kayaba's analysis and opinion on this     

> __< r​ucknium:monero.social >__ Good thing I have these typing notifications, or I would have moved on to the next item already :P     

> __< b​oog900:monero.social >__ I actually did this at one point, could dig it out again, I remember there been quite a bit still there     

> __< r​ucknium:monero.social >__ 4) Making transaction weight a function of number of inputs, outputs, and `tx_extra` length instead of number of bytes.     

> __< r​ucknium:monero.social >__ IMHO, the protocol currently already has an implicit tradeoff value between verification time and tx size because of the Bulletproofs clawback. Does anyone know of any meeting logs or anything where the tradeoff was discussed?     

> __< a​rticmine:monero.social >__ My preference with this is to eliminate TX weight entirely out of consensus     

> __< a​rticmine:monero.social >__ This should be addressed if needed at the node relay level     

> __< a​rticmine:monero.social >__ It is redundant especially with the proposed input and output proposals     

> __< a​rticmine:monero.social >__ I was by the way involved in the tx weight department     

> __< a​rticmine:monero.social >__ Development     

> __< r​ucknium:monero.social >__ Doesn't consensus need some concept of tx weight to decide how much of the tail emission is not emitted when a miner mines a block above the aggregate penalty weight?     

> __< a​rticmine:monero.social >__ We just use the actual transaction size in bytes     

> __< a​rticmine:monero.social >__ No need to add an additional weight for verification time     

> __< a​rticmine:monero.social >__ The latter was the idea behind the tx weight s     

> __< s​gp_:monero.social >__ Verification time would still not directly be related to transaction size though right?     

> __< j​effro256:monero.social >__ Note that this would break economically if the transaction format ended up being malleable     

> __< a​rticmine:monero.social >__ If the concern is a possible attack this can be dealt with by node relay     

> __< s​gp_:monero.social >__ Consensus seems like a far preferable way to address this to me     

> __< r​ucknium:monero.social >__ For the potential malleability issue, I think you can just set a safeguard limit on tx size with respect to the input/output/tx_extra size     

> __< j​effro256:monero.social >__ And then we end up hitting arbitrary limits during the next stressnet ;)     

> __< a​rticmine:monero.social >__ With the proposed limitations in numbers of inputs and outputs 4 maybe 8 or 16. I really do not see the point     

> __< a​rticmine:monero.social >__ It just adds un necessary complexity to consensus     

> __< a​rticmine:monero.social >__ ... and the potential for bugs     

> __< r​ucknium:monero.social >__ I think jeffro256  means "malleable" as if the tx fee is set by the number of inputs and outputs, and someone figures out how to pack more data into the input or outputs than expected, then tx size could be very large. A little like Ordinals getting a discount on data when putting it in the SegWit part of BTC blocks.     

> __< j​effro256:monero.social >__ Yes     

> __< j​effro256:monero.social >__ Malleable was the wrong word     

> __< a​rticmine:monero.social >__ But we have a consensus limit on the number of inputs and outputs to certain discreet values     

> __< s​gp_:monero.social >__ I'm for skipping unnecessary complexity, but my understanding is that verification time cost can still be detached from size by a meaningful amount     

> __< r​ucknium:monero.social >__ If the tx fee is set by number of bytes, it will be much easier for an adversary to guess which wallet software constructed each tx because wallet developers do not exactly match the reference software fee algorithm.     

> __< s​gp_:monero.social >__ I'm wading through kayaba's writings in search for the right numbers to compare     

> __< a​rticmine:monero.social >__ Weights does not help with this     

> __< a​rticmine:monero.social >__ The reason this was introduced is that at the time there was a choice between 1 and 16 outpouts     

> __< a​rticmine:monero.social >__ Now the choice could at most between 4 and 16 outputs     

> __< a​rticmine:monero.social >__ With no other choices in-between     

> __< r​ucknium:monero.social >__ My suggestion is not to go with weights, as they exist today. But to set tx fees as a function of inputs, outputs, and tx_extra length. Two txs with the same ins/outs and tx_extra today can have different tx weights because the number of bytes is different, by chance.     

> __< s​gp_:monero.social >__ The reason kayaba recommended the specific multiplier in the transaction is to enforce specific fees, in this proposal per the weight. In theory it could be against size as ArticMine wants, afaict     

> __< s​gp_:monero.social >__ Maybe we need data on how different verification time is versus size for various transaction combinations before making a decision. Kayaba may have already done that but it's hard for me to read. If there's a single digit % difference then I lean ArticMine's way of simplicity     

> __< a​rticmine:monero.social >__ Fees belong in node relay., and outside of consensus     

> __< rbrunner >__ Not sure I understand. Then somebody can mine themselves a tx with any fee?     

> __< v​tnerd:monero.social >__ then a miner could still “stuff” a longer to verify tx in a block? I don’t see anything wrong with doing it at both levels     

> __< a​rticmine:monero.social >__ The miner can always do this by providing an off chain rebate or recruiting an off chain payment     

> __< a​rticmine:monero.social >__ This is  why fees must never be baked into consensus     

> __< s​gp_:monero.social >__ Yeah but this would allow a discernable on-chain, publicly-visible mark on transactions. Isn't that something we should at least try to make more difficult?     

> __< s​gp_:monero.social >__ The goal isn't to prevent miner fee sillyness (off chain dealing etc), it's transaction uniformity     

> __< a​rticmine:monero.social >__ This issue is and can be addressed by node relay     

> __< r​ucknium:monero.social >__ Consensus is baked into fees, I guess. The consensus rules on block size increase are activated by the interaction of fees and miners' self-interest. So the fees have to be set with the consensus rules in mind.     

> __< a​rticmine:monero.social >__ Yes of course     

> __< a​rticmine:monero.social >__ ... but the fees have also to keep in mind the free market     

> __< s​gp_:monero.social >__ consensus would require the majority of miners to agree to stupid fees; it would not allow a specific rogue miner to act stupidly like relay would do     

> __< a​rticmine:monero.social >__ Fees can become  really stupid over time     

> __< j​effro256:monero.social >__ Look, I might be in the minority here, but I'm much much less worried about uniformity with FCMP++ since now the EXTERNAL impact is very much mitigated. It used to be that weird fees cause everyone's privacy to suffer, but that largely is less true anymore. We should start focusing on UX (off chain reimbursements in this case)  when considering tradeoffs IMHO. A relay rule would p<clipped messag     

> __< j​effro256:monero.social >__ revent silly mistakes for people who aren't colliding with miners     

> __< a​rticmine:monero.social >__ I agree     

> __< j​effro256:monero.social >__ Tho I do agree that vtnerd's point is valid : adding heavy txs would basically be free to a miner, but cause a lot of network load if fees aren't asserted at consensus     

> __< a​rticmine:monero.social >__ ...but we do have and will have consensus rules on the number of inputs and outputs     

> __< a​rticmine:monero.social >__ We can also limit the size of discretionary fields at consensus     

> __< j​effro256:monero.social >__ I guess that's not a NEW concern: spam is free up to the penalty-free zone limit. It's just that that 300KB can be packed with more compute requirements     

> __< s​gp_:monero.social >__ the only cost before then is opportunity cost, consensus rule or no     

> __< r​ucknium:monero.social >__ jeffro256: "I'm much much less worried about uniformity with FCMP++ since now the EXTERNAL impact is very much mitigated." I agree with this. IMHO, you can group a lot of de-anonymization "heuristics" into a class of "set intersection attacks". The ring size 16 is a set. Then you intersect that with the set of nonstandard fees. Then other sets if you have the data on it. The origi<clipped message     

> __< r​ucknium:monero.social >__ nal ring size 16 makes the other set intersection operations much more powerful for an adversary. With FCMP, that initial set size is they whole chain. On the other hand, having as much tx uniformity as possible (especially to prevent against attacks that no one has anticipated yet) is a good goal IMHO.     

> __< r​ucknium:monero.social >__ And IP address is a set, by the way     

> __< j​effro256:monero.social >__ Yes uniformity is always a good thing, but you've also got to factor in the difference in the size of the total FCMP set if you bring in more people because of enabled use cases , UX, etc     

> __< r​ucknium:monero.social >__ So you combine the nonstandard fee with the probable IP origin of a tx.     

> __< r​ucknium:monero.social >__ I don't understand the UX issue involved here     

> __< s​gp_:monero.social >__ UX would be an issue only if terrible multipliers were chosen imo. Eg if moving up to the next tier costs 100x more     

> __< r​ucknium:monero.social >__ The interaction of the fee tiers, users' economic behavior, and the block size adjustment algorithm is quite untested IMHO.     

> __< r​ucknium:monero.social >__ Literally untested on mainnet until this year with March spam. A patch to wallet2 had to be released to get the wallet fees to automatically increase     

> __< rbrunner >__ Wonder how an approach to test that could look, with user behavior in there ...     

> __< r​ucknium:monero.social >__ You could estimate some demand curves from behavior on other chains, probably     

> __< a​rticmine:monero.social >__ There is some limited information from early 2017, and also from some of the times that we have gone over the penalty free zone     

> __< a​rticmine:monero.social >__ What I have seen in those cases is that users have not responded to the market efficiantly     

> __< r​ucknium:monero.social >__ IIRC, this paper does some empirical demand estimation on BTC: Huberman, G., Leshno, J. D., & Moallemi, C. (2021). Monopoly without a Monopolist: An Economic Analysis of the Bitcoin Payment System, The Review of Economic Studies, 88(6), 3011–3040. https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=78     

> __< a​rticmine:monero.social >__ They for example tend to pay a fee that is too low     

> __< s​gp_:monero.social >__ imo we have two real options. Pick sane multipliers and strongly enforce, or decide to allow truly arbitrary fees like Bitcoin     

> __< s​gp_:monero.social >__ Picking multipliers and then weakly enforcing seems like the worst of both worlds imo     

> __< a​rticmine:monero.social >__ Any fee  multiplayer enforcement has to be at node relay and not at consensus     

> __< k​ayabanerve:matrix.org >__ Apologies. I'm off by about an hour. That's on me.     

> __< s​gp_:monero.social >__ That's not true though right? Kayaba demonstrated how you can do at consensus right? Are you speaking about a miner reimbursing out of band which is a different problem with different considerations?     

> __< r​ucknium:monero.social >__ I think people pick a fee that is too low since they don't know that the txpool is congested. They just expect it not to be, as it almost always is like that. The auto fee increase in the patch this year helped a little with that.     

> __< k​ayabanerve:matrix.org >__ My argument was for the fee per weight to be embedded in the TX, not the fee. In order for the TX to balance, the wallet must correctly calculate the TX weight.     

> __< a​rticmine:monero.social >__ It can be done at consensus. It is not a good idea, because a miner can always circumvent off chain. This then can lead to centralized control     

> __< j​effro256:monero.social >__ Sorry y'all , I have to dip out for the time being, but will catch up on the chats later. Thanks everyone for participating     

> __< k​ayabanerve:matrix.org >__ We can still, at node relay rules, penalize specific TX patterns and demand they require a higher fee rate.     

> __< r​ucknium:monero.social >__ Of course, the question with the auto fee increase is how high should it go? IIRC, right now it moves from the first to the second tier, and doesn't go higher unless manually changed by the user.     

> __< k​ayabanerve:matrix.org >__ But forcing wallets to calculate the weight correctly should prevent them from being non-uniform with weight calculation.     

> __< a​rticmine:monero.social >__ My proposal is to simply use the physical size in bytes of the tx and eliminate any weights     

> __< a​rticmine:monero.social >__ KISS in consensus     

> __< k​ayabanerve:matrix.org >__ That isn't inherently incompatible with my proposal.     

> __< k​ayabanerve:matrix.org >__ I think it's wrong though as it harms certain functionality and is annoyingly complicated.     

> __< k​ayabanerve:matrix.org >__ If we define a simplified weight formula, we never have the annoyance of what a varint is in practice.     

> __< k​ayabanerve:matrix.org >__ That's where wallets are currently being wrong, causing fingerprinting issues.     

> __< a​rticmine:monero.social >__ What we are doing is not trying to price verification time     

> __< k​ayabanerve:matrix.org >__ It also harms pre-signed TXs (transaction chaining). If I sign a TX now, and go to publish it in a year, and the tree has grown a layer, I'll have signed a TX for byte length X and it'll now be byte length Y.     

> __< a​rticmine:monero.social >__ This is appropriate if we limit the numbers it inputs and outputs     

> __< k​ayabanerve:matrix.org >__ By using a simplified weight formula dependent on input/output count, we become agnostic to how big the membership proof is in practice.     

> __< k​ayabanerve:matrix.org >__ I'd agree if we did 4/4 and transaction uniformity. I disagree if we allow 16 outputs. That justifies a clawback existing, as we have now, IMO.     

> __< k​ayabanerve:matrix.org >__ *I'd agree we don't have to price verification time     

> __< s​gp_:monero.social >__ Thanks kayaba this is helpful     

> __< k​ayabanerve:matrix.org >__ I still think weight shouldn't equal bytes due to the pre-signing usecase I mentioned and the complexities of calculating TX size ahead of time     

> __< a​rticmine:monero.social >__ Yes this is a serious issue. The fee has  to remain the  same after a layer change     

> __< k​ayabanerve:matrix.org >__ Since a layer change always increases the amount of bytes, that requires we pay by input count or prefix size, not by TX size.     

> __< k​ayabanerve:matrix.org >__ Prefix size should be a valid alternative but it is a really really broad thing to do as it makes inputs as expensive as outputs, when by verification time, it's no where close.     

> __< s​gp_:monero.social >__ Speaking of KISS, is there a reason _not_ to use powers of 2 as the allowed multipliers? And to set the default fee selection logic to be in effect "pick the lowest power of 2 that's likely to get me into the next block"     

> __< r​ucknium:monero.social >__ We are twenty-five minutes over the hour. We can end the meeting time here, but feel free to continue discussing. Maybe someone could make a `research-lab` issue about it. We didn't get to the "Preventing P2P proxy nodes" item today, but we can get to it next meeting.     

> __< a​rticmine:monero.social >__ There are two ways of doing this. One is to normalize the proof size by using weights to the initial number of layers. So the transaction weight does not change. The other is to change the minimum penalty free zone size.     

> __< a​rticmine:monero.social >__ I really do like weighting the proof size to the initial number of layers     

> __< s​gp_:monero.social >__ The larger the multiplier differences, the greater the incentive there is to work with a mining pool on a fee rebate etc     

> __< r​ucknium:monero.social >__ sgp_: AFAIK, two potential issues with that: 1) We don't know how well block size auctions actually work with just discrete bids allowed. Right now the 4-tiers are just a wallet convention, but wallets software can be changed easier than consensus rules. 2) If fees are discrete but weight is not, then users who happen to have a high tx weight (but the same fee as others) will be s<clipped message     

> __< r​ucknium:monero.social >__ tuck at the back of the confirmation queue for a long time. Maybe until the txpool empties completely.     

> __< a​rticmine:monero.social >__ So yes using a fixed weight instead of the actual size for the proof size would be the most elegant way to deal with the proof Bauer issue     

> __< s​gp_:monero.social >__ Miners are given a block weight to fill though right? Not a true, byte block size?     

> __< a​rticmine:monero.social >__ Correct     

> __< r​ucknium:monero.social >__ Right now the default block template creation behavior is first-in/first-out for txs on the same fee-per-weight tier     

> __< s​gp_:monero.social >__ since the fee per weight is the same, and miners pick (by default) for fee per weight, I don't quite get the back of the queue issue     

> __< r​ucknium:monero.social >__ AFAIK, the raw fee in Seraphis was supposed to be an exponential power. That does not get you discrete fee-per-weight since weight is basically continuous.     

> __< r​ucknium:monero.social >__ So you would have to define the discrete fee as fee-per-weight, not the raw fee.     

> __< r​ucknium:monero.social >__ AFAIK, the Seraphis fee _field_ in the tx was supposed to be an exponential power.     

> __< s​gp_:monero.social >__ that's similar to what we are discussing here, right? Defining the fee per weight (the multiplier) in the tx. And I'm suggesting specifying a power of 2 in there     

> __< r​ucknium:monero.social >__ IIRC, txs do not say what their size nor weight is. You have to calculate that "manually". So you would have to change how that is handled in the data that txs carry.     

> __< k​ayabanerve:matrix.org >__ ArticMine: Then we're back at not using TX size yet a formula dependent on the amount of inputs, outputs, and length of TX extra 😅     

> __< k​ayabanerve:matrix.org >__ Because we're proposing using input_proof_base_cost * inputs instead of those actual proof sizes.     

> __< k​ayabanerve:matrix.org >__ It doesn't have to be a complicated and long formula. I just wanted something better defined than 'build and test serialize a TX and also know how to handle XYZ variable length fields properly'.     

> __< k​ayabanerve:matrix.org >__ If we define all the constants in the formula to be the byte lengths seen within a TX, that's still a massive step up.     

> __< a​rticmine:monero.social >__ What we could do is set a fixed weight for the transaction excluding  any discretionary fields based upon the number of inputs and outputs. This weight would be used instead of the proof and non discretionary fields size. In determining the  TX weight . I would leave any discretionary fields if they are allowed outside of this calculation.     

> __< k​ayabanerve:matrix.org >__ input_proof_base_cost + (input_ additional_cost * inputs) + output_proof_base_cost + (output_additional_cost * outputs) + tx_extra_len     

> __< k​ayabanerve:matrix.org >__ Where cost can simply be the byte length expected for such items     

> __< k​ayabanerve:matrix.org >__ As long as we define actual constants, and the only variables are inputs/outputs/length of TX extra, I'd be significantly happier.     

> __< a​rticmine:monero.social >__ Yes based upon the initial proposed number of layers in the proofs     

> __< a​rticmine:monero.social >__ This will also make me much happier     

> __< k​ayabanerve:matrix.org >__ Cool     

> __< k​ayabanerve:matrix.org >__ As of right now, fee, decoy selection, is in the way.     

> __< k​ayabanerve:matrix.org >__ Even after FCMP++, the reference block and associated tree will be in the way.     

> __< k​ayabanerve:matrix.org >__ *the fee field is a varint meaning calculation of the fee itself affects the fee as the calculated fee may have a distinct length than used in the calculation     

> __< a​rticmine:monero.social >__ What I see is that we need defined weights for each allowed combination of inputs and outputs and any other required fields     

> __< a​rticmine:monero.social >__ Tx extra if allowed would also have to have defined limits in bytes     

> __< a​rticmine:monero.social >__ So this effectively makes transaction weights discreet at consensus, which is fine     

> __< a​rticmine:monero.social >__ ... and solves the layer issue on scaling     

> __< a​rticmine:monero.social >__ So all I would need is the proposed weight of a 4 in 4 out tx with no additional discretionary fields.     

> __< a​rticmine:monero.social >__ ... and the appropriate estimated actual size with the initial number of layers in the proofs     

> __< a​rticmine:monero.social >__ If we have discrete tx weights then we have discrete fees at each fee level     

> __< k​ayabanerve:matrix.org >__ https://github.com/kayabaNerve/fcmp-plus-plus/blob/develop/crypto%2Ffcmps%2Fsrc%2Flib.rs#L127     

> __< k​ayabanerve:matrix.org >__ This code exists for the FCMP itself (which is not the entire set of FCMP++ proofs).     



# Action History
- Created by: Rucknium | 2024-11-19T20:55:54+00:00
- Closed at: 2024-12-03T21:12:27+00:00
