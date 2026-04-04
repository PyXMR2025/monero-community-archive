---
title: Monero Research Lab Meeting - Wed 15 February 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/797
author: Rucknium
assignees: []
labels: []
created_at: '2023-02-12T19:33:35+00:00'
updated_at: '2023-02-20T19:33:56+00:00'
type: issue
status: closed
closed_at: '2023-02-20T19:33:55+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss: [Consider removing the tx_extra field](https://github.com/monero-project/monero/issues/6668).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#794 

# Discussion History
## rbrunner7 | 2023-02-15T06:57:31+00:00
I have a proposal about 2. I am a bit late with that, I know, but so be it:

It's one possible definition of **madness** that you try the same again and again in the hope that suddenly the outcome will be different.

We discuss this tx_extra issue on GitHub since middle of 2019, almost 3 years now, without reaching consensus. We missed about 2 or even 3 excellent chances to improve something in this regard, in the form of hardforks, mostly because of missing consensus.

For me, our failure to find some consensus so far in this matter mutated into a bigger problem than tx_extra itself. Because, frankly, we live with it for 8 years now, and the sky hasn't falllen yet, right? But if the size of our dev community has passed a threshold where we need some fresh ideas about how to make difficult and controversial decisions, without noticing, that would be bad.

So, a proposal: Do not let us discuss removing tx_extra itself later today and merely hash and rehash the same arguments that already fill the two GitHub issues and waste that hour of meeting with doing so, but let us talk a bit about possible ideas how to **improve our decision process**.


## tarris034otheracc | 2023-02-15T07:53:47+00:00
I would like to point out that removing tx_extra will not remove the possibility of putting illegal data on the blockchain as you can do so as well using crafted amounts that would correspond to data, add to this the view key and you have potentially illegal data shared to everyone via sites that will decrypt it for you.

On the other hand maybe it posses a regulatory risk of forcing CeX to include some tracking data ? 

## spirobel | 2023-02-15T07:55:31+00:00
@rbrunner7 
> how to improve our decision process.

I agree with this! 

We should establish some clear rules to accept or dismiss proposals for protocol changes and have a formalized process around this. Here are 3 simple rules that a proposal should follow:

To avoid fatal mistakes, consensus and relay rules should only be added if they meet these requirements:

1.  **they should have a clear goal**
2.  **they should achieve that goal**
3.  **they should be as simple as possible**
If rules are added in the heat of the moment as a reaction to things without clearly considering this, people will trust the protocol and its continuity less and less.

Neither the tx_extra size limit on the relays nor the statistical uniformity checks pass these requirements.

It seemed like an adhoc reaction to ordinals that was well meant, but after more consideration can not achieve its objective.

## fluffypony | 2023-02-15T08:05:21+00:00
There's a [good post from Apache on how they use "broad consensus"](https://blogs.apache.org/comdev/entry/how_apache_projects_use_consensus) that bears reading. My suggestion is that a decision maker is appointed, maybe a maintainer or high-value committer, and their job is to focus attention + read the room and ultimately make the decision that they believe reflects the broad consensus or loose consensus of the group.

Some people will be upset with the decision, but other people will be upset with no decision being made. Someone is going to be upset, and that's fine.

The only real technical comment I want to make here is that tx_extra is a field of convenience, but data can be packed into all sorts of places (range proofs, output "addresses", etc) so removing it does not really remove functionality, it just means developers need to be a little more creative.

## spirobel | 2023-02-15T08:36:09+00:00
>My suggestion is that a decision maker is appointed, maybe a maintainer or high-value committer, and their job is to focus attention + read the room and ultimately make the decision that they believe reflects the broad consensus or loose consensus of the group.

That is basically the status quo. It means that decisions are based on the highly subjective feelings of people that draw their legitimacy from a highly subjective basis. 

There should be at least a basic process or ruleset to go by.

I think these 3 simple questions are a good place to start. It is much easier to find a clear answer to those without going in circles forever:

1. **What is the goal of the proposed change?**
2. **Does it achieve this goal?**
3.  **Is it the simplest possible solution?**

>The only real technical comment I want to make here is that tx_extra is a field of convenience, but data can be packed into all sorts of places (range proofs, output "addresses", etc) so removing it does not really remove functionality, it just means developers need to be a little more creative.

which means that the new rules that were being proposed didn't achieve their goal.

## tarris034otheracc | 2023-02-15T08:49:10+00:00
> which means that the new rules that were being proposed didn't achieve their goal.

By it's own maybe not but it could be part of bigger picture, I don't like this black & white approach.
In this manner we won't be able to polish small things because they ultimately not achieving anything (at the time).

## spirobel | 2023-02-15T09:55:08+00:00
>In this manner we won't be able to polish small things because they ultimately not achieving anything (at the time).

Yes. We should also go back and reevaluate the current ruleset and decide one by one if each rule has a good answer to these three questions.
Rephrased as:


1.  **What is the purpose of this rule?**
2.  **Does it achieve its goal?**
3.  **Is it the simplest possible solution?**



## tarris034otheracc | 2023-02-15T10:04:06+00:00
Maybe we could try create a rule set based on past decisions and see if it fits.

The tx_extra field is still discussed but why it was added in the first place and how much in percentage of the transactions really use it ? is it really enhancing user experience or is it just more convenient for third-parties but could be executed differently ?

If it's something that can be made using other means, then I don't see why it should stay - and if it's used by very small percentage of the network then why the rest of the network should carry the weight ? It's like driving a pick-up truck whole year because once in a month you need to transport something bigger.

## spirobel | 2023-02-15T10:13:26+00:00
>If it's something that can be made using other means, then I don't see why it should stay - and if it's used by very small percentage of the network then why the rest of the network should carry the weight ? It's like driving a pick-up truck whole year because once in a month you need to transport something bigger.

It is used by every single transaction you make. 

>Maybe we could try create a rule set based on past decisions and see if it fits.

Decisions should be made according to basic rules that put rails on the conversation.

I made a proposal for 3 basic rules that are easy to remember and easy to follow.

1. **protocol rules should have a clear goal**
2. **they should achieve that goal**
3. **they should be as simple as possible**

Would you agree with these rules, or do you have a different suggestion?

## rbrunner7 | 2023-02-15T10:49:12+00:00
> I made a proposal for 3 basic rules that are easy to remember and easy to follow.

I think those rules are **anything** but easy to follow. In fact, our almost-3-year-deadlock seems to have as one of the main reasons failing consensus about what the goal(s) should be in the first place. We have several conflicting goals, some people see one of them as paramount, some other people disagree and have a different goal on top of their mind.

For example, some people say "Transactions must be as uniform as possible", other people say "We need some flexibility in the protocol", goals which seem to conflict.

If is was so easy as making 3 bullet points, like you did, and then all stick to that, don't you think we would have agreed on a way to  already years ago?

I am brainstorming about something along the lines of "Agreeing to disagree": If we have something we can't achieve consensus about for more than 1 year, we agree to switch gears and do something else than simply continue to argue back and forth. For example, like @fluffypony suggested, put the problem into the hands of a trusted arbitrator.

## spirobel | 2023-02-15T11:04:34+00:00
>we agree to switch gears and do something else than simply continue to argue back and forth. 

That is a great approach. The 3 rules would aid in detecting this situation. Because they bring the focus back to the goals as quickly as  possible if it becomes clear that a change does not lead to the desired result.

>"Transactions must be as uniform as possible" vs  "We need some flexibility in the protocol"

I do not see it this way. For me this discussion was about: **does the removal of tx_extra achieve its goal?**

The answer to this is a very clear no. And after that became clear we should have moved on to: **why does this goal of increasing transaction uniformity matter and how can we lessen its impact on privacy?**

## tarris034otheracc | 2023-02-15T11:10:09+00:00
> It is used by every single transaction you make.

It's not true, unless I'm out of the loop - it is **included** but used only by some services - not USED on every transaction you send.

> does the removal of tx_extra achieve its goal?
> The answer to this is a very clear no. 

Depends where you stand, for someone else it can be very clear YES - it's making transactions more uniform.
What was the goal again ? what if there are multiple goals ? 

## spirobel | 2023-02-15T11:17:14+00:00
>not USED on every transaction you send.

yes it is! here is the code:
https://github.com/monero-project/monero/blob/451ff7bd91c68cc9861711fbd45587a388df77dc/src/cryptonote_core/cryptonote_tx_utils.cpp#L230

You can also look at any transaction on xmrchain.net and you will  see a tx_extra.

Here is an example: https://xmrchain.net/tx/2a132df5b7f6c7ef7b7a521ec98b8f247e2bd3bc0717b17f168bed4ad24e2a13/1 scroll down and click on show json. And you will see the array.

> What was the goal again ? what if there are multiple goals ?

The goals need to be clearly stated. That was also a problem: shifting of goalposts. You can also see how people shifted their opinions after ordinals happened. If you read the whole thread you can see people debating against standpoints that they held just a few months earlier.




