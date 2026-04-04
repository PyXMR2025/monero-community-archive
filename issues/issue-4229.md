---
title: '[Discussion] Move to a Fixed Ringsize'
source_url: https://github.com/monero-project/monero/issues/4229
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2018-08-05T23:07:40+00:00'
updated_at: '2018-08-22T23:01:11+00:00'
type: issue
status: closed
closed_at: '2018-08-22T20:18:35+00:00'
---

# Original Description
I would like to receive feedback on moving to a fixed ringsize for the September 2018 (v8) protocol upgrade (hardfork). This will happen regardless of the selected ringsize. The current minimum ringsize is 7.

# Scope of Discussion

This discussion includes the impact of setting a mandatory ringsize and support for a mandatory ringsize in wallet software and merchant services (eg: CLI, GUI, MyMonero, and Monero Integrations).

Please keep all comments and discussion related to these topics only, not the broader issues of different ringsizes. However, if you support this proposal under certain situations, such as supporting only if the ringsize is greater than _x_, you can comment with that information.

# Major reasons for the change:

**1. Few people use the non-default ringsize**. At the time of writing, >96% of transactions in the past month used a ringsize <10 [[1](https://moneroblocks.info/stats/ring-size)]. This is consistent with other findings where the minimum ringsize is used for the vast majority of transactions.

**2. Non-default ringsizes reduce entropy and therefore decrease privacy**. Ringsize is an important piece of metadata, and having people use different values allows users to more easily be identified.

**3. Unusual ringsizes for multiple transactions can be linked**. If a user sends multiple transactions with an atypical ringsize, then it is likely that these transactions are associated with each other. If this behavior is not permitted, users will not have their transactions linked this way.

**4. Non-default ringsizes complicate research**. Having exceptions to the number of decoys used complicates analysis on the effectiveness of Monero's privacy claims. Most analyses to-date assumed that all transactions use the minimum ringsize.

# Major reasons against the change

**1. A configurable ringsize provides flexibility**. If a user would like to send transactions with a different ringsize for some purpose, they are able to do with a configurable ringsize.

**2. Increasing ringsize increases privacy**. Some people believe that increasing the ringsize increases privacy. While this is strictly true since there are more decoys included in the ring signature, the possibility of leaked metadata typically results in the opposite effect.

**3. Support for services using non-default ringsizes**. Users may be upset if they are unable to send transactions from outdated wallet software.

---

Overall, I believe that the pros outweigh the cons. I recommend setting a fixed ringsize in the September protocol upgrade (hardfork) and updating the CLI and GUI to support only a single ringsize.

# Discussion History
## cryptochangements34 | 2018-08-05T23:36:07+00:00
I think that the loss of flexability, especially with a ring size as low as 7, can be a major downside. If for some reason it is a good idea for people to use a non standard ring size then it can't be done without changing the consensus rules again. For example, with the MoneroV fork it was recommended that users use a higher ring size than the default (at the time 5) if transacting within a couple days from the fork because of the possibility of the MoneroV airdrop deanonymizing some transactions, essentially making some decoys useless. This was an unforseen event that nobody had thought of before and by fixing the ring size we lose the flexibility that could be useful if another more serious unforseen event comes

## Gingeropolous | 2018-08-06T00:42:40+00:00
In general I support move to a fixed ringsize, but I think a lot more needs to be put in stone before this kind of shift. Primarily, how will the fixed ringsize change over time? If we fix it at 12 this fall, is it going to stay 12 forever? 

That, in my opinion, would be bad. Ideally, the ringsize will increase as computational ability increases.

I had discussed this in this proposal to algorithmify the ringsize: https://github.com/monero-project/monero/issues/3069 , basically do with the ringsize what monero did with the blocksize.

Because I see the ringsize having similarities to the blocksize debate. "We should change it to be fixed ringsize of 200! Because privacy!" and the other side going "we need to keep it at 12, because decentralization!"

I really think this is another case where we have to remove humans from the decision as much as possible. 

## anonimal | 2018-08-06T00:44:50+00:00
>2. Non-default ringsizes reduce entropy and therefore decrease privacy. Ringsize is an important piece of metadata, and having people use different values allows users to more easily be identified.

Yes, when constructing the RingCT language, ring-count *diversity* creates an unintended vocabulary.

For example, this type of weakness from *diversity* has been proven in Tor's random guard selection `F=(k/N)^2` where the observer of `(k/N)` can "de-anon" `F`. Your claim also implies uniform distribution across multiple transactions on a per-user basis, no?

Regardless, where are the samplings? Where are the distribution models? Where are the equations backing these variable-fixed-ringsizes per hardfork? Why aren't the Noethers proposing this issue?

>3. Unusual ringsizes for multiple transactions can be linked. If a user sends multiple transactions with an atypical ringsize, then it is likely that these transactions are associated with each other. If this behavior is not permitted, users will not have their transactions linked this way.

This is under the assumption that the 'unusual' ringsize is static per-user, i.e., one static 'unusual' size per transaction? Where is the formal study disproving the effectiveness of random-N of random sets? Are you claiming to disprove the effectiveness of differential privacy equations? If not, why can't we apply a new working definition here?

>4. Non-default ringsizes complicate research. Having exceptions to the number of decoys used complicates analysis on the effectiveness of Monero's privacy claims. Most analyses to-date assumed that all transactions use the minimum ringsize.

Good. Fix the claims until the math can prove otherwise. The math must evolve. The claims must evolve.

## SamsungGalaxyPlayer | 2018-08-06T01:10:45+00:00
@cryptochangements34 generally consensus is pointing to churning being more effective than increasing the ringsize for cases like these.

@Gingeropolous this proposal does not imply that the ringsize will be fixed forever. It is compatible with your algorithmic ringsize proposal. Whatever the algorithm picks will be the fixed size.

@anonimal I need you to elaborate more on your connections to the Tor analogy, but I will explain more about what I mean with the metadata.

No matter what ringsize you select with a Monero transaction, it is recorded on the blockchain.

If everyone uses the same ringsize, this metadata is meaningless. An attacker could learn nothing by knowing the ringsize is the same as every other transaction's.

However, if a user uses a default ringsize of a different wallet (suppose MyMonero recommends a ringsize of 20), then this metadata could suggest that the transaction was sent from a MyMonero wallet. Or if an attacker is transacting with a party and trying to find more about their identity, they could notice that the attacker is using a random ringsize each time. These are potential vulnerabilities that arise from unusual, unique metadata. Even if different ringsizes are used, heuristics can be formed from any of these patterns in an attempt to find unusual behavior.

> This is under the assumption that the 'unusual' ringsize is static per-user, i.e., one static 'unusual' size per transaction? Where is the formal study disproving the effectiveness of random-N of random sets? Are you claiming to disprove the effectiveness of differential privacy equations? If not, why can't we apply a new working definition here?

My topic was mostly focused on a user selecting and reusing a single ringsize (eg: 23). However, even if you were to choose a random selection, eg: select a ringsize between 10 and 50 for each transaction you send, this is still susceptible to heuristics. There are no studies I am aware of that specifically speak to this vulnerability, but given the small proportion of transactions that use a different ringsize _at all_, I feel comfortable claiming that the entropy is too small to even protect users in this scenario. The random-ringsize solution could be instituted in all wallets to increase entropy, but this would have severe downsides. Most importantly, different wallets could ignore this, and there would be no way to reasonably establish consensus to enforce this behavior.

> Good. Fix the claims until the math can prove otherwise. The math must evolve. The claims must evolve.

I do not think you understand the significance of this effort. It is immense, and we do not have an unlimited number of people contributing. Unless someone from MRL says otherwise, I do not feel comfortable recommending further research resources being allocated to something that does not need allocation. In any case however, this is the smallest point of those that I have made. Research will continue to improve, but it takes time. Finding the nuances that are introduced by <5% of transactions is low priority.

## Gingeropolous | 2018-08-06T02:13:58+00:00
@SamsungGalaxyPlayer ,

> this proposal does not imply that the ringsize will be fixed forever.

Indeed, but it also doesn't propose any mechanism to increase the fixed ringsize. I mean, every fork are we just gonna come to a rough consensus and say "yeah, we should totally bump it by 2"... or is it gonna be an algorithm... or are we going to setup one of those lottery ball systems with the ping pong balls with numbers on them. 

## SamsungGalaxyPlayer | 2018-08-06T02:19:35+00:00
@Gingeropolous I understand you concern, but I recommend opening a different issue to discuss this. If we include this discussion here, I don't think we can keep it focused.

## OFRBG | 2018-08-06T03:33:42+00:00
I'm not a Monero dev, but I think fixed sized rings matter from the point of view of end-users. For someone familiar with the environment, choosing a ring size is an educated choice. However, for end-users choosing the size adds choice complexity. Users will randomly pick either the smallest number possible, the highest one available on the UI or some random default.

If you want to take into consideration how people choose their signatures, maybe take into account the power of default choice: make every transaction have a default ring signature size which may be explicitly increased or decreased for a fee. This avoids the problem of MM transactions being "linked" to the default suggested signatures, as well as letting users who know what they are doing use different sizes.

People are *very* willing to simply use default options when dealing with tough decisions. In order to keep the freedom of choice for the size, you can allow users to change the ring size with a fee: said cost being the consequence of disturbing the entropy.

(Previous discussion related here: https://www.reddit.com/r/Monero/comments/6ryeln/ring_size_vs_transaction_cost/)

---

TL;DR: set a chain-level default N that may be overridden at a higher cost. People are highly likely to use default options on difficult questions. Users who wish to use a different ring size may do so at a cost representing the disturbance of the entropy. Overall this should make the chosen ring size converge to the default.

## SamsungGalaxyPlayer | 2018-08-06T04:11:41+00:00
@OFRBG you are explaining the situation which has existed since Monero's inception. You have always been able to increase the ringsize for an additional fee. The default is currently the minimum. We learned through past experience that the minimum is the most widely-used, since exchanges and merchants use this to save money.

In practice, increasing the ringsize typically causes more harm than good. Wallets should instead recommend a churning process for users that want to spend more Monero for greater privacy.

## OFRBG | 2018-08-06T04:36:32+00:00
@SamsungGalaxyPlayer from what I read on that reddit thread, the cost difference between 5 signatures and 21 is not significant, making the decision irrelevant for individual users. I would personally like to see a fixed ringsize, but this comes at a community cost of "forcing" said size. Monero's community is one I admire a lot, and while most users will not even understand the relevance of the choice, others might feel like their choices are being unfairly cut down.

Perhaps I didn't really get my idea across. I would set a default ringsize N for no "extra" charge, and add scaling costs to adding more signatures. As long as people don't see the difference between N and N+1 signatures the choice problem remains. A simple example would be like this:

```
Tx0 with default 10 signatures:         Y XMR base fee, 0 extra fee
Tx0 with 20 signatures:                 Y XMR base fee, Y extra fee
Tx0 with 30 signatures:                 Y XMR base fee, 3Y extra fee
```

I'm trying to keep the more "radical" members in mind who wish to keep their freedom of choice. A good middle ground could be allowing a default ringsize and then 10 signature steps with higher cost each. It would probably be best if people just agreed to move to a fixed size, but I'm bringing this up this solution in case there is opposition.

## julian1 | 2018-08-06T06:39:22+00:00
By all means disable choice it in the GUI, but I don't think fixed size should be part of the conensus layer. 2c

## tekcash | 2018-08-06T07:27:16+00:00
NACK

## ancap19 | 2018-08-06T07:48:13+00:00
Middle ground: we could allow to choose just between two or three standard ring sizes

## dnaleor | 2018-08-06T08:17:43+00:00
If a fixed size is too contentious, at least I would propose to use fixed multiplicators.
For example, if minimum ring size is 10, then only allow:
10, 20, 40, 80, 160, 320, ...
This will mitigate some of the analysis risks already

@OFRBG , your idea is similar to mine, but I guess exponential increase in ring size makes more sense. The lesser choices, the better: more people will be using the same size, hence better entropy. 

It also makes more sense: what's the difference between ring size 40 and ring size 50? Not that much. If you want more privacy, just go for the next double, 80. Hence, exponential increase.

## OFRBG | 2018-08-06T09:00:11+00:00
@dnaleor I was using linear increases of ringsize with exponential cost, but you make a good point about the difference between 40 and 50. Sticking to a system of exponentially increasing sizes with scaling costs might do the trick.

## moneromooo-monero | 2018-08-06T10:25:15+00:00
The ring size is moved to 11 for next fork. ArticMine's new fee formula is based on this.

## laachoir | 2018-08-06T11:13:32+00:00
As far as I remember that formula is flexible enough to take different ringsizes into account.
Also, ruling the decision without having the discussion first feels a little excluding.

## dnaleor | 2018-08-06T12:56:42+00:00
11 then, no problem. Just limit the allowed ring sizes to 11, 22, 44, 88, 176, 352, ...

The huge befit is that if people desire to sometimes use a bigger ring size, there are probably others who used the same ring size as well sometimes. This is way more likely then when every ring size is allowed.

Also, especially for the bigger ones, it's not that unlikely if you use ring size 176 that a certain decoy is the result of a spent with ring size 176. SO this even adds a bit of plausible deniability to the assumption that if you see this pattern, the real input is the one previously spent with ring size 176.

## moneromooo-monero | 2018-08-06T13:26:34+00:00
>  Also, ruling the decision without having the discussion first feels a little excluding.

If you did not participate in this discussion, it is irrelevant. Maybe you were not here yet at the time, but we will not delay something forever just because new people arrive all the time. If you're interested in contributing, you're welcome, but complaining that you're being ignored when you arrive after something was done is NOT contributing.

If you have arguments not presented in the previous discussion, you present your arguments. You do not complain you were ignored.

Read https://github.com/monero-project/monero/issues/1673 first. If you did not know it existed, then maybe you should have looked before complaining.

## paulshapiro | 2018-08-06T13:27:38+00:00
I second @moneromooo-monero's sentiment. This has been under discussion for ages.

## laachoir | 2018-08-06T13:32:20+00:00
I apologize for rousing your emotions. Of course there's no reason to wait for potential newcomers, and I did not mean to complain on my regard. Reading through the corresponding reddit thread it seems like at least one more party shared my concerns.
Starting a new issue with such a fundamental decision now made it seem like there was no discussion before. Because if there was, why start a new issue? Linking to previous discussions might also have been helpful, thanks for the pointer @moneromooo-monero 
Anyway. Back to the topic at hand.

## paulshapiro | 2018-08-06T13:33:27+00:00
@laachoir we have dev meetings on IRC every second Sunday

## moneromooo-monero | 2018-08-06T13:33:51+00:00
Thanks.
If you want to participate, then #monero-dev on IRC. But keep it to monero development please. Other stuff in #monero.

## SamsungGalaxyPlayer | 2018-08-06T14:43:46+00:00
@moneromooo-monero with the ringsize 11 change, will the ringsize also be fixed at 11?

## cryptochangements34 | 2018-08-06T14:48:57+00:00
I would be in favour of a fixed ring size 11

## moneromooo-monero | 2018-08-06T14:54:50+00:00
Yes, it is fixed. See https://docs.google.com/document/d/1Y3IsjH7ywJOvFeZd1qT1fRfz2lw8APp8ptcyDXzYrxk/edit from ArticMine, and https://github.com/monero-project/monero/pull/4219/commits/6700eb0cddef083c02a0e9488be8e332811e9337 for the code.

## SamsungGalaxyPlayer | 2018-08-06T15:18:54+00:00
Thanks @moneromooo-monero.

## SamsungGalaxyPlayer | 2018-08-07T17:38:42+00:00
[Here](https://paste.debian.net/plainh/362ed9d4) are the logs from the July 23 Monero Research Lab meeting. Relevant section is below:

> 2018-07-23 17:38:39< ArticMine> One other point here is increasing the ring size to 11 or using a fixed ring size of 11
> 2018-07-23 17:39:02< ArticMine> This actually helps mitigate the verification issue
> 2018-07-23 17:39:08<@sarang> This is where I'd hoped we would have better data on churn/diffusion and its relationship to ring size
> 2018-07-23 17:39:20< sgp_[m]> Why 11?
> 2018-07-23 17:39:22<@suraeNoether> oh, gosh, moneromoo o built me a utility that i can use to figure out whether there is a numerical solution to that!
> 2018-07-23 17:39:31<@suraeNoether> i forgot! i've been so busy finishing multisig
> 2018-07-23 17:39:36<@sarang> yup yup
> 2018-07-23 17:39:38< sgp_[m]> Likewise
> 2018-07-23 17:39:54<@suraeNoether> moneromooo built a utility that computes the # of unique transaction outputs in the history of any given transaction
> 2018-07-23 17:39:58< ArticMine> I piked 11 as the largest ring that would still allow for an 80% fee reduction
> 2018-07-23 17:40:10<@suraeNoether> oh, that's a good metric :D
> 2018-07-23 17:40:15<@sarang> We should have concrete data to show the benefit
> 2018-07-23 17:40:24<@sarang> Otherwise we're just saying "surely bigger is better"
> 2018-07-23 17:40:29< ArticMine> So all the fee calculations are based upon a ring size of 11 and a 2 in 2 out tx
> 2018-07-23 17:40:41<@sarang> and then there's a counterargument about keeping ring size and taking smaller txn size
> 2018-07-23 17:41:03< rehrar> at the very least we wanted to moved to a fixed ringsize this upcoming hard fork, yes?
> 2018-07-23 17:41:08< rehrar> regardless of bigger or not
> 2018-07-23 17:41:16<@sarang> I believe that is best
> 2018-07-23 17:41:19<@suraeNoether> i think that would be beneficial, yes
> 2018-07-23 17:41:25<@suraeNoether> we are at 7 now?
> 2018-07-23 17:41:26<@suraeNoether> is that rihgt?
> 2018-07-23 17:41:33< ArticMine> In my proposal my recommendation is fixed 11
> 2018-07-23 17:41:33< rehrar> yes
> 2018-07-23 17:41:35< sgp_[m]> Yes
> 2018-07-23 17:41:36<@sarang> that is rihgt
> 2018-07-23 17:41:56< sgp_[m]> Yes 7
> 2018-07-23 17:42:05<@sarang> We can at least make fun Spinal Tap references to convince people it's a good thing
> 2018-07-23 17:42:10<@suraeNoether> i'd support a fixed number between 7 and 11. i have no skin in this game, so to sepak
> 2018-07-23 17:42:27<@sarang> I'd support learning the effects
> 2018-07-23 17:42:31<@suraeNoether> sarang: oh yeah we can brand this the spinal tap update, with bulletproofs and ring size all the way to 11
> 2018-07-23 17:42:32<@sarang> and making a decision based on that
> 2018-07-23 17:42:43< unknownids> 11 rings when you need 1 more ring than 10
> 2018-07-23 17:42:53< oneiric_> lol
> 2018-07-23 17:42:53< unknownids> why not just make 10 bigger? cause ours go to 11
> 2018-07-23 17:43:10< moneromooo> I see you got the idea rihgt.
> 2018-07-23 17:43:52< ArticMine> The case for a fixed 11 are 1) User simplicity 2) No ring profiles 3) There may also be a regulatory advantage in taking away control from the user here
> 2018-07-23 17:44:07<@sarang> I still think we need to start naming our changes (PoW, network upgrades, etc.) to make them seem less contentious
> 2018-07-23 17:44:12<@suraeNoether> i'll run moneromoo's utility, it'll take a day or three of boiling my ram, then i'll have an answer about "what ring size is so large that improvements become negligible?
> 2018-07-23 17:44:23<@sarang> ty suraeNoether
> 2018-07-23 17:44:29<@sarang> keep me in the loop
> 2018-07-23 17:44:48< rehrar> post results here, I wanna know too
> 2018-07-23 17:44:59< ArticMine> Any questions?
> 2018-07-23 17:45:07<@suraeNoether> rehrar:  of course
> 2018-07-23 17:45:16< rehrar> Will we be ready for the "freeze"?
> 2018-07-23 17:45:19< dEBRUYNE> Moving to a static ring size is more important than bumping it imo
> ...
> 2018-07-23 17:45:40< ArticMine> Is there support for static 11 ring size?
> 2018-07-23 17:45:47< moneromooo> Yes.
> ...
> 2018-07-23 17:46:14<@suraeNoether> ArticMine: i support a static ring size. i will hold off on a number for a day or three
> 2018-07-23 17:46:21< oneiric_> Are there any arguments/reasons against using a static ring size?
> 2018-07-23 17:46:24< sgp_[m]> ArticMine I need to compile more info before agreeing, but I think the number is generally reasonable
> 2018-07-23 17:46:32< sgp_[m]> I definitely support static
> 2018-07-23 17:46:33<@sarang> Some users will argue they want "greater privacy"
> 2018-07-23 17:46:41<@suraeNoether> i think 11 in general is fine, actually
> 2018-07-23 17:46:44<@sarang> I think those users are wrong
> 2018-07-23 17:46:50<@suraeNoether> i may support a slightly higher number
> 2018-07-23 17:46:52< scoobybejesus> i tentatively support static 11
> 2018-07-23 17:46:55< moneromooo> No, they're not. Everyone should want greater privacy.
> 2018-07-23 17:47:11< moneromooo> They get to send to themselves once, and wait for a day or so.
> 2018-07-23 17:47:16< sgp_[m]> People who REALLY know what they're doing lose flexibility
> 2018-07-23 17:47:24<@sarang> I think they're wrong about the big ring size moneromooo, not wanting privacy
> 2018-07-23 17:47:29< tnsepta> isn't there a balance between privacy and prices?
> 2018-07-23 17:47:36< ArticMine> Yes
> 2018-07-23 17:47:46<@suraeNoether> tnsepta: there is, the question is whether the balance will be on the side of privacy or prices. :P
> 2018-07-23 17:48:03< isthmuscrypto> @xmrhaelan et al over in Monero Outreach could do some preemptive education about "ringsize > default ---> LESS privacy, not more"
> 2018-07-23 17:48:04< dEBRUYNE> tnsepta: Price as in fee price or?
> 2018-07-23 17:48:08< hyc> but it's misguided to believe "I want greater privacy than the average monero user so whatever ringsize they use, I'm going to use a bigger one"
> 2018-07-23 17:48:21< ArticMine> A increase over 11 will require a modification of the fees.
> 2018-07-23 17:49:14< ArticMine> Basically what matters is the ratio of the reference transaction weight to the effective minimum block weight
> 2018-07-23 17:50:09<@suraeNoether> okay, let's move on for now; seems like a static ring size is supported regardless of whether we increase it or not or by how much

Again, please note the discussion about the ringsize 11 is off-topic for this discussion unless your opinion on a fixed ringsize is contingent on a specific ringsize.

## pepsidrinkinglurker | 2018-08-07T22:34:29+00:00
Increasing the default minimum ring size to 11+ is the correct path. If with bulletproofs the tx fees as related to tx size can tolerate a higher ring size such as 20 then that would be the way to go. 
Setting the ring size as a fixed value however is unwise.
The mainnet is not and should not be a testnet. 
You are proposing a major change without any concrete information or study on the impact of it. 
Citing that "Non-default ring sizes complicate research" is not a valid reason since non-default ring sizes also complicate statistical analysis by advisories and this is a very good thing.
I urge you to reconsider 

Edit:
Also for proposals such as this a short time frame for input from others is not optimal. 
Rounded for sanity a 48 hour window is too small. 

## julian1 | 2018-08-07T23:38:46+00:00
Reading the discussion, it seems ring-size choice is determined/curtailed by fee calculation. What is it about fee calculation, that mean that fees do not scale linearly with tx bytes, or with total inputs + outputs + proof size? 

Also, is it always true that diverging from the common/default ring-size makes a tx more identifiable in all cases?

A specific deception could involve choosing a less common ring-size to lend the appearance of association with other txs in the anonymity set of that ring-size, when in fact there is no underlying relation.  

And what about a merchant might who might want to collect low value outputs, that are only profitable to aggregate with a lower fee/smaller ring-size profile? 


## hyc | 2018-08-07T23:47:53+00:00
@julian1 The entire point of bulletproofs is that the proofs are sub-linear in size wrt number of outputs. But verification cost remains linear. So the fee must  scale linearly with verification cost, not size.


## SamsungGalaxyPlayer | 2018-08-08T14:21:15+00:00
@pepsidrinkinglurker the discussion on ringsize 11+ is off-topic for this discussion.

My argument on research is the most minor point of those mentioned and comes down to the following: all research so far has been for a fixed ringsize. We have little to no research on the effects of unusual, non-default ringsizes and their effects. You may claim that there are benefits, but these have never been shown. Instead, mounting evidence points to the opposite. The ringsize metadata is a potential attack surface that can be eliminated, so it should be. Especially if there is no evidence that this potential attack surface should remain.

Respectively, this discussion has been ongoing for many months. The research meeting received a higher approval for a fixed ringsize than for a ringsize of 11. The concept of a fixed ringsize was introduced at least a year ago. Just because this is a new discussion does not mean it was the only discussion on this topic. Yes, it seems that this specific discussion should have been opened earlier, but it definitely has received the buy-in from the majority of contributors over the past several months.

@julian1 I cannot think of a reasonable case where selecting a specific ringsize in an attempt to be deceptive is realistic. It should always be less effective than hiding among the greatest entropy set.

Furthermore, we absolutely need minimum ringsizes to prevent 0-decoy-like issues. Even if a merchant prioritizes low fees, they should not be able to directly harm the network. Since there is already a network minimum and a ringsize increase is not considered in this discussion, it is irrelevant.

## moneromooo-monero | 2018-08-15T11:48:38+00:00
For those who want to read what was said before, here's another: https://github.com/monero-project/monero/issues/3035

## SamsungGalaxyPlayer | 2018-08-15T18:35:48+00:00
@Wigmnd @anonimal researchers have supported a fixed ringsize in Monero for several months, going back to at least December 2017 in the linked discussion by @moneromooo-monero and reinforced in the logs provided. I believe the burden should instead be placed on those who wish to preserve a non-fixed ringsize, since ringsize is a specific point of metadata that can be removed. Unless there are significant, evidence-based reasons to keep this potential metadata leak available, it should be closed.

## SamsungGalaxyPlayer | 2018-08-16T20:32:30+00:00
@Wigmnd please read the top comment under `Scope of Discussion`. I make absolutely no recommendation or argument here for an increased ringsize.

> Please keep all comments and discussion related to these topics only, not the broader issues of different ringsizes. However, if you support this proposal under certain situations, such as supporting only if the ringsize is greater than x, you can comment with that information.

> The amount of time that has passed since the issue*2 mentioned by @moneromooo-monero and the one mentioned by @Gingeropolous has been more than adequate enough for research to be preformed if the assumed threat of none default ring sizes was perceived to be so impacting. I am unaware of any such study that has been announced, preformed or published. You have not provided evidence of its existence.
It is unclear to me if you did not bother to read my response fully or if a misunderstanding has occurred.

Simply saying that time for research to be conducted does not mean that it has been conducted. The researchers have been busy on far more important matters such as bulletproofs and multisig. I am not here to provide evidence of such research, yet nevertheless, the researchers have consistently supported a fixed ringsize even in this absence. We feel generally (see the quoted MRL meeting) that a fixed ringsize is preferable. There is no evidence to support other ringsizes are helpful, and there is some evidence that they are harmful. As a result, since there is no significant reason voiced here *not* to adopt a fixed ringsize other than user choice/flexibility, and most people so far generally support it, then we should adopt a fixed ringsize.

## SamsungGalaxyPlayer | 2018-08-17T22:08:52+00:00
@Wigmnd it seems like you have bigger quarrels with Monero Research Lab and the work that they do. This is not the time or place for you to accuse them of having incorrect priorities. If you feel that bulletproofs and multisig are frivolous "features," then please do not bring these up here. Please re-read the discussion scope before commenting further. I have needed to mention this several times.

I do not believe that you fully understand how ring signatures work, and the scope of potential metadata that is leaked with unusual ringsizes. Allow me to create some hypothetical scenarios where an unusual ringsize is harmful:

1. You always use ringsize 73 for your transactions. Even if there is only circumstantial evidence that these transactions are all sent by you, it is strong circumstantial evidence.

2. You use a specific wallet client that always uses 13 as its ringsize. You reveal a strong likelihood that you are using a specific wallet by sending transactions.

3. It exacerbates many other attacks by adding another level of metadata to circumstantial evidence. Trying to catch someone with poisoned decoys? The ringsize metadata can help. Looking at timing attacks? The ringsize metadata can help.

I have mentioned before that I am not aware of any sweeping research that looks into these details. Nevertheless, these attacks are are considered possible, and can be easily mitigated or eliminated by setting a fixed ringsize. Since the threat of these attacks are >0, and there is no significant privacy reason for maintaining the current flexible ringsize that has ever been shown, we should move towards a fixed ringsize. It's that simple.

I have heard your argument that you would like more research before proceeding, and it is noted here. I disagree for the other reasons that I have provided in this thread and elsewhere.

If you would like to join these discussions years earlier, I strongly recommend joining #monero-community, #monero-dev, and #monero-research-lab. Even if we do not understand the full impact of something does not mean that we cannot move towards something that most contributors feel is beneficial. We never had a huge discussion to establish that flexible ringsizes are good, either. If the majority of people support a fixed ringsize, and if there is more evidence to suggest it is better than not with limited potential harm to the network, we should move towards a fixed ringsize.

I am happy that you made your voice heard in this thread. If you have any research or even circumstantial evidence to suggest that a flexible ringsize is beneficial, please comment again here.

## laachoir | 2018-08-18T02:42:39+00:00
Scenario 1 and 2, standard ringsize

Carol creates a transaction to Dave. It enters the mempool at blockheight 27, referencing the freshly unlocked transaction of the exchange to Alice. Both transactions are included in block 28.

Who can distinguish whether or not Carol is in fact Alice?

Scenario 1 and 2, non-uniform ringsize.

Carol creates a transaction to Dave. She uses ringsize 73. Her transaction enters the mempool at blockheight 27, referencing the freshly unlocked transaction of the exchange to Alice. It also references an output that was part of a transaction with ringsize 73. Both transactions  are included in block 28.

For an outside observer, circumstantial evidence suggests that the two transactions using ringsize 73 are indeed from the same entity. Thus, the other transaction referencing Alices input is far more likely to be in fact created by Alice.

This is, if I understand it correctly, the biggest issue @SamsungGalaxyPlayer has with non-uniform ringsizes.

For the record, I'm not yet fully convinced we should make the move to a fixed ringsize in the way we're currently doing it. If you want to count, count me as withholding my vote lacking necessary evidence in either direction.

## laachoir | 2018-08-18T06:13:54+00:00
The distribution with which mixins are selected is something done by wallet software, the protocol is unaffected by this. Whether or not you use a gamma distribution over the mixins age doesn't matter to the protocol, as long as you reference at least seven mixins (one of which is of course the true input).

Along the same lines, concerning my above example of Carol creating a transaction at the same time as Alice, referencing at least one identical input as Alice: Since Alice can in fact spend her output at that time (block 27), it is also a valid mixin for Carol. Whether or not currently existing wallet software picks up on transactions that _just_ became available I do not know. But for the protocol, that doesn't matter, since there's no telling who of the two used it as a mixin only.

This also means that the claim that you can't broadcast a transaction sharing any input with ones currently in the mempool is highly unlikely. If it were true, I can sketch a very straight-forward DoS that I have never heard of before: Imagine I want to prevent a given output from ever being spent. I create a transaction referencing this output as a mixin. As soon as that "blocking" transaction is confirmed, I create another such transaction. And so on. Since outputs are spendable independ of the current mempool, your claim cannot be true. (I'd be glad to be enlightened if such a DoS is in fact possible.)

