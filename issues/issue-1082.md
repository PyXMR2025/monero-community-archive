---
title: Monero Research Lab Meeting - Wed 25 September 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1082
author: Rucknium
assignees: []
labels: []
created_at: '2024-09-25T16:24:45+00:00'
updated_at: '2024-10-09T14:59:24+00:00'
type: issue
status: closed
closed_at: '2024-10-09T14:59:24+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). Reviews for [Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md).

5. 10 block lock discussion: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259 , [Monero output lock analysis](https://github.com/AaronFeickert/pup-monero-lock/releases/tag/final)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1078 

# Discussion History
## Rucknium | 2024-09-26T14:49:45+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1082     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< o​ne-horse-wagon:monero.social >__ Hello.     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ Hi     

> __< a​rticmine:monero.social >__ Hi     

> __< j​effro256:monero.social >__ howdy     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< r​ucknium:monero.social >__ me: Wrote "Required possession duration of malicious hashpower for successful double-spend attack with a _z_ stopping rule." https://gist.github.com/Rucknium/37d772f7232aef3989bfd5b9c6d99596     

> __< j​effro256:monero.social >__ me: Carrot balance recovery handling and getting updated quotes from auditors which include security proofs for Janus attacks     

> __< v​tnerd:monero.social >__ Me: converted lws rest server to boost::beast and going to finish up some monerod stuff today hopefully     

> __< k​ayabanerve:matrix.org >__ I made my library for calculating divisors constant time to avoid any concerns there. I'm now working on redoing the data flow for FCMP++ prove/verify from the current shims to what we actually need in a production context.     

> __< 0​xfffc:monero.social >__ 1, Fixed the pop blocks, submitted the PR. 2. Fixed rpc limit ( not pushed yet ). 3. Breaking dynamic bss code to different PRs ( smaller PR and will submit it tomorrow ). Spent a little bit of time on a new problem about public nodes.     

> __< r​ucknium:monero.social >__ 3) Stress testing monerod https://github.com/monero-project/monero/issues/9348     

> __< r​ucknium:monero.social >__ There's a problem with the txpool limiter that appears rarely. Sometimes the node sets a low txpool limit arbitrarily, like 10-50MB. The trigger for the bug is unknown.     

> __< r​ucknium:monero.social >__ This could be a problem for mining nodes. It also slows down block verification since the nodes have to ask for the txs they are missing when they get a fluffy block     

> __< j​berman:monero.social >__ me: working on wallets sync the tree locally for fcmp++ (to avoid needing to reveal any statistical trace to daemons which outputs are the users when spending)     

> __< j​effro256:monero.social >__ So the pool just shrinks dramatically, dropping txs without the txs showing up in the chain?     

> __< r​ucknium:monero.social >__ I don't know if it keeps the old ones and throws the new ones out, or throws out old ones to fit the new ones     

> __< j​effro256:monero.social >__ How long does it stay at this reduced size?     

> __< r​ucknium:monero.social >__ The node that's actively having this problem now has the "Sync data returned a new top block candidate..." message for almost every block     

> __< r​ucknium:monero.social >__ AFAIK, until node restart     

> __< r​ucknium:monero.social >__ It has happened at least to my node and spackle's node on stressnet. Maybe other people's nodes, but they may not have noticed.     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs. Reviews for Carrot. https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< j​effro256:monero.social >__ I've been receiving updated quotes for including Janus resistance in scope of properties for which we want security proofs. I plan to invite them to the next MRL for a quick schpeal if that's okay with everyone     

> __< j​berman:monero.social >__ good with me     

> __< r​ucknium:monero.social >__ Sounds good :)     

> __< k​ayabanerve:matrix.org >__ I'm still trying to work things out with veridise. Should be done next week. I also saw Rucknium's request and have to do the book keeping     

> __< r​ucknium:monero.social >__ Thanks, kayabanerve     

> __< j​effro256:monero.social >__ By "work things out", are you referring to allocating more budget to Veridise with their current audit?     

> __< k​ayabanerve:matrix.org >__ No, confirm scope and quote.     

> __< j​effro256:monero.social >__ Oh, for which audit?     

> __< k​ayabanerve:matrix.org >__ The remaining work on divisors prior discussed.     

> __< r​ucknium:monero.social >__ Anything more on FCMP++?     

> __< j​effro256:monero.social >__ Nothing here     

> __< k​ayabanerve:matrix.org >__ I have one topic     

> __< k​ayabanerve:matrix.org >__ Helioselene (my lib for Helios/Selene) is multiple times slower than other EC libs. My CCS explicitly states my impl is not expected to be prod grade. The fact it happens to be usable in prod is more commentary on how well I did my work on the proofs.     

> __< k​ayabanerve:matrix.org >__ I have an EC divisor library which is functional. It's also the most computationally expensive part of the proving. Thankfully, it can be done asynchronously. Before a user signs a TX, or even does a membership proof, the wallet can create divisors to be used.     