## fluffypony | 2023-02-15T11:18:57+00:00
> yes it is! here is the code: https://github.com/monero-project/monero/blob/451ff7bd91c68cc9861711fbd45587a388df77dc/src/cryptonote_core/cryptonote_tx_utils.cpp#L230

That's because we added a dummy payment ID into every tx for uniformity. That obviously would no longer be needed. Payment IDs have - in any event - been superseded by subaddresses, so this is literal blockchain bloat done for the sake of tx uniformity:)

## tevador | 2023-02-15T11:22:11+00:00
I agree that Monero needs a more formal review process for proposals.

I read the Apache consensus process posted by @fluffypony and it sounds good to me, We could have a committee of 3-7 members who can each vote -1 (reject), 0 (abstain) or +1 (approve) for each proposal.

 There are clearly different categories of proposals depending on how hard they are to reverse:

1. Wallet-side changes.
2. Non-consensus changes (e.g. p2p protocol or relay rules).
3. Consensus changes.

For consensus changes, the commitee members would have a veto right, i.e. if any member votes -1, the proposal cannot be accepted. Otherwise, each of the 3 categories would have some required number of +1 votes to be accepted.

## fluffypony | 2023-02-15T11:25:12+00:00
@tevador I'd support something like that - the only thing is that such a self-assembling committee would need to aim to place their votes in line with what they're viewing as the broad consensus among the community, and not in line with their own ideas / feelings. I don't want to reinvent democracy, but ultimately we're going to be gridlocked otherwise.

Also, I would like to point out that if a change is made that the community actually disagrees with, then miners + node operators will simply not run that code - consensus can also emerge from violent forks, so we shouldn't be afraid of making decisions or having some sort of federated decision making model.

## spirobel | 2023-02-15T11:27:08+00:00
>Payment IDs have - in any event - been superseded by subaddresses, so this is literal blockchain bloat done for the sake of tx uniformity:)

Please dont open this can of worms. Subaddresses superseded standard addresses. Encrypted paymentids are an orthogonal concept to this. You can have integrated Subaddresses in Monero.

>We could have a committee of 3-7 members who can each vote -1 (reject), 0 (abstain) or +1 (approve) for each proposal.

I am strictly against this. We see enough gatekeeping already in the "community crowd funding system".




## tevador | 2023-02-15T11:34:04+00:00
> if a change is made that the community actually disagrees with, then miners + node operators will simply not run that code

In addition to devs, the committee could have representatives of pool operators and economically-relevant nodes (merchants/exchanges), so it would be hard to approve changes that are unacceptable to them.

## spirobel | 2023-02-15T11:37:18+00:00
>In addition to devs, the committee could have representatives of pool operators and economically-relevant nodes (merchants/exchanges), so it would be hard to approve changes that are unacceptable to them.

How do you prevent it from becoming a power tripping cabal? 
What exactly should its mandate be?
Should we allow people on there that attended Davos?
How do we avoid people with vested interests?

## fluffypony | 2023-02-15T11:37:29+00:00
> I am strictly against this. We see enough gatekeeping already in the "community crowd funding system".

A maintainer is a gatekeeper of pull requests anyway, so we already have them.

Furthermore, most open-source projects have people maintaining code forks that don't implement something they disagree with, so there's nothing that would prevent you from operating your own fork of the repo so you can gatekeep things yourself.

Effectively what @tevador is suggesting is moving the burden from a single maintainer to a maintainer-committee, and I think that's a good thing.

## Gingeropolous | 2023-02-15T11:41:05+00:00
I mean, there's this:

