---
title: 'Seraphis wallet workgroup meeting #11 - Monday, 2023-01-30, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/787
author: rbrunner7
assignees: []
labels: []
created_at: '2023-01-27T14:56:01+00:00'
updated_at: '2023-02-13T00:09:56+00:00'
type: issue
status: closed
closed_at: '2023-02-13T00:09:56+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #783 

I think we should together look at possibilities to widen the group of people working on Seraphis code.

IMHO we are at the same time in a very good and a somewhat difficult situation right now. Good is that we have 3 people coding for Seraphis at the moment, which is quite something, and somewhere between 3 to 5 new people in the process of joining the Monero project to work on Seraphis, which is a bit unexpected, at least for me, but of course very welcome!

But on the other hand, it's quite difficult right now to assign suitable coding tasks to more people. The emphasis is on *right now*: I think in a few months the situation will be much better.

In a recent chat I compared it with building a house: A lot of work, for many people like plumbers, electricians, workers who set tiles, who put windows and doors, and so on. But all those people have to wait until the walls, the floors and the roof are there. It's a bit like that with the Seraphis wallet, as I see it: Until there is more "structure" realized, it's somehow hard to find jobs to work on it in parallel.

Anyway, I hope that if we look for ideas, starting in this meeting, we will muddle through the first few months!