> __< k​ayabanerve:matrix.org >__ So wallet UX should be able to make the time to calculate divisors a complete non-issue in practice EVEN IF we don't have wallet trees and do use RPC calls to fetch path information (as the divisors can have their calculation started before committing to making a TX and starting to send RPC requests).     

> __< k​ayabanerve:matrix.org >__ I have some degree of interest in organizing a contest for anyone to develop more efficient implementations. I think they're clearly defined, concise parts of the codebase, amenable to such incentivization.     

> __< k​ayabanerve:matrix.org >__ That's actually all I have to say on this for now, I just wanted to have the idea noted.     

> __< j​berman:monero.social >__ I figure tevador would also be a good candidate here, perhaps we can put up the bat signal for tevador / see if they're interested? and if not, then go with bounties?     

> __< k​ayabanerve:matrix.org >__ I'll also clarify the divisors should be a fraction of a second on a modern laptop. We need more than ten of them for a FCMP so it can become seconds depending on the device hardware. I'm not concerned about it because threads exist (I've only used single threads) AND again, they can be calculated at any time. Even when you open a wallet, it can start 10 sets in the background for<clipped message     

> __< k​ayabanerve:matrix.org >__  the hell of it. If a user does start to make a TX, the time for them to enter the address/amount/review/hit confirm should be longer than the calculation time.     

> __< r​ucknium:monero.social >__ Does that scale linearly with the number of inputs?     

> __< k​ayabanerve:matrix.org >__ tevador prior agreed to do an optimized version of Helios/Selene. tevador hasn't been seen in a while AND tevador being able to do an optimized version doesn't mean they'd do the best implementation.     

> __< r​ucknium:monero.social >__ And does not depend on the merkle tree "anchor"?     

> __< j​berman:monero.social >__ to be clear, there's also all the other Helioselene ec arithmetic that affects tree building that has room for optimization, right? not just divisors     

> __< j​effro256:monero.social >__ If the total time is less than a few seconds , that cost will likely be dwarfed by scanning times anyways and there might not be a very compelling reason to put a ton of effort into optimizing it IMO     

> __< k​ayabanerve:matrix.org >__ It's necessary per input, it's not bound to the input nor the tree. The amount of divisors necessary for an input is variable to the tree depth.     

> __< k​ayabanerve:matrix.org >__ Yeah, ideally, a new Helioselene lib gets 3x across the board jberman     

> __< j​effro256:monero.social >__ Can divisior generation can be done without access to spend or view opening of tx outputs?     

> __< k​ayabanerve:matrix.org >__ Jeffro256: I'm concerned on phones it'll become tens of seconds, but including the divisors lib may be reasonably not worthwhile for such a contest (limiting this discussion to Helioselene)     

> __< k​ayabanerve:matrix.org >__ jeffro256: It doesn't need any keys but would leak sender privacy     

> __< j​berman:monero.social >__ a contest sgtm. with community buy-in, since it looks like some of the research funds will be leftover, could perhaps allocate some of what looks like leftovers toward seed funding a contest     

> __< k​ayabanerve:matrix.org >__ If tevador comes back within the next month or so and delivers a 3x faster Helioselene, we can say this isn't sufficiently worthwhile. I think this contest format can attract fresh talent and is our best chance at the highest performant library possible.     

> __< k​ayabanerve:matrix.org >__ I would want to do it on a new CCS.     

> __< k​ayabanerve:matrix.org >__ The research funds can't be used for this (I don't hate the idea but they're earmarked otherwise). Upon research completion, the leftover funds turnover to MRL and would be eligible, yet that only occurs at the end of the road. I'd ideally propose this contest around EOY (not end of the road for the research tasks).     

> __< k​ayabanerve:matrix.org >__ It's an idea. I'm months away from being able to actually put it forth. I'd need to spend weeks organizing it due to the development time of an evaluation framework.     

> __< r​ucknium:monero.social >__ 5) 10 block lock discussion https://github.com/monero-project/research-lab/issues/102 https://github.com/AaronFeickert/pup-monero-lock/releases/tag/final     

> __< r​ucknium:monero.social >__ I wrote "Required possession duration of malicious hashpower for successful double-spend attack with a _z_ stopping rule."     

> __< r​ucknium:monero.social >__ Direct link to table: https://gist.github.com/Rucknium/37d772f7232aef3989bfd5b9c6d99596#table-duration-of-meta-attack-to-achieve-attack-success-probability-of-50-percent     

> __< r​ucknium:monero.social >__ IMHO, the relevance of this table depends on the threat model. If the cost to the attacker to acquire more hashpower is a roughly linear function of the desired malicous hashpower, then it is best to go big or go home: Get a majority of hashpower.     