Apart from all this, we're taking the discussion way off-topic again.

## SamsungGalaxyPlayer | 2018-08-18T19:21:43+00:00
@Wigmnd @laachoir thanks for these discussions.

> These examples are somewhat comical as the improper usage of anything can and will have negative results. They are also highly dependent on the user to re use a static ring size continuously and to be the only user to use that ring size. While they also depend on meta data which is seriously way outside of the scope of this issue I will entertain the notion somewhat.

This is literally the entire point though. Having a non-fixed ringsize creates the opportunity for error, the opportunity for nefarious wallets to add metadata to better differentiate users. I understand these are extreme examples, but the absolutely are possible with a fixed ringsize. We saw a similar scare with X Wallet, who wanted to use an unusual number of outputs for each transaction. I understand these are not the same, but the effect is essentially the same: a piece of information can identify users of a specific wallet.

I'm not going to comment further on the input selection algorithm. Of course, a better input selection algorithm supports all ringsizes, including fixed and flexible ringsizes. Luckily with the new gamma distribution that will be included in 0.13, this is *mostly* solved. See the Moser, Miller, et. all paper for the research here.

Under the scenarios you explained, it unfortunately is relatively weak support for a flexible ringsize. Your argument boils down to the following: a flexible ringsize allows Alice to select a larger ringsize to protect herself, especially in short scenarios.