# Discussion History
## rbrunner7 | 2023-01-30T19:02:45+00:00
````
<rbrunner7[m]1> Meeting time. Hello! https://github.com/monero-project/meta/issues/787
<rbrunner7[m]1> Who is around?
<jberman[m]> waves
<JoshBabb[m]1> Hiya
<Rucknium[m]> *waves*
<dangerousfreedom> Hello
<one-horse-wagon[> Hello!
<rbrunner7[m]1> Alright. Anything to report from last week's work? From me, just for the record, already mentioned yesterday, an FAQ: https://github.com/seraphis-migration/strategy/wiki/Seraphis-and-Jamtis-FAQ
<UkoeHB> hi
<UkoeHB> I've been thinking about how to do async architecture around balance recovery
<rbrunner7[m]1> As an optimization?
<jberman[m]> I've also been working on performant multi-threaded scanning using the seraphis lib; I'm hoping to have some code to share on that in the next 1-2 days. Working through some final kinks
<ghostway[m]> UkoeHB: That sounds interesting, how are you gonna achieve that? An actual async runtime or thread pools?
<ghostway[m]> If you want and have time to explain a little, Id be interested!
<UkoeHB> rbrunner7[m]1: for UX the wallet needs to support background refresh
<dangerousfreedom> I finished the first version of the knowledge proofs and made a PR to Koe. I believe I have all the proofs working with a basic unit_test for each. There are still clean-ups and more tests to add and also some extra work for the legacy and serialization but I guess that the core is building up nicely (https://github.com/UkoeHB/monero/pull/5/files)
<dangerousfreedom> I will focus back again on the wallet and I will probably have a simple demonstrator to show by next week (so we can better discuss the next tasks and the directions we want to go for some points).
<rbrunner7[m]1> As written in the meeting issue, today I would like to get an overview of the dev work directly on Seraphis code, and possibilities to have more people working on it
<rbrunner7[m]1> We have the very pleasant situation that we have (at least) 3 people interested to contribute, and that's quite a lot
<rbrunner7[m]1> Let me quickly make a list, so we have a common ground for the following discussion:
<rbrunner7[m]1> UkoeHB is of course working his Seraphis library, giving it finishing touches as far as I understand
<rbrunner7[m]1> jberman, as reported, is working on scanning
<rbrunner7[m]1> dangerousfreedom[m] implemented proofs, and will now switch to creating wallets
<rbrunner7[m]1> As new entrants, we have ghostway. I currently support them implementing something for this here: https://github.com/seraphis-migration/wallet3/issues/39
<rbrunner7[m]1> Then shalit. I adviced them to maybe make first some smaller PRs to the "old" codebase, and in parallel try their luck with this tricky conceptial problem: https://github.com/seraphis-migration/wallet3/issues/7
<rbrunner7[m]1> Then Josh Babb which I think has something to work on already, with some tests for Blake2b or so, if I got that correctly
<JoshBabb[m]1> Yes, I'll take a whack at it this week
<rbrunner7[m]1> Did I miss somebody who is also ready to work on Seraphis, but I am not aware, or simply forgot?
<rbrunner7[m]1> But anyway, a team of 6 people working to implement a part of Monero is quite remarkable, I don't remember when the last might have been like that
<rbrunner7[m]1> Even if koe soon retires from direct dev work
<UkoeHB> ghostway[m] Summary: The 'enote store problem' is that an enote store is responsible for a huge part of wallet functionality (it records details about a user's balance and makes enotes available to be used as tx inputs.), while at the same time being subject to continuous updating (chain and pool monitoring, plus the possibility of a legacy key image import). To manage access to the enote store, I built a 
<UkoeHB> single-reader/multi-writer locking utility. The 'mutating process' is a task chain (async process) that owns the `writable` handle to an enote store that can be `write_locked` whenever an update is needed (only one `writable` may exist). Readers own `readable` handles that may be `read_locked` for const-ref access to the store (e.g. UI utilities or the tx input selector utility). Instead of requiring readers to scan 
<UkoeHB> the entire enote store for diffs, the enote store will produce a diff report every time it's updated. Diff reports can be sent along with `readable` handles to any potential listeners.
<rbrunner7[m]1> And with so many people there is a problem when we will have parts for them to work on.
<rbrunner7[m]1> As things progress, it probably will become easier and easier to have several people working in parallel, but right now I got the impression it's a bit difficult still.
<UkoeHB> The other main piece is when a user request comes in to mutate the enote store (e.g. a legacy key image import), the request will be packaged into an update task and sent into the enote store process. The enote store process will eventually pull pending update requests out and schedule them.
<rbrunner7[m]1> What do people think? jberman , dangerousfreedom[m] , what's your take on this?
<ghostway[m]> UkoeHB: Oh ok, a standard pattern 
<UkoeHB> That's how far I got ^
<ghostway[m]> UkoeHB: So what does need to be done? Sounds pretty planned out
<ghostway[m]> * So what needs to be done? Sounds pretty planned out
<UkoeHB> No idea, this is new territory for me plus who knows if jberman[m] will put up with it lol
<rbrunner7[m]1> Maybe we have already a candidate for a piece of the wallet, or an extension of the library, that some added dev could work on?
<UkoeHB> Right now I am experimenting with continuations to see how the updater process could run itself. Might look into `boost::then` soon
<rbrunner7[m]1> Or does that "naturally" fall into the code region that jberman is currently working on?
<ghostway[m]> UkoeHB: I see, can you point me to the relevant code? 
<ghostway[m]> Jberman seems to be here heh
<ghostway[m]> Ah, I've misread your message. Ok, so you have something already.. thought I could help
<ghostway[m]> That's a standard pattern afaik (well, it's what I've used for similar stuff)
<UkoeHB> it's not implemented, just theoretical (aside from `rw_lock`)
<UkoeHB> rw_lock: https://github.com/UkoeHB/monero/blob/seraphis_lib/src/common/rw_lock.h
<ghostway[m]> That I've seen
<ghostway[m]> Thanks
<rbrunner7[m]1> So, any ideas for parts of Seraphis related or Jamtis related code that additional devs could soon, medium term, start to work on, because A) it's reasonably clear what is needed and B) there is not too high a danger of overlap with what other devs are doing?
<dangerousfreedom> <rbrunner7[m]> "What do people think? jberman..." <- Looks great to have more people aboard. I hope we can have the work a bit more structured soon so we can efficiently work in parallel. For that I think we need the basics of the wallet I guess. Like a common source code where we can start implementing the features.
<dangerousfreedom> I'm trying to re-use all the console-handler functions to create a minimum interface where the commands can later be implemented.
<jberman[m]> Basically how scanning development has gone so far: I've been working on using the Seraphis lib as is to implement scanning pointing to a daemon today. There are nuts and bolts things that I've implemented such as converting "old" tx data types into Seraphis compatible types, and slotting in network requests/processing into the expected place using the lib
<rbrunner7[m]1> So you did not yet start to work on the enotes input selection stuff?
<jberman[m]> I mentioned I intended to switch and then switched to working scanning/balance recovery some weeks ago
<rbrunner7[m]1> Ah, ok, maybe that escaped me somehow.
<rbrunner7[m]1> Would it make sense then for somebody else than you to take that over? Or would that only lead to a situation where you run out of work soon?
<jberman[m]> input selection or scanning?
<rbrunner7[m]1> But maybe that's anyway more something for somebody with experience already
<rbrunner7[m]1> The input selection module
<rbrunner7[m]1> I was somehow thinking you implemented both things together somehow ...
<jberman[m]> would make sense for somebody to take that over I think
<jberman[m]> I actually originally thought we'd want to keep a lot of the same decisions wallet2 makes when biasing towards certain inputs, and in that case it would be more useful for someone familiar with how wallet2 does it, but moo recently said in #monero-dev that the bulk of those decisions can just be removed
<jberman[m]> discussion starts here: https://libera.monerologs.net/monero-dev/20230125#c195088
<rbrunner7[m]1> How could that work, with that enote store architecture still quite in flux? Just pretend that the store is very simple, to have at least something where to draw enotes from?
<jberman[m]> goes into the next day
<rbrunner7[m]1> And then later slot in the "real" enote store?
<rbrunner7[m]1> Ah lol, somehow typical moneromooo :)
<rbrunner7[m]1> Anyway, noted, maybe we can make some direct talk about this in the next few days, so that I know better how that could work, and would be able to support however wants to give it a try
<jberman[m]> I think UkoeHB can give a more informed answer there^
<rbrunner7[m]1> dangerousfreedom[m]: I remember that as part of your early work on wallets you implemented some Base32 stuff. Would it be reasonable to separate that from your direct wallet reading / writing work you plan for you, and that would be something small and not too complicated for a newcomer to hammer into shape?
<UkoeHB> rbrunner7[m]1: I think the current enote store will not need to change much between now and production. It's better to not overload its responsibilities, and instead keep it focused on balance recovery. My idea instead is for enote store consumers to build their own personal mirror images of the enote store, using whatever caching strategy makes the most sense. Those mirror images can use diff reports from enote store 
<UkoeHB> updates + a `readable` handle on the enote store to update themselves (I'm not 100% sure this will work well, since if you read-lock the enote store and interpret it with a stale diff report, that may cause problems - have to think about it carefully).
<rbrunner7[m]1> Or maybe we have some parts of Jamtis in general that somebody could implement?
<dangerousfreedom> rbrunner7[m]: Yes. I guess so. There is actually no coherent workflow in my wallet work. Just a bunch of code floating :p
<rbrunner7[m]1> Parts that I overlooked so far as "implementation-ready"
<dangerousfreedom> I'm trying to give a coherent workflow to my job yet
<ghostway[m]> UkoeHB: Who are enote store consumers? They're not the same node are they?
<rbrunner7[m]1> "Just a bunch of code floating" well, that's something :)
<rbrunner7[m]1> Remember, if you need somebody to brainstorm with about good ideas how to tackle things, I am ready
<dangerousfreedom> Not really a bunch, some :p
<rbrunner7[m]1> But maybe we just keep that separate for the time being, that Base32 stuff, and I have a closer look whether somebody could take over from you there
<dangerousfreedom> So if someone wants to nail down the base32 history.. Feel free. I think it is almost done but needs some review.
<rbrunner7[m]1> I mean, not just continue there out all things floating, dangerousfreedom[m] 
<UkoeHB> ghostway[m]: I will think about a way for you to help. I don't plan on getting sucked into wallet implementation stuff, so I don't want to 'lick the cookie' on anything. One thing I definitely help with is reviewing PRs: https://github.com/monero-project/monero/pulls?q=is%3Apr+is%3Aopen+UkoeHB . Everyone working on the seraphis migration project should be reviewing seraphis-related PRs where possible (I don't expect 
<UkoeHB> crypto reviews from everyone).
<UkoeHB> ghostway[m]: enote store consumer = anyone who wants to read the store contents
<rbrunner7[m]1> Ah, yes, that's also a possible work, you mentioned that those PRs need review. But, uh, what do I have to know if I want to review those?
<ghostway[m]> UkoeHB: Why would they duplicate the store though? Is that only the cache?
<rbrunner7[m]1> Aren't those review quite a challenge, depending on know-how?
<UkoeHB> ghostway[m]: the store has multiple internal caches, it doesn't make sense to add more and more internal caches for different use-cases
<ghostway[m]> So I don't understand what you duplicate
<JoshBabb[m]1> rbrunner7[m]1: Sometimes it's hard to see errors, sometimes you see something easy someone else glanced over.  It's good practice for everyone to check it all to learn anyhow
<UkoeHB> the duplication is when you want a different mapping strategy to avoid O(N) reads
<UkoeHB> O(N) is a problem for very large enterprise-grade wallets, which the core software needs to support
<ghostway[m]> Aha. That's not obvious from what you've wrote. I thought you're trying to solve some threading issue
<ghostway[m]> Sorry
<UkoeHB> yeah mb
<UkoeHB> rbrunner7[m]1: I'd say, take a look at the PRs and decide for yourself if it's in-scope of your capabilities.
<rbrunner7[m]1> Ok, so far we seem to have input selection and Base32 as good medium-term dev work that could be "handed out", and a look at those PRs to see whether a review is within reach. And possibly some help working out the thing discussed here about the enote store, which goes a bit over my head :)
<ghostway[m]> UkoeHB: I have to say, thanks for trying to see where I could help, I'd like to 
<rbrunner7[m]1> Anything else for today? Time flies, we are already near the full hour
<rbrunner7[m]1> I wonder how thing will look with so many people when dev work will be in full swing on many fronts at once. That might get intesting.
<rbrunner7[m]1> Ok, thanks for the interesting discussion, and the good attendance. See you next week again in this theater :)
<dangerousfreedom> Thanks for writing the FAQ and your work rbrunner7[m] 
````


# Action History
- Created by: rbrunner7 | 2023-01-27T14:56:01+00:00
- Closed at: 2023-02-13T00:09:56+00:00
