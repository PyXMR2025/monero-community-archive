---
title: Monero Research Lab Meeting - Wed 01 February 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/790
author: Rucknium
assignees: []
labels: []
created_at: '2023-02-01T13:27:45+00:00'
updated_at: '2023-02-08T15:16:40+00:00'
type: issue
status: closed
closed_at: '2023-02-08T15:16:40+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss [Jamtis address checksums](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#64-checksum).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#786

# Discussion History
## UkoeHB | 2023-02-01T17:50:23+00:00
`[02-01-2023 17:01:47] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/790`
`[02-01-2023 17:01:47] <UkoeHB> 1. greetings`
`[02-01-2023 17:01:47] <UkoeHB> hello`
`[02-01-2023 17:01:59] <UkoeHB> sorry got distracted by that ordinal nonsense`
`[02-01-2023 17:02:26] <rbrunner> Hello`
`[02-01-2023 17:02:32] <ArticMine[m]> Hi`
`[02-01-2023 17:02:32] <Rucknium[m]> Hi`
`[02-01-2023 17:02:42] <isthmus> Heya`
`[02-01-2023 17:02:55] <plowsof11> hi`
`[02-01-2023 17:02:55] <dangerousfreedom> Hello`
`[02-01-2023 17:03:47] <UkoeHB> 2. updates, what's everyone working on?`
`[02-01-2023 17:05:07] <Rucknium[m]> Doing some initial Monte Carlo simulations for OSPEAD. Checking computational bottlenecks and performance in estimating parameters.`
`[02-01-2023 17:05:07] <isthmus> Chatting with Rucknium about ways that my team at Geometry Labs can support OSPEAD parameterization. We have some extra bandwidth on the engineering team and plenty of computational resources to throw at it :)`
`[02-01-2023 17:05:07] <isthmus> Still in early stages of discussing Ruck’s dev wish list, haven’t formalized anything yet but planning to draft up a CCS in the next week or two to share here for feedback.`
`[02-01-2023 17:09:09] <UkoeHB> me: doing a lot of thinking about how to architect the core wallet engine for the seraphis migration project, focusing on coordinating async processes (mainly around balance recovery right now) with the ambitious goal that the engine should be able to work as an enterprise backed with support for 10s or 100s of concurrent wallets`
`[02-01-2023 17:11:32] <isthmus> "enterprise backed with support for 10s or 100s of concurrent wallets" This would be awesome`
`[02-01-2023 17:11:40] <Rucknium[m]> UkoeHB: Does that mean that monero-wallet-rpc could have more than one wallet open at a time?`
`[02-01-2023 17:12:12] <UkoeHB> Rucknium[m]: that's what I'm thinking yeah, it's been a pain-point for a long time I think`
`[02-01-2023 17:12:15] <rbrunner> You mean whatever will come after monero-wallet-rpc ...`
`[02-01-2023 17:12:57] <Rucknium[m]> That would be very nice :)`
`[02-01-2023 17:13:40] <UkoeHB> 3. discussion, anything to talk about today?`
`[02-01-2023 17:15:10] <dangerousfreedom> I'm trying to understand the pros/cons of different wallet designs and one thing that scared me was the fact that we didnt talk much about the daemon/rpc communication yet for seraphis. Is it part of the no-wallet-left-behind efforts?`
`[02-01-2023 17:15:11] <dangerousfreedom> For the moment I believe we could use a fake ledger to simulate transactions and create the necessary wallet functions (I'm making a prototype in this direction). But it may have a big impact on some wallet decisions too.`
`[02-01-2023 17:15:11] <dangerousfreedom> How do you guys see this part advancing?`
`[02-01-2023 17:16:27] <rbrunner> Well, if we have you thinking on this, I think that's already a good way.`
`[02-01-2023 17:16:34] <Rucknium[m]> I think communication between monero-wallet-rpc and remote nodes is one of the less reliable parts of the Monero ecosystem.`
`[02-01-2023 17:17:30] <rbrunner> That's why I still advertise a bottom-up approach: Start with something small, see how it turns out, work your way up`
`[02-01-2023 17:17:46] <rbrunner> The greater shapes of the whole architecture will reveal themselves over time`
`[02-01-2023 17:19:02] <rbrunner> Needs a bit of confidence that we won't chase down too many dead ends of course,`
`[02-01-2023 17:19:09] <rbrunner> and don't have to backtrack too often.`
`[02-01-2023 17:19:59] <rbrunner> But take only such little question like this one: More than 1 wallet open at any given time over RPC is nice, but how does that influence the RPC interface?`
`[02-01-2023 17:20:30] <rbrunner> How will that best look if you introduce state like "the set of currently open wallets"`
`[02-01-2023 17:21:09] <rbrunner> And these even update like crazy with UkoeHB's enterprise grade scan engine :)`
`[02-01-2023 17:22:17] <UkoeHB> well not that crazy unless you have a lot of threads`
`[02-01-2023 17:22:18] <blankpage[m]> What is "that ordinal nonsense"?`
`[02-01-2023 17:22:30] <UkoeHB> blankpage[m]: check -lounge`
`[02-01-2023 17:23:22] <rbrunner> Who knows, maybe we will even move away from RPC towards ZMQ because it turns out things are better to handle through that by an order of magnitude`
`[02-01-2023 17:23:31] <rbrunner> after we granted all possible wishes`
`[02-01-2023 17:24:39] <blankpage[m]> Will do thanks`
`[02-01-2023 17:24:41] <Rucknium[m]> IMHO, RPC should keep working for legacy systems and legacy coders :)`
`[02-01-2023 17:25:27] <rbrunner> It should, agree. Just don't know where we land after we will have walked the full way.`
`[02-01-2023 17:27:24] <UkoeHB> rbrunner: for a public interface you'd probably issue wallet ids for each wallet activated, then forward requests based on id. Layers of forwarding isn't that exciting, but idk what other options there are.`
`[02-01-2023 17:28:16] <rbrunner> Yeah, the familiar "handle" pattern that OSs use for files, for example.`
`[02-01-2023 17:29:29] <rbrunner> With all the problems you will get if clients do not correctly handle those on their side and forget to close wallets until you have 1000 open :)`
`[02-01-2023 17:29:57] <rbrunner> Or the same wallet a thousand times.`
`[02-01-2023 17:30:20] <rbrunner> Ever the pessimist :)`
`[02-01-2023 17:30:25] <Rucknium[m]> I thinking about giving a text-to-speech presentation at Monerotopia: "A Statistical Research Agenda for Monero." An overview of questions including decoy selection of course, but also post-Seraphis fee estimation, possible remote node timing attacks, transaction churning, tx flood detection, dynamic block size, etc. How does that sound, or does anyone have a better idea?`
`[02-01-2023 17:31:06] <UkoeHB> easy enough to enforce open wallets are unique`
`[02-01-2023 17:31:41] <UkoeHB> Rucknium[m]: that sounds good to me`
`[02-01-2023 17:31:48] <rbrunner> Are these one-hour presentations? If yes, you might really have to limit yourself to an overview`
`[02-01-2023 17:32:01] <rbrunner> with some many possible points`
`[02-01-2023 17:32:19] <rbrunner> But sounds interesting, yes`
`[02-01-2023 17:32:55] <UkoeHB> more like 25-35 minutes I think`
`[02-01-2023 17:32:59] <Rucknium[m]> For Monerotopia, an overview is appropriate. MoneroKon is the more technical conference.`
`[02-01-2023 17:34:28] <dangerousfreedom> Rucknium[m]: Sounds really cool :)`
`[02-01-2023 17:35:24] <rbrunner> Did you ever do already such a "text-to-speech" presentation? Does that work well=`
`[02-01-2023 17:37:04] <Rucknium[m]> No. I have been experimenting with some tools. I hope it works OK.`
`[02-01-2023 17:46:10] <blankpage[m]> If it is janky you could give someone a copy of your script to act as your physical avatar. Even better if they understand enough to answer basic questions.`
`[02-01-2023 17:46:29] <UkoeHB> Hmm I don't have anything to say so maybe we can wrap it up early. Fortunately or unfortunately, it seems I will be spending a lot more time on seraphis migration than I originally planned, since it looks like there is a lot of advanced architectural work that A) interests me, B) probably needs my help. Not sure how much actual wallet-level code I'll write, but we'll see how it goes.`
`[02-01-2023 17:49:44] <UkoeHB> thanks for attending everyone`