> __< j​berman:monero.social >__ maybe a comment on here may be a good place to try to contact tevador https://gist.github.com/tevador/d3656a217c0177c160b9b6219d9ebb96     

> __< r​ucknium:monero.social >__ So, if the equation is `total_budget = duration * hashpower_share`, then it is best to put the money into hashpower share instead of duration. But if the threat actor is a hacker who acquires control of a large mining pool, then it's more relevant, since the hacker isn't spending a linear amount of money to acquire hashpower.     

> __< k​ayabanerve:matrix.org >__ For 15m USD of opportunity cost (assuming zero TX fees), 10% of the hash power can likely perform a 8 block reorg from my reading of that table.     

> __< r​ucknium:monero.social >__ 15m USD can do a 720-block re-org if they possess hashpower for 24 hours.     

> __< r​ucknium:monero.social >__ A much smarter move by an adversary.     

> __< r​ucknium:monero.social >__ The risk of collateral damage from a deep re-org also depends on the chosen full confirmation time of potential suitable victims. The best suitable victim type IMHO is an exchange. Kraken requires 15 blocks: https://support.kraken.com/hc/en-us/articles/203325283-Cryptocurrency-deposit-processing-times     

> __< r​ucknium:monero.social >__ Most of Trocador's instant swap partners require 10-15 blocks.     

> __< k​ayabanerve:matrix.org >__ Rucknium: Can you please clarify?     

> __< k​ayabanerve:matrix.org >__ 15m USD isn't the cost to acquire 51% of hash power for 24 hours, is it? Is the suggestion by bribing the top pools as that'd be profitable for them?     

> __< k​ayabanerve:matrix.org >__ (15m exceeds a day's block rewards by farrrr)     

> __< r​ucknium:monero.social >__ The durations in that table are probably an upper bound because the simple _z_ stopping rule isn't optimal. A smart adversary would halt an attack and re-start from scratch sometimes before the _z_th block is reached, and even sometimes after. A paper (Hinz (2020). "Resilience Analysis for Double Spending via Sequential Decision Optimization.") could be useful for analyzing optima<clipped message     

> __< r​ucknium:monero.social >__ l stopping rules, but their solution algorithm requires a parameter for the value of the double-spent tx.     

> __< r​ucknium:monero.social >__ I get `720 * 0.6 * 170 = 73440` Am I wrong?     

> __< r​ucknium:monero.social >__ Oh, you were saying that it exceeds the block rewards     

> __< k​ayabanerve:matrix.org >__ No, but if this is your premise, we have two different discussions     

> __< r​ucknium:monero.social >__ Yes, that's my point. Much better and cheaper to acquire hashpower for a shorter period of times     

> __< k​ayabanerve:matrix.org >__ I'm unsure in practice that top mining pools would accept such bribes.     

> __< k​ayabanerve:matrix.org >__ If they wouldn't, one would have to acquire new hash power. New hash power is much more expensive to require.     

> __< k​ayabanerve:matrix.org >__ Eh. There's enough social engineering/illegal methods the multiple is probably small enough we can drop it from being an issue/consideration.     

> __< r​ucknium:monero.social >__ Drop what?     

> __< k​ayabanerve:matrix.org >__ Drop my concern about the difference in price of existing and new hash power.     

> __< j​effro256:monero.social >__ But potentially the resale value it still very good if only used for a 24 hour attack     

> __< rbrunner >__ You mean use a warehouse full of PCs ready to go to shops for 24 hours :)     

> __< k​ayabanerve:matrix.org >__ '1000 Threadrippers, lightly used, BTC only'     

> __< r​ucknium:monero.social >__ nanopool has more than 30% of hashpower usually. If a hacker got control of their hashpower for 1/3rd of a day, the hacker could achieve a 10-block re-org with 50% probability.     

> __< o​ne-horse-wagon:monero.social >__ Does anyone know the percentage of Monero users that need to reduce the 10 block lock mechanism because it is cramping what they are trying to do?     

> __< k​ayabanerve:matrix.org >__ We have evidence at scale, RISC-V boards are most efficient *from a production/new hardware acquisition standpoint*.     

> __< rbrunner >__ Well, we could come to the conclusion that this Nanopool hacked scenario is too dangerous and go *higher*, e.g. to 15 blocks ...     

> __< k​ayabanerve:matrix.org >__ We'll always fundamentally have a 1 block lock fwiw     

> __< k​ayabanerve:matrix.org >__ I'm unsure user experience is notably different for 8 vs 10 (as an example)     

> __< rbrunner >__ Yeah, and data sure does not seem to point towards 5 blocks or so, right?     

> __< r​ucknium:monero.social >__ By the way, the table is an upper bound of the required possession duration. The _z_ stopping rule isn't optimal, because a smart attacker would end an attack and re-start at less than _z_ blocks sometimes, and continue past _z_ sometimes, too, depending on how far behind they are in the race against the honest chain. A paper (Hinz (2020). "Resilience Analysis for Double Spending <clipped message     