![image](https://user-images.githubusercontent.com/10169740/219017684-aab2c30c-a79f-4e9e-a5e4-c5056673329d.png)


## tarris034otheracc | 2023-02-15T11:48:12+00:00
The voting and tx_extra discussion merged here, how about using tx_extra by miners to include votes in the coinbase transaction on the added block, like in Bitcoin ? could help in decision making ?

## fluffypony | 2023-02-15T11:50:03+00:00
> The voting and tx_extra discussion merged here, how about using tx_extra by miners to include votes in the coinbase transaction on the added block, like in Bitcoin ? could help in decision making ?

No, voting by miners is a bad idea, same as stake-weighted voting. Miner votes might be useful to indicate readiness for a particular feature, which is how Bitcoin's soft fork activation works, but miners do not and cannot represent the entirety of the network, nor should developers ever be beholden to them.

## spirobel | 2023-02-15T11:52:41+00:00
So how do you actually join the core team? How do you become part of the cabal?

To solve this problem in a satisfying way means solving the sybil problem.

We need to find a way to give people the opportunity to join the Monero community in a permissionless way and advance through their merits. I dont think sham democratic committees are going to build the money of the future. 


## tarris034otheracc | 2023-02-15T11:57:02+00:00
> So how do you actually join the core team? How do you become part of the cabal?

This question has been already answered in the past along with the concerns for which is a simple answer: if the community don't agree, fork.

## fluffypony | 2023-02-15T11:58:32+00:00
> I mean, there's this:

This has been superseded.

> So how do you actually join the core team? How do you become part of the cabal?

You can't - the Core Team is specifically designed to have no real power or control, be trivially forked away if they're bad, and only replace members if they leave / die / become inactive.

> To solve this problem in a satisfying way means solving the sybil problem.
> 
> We need to find a way to give people the opportunity to join the Monero community in a permissionless way and advance through their merits. I dont think sham democratic committees are going to build the money of the future.

We're not trying to solve this in the grander sense; we're trying to find a way for developers to make decisions around features, in a way that is cognizant of the *requests* of users / ecosystem participants. We have to *try* something before we can refine it. Your path seems to suggest that we must first design the perfect model and then implement it, I'm saying we should implement an imperfect model and then perfect it.

## spirobel | 2023-02-15T12:10:34+00:00
>This question has been already answered in the past along with the concerns for which is a simple answer: if the network don't agree, fork.

If you dont like it leave it. Let the cabal be the cabal. That is not a satisfying answer. Forks are mostly unrealistic or if they do happen they weaken the community.

>You can't - the Core Team is specifically designed to have no real power or control

Would you say it is a bit like the WEF? It supposedly also does not have "real power or control" but still decisions get made in private and the cabal stays among itself behind closed doors?

>We're not trying to solve this in the grander sense; 

Who are "we"? It seems like this is an important problem to solve. How are you going to build a money that people can put their trust in if there are opaque unclear power structures? 

## fluffypony | 2023-02-15T12:12:52+00:00
> Would you say it is a bit like the WEF? It supposedly also does not have "real power or control" but still decisions get made in private and the cabal stays among itself behind closed doors?

What decisions? You're sealioning, and going off topic. Feel free to open an issue on Meta about the Core Team.

> Who are "we"?

The people in this thread and the Monero community in general.

> How are you going to build a money that people can put their trust in if there are opaque unclear power structures?

Monero is nearly 10 years old. I think we've done just fine over the last decade.

## spirobel | 2023-02-15T12:27:11+00:00
>What decisions? You're sealioning, and going off topic. Feel free to open an issue on Meta about the Core Team.

Never mind. I just thought because you attended the WEF meeting in Davos before, you might understand the analogy.
It seems surprising that the Core Team has supposedly no power and control. 

>The people in this thread and the Monero community in general.

Seems a bit presumptuous to speak for the "Monero community in general", but okay you are the boss here.

>Monero is nearly 10 years old. I think we've done just fine over the last decade.

Could have gone better. I really expected to see more progress and adoption. Having private fungible money seems like the killer feature. Should be more successful.
 
The lack of good governance systems is maybe part of the problem.

## tarris034otheracc | 2023-02-15T12:29:48+00:00
> Seems a bit presumptuous to speak for the "Monero community in general", but okay you are the boss here.

This thread is linked on reddit, everyone can join here - not everyone wants to.
Seems you're just trolling now.

## rbrunner7 | 2023-02-15T12:58:23+00:00
Another thought that crossed my mind:

We have our almost-famous-by-now *rough consensus*, and I find an interesting and useful concept, despite being "rough". It's ok that we talk about it, remind each other about it, try to make it part of the identity of the dev community.

We could, and maybe we should, try to add something to that: Some culture of **compromise**.

Because that's it, right? If people can't agree, but still are all share some core goals that are non-negotiable, they have to start making compromises. "Something has to give", and "can't have it all", or there is deadlock, that over time threatens everything.

The most top-level goal I can think of is progress: bringing Monero forward, and improve it. What happens with tx_extra starts to affect that. We really don't want to ossify already, Bitcoin-style, because nobody wants to compromise.

## LocalMonero | 2023-02-15T14:23:06+00:00
>  let us talk a bit about possible ideas how to improve our decision process.

Core team decides. Core team isn't dumb and core team's decisions are based on their own expertise and reading the room. This process has worked. tx_extra seems to be the only exception where core team didn't have the will to make a decision, either through their own uncertainty over the question or over the inability to determine the room.

## rbrunner7 | 2023-02-15T14:55:04+00:00
> Core team decides.

Really? You don't mean in the sense of "If deadlock, then Core Team decides", right? You mean that the core team regularly makes **technical** decisions, as a team?

If yes, I don't remember this happening.

I remember @ArticMine basically deciding things about fees and dynamic block size, but not because he is a Core Team member, but because is our main technical authority regarding this.

## luigi1111 | 2023-02-15T15:31:08+00:00
Core doesn't make regular technical decisions as a team, at least not since the early days.

## LocalMonero | 2023-02-15T15:58:21+00:00
Didn't mean as a team.

## paulshapiro | 2023-02-15T16:48:13+00:00
Members of the core team have made plenty of technical decisions, and also been quite vocal about their opinions online as well. That holds sway. 

This is what MRL was supposed to be for but as a project I at least can admit we dropped the ball in making their presence sustainable. 

## UkoeHB | 2023-02-15T18:26:21+00:00
`[02-15-2023 17:03:38] <UkoeHB> whoops meeting time`
`[02-15-2023 17:03:52] <Rucknium[m]> UkoeHB: Ready to start meeting?`
`[02-15-2023 17:03:57] <UkoeHB> https://github.com/monero-project/meta/issues/797`
`[02-15-2023 17:03:57] <UkoeHB> 1. greetings`
`[02-15-2023 17:03:57] <UkoeHB> hello`
`[02-15-2023 17:04:04] <tevador> Hi.`
`[02-15-2023 17:04:08] <rbrunner> Hello`
`[02-15-2023 17:04:12] <one-horse-wagon[> Hello!`
`[02-15-2023 17:04:14] <kayabanerve[m]> Hello`
`[02-15-2023 17:04:14] <dangerousfreedom> Hello`
`[02-15-2023 17:04:17] <Rucknium[m]> Hi`
`[02-15-2023 17:04:22] <isthmus> Heya`
`[02-15-2023 17:05:01] <AlexanderSchmidt> Hallo`
`[02-15-2023 17:05:04] <Alex|LocalMonero> Hi`
`[02-15-2023 17:05:31] <UkoeHB> 2. updates, what's everyone working on?`
`[02-15-2023 17:05:35] <ArticMine[m]> Hi`
`[02-15-2023 17:05:51] <Stnby[m]> Heya`
`[02-15-2023 17:05:56] <isthmus> I’m chatting with Rucknium about providing support on OSPEAD computational work. The plan is to have one of my engineers convert the R prototypes to a compiled language, and then we’ll run the faster code for tens of thousands of CPU hours on GL’s scientific computing infra. The benefit of being able to process more rings will be better precision in the final OSPEAD parameterization.`
`[02-15-2023 17:05:56] <isthmus> The plan is that we’ll first build a little demo for Rucknium pro bono, showcasing the relevant engineering skills, and then move the CCS forward for the main project. Even though we’re still in the pre-CCS demo phase, I went ahead and uploaded a draft of the CCS proposal (#375) in case anybody is curious wants to take a peek at the details in the interim.`
`[02-15-2023 17:06:39] <jeffro256[m]> hello!`
`[02-15-2023 17:06:53] <Rucknium[m]> me: Learning how to connect C++ and R. I left a comment on isthmus's proposal: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/375`
`[02-15-2023 17:07:07] <vtnerd> jo`
`[02-15-2023 17:07:09] <vtnerd> hi`
`[02-15-2023 17:07:23] <plowsof11> hi`
`[02-15-2023 17:08:19] <Monegro> Is this the tx_extra discussion? I just came to watch. `
`[02-15-2023 17:08:35] <vtnerd> Ive been working on webhook support for lws, which is not really mrl related. unfortunately no recent progress on bp++, but I pushed back the 2nd feature set for webhooks to get some bp++ time in the upcoming weeks`
`[02-15-2023 17:09:00] <vtnerd> someone just needed lws stuff with a very high priority (or so they claim)`
`[02-15-2023 17:09:02] <rbrunner> Monegro: Yes, in a bit`
`[02-15-2023 17:09:12] <UkoeHB> me: I've been building an experimental tasking system which may or may not be useful in the seraphis wallet migration project. My threadpool appears to have comparable performance to the current one tools::threadpool, but lets you 'sleep' on tasks inside the pool which increases throughput drastically if you have tasks that would normally hang to sleep for a long time.`
`[02-15-2023 17:09:21] <one-horse-wagon[> Monegro: yes`
`[02-15-2023 17:09:34] <vtnerd> ukoehb is it published anywhere? I can give immediate feedback`
`[02-15-2023 17:09:45] <vtnerd> it will take my mind off going through the math you want me to go through :/`
`[02-15-2023 17:09:59] <vtnerd> I will comment on the read/lock thing  you did, a couple of trivial comments`
`[02-15-2023 17:10:03] <endogenic> UkoeHB: does it make sense to focus on that at this second? i bet parallelization could be added later`
`[02-15-2023 17:10:05] <UkoeHB> vtnerd: https://github.com/UkoeHB/monero/tree/seraphis_lib/src/async`
`[02-15-2023 17:10:16] <UkoeHB> endogenic: don't know, don't care!`
`[02-15-2023 17:10:22] <endogenic> wonderful`
`[02-15-2023 17:10:28] <endogenic> forget asking me for feedback then`
`[02-15-2023 17:11:25] <UkoeHB> vtnerd: I haven't been able to figure out how to do very small tasks quickly unfortunately.. might be unavoidable overhead of the extra things I have in there.`
`[02-15-2023 17:11:46] <vtnerd> yeah the allocations and locking usually kill that`
`[02-15-2023 17:12:11] <UkoeHB> 3. discussion, today we are supposed to talk about possible consensus rule changes around the tx_extra`
`[02-15-2023 17:12:13] <vtnerd> its typically better to have largish tasks for a system like that`
`[02-15-2023 17:13:30] <rbrunner> People may have seen my idea to talk about alternative ways to get consensus about such consensus rule changes, see the meeting issue`
`[02-15-2023 17:13:51] <rbrunner> At least as an additional thing to discuss`
`[02-15-2023 17:14:01] <UkoeHB> re: tx_extra there has been considerable debate in these places https://github.com/monero-project/monero/issues/6668 https://github.com/monero-project/meta/issues/797`
`[02-15-2023 17:14:30] <Alex|LocalMonero> rbrunner: Can we do this next time please? There's no point in this last minute change`
`[02-15-2023 17:15:03] <Rucknium[m]> I read all 150 comments on tevador's GitHub issue. I don't have a strong opinion on the matter due to the tradeoffs between different options. If there is a need/desire for a statistical check of the randomness (encrypted status) of the tx_extra field, I can help search for an appropriate statistical test.`
`[02-15-2023 17:15:11] <rbrunner> If there is some progress today, we can easily move that weeks. If not I see it getting important.`
`[02-15-2023 17:15:13] <kayabanerve[m]> My summary is: Steganography has multiple performance impacts and is a uniformity trade off, not solution. I personally appreciate TX extra. I'd advocate a 255 byte limit, and wouldn't mind a statistical check/ASCII ban.`
`[02-15-2023 17:15:13] <kayabanerve[m]> There's a lot of further discussions possible, and I'm unsure, per rbrunner, we'll actually reach consensus. I'd advocate either we take steps to limit it, which have minimal disagreement, we vote, or we drop the discussion entirely for consensus process discussions.`
`[02-15-2023 17:15:31] <tevador> The current situation is that we have tx_extra as an arbitrary size field for arbitrary data. Does anyone think the current state is ideal?`
`[02-15-2023 17:15:38] <vtnerd> no`
`[02-15-2023 17:15:43] <jeffro256[m]> no`
`[02-15-2023 17:15:52] <rbrunner> No`
`[02-15-2023 17:15:56] <jtgrassie> no`
`[02-15-2023 17:15:59] <tobtoht[m]1> no`
`[02-15-2023 17:16:00] <kayabanerve[m]> Nope`
`[02-15-2023 17:16:00] <Alex|LocalMonero> no`
`[02-15-2023 17:16:05] <Guest26> no`
`[02-15-2023 17:16:05] <vtnerd> and projects publicly listing their decryption keys for new tx_extra, is also not ideal`
`[02-15-2023 17:16:17] <tevador> So we can have at least some consensus.`
`[02-15-2023 17:16:18] <Alex|LocalMonero> so steg`
`[02-15-2023 17:16:35] <vtnerd> if the steg is public, its the same problem as public decryption keys`
`[02-15-2023 17:16:36] <UkoeHB> I have a hard time estimating what is ideal and not logically impossible`
`[02-15-2023 17:16:39] <kayabanerve[m]> I see that the same as view keys @vtnerd`
`[02-15-2023 17:16:49] <vtnerd> steg has to remain private to work, thats the difference between it and cryptography`
`[02-15-2023 17:17:01] <UkoeHB> but I'll accept 'could be improved'`
`[02-15-2023 17:17:13] <vtnerd> monero doesn't advocate that large projects publish their view keys publicly`
`[02-15-2023 17:17:28] <kayabanerve[m]> Any public output set is a privacy issue so long as we have subset membership proofs.`
`[02-15-2023 17:17:42] <vtnerd> at least afaik, like many people are on edge about MyMonero and privacy, and don't want it worsened, etc`
`[02-15-2023 17:18:05] <kayabanerve[m]> And her we do explicitly state view keys can be shared for verifiability.`
`[02-15-2023 17:18:10] <vtnerd> which is irrelevant to what Im saying`
`[02-15-2023 17:18:19] <vtnerd> thats just whataboutism on some next level crypto talk`
`[02-15-2023 17:18:24] <kayabanerve[m]> *and yet`
`[02-15-2023 17:18:40] <Alex|LocalMonero> If arbitrary data is to be stored it should be stored in a way that makes it look just like any other tx to the greatest possible extent`
`[02-15-2023 17:19:11] <endogenic> there are researchers working on this stuff right now`
`[02-15-2023 17:19:16] <endogenic> why doesnt this room care?`
`[02-15-2023 17:19:17] <vtnerd> the problem is this DEX (thats whats tx_extra) cannot market itself as a privacy solution, only a decentralized exchange`
`[02-15-2023 17:19:21] <endogenic> they're the experts`
`[02-15-2023 17:19:40] <kayabanerve[m]> Somewhat? I'm more trying to comment this isn't an issue unique to extra and I don't care to premise this extra discussion on it.`
`[02-15-2023 17:19:55] <vtnerd> provided the community understands this, its probably no worse than Kraken having a bunch of view_keys and info`
`[02-15-2023 17:20:07] <ArticMine[m]> Can we find a compromise on TX extra?`
`[02-15-2023 17:20:23] <vtnerd> just include it with a fixed size, thats probably the most reasonable thing to do at this stage`
`[02-15-2023 17:20:29] <kayabanerve[m]> There's an active PR to make it ~2kb`
`[02-15-2023 17:20:33] <Alex|LocalMonero> ArticMine: why is a compromise with arbitrary data injeciton desirable?`
`[02-15-2023 17:20:38] <kayabanerve[m]> I'd advocate 255b.`
`[02-15-2023 17:20:47] <jtgrassie> I thought that's what #8733 is, a compromise`
`[02-15-2023 17:20:49] <vtnerd> tevador?`
`[02-15-2023 17:20:50] <rbrunner> If we can achieve a rough consensus that compromising is within reach.`
`[02-15-2023 17:20:56] <isthmus> I really like the Zcash approach - fixed size encrypted memo on *every* transaction so that no transaction with a memo sticks out. `
`[02-15-2023 17:21:01] <rbrunner> If people are not ready to compromise ...`
`[02-15-2023 17:21:08] <ArticMine[m]> Along the lines of a limited number of fixed sizes `
`[02-15-2023 17:21:36] <tevador> Some options are: 1. Limit the size. 2. Make it fixed-size. 3. Make it optional with a fixed size.`
`[02-15-2023 17:21:43] <Alex|LocalMonero> isthmus: this means that 99% is paying additional 15% tx fees (not to mention space and bandwidth) for the benefit of the application layer`
`[02-15-2023 17:22:05] <isthmus> Correct, it's for uniformity and everybody's privacy`
`[02-15-2023 17:22:22] <Alex|LocalMonero> Yeah, or tx_extra can just be dropped for even more uniformity and privacy`
`[02-15-2023 17:22:22] <isthmus> No free lunch`
`[02-15-2023 17:22:23] <vtnerd> Alex|LocalMonero : yup :/ and I agree with tevadors condensed description, thats really what the debate is over`
`[02-15-2023 17:22:27] <ArticMine[m]> And pusedo enforcement of randomness via node relay `
`[02-15-2023 17:22:33] <tevador> #8733 is a stop gap measure before Seraphis can change tx_extra.`
`[02-15-2023 17:23:01] <Alex|LocalMonero> vtnerd: why isn't removing it an option?`
`[02-15-2023 17:23:05] <blankpage[m]> Mandatory blob of fixed size would have very low computational/verification cost, yes? Downside would be purely storage/bandwidth`
`[02-15-2023 17:23:15] <jtgrassie> moo had a patch a while ago that did that (fixed size extra) if IRC`
`[02-15-2023 17:23:19] <Alex|LocalMonero> blankpage: fees`
`[02-15-2023 17:23:45] <rbrunner> And a terrible hit rate, very few people wanting to store something there, and doing so`
`[02-15-2023 17:23:46] <ArticMine[m]> One of the size choices can be zero `
`[02-15-2023 17:24:06] <kayabanerve[m]> As  distinct discussion, if tx extra is kept, I believe it should be prunable and prunes by pruned nodes`
`[02-15-2023 17:24:06] <Rucknium[m]> Just reduce minrelayfee by 15% and the fee issue disappears`
`[02-15-2023 17:24:07] <vtnerd> your right, there's no reason why we cannot force steg approaches, even though they are suboptimal`
`[02-15-2023 17:24:37] <Monegro> Would forcing steg reduce the frequency of usage?`
`[02-15-2023 17:24:38] <jtgrassie> #8733 should be a nobrainer whilst other things are worked out`
`[02-15-2023 17:24:42] <Alex|LocalMonero> vtnerd: they are suboptimal for arbitrary data, which makes monero more optimal for tx data`
`[02-15-2023 17:24:44] <kayabanerve[m]> *As a, pruned by`
`[02-15-2023 17:24:50] <vtnerd> Monegro: probably, as its much harder to do`
`[02-15-2023 17:25:03] <Alex|LocalMonero> Monegro: A higher cost of arbitrary data injection disincentivizes its usage`
`[02-15-2023 17:25:05] <ArticMine[m]> Rucknium[m]: Not that simple `
`[02-15-2023 17:25:09] <kayabanerve[m]> Alex | LocalMonero | AgoraDesk: Not definitively`
`[02-15-2023 17:25:14] <UkoeHB> From a protocol design standpoint, our goal is privacy by default (i.e. opt-out privacy). It is impossible to mandate privacy, so any proposals with that goal should be discarded. What are the default-usage privacy defects of tx extra? Lack of uniformity among tx extra users (non-users are uniform in that they all have 'empty' fields [excluding ephemeral pubkeys]). Assuming we want to keep a tx extra in some form, we `
`[02-15-2023 17:25:14] <UkoeHB> can A) improve uniformity globally by mandating all txs have identical-looking tx extras by default (fixed-size and encrypted by default), B) improve scoped uniformity by mandating all txs have EITHER no tx or a fixed-size tx extra (encrypted by default). (A) is better than (B) in terms of uniformity, and (B) is better than (A) in terms of scalability (a fixed-size tx extra would be a big chunk of txs, maybe 25%). `
`[02-15-2023 17:25:14] <UkoeHB> Option (C) is deleting the tx extra if we decide it isn't a feature needed by default (steganography could be implemented as a non-default alternative).`
`[02-15-2023 17:25:18] <vtnerd> the problem is that theoretically monero could support _some_ application layer stuff without being a privacy sieve`
`[02-15-2023 17:25:23] <kayabanerve[m]> Re: optimality`
`[02-15-2023 17:25:39] <vtnerd> I believe thats why tevador tentatively agreed to keeping tx_extra around - theres a way to use the memo field "properly"`
`[02-15-2023 17:25:44] <endogenic> does no one care that actual qualified researchers specialize in this`
`[02-15-2023 17:25:49] <endogenic> and that we have blinders on`
`[02-15-2023 17:25:56] <endogenic> we could invite them into the room as a community`
`[02-15-2023 17:26:02] <endogenic> but we choose to wander in the dark`
`[02-15-2023 17:26:08] <vtnerd> I think we have a handle on this`
`[02-15-2023 17:26:14] <endogenic> no you dont`
`[02-15-2023 17:26:27] <endogenic> you cant predict the future of tech or you'd be those researchers`
`[02-15-2023 17:26:40] <endogenic> besides`
`[02-15-2023 17:26:40] <Rucknium[m]> endogenic: Sure. Invite them.`
`[02-15-2023 17:26:55] <endogenic> what kind of nonsense is it to not decide we need people who actually specialize in this`
`[02-15-2023 17:26:57] <vtnerd> and researchers are never wrong? please, dont waste our time`
`[02-15-2023 17:27:03] <endogenic> what motives do you have exactly?`
`[02-15-2023 17:27:04] <Alex|LocalMonero> vtnerd: "proper" use of the arbitrary data field is an oxymoron if the design goal of monero is to be the best possible digital cash`
`[02-15-2023 17:27:09] <nikg83[m]> endogenic: The room is open, feel free to invite “them”`
`[02-15-2023 17:27:10] <endogenic> vtnerd what a ridiculous argument`
`[02-15-2023 17:27:13] <jeffro256[m]> > Can we find a compromise on TX extra?`
`[02-15-2023 17:27:13] <jeffro256[m]> I'll summarize the idea I had for tx_extra. I discussed it with kayabaNerve, but didn't make it public. Disclaimer: kayabaNerve doesn't necessarily support this idea. Make tx_extra a public ed25519 point + signature (proving knowledge of private scalar corresponsding to aforementioned point) which reduces the amount of arbitrary data possible to encode into a transaction limited to just a few brute-forced bits. However, any`
`[02-15-2023 17:27:13] <jeffro256[m]> arbitrary data could be privately verified to be "attached" to this transaction by hashing to the point provided in the transaction. This tx_extra is small and fixed size but allows for off-chain verification of arbitrary data. ALSO, for data availability, "archival" nodes would relay and save corresponding blobs which match the tx_extra of certain transactions. Full nodes would also relay and save for up a week (this period`
`[02-15-2023 17:27:13] <jeffro256[m]> could be determined later). This solves the data availability problem, the DEX problem, and increases transaction uniformity. It does have tradeoffs, but I like this solution.`
`[02-15-2023 17:27:14] <Rucknium[m]> I have invited plenty of researchers here. Some have showed up.`
`[02-15-2023 17:27:19] <endogenic> i have invited them`
`[02-15-2023 17:27:25] <endogenic> they often feel disregarded`
`[02-15-2023 17:27:26] <endogenic> surprise`
`[02-15-2023 17:27:30] <endogenic> that's why i said as a project`
`[02-15-2023 17:27:33] <vtnerd> if it were fixed size, and always encrypted by all parties, its no worse than ring signatures`
`[02-15-2023 17:27:38] <endogenic> none of you seem to value their free contributions`
`[02-15-2023 17:27:45] <isthmus> +1 vtnerd `
`[02-15-2023 17:28:04] <vtnerd> the more options _allowed_, the more problematic it becomes`
`[02-15-2023 17:28:12] <jtgrassie> +1`
`[02-15-2023 17:28:18] <ArticMine[m]> Interesting `
`[02-15-2023 17:28:25] <Alex|LocalMonero> vtnerd: it is worse because its an extra added on top that everyone has to pay for whether they use it or not`
`[02-15-2023 17:28:28] <vtnerd> using steg approaches works, but its funky`
`[02-15-2023 17:28:30] <UkoeHB> endogenic: if you have something to say, be specific`
`[02-15-2023 17:28:35] <endogenic> i have`
`[02-15-2023 17:28:38] <endogenic> stop strawmanning`
`[02-15-2023 17:28:45] <kayabanerve[m]> jeffro256's idea has a pointless component, otherwise I'd have a similar option`
`[02-15-2023 17:28:47] <Rucknium[m]> endogenic: Give us some names`
`[02-15-2023 17:28:49] <vtnerd> Im not talking about cost, Im talking about privacy, which is why isthmus gave me the +1`
`[02-15-2023 17:28:53] <endogenic> koe has names`
`[02-15-2023 17:29:02] <endogenic> and there are more of them too`
`[02-15-2023 17:29:05] <ArticMine[m]> I suggested one of the options being zero `
`[02-15-2023 17:29:10] <endogenic> dont think i'm talking out of my ass`
`[02-15-2023 17:29:18] <moneromooo> endogenic: please be useful or shut the fuck up.`
`[02-15-2023 17:29:19] <endogenic> i'm not that flush with free time`
`[02-15-2023 17:29:22] <endogenic> i am`
`[02-15-2023 17:29:23] <vtnerd> from a stat perspective, a symmetricall encrypted field is not going to be worse than the ECDH madness`
`[02-15-2023 17:29:26] <endogenic> try to listen`
`[02-15-2023 17:29:32] <kayabanerve[m]> vtnerd: Fine with me, if 256b (> than a jamtis addr)`
`[02-15-2023 17:29:40] <moneromooo> Link us to whatever work is there, fr instance. Dont' say "why don't we listen to them".`
`[02-15-2023 17:30:07] <kayabanerve[m]> It's a bit bloated, but it solves the privacy, usability, and soft fork discussions`
`[02-15-2023 17:30:08] <endogenic> i habe`
`[02-15-2023 17:30:09] <endogenic> habe`
`[02-15-2023 17:30:10] <endogenic> have`
`[02-15-2023 17:30:13] <endogenic> it has been ignored`
`[02-15-2023 17:30:25] <ArticMine[m]> I believe a compromise is possible here`
`[02-15-2023 17:30:27] <endogenic> and it's notable there are individuals with conflicts of interest here`
`[02-15-2023 17:30:27] <moneromooo> Sorry, I missed it then. I'll re-read.`
`[02-15-2023 17:30:32] <kayabanerve[m]> We can also make TX extra prunable to help there`
`[02-15-2023 17:31:18] <kayabanerve[m]> If referring to me, I don't mind disclosing, yet I'll comment I am minimally effected by this discussion.`
`[02-15-2023 17:31:22] <Alex|LocalMonero> 1. If it's fixed length and encrypted then everyone is overpaying and overusing resources for the benefit of the few (and the junk outputs are still exploitable)`
`[02-15-2023 17:31:22] <Alex|LocalMonero> 2. if it's optional then fungibility is harmed as we have what are essentially subchains`
`[02-15-2023 17:31:22] <Alex|LocalMonero> 3. if arbitrary data injectors are forced to make their data look as txs then they effectively are txs and for all intents and purposes are a legitimate use of the Monero chain`
`[02-15-2023 17:31:39] <blankpage[m]> I read the discussion of jeffro256s idea recently and I think it is very interesting. I do wonder if there are use cases which are only serves by the arbitrary data being on chain though, rather than a hash representation of what is happening in a mempool of blobs`
`[02-15-2023 17:31:40] <kayabanerve[m]> But sure, I work on a real world use case of TX extra for arb data.`
`[02-15-2023 17:31:55] <moneromooo> I re-read, no link or similar searchable info.`
`[02-15-2023 17:32:27] <ArticMine[m]> We can have a limited number of anonymity sets like we do with tx outputs`
`[02-15-2023 17:32:29] <tevador> Alex|LocalMonero: 2. is not much worse than 3. because transactions with more than 2 outputs already stand out.`
`[02-15-2023 17:32:36] <UkoeHB> jeffro256[m]: my take is your proposal implies quite a large engineering effort (maybe more than is justified by a field that's barely used right now). Uniformity isn't really improved if you can just connect archived data to txs (there is no way to upload a tx and archive data at the same time without linking them).`
`[02-15-2023 17:32:47] <vtnerd> Alex|LocalMonero the problem is that the steg approach are almost certainly less optimal than the encrypted approach, thus why we keep going in circles`
`[02-15-2023 17:33:06] <Alex|LocalMonero> tevador: txs with more than 2 outputs standing out sounds like a separate protocol issue to be fixed`
`[02-15-2023 17:33:20] <Alex|LocalMonero> vtnerd: less optimal for arbitrary data, so who cares?`
`[02-15-2023 17:33:35] <kayabanerve[m]> I have a question`
`[02-15-2023 17:33:39] <Alex|LocalMonero> arbitrary data isn't monero's design goal`
`[02-15-2023 17:33:40] <endogenic> moneromooo: it has been over the past year`
`[02-15-2023 17:33:42] <tevador> Alex|LocalMonero: and 2. is much better for scalability than 3.`
`[02-15-2023 17:33:47] <endogenic> i will dm you`
`[02-15-2023 17:33:49] <kayabanerve[m]> Who here actively wants to remove, not fix, TX extra?`
`[02-15-2023 17:34:08] <moneromooo> I am not the one that'll do the work anymore. Link it here please.`
`[02-15-2023 17:34:40] <endogenic> the record can be searched. time for you guys to stop trampling on people`
`[02-15-2023 17:34:41] <kayabanerve[m]> If we can limit this discussion to improvements, which we can discuss incrementally, that may be more effective as right now we're exhibiting the concerns stated before this started`
`[02-15-2023 17:35:07] <Lyza> I also interested in this research or whatever, I don't see the point in complaining without bothering to share what you're trying to talk about`
`[02-15-2023 17:35:07] <rbrunner> I support that question. Full removers, please wink.`
`[02-15-2023 17:35:12] <Alex|LocalMonero> tevador: scalability of arbitrary data? Again, who cares? We should be optimizing he scalability of tx data. The 0.01% usage of application layer data being unoptimized is not a concern`
`[02-15-2023 17:35:21] <john_r365[m]> +1 remove - it sounds like arbitrary data can be added in other ways`
`[02-15-2023 17:35:23] <Lyza> some people might know what you're talking about <endogenic> but I would wager most of us do not`
`[02-15-2023 17:35:25] <ArticMine[m]> ... but if people insist on uniformity adding 128 bytes to each tx is less than 2 months of Neilsen's law `
`[02-15-2023 17:35:30] <Alex|LocalMonero> +1 remove`
`[02-15-2023 17:35:38] <rbrunner> Because getting full removal out of the way, per way of compromise, would be progress`
`[02-15-2023 17:35:53] <jeffro256[m]> > the record can be searched. time for you guys to stop trampling on people`
`[02-15-2023 17:35:53] <jeffro256[m]> For everybody's sake could you please link it if it's relevant? I want to know about formal research around this topic if it exists. It would be helpful to everyone who is not on here 24/7`
`[02-15-2023 17:36:22] <rbrunner> Two votes so far for full removal. Any more?`
`[02-15-2023 17:36:30] <one-horse-wagon[> +1 remove`
`[02-15-2023 17:36:31] <jtgrassie> remove`
`[02-15-2023 17:36:35] <hbs[m]> +1 remove`
`[02-15-2023 17:36:47] <Alex|LocalMonero> ArticMine: nielsen's law sure but what about fees?`
`[02-15-2023 17:36:52] <endogenic> Lyza: i have been laboring for years to bring that research here`
`[02-15-2023 17:37:08] <endogenic> now when i've been treated like i'm the asshole i have to forget all that?`
`[02-15-2023 17:37:13] <ArticMine[m]> The impact on fess is minimal `
`[02-15-2023 17:37:14] <blankpage[m]> How about hard-limiting tx_extra as a immediate action, and then jeffro256's idea could be further thought through to see if it covers all use cases? `
`[02-15-2023 17:37:22] <Lyza> smh ok don't share it then but if you're not trying to be helpful waht are you doing here`
`[02-15-2023 17:37:30] <rbrunner> Hmm, with 5 removal votes compromise will probably be difficult ...`
`[02-15-2023 17:37:32] <UkoeHB> As meeting leader, I'm going to slow this down (getting a little too chaotic). Let's get a read on everyone's stance. I will list some options, then everyone should reply with the number they like best, and a small comment justifying your position.`
`[02-15-2023 17:37:32] <UkoeHB> 1. get rid of tx extra and be done with it`
`[02-15-2023 17:37:32] <UkoeHB> 2. mandate maximum tx extra size (e.g. anything in 0 - 1000 bytes)`
`[02-15-2023 17:37:32] <UkoeHB> 3. mandate optional fixed-length tx extra size + encrypt by default`
`[02-15-2023 17:37:32] <UkoeHB> 4. mandate fixed-length tx extra for all txs + encrypt by default`
`[02-15-2023 17:37:33] <UkoeHB> 5. other (specify)`
`[02-15-2023 17:37:44] <jeffro256[m]> I would be okay with a fixed-length mandatory encrypted field `
`[02-15-2023 17:37:45] <Alex|LocalMonero> 1`
`[02-15-2023 17:37:47] <tevador> I personally don't mind removal (that was my original proposal), but I'm open for compromises (since pretty much anything is better than what we have now).`
`[02-15-2023 17:37:49] <moneromooo> Some of the latest work of Moreno Sanchez, he said in private. In case someone wants to search/read.`
`[02-15-2023 17:37:54] <isthmus> All NRL research points towards tx_extra being Monero's Achilles heel as of 2023. While the most straightforward solution would be to remove it, I also understand that there are valuable ecosystem components coupled to this, so I am also very open to discussing improvements. Anything better than currently.`
`[02-15-2023 17:37:55] <ArticMine[m]> This is like 5% of tx size`
`[02-15-2023 17:37:59] <jtgrassie> the case for keeping seems to be only for  unknown future use cases`
`[02-15-2023 17:38:01] <jeffro256[m]> I'm also fine with removal`
`[02-15-2023 17:38:05] <Lyza> thx moo`
`[02-15-2023 17:38:07] <UkoeHB> please no more comments other than replying to me for 4 minutes`
`[02-15-2023 17:38:20] <UkoeHB> I need to moderate this`
`[02-15-2023 17:38:40] <blankpage[m]> 4`
`[02-15-2023 17:38:44] <Alex|LocalMonero> UkoeHB: 1`
`[02-15-2023 17:38:52] <kayabanerve[m]> blankpage: There's a PR for a hard limit`
`[02-15-2023 17:38:55] <dangerousfreedom> 1`
`[02-15-2023 17:39:01] <moneromooo> Kinda conflicted between 1 and 3.`
`[02-15-2023 17:39:07] <hbs[m]> 1`
`[02-15-2023 17:39:08] <kayabanerve[m]> 2,3,4`
`[02-15-2023 17:39:15] <isthmus> 1, 4, open to others' 5`
`[02-15-2023 17:39:20] <fredsmith> 1 , possibly 4`
`[02-15-2023 17:39:21] <vtnerd> jtgrassie: fair point, and we could always bring it back in a hard-fork`
`[02-15-2023 17:39:29] <rbrunner> 2 because length restriction, plus the encryption from 3`
`[02-15-2023 17:39:30] <jtgrassie> vtnerd: exactly`
`[02-15-2023 17:39:31] <tevador> 1 or 3 are probably the best.`
`[02-15-2023 17:39:38] <jeffro256[m]> UkoeHUB: In order of perference, best to worst: 4, 1, 3, 2`
`[02-15-2023 17:39:38] <ArticMine[m]> 3`
`[02-15-2023 17:39:39] <andytoshi>  /iwn 21`
`[02-15-2023 17:39:41] <andytoshi> sorry`
`[02-15-2023 17:40:01] <one-horse-wagon[> 1. remove.  Better for uniformity of transmissions.`
`[02-15-2023 17:40:12] <tobtoht[m]1> 1 or 3`
`[02-15-2023 17:40:17] <john_r365[m]> 1. Fallback 4`
`[02-15-2023 17:40:20] <UkoeHB> 3`
`[02-15-2023 17:40:46] <jtgrassie> hence #1 is the ideal and #2 at least nudges in the right directon (quick change)`
`[02-15-2023 17:40:53] <Rucknium[m]> Like I said, I don't have a strong opinion because of the complicated tradeoffs. If I have to choose a single option, I would choose (1).`
`[02-15-2023 17:41:43] <unwantedfondue[m> 2`
`[02-15-2023 17:42:28] <endogenic> Lyza: this is the help the project needs. the people here repeatedly throw away connections i've made. i'm not going to name names`
`[02-15-2023 17:43:09] <Alex|LocalMonero> 4 minutes are up, shall we tally?`
`[02-15-2023 17:43:33] <moneromooo> Oh. 1 would also prevent merge mining fwiw. But I'm biased of course.`
`[02-15-2023 17:43:58] <UkoeHB> 1 [alex, jeffro, dangerous, moo, hbs, isthmus, fred, tevador, tobtogh, john, jtgrassie], 2 [kaya, rene, jtgrassie, uwanted], 3 [moo, kaya, tevador, artic, koe, tobtoht], 4 [jeffro, blank, kaya, isthmus, fred, john], 5 [isthmus]`
`[02-15-2023 17:43:58] <tevador> We have to keep tx_extra for coinbase in any case (at least a fixed size one).`
`[02-15-2023 17:44:31] <isthmus> Sorry, I forgot to include a comment explaining my votes: I said 1 & 4 because they maintain transaction uniformity (central to user safety) and preserve a single anonymity pool. I am open to others’ suggestions for 5 if they maintain transaction uniformity.`
`[02-15-2023 17:44:47] <kayabanerve[m]> It sounds like due to fragmentation among 2,3,4, 1 is the most popular option there`
`[02-15-2023 17:44:51] <fredsmith> +1 isthmus`
`[02-15-2023 17:44:57] <kayabanerve[m]> tevador: For merge mining or yet something else?`
`[02-15-2023 17:45:14] <tevador> extra nonce`
`[02-15-2023 17:45:21] <one-horse-wagon[> UkoeHB: You didn't count my vote for 1.`
`[02-15-2023 17:45:28] <jtgrassie> kayabanerve[m]: the field is used for additional pub keys`
`[02-15-2023 17:45:31] <UkoeHB> sorry I may have missed a couple`
`[02-15-2023 17:45:31] <kayabanerve[m]> TIL That's how that works`
`[02-15-2023 17:45:47] <Rucknium[m]> kayabanerve: If we had ranked-choice "voting", the vote-splitting between similar options would be less of an issue`
`[02-15-2023 17:45:51] <ArticMine[m]> Yes but a binary vote keep or not would be helpful `
`[02-15-2023 17:45:52] <UkoeHB> 1 [alex, jeffro, dangerous, moo, hbs, isthmus, fred, tevador, tobtogh, john, jtgrassie, onehorse, rucknium], 2 [kaya, rene, jtgrassie, uwanted], 3 [moo, kaya, tevador, artic, koe, tobtoht], 4 [jeffro, blank, kaya, isthmus, fred, john], 5 [isthmus]`
`[02-15-2023 17:46:02] <blankpage[m]> Democracy is irrelevant here IMO. No one has technical objections to limiting the size so let's just do that. Then if the ideas like jeffro256's turn out to be infeasible or not useful then we remove it completely in the future.`
`[02-15-2023 17:46:03] <moneromooo> kayabanerve[m]'s idea (link to TF above) ensures uniformity and allows arbitrary encrypted data. So I also like 5 :D`
`[02-15-2023 17:46:21] <jtgrassie> we have t keep it till the tx structure is changed, hence why #2 is a good stop-gap to #1`
`[02-15-2023 17:47:04] <tevador> The current PR #8733 is a soft-limit for tx_extra. It cannot be removed right now because it contains mandatory public keys.`
`[02-15-2023 17:47:06] <rbrunner> I think when Seraphis comes near we will have tons of things to discuss. I would love to decide this today.`
`[02-15-2023 17:47:13] <kayabanerve[m]> We already immediately have a PR to limit size. I believe this is discussing changes to make at time of seraphis.`
`[02-15-2023 17:47:19] <rbrunner> To get it out of the way, so to say.`
`[02-15-2023 17:47:52] <Alex|LocalMonero> Seems like removing it is the option the most people find acceptable. Not that this matters to the technical soundness of it.`
`[02-15-2023 17:48:01] <kayabanerve[m]> We can either:`
`[02-15-2023 17:48:01] <kayabanerve[m]> - Remove`
`[02-15-2023 17:48:01] <kayabanerve[m]> - Call for a ranked choice vote`
`[02-15-2023 17:48:01] <kayabanerve[m]> - say one IRC Nick != one vote`
`[02-15-2023 17:48:22] <kayabanerve[m]> Though as noted, coinbase will still need extra`
`[02-15-2023 17:48:23] <sech1> I said it before, and I say it again: voting is idiotic in a technical matter`
`[02-15-2023 17:48:39] <Alex|LocalMonero> @sech1 where do you stand?`
`[02-15-2023 17:48:42] <sech1> whatever path forward is taken, it must be justified`
`[02-15-2023 17:48:43] <kayabanerve[m]> ... That'd be option #3 :p`
`[02-15-2023 17:48:52] <sech1> I prefer option #1 eventually (after HF)`
`[02-15-2023 17:49:02] <sech1> all needed like tx pubkeys can be moved to separate fields`
`[02-15-2023 17:49:11] <Alex|LocalMonero> I thought this discussion was meant to mean removing it post seraphis?`
`[02-15-2023 17:49:24] <Alex|LocalMonero> Did people discuss removing it now?`
`[02-15-2023 17:49:34] <rbrunner> Why would that matter?`
`[02-15-2023 17:49:45] <Alex|LocalMonero> Time for people to swithc`
`[02-15-2023 17:49:54] <rbrunner> The "when" is a separate question`
`[02-15-2023 17:49:56] <sech1> I mean #1 after seraphis`
`[02-15-2023 17:50:01] <tevador> Seraphis already moves public keys from tx_extra, so it would be purely for arbitrary data then.`
`[02-15-2023 17:50:07] <Siren[m]> UkoeHB: I also vote 1, if my vote counts`
`[02-15-2023 17:50:07] <moneromooo> What would we do with payment ids ? Some poeple like it even with subaddresses available.`
`[02-15-2023 17:50:13] <sech1> before that, it can be size-limited and have higher fee per byte`
`[02-15-2023 17:50:25] <ArticMine[m]> Voting on keeping it or not should be separated from how to keep it`
`[02-15-2023 17:50:31] <isthmus> +1 artic`
`[02-15-2023 17:50:35] <Siren[m]> moneromooo: Deprecate it :))`
`[02-15-2023 17:50:38] <tevador> moneromooo: payment ids have been deprecated/replaced by encrypted address tags`
`[02-15-2023 17:50:43] <Monegro> Just to be clear a "no change" option is not what anyone wants, correct? Everyone thinks something should be done?`
`[02-15-2023 17:50:45] <jtgrassie> +1 ArticMine`
`[02-15-2023 17:51:15] <kayabanerve[m]> So, it sounds like the agreeable option is remove with Seraphis. The only way to threaten this is to call for a ranked choice vote or to call voting idiotic`
`[02-15-2023 17:51:15] <Alex|LocalMonero> Exactly, as moneromooo points out its very impractical to remove tx_extra prior to seraphis`
`[02-15-2023 17:51:15] <UkoeHB> I think 1 is a strong option. We can divide the options into two categories: A) remove, B) keep in some form. The reason for keeping it is 'all the things we don't know in advance and don't want to depend on a hardfork for'.`
`[02-15-2023 17:51:16] <rbrunner> Monegro: Looks like it, "doing nothing" only got "nos" earlier in the meeting`
`[02-15-2023 17:51:36] <Alex|LocalMonero> ArticMine: -1, there's no point in discussing how to keep it if we decide not to keep it`
`[02-15-2023 17:51:58] <moneromooo> I did not intend to weigh in on the timing fwiw.`
`[02-15-2023 17:51:59] <ArticMine[m]> Of course `
`[02-15-2023 17:52:08] <UkoeHB> From a protocol longevity standpoint, keeping it is better because it reduces the need/desire for future hardforks.`
`[02-15-2023 17:52:12] <rbrunner> At least A) or B) would give a clearer picture after the vote`
`[02-15-2023 17:52:12] <sech1> also, did anyone do a research on how tx_extra is used now?`
`[02-15-2023 17:52:26] <ArticMine[m]> We vote first on whether to keep it`
`[02-15-2023 17:52:27] <MajesticBank> yes wanted to ask do anyone use it for something`
`[02-15-2023 17:52:32] <Lyza> what are the chances rn of having another HF before Seraphis? tx_extra aside`
`[02-15-2023 17:52:40] <tevador> Yes: https://github.com/noncesense-research-lab/monero_tx_extra/blob/master/ascii_data.md`
`[02-15-2023 17:52:50] <Alex|LocalMonero> UkoeHB: soft forks have proved themselves to be a disaster for BTC, hard forks have proved themselves to be a blessing for XMR`
`[02-15-2023 17:52:56] <sech1> tevador 2020 != now`
`[02-15-2023 17:53:02] <ArticMine[m]> Then only if the decision is to keep them we work on the technical details `
`[02-15-2023 17:53:09] <MajesticBank> data might be encrypted`
`[02-15-2023 17:53:34] <tevador> now it's mostly bee videos (anecdotally)`
`[02-15-2023 17:53:59] <isthmus> This room was bridged to tx_extra for a few hours a while back`
`[02-15-2023 17:54:08] <kayabanerve[m]> *a Script for a bee video`
`[02-15-2023 17:54:12] <rbrunner> I am in the "keep" camp mostly for softforks as an emergency option. Not terribly important to me personally what people do with it otherwise`
`[02-15-2023 17:54:24] <MajesticBank> is there info how much data is in tx_fields in total on blockchain?`
`[02-15-2023 17:54:41] <fredsmith> i think the softfork for emergency option can be maintained with tx_extra in coinbase only`
`[02-15-2023 17:54:43] <Alex|LocalMonero> Softforks led to massive fragmentation and tribalization of the BTC network, which doesn't even rely on fungibiliy to work.`
`[02-15-2023 17:54:53] <Alex|LocalMonero> rbrunner:`
`[02-15-2023 17:54:58] <ArticMine[m]> Also we separate coinbase`
`[02-15-2023 17:55:09] <sech1> Does anyone know what's the max size for legit tx_extra usage now? Not counting tx pubkeys?`
`[02-15-2023 17:55:10] <jeffro256[m]> I am also not concerned with soft forks regarding tx_extra. There is good reason why Monero never soft forks: it's bad for uniformity. The community/dev team has always gone with the principle of fast deprecation for non conforming transactions, which is a good thing `
`[02-15-2023 17:55:25] <jtgrassie> size restriction (per #8733) is the ideal stop-gap. One can still do non-standard "experiments" using extra. It may also help in future discussions on whether to keep or kill it.`
`[02-15-2023 17:55:29] <Alex|LocalMonero> soft forks are incongruent with fungibility`
`[02-15-2023 17:55:32] <tevador> If coinbase tx_extra is kept, we can still have a soft fork.`
`[02-15-2023 17:55:34] <rbrunner> I am talking about *emergency* softforks for problems that can't wait for a hardfork.`
`[02-15-2023 17:55:35] <kayabanerve[m]> We could keep a 64b extra to hedge against wallet protocol updates? It'd be a minimal size`
`[02-15-2023 17:55:35] <isthmus> There have been some outliers (e.g. 1028 kB tx_extra for one of the txns mentioned above)`
`[02-15-2023 17:55:48] <isthmus> We have size data, though I don't have a summary handy`
`[02-15-2023 17:56:06] <isthmus> NRL uses len(tx_extra) as a go-to fingerprint for clustering transactions`
`[02-15-2023 17:56:15] <Lyza> asking again: if we do this before seraphis, would we be hardforking primarily for tx_extra, or what else might we be trying to do in a pre-seraphis HF?`
`[02-15-2023 17:56:30] <fredsmith> oh boy thats a can of worms`
`[02-15-2023 17:56:56] <blankpage[m]> Removing is easy and good for fungibility, so I change my vote to 1 unless there is a fully sketched out plan of how to keep it in a useful way similar to jethro's idea at a point X months before seraphis`
`[02-15-2023 17:57:30] <rbrunner> Do people want an A) or B) vote? To simplify, and getting a clearer picture?`
`[02-15-2023 17:57:35] <blankpage[m]> basically, it could be useful for unknown applications but unless someone goes the work then it is better to have it gone than as-is`
`[02-15-2023 17:57:47] <tevador> I don't think a hardfork is planned before Seraphis. I think we can survive with #8733 until Seraphis.`
`[02-15-2023 17:57:51] <ArticMine[m]> Yes `
`[02-15-2023 17:57:56] <jtgrassie> yes`
`[02-15-2023 17:57:58] <tobtoht[m]1> I'm for merging 8733 now. We have more time to work out what do with tx_extra in seraphis.`
`[02-15-2023 17:58:26] <UkoeHB> Alex|LocalMonero: hard forks work well for privacy and scalability upgrades, which is all they have been used for up to this point. The tx extra represents utility, so this debate is about A) all future utility changes/innovations that require on-chain data should be supported by hard fork (a change in hard fork policy), B) some future utility flexibility should be baked into the tx extra.`
`[02-15-2023 17:58:37] <Rucknium[m]> Lyza: Possibly ending user-determined output lock time. Improvements to the decoy selection algorithm can be implemented without worrying much about creating anonymity puddles with wallets using different algorithms. I think there are more.`
`[02-15-2023 17:59:00] <moneromooo> I'm going for a bit, so https://dblp.uni-trier.de/pid/128/4640.html has the list of Pedro Moreno Sanchez papers, not obvious which one it might be that suggests an extra solution, I wasn't told. But it's his "latest" work if someone wants to look.`
`[02-15-2023 17:59:04] <ArticMine[m]> Fee scaling updates`
`[02-15-2023 17:59:07] <jeffro256[m]> Before merging 8733, we need wallet-side error checking!! I can PR that today, but we need a mechanism for the wallet to know the tx_extra size limit before constructing and attempting to broadcast a non-conforming transaction`
`[02-15-2023 17:59:10] <Alex|LocalMonero> UkoeHB: the only utility monero should be concerned about is utility as a decentralized electronic and fungible currency`
`[02-15-2023 17:59:20] <tevador> tobtoht[m]1: it would be good to make a decision now because Seraphis is already (mostly) implemented.`
`[02-15-2023 17:59:50] <one-horse-wagon[> Are we going to vote again on "A" or "B" option?`
`[02-15-2023 17:59:52] <rbrunner> After almost 3 years we all *deserve* a decision`
`[02-15-2023 18:00:02] <sech1> 8733 could be a nice workaround until the actual tx_extra solution`
`[02-15-2023 18:00:14] <Alex|LocalMonero> I don't mind 8733 either.`
`[02-15-2023 18:00:23] * isthmus is 100% OK with relay rules as temporary measures, but notes that relay rules are not a good long-term replacement for consensus rules`
`[02-15-2023 18:00:29] <Lyza> +1 8733 seems like a fine stopgap`
`[02-15-2023 18:01:08] <Alex|LocalMonero> But I agree with rbrunner that this question needs to be solved for the sake of seraphis`
`[02-15-2023 18:01:15] <Alex|LocalMonero> Solved now ideally`
`[02-15-2023 18:01:26] <jeffro256[m]> jeffro256 agrees with isthmus but doesn't know how to talk in third person with the little blue text`
`[02-15-2023 18:01:28] <UkoeHB> one-horse-wagon[: I'd like to table further temperature checks until next meeting. This week I'd like people to ruminate on the A/B distinction specifically, and on the consequences of each one.`
`[02-15-2023 18:01:37] <isthmus> "/me <text>"`
`[02-15-2023 18:01:40] <UkoeHB> this has already been a long meeting`
`[02-15-2023 18:01:50] <tevador> If there are just two options keep/remove, I'd lean towards remove (keep only for coinbase).`
`[02-15-2023 18:02:13] <Lyza> I think my position is that if we don't have a solid use case for it now, something most of the community wants that only can be done with tx_extra, we ditch it. I do think killing the ability to merge mine with monero is worth considering, for sure`
`[02-15-2023 18:02:17] <UkoeHB> tevador: the options are remove or keep 'in some as-yet-undetermined form'`
`[02-15-2023 18:02:24] <Alex|LocalMonero> And by the way @ArcticMine even a 0.1% difference in fees is enough to justify competition in the global financial markets, so 5% is massive.`
`[02-15-2023 18:02:28] <Lyza> not sure if proposals for payments channels used tx_extra or not`
`[02-15-2023 18:02:49] <jeffro256[m]> Let's vote then! Ppurely between A) remove entirely or B) keep is some undetermined form`
`[02-15-2023 18:03:09] <rbrunner> Just want to say that fundamentalist approaches (and I see removal as that) rarely play out well.`
`[02-15-2023 18:03:16] <tevador> Lyza: merged mining would still be possible because coinbase would keep tx_extra (it has to).`
`[02-15-2023 18:03:24] <ypavtv97lx[m]> just remove that garbage and be over with it..... it's used by lazy devs that could do better without it.`
`[02-15-2023 18:03:25] <jeffro256[m]> I mean voting shouldn't decide it, but just to guage what smarter people than me have so say`
`[02-15-2023 18:03:26] <Alex|LocalMonero> rbrunner: was RandomX not a fundamentalist approach?`
`[02-15-2023 18:03:51] <Lyza> next meeting sounds okay if koe thnks so (gotcha tevador, ty)`
`[02-15-2023 18:04:12] <Alex|LocalMonero> I'm old enough to remember everyone decrying that we need to compromise with ASICs`
`[02-15-2023 18:04:15] <UkoeHB> to summarize:`
`[02-15-2023 18:04:15] <UkoeHB> A) [remove tx extra]: tx utility flexibility tied to hardfork (or steganography)`
`[02-15-2023 18:04:15] <UkoeHB> B) [keep tx extra in some optimized form]: uniformity and scaling trade-offs depending on the solution`
`[02-15-2023 18:04:23] <blankpage[m]> Binary referendums where one option is not clearly defined often end in unsatisfying ways`
`[02-15-2023 18:04:35] <UkoeHB> let's end the meeting here, it is past the hour so we should not do any voting`
`[02-15-2023 18:04:39] <UkoeHB> thanks everyone`
`[02-15-2023 18:04:55] <fredsmith> thank you UkoeHB`
`[02-15-2023 18:04:56] <isthmus> Thanks much @UkoeHB `
`[02-15-2023 18:04:59] <ArticMine[m]> Thanks `
`[02-15-2023 18:05:02] <Monegro> ++`
`[02-15-2023 18:05:03] <Alex|LocalMonero> thanks UkoeHB !`
`[02-15-2023 18:05:06] <tobtoht[m]1> thanks`
`[02-15-2023 18:05:06] <jeffro256[m]> Thanks y'all`
`[02-15-2023 18:05:08] <hbs[m]> thx`
`[02-15-2023 18:05:09] <rbrunner> I vote for thanking :)`
`[02-15-2023 18:05:12] <jeffro256[m]> Especially koe`
`[02-15-2023 18:05:16] <Lyza> +1 to giving thanks`
`[02-15-2023 18:05:18] <Rucknium[m]> Thank you :)`
`[02-15-2023 18:05:20] <one-horse-wagon[> Thanks.`
`[02-15-2023 18:05:27] <tevador> Thanks`
`[02-15-2023 18:05:36] <ofrnxmr[m]> Thanks Koe `
`[02-15-2023 18:05:48] <fredsmith> when tx_extra tshirts`
`[02-15-2023 18:05:53] <john_r365[m]> Thanks koe and all `
`[02-15-2023 18:05:56] <gonbatfire[m]> Regular user hopping here:`
`[02-15-2023 18:05:56] <gonbatfire[m]> Limiting the size of tx_extra may incentivize users to attach data some other X way`
`[02-15-2023 18:05:56] <gonbatfire[m]> - What would this X way look like? What effects would it have over the network?`
`[02-15-2023 18:05:59] <tevador> The note on A) is not entirely true, you can attach extra data in a soft fork by putting a merkle root into the coinbase tx_extra.`
`[02-15-2023 18:06:53] <UkoeHB> tevador: I think that's cheating lol`
`[02-15-2023 18:07:00] <UkoeHB> but interesting idea`
`[02-15-2023 18:08:23] <kayabanerve[m]> Thanks y'all`

# Action History
- Created by: Rucknium | 2023-02-12T19:33:35+00:00
- Closed at: 2023-02-20T19:33:55+00:00