## spirobel | 2023-02-01T19:26:06+00:00
can we use the seraphis code to build a wallet right now? or is this code still going to change based on your mood?
it seems really uncertain what features will be included and what the target of this wallet code is.
is it an "enterprise wallet", is it a "mobile wallet" how is this decision made and by whom? 

from reading this chat log it seems like it will depend on how @UkoeHB  feels about it. 

I also want to mention that wasm does not have threads.
So you would only be able to address this target with a duct tape solution like emscripten.

Also keep in mind wasm does not have garbage collection, so a long running giant blob produced by emscripten will lead to instability.

On the other hand there are wonderful solutions for threading and data fetching in javascript.
So if this code was modular enough, smaller monero business logic related chunks could be orchestrated from javascript.

That would make it better.
But this wont be possible if this very foundational library is written with a specific target like an "enterprise backend wallet" in mind. 

## paulshapiro | 2023-02-01T19:30:51+00:00
What is an enterprise wallet, and what's a mobile wallet?
Any code handling transactions should be built to easily handle anywhere from 1 to 1000 wallets. Where's the issue?

WASM has had threading and data "fetching" support for some time. It has worked the same way it has worked in JS.

Whatever code you want can already be orchestrated by JS via the embeddable factorization of Monero src which I have maintained for... about 6 years now.

