---
title: Monero Research Lab Meeting - Wed 10 September 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1266
author: Rucknium
assignees: []
labels: []
created_at: '2025-09-09T23:45:07+00:00'
updated_at: '2025-09-19T21:07:07+00:00'
type: issue
status: closed
closed_at: '2025-09-19T21:07:07+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Carrot follow-up audit](https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).

4. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).

5. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

6. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064) and [Publish or Perish](https://github.com/monero-project/research-lab/issues/144).

7. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1263 

# Discussion History
## Rucknium | 2025-09-12T19:59:50+00:00
Log

```

> __< br-m >__ <rucknium> Meeting time! https://github.com/monero-project/meta/issues/1266     

> __< br-m >__ <rucknium> 1. Greetings     

> __< br-m >__ <jberman> waves     

> __< br-m >__ <vtnerd> Hi     

> __< br-m >__ <0xfffc> Hi everyone. My apologies. I will absent from today’s meeting, have to take care of a personal business.     

> __< br-m >__ <0xfffc> 9933 is ready.     

> __< br-m >__ <articmine> Hi     

> __< ArticMine >__ Hi from IRC     

> __< rbrunner >__ Hello     

> __< br-m >__ <boog900> Hi      

> __< br-m >__ <jeffro256> Howdy     

> __< guest55 >__ hi (its gingeropolous)     

> __< br-m >__ <ack-j:matrix.org> Hi     

> __< br-m >__ <rucknium> 2. Updates. What is everyone working on?     

> __< br-m >__ <jberman> me: continuing on PR 81 wallet2 FCMP++ refresh refactor updating for jeffro's review comments (PR update incoming today), implemented multithreaded FCMP++ batch verification in the daemon (for txs in a single block), then planning to debug an FCMP++ consensus bug both jeffro and ofrn encountered after the recent round of changes     

> __< br-m >__ <jeffro256> Me: reviewed j-berman's seraphis-migration PR #81 and am working on reorg handling fixes for multisig wallets on upstream. Hopefully improves UX in Haveno     

> __< br-m >__ <vtnerd> Me: knocked out some lws+lwsf bugs, still have to fix auto fee in lwsf. Otherwise been working on carrot in lws, and luckily little changed in the libs such that fcmp++ branch is already compiled and linked into lws. Much work to do with carrot though      

> __< guest55 >__ monerosim - got monero's native p2p discovery working on a simulated internet, txs relaying, can run xmrchain after a sim and browse the blockchain. ramping up to that 1k node mark.     

> __< br-m >__ <rucknium> me: Empirical analysis of risks of rolling DNS checkpoints ("Paths to majority hashpower": https://github.com/monero-project/monero/issues/10064 and https://gist.github.com/Rucknium/fb9a02fbd89c8d93e0d9f48fbc470e05 ). Working on a transaction spamming library for stressnet.     

> __< ArticMine >__ I am working on oprions for the fee scaling and addition of the sanity median. Should have something by the end of this week. Also reviewing POS attacks especially related to cost of capital Also preparing for a talk this Friday.     

> __< br-m >__ <ofrnxmr> Hit 40mb blocks on an fcmp testnet     

> __< br-m >__ <kayabanerve:matrix.org> I announced monero-oxide and the $100,000 bug bounty for it, and the Monero FCMP++ testnet will use the monero-oxide repository for the FCMP++ libraries 🎉     

> __< br-m >__ <kayabanerve:matrix.org> (advertisement for people to come take Power Up Privacy's money by breaking monero-oxide)     

> __< rbrunner >__ kayabanerve: Have a link?     

> __< br-m >__ <jberman> kayabanerve:matrix.org: (repeating from NWLB, this means tx construction time for large input txs will have the latest faster impl, where higher n inputs takes n times as long to construct)     

> __< br-m >__ <kayabanerve:matrix.org> rbrunner: To monero-oxide or the $$$?     

> __< br-m >__ <rucknium> 3. Carrot follow-up audit (https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).     

> __< rbrunner >__ Why not both? :)     

> __< br-m >__ <kayabanerve:matrix.org> https://github.com/monero-oxide/monero-oxide     

> __< br-m >__ <kayabanerve:matrix.org> https://immunefi.com/bounty/monero-oxide     

> __< rbrunner >__ Thanks!     

> __< br-m >__ <jeffro256> Not much to report about the Carrot follow-up audit, Cypherstack hasn't responded last week     

> __< br-m >__ <jeffro256> Will probably ping them in the next couple days      

> __< br-m >__ <freeman:cypherstack.com> I believe the plan is a response later today, but let me verify      

> __< br-m >__ <jeffro256> Awesome, thanks a lot freeman:cypherstack.com!     

> __< br-m >__ <rucknium> 4. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).     

> __< br-m >__ <rucknium> If no objection, I will limit discussion of this item to 30 minutes.     

> __< ArticMine >__ I expect to have options for this later this week based upon keeping the minimum penalty block weight at 1 MB     

> __< br-m >__ <jberman> Going to raise this point I raised in NWLB again: voicing my own support for ArticMine 's latest fee proposal to scale fee by tx byte size alone without considering verification time, considering tx size as a whole actually does increase a significant amount as n inputs increases beyond just membership proofs size     

> __< ArticMine >__ I should point out that large transactions are a problem. for example 50% of the ZM we are looking at 25% of the block reward to scale and 50% if they are competing with smaller transaction in the same fee tier      

> __< br-m >__ <ofrnxmr> I would argue that we should charge by input count instead of byte size, which (to end user) makes 1 inout vs 128 input scale linearly, but to node runners / miners, it means higher per-byte fee for higher input txs     

> __< ArticMine >__ We can to a degree factor in verification time, but the reality is that when transactions are over 4% of ZM thinng do start to break down     

> __< ArticMine >__ The penalty does not see number of inputs it only see weight     

> __< br-m >__ <jberman> kayabanerve:monero.social raised objection to this in favor of instead implementing an approach that incentives multiple lower input over single high input txs (with the underlying goal being to nudge the ecosystem toward low input uniform txs), and stated satisfaction with no incentive either way toward low input or high input (i.e. perfectly linear weight increase)     

> __< ArticMine >__ Ultimatly the penalty drives fees     

> __< br-m >__ <jeffro256> ArticMine: Yes miners only care about weight, but weight can defined however we want it to be     

> __< ArticMine >__ Yes this is an option     

> __< ArticMine >__ for example incentivzing up to 8 inputs     

> __< br-m >__ <ofrnxmr> Incentivizing chain bloat doesnt make sense to me.     

> __< ArticMine >__ It is the 32+ inputs that start to be a problem     

> __< ArticMine >__ The idea is to incentivise wallet maintenance with say 4 inputs etc. It is something I support     

> __< br-m >__ <ofrnxmr> its not something i support at all     

> __< br-m >__ <jberman> From the perspective of minimizing chain size and verification time, 32+ input txs are strictly better than 4+ 8-input txs     

> __< br-m >__ <ofrnxmr> I can only reach 40mb blicks easily by abusing 2input txs     

> __< br-m >__ <jeffro256> ArticMine: is this 4% of Zm figure coming from the fact that it starts to be very profitable to start solving the discrete optimization problem for transaction inclusion versus approximating it? > <ArticMine> We can to a degree factor in verification time, but the reality is that when transactions are over 4% of ZM thinng do start to break down     

> __< ArticMine >__ Shure but they simple do not scale      

> __< ArticMine >__ Yes that is part of it     

> __< br-m >__ <ofrnxmr> incentives to force merchants, exchanges, or users to make excessivelt large txs makes no sense to me     

> __< br-m >__ <jeffro256> What is the other part?     

> __< br-m >__ <ofrnxmr> If i can send 128input tx at say, 1.5kb per input, why should i be forced to split that up into 2.5+ kb/input? thats just bloat for no reason. Sure it charges more money, but its huge     

> __< ArticMine >__ but even simple approximations to optimize discrete optimization problem come in. Fore example priortizing small transaction wtihin a fee tier      

> __< br-m >__ <ofrnxmr> You can charge more per-byte for large input txs by "simply" charging "static" fees per input     

> __< ArticMine >__ If we set a fixed weight for the proofs that is what we are doing      

> __< ArticMine >__ We need that anyway for FCMP+     

> __< ArticMine >__ I mean 128 input tx can be an attack vector     

> __< br-m >__ <jberman> Has anyone stated an explicit objection toward linear increasing weight (i.e. 128 input has ~128x the weight of 1-input)?     

> __< br-m >__ <jeffro256> I prefer that at the moment     

> __< br-m >__ <jberman> Seems the approach that's most likely to get consensus imo     

> __< ArticMine >__ You want to apply this to the membership proof?     

> __< ArticMine >__ It can be done     

> __< br-m >__ <jberman> It probably makes more sense to be applied toward tx weight as a whole, because tx weight overall is where incentives apply     

> __< ArticMine >__ ... but we still have to pay the higher fee rate at least above 8in     

> __< ArticMine >__ we have to deal with the penalty     

> __< tevador >__ I disagree with a 1MB penalty free zone. That's unnecessarily large.     

> __< br-m >__ <jeffro256> I say b/c of all the battling interests and opinions, we go with the simplest reasonable weighting system (linear wrt input count roughly following byte count).     

> __< ArticMine >__ There is a lot of evidence it is not     

> __< ArticMine >__ Starting with fees vs adoption     

> __< ArticMine >__ if we increase the tx wieght by a factor of 4 we need to increase the penalty free zone     

> __< ArticMine >__ it actually shoud be 1.2 MB     

> __< tevador >__ Before bulletproofs, we had much larger transactions and a much smaller penalty free zone.     

> __< br-m >__ <jeffro256> I still don't understand why, though     

> __< ArticMine >__ ... and adoption was lover by a factor of 5      

> __< ArticMine >__ on chain adoption     

> __< tevador >__ That's what the dynamic scaling is for.     

> __< tevador >__ A large penalty free zone invites spam.     

> __< ArticMine >__ No if you start with very hign fees that merket just walks away     

> __< br-m >__ <jeffro256> Why does a 4x increase in transaction weight necessitate a ~3.33x increase in the minimum penalty free zone? The median transaction size will still be significantly smaller than the minimum penalty free zone     

> __< br-m >__ <jeffro256> ArticMine: You said last meeting that you would also want an increase in fees     

> __< ArticMine >__ https://bitinfocharts.com/comparison/monero-transactions.html#log&alltime Just take a look at the evidence     

> __< tevador >__ Last meeting I calculated a tx fee of $0.03 with a penalty free zone of 600KB. That's not very high.     

> __< ArticMine >__ Actually at the height of the recnet bul market is is highe     

> __< ArticMine >__ and transaction barely scale     

> __< guest55 >__ and how many txs fit in 600 kb?     

> __< ArticMine >__ That is not the point.     

> __< ArticMine >__ it is the fee that have to be paid to scale     

> __< br-m >__ <ofrnxmr> ~80     

> __< tevador >__ We can adjust the long term median at hardfork to match the historic tx volume with the new reference tx size.     

> __< br-m >__ <ofrnxmr> but we avg abt 40tx/block atm     

> __< br-m >__ <jeffro256> 95 1-in/2-out, if going purely off raw byte size      

> __< ArticMine >__ as it is we are barely able to scale and there was an attack recently to prove that     

> __< guest55 >__ barely able to scale as in the dynamic blocksize didn't kick in?     

> __< ArticMine >__ Wen we kept ZM at 300000 bytes after bulletproofs adoption increased by a factor of 5x     

> __< tevador >__ I fail to see the causal connection.     

> __< br-m >__ <blurt4949:matrix.org> correlation is not causation.      

> __< ArticMine >__ I mean Please take a look at the blocksize evidence     

> __< ArticMine >__ it is not casual     

> __< ArticMine >__ there is also evidence of a small drop in adoption after the last fee increase     

> __< br-m >__ <ofrnxmr> The blocks didnt grow during the spam attack due to the auto-fee not using the "normal" fee tier     

> __< ArticMine >__ Which means that the minimalistc fee calculated at 600000 ZM does not work     

> __< br-m >__ <ofrnxmr> the unimportant fee tier (afaik) isnt supposed to trigger scaling     

> __< tevador >__ Look at what happened to zcash with their generouly low fee policy.     

> __< ArticMine >__ Zcash is totaly broken. Monero is not     

> __< ArticMine >__ We have tight pricing     

> __< br-m >__ <jeffro256> I think it simply means that it was a bug in the wallet, not a protocol issue. It does matter what dynamic sizing policy we have in place if wallet2 screws it up lol     

> __< tevador >__ If "drop in adoption" means "less spam", then I take it as a success.     

> __< ArticMine >__ That was part of it. the bug was that the wallent did not incentivse an increase in fees     

> __< ArticMine >__ not is not less spam is is real adoption. this is acompetiive market     

> __< tevador >__ Yes, that's another issues. AFAIK wallet2 does not look into the tx pool at all when estimating the required fee.     

> __< br-m >__ <ofrnxmr> it does tevador     

> __< ArticMine >__ It is very much related     

> __< br-m >__ <jeffro256> IMO, we can keep tight pricing by not increasing the minimum penalty free zone, while always still allowing it to scale if people are willing to pay the fees to offset block reward. I don't really care if fewer people are putting <1 US cent microtransactions on the L1 b/c the fee is now 3 cents     

> __< br-m >__ <ofrnxmr> It checks if there is > 0 blocks backlog, or if recent blocks are >80% of the penalty free zone     

> __< ArticMine >__ It is more like 0.10 USD minimum     

> __< tevador >__ It should also take into account the fees in the tx pool.     

> __< ArticMine >__ In fact if we want to increase fees increasing the scaling rate to 2 % is a uch better way to go     

> __< tevador >__ If there was a backlog e.g. at the high fee level, it makes no sense to send a tx with the a normal priority fee.     

> __< br-m >__ <ofrnxmr> it does tevador, thats how it calc the backloh     

> __< ArticMine >__ People do this     

> __< tevador >__ OK, then the dynamic scaling should be able to kick in when needed.     

> __< br-m >__ <rucknium> 30 minutes have elapsed since discussion started on this item. It will be discussed next week. Moving to next agenda item:     

> __< br-m >__ <rucknium> 5. FCMP alpha stressnet planning (https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< ArticMine >__ In any case I am not supporting less that 1 MB for ZM     

> __< ArticMine >__ there simly is not the case for this     

> __< br-m >__ <ofrnxmr> Fcmp repo is a bit broken right now, so probably after its fixed :P     

> __< br-m >__ <ofrnxmr> As jberman noted in his opening statement     

> __< rbrunner >__ I learned in Monday's meeting that PR #81 is a quite complex affair     

> __< br-m >__ <jberman> Re: alpha stressnet. Aiming to get 81 in today, then will debug the current consensus failure. Considering the scope of current changes, once 81 is in and bug is solved, I would feel more comfortable with giving ofrn a couple more days to continue on his stressnet, to make sure everything is smooth on top of that latest state     

> __< br-m >__ <jberman> Sorry, wrt 81, I'm aiming to have it ready for jeffro's review today*     

> __< br-m >__ <jberman> 81 has become a bit of a beast, and we'll want to be sure it's totally smooth before rolling out the stressnet     

> __< br-m >__ <jberman> One bright side to this is that the functional tests have been beefed up quite a bit for wallet sync testing     

> __< br-m >__ <rucknium> ofrnxmr:monero.social and I are working on separate transaction spamming codebases. It's sort of redundant work, but it helps exercise different code paths in the node and wallet especially.     

> __< br-m >__ <ofrnxmr> rucknium:monero.social  i'm using wallet-rpc with 30 wallets and can definitely not produce >5mb blocks within 2mins     

> __< br-m >__ <ofrnxmr> at best, i think i can produce about 2mb per min     

> __< br-m >__ <rucknium> My dev & testing has been with ordinary RingCT testnet so far.     

> __< br-m >__ <rucknium> It could be useful to spread the spammers to even more machines. Last stressnet last year, some participants were asking how they could do their own spamming. At that time, the answer was "write your own spammer".     

> __< br-m >__ <ofrnxmr> http://stressgguj7ugyxtqe7czeoelobeb3cnyhltooueuae2t3avd5ynepid.onion/block?id=4592     

> __< br-m >__ <ofrnxmr> (block explorer for my stressnet)     

> __< br-m >__ <rucknium> I took what I wrote last year and I'm making it more production-ready. Handling crashes & restarts, etc. That way, ordinary users could potentially use it.     

> __< br-m >__ <rucknium> Or, at least, there will be less manual management if I'm the only one using it.     

> __< br-m >__ <rucknium> Anything more on stressnet?     

> __< br-m >__ <jberman> what block explorer code is that? haven't seen that format before     

> __< br-m >__ <ofrnxmr> thats duggavo's     

> __< br-m >__ <ofrnxmr> duggavo:matrix.org     

> __< br-m >__ <jberman> cool     

> __< br-m >__ <ofrnxmr> https://github.com/duggavo/MoneroBlock     

> __< br-m >__ <rucknium> 6. Mining pool centralization: Temporary rolling DNS checkpoints (https://github.com/monero-project/monero/issues/10064) and Publish or Perish (https://github.com/monero-project/research-lab/issues/144).     

> __< rbrunner >__ Wonder whether that will get updated for FCMP++, that block explorer ...     

> __< rbrunner >__ Or does it work already with that?     

> __< br-m >__ <ofrnxmr> rbrunner: already     

> __< br-m >__ <ofrnxmr> That is fcmp     

> __< rbrunner >__ Ah, of course. Dumb question.     

> __< br-m >__ <ofrnxmr> It just uses rpc to ask for info from each block     

> __< br-m >__ <ofrnxmr> It doesnt show any tx details, nor have pagination. Very bare bones, but good enough for now     

> __< br-m >__ <rucknium> With DataHoarder 's helped, I pulled together data to get an idea of how much hashpower share Nanopool, MoneroOcean, SupportXMR, and Hashvault have during Qubic's activities. The plots are in issue #10064     

> __< br-m >__ <ofrnxmr> For dns checkpoints: i'll probably push a draft pr with some proposed changes. Hopefully we can build on it and get it ready for merge     

> __< br-m >__ <ofrnxmr> The non-code issues need to be stored out, namely depth of checkpoints and how many to store.     

> __< br-m >__ <rucknium> My acronym for these four pools is "NOSH". In 2023, the NOSH mining pools changed their block template config to help confirm transactions more quicky.     

> __< br-m >__ <rucknium> Therefore, they may be open to enforcing rolling DNS checkpoints.     

> __< br-m >__ <ofrnxmr> p2pool also changed recommendation to enforce checkpoints     

> __< br-m >__ <rucknium> However, their combined hashpower is barely above a majority at certain times. The safety margin may be uncomfortably thin.     

> __< DataHoarder >__ P2Pool v4.10.1 was released including Monero block broadcast for non-p2pool blocks https://github.com/SChernykh/p2pool/releases https://www.reddit.com/r/Monero/comments/1ncde8h/psa_p2pool_v410_update_will_speed_up_the_whole/     

> __< DataHoarder >__ This will help broadcast all blocks faster across Monero (and in some cases help push alternate chains)     

> __< br-m >__ <rucknium> Anyone know what happens when p2pool miners in a single side chain (e.g. main, mini, or nano) mine on top of different alt chains?     

> __< DataHoarder >__ this is effectively a faster block propagation network, no need to mine to use this both for receiving or sending blocks founds     

> __< DataHoarder >__ rucknium: that can happen due to normal reasons (specially with laggy miners) so it shows a warning to them and others     

> __< DataHoarder >__ if they diverge too many heights they get "banned" by peers     

> __< br-m >__ <rucknium> And what happens in the side chain? Side chain accepts or rejects these "conflicting" shares?     

> __< DataHoarder >__ if they are too stale or diverging the peer is banned (and share not accepted)     

> __< DataHoarder >__ 10 blocks I believe from checking the code     

> __< br-m >__ <rucknium> Whether p2pool miners enforce DNS checkpoints depends on the monerod node config, not on the actual p2pool software config AFAIK. (Saying for clarity)     

> __< DataHoarder >__ correct.     

> __< DataHoarder >__ each peer mines on their own or with agreeing peers     

> __< br-m >__ <ofrnxmr> proposed changes:     

> __< br-m >__ <ofrnxmr> 1. 300 seconds check     

> __< br-m >__ <ofrnxmr> 2. BFT consensus (2/3 +1)     

> __< br-m >__ <ofrnxmr> 3. Ban time reduced to 5mins     

> __< br-m >__ <rucknium> It's hard to recruit p2pool in DNS checkpointing, ironically due to its decentralized nature.     

> __< br-m >__ <rucknium> p2pool has more hashpower than MoneroOcean and C3Pool     

> __< DataHoarder >__ we updated recommendations, and defaults in the Docker setup     

> __< DataHoarder >__ people can make some noise, but even today there's people running old p2pool versions :)     

> __< br-m >__ <ofrnxmr> We might be able to get c3pool on board as well     

> __< DataHoarder >__ the majority of miners updates within a few days (software wise) but some major ones lag a few versions behind     

> __< br-m >__ <rucknium> ofrnxmr:monero.social: Another possible change is nodes remembering or forgetting DNS checkpoints that are no longer in the set of active DNS records.     

> __< br-m >__ <rucknium> AFAIK, now node remember the checkpoints (until restarted).     

> __< DataHoarder >__ the majority of p2pool miners are running any of the recent versions in the past weeks     

> __< br-m >__ <ofrnxmr> They remember, yeah     

> __< br-m >__ <rucknium> It has its advantages and disadvantages     

> __< DataHoarder >__ alternatively for the remember issue the opposite checkpoints could be set to "delete" old ones if this is supported     

> __< tevador >__ Do we have 7 domains? For 5/7 checkpoint consensus.     

> __< br-m >__ <rucknium> Disadvantage: Edits to DNS records cannot change the chain fork that the enforcing nodes are on. If something goes wrong, it is hard to back out     

> __< DataHoarder >__    /say // return false if adding at a height we already have AND the hash is different     

> __< DataHoarder >__     if (m_points.count(height))     

> __< DataHoarder >__ no checkpoints cannot be taken back ^     

> __< br-m >__ <rucknium> Advantage: Because it is nearly impossible to back out of a defense, a selfish miner may be more hesitant to launch a big attack.     

> __< DataHoarder >__ it errors with "Checkpoint at given height already exists, and hash for new checkpoint was different"     

> __< br-m >__ <ofrnxmr> moneropulse.ch, moneropulse.de, moneropulse.co, moneropulse.se, moneropulse.org, moneropulse.net, moneropulse.fr     

> __< DataHoarder >__ note if setup well the subdomain keys can be split from main one ^     

> __< DataHoarder >__ so full control of main domain is not necessary for the checkpointing system     

> __< br-m >__ <rucknium> rucknium: Similar to the logic of https://en.wikipedia.org/wiki/Dead_Hand     

> __< tevador >__ Who controls these domains?     

> __< br-m >__ <ofrnxmr> Binaryfate     

> __< tevador >__ It would be better if it wasn't a single person controlling all 7.     

> __< br-m >__ <rucknium> > The purpose of the Dead Hand system, as described in the book of the same name,[8][9] was to maintain a second-strike capability, by ensuring that the destruction of the Soviet leadership would not have prevented the Soviet military from releasing its weapons.[2]     

> __< br-m >__ <ofrnxmr> Right? 😁 we can always add / remove some     

> __< br-m >__ <rucknium> DataHoarder had an idea to delegate and disperse DNS record management.     

> __< br-m >__ <rucknium> I made this draft diagram of how the system could work (click the arrows at the bottom to page through the "slides"): https://cryptpad.disroot.org/diagram/#/3/diagram/view/6ab5ffc35d0775e5216a179a42bcd1e2/embed/     

> __< DataHoarder >__ not just management (ownership) but using DNS delegation for the checkpointing subdomain, the main domain can be kept well secured, while updates to the checkpointing subdomain can be done offline -> then pushed to DNS secondary servers that do not have the keys     

> __< br-m >__ <blurt4949:matrix.org> Qubic is clearly willing and able to rent large amounts of hashpower for a few hours. Rolling DNS checkpoints could lead to very deep reorgs so long as Qubic could get enough HP so that NOSH has <50%.     

> __< DataHoarder >__ using such a system refresh times can be lower than 10 seconds, but I wouldn't recommend a lower TTL than 5 minutes due to DNS     

> __< br-m >__ <rucknium> DataHoarder suggested that the big "secure server" in the middle of the diagram could be separate secure servers     

> __< br-m >__ <blurt4949:matrix.org> Even if they lose the fork eventually, i wouldn't put it past them to do it just for fun     

> __< br-m >__ <chaser> rucknium: rucknium:monero.social the link isn't a share link     

> __< DataHoarder >__ you need to use the share function, rucknium     

> __< br-m >__ <rucknium> no?     

> __< br-m >__ <ofrnxmr> blurt4949:matrix.org: Theyd have to sustain that >50% indefinitely     

> __< DataHoarder >__ I believe this is the diagram https://cryptpad.disroot.org/diagram/#/2/diagram/view/glZWi196m1pxGKKdZZKC66exXJAm9WiJsQvN8kJutOM/     

> __< DataHoarder >__ the view key changes once loaded     

> __< br-m >__ <rucknium> That link used to work AFAIK. Try this: https://cryptpad.disroot.org/diagram/#/2/diagram/view/glZWi196m1pxGKKdZZKC66exXJAm9WiJsQvN8kJutOM/     

> __< br-m >__ <rucknium> blurt4949:matrix.org: Yes. This makes me nervous.     

> __< br-m >__ <blurt4949:matrix.org> ofrnxmr:monero.social: no, I mean they rent enough hashpower to get non-DNS above >50%, get a selfish mining start to fork the DNS and non-DNS network, then maintain the fork for a few hours. After their rental is over, likely another few hours for the DNS side to catch up, and suddenly we're looking at 8 hour reorgs.     

> __< DataHoarder >__ As shown last time I have been running my own direct DNS server for checkpointing subdomains https://git.gammaspectra.live/P2Pool/monero-highway#cmd-dns-checkpoints with a list of necessary setup     

> __< DataHoarder >__ Note this software is NOT necessary, it was written to ensure quick replication and limited subset to support DNSSEC     

> __< DataHoarder >__ An alternate DNS server can be used like bind, to then push records to secondaries or serve DNS queries on its own     

> __< br-m >__ <rucknium> DataHoarder: I was able to follow your steps and set up delegated DNS checkpointing for testnet     

> __< br-m >__ <rucknium> blurt4949:matrix.org: Because of the risk, DNS checkpoints could be set up to only activate if there were an attempted 10+ block re-org. Then, Qubic can do what it wants below 10 block re-orgs.     

> __< br-m >__ <rucknium> It would be risky on both sides for Qubic to re-org above 9 blocks, because of the DNS checkpoint punishment strategy.     

> __< DataHoarder >__ the possible damage / marketing would already be done at that point, unless the checkpoints are issued immediately (automated) in case such a reorg is detected     

> __< br-m >__ <blurt4949:matrix.org> rucknium:monero.social: okay? So they attempt to selfish mine a 10 block alt chain, then release it, and do the same procedure as before     

> __< DataHoarder >__ then kept forever afterwards     

> __< br-m >__ <ofrnxmr> blurt4949:matrix.org: More like a few mins to catch up     

> __< br-m >__ <blurt4949:matrix.org> Qubic is not a rational actor, at least not without considering externalities.      

> __< br-m >__ <blurt4949:matrix.org> The "punishment" doesn't work     

> __< br-m >__ <rucknium> I don't think that Qubic wants to facilitate accidental or deliberate double-spends because they can be punished for that by de-listings on exchanges, which would be the usual victim of that.     

> __< br-m >__ <blurt4949:matrix.org> ofrnxmr:monero.social: Depends on how much above 50% they can get the non-DNS side. Either way, at least a few hours     

> __< DataHoarder >__ For the punishment to work it has to be automatic, on detection of such a reorg attempt     

> __< br-m >__ <ofrnxmr> I don't think we should focus on what qubic, as a public pr campaign, would do, but what someone unknown actor could do     

> __< DataHoarder >__ ^     

> __< br-m >__ <blurt4949:matrix.org> rucknium:monero.social: how sure are we of that?     

> __< DataHoarder >__ Anyone could be working in secret to release a 20+ reorg at their chosen timing     

> __< br-m >__ <ofrnxmr> blurt4949:matrix.org: I sincerely doubt that. To get a few hours ahead, theyd need 8gh     

> __< br-m >__ <ofrnxmr> At 4gh, their chain grows at the same speed as the honest chain.     

> __< DataHoarder >__ A system that follows the grim trigger would also need to trigger in such a case automatically, even with distinct controlling entities, so they all have to follow the same logic and share information in excess (ie, not just existing chain they follow, but any other alternates they are aware of)     

> __< br-m >__ <blurt4949:matrix.org> ofrnxmr:monero.social: I mean, total reorg size of a few hours. As long as the non-DNS side is above 50%, they should be able to maintain the lead. You're right that a few hours for the DNS side to catch up post-rental is probably excessive, but the point stands     

> __< br-m >__ <blurt4949:matrix.org> few extra hours*     

> __< br-m >__ <rucknium> blurt4949:matrix.org: Not very sure. AFAIK, this scenario is unprecedented. Another blockchain attacking another. The only other possible precedent I can think of is SHA256 miners attacking Bitcoin Cash and Bitcoin Satoshi Vision. But that's not very comparable.     

> __< br-m >__ <rucknium> And, doing it as an identifiable entity.     

> __< br-m >__ <ofrnxmr> i think always-on checkpoints are better, since it prevents the reorg in the first place     

> __< br-m >__ <blurt4949:matrix.org> rucknium:monero.social: Exactly, we have no precedent. And we are already very aware that Qubic is willing to "burn" money on attacking Monero for PR purposes. Shouldn't this attack itself get them delisted under this logic? I suppose allowing for double spends is different, but they were already planning to do that after most major exchanges increased their conf number     

> __< br-m >__ <ofrnxmr> No reorging back and forth, breaking wallets etc     

> __< br-m >__ <rucknium> If rolling DNS checkpoints are truly too risky, then it shouldn't be done. Qubic is causing disruptions to honest miners' revenue and some tx confirmation slowdowns for users, but not the major disruptions that could occur with 10+ block re-orgs.     

> __< DataHoarder >__ ^ that or automated deployment on detecting one. but that would cause two reorgs back and forth     

> __< br-m >__ <ofrnxmr> dh, right. I much prefer ignoring the reorg thsn going through it     

> __< br-m >__ <ofrnxmr> Its a bit messy to reorg back and forth     

> __< br-m >__ <blurt4949:matrix.org> if we get the entire non-Qubic network on board with DNS checkpoints then that's one thing. But breaking up the honest miners into these two camps makes us much easier to attack     

> __< br-m >__ <ofrnxmr> Messy in that, some reorgs (temporarily) break wallets     

> __< br-m >__ <ofrnxmr> When the reorg is ignored, it causes no downtime for the checkpointed chain     

> __< br-m >__ <rucknium> Getting major mining pools to enforce DNS checkpointing is its own Byzantine Generals problem, too.     

> __< DataHoarder >__ the enforcement of DNS checkpoints and activation of these are two different issues     

> __< br-m >__ <ofrnxmr> Of coursr, before we start deploying, we'd need to release binaries, then get pools to confirm they are running them     

> __< br-m >__ <rucknium> Because each pool would be wondering if all the ostensibly "committed" pools are actually committed.     

> __< DataHoarder >__ we can do all the work up to activation and still decide then to not go ahead with it     

> __< br-m >__ <ofrnxmr> With checkpointing enabled and working     

> __< tevador >__ Checkpoints should stay opt-in.     

> __< br-m >__ <ofrnxmr> Yeah, opt in     

> __< DataHoarder >__ I don't think that's changing at the moment, at least monero release wise     

> __< br-m >__ <ofrnxmr> But we shouldnt start aggressively updating dns until we confirm that >50%of the global hash is opted in     

> __< tevador >__ Can we put some flag in blocks? Like bitcoin's soft fork signaling.     

> __< DataHoarder >__ these could be in the tx extra data     

> __< br-m >__ <rucknium> The proposal isn't nearly at the necessary level of community engagement yet, IMHO. The details are still being worked through, of course. I can post it on monero.town for exposure.     

> __< tevador >__ Yes, tx_extra in the miner tx.     

> __< br-m >__ <rucknium> IIRC, there is some signaling capability in the node already. Maybe it's just peers(?)     

> __< DataHoarder >__ altering block templates might introduce more friction on pools updating their setup     

> __< DataHoarder >__ if all they need is update monerod + dns flags, that's simpler than changing backend     

> __< br-m >__ <blurt4949:matrix.org> There's a hard fork voting mechanism (that's never been used AFAIK) that could be co-opted too? Just without a hard fork attached to it.     

> __< br-m >__ <ofrnxmr> Even if they signal that they are enforcing checkpoints, we need to know that they are actually able to reach 2/3+1 of the dns endpoints     

> __< br-m >__ <rucknium> blurt4949:matrix.org: Right. That is what I was thinking of.     

> __< br-m >__ <blurt4949:matrix.org> Ah, my bad     

> __< DataHoarder >__ for readily parseable tx extra entries that are not used for other purposes it would be the mysterius minergate tag 0xde or adding a mask to the nonce     

> __< DataHoarder >__ (tx extra nonce)     

> __< br-m >__ <ofrnxmr> Just blindly assuming that the nodes are able to use the checkpoints is a bad idea. We should manually confirm that the pools are able to reach all of the dns endpoints     

> __< br-m >__ <rucknium> DataHoarder suggested that major pools should run their own DNS servers. That makes sense, for security reasons in general.     

> __< DataHoarder >__ DNS Resolvers*     

> __< DataHoarder >__ which then act as DNS recursive servers internally     

> __< DataHoarder >__ mysterius minergate tag is varint + data, no "max size"     

> __< DataHoarder >__ according to monero code plus my own parsing code :)     

> __< br-m >__ <rucknium> Maybe you could change the get_block_template RPC endpoint to automatically insert something in tx_extra that signals the enforcement, when it is turned on.     

> __< rbrunner >__ Clever, but might have unintended side effects     

> __< DataHoarder >__ if done, that field could explicitly have the most recent checkpoint they are aware of, plus % that agree     

> __< DataHoarder >__ rbrunner: unintended examples?     

> __< rbrunner >__ Can't come up with something, but wouldn't such a change make it impossible to get an unmodified template which might be needed for some purpose?     

> __< br-m >__ <blurt4949:matrix.org> Well for one Qubic could signal DNS enforcement to activate the mechanism at <50% true enforcement, unless we're talking about someone manually looking at the percentages and deciding when to acitvate     

> __< tevador >__ We have the minor version field, which is probably unused by consensus.     

> __< DataHoarder >__ the template data is already modified in tx extra due to having to include the pubkey     

> __< br-m >__ <rucknium> IIRC, P2Pool miners use ZMQ to get txs and assemble their own block templates. They would be unaffected by changes in get_block_template RPC, FWIW.     

> __< DataHoarder >__ plus nonce data there     

> __< rbrunner >__ And then we may have doctored daemons that start to lie ...     

> __< DataHoarder >__ indeed. for p2pool it'd be a breaking change or flagging via extra nonce     

> __< DataHoarder >__ note qubic could also add random data in these, ofc     

> __< DataHoarder >__ p2pool could alternatively signify this via other means in-p2pool itself     

> __< DataHoarder >__ this was done in the past to signal support for X feature     

> __< br-m >__ <kayabanerve:matrix.org> I still find it absurd DNS checkpoints can be discussed without the outrage seen when discussing a finality layer.     

> __< rbrunner >__ Maybe not the same page that rage?     

> __< rbrunner >__ *people     

> __< br-m >__ <rucknium> I don't think the tx_extra data would automatically trigger something in teh DNS servers. Manual activation, still. But it would show miners what other miners are doing (or saying that they are doing).     

> __< DataHoarder >__ they are understood as a bandaid to have while we rip out each other when discussing permanent finality layers :)     

> __< tevador >__ DNS checkpoints are not a finality layer. They can be deleted once the honest chain overtakes the attacker.     

> __< br-m >__ <kayabanerve:matrix.org> I don't have anything helpful to contribute at this time other than that, sorry ^ something something DNS checkpoints _are_ a Proof of Authority finality layer.     

> __< DataHoarder >__ they are, indeed     

> __< br-m >__ <kayabanerve:matrix.org> tevador: we can also soft fork a PoS finality layer.     

> __< DataHoarder >__ rucknium: I think suggesting a mask on miner tx extra nonce would be reasonable     

> __< DataHoarder >__ but some non-cooperating pools might delay signaling that way     

> __< guest55 >__ and then turn it off the soft fork PoS finality layer?     

> __< br-m >__ <rucknium> The main practical problem with PoS finality layer is long R&D timeline.     

> __< tevador >__ <kayabanerve: DNS checkpoints can be deployed tomorrow, PoW finality layer when? In 6 months?     

> __< br-m >__ <kayabanerve:matrix.org> We couldn't implement slashing, but we could do decentralized validator selection + checkpoint creation + nodes could only follow checkpoints + miners can attempt to make it the chain with the most work.     

> __< br-m >__ <kayabanerve:matrix.org> tevador: I'm not saying "don't discuss DNS checkpoints". I'm noting my frustration at the distinction.     

> __< br-m >__ <kayabanerve:matrix.org> rucknium:monero.social: So we should start the clock sooner than later, and also, we can use Ethereum as 'DNS' in order to immediately (within a few weeks) decentralize the checkpointing solution.     

> __< DataHoarder >__ Publishing checkpoints on an alternate medium other than DNS does sound good     

> __< tevador >__ If implemented, a (softforking) PoS checkpointing layer would be preferable to DNS checkpoints.     

> __< DataHoarder >__ can rollover DNS onto softfork checkpoint layer onto other long term solutions     

> __< tevador >__ DNS checkpoints is the only thing that can be rolled out quickly (in days).     

> __< DataHoarder >__ Also, regarding checkpoints, I do support showing checkpoints onto the qubic snooper that I built anew https://qubic-snooper.p2pool.observer/tree/     

> __< DataHoarder >__ either real or test ones     

> __< DataHoarder >__ can help show what they'd do live on mainnet without actually activating such a system     

> __< br-m >__ <blurt4949:matrix.org> ...there's also rolling checkpoints, but I understand those are somewhat unpopular here     

> __< br-m >__ <blurt4949:matrix.org> (non-DNS rolling checkpoints)*     

> __< DataHoarder >__ what would that entail?     

> __< tevador >__ kayabanerve: FWIW, I support merging your CCS.     

> __< plowsof >__ ofrnxmr ">50%of the global hash is opted in" im sure 2 pools will agree to avoid losing several mined blocks lol     

> __< br-m >__ <kayabanerve:matrix.org> We can have a solution where blocks are posted to Ethereum, and nodes follow the first valid blockchain posted to Ethereum, in a few weeks so long as they can connect to an Ethereum node. The primary issue would be:     

> __< br-m >__ <kayabanerve:matrix.org> 1) Extending the Monero network to carry Ethereum SPV proofs     

> __< br-m >__ <kayabanerve:matrix.org> 2) The fees miners would have to pay     

> __< br-m >__ <kayabanerve:matrix.org> tevador: Thank you.     

> __< br-m >__ <kayabanerve:matrix.org> Again, I wasn't here to speak out against DNS. Solely to raise the other ideas because I consider them better and unfairly degraded in comparison.     

> __< guest55 >__ can the PoS finality things be temporary?     

> __< br-m >__ <rucknium> It could potentially be a lot of fees. 0.6XMR revenue per block minus how much in ETH fees?     

> __< DataHoarder >__ Everything else is better to DNS checkpoints but we can't have a successful discussion with fire on our backs     

> __< br-m >__ <chaser> ETH is very cheap these days.     

> __< DataHoarder >__ alternatively, we could use CT Logs :)     

> __< br-m >__ <chaser> I mean tx fee-wise.     

> __< DataHoarder >__ it's not crypto but it would also show proof of inclusion     

> __< guest55 >__ i assume because your saying soft fork PoS finality that it can be turned off     

> __< tevador >__ Our own PoS checkpointing is much better than Ethereum, which is also PoW on another blockchain...     

> __< br-m >__ <blurt4949:matrix.org> kayabanerve:matrix.org: what happens in the scenario where an attacker mines a block privately, posts it to ETH, then withholds it for weeks before publishing to Monero? Genuine question, but maybe (probably) i'm just stupid     

> __< tevador >__ PoS*     

> __< tevador >__ blurt4949: I think the idea was to post the entire 300KB block on Ethereum.     

> __< DataHoarder >__ if the ETH part is to be done, it'd need to include full transactions     

> __< br-m >__ <kayabanerve:matrix.org> It appears 256 KB of data on Ethereum is currently 0.25 USD.     

> __< br-m >__ <blurt4949:matrix.org> tevador: Oh.     

> __< br-m >__ <rucknium> AFAIK, any softforking proposal is vulnerable to the issue I discussed in "Paths to majority hashpower" in https://github.com/monero-project/monero/issues/10064 and that blurt4949:matrix.org  is persistent about.     

> __< br-m >__ <kayabanerve:matrix.org> blurt4949:matrix.org: Monero nodes get it from ETH?     

> __< br-m >__ <kayabanerve:matrix.org> I said post blocks, not block hashes, and meant it.     

> __< br-m >__ <blurt4949:matrix.org> Right, I was thinking header-only or something like that. My apologies     

> __< br-m >__ <blurt4949:matrix.org> rucknium:monero.social: It's in my name     

> __< br-m >__ <rucknium> Which is, temporarily or permanently losing majority hashpower. Nodes that aren't updated will follow the majority-hashpower chain fork.     

> __< br-m >__ <kayabanerve:matrix.org> So Ethereum's fees may go ballistic, but potentially just a dollar a block.     

> __< tevador >__ I wouldn't prefer going the ETH route.     

> __< br-m >__ <articmine> There are serious problems with POS that need to be discussed     

> __< br-m >__ <articmine>       

> __< br-m >__ <articmine> Starting with cost of capital attacks, and exchange centralization.      

> __< br-m >__ <articmine> And of course finality layers walk straight into the well known not at stake problem.     

> __< rbrunner >__ Never imagined that connecting to Ethereum for a finality layer would meaning posting *full blocks* there. Color me surprised.     

> __< br-m >__ <kayabanerve:matrix.org> I would prefer a native solution. I would prefer Ethereum to DNS (Proof of Authority).     

> __< DataHoarder >__ rbrunner: any other opens the world to qubic also posting theirs there first     

> __< br-m >__ <articmine> This whole POS proposal is a major change to the Monero social covenant      

> __< DataHoarder >__ and just holding the full blocks before trying to reorg     

> __< br-m >__ <kayabanerve:matrix.org> I don't consider DNS a preferable native solution.     

> __< br-m >__ <chaser> > There are serious problems with POS that need to be discussed     

> __< br-m >__ <chaser> > can the finality layer CCS then be merged please?     

> __< guest55 >__ i don't think anyone does     

> __< tevador >__ arcticmine: using PoS as a soft checkpointing layer would be completely OK     

> __< br-m >__ <articmine> Let's call a spade a spade     

> __< rbrunner >__ DataHoarder: Yes, my surprise is probably rooted in my limited understanding of these things     

> __< br-m >__ <kayabanerve:matrix.org> Is it? Before, 51% of hash power decides who can participate. Now, validators do.     

> __< br-m >__ <rucknium> The advantage of DNS is that it is easier to manually adjust it or turn it off, in response to events.     

> __< br-m >__ <articmine> The reality is setting up a parallel POS network that makes the POW essentially redundant      

> __< guest55 >__ and the DNS thing was put their to address bugs / vulnerabilities, and it turns out selfish mining is a vuln     

> __< DataHoarder >__ as more or less tested the checkpoints set these at depths from tip, so the top area is still able to reorg as usual.     

> __< DataHoarder >__ it limits how deep later reorgs can go, but the rest above is left to normal mining behavior, including selfish     

> __< tevador >__ Checkpointing would be used to prevent 10+ deep reorgs, which cause invalid transactions to get stuck for a week in the mempool.     

> __< br-m >__ <articmine> I am actually studying the POS in Ethereum. It will make many members of the Monero community cringe     

> __< DataHoarder >__ or allow mostly anyone to do double spends when someone does a 20+ reorg     

> __< br-m >__ <kayabanerve:matrix.org> articmine:monero.social: Proof of work still nominates the builder of the next block.     

> __< rbrunner >__ Well, we could move away from that long 1 week, but of course the invalid transactions problem stays     

> __< DataHoarder >__ on guest55 topic, are we able to write this change on moneropulse page / blog? I guess we still need more time before we change the documentation to reflect plans     

> __< br-m >__ <articmine> Until POS says it is redundant      

> __< br-m >__ <articmine> It took ETH like 7 years and they have not addressed many of y problems      

> __< br-m >__ <chaser> articmine:monero.social: a finality layer can't just create valid blocks out of thin air     

> __< br-m >__ <rucknium> Wallets using nodes that do not enforce DNS checkpoints could create txs that depend on outputs in the Qubic 10+ attacking chain, which would make those tx invalid when the checkpointed chain overtakes the attacking chain. Need to keep that in mind.     

> __< br-m >__ <articmine> Zcash their proposal is like 3 years ago     

> __< rbrunner >__ Well, if ever PoS would come later, but seems to me we have lose consensus that we should prepare a *short term* solution, even if only band-aid level     

> __< br-m >__ <rucknium> Without careful design, a finality layer could slow-walk the blockchain down to very low PoW difficulty, then co-opt it with low hashpower rigs, AFAIK. Isn't that true?     

> __< DataHoarder >__ Another question that came yesterday, in the case of a deep reorg and invalidated txs/decoys happen     

> __< br-m >__ <articmine> Yes but the "short term solution" should not be a back door to POS     

> __< br-m >__ <kayabanerve:matrix.org> For whatever reasons, DNS hasn't been rejected by the community yet.     

> __< DataHoarder >__ how would the new remade tx select the decoys?     

> __< br-m >__ <kayabanerve:matrix.org> It can also he implemented in days.     

> __< tevador >__ We should work on decentralizing the moneropulse domain control and open a PR for the minor changes (2/3+1, ban time, etc.). That can probably be done by next week.     

> __< DataHoarder >__ Would it be able to use the ringdb to select similar ones or is this information lost, disclosing the true spend?     

> __< br-m >__ <kayabanerve:matrix.org> rucknium:monero.social: Fundamentally, not without careful design.     

> __< DataHoarder >__ regardless of using DNS checkpoints for deep reorgs or not, indeed tevador decentralizing that part and increasing consensus on that is a good idea regardless     

> __< guest55 >__ and just for fun, does running a DNS checkpointing thingy put the monero project in any weird legal situation     

> __< tevador >__ It's still up to the node operator to decide if they will follow the checkpoints.     

> __< spaceman >__ did my legal situation message go through? sorry weird connection     

> __< br-m >__ <drinksomemilk:matrix.org> Regardless of the checkpointing solution implementet a permanent chainsplit with nodes on the "honest" less heavy chain only beeing kept on the chain due to the checkpointing mechanism would not be ideal     

> __< DataHoarder >__ it did.     

> __< br-m >__ <deltaplex:matrix.org> kayabanerve:matrix.orgMost people in crypto probably have heard about PoS but not so much about DNS and I haven’t seen an     

> __< br-m >__ <rucknium> tevador: tevador: That sounds good to me. DataHoarder  can help with delegating/decentralizing domain control AFAIK.     

> __< br-m >__ <kayabanerve:matrix.org> Rebranding to "Proof of Monero" :(     

> __< br-m >__ <ofrnxmr> spaceman: Yes     

> __< DataHoarder >__ I can suggest setups to follow to ensure root domain and checkpointing sub domain are safe or review configurations     

> __< spaceman >__ do we have criteria for when this would be activated?     

> __< spaceman >__ like, which conditions?     

> __< DataHoarder >__ spaceman: there's still a split on having it always on from the start or "grim trigger"     

> __< DataHoarder >__ once enabled, it's enabled more or less, as nodes remember them     

> __< br-m >__ <kayabanerve:matrix.org> I don't see a message on "legal" by spaceman:     

> __< spaceman >__ and just for fun, does running a DNS checkpointing thingy put the monero project in any weird legal situation     

> __< DataHoarder >__ but that decision can be delayed while the rest of the system is cleaned up regardless of later decision      

> __< DataHoarder >__ it was guest55 who sent it     

> __< DataHoarder >__ as for DNS servers, Can use what I have deployed or alternatively use anything you prefer. Diversity here (with alright TTL) should be embraced as well     

> __< DataHoarder >__ 21:08:15 <guest55> and just for fun, does running a DNS checkpointing thingy put the monero project in any weird legal situation     

> __< br-m >__ <vtnerd> tevador are you mostly on board with dns checkpointing? it seems like you are?     

> __< br-m >__ <articmine> kayabanerve:matrix.org: ... but no proof of beneficial ownership of said Monero     

> __< spaceman >__ i mean the real solution is to double network hashrate     

> __< tevador >__ I think it's the best short term solution. The alternative is not doing anything.     

> __< tevador >__ It's still opt-in and can be shut down once qubic goes away.     

> __< DataHoarder >__ on the topic of diversification - other people also brought it up https://github.com/monero-project/monero/issues/10064#issuecomment-3276165999     

> __< br-m >__ <vtnerd> ok, wondering because I’m on the fence. worried it could be chaotic if it triggers     

> __< DataHoarder >__ even if the final decision is to not deploy, working to having a realistic solution that could plausibly be used is on its own already doing most of the work     

> __< tevador >__ We could deploy and wait to activate it if qubic starts with 10+ deep reorgs. That's the "grim trigger" strategy.     

> __< spaceman >__ id hazard a bet that qubic will stress test whatever we implement on mainnet     

> __< DataHoarder >__ grim trigger could also trigger on lower reorgs, 9, 8, 5 etc.      

> __< br-m >__ <kayabanerve:matrix.org> articmine:monero.social: We can link the validator signing key directly to the private spend key which would be approximate?     

> __< DataHoarder >__ yeah, for the test harness I'm writing on my own I have a "fuzzer" to generate several chains of reorg attempts across a sample of split nodes. but it's still too early to share     

> __< br-m >__ <articmine> spaceman: The Qubic attack is protocol agnostic. It is nothing more than basic bribery. One can attack a centralized ledger bank with bribery.     

> __< DataHoarder >__ I don't know if it was seen or there is no answer yet, but for:     

> __< DataHoarder >__ 21:06:46 <DataHoarder> Another question that came yesterday, in the case of a deep reorg and invalidated txs/decoys happen     

> __< DataHoarder >__ 21:06:56 <DataHoarder> how would the new remade tx select the decoys?     

> __< DataHoarder >__ 21:07:16 <DataHoarder> Would it be able to use the ringdb to select similar ones or is this information lost, disclosing the true spend?     

> __< DataHoarder >__ I remember ofrn mentioned the ring db also had issues on deep reorgs     

> __< br-m >__ <rucknium> DataHoarder: shared ring DB will probably screw things up.     

> __< br-m >__ <articmine> kayabanerve:matrix.org: Of the staked XMR, but not the beneficial owners of the Monero     

> __< DataHoarder >__ so in such cases it also ends up as a privacy issue if a deep reorg happens, and avoiding such privacy issues is core to XMR as well     

> __< br-m >__ <rucknium> i think it will just fail to construct a valid tx without deleting shared ring DB. Happened to me on testnet     

> __< tevador >__ I thought we already had mitigations in place for this in case of hard forks like Monero Classic etc.     

> __< br-m >__ <rucknium> I don't know if all or many "third-party" Monero wallets use shared ring DB.     

> __< DataHoarder >__ so the tx gets stuck for a week -> but you may not be able to create a new tx without creating wallet anew or manually deleting ringdb?     

> __< br-m >__ <rucknium> The smart thing would be to use the ring members that are still valid. The older ones. And re-select the younger ones.     

> __< br-m >__ <rucknium> Right?     

> __< DataHoarder >__ Could that disclose information about how old the spend is?     

> __< tevador >__ Yes, that's the best you can do AFAICS. This leaks the fact that the spent input was not in the reorged subchain.     

> __< DataHoarder >__ I guess the old + true spend would be static     

> __< br-m >__ <rucknium> If the real spend is in the re-orged part of the chain, it's hopelessly invalid on the other chain, AFAIK.     

> __< DataHoarder >__ yeah, 20+ for a real double-spend (including confirmation times) but 10+ for breakage     

> __< DataHoarder >__ it's a bit more complex on the "long reorg" case as the real spend can have a different output index, but I believe that'd still have the same key image ofc     

> __< br-m >__ <rucknium> I plan to run some empirical analysis on how likely invalid txs could be in realistic scenarios, e.g. if Qubic were to re-org 12 blocks or something. And what could happen to wallets constructing txs on nodes that don't enforce checkpoints, if there is a temporary chain split.     

> __< DataHoarder >__ if tx1 gets "orphaned" but not invalidated, it gets mined later on, tx2 built on output of tx1, but this gets invalidated     

> __< DataHoarder >__ tx2 is remade as tx3, but needs to pick the new global output index of tx1     

> __< br-m >__ <rucknium> DataHoarder: Your 20+ number is assuming that the potntial victim accepts txs as fully confirmed when a tx has 10 confirmations, right?     

> __< DataHoarder >__ yeah, 20+ is for "double spend" abusing that (disregarding mempool)     

> __< br-m >__ <rucknium> If a victim accepts txs with 3 confirmations, for example, that would be 13+....?     

> __< DataHoarder >__ yes     

> __< br-m >__ <rucknium> I think the plan to further develop DNS checkpoints is clear. Maybe never actually deploy it, depending on more debate and community feedback. But have it ready if necessarily.     

> __< br-m >__ <rucknium> Should other medium-term countermeasures like Publish or Perish be discussed now or should those be discussed asynchronously?     

> __< DataHoarder >__ These could be deployed along a short term system right?     

> __< br-m >__ <rucknium> The selfish mining countermeasure papers, using Markov Decision Process (MDP), don't show the data on how common each depth of re-org is. I think I will try to pull that data by running their models.     

> __< br-m >__ <rucknium> DataHoarder: Some of them, yes.     

> __< DataHoarder >__ could be part of any checkpointing selection system first, then soft forks?     

> __< br-m >__ <rucknium> AFAIK, any of the countermeasures that change miner rewards directly like Proportional Reward Splitting would require a hard fork.     

> __< br-m >__ <kayabanerve:matrix.org> Should we also further develop finality layer research? 🤔     

> __< DataHoarder >__ Those will indeed, so it's a subset. I think making an overview table (some was done already weeks ago) with eligibility of each as either part of checkpoint selection, soft fork (non-breaking), soft fork (requiring majority), hard fork     

> __< DataHoarder >__ you have my support but not my mind kayabanerve:matrix.org :)     

> __< br-m >__ <rucknium> kayabanerve:matrix.org: IMHO, you may direct your questions to specific people, because most people support your CCS AFAIK.     

> __< DataHoarder >__ my focus is on bandaids to give all of that time :)     

> __< br-m >__ <venture> Hi all. sorry for jumping in late.      

> __< br-m >__ <venture> just to give a quick update on the PoP simulation I have been working on: Making progress, but it's quite complex... and the project grew...     

> __< br-m >__ <venture> I'm currently working on Monte-carlo-tree search (basically sarsa(lambda=1)) for the selfish mine strategy given PoP      

> __< br-m >__ <rucknium> venture:monero.social: Do you need more RAM and/or CPU? Or is it not bottlenecked by that?     

> __< br-m >__ <venture> it's all one-threaded.. since the ticks are generated by the distribution.. i think if threading would be involved, it would skew things up.. so yeah, it gets slow with number of steps per training episode, but i think it's fine right now...      

> __< br-m >__ <venture> currently converging on roughly 8-10 % gain, on 40% attacker-share     

> __< br-m >__ <kayabanerve:matrix.org> rucknium:monero.social: completely fair :p I was just riffing off how you said the plan to develop DNS checkpoints is clear. It was meant as a joke.     

> __< br-m >__ <articmine> kayabanerve:matrix.org: A finality layer is fundamentally dependent on POS and I just don't see the consensus in the Monero community for POS.     

> __< br-m >__ <articmine> If people want to fund this research they of course can fund it. I just believe that it is  fair to say that the consensus is not there     

> __< br-m >__ <kayabanerve:matrix.org> Or Proof of Authority, as seen with DNS checkpoints     

> __< br-m >__ <kayabanerve:matrix.org> Or historically mined blocks     

> __< br-m >__ <rucknium> We can end the meeting here. Thanks everyone.     

> __< br-m >__ <ofrnxmr> https://github.com/monero-project/monero/pull/10075     

> __< DataHoarder >__ on 10075, is the ownership of these domains distributed?     

> __< DataHoarder >__ and/or across a few providers     

> __< br-m >__ <ofrnxmr> Its in draft - idk what we want to do about the domains     

> __< br-m >__ <rucknium> Isn't the registrar of all the domains Gandi?     

> __< br-m >__ <syntheticbird> oh no     

> __< br-m >__ <syntheticbird> not Gandi...     

> __< DataHoarder >__ registrar != DNS provider as well     

> __< br-m >__ <basses:matrix.org> The DNS provider is cloudflare, right?     

> __< br-m >__ <basses:matrix.org> https://discuss.privacyguides.net/t/suspicious-services-used-by-le-to-intercept-data-cloudfare-gandi-ovh-hetzner-etc/18889     

> __< br-m >__ <basses:matrix.org> https://mrelay.p2pool.observer/m/matrix.org/zwUjnxCPFvSeaWHbnfyoezQB.png (clipboard.png)     

> __< br-m >__ <syntheticbird> Gandi is one of the most glowie (pardon my language) dns provider out there     

> __< br-m >__ <syntheticbird> I'm surprised they haven't kicked out monero domains registration years ago     

> __< DataHoarder >__ a couple could be distributed across, but yeah several others specially some that allow direct XMR payment would be usefull (or specifically anon mode)     

> __< DataHoarder >__ njalla / 1984hosting plus others     

> __< DataHoarder >__ that's the registrar, then authoritative DNS servers for it could be had on other platforms or directly hosted     

> __< br-m >__ <syntheticbird> i do not recommend njalla     

> __< br-m >__ <ofrnxmr> the main thing is probably to ensure that people updating dns checkpoints, are doing so regularly and reliably     

> __< br-m >__ <syntheticbird> they have a great history of stealing domains that become famous, it is marked in their terms of services that the domains you buy is detained and owned by them     

> __< br-m >__ <ofrnxmr> Some seed nodes are notoriously offline, for example     

> __< br-m >__ <syntheticbird> and they are free to keep it for sale if they decide so     

> __< DataHoarder >__ yeah those can be in subdomains, which has lesser risk     

> __< DataHoarder >__ yeah, that's also part how they can legally comply with the privacy with current laws syntheticbird     

> __< br-m >__ <syntheticbird> ack     

> __< br-m >__ <monerobull:matrix.org> it would instantly become a hard layer > <tevador> arcticmine: using PoS as a soft checkpointing layer would be completely OK     

> __< br-m >__ <monerobull:matrix.org> of course im going to trust the PoS layer checkpoints, why wouldnt i? do i have any alternatives?      

> __< br-m >__ <monerobull:matrix.org> DNS checkpoints? yeah no thank you im going to rely on the decentralized consensus mechanism where people have to put their money where their mouth is     

> __< plowsof >__ seed nodes arent that bad, just 51.79.173.165 / lalanza is the terminally offline one  https://github.com/plowsof/check-monero-seed-nodes     

> __< br-m >__ <ofrnxmr> hey, i wasnt naming names :D     

> __< br-m >__ <ofrnxmr> plowsof is also like 30% of the seed nodes haha     

> __< plowsof >__ 100% of the tor seeds at your service     

> __< br-m >__ <ofrnxmr> so whats the plan on updating records?     

> __< br-m >__ <ofrnxmr> i think we should update proactively (as opposed to reactively), maybe rolling blocks 4-10? Updating at every new block     

> __< br-m >__ <ofrnxmr> whoops, this is lab, my bad. thought we were in lounge     

> __< br-m >__ <deltaplex:matrix.org> So the PoS finality layer won’t have slashing and bleeding?     

> __< br-m >__ <deltaplex:matrix.org> I would just prefer PoP & full node mining if that’s the case     

> __< DataHoarder >__ that hasn't been discussed yet fully     

> __< br-m >__ <basses:matrix.org> for political reasons! > <syntheticbird> i do not recommend njalla     

> __< br-m >__ <basses:matrix.org> if not technical then I don't want answer because could be off topic     

> __< br-m >__ <basses:matrix.org> who is the person managing all this stuff? > <ofrnxmr> the main thing is probably to ensure that people updating dns checkpoints, are doing so regularly and reliably     

> __< br-m >__ <basses:matrix.org> basses:matrix.org: oh, scrolling I see     


```

# Action History
- Created by: Rucknium | 2025-09-09T23:45:07+00:00
- Closed at: 2025-09-19T21:07:07+00:00
