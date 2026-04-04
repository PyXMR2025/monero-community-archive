---
title: 'Seraphis wallet workgroup meeting #71 - Monday, 2024-05-20, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1011
author: rbrunner7
assignees: []
labels: []
created_at: '2024-05-19T04:47:20+00:00'
updated_at: '2024-05-20T19:08:59+00:00'
type: issue
status: closed
closed_at: '2024-05-20T19:08:58+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1005

# Discussion History
## rbrunner7 | 2024-05-20T19:08:58+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1011
<s​needlewoods> hey
<d​angerousfreedom> Hello
<r​brunner7> Ok, maybe some more people will join later. Anything to report from you two?
<d​angerousfreedom> I didnt do much last week other than bothering jeffro with some questions.
<j​effro256> howdy
<s​needlewoods> I worked on the API until your comments, after started to look at which functions the current API is missing, but haven't started coding
<s​needlewoods> after that I started*
<s​needlewoods> I'd still like to hear other opinions on how we should proceed exatcly
<r​brunner7> For the record, the work in progress in question that I commented on is this: https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_feature_complete_api_1
<j​effro256> After some back and forth with @tevador, we figured out that Jamtis-RCT is not as private against quantum adversaries as Jamtis on Seraphis in its current state
<jberman> sorry I'm late! here
<s​needlewoods> yes, I have two local commits for that branch that I haven't pushed yet
<jberman> me: implemented growing an existing tree for fcmp's, this week I'm planning to make it cleaner, implement in the DB, and implement `trim`
<r​brunner7> Nice how many things run in parallel now
<r​brunner7> jeffro256: Already decided what will happen after these insights? "Back to the drawing board", maybe?
<r​brunner7> Anyway, I think we should look at SNeedlewoods 's work so far today and try to decide how to proceed
<r​brunner7> As you can read in the backlog, I am beating the drum for a quite-modest-in-comparison first step
<r​brunner7> Which means two things, basically:
<r​brunner7> A) Define the feature-complete API
<r​brunner7> B) Implement that on current Monero master using purely `wallet2` and some new code. No Seraphis lib (yet), no big refactoring
<r​brunner7> With the hope that we could bring this into actual service relatively quickly - say, this fall for example.
<j​effro256> I like this approach to kick things off
<r​brunner7> I would like to hear people's opinion whether they think that would be worthwhile
<r​brunner7> I think I never mentioned this, but certainly not for a long time: Don't underestimate the work needed to define a good API.
<jberman> I think this is a fine general approach, but I also am in favor of accelerating the timeline to move the new scanner forwards
<r​brunner7> If you look at a good interface or API, you see almost immediately that it's good. And everthing looks so simple, so straightforward. Until you try yourself to define one :)
<r​brunner7> jberman: How much of the Seraphis library would be needed for that scanner?
<jberman> also having a look at @sneedlewoods code, it generally looks like a solid approach and in line what was I thinking too (housing wallet settings in a separate class e.g. looks solid), though I'd need to look at it deeper, it passes my initial smell test
<r​brunner7> The "wallet settings class" is quite a bit bigger now that I would probably have defined it, and how it may enter the new feature-complete API
<r​brunner7> And of course right now it saves itself, which it wouldn't do in a very first version, that would still be the job of `wallet2`
<jberman> "How much of the Seraphis library would be needed for that scanner" -> off the cuff: the scan machine, the enote store, all legacy enote types and utils, my PR, and then code to import the Seraphis lib enote store / state into a wallet2 instance. I could get a list of files
<r​brunner7> Do you think it would be "doable" to get this into current Monero master without, well, too much drama and controversies?
<jberman> + all the code for the scanner not currently implemented that's still needed (pool scanning, mutable subaddress lookahead, scanning all necessary data wallets need)
<jberman> considering it speeds up wallet scanning such a significant amount (in my tests), I would be surprised if it caused drama/controversy
<r​brunner7> And we just order jeffro256 to review everything, over a single weekend, problem solved :)
<r​brunner7> (Joking aside, I don't think we have another candidate as good as him for that ...)
<j​effro256> lmao
<j​effro256> I'd definitely be willing to review it
<r​brunner7> That's the spirit!
<j​effro256> But there's also plenty of other good candidates, can't personally say that I'm the best
<j​effro256> thank u though
<r​brunner7> I think if we really manage to get that faster scanner in, that would be quite good advertising, and would probably enhance "momentum"
<r​brunner7> jberman, I also worry a bit about larger changes that you might want to do still in `wallet2` following your FCMP track. What's the current thinking there, how to get those in?
<j​effro256> does the scanner "mesh" well with wallet2? I.e. can we construct messages to pass to `wallet2::process_new_transaction` easily?
<j​effro256> In the interim between introducing the faster scanner and completely removing `wallet2`, we could use the scanner to filter out all the relevant txs, then introduce them to `wallet2` as we normally would in the `refresh()` method
<r​brunner7> jeffro256: Sounds like a good approach
<r​brunner7> It's basically that, right, a new "super refresh" :)
<jberman> re: fcmp in wallet2: I haven't given it deep thought yet, but I can keep as much logic as possible out of wallet2, only do the bare minimum in wallet2 (e.g. try to include a `get_full_chain_membership_proof` which encapsulates all logic for constructing the fcmp somewhere)
<r​brunner7> Ok, jberman , let's keep an eye on that while we move forward on at least two fronts at once
<k​ayabanerve> Ideally, we replace CLSAG_prove? with a rather complete fn
<jberman> re: Seraphis async scanner meshing well with wallet2: I wrote up an issue here showing what data the async scanner currently doesn't capture that wallet2 does: https://github.com/UkoeHB/monero/issues/48
<r​brunner7> Hmm, quite a list. Will you have to go through that before your scanner can go live? Could be?
<jberman> re: constructing messages to pass to `wallet2::process_new_transaction`: that's actually doable with the approach discussed in that issue^
<jberman> basically async scanner identifies which txs the wallet cares about, then `process_new_transaction` consumes those which the wallet cares about
<j​effro256> nice
<jberman> Ideally i'd imagine getting rid of process_new_transaction entirely though
<r​brunner7> Isn't there code around depending on that?
<r​brunner7> (Thinking again in short time frame)
<r​brunner7> If we manage to achieve almost 100% interface stability for all existing clients for our very first version, the less friction it produces
<jberman> wallet2::refresh depends on it, I think it's replaceable without much effort once the approach described in that issue is implemented though
<r​brunner7> Ah, maybe I confuse this with that kind of "event hooks" that `wallet2` provides
<r​brunner7> Are you talking about an especially complex *internal* method?
<jberman> process_new_transaction does fire events like on_money_received and on_money_spent
<r​brunner7> Yeah, that "on_xyz" stuff
<r​brunner7> That probably better stays functional, I was meaning to say
<jberman> ya process_new_transaction is a fairly large complex function doing a lot: it scans a tx (or reuses a cache if there is one, which there is in the normal case), then places all structured scanned data from that tx in the wallet's state
<r​brunner7> So I think support is here to wait with restructuring and starting to supersede larger parts of `wallet2` *except* scanning, and come up first with a `wallet2` based feature-complete Wallet API
<sneedlewoods> +1
<jberman> thumbs up from me
<r​brunner7> Alright. We still have some time left to maybe touch another, smaller question regarding that API, which I think still has some importance, the naming of new parts of that API, mostly new methods
<r​brunner7> I noticed that there is quite a difference in "style"
<s​needlewoods> Sorry, I'm having a hard time communicating my thoughts, I will just work on a new branch (pause the current API work) with rbrunner's suggestions and try to come up with something this week.
<r​brunner7> between the naming of the API methods and the rest of the Monero codebase
<r​brunner7> Basically, Pascal casing versus snake casing
<r​brunner7> It's a bit unfortunate IMHO, but the interface mostly uses Pascal casing
<r​brunner7> And now it's the question what we try to stay compatible with when naming new things
<r​brunner7> Consistency within the API, or consistency with the Monero codebase at large
<r​brunner7> Do people see what I mean?
<j​effro256> Are we talking about new names for outwards facing parts of the API?
<r​brunner7> Yes
<r​brunner7> There will be quite a lot of those, I guess
<s​needlewoods> I didn't have a strong opinion and you convinced me that staying consistent with the current API is the lesser evil
<jberman> staying consistent with current API makes sense to me for the external API
<r​brunner7> Yeah, personally I find a mix of styles worse than two styles in two quite separated parts of the codebase
<j​effro256> Yeah it makes sense to be consistent locally for the API
<r​brunner7> Ok, hammer down like in those court movies, consensus :)
<sneedlewoods> +1
<r​brunner7> Anything else for this very meeting?
<s​needlewoods> Can you maybe give a little more detail on what "define feature-complete API" means in terms of pull requests?
<r​brunner7> "Sorry, I'm having a hard time communicating my thoughts" SNeedlewoods , that's just the normal and natural learning process, don't worry
<s​needlewoods> How big (changed lines of code) should a PR be approximately? I assume we don't want just one PR for A)
<s​needlewoods> Should be easy to review, but we also don't want hundreds of tiny one function PRs I guess
<r​brunner7> Hmm, difficult to say. I would probably just work forward on my own separate branch, with as many intermediate commits as are convenient, and worry about PR'ing that to the Monero codebase later, after it's basically finished
<j​effro256> This would entail expanding the wallet API so that all direct references to `wallet2` can be removed from `monero-wallet-rpc` and simplewallet
<r​brunner7> I think that's also the approach that jberman is using for his new scanner: Worry about PRs after it's more or less complete
<r​brunner7> It will be a big PR finally, but also well-defined and "closed in itself", and won't introduce non-working intermediate steps
<jberman> that reminds me, I need to get some bite-sized PR's from that scanner up so daemons are prepared for it
<s​needlewoods> jeffro that's what I tried to do in my first approach, but it's not what rbrunner is suggesting, if I'm not totally confused right now
<jberman> but ya those PR's are small and not encapsulating the scanner logic, which will be a bit trickier to divvy up PR's for considering all those pieces (enote types, scanner types etc.)
<s​needlewoods> rbrunner thanks, that answered my question
<r​brunner7> Yes, as I see it, moving the CLI wallet and the RPC server over to the new API will be follow-up steps. Maybe even suitable for people that newly join our effort, who knows?
<r​brunner7> Or one for you, and one for dangerousfreedom  :)
<dangerousfreedom> +1
<r​brunner7> Anyway, I am around, if there are questions, just shoot.
<s​needlewoods> will do
<r​brunner7> Ok, the hour is full, and we have been very productive today IMHO. Thanks everybody for attending, read you next week at the latest.
<s​needlewoods> thanks everyone, bye
<j​effro256> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2024-05-19T04:47:20+00:00
- Closed at: 2024-05-20T19:08:58+00:00
