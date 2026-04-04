---
title: Monero Research Lab Meeting - Wed 25 October 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/913
author: Rucknium
assignees: []
labels: []
created_at: '2023-10-25T15:02:56+00:00'
updated_at: '2023-11-01T17:01:07+00:00'
type: issue
status: closed
closed_at: '2023-11-01T17:01:07+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

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

#910 

# Discussion History
## j-berman | 2023-10-25T18:57:22+00:00
Meeting logs

```
17:00:44 <Rucknium> Meeting time! https://github.com/monero-project/meta/issues/913

17:00:52 <Rucknium> 1) Greetings

17:01:24 <m-relay> <v​tnerd:monero.social> Hi

17:01:55 <rbrunner> Hello

17:03:20 <Rucknium> 2) Updates. What is everyone working on?

17:03:23 <m-relay> <j​berman:matrix.org> hello

17:04:08 <m-relay> <h​into.janaiyo:matrix.org> hi

17:04:26 <m-relay> <v​tnerd:monero.social> still on subaddresses in lws :/ getting to the testing phase
though; the upsert algorithm is a pain

17:04:27 <Rucknium> me: Translating jeffro256's explanation of the wallet2 decoy selection algorithm (
https://github.com/jeffro256/monero/blob/decoy_selection_md/docs/DECOY_SELECTION.md ) into a mathematical
formula.

17:05:11 <Rucknium> My draft is here. It might have an off-by-one error, but It's close to done:
https://www.overleaf.com/read/ndbtkwrbrdjq

17:06:41 <m-relay> <j​berman:matrix.org> me: hardening the Seraphis wallet lib scanner for legacy wallet
scanning + some work on fcmp integration getting the rust code running from the monero repo in c++

17:07:19 <Rucknium> 3) Discussion. What do we want to discuss?

17:08:20 <m-relay> <j​berman:matrix.org> I wrote up a comment yesterday regarding Seraphis migration txs
including {pre-RingCT, post-RingCT, coinbase} outputs as members of the same ring signature here:
https://github.com/monero-project/research-lab/issues/59#issuecomment-1778565614

17:08:45 <m-relay> <j​berman:matrix.org> I believe it's been discussed in the past in MRL, but since then,
there's been a solid push to separate coinbase outputs when spending, which is at odds with that design
decision for Seraphis, so wanted to bring it back up for discussion

17:09:34 <m-relay> <j​berman:matrix.org> tagging UkoeHB in case they're around too

17:11:27 <rbrunner> Do you have a link to that discussion about separating?

17:11:40 <rbrunner> Also already quite a while back, I think

17:12:05 <rbrunner> And maybe a bit less pressing due to changes in p2pool, if I remember correctly

17:12:19 <Rucknium> Would it be possible to combine current RingCT and Seraphis enotes in the same ring? I
thought the answer was "no", but I want to check.

17:13:49 <m-relay> <j​berman:matrix.org> you mean a discussion about combining? here's a link about separating
coinbase from non-coinbase: https://github.com/monero-project/research-lab/issues/109

17:13:52 <Rucknium> Users producing transactions today cannot create a non-RingCT enote, right? I can't
remember the non-mixable rules exactly.

17:14:32 <rbrunner> jberman: Yup, that one, thanks

17:14:33 <m-relay> <j​berman:matrix.org> it's not possible to combine current RingCT and Seraphis enotes in
the same ring, no

17:15:22 <m-relay> <j​berman:matrix.org> users producing txs today *can* create non-RingCT enotes

17:16:19 <m-relay> <j​effro256:monero.social> Hi sorry Im late

17:16:29 <Rucknium> Combining RingCT and non-RingCT enotes in the same ring would be a new feature under the
Seraphis proposal, right? Cannot do that today.

17:16:32 <m-relay> <j​berman:matrix.org> IIRC double checking

17:16:55 <m-relay> <j​berman:matrix.org> correct, combining ringCT and non-RingCT in the same ring would be a
new feature

17:17:05 <m-relay> <j​berman:matrix.org> and cannot do that today

17:18:15 <m-relay> <j​effro256:monero.social> What would be the benefit of that? To me, that seems like you
would be reducing your anon set OR revealing your amount

17:18:49 <m-relay> <j​berman:matrix.org> the benefit would be providing greater anonymity for very old pre-
RingCT outputs

17:19:33 <m-relay> <j​effro256:monero.social> So would everyone include a couple very old pre-RingCT outputs
in their rings?

17:20:27 <m-relay> <j​berman:matrix.org> no they would just be included in the set of all enotes from which
the wallet would select decoys

17:20:31 <m-relay> <v​tnerd:monero.social> I dont see how this works given that those outputs had public
amounts. Could you have multiple pre-ringct outputs in a ring? I guess it would work because only the ZKP
would "know" which amount was the real one

17:20:59 <m-relay> <j​berman:matrix.org> it works the same way you can include coinbase outputs in rings today

17:21:23 <m-relay> <j​berman:matrix.org> as per this issue: https://github.com/monero-project/research-
lab/issues/59

17:22:19 <m-relay> <j​berman:matrix.org> Rucknium: here's a comment I wrote in the past explaining how it's
possible to create pre-RingCT outputs today: https://github.com/monero-
project/monero/pull/8178#issuecomment-1081307990

17:22:28 <m-relay> <v​tnerd:monero.social> ah right. This is separate from seraphis then, but still requires a
hard-fork iirc

17:22:45 <m-relay> <j​berman:matrix.org> right

17:24:23 <rbrunner> From your comment, what would be needed: "A database migration that stores total output
counts not keyed by amount" People would probably cry out in joy ...

17:25:42 <rbrunner> And maybe hordes of people running into the problem that they don't have enough harddisk /
SSD space for something like that

17:25:45 <Rucknium> I think there's a small privacy benefit to allowing pre-RingCT and RingCT enotes in the
same ring. Is it worth the engineering effort? You have to change how the RPC responds when wallets ask it for
the output age distribution, too.

17:27:02 <Rucknium> FWIW, I support requiring coinbase and non-coinbase enotes to be in separate rings.

17:27:31 <m-relay> <j​berman:matrix.org> 8 bytes per output + 8 bytes per block I think would be the extra
data stored, so nothing crazy

17:28:13 <m-relay> <j​effro256:monero.social> So if a pre-RingCT output were to be spent, they would not do
decoy selection from outputs with their amount, but instead everything? I think this has a couple trade offs.
Since in the future, those outputs will be so so old. If we naively make a heuristic that says "if an old pre-
RingCT output is in a ring, it's the true spend", we might actually be correct more often than not

17:29:07 <m-relay> <j​berman:matrix.org> yes to your question

17:29:52 <Rucknium> If the decoy selection distribution is set up correctly, then that heuristic shouldn't
work. Setting it up correctly would require more work and thought.

17:30:09 <m-relay> <j​berman:matrix.org> that's probably a fair point. especially if you have a single tx with
>1 rings with a pre-RingCT output in it

17:30:55 <Rucknium> Right now I'm ignoring non-RingCT outputs in the new proposed decoy selection algorithm
distribution.

17:31:28 <m-relay> <j​berman:matrix.org> and spending pre-RingCT outputs a user probably has multiple which
would be spent in a single tx

17:32:00 <Rucknium> If you have a big consolidation (lots of inputs) of very old outputs, then it's easier to
guess the real spend even if they are RingCT enotes.

17:32:55 <m-relay> <j​berman:matrix.org> that's true, but it's even easier with pre-RingCT

17:33:19 <m-relay> <j​berman:matrix.org> and we're talking about a change to enhance privacy specifcally for
spending very old outputs

17:34:29 <rbrunner> Seems like a hard sell to me, without understanding all the details yet however

17:34:37 <m-relay> <j​berman:matrix.org> i.e. we're talking about a likely situation where the user isn't
getting much benefit anyway from constructing a ring sig that includes both ringCT and pre-RingCT

17:35:21 <rbrunner> Maybe for a true privacy gain one would have to build a ring only out of pre-RingCT txs?

17:35:43 <rbrunner> Party like it's 2017 :)

17:35:54 <Rucknium> The best thing for users with pre-RingCT outputs to do is to self-spend so their outputs
are RingCT. How many of those users know that?

17:36:17 <m-relay> <j​effro256:monero.social> We could put in a wallet rule that if you're spending old
outputs, you should churn to yourself once first so that the amount is definitely hidden during the next tx

17:36:27 <m-relay> <j​effro256:monero.social> Haha you read my mind

17:38:07 <Rucknium> I can come back next week with data on how many recent rings have pre-RingCT enotes. Or in
a couple of days.

17:38:14 <rbrunner> And the CLI wallet would most probably the only one that would really bother to properly
implement that including informing the user in a sensible way ...

17:39:29 <m-relay> <j​effro256:monero.social> Because some output amount anon sets are genuinely tiny (i.e.
they're "unmixable"). There's a lot of edge cases to consider with spending pre-RingCT outputs, but basically
all of them can be fixed if you churn to yourself first, then reap the benefit of the large anon set and
hidden amounts of all RingCT outputs.

17:39:44 <m-relay> <j​berman:matrix.org> "Maybe for a true privacy gain one would have to build a ring only
out of pre-RingCT txs?" -> this is already the case, except when spending a pre-RingCT amount that doesn't
have enough amounts to mix with. Today wallets mix pre-RingCT with other pre-RingCT outputs of the same
amount. Technically this could be changed with a hard fork to allow spending pre-RingCT of any amount in
<clipped message>

17:39:44 <m-relay> <j​berman:matrix.org> a single ring, and create RingCT outputs (or Seraphis enotes)

17:40:01 <Rucknium> jeffro256: Good summary

17:40:22 <rbrunner> Ah, I see

17:40:52 <rbrunner> Already a lot of complexity built in for something that now must be quite rare

17:41:13 <Rucknium> There are probably more txs created with nonstandard fees in a week than txs using non-
RingCT enotes in a year.

17:41:27 <rbrunner> Just the old pre-RingCT tx construction code left standing then, I guess

17:42:14 <m-relay> <j​berman:matrix.org> agree this is added complexity for something rare, I'm generally for
a warning in wallets and moving forward, bu the Seraphis wallet lib would need to be modified to match this
behavior from wallet2 too

17:42:14 <m-relay> <j​effro256:monero.social> And pre-RingCT spends get rarer and rarer each month, I don't
know if its worth adding consensus rules to accommodate that when you can get the same benefits if you exert a
little bit extra tx fees

17:42:31 <Rucknium> I like jeffro's idea of producing an error or required confirmation in wallet2 if you
don't self-spend non-RingCT enotes first.

17:43:11 <rbrunner> But that would be only up to the Seraphis hardfork?

17:43:38 <m-relay> <j​berman:matrix.org> no, for after too, since pre-ringct outputs need to always be
spendable using the Seraphis wallet lib

17:44:31 <rbrunner> Do I understand correctly that this would mean to swap out the library's current solution
to that pre-RingCT spending case, and program a new one?

17:45:07 <Rucknium> The small downside of a strongly suggested self-spend is that it is likely that the real
spend will happen a short time after that spend. But with 128+ ring size, that is less of a concern.

17:45:54 <m-relay> <j​berman:matrix.org> correct rbrunner . I think that would still be simpler than the
alternative which is: consensus changes to support pre-RingCT + post-RingCT in the same ring, database
migration, and RPC changes

17:46:42 <m-relay> <j​effro256:monero.social> And again, if we wanted to really be authoritative about the
privacy in this case, we could force (or at least warn) users not to spend these outputs immediately after
they're unlocked. But that's honestly a concern for every single user with the 10-block-lock

17:49:48 <Rucknium> With a DSA that matches the real spend age distribution, that shouldn't really be a
concern to every user.

17:50:47 <Rucknium> Since a quick re-spend would be just as likely to be a decoy.

17:51:06 <m-relay> <j​effro256:monero.social> True

17:53:13 <rbrunner> I am a bit confused now, frankly. That problem with those coinbase enotes, doesn't that
get a lot less problematic with those large Seraphis rings?

17:53:47 <Rucknium> Yes, but why waste ring member slots?

17:54:38 <rbrunner> Well, because maybe the added complexity is not worth the presumably little privacy gain,
with 128-member rings?

17:55:18 <m-relay> <j​berman:matrix.org> one thing I wanna make clear: even after the Seraphis hard fork,
users would still need to construct 16 member rings *sometimes* when spending older outputs

17:55:39 <m-relay> <j​berman:matrix.org> where older outputs = any output pre-Seraphis

17:56:13 <rbrunner> Sometimes? What would be the condition then?

17:56:19 <m-relay> <j​berman:matrix.org> users have to migrate their older outputs into Seraphis enotes, in
order to construct Seraphis membership proofs

17:57:04 <m-relay> <j​berman:matrix.org> that migration happens in a tx. any time you spend a pre-Seraphis
output that existed in the chain before the Seraphis fork

17:57:47 <Rucknium> jeffro256 has already written code to not spend coinbase outputs in rings IIRC. He can say
how high the complexity is.

17:57:56 <rbrunner> Ok. Here we have a tangle of so many things all influencing each other that my poor brain
is overloaded right now.

17:58:10 <Rucknium> I mean, in rings that spend non-coinbase enotes.

17:58:58 <m-relay> <j​effro256:monero.social> How do you migrate outputs which you don't know the private key
of ?

17:59:07 <rbrunner> I think interesting is the complexity past-Seraphis-hardfork, and the new, additional work
needed to get there, and what we win with all this

17:59:42 <rbrunner> Huh? You don't, I assume.

17:59:44 <m-relay> <j​berman:matrix.org> you migrate your own outputs in a migration tx. maybe "migration tx"
is a poor term

18:01:40 <Rucknium> Arrange a wishlist of privacy features. Measure their privacy benefit and engineering
effort. Then do a cost-benefit analysis to choose which ones to include :)

18:01:57 <m-relay> <j​berman:matrix.org> I receive a 0.5 Monero RingCT output today. Let's assume the Seraphis
hard fork is 1 year from now. After the Seraphis hard fork, when I spend this 0.5 Monero RingCT output, my
wallet would need to construct a CLSAG 16 member ring composed of pre-Seraphis outputs. That is the "input"
side of the tx. On the "output" side of the tx, my wallet would create Seraphis enotes, which can <clipped
message>

18:01:58 <m-relay> <j​berman:matrix.org> then in future txs be included in Seraphis-style membership proofs

18:01:58 <m-relay> <j​effro256:monero.social> Can I not construct a Seraphis tx with normal CLSAG inputs on
RingCT ring members which creates new Seraphis enotes?

18:02:45 <m-relay> <j​effro256:monero.social> Oh okay that's how I assumed it worked

18:03:24 <m-relay> <j​effro256:monero.social> It sounded like you were saying that you migrate the outputs in
the transaction then immiedately use them in Seraphis membership proofs in the same tx

18:03:48 <m-relay> <j​berman:matrix.org> ah

18:03:56 <m-relay> <j​berman:matrix.org> does it all make sense now rbrunner ?

18:04:00 <Rucknium> The 16 ring size for CLSAG could be raised when the Seraphis hard fork goes into effect
AFAIK. That would increase the tx size of those tx a lot.

18:07:06 <Rucknium> We are past the hour. Discussion on this can continue here and on the GitHub issue.

18:08:24 <rbrunner> jberman: Yes, but now you still have to add pre-RingCT txs into the picture, seems to me

18:08:52 <m-relay> <j​effro256:monero.social> Yeah the complexity was sort of high but honestly not too bad.
My solution used a database migration just because it was miles faster. I simply created a table which was
exactly like the RingCT distribution but only for coinbase outputs. You then download those two distributions
over RPC, then according to which output you're spending, you pick from the corresponding distribution

18:12:03 <m-relay> <j​berman:matrix.org> rbrunner: right. either those CLSAG rings could be composed of the
set of {pre-RingCT, RingCT, coinbase} outputs, or pre-RingCT rings can be kept separate from RingCT the same
as wallet2 (and consensus) implements today

18:13:27 <m-relay> <j​berman:matrix.org> i.e. either those CLSAG rings could potentially include {pre-ringCT,
ringCT, coinbase} outputs all in the same ring, or the latter

18:15:29 <rbrunner> Sometimes I wish we could just emulate the nonsense and borderline scams of other coins
and force all users through a non-trustless coin swap here. Problems solved :)

18:16:53 <rbrunner> It's so exhausting to be, and to stay, a real and trustworthy cryptocurrency

18:19:26 <m-relay> <j​effro256:monero.social> Fr

18:19:33 <m-relay> <j​berman:matrix.org> honestly the Seraphis hard fork isn't particularly relevant to the
decision of whether or not to include pre-RingCT and RingCT outputs in the same ring, like vtnerd was saying.
I mentioned it because the Seraphis wallet lib does that

18:20:10 <m-relay> <j​effro256:monero.social> So the seraphis wallet lib already mixes pre-RingCT and RingCT ?

18:20:16 <m-relay> <j​berman:matrix.org> yes

18:21:02 <m-relay> <j​berman:matrix.org> it constructs txs like that, but there is still a lot of work that
needs to be done to actually make it work in a wallet

18:22:05 <m-relay> <j​berman:matrix.org> (consensus changes, database migration, RPC changes)

18:23:06 <m-relay> <j​effro256:monero.social> interesting... I would prefer it to not be able to mix (at
consensus) unless there's evidence that points to it being a net positive for privacy. So I would (personally,
but I can't tell anyone what to do) hold off on that work
```

# Action History
- Created by: Rucknium | 2023-10-25T15:02:56+00:00
- Closed at: 2023-11-01T17:01:07+00:00