## spirobel | 2023-02-01T19:37:43+00:00
>WASM has had threading and data "fetching" support for some time. It has worked the same way it has worked in JS.

no. That is coming through emscripten duct taping stuff together. Even just the shared array buffers feature can be a problem.

>Any code handling transactions should be built to easily handle anywhere from 1 to 1000 wallets. Where's the issue?

I agree. Offer a clearly defined api that just  handles the blocks and can be compiled to wasm. 

> whatever code you want can already be orchestrated by JS via the embeddable factorization of Monero src which I have maintained for... about 6 years now.

public release when?

## paulshapiro | 2023-02-01T19:47:15+00:00
> no. That is coming through emscripten duct taping stuff together. Even just the shared array buffers feature can be a problem.

Please describe one or two problems specifically then. Emscripten's pthread support has come out of experimental status.

> I agree. Offer a clearly defined api that just handles the blocks and can be compiled to wasm.

I did that a few years ago. I dont think you where here yet.

I will publish that soon then via PR along with about 10-20 others in backlog.

> public release when?

What do you mean? I was the first person to publish the scripts to produce a successful WASM transpilation of the Monero core source. When I took over mymonero in 2016 we were leaning on luigi to handwrite transaction format upgrades like ringct in JS on top of a crypto.c only WASM file  from like 2014. luigi is elite and 1 in 1B so he did delivered consistently, but I knew it was better to share such critical code; so I built the emscripten chain from scratch and factored an embeddable form of core monero, and then built the wrapper code to bypass wallet2 like that. So all of the monero-ecosystem code that everyone is using which does JS on top of emscripten came from my work. And it's true i maintain an evolved but still in stealth form but I cannot tell you when it will be public yet. I have no help yet.

## UkoeHB | 2023-02-01T19:51:10+00:00
> can we use the seraphis code to build a wallet right now? or is this code still going to change based on your mood?

The core library is mostly stable now, I don't expect any major changes aside from iterative feedback although there's no account for where my mood might take me :).

> it seems really uncertain what features will be included and what the target of this wallet code is.

Correct, you'd probably have to be crazy to start building a third-party wallet now.

> from reading this chat log it seems like it will depend on how @UkoeHB feels about it.