> __< r​ucknium:monero.social >__ via Sequential Decision Optimization.")  has an algorithm that could help compute a better bound, but it depends on a parameter for the value of the double-spent tx.     

> __< k​ayabanerve:matrix.org >__ The unfortunate discussion is that if we want lower confirmations, the solution is PoS at least as a secondary layer.     

> __< k​ayabanerve:matrix.org >__ That's unfortunate not because of my opinions on PoS, yet because I can't imagine that discussion being well received.     

> __< rbrunner >__ You can bet :)     

> __< r​ucknium:monero.social >__ rbrunner: Depends on the threat actor. If the adversary is just buying hashpower at a linear cost, then the adversary will probably just perform a 51% attack. Then any block lock is irrelevant. If the threat model is a mining pool operator, then the risk table is relevant.     

> __< k​ayabanerve:matrix.org >__ As a secondary layer, we'd still be PoW. We'd just have some declaration of validators (with transparent stake) who cement the PoW blocks.     

> __< r​ucknium:monero.social >__ Or...rolling checkpoints! :D     

> __< rbrunner >__ I think that table is at least a nice new tool to direct people to and have them check the results if they vote for lowering from 10     

> __< r​ucknium:monero.social >__ If a minority-hashpower attack is assumed to be unlikely, then evaluation of a safe N block lock would analyze benign re-orgs. Which are pretty shallow in the empirical record. (There are papers on the theoretical benign re-org depth that we could look at)     

> __< r​ucknium:monero.social >__ I will probably clean up the gist and put it in the 10 block lock GitHub issue.     

> __< r​ucknium:monero.social >__ Or one could say that the risk of tx invalidation from a rare, shallow re-org caused by a malicious double spend attack is an acceptable risk     

> __< r​ucknium:monero.social >__ If an attacker cannot earn money from a DS because any of the big targets have high confirmation times, then there will not be the collateral damage to other users, anyway.     

> __< rbrunner >__ I think inflicting "reputational damage" is also a possible motivation for people with money to burn through     

> __< r​ucknium:monero.social >__ And the 10 block lock doesn't prevent a victim from accepting a tx at 5 confirmations, then getting double-spent against. It just prevents collateral damage of txs necessarily being invalidated because they referenced a now-invalid merkle tree.     

> __< r​ucknium:monero.social >__ More things to think about. We can end the meeting here.     

> __< j​effro256:monero.social >__ Thanks everyone!     

> __< a​leenor:matrix.org >__ imo if you use monero regularly it's just something you learn to account for ahead of time     

> __< a​rticmine:monero.social >__ Thanks     

> __< k​ayabanerve:matrix.org >__ If we pad outputs, we can make standard practice for a payment to X to be to use multiple outputs for the one payment.     

> __< o​ne-horse-wagon:monero.social >__ Which is why I wonder how big of a problem is the 10 block lock?  It has served Monero well all these years.     

> __< r​ucknium:monero.social >__ Everyone hates the 10 block lock.     

> __< a​leenor:matrix.org >__ I've often wondered too. it used to bother me in the beginning, but then I adapted. it seems that it mostly bothers newbies and infrequent users, it's probably a decent percentage     

> __< a​leenor:matrix.org >__ of course, I would also prefer if it wasn't there     

> __< r​ucknium:monero.social >__ In most cryptocurrencies, you can spent an output from a tx that is in the mempool/txpool. You can chain them together.     

> __< r​ucknium:monero.social >__ In Bitcoin Cash, some services were hitting their limit of 50 chained txs in the mempool. Programmers changed an algorithm from O(n^2) to something faster and eliminated the limit a few years ago.     

> __< a​leenor:matrix.org >__ yeah. it doesn't make intuitive sense either, like being handed change in cash and not being able to get it out of your pocket for 20 mins. it catches people by surprise     

> __< a​leenor:matrix.org >__ but with the current ring size arrangement I also appreciate why it's there     

> __< k​ayabanerve:matrix.org >__ Rucknium: I have scheduling code to avoid exactly that bound on Bitcoin (and derivatives).     

> __< r​ucknium:monero.social >__ If you added BCH to Serai instead of BTC, you wouldn't have had to worry about it :P     

> __< k​ayabanerve:matrix.org >__ Silence shill D:     

> __< rbrunner >__ With FCMP++ churning / "PocketChange" and similar mechanisms to produce outputs for oneself are much less of a privacy problem than today with rings, right? While they still can bloat the chain, of course     

> __< k​ayabanerve:monero.social >__ Correct  

# Action History
- Created by: Rucknium | 2024-09-25T16:24:45+00:00
- Closed at: 2024-10-09T14:59:24+00:00
