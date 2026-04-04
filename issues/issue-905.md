---
title: Monero Research Lab Meeting - Wed 04 October 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/905
author: Rucknium
assignees: []
labels: []
created_at: '2023-10-04T14:46:59+00:00'
updated_at: '2023-10-11T14:35:44+00:00'
type: issue
status: closed
closed_at: '2023-10-11T14:35:44+00:00'
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

#901 

# Discussion History
## plowsof | 2023-10-07T13:20:03+00:00
Logs 
```
17:00:41 <Rucknium> Meeting time! https://github.com/monero-project/meta/issues/905

17:00:47 <Rucknium> 1) Greetings

17:01:09 <tevador> Hi

17:01:12 <m-relay> <j​effro256:monero.social> Howdy

17:01:15 <rbrunner> Hello

17:02:47 <Rucknium> 2) Updates. What is everyone working on?

17:04:30 <m-relay> <j​effro256:monero.social> discussing and implementing Jamtis changes, trying to formalize
wallet2 decoy selection algo

17:04:32 <Rucknium> me: Working with jeffro256 on interpreting wallet2's decoy selection algorithm. Second,
excluding the set of txs with nonstandard fees from analysis of on-chain ring member age.

17:05:55 <Rucknium> 3) Discussion. What do we want to discuss?

17:06:40 <tevador> Has a decision been made to go forward with the Jamtis changes?

17:07:31 <m-relay> <j​effro256:monero.social> I brought up an issue on the Jamtis gist, but I wanted to
hopefully dive deeper into it here in this meeting. Simply put, the issue is this: multiple self-send enotes
within a transaction creates a significant statistical fingerprint for finding outgoing enotes for anyone with
knowledge of the find-received/assist-filter/filter-involved key (whatever we're calling it in the new or old
scheme)

17:08:46 <Rucknium> Can you post the gist URL again for the meeting log?

17:08:47 <m-relay> <j​effro256:monero.social> I think most people (correct me if wrong) are in agreement about
using the extra public key to guard against third-parties knowing the nominal address tags

17:09:32 <tevador> I generally agree with the change regarding self-send enotes, although it has a potential
to increase the required wallet traffic 2.5x or more.

17:10:12 <m-relay> <j​effro256:monero.social> Yes, you can find my original comment here: https://gist.github.
com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4706509#gistcomment-4706509

17:11:22 <tevador> There was a pushback against dynamic view tags and I expressed my opinion that the proposed
Jamtis changes might not be worth it without them: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d
17024?permalink_comment_id=4708830#gistcomment-4708830

17:11:46 <m-relay> <j​effro256:monero.social> Yes, which is unfortunate, but luckily only affects light
wallets, and it's limited a certain constant. And *if* we have a decent flexible view tag scheme, hopefully we
can mitigate performance issues down the line

17:12:17 <rbrunner> Don't understand half of that stuff, frankly, I just get the impression that things are
still pretty much in flux, not yet "converging" to a solution

17:12:34 <m-relay> <j​effro256:monero.social> I highly disagree that the extra public key is useless without
the view tag changes

17:13:08 <tevador> I didn't say "useless".

17:13:39 <tevador> "potentially wasteful" would be the right expression

17:14:41 <rbrunner> At the end that Reddit poll "Do you support variable size viewtags?" only had around 40
voters in total.

17:15:06 <tevador> One advantage of the original 3-key design is that it doesn't cater to remote scanners, yet
still improves them significantly with lower costs.

17:17:05 <m-relay> <j​effro256:monero.social> Okay fine, but still I disagree with this sentiment: "The static
8-bit view tag works well with a "medium" transaction volume, which is a range from mid tens of thousands to
mid hundreds of thousands of enotes per day.". A static 8-bit view would work well for *any* transaction
volume, assuming that light wallet users always can handle ~0.5% of the traffic as full wallets

17:17:35 <m-relay> <j​effro256:monero.social> We might not be able to assume that for all users, but it's not
a terrible assumption

17:18:55 <m-relay> <j​effro256:monero.social> If we assume constant load handling capacity, then yes static
view tags are bad for high volume (and low volume for privacy)

17:20:05 <Rucknium> What kind of use cases do pre-signed transactions, signed days+ in advance, fill? There's
an atomic swap protocol that needs them, but I don't know if you would really need pre-signing for that more
than 24 hours in advance.

17:20:26 <Rucknium> Hoenisch et al. (2022) "Lightswap: An atomic swap does not require timeouts at both
blockchains"

17:20:35 <m-relay> <j​effro256:monero.social> Yeah this is true, it's nice that it's effectively 0-cost.
Although I think believe that light wallets will take a bigger part in the ecosystem from Jamtis onwards,
especially with mobile wallets

17:20:52 <tevador> "assuming that light wallet users always can handle ~0.5% of the traffic" -> do we have
something to base this assumption on?

17:23:44 <rbrunner> I would claim that with actually tens of thousands of enotes *per day* all kinds of
bottlenecks would spring up, with 1-byte viewtags only one among many.

17:24:51 <m-relay> <j​effro256:monero.social> One use case I can think of is if you wanted a dead man switch
to pass on your funds to your next of kin. But more generally, delegating membership proofs lets you make
transaction cermemonies that can take a while to complete but don't necessarily make fingerprintable decoy
selections

17:24:52 <tevador> We currently have about 50 000 per day.

17:25:33 <m-relay> <j​effro256:monero.social> Yeah this is true, it's nice that it's effectively 0-cost.
Although I believe that light wallets will take a bigger part in the ecosystem from Jamtis onwards, especially
with mobile wallets

17:25:38 <rbrunner> Yeah, just saw that, I have to switch my argument to the "hundreds of thousands" then :)

17:27:06 <rbrunner> Multisig transactions can also take a while until everybody signed, right?

17:28:32 <tevador> We could hardfork in the future to adjust the view tag, but we'll be stuck with the address
format forever. something to bear in mind.

17:28:37 <m-relay> <j​effro256:monero.social> There is an argument to be made that if light wallet users can't
handle 0.5% of transaction prefix traffic, then our full nodes will have to handle far too much traffic for
the network to be as decentralized as it should be

17:29:19 <m-relay> <j​effro256:monero.social> Exactly

17:29:47 <rbrunner> So the decision how many keys to have there is much more important than the decision
whether fixed size viewtag or flexble ones?

17:29:55 <tevador> Yes.

17:31:27 <rbrunner> And well, where do we stand regarding opinions to introduce, or not, another key in the
address? I lost overview a bit.

17:32:45 <tevador> There are pros and cons of both.

17:33:21 <rbrunner> Reminds me of the unlucky tx_extra story ...

17:34:01 <rbrunner> In regard of difficult decision processes, I mean

17:37:20 <m-relay> <j​effro256:monero.social> I thinks the pros of the extra public key in the address far
outweigh the downsides, but I admit a lot of that is because of my predisposition for imagining what actually
decent light wallets could give us

17:39:37 <rbrunner> My focus is more on what I consider something like a "hole" in Jamtis that doesn't belong
there in anotherwise so beautiful and powerful construct

17:39:55 <rbrunner> that story with the dangers of repeated use of an address

17:40:09 <m-relay> <j​effro256:monero.social> what would you think about flexible sized view tags by hard
consensus rules, but which the relay rules enforce a constant size

17:40:11 <rbrunner> with remote scanning services in the picture

17:40:53 <tevador> The 3rd key gives Janus attack protection and a separate key to view amounts, which is
generally useful to everyone. The 4th key is only for light wallets. Users running their own nodes won't see
much benefit.

17:41:11 <m-relay> <j​effro256:monero.social> And the bad thing is that it is out of your control whether
someone sends to your public address more than once. Trying to mitigate it as a light wallet user is basically
impossible

17:42:11 <UkoeHB> Have the proposed jamtis design changes stabilized? I have not been following the
discussion.

17:42:35 <rbrunner> So it's a bit also a discussion whether we accept light wallets as "first class citizens",
as integral part of the system

17:43:19 <rbrunner> UkoeHB: From what I can see, no ...

17:44:10 <m-relay> <j​effro256:monero.social> tevador and I have agreed upon a key derivation tree, public
address layout, and sender-receiver secret derivation scheme *if* we choose to add the extra pubkey to the
address. The main point on contention is how to do the view tags

17:45:00 <tevador> A soft-rule for view tags would probably work.

17:45:45 <tevador> But I would not see the 3-key/4-key debate as settled yet regardless of the view tag
decision.

17:45:46 <rbrunner> But those new problems / points that you mentioned could force some re-considerations
there, worst-case?

17:47:18 <rbrunner> "multiple self-send enotes within a transaction creates a significant statistical ..."

17:47:20 <m-relay> <j​effro256:monero.social> With a soft-rule flexible view tag,  if we later wanted to
switch to your dynamic `trunclog2(3 * num_output_100k / 200000)` view tag method, we could do so without a
consensus change

17:47:44 <tevador> good point

17:48:37 <tevador> If a large portion of users start using 3rd party scanners, then the 4th key is most likely
worth it. I'm not sure if we have any data on this.

17:49:48 <rbrunner> I am not sure current data is very valuable if we switch to a third-party scanning system
with significantly less privacy problems

17:50:45 <rbrunner> And one that could also technically be simpler to implement, as an add-on to normal
wallets instead of fully different wallets to connect to light-wallet servers

17:50:48 <m-relay> <j​effro256:monero.social> Yeah, it's impossible to tell for sure. However, could we agree
that the usage for Jamtis light wallets would likely be even higher than usage of MyMonero, monero-lws, etc
considering that the privacy is orders of magnitude better in many ways?

17:51:43 <rbrunner> For me it's telling how already today pretty much *every* multi-coin wallet uses MyMonero
technology for their XMR support

17:51:49 <rbrunner> privacy be damned

17:52:32 <rbrunner> I think light-wallet use under Jamtis has the potential to become a stampede.

17:53:09 <tevador> More users will probably choose some kind of light wallet setup with Jamtis, but it's not
clear if it's +5% or +50% of users. Running a local node will always be more private.

17:53:10 <rbrunner> Just think about all the third-world countries where you still buy your mobile data
traffic in megabytes

17:54:13 <Rucknium> MyMonero had a slightly nonstandrad fee calculation for a while. If we knew how to
identify them on chain, we could look back at the data. The fundraiser to have mj do that nonstandard fee
investigation was unsuccessful.

17:54:50 <rbrunner> Was that on Magic?

17:55:11 <Rucknium> I think MyMonero's decoy selection algorithm is slightly different, too, but it's harder
to see through the statistical noise of just 15 decoys per ring

17:55:17 <Rucknium> rbrunner: Yes

17:55:28 <rbrunner> Hmm, didn't even hear about that.

17:55:51 <tevador> fluffypony could just say how many users they have...

17:56:15 <rbrunner> Maybe they are not allowed to by some contracts

17:56:43 <Rucknium> IIRC fluffypony stated somewhere on IRC that MyMonero has low single digits in percent of
txs. But that probably does not include the other wallets like Guarda that use MyMonero.

17:56:44 <tevador> or just the % of matched outputs

17:57:15 <rbrunner> But, well, yeah we don't know the number of probable light wallet users on Jamtis, but on
the other hand, couldn't even 5% percent lead to problems without a 4th public key?

17:58:29 <tevador> Someone could do the math and figure that out. However, 3-key Jamtis is still way more
private than cryptonote.

18:01:12 <m-relay> <j​effro256:monero.social> This is true, but I want to reiterate again that the scenarios
in which you lose privacy are basically impossible to plan for

18:02:31 <Rucknium> No. It was Reddit, not IRC.
https://www.reddit.com/r/Monero/comments/uth0un/comment/i9bk0sf/

18:02:50 <Rucknium> "Whilst we don't disclose user numbers, I can assure you that the number of viewkeys we
have is not even double-digit percentages."

18:05:00 <Rucknium> We can end the meeting. Discussions about dynamic view tag length and the 4th public key
will continue :)


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-10-04T14:46:59+00:00
- Closed at: 2023-10-11T14:35:44+00:00