Unfortunately, Alice could increase her ringsize to 100, and there would still be generally high evidence that she was the real spender, even under the current distribution. When we discuss churning, we discuss significantly higher entropy sets than 10,000. While you are correct that any number >7 is strictly better than 7, the effective protection here is essentially impossible to quantify. Yes, it means there are more likely to be more outputs from a recent transaction, but depending on the attacker, these ringsizes likely have no practical impact. Unfortunately, Monero ring signatures are simply ineffective at providing protection against powerful heuristics in a quick-turnaround scenario. Even if Moneor had a minimum ringsize of 100, I would need more research before recommending people put themselves in this position, especially against a motivated attacker.

Essentially what I'm getting to is this: we have two threat models to consider. One is against an attacker who is only looking for plausible deniability, and another is an attacker who is using advanced heuristics. For any given minimum ringsize >2, plausible deniability is guaranteed in most circumstances. Ringsize 7 was selected to provide plausible deniability even in the most reasonable extreme circumstance we have discovered. It's possible that several of these attacks can work together, but I digress. Such scenarios would be evidence for increasing the minimum ringsize, since you need the whole network to be on board to provide significant protection.

For an attacker with advanced heuristics (including those we haven't thought of yet), any reasonable ringsize is likely ineffective for a single transaction. Although higher is better, there is evidence to support that any of these entropy sets for a standalone transaction probably don't matter much. I recommend asking more in #monero-research-lab, since research here is ongoing. I will say that for churning, we originally were looking at entropy sets of at least 73,000 for a "reasonable recent zone" and 25,000,000 for a near-complete "entire Monero entropy set." These are all a far cry from any reasonable ringsize unfortunately.

Getting back to your scenarios, you are technically correct that Alice is better protected with a ringsize >7 than 7, at least from a strict ring signature perspective. However, the effect is likely limited. It likely will not matter. Furthermore, it opens up opportunities for people to make mistakes, for merchants to look for and collect information about people who use non-default ringsizes, etc. Especially for in-person transactions, using a non-default ringsize may lead to increased scrutiny of these transactions. Remember that this is a point of metadata that can be used for whatever purpose. Every time you interact with a different ringsize, you need to be extremely careful. As heuristics get more advanced, this metadata could be used in incredible attacks that we have not theorized yet. I make no claims here though for the sake of this argument, since I know it's relatively far-fetched.

> A network wide benefit of using a non uniformed ring size does in fact exist. By increasing the ringsize you increase the amount of decoys, this means if someone was to be tracking outputs of TXs to see when they are being reused as inputs for TXs the amount of reuse would grow in a non conforming manner that would be very difficult to preform statistically analysis on and it will also make certain statistical known truths to become false. Also statistically the benefit should increase once we switch to gamma because of the likeness of the decoys selected by default.

Unfortunately this is essentially security/privacy through obscurity. The information is there, and attackers can perform more sophisticated models to learn more. We already have forms of a relatively sophisticated tool (see monero-blockchain-blackball) to seach unusual ringsizes. This does not reasonably provide a significant enough burden for attackers.

> The distribution with which mixins are selected is something done by wallet software, the protocol is unaffected by this. Whether or not you use a gamma distribution over the mixins age doesn't matter to the protocol, as long as you reference at least seven mixins (one of which is of course the true input).

This is another example of the same effect of non-default ringsizes. If I created a wallet that used a non-default distribution (ahem... MyMonero... ahem... [it's since been patched]), then this is potentially severely damaging to the network and could separate transactions in this wallet from others. While *technically* ring signatures provide as much protection as the number of outputs they control, the *real* protection provided with a decent selection algorithm is far greater than under a weak selection. I make a similar argument for a fixed ringsize: it would increase the real effectiveness against heuristics.

## ArticMine | 2018-08-22T02:37:42+00:00
I would suggest that dnaleor's idea is a very reasonable compromise at this point. We allow a ring size of 11*2^N with N >= 0 and N an integer. (ring=11 N=0, ring=22 N=1, ring=44 N=2, ring=88 N=3, ring=176 N=4, etc.) This will mitigate the ring persona issue by eliminating non trivial ring size changes. It is also the approach that we are taking on fees for the same reason, namely avoiding fee personas. I should point out that the fee formula will still work since there would be a significant number of transaction with ring = 11 to allow the block weight to scale with the default fee. This is also the situation now with some transactions at the default fee that would not allow the block weight to scale if they were the only transaction type.

My read of the situation is that there is not enough community consensus to move to a fixed ringsize at this point. 

## iamsmooth | 2018-08-22T03:28:33+00:00
@ArticMine I don't agree about community consensus. People showing up at the last minute after months or even years of discussion and quite broad consensus among the continuously active participants who have devoted a lot of time and resources to the matter is not lack of consensus. That includes, by the way, both of the MRL researchers quoted above. It's pretty stupid to pay full time researchers and then disregard them based on a few last minute objections from mostly non-participants.

There will always be _some_ disagreement, from someone (and if there isn't, those seeking to disrupt will invent them). That can't be a reason to stop progress.

IMO the better process on the matter is to perhaps open discussion on whether or how to reintroduce variable ring sizes in the future, in particular based on what benefits they supposedly provide, if someone actually wants to carry that torch on it and make a real contribution, and not just throw bombs at other people's work.

Unless someone can come up with a clear reason why fixed ring sizes are _seriously harmful_ which would justify reversing course. That hasn't happened yet as far as I can see.

@Wigmnd 
> The issue of ring size 0 decoy usage comes down to the lack of users using blackballing

No it doesn't, that is wrong. Users can't blackball 0 decoy spends that happen after their own. It requires either entirely prohibiting them altogether or a different model of non-fungible outputs. The issue of non-uniform ring sizes is somewhat similar. It causes harm to others because everyone is trying to hide among others' transactions. That is facilitated by those transactions being uniform and harmed by them being non-uniform. Even if there is some benefit (which is questionable) to the person using the non-standard ring size, the cost to others is an offsetting consideration.


## fluffypony | 2018-08-22T03:38:18+00:00
I think we have a pretty solid understanding of what "broad consensus" is and how to measure it. My reading is that there's "broad consensus" for a fixed ring size, but perhaps for the sake of caution we push this out to April 2019 and let the MRL demonstrate how broken a non-fixed ring size is.

## iamsmooth | 2018-08-22T03:50:22+00:00
> for the sake of caution we push this out to April 2019 

I don't see any identified danger that would suggest this sort of caution is useful. It is just as likely (and indeed based on the consensus of people who have been looking at this for years, more likely) that caution points toward switching ASAP and considering switching back later if anyone can demonstrate a benefit.

We know there are methods of analyzing ring signature usage on the blockchain that can be used to hurts people. Leaving identified weaknesses (or even identified likely risks) in place longer than necessary is not caution, it is the opposite.

## fluffypony | 2018-08-22T03:54:14+00:00
@iamsmooth it's more to give the MRL time to publish a paper on it - I don't think that "just check these old GitHub issues" is a reasonable way to demonstrate how the conclusion was reached. Or maybe more to the point: "we know that X" is true, but we still need to communicate that to the next generation of Monero contributors and maintainers.

## iamsmooth | 2018-08-22T04:08:29+00:00
I wouldn't say old GitHub issues is the point. There have been numerous discussions in public channels (including GitHub issues, but not specifically that) both on an ad hoc basis and as part of organized meetings which have resulted in the consensus.

I suppose a paper couldn't hurt though.

But I do think there is an ongoing risk of further analysis of identifying chain data along the lines of monerolink that ends up being harmful and remains unmitigated. One of the things that we saw with monerolink was that most if not all of the issues in the paper were already mitigated (at least to some extent) by the time the paper came out. Most of those didn't have a paper written first, it happened through a process of continuous improvement. Throwing a monkey wrench into that process of continuous improvement because of a few last minute objectors seems dangerous to me.


## ArticMine | 2018-08-22T04:17:43+00:00
My initial thought when I made the recommendation was that there was broad consensus for a fixed ring size; however after reading some of the comments and more importantly giving this some more thought myself I have come up with some possible arguments against a fixed ring size:

1) It embeds a parameter into the consensus code that is dependent upon technological change. For example: Consider a future where the cost of computing power, digital storage, memory and bandwidth falls by a factor of say 10^9, as has happened in the past. In such a future a ring size of say ~10^5 would be economically very reasonable; however since it would require a consensus change it may not happen if there were interests against it. Also an attacker would also enjoy the same lower costs.
2) There could be an unforeseen security threat as occurred with the XMO and XMV forks. In the XMO case one way to achieve an effective ring size of say ~5-7 and spend on both chains was to use a ring size of about 20 in order to ensure 5-7 fake inputs were from before the fork. The latter could then be input into the XMR spend.

I still consider the idea proposed by @dnaleor I mentioned above a very good first step.  We can allow for six months to give the MRL time to publish a paper making the case for a fixed ring size as @fluffypony has suggested. Also the fixed ring size would not be tested against the current broken situation but against  the idea proposed by @dnaleor. 

## fluffypony | 2018-08-22T04:51:18+00:00
@iamsmooth I don’t disagree, but my recommendation has *always* been that the dev workgroup chooses to implement recommendations by the research lab. I fear we’ve become so accustomed to doing it the other way that we we no take that as the norm.

I also think we’re at a high enough min ring size that most of the obvious attacks are quite mitigated.

I like @articmine’s idea of putting a paper out that compares both ideas, if that’s not massively objectionable.

## iamsmooth | 2018-08-22T05:04:17+00:00
@fluffypony This is a recommendation from the research lab. At least one of the researchers (I don't remember which one) has been informally recommending this for 1-2 years at least. Maybe we just need them to write up a half page research note stating that?

## ArticMine | 2018-08-22T05:22:18+00:00
@iamsmooth I agree with the process issue of late comers disrupting existing consensus; however sometimes there is significant value to look at ideas that solve most of a problem while avoiding long term issues especially in the case of consensus code. In this case I would put  @dnaleor idea in that category.  

I see @dnaleor idea as a solid stepping stone while the paper is produced. It is also no secret that the MRL see ring signatures as a weak point. 
.


## iamsmooth | 2018-08-22T05:23:47+00:00
@ArticMine In the event of an unforeseen situation such as XMV (or really for any reason), one can achieve the same effect of ring size N*2 (minus 1) by performing one round of churn with ring size N (with sensible delay to prevent the obvious timing attack). An attacker would have to control all of the fake outputs on _both_ of the transactions to successfully identify the true source, which is really the same as one transaction with twice the ring size. This introduces an undesirable time delay, and some additional cost for the additional outputs (much smaller with bulletproofs), but I don't find that objectionable considering we are looking at a "how to mitigate some unforeseen disaster" scenario. 

Perhaps this can be addressed in a paper. 

In practice, we will still see (as we always have) that these non-standard ring sizes are almost never used anyway, so I guess from that perspective the objective harm is low of not fixing it is somewhat low. I would say this is largely true whether or not @dnaleor 's proposal is adopted.

**Still, I very much do not like the process of people showing up at the last minute and throwing bombs at work that other people have contributed to and collaborated on for months/years (without the bomb throwers having identified and clearly-articulated a serious problem that everyone else has missed). Nor do I like the precedent of backing out code which has already been implemented, reviewed and merged as a result of this lengthy collaboration, also due solely to last minute bomb throwers. I feel it is a mistake to proceed on that basis, and it emboldens future bad actors.**

I would rather see the MRL researchers promptly write a brief research note documenting and explaining their (otherwise somewhat informal) recommendation which gave rise to the aforementioned implementation, but of course that is up to then, as I won't volunteer someone else's effort.

## iamsmooth | 2018-08-22T05:55:59+00:00
BTW, this issue is indeed addressed, if somewhat indirectly, in MRL-0004, specifically section 3.2

> Any data available to an observer about the transactions used to fashion a ring
signature can be used in a combinatorial analysis to draw a conclusion about funds
ownership ... This information can be used in tandem with other routes of attack ... Our definition of a combinatorial attack seems strikingly general ...

A fixed ring size is minimizing the attack surface of "Any data available to an observer about the transactions"


## ArticMine | 2018-08-22T05:58:55+00:00
@iamsmooth Actually in the XMO case  I do not see churning as equivalent since the point of the large ring size was to have enough pre fork fake inputs to allow for an effective 5-7 ring, by literally brute forcing the selection algorithm.  This is actually not necessary in the case of XMV since it supports the mitigations. I do recognize this is an edge case nevertheless it does provide an argument because it was unforeseen. I do agree that in most cases properly timed churning may address the additional privacy issue.

The bad actors argument is of course a very legitimate one; however it also has to be balanced with not allowing process to be so rigid as to effectively negate what may turn out to be a very legitimate proposal that was not made by a "bad actor". 



## ArticMine | 2018-08-22T06:15:36+00:00
> A fixed ring size is minimizing the attack surface of "Any data available to an observer about the transactions

... and what was proposed by @dnaleor is to for example reduce this attack surface between 11 and 200 ring sizes from 189 possible ring sizes to 5 possible ring sizes. 

It is not the kind of proposal that a "bad actor" would propose because it is very constructive, so the bad actor gain is debatable at best. 

I can support a fixed ring size of 11 or @dnaleor's proposal as 11, 22, 44, ... etc. I am not supporting leaving the 1 ring increments since then the "bad actors" would win.  

## iamsmooth | 2018-08-22T06:45:19+00:00
@ArticMine 

In the case of using churn to mitigate XMV, the transactions would need to be constructed to ensure that, across the two, they have a minimum number of pre-fork outputs. From the perspective of tracing, one can view the sequence of TX_a(ring size=N)->TX_b(ring size=N)->destination as equivalent to TX_c(ring_size=2N-1)->destination. The reason being that if the attacker manages to trace TX_b (which requires excluding N-1 fake outputs), they can only get to the original source if they _also_ trace TX_a (which requires excluding _another_ N-1 fake outputs). So the resulting number of outputs that need to be excluded is 2N-2, which is the same as what is required to trace TX_c.

To ensure that the combination of TX_a and TX_b have a sufficient number of pre-fork outputs in the XMV case requires a wallet change to implement, but so would (and did) doing the same thing with one larger ring.

As for bad actors, I wasn't actually accusing anyone of being a bad actor _in this case_. I was suggesting that removing a useful improvement (part of a long process of continuous improvement which has resulted in a much stronger Monero) on the basis of vague last minute objections from non-participants would embolden bad actors in the future. 

I agree that @dnaleor's suggestion is certainly not coming a bad actor and in fact he _has_ made that or a very similar suggestion previously in the process.


## ArticMine | 2018-08-22T06:59:12+00:00
@iamsmooth For XMV what you suggest above works because XMV supports the mitigation that were added after the XMO fork. So one could construct transactions on both chains with common pre fork outputs. XMO on the other hand does not support the mitigations. With XMO, short modifying the wallet code, the only way to generate the required 5-7 pre fork outputs in a post fork XMO spend was to drastically increase the ring size so the the algorithm would chose about 5 - 7 pre fork outputs. These pre fork outputs could then be imputed into the subsequent XMR spend. 

## iamsmooth | 2018-08-22T07:04:43+00:00
@ArticMine 

> the only way to generate the required 5-7 pre fork outputs in a post fork XMO spend was to drastically increase the ring size so the the algorithm would chose about 5 - 7 pre fork outputs. These pre fork outputs could then be imputed into the subsequent XMR spend

We're veering off topic a bit here, but that doesn't seem like a very good mitigation to me. Over time the necessary ring size would need to be larger and larger and eventually it would be unlikely to ever get 5-7 pre-fork (once the fork is far enough in the past).

For any desired ring size you can construct a chain (as with TX_a->TX_b above) with the same properties across all of the fake outs within the chain. If you are relying on the statistical random selection of the unmodified wallet to give the necessary outputs (though, as above, this seems poor), then  multiple chained transactions with the same number of total fake outs would have the (statistically) same total number of pre-fork fake outs.


## ArticMine | 2018-08-22T07:39:06+00:00
Of course it only really works right after the fork, The practical reality however is that over time the problem will likely become moot due to the price of XMO continuing to fall. So those who used this very crude mitigation at the start simply helped accelerate making the problem become moot. 

## SarangNoether | 2018-08-22T11:55:14+00:00
I am in favor of moving to a fixed ring size. New blackball analysis indicates that deanonymization by effective ring size reduction from known outputs is negligible, even at the current minimum. Most recent research into ring-based attacks has focused on output heuristics, leading me to conclude that maximizing transaction entropy provides better protection overall, as @SamsungGalaxyPlayer brought up early in this conversation.

I will state, however, that heuristic-based analysis of transactions is extremely complex, since it is difficult to determine all the metrics an attacker might develop to determine "how suspicious" a transaction appears.

## ArticMine | 2018-08-22T17:55:16+00:00
@Wigmnd There is an overall fallacy here in that only the change needs to be justified with detailed research, and the status quo does not. One can equally ask the question where is the research that justifies the status quo in this case?

## SamsungGalaxyPlayer | 2018-08-22T17:57:07+00:00
@Wigmnd we do not have all the facts available. However, the situation as it currently exists is the following:

1. There is some evidence that suggests an unusual ringsize is harmful.
2. Very few people use a non-default ringsize.
3. There is no evidence to suggest a non-default ringsize is effective under any known use-case.
4. Surae and Sarang support a fixed ringsize.
5. The code has already been written for a fixed ringsize.

I believe that while not every point of research has been evaluated, the preponderance of the evidence points towards supporting a fixed ringsize. Since the supporting reasons for a non-fixed ringsize have received little support, I feel more comfortable with a fixed ringsize than a non-fixed ringsize, even if there isn't significant evidence showing the exact implications of non-fixed ringsize harms in every known use-case.

Under every situation that has been brought up for increasing the ringsize above the minimum, churning has been shown to be a more effective solution. We can limit our attack surface to timing, not both timing and ringsize. I think that even without the full impact of this being presented in a research paper, it is clear enough that most developers and the Monero researchers concur that a fixed ringsize is preferable unless evidence to the contrary can be presented.

**While we do not have all the evidence in the world to support a fixed ringsize, we have more evidence to support a fixed ringsize than a non-fixed ringsize. Thus, we should move to set a fixed ringsize.**

@dnaleor has a middle-ground that may seem like a good compromise, but I generally disagree. While it would limit the attack surface, it will have nearly no impact in my estimation. Since people today rarely use non-default ringsizes, I do not believe that this will change, even with fewer options. It will in effect result in the status-quo. We can always increase the ringsize again in the future if new attacks are discovered. It's not like end-users will magically know what ringsize is best anyway for currently-unknown theoretical attacks.

## fluffypony | 2018-08-22T17:59:13+00:00
@Wigmnd sorry but the absence of a published paper does not imply that "actual research" has not happened. We *know* that transaction uniformity is a goal in enhancing Monero's privacy, and that means uniformity in ring size as well. That there isn't a formal paper is evidence of how obvious this is, not of a lack of research.

## b-g-goodell | 2018-08-22T18:48:28+00:00
I'm going to respond first with my recommendations, and in a moment I'll make another comment responding to specific commenters.

TLDR of my conclusion first:  We should use a fixed ring sizes, and this ring size should increase occasionally.  This ring size should probably not exceed 25 without a change in our ring signature algorithm. Ring sizes as low as 11 may, in fact, be insufficient to guard against certain statistical methods of linkability for targeted individuals. For efficiency reasons, it is reasonable for Monero to begin using Matthew Green's ["How to Squeeze a Crowd"](http://spar.isi.jhu.edu/~mgreen/mixing.pdf) for further blockchain pruning for ring sizes in this range.

All the above recommendations are loosely based on the following idea, with an arbitrary 1% threshold: improving privacy by reducing a the true-positive rate of a single-sample test in a simple linkability analysis to under 1% is wasteful.

These recommendations are based on some catch-and-release-style statistical models of Monero blockchain linkability (see below) laden with assumptions (ugh) together with some (ugh) heuristic arguments. However, we have some independent verification: my results are not dissimilar from the simulation results by sgp, showing marginal gains for large ranges of possible ring sizes. The 1% threshold was selected somewhat arbitrarily based on a "controlled purchases" model of tracking money, under the assumption that this attack would have to be executed sequentially (at the expense of the attacker) to collect a sufficient sample size to obtain practically useful true positive rates.

I do not make complete, formalized arguments here, I am merely presenting the *beginning* of my work on the matter; either way, the Monero community ought not wait on the entire analysis before making decisions based on some preliminary results.

**General stuff first.** This is a discussion that normally would not require any input from the community. Why? Ring size is a security parameter, like key length. Larger is generally better for security, at a cost of efficiency. Choosing a fixed security parameter when implementing a scheme is objectively preferable to a non-fixed security parameter, because outputs from the scheme statistically match each other, at least with respect to the security parameter. 

This is why encryption standards recommend common/fixed key and ciphertext lengths. Totally contrived example: all the angels in heaven are assigned a serial number based on when they were created by the almighty, and all use that serial number as their ciphertext and key lengths for the heavenly encryption scheme. Lucifer happens to have serial number 666; it's always easy to tell a ciphertext was encrypted by Lucifer.

Fixed ring sizes increase the indistinguishability of two transactions but they also **remove an avenue of heuristic linkability.** This is so important it cannot be quantified. Cryptography has a long history of people trying to disarm specific heuristics instead of constructing schemes against which heuristics are useless. This removes an avenue of heuristic linking. 

*So, this brings me to the big first point: fixed ring sizes should be included in the next update, and they should increase at least occasionally in future updates.*

**When should we increase ring size?** Any time we have an opportunity to increase ring size to obtain a _non-trivial_ gain in privacy without increasing the overall _weight_ of the blockchain, we should do so. This way, weight always goes down and privacy always goes up. There are also circumstances where we should increase ring size despite overall weight of the blockchain, but that is a discussion for another day, because no one is proposing it here.

The tricky parts of the question: how to define weight and how to define non-trivial?  We've defined weight elsewhere using the total time to download and verify, and we used that to pick our new fee structure for bulletproofs. Based on those approaches, here's a for-instance: we are currently sitting at what looks to be a 80% improvement in Monero's overall speed and efficiency if we take the ring size all the way to 11. This is a five-fold improvement in speed; are the gains we get in ring size non-trivial?

**Catch-and-Release Corrupt Exchange Game:** Assume we have a blockchain with C outputs on it (C for chain). To assess privacy gains against linkability analyses, I constructed the following two-player game using an atomic output-based cryptocurrency network. Alice (a corrupt exchange working with an evil government) sends a set of  B transaction outputs to Bob ~~called the _blacklist, (B for blacklist)_~~ a better way to think of these are as a list of _tagged_ transactions in a catch-and-release sort of ecological sense. Bob goes about his economic business, presumably churning a bunch, and eventually sends a set of transaction outputs called the _deposit_ back to Alice. Alice outputs a bit, indicating whether Alice thinks any of the outputs in the deposit ``came from'' the ~~outputs in the blacklist~~ _tagged outputs_.
 - If Alice outputs 1 and any ~~blacklist~~ tagged output was truly spent in the history of any deposit output made by Bob, then Alice wins (the value of) her ~~blacklist~~ tagged output back (she caught Bob trying to deposit a ~~blacklist~~ tagged output) so she has a net gain of zero and Bob loses, going to jail. 
 - If Alice outputs 1 and no ~~blacklist~~ tagged output was truly spent in the history of any deposit output made by Bob, then Bob loses, going to jail, but Alice does not get her ~~blacklist~~ tagged output back and her net loss is the value of the B ~~blacklist~~ tagged outputs.
 - If Alice outputs 0 and any ~~blacklist~~ tagged output was truly spent in the history of any deposit output made by Bob, then Bob wins the value of all ~~blacklisted~~ tagged deposit outputs, and Alice's net loss is the value of all B ~~blacklist~~ tagged outputs.
 - If Alice outputs 0 and yet Bob is innocent, Alice loses her B ~~blacklist~~ tagged outputs and Bob gains (and loses) zero.

This is the first step towards making complete, formal treatment of fungibility in cryptocurrencies. In the case that the ~~blacklist~~ tagged list has only one output and Alice wishes to determine whether the output is included in the deposit or not, Alice has only two reasonable hypotheses: H_0, the null hypothesis, is that Bob made no ~~blacklist~~ tagged deposit, and H_1, the alternative, is that Bob made a ~~blacklist~~ tagged deposit. We assume for convenience that B = 1, and we set p = 1/C.

**An analysis based on some assumptions:** Alice has lots of data available from Bob's deposit to come to a conclusion. For example, she can go through every deposit's transaction history on the Monero blockchain and see how many (if any) of his deposits reference the blacklist deposit, and she can compare the distribution of the occurrences of the ~~blacklist~~ tagged list in the deposit history against H_0. If the ~~blacklist~~ tagged outputs occur too often, Alice can accuse Bob.

I assume each layer of outputs in a transaction's history is filled ring members for ring signatures at the previous layer. Each ring member is poison or not. Rings are selected independently from each other. We assume that the attacker has been executing a sustained attack over time such that, for any new ring signature, the probability of any one ring member being a ~~blacklist~~ tagged output is p = B/C = 1/C.

Under these assumptions and H_0, the number X of poison outputs at layer d in an R-ary tree of ring signatures, each with R ring members, is a Binomial random variable with parameters (R^d, p) where p=B/C. Under H_1, on the other hand, X-1 is a Binomial random variable with parameters (R^d - 1, p). The Neyman-Pearson lemma gives us the best possible statistical test to distinguish these hypotheses (hint: if X = 0, H_1 can always be discarded, and the best possible test is monotonic, so our rejection region for H_0 is all X > X_c for some critical X_c, i.e. we disregard the idea that Bob accidentally included a ~~blacklist~~ tagged output as a ring member totally at random if the single ~~blacklist~~ tagged output occurs too many times). Now, here's the fun part: this statistical test has a well-defined *power*, which can be computed numerically, and we can try to make this test as low-power as possible. When we do this, we obtain some nasty summations, but we can apply Chebyshev's inequality to obtain a lower bound.

**Long story short, an attacker doing a catch-and-release style linkability analysis of Monero transactions on a blockchain of C outputs who has released exactly 1 poison output to catch someone performing d churns with a ring size of R has an approximate true positive probability <= C/R^d.**

This is an asymptotic formula justifiable using (1) a binomial model with some specific null and alternative hypotheses, (2) the Neyman-Pearson lemma for finding the best possible statistical test of those hypotheses, and (3) bounding some integrals from below using Chebyshev's inequality. Obviously, if R is too small, this bound is useless, it's bigger than one! This is a consequence of the weakness of Chebyshev's, but that's okay, the inequality still holds. 

For a blockchain with 10^6 outputs on it, a ring size 11, and churning d=5 times, the above test has a true positive probability of *at most* 62% (that ain't good, although it is likely lower due to the weakness of Chebyshev's) but increasing the ring size to 25 brings that true positive probability down to a hair over 1%. To give an idea, a true positive rate better than 50% is actually not super great for ~~us~~ fungibility, which brings me to my second and third major points: *increasing ring size past 25 is probably wasteful, and 11 is arguably too low to guard against certain controlled-purchase catch-and-release-style attacks.*

**Those are unreaslistic assumptions though!** Yeah, they are. If Alice changes her technique, or if Bob selects rings in a way that aren't independent, or does something wonky, then the above model breaks down. But it's a quantitative starting point for assessing "when will increasing ring size be a wasteful decision?" to manage against inadvertent linkability information being leaked.

**One last addition:** Note that the tagged outputs are merely tagged; the terminology "blacklist output" is misleadingly sinister, as some community members have pointed out to me.

## fluffypony | 2018-08-22T19:12:41+00:00
> I apologizes then however this will bring me back to the point that this is using insider knowledge known only to a few and which is not publicly available. If the goal is public consensus you must present those findings to the public and allow time for the public to review them before asking for a pubic consensus. This all has its own issues but I don't want to stray off topic right now.

No, obvious is not the same as insider. Would you consider it "insider knowledge" that √2 is an irrational number? Or would you merely consider that to be something that someone with a sufficient grasp of mathematics would know? I'd argue that the onus is on you to prove you have the background and understanding to present a valid counterpoint, otherwise you're effectively saying "I don't understand this so it shouldn't happen" which is an irrational argument (excuse the pun).

## paulshapiro | 2018-08-22T19:16:46+00:00
lol insider knowledge this has been discussed on IRC for ages

## Gingeropolous | 2018-08-22T19:19:31+00:00
IRC == Insider Relay Chat. ( mic drop )

/ end of issue

## fluffypony | 2018-08-22T19:26:14+00:00
@Wigmnd Nope, you just haven't been paying attention for the LAST TWO YEARS, but everyone else has.

https://monero.stackexchange.com/questions/7233/would-a-fixed-ring-size-improve-anonymity

https://github.com/monero-project/monero/issues/1673#issuecomment-277584232

https://github.com/monero-project/monero/issues/1673#issuecomment-277598381

https://github.com/monero-project/monero/issues/1673#issuecomment-314561088

https://github.com/monero-project/monero/issues/1673#issuecomment-314567593

https://github.com/monero-project/monero/issues/1673#issuecomment-328359308

https://www.reddit.com/r/Monero/comments/8ullip/im_back_with_even_more_monero_subs/e1gsq36/

https://www.reddit.com/r/Monero/comments/92vkdf/july_monthly_report_from_sarang_noether/e38t5je/

https://www.reddit.com/r/Monero/comments/7oy8vx/monero_transactions_are_about_to_get_80_cheaper/dsdmn0u/

https://www.reddit.com/r/Monero/comments/65iund/thoughts_output_selection_and_ring_size_and/

https://www.reddit.com/r/Monero/comments/7y97yo/higher_ringsize_than_the_default_stands_out/duevwc0/

https://www.reddit.com/r/Monero/comments/6zqqvn/is_ability_to_choose_custom_ring_size_a_problem/

https://www.reddit.com/r/Monero/comments/79akfc/who_is_this_person_everyday_he_send_tx_with_41/

https://www.reddit.com/r/Monero/comments/82flll/at_what_block_will_the_fork_happen/dvahsx4/

https://www.reddit.com/r/Monero/comments/6tjy9k/ringct_20_by_sun_et_al_is_this_a_part_of_monero/dllp62y/

https://www.reddit.com/r/Monero/comments/7st3v1/with_bp_incoming_in_september_can_we_start/

## b-g-goodell | 2018-08-22T19:31:19+00:00
@wigmnd rather than providing a detailed response to each of your comments, I'm going to say two things. 

First, I strongly recommend that you read [this book here](https://www.amazon.com/Introduction-Modern-Cryptography-Principles-Protocols/dp/1584885513). You have displayed a disconcerting level of misunderstanding of some very basic properties of crypto schemes like statistical indistinguishability that have been known for decades. Don't hop onto a racecar engine discussion forum with only rudimentary understanding of internal combustion and start giving advice to other forum members. To be as polite as possible: it's a bad look, dude. 

Second, MRL has public meetings once a week to discuss issues like this, and so does monero-dev. You keep saying basic research has not been done, or that it's based on information not available to the public, etc etc, and yet you have not attended a single meeting, you haven't bothered asking for logs, nothing. You come into this conversation as fresh as possible, demanding a complete re-iteration of over a year's of discussions. If you don't think those discussions are public, it's because you haven't looked for them in monero-dev logs, monero-research-lab logs, nowhere. It's not only lazy, it's offensive. It's like a freshman physics student walking into a PhD level class and demanding definitions of every word, and you are totally unaware that you are asking for *years of education to be compressed into a few moments.* You then follow these statements up with "my request for basic information isn't unreasonable" and "I don't want to be rude to the professor but I feel like she should walk us through this info from the start, you know?" 

If you think you are acting in good faith, please take a step back and re-assess your behavior.

## fluffypony | 2018-08-22T19:34:44+00:00
@Wigmnd also less [sealioning](https://www.quora.com/What-is-sealioning) would go a long way to making it look like you're acting in good faith.

## SamsungGalaxyPlayer | 2018-08-22T19:45:02+00:00
@Wigmnd I have written about my points several times. Would you mind condensing your question down? I have discussed the logic behind my position repeatedly over several comments.

## fluffypony | 2018-08-22T20:03:36+00:00
@Wigmnd I've pointed to a bunch of places (not IRC) where it's been discussed over two years, and @b-g-goodell has given you a write-up on why its necessary. I would recommend you go through those, and understand all of them, before you respond to this thread again.

## SamsungGalaxyPlayer | 2018-08-22T20:18:35+00:00
There has been a significant amount of conversation here, and the objection has boiled down to the following:

> There is not a significant amount of evidence that supports a fixed ringsize.

However, MRL and most other devs say that:

> There is more evidence in favor of a fixed ringsize than a non-fixed ringsize.

Given that there are real attacks possible from the metadata revealed from an unusual ringsize, and that there have been no stated reasons why a non-fixed ringsize is better in any scenario, I am going to close this comment since no new topics are being introduced. I strongly recommend that Monero moves to a fixed ringsize in the September/October v8 network upgrade.

I strongly encourage @Wigmnd and anyone else to come up with new evidence to support their position. They can then open a new issue to recommend it is changed back. At the present, we have more reason to make the change than not make the change for all the scenarios and attacks that @b-g-goodell, @SarangNoether, @iamsmooth, @ArticMine, and I have listed.

@Wigmnd we have walked you through a large number of these scenarios. All of us feel comfortable with them. If you are unable to understand the evidence that we have presented, we encourage you to spend more time learning from the resources that we have linked. It is a difficult issue to understand well. Respectfully, the only point you have brought up is that we have not brought up enough points, which the majority of contributors here disagree with. You did not quantify any of your other scenarios, and there was ample evidence to dispute them.

For these reasons and more this discussion is now closed.

# Action History
- Created by: SamsungGalaxyPlayer | 2018-08-05T23:07:40+00:00
- Closed at: 2018-08-22T20:18:35+00:00