Who are you complaining to, exactly? Step up to the plate if you don't want me taking lead on major architectural questions.

> I also want to mention that wasm does not have threads. So you would only be able to address this target with a duct tape solution like emscripten.

An ideal solution would use an implementation-defined task scheduler that can work in environments that only have one thread. It's an engineering challenge, who knows if we will manage to achieve that.

> So if this code was modular enough, smaller monero business logic related chunks could be orchestrated from javascript.

We will see how it goes. @jberman has said he doesn't want users of the wallet engine to need to worry about async at all (other than startup and compiletime configurations, presumably).


## spirobel | 2023-02-01T20:13:28+00:00
@paulshapiro 
>but I knew it was better to share such critical code; 

smart move

>So all of the monero-ecosystem code that everyone is using which does JS on top of emscripten came from my work

thank you for your work!
Have you taken a look at the seraphis code yet?
maybe you can give some input on how to factorize it!

@UkoeHB 
>Step up to the plate if you don't want me taking lead on major architectural questions.

do you really want to get others involved with "your" project? If you mean this sincerely, I am happy to help.

>An ideal solution would use an implementation-defined task scheduler that can work in environments that only have one thread. It's an engineering challenge, who knows if we will manage to achieve that.

"implementation-defined task scheduler" sounds like a complex word. It sounds like you view this as a large preassembled puzzle with only one piece missing that the wallet implementer can then insert. Is that correct?

A better solution would be to provide the wallet implementers with a box of functional lego pieces instead of this preassembled puzzle.
If you set the requirement that these code blocks need to be compiled to a single threaded wasi target everything could fall into place.

So we should setup a toolchain that does that (without emscripten) and use it to build the "wallet engine".
The api that falls out of this will also solve many issues for wallet implementers that have other targets than wasm.
Because it is the most restricted target, we will be assured that the code will work fine on all the other targets.

## UkoeHB | 2023-02-01T20:40:47+00:00
> do you really want to get others involved with "your" project? If you mean this sincerely, I am happy to help.

Idk where you got this idea that it's 'my project', but your baseless hostility is definitely a turn-off. tevador, jberman, dangerousfreedom, rbrunner are all people very involved in and influencing the seraphis project one way or another.

> It sounds like you view this as a large preassembled puzzle with only one piece missing that the wallet implementer can then insert. Is that correct?

No, I am only talking about the engine's internal async handling here. It would be pretty insane to want to support 100+ wallets without internal async.

> A better solution would be to provide the wallet implementers with a box of functional lego pieces instead of this preassembled puzzle.

As you said "it seems really uncertain what features will be included", so idk how you seem to know what 'this' will turn out to be (preassembled puzzle or otherwise).

> If you set the requirement that these code blocks need to be compiled to a single threaded wasi target everything could fall into place.

Being able to run single-threaded is a goal I already had. Which you might know if you showed up in IRC and asked questions and initiated discussions about the things you are interested in.

## paulshapiro | 2023-02-01T20:45:57+00:00
It's not that complicated to make an API which supports asynchrony via events, into one which executes serially... and you can just use an ifdef statement to redact the threading implementation at compile time, .. no?

And the implementor of the wallet's asynchronous aspects could avoid worrying whatsoever about modifying their own code for single threaded execution if they use a dependency injected concurrency interface that you can then concretely implement for your emscripten transpilation.

Threading is going to be important for other parts of Monero's code too. If you're having issues with threading in Monero code under WASM I would first look at whether the Monero code needs enhancing before thinking about changing emscripten's code on implementing such fundamental things - though I have made PRs to it in the past. I have also not had any issues with pthread support under emscr yet.

So basically, whether the wallet is built as pure functions so that us third party peasants can safely consume the code, or wallet implementation continues to be complected (rich hickey what up) with the wallet object implementation, is, oddly, fairly orthogonal to whether it can support single threaded integration. 

Regards

@UkoeHB I would instrument first. Chances are that the real latency causers are e.g. persistence API IO so the concurrency might even be able to be pushed off to that for now.

## paulshapiro | 2023-02-01T20:47:43+00:00
Oh, you're talking about scanning, too.

## UkoeHB | 2023-02-01T20:54:58+00:00
> And the implementor of the wallet's asynchronous aspects could avoid worrying whatsoever about modifying their own code for single threaded execution if they use a dependency injected concurrency interface that you can then concretely implement for your emscripten transpilation.

You still need to take care not to introduce situations where tasks can get black-holed or where calling tasks that launch their own continuations can cause stack overflow if your task queue has a max size (Monero's current threadpool immediately invokes scheduled tasks if the task queue is full). Although both of those cases can happen with multiple threads (just with less frequency than single-threaded), so I guess it's a general problem for async.

## spirobel | 2023-02-01T20:59:20+00:00
@UkoeHB 
>idk how you seem to know what 'this' will turn out to be

I dont know that is why I am asking. 

>It would be pretty insane to want to support 100+ wallets without internal async.

You see, we need to define clearly what your scope is. Is your task to build an enterprise backend wallet, or is it to build a poc wallet and a wallet engine that others can use to implement their wallets?

If the scope is undefined and fluidly changing it is hard to say what is internal to your project and how it interfaces with the rest of us.


@paulshapiro 
> dependency injected concurrency interface that you can then concretely implement for your emscripten transpilation.

the solution is to not use emscripten at all. Just compile directly to wasi and keep things functional.
Instead of us "third party peasants" injecting our code into @UkoeHB  preassembled puzzle, it would be better if we were handed a lego box.

The end result will be  more flexible and likely to run on all targets. 

> You still need to take care not to introduce situations where tasks can get black-holed or where calling tasks that launch their own continuations can cause stack overflow if your task queue has a max size 

so just let the implementer do the async parts. You achieve that by keeping the wallet engine functional. You can still write async parts for your wallet poc on top of that.

## paulshapiro | 2023-02-01T21:07:47+00:00
Oh, you're using wasi, not emscripten.

I have argued for the lego approach for years.

Whether a concurrency interface is dep injected has nothing to do with emscripten or not.
And whether a concurrency interface is dep injected also has nothing to do with whether the code is written as legos.
You still haven't replied about whether you found issues with emscripten's implementation..

Whatever you do in wasi is still going to be interfaced into at your application level somehow. 
So it really has nothing to do with threading. 

Regardless, there's a reason I gave a whole talk in 2019 about how Monero needs to have a standard for acceptability of code consumability in an embedded context. Have you ever seen it?

## spirobel | 2023-02-01T21:16:48+00:00
>Regardless, there's a reason I gave a whole talk in 2019 about how Monero needs to have a standard for acceptability of code consumability in an embedded context. Have you ever seen it?

Yes I saw it. You raised many valid points in this talk!

I think the issue here is really communication and finding the right scope.
I also think that Monero should provide precompiled libraries for the most common targets, including linux, mac, wasi. (and arm builds for mobile)

These libraries should also be able to be used from the most commonly used programming languages.

If @UkoeHB manages to build a great POC for Seraphis that also works great as a backend enterprise wallet, that is a good stretch goal.
But it should not come at the expense of the things that the Monero developer community really needs.
Which is precompiled, well documented libraries that can be interoperated with from the most commonly used programming languages without the hassle of needing a custom build process and and wrapper code.


## paulshapiro | 2023-02-01T21:26:26+00:00
Thank you. I had no idea you saw it this past year or two. 
I guess you may not be aware but Monero already builds to precompiled granular libraries. Granted it's not zero dep as I would like but it's been done for years. Look at how monero-lws consumes links to monero. https://github.com/vtnerd/monero-lws/blob/0435e7a2d38beb9ad340560a5de32285ecc08803/CMakeLists.txt#L36

What stops you from making your own cmake file?

I think what you're really arguing for is adding a wasi target to mainline official.

# Action History
- Created by: Rucknium | 2023-02-01T13:27:45+00:00
- Closed at: 2023-02-08T15:16:40+00:00
