---
title: 'Seraphis wallet workgroup meeting #24 - Monday, 2023-05-29, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/842
author: rbrunner7
assignees: []
labels: []
created_at: '2023-05-26T16:48:46+00:00'
updated_at: '2023-05-29T19:16:42+00:00'
type: issue
status: closed
closed_at: '2023-05-29T19:16:41+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #840

# Discussion History
## rbrunner7 | 2023-05-29T19:16:41+00:00
````
<dangerousfreedom> I might be late for today's meeting so any feedback on this [issue](https://github.com/seraphis-migration/wallet3/issues/54) is appreciated 
<rbrunner7[m]> dangerousfreedom[m]: I have basically only one question here: Did you coordinate with shalit in this matter? I mean, is this issue a "joint initiative" of the two of yours? I ask because what you wrote here Thursday sounded like you would put that job into their hands, and I think they understood it that way in fact.
<rbrunner7[m]> Meeting in a bit more than 1 hour
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/842
<plowsof> waves
<Rucknium> waves
<ghostway[m]> Hello
<shalit[m]> Hello
<jberman[m]> hello
<rbrunner7[m]> So, what's there to report from last week?
<rbrunner7[m]> I finally came around to update our own wallet development repository: https://github.com/seraphis-migration/monero
<rbrunner7[m]> It now has the same state as UkoeHB repository.
<plowsof> +1
<jberman[m]> +1
<ghostway[m]> I wrote more of the migration tool. Now its able to migrate legacy keys to jamtis keys and has some more stuff
<ghostway[m]> For the key container, I'm waiting for feedback on what I should keep an eye on when finishing the key container and best practices there
<ghostway[m]> Not much more, had only a few hours to work on this the last week
<UkoeHB> hi
<rbrunner7[m]> I hope dangerousfreedom[m] can join soon, so we can clear up any doubts who will work on the enote store reading and writing ...
<UkoeHB> ghostway[m]: did you follow the jamtis migration guideline?
<ghostway[m]> I used what was written in jamtis.md in the migration section
<ghostway[m]> And read your comments 
<UkoeHB> ok
<rbrunner7[m]> Is that a part of the upcoming paper?
<UkoeHB> what upcoming paper?
<rbrunner7[m]> Your Seraphis and Jamtis paper
<rbrunner7[m]> Can't remember that Tevador's Jamtis gist has a section about migrating, but maybe I just overlooked
<jberman[m]> Nothing in particular to report from my end (haven't been working on wallet3 work but moving back over soon). I thought jeffro256  's proposal above to move away from the epee http client and use a new http client dependency in the new wallet was solid and worth bringing up again here
<ghostway[m]> Oh, I didn't fully read your new migration thing on github
<UkoeHB> rbrunner7[m]: you mean this? https://raw.githubusercontent.com/UkoeHB/Seraphis/master/implementing_seraphis/Impl-Seraphis-0-0-2.pdf
<ghostway[m]> (if you mean the implementing_seraphis)
<rbrunner7[m]> Probably, yes.
<UkoeHB> implementing seraphis does not discuss migration
<rbrunner7[m]> So ghostway with "jamtis.md" did refer to the original gist from Tevador after all?
<UkoeHB> yah
<rbrunner7[m]> Ok, sorry, then it's just me being a bit out of the loop :)
<rbrunner7[m]> I would like to pick up that proposal from jeffro256 to toss out the ages-old epee HTTP client and switch to something more modern and reliable and lose a few words about it
<rbrunner7[m]> On the one hand, I certainly see the appeal, and the merit, of this proposal
<rbrunner7[m]> On the other hand, well, I look at the time we are working already on the Seraphis wallet, half a year now, and where we stand after that
<rbrunner7[m]> and then a slight uneasiness grips me whether we really should do such a switch now
<rbrunner7[m]> out of all times
<rbrunner7[m]> What's the sentiment of the other people here?
<UkoeHB> how much effort is actually required to swap them?
<rbrunner7[m]> Not sure, that's probably hard to say, but such things tend to take more work than originally planned. Like my incremental tx pool update ...
<rbrunner7[m]> And well, maybe we can even get jeffro256 "over to the dark side" and help with wallet dev for some time, beside smaller things on the codebase, just not big things like switching the HTTP library now
<jberman[m]> I think it would be more work to re-use it than to swap them tbh
<jberman[m]> The reason it was brought up in the first place was because to achieve a significant perf boost in the scanner, it would be nice if the http client supported concurrent requests. epee does not currently and that's a decent investigation to fully understand why and how to safely modify it to support parallel requests
<rbrunner7[m]> Well, I have to leave such decisions to the pro's, certainly. I say to just not rush such things because the amount of work ahead is already monumental, so better not make it larger still without a good reason.
<rbrunner7[m]> And as a dev I know bloody well how tempting the lure of tossing out old and cranky things can be :)
<UkoeHB> it should be fine to do a preliminary investigation of the work required to swap - look at interface parity and how may loc are using the epee library
<rbrunner7[m]> Agree, after what jberman argued with that "concurrent requests" problem
<UkoeHB> it would probably be necessary to do the switch on master since otherwise rebasing will become a nightmare
<UkoeHB> or just use the new library for new code
<rbrunner7[m]> I think we could very well use two libraries side-by-side for some time?
<UkoeHB> and deprecate epee http at a later date
<valldrac[m]> The HTTP library is reemplacable in higher layers if needed, because there's a simple abstract http client already in wallet2. However, it doesn't solve the concurrent requests because wallet2 doesn't support that yet
<UkoeHB> all these questions can be answered by a preliminary investigation
<UkoeHB> valldrac[m]: we don't need concurrent requests in wallet2, just in new wallet code + the daemon
<ghostway[m]> rbrunner7[m]: The problem they stated earlier, is that a "correct" http client might not behave like what the epee client expects 
<valldrac[m]> s/reemplacable/replaceable/
<UkoeHB> if epee http is off-spec, it would be better to figure that out in the next 2 years instead of 10 years from now
<rbrunner7[m]> Well, we probably only have a problem with being off-spec if we start to use a new library and then have a mix on the Monero network for some transition period
<jberman[m]> I think the best reason to ditch it would be an epee http client-specific bug, which is further proof that having a re-implemented http client in the code is a net drag
<jberman[m]> I don't know of any atm (perhaps others more familiar with the history are aware), but I do have some thoughts as to potential ones I'd also like to look into more tangentially (ubuntu 22 local daemon SSL connection drops, iphone issues I don't run into on android connecting to a daemon using SSL)
<UkoeHB> jeffro256[m]: is investigating http swap something you'd want to work on?
<rbrunner7[m]> If we are cool with an investigation and are for it, do you think jeffro256 would take that work?
<valldrac[m]> Just as a side note. I wouldn't want to deal with any transportation protocols myself. I'd rather leave that to an external library. And if the HTTP client is only for making RPC calls, then I would go for a library like gRPC or something similar to do the job
<rbrunner7[m]> I would be surprised if not, seems like a good and interesting work. Not many such things left on the codebase, probably :)
<rbrunner7[m]> Er, that was what I was talking about: Switching to a new form of RPC just on top of everything else is more work again ...
<valldrac[m]> +1
<rbrunner7[m]> It's not a complaint, just a word of caution: We meet for half a year now in this Seraphis wallet working group, and our repository is still waiting for its very first PR.
<jberman[m]> https://github.com/j-berman/monero/blob/1180c8262e405708411d166ef3cb36bd5f98cb92/src/blockchain_utilities/blockchain_scanner.cpp#L264-L268
<jberman[m]> this section of code is not only gross, it's slow. an http client that supports concurrent requests would allow me to remove that and other lines of code, ideally down just to 1-2 every request
<jberman[m]> It's one of the things keeping me from PR'ing the code
<jberman[m]> I'm almost positive using an external dependency I don't have to deal with that grossness
<rbrunner7[m]> "grossness" is a coll word
<rbrunner7[m]> *cool
<jberman[m]> haha basically it's creating a pool of 15 connections to a single daemon from one client, to allow making concurrent requests
<rbrunner7[m]> I feel your pain
<jberman[m]> and then later on I have code to make it extendable so the connection pool can increase if a connection is currently processing a request, which I needed to manage safely too. it's code that I don't think should make it to production nor is it performant. the initial 15 connections take time
<jberman[m]> I'm sure it would be simple to replace with an external dependency and we can move forward with wallet3 stuff using the external dependency everywhere
<rbrunner7[m]> Ok, then let's see what develops re: investigation of replacing the HTTP client
<valldrac[m]> You guys might hate me, but maybe some project management could be useful here, to prioritize and analyze the impact of tasks like this (whether to switch to a new RPC or not). Because otherwise, it's hard to make decisions between what's better and what's possible... For me at least, that I know very little about the current efforts
<rbrunner7[m]> Well, these weekly meetings right now are our "project management" at the moment... As long as not more people are really working on it, and work on it with substantial time budgets, and in parallel, not much more is needed yet.
<valldrac[m]> +1
<rbrunner7[m]> Anyway, I would like to encourage everybody to open issues to discuss anything they feel is important, and hopefully we can get interesting and focussed discussions going there.
<rbrunner7[m]> That would be here: https://github.com/seraphis-migration/wallet3/issues
<jberman[m]> will give jeffro256 a day or so to get back on if they're interested in the investigation. if not, I can investigate and lay out clearer pros/cons of switching vs not
<rbrunner7[m]> Sounds like a deal
<jberman[m]> +1
<rbrunner7[m]> Looks like we will have to clear up that question about the enote store later, when dangerousfreedom[m] returns.
<rbrunner7[m]> Anything else for this meeting here?
<jberman[m]> ya probably a dumb question, but what UkoeHB  were the "jamtis migration guidelines" you were referring to?
<rbrunner7[m]> https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#43-migration-of-legacy-wallets
<rbrunner7[m]> Maybe this
<jberman[m]> right I wasn't sure if that or something else
<jberman[m]> also with regards to dangerousfreedom[m] 's serialization stuff, fwiw I went back and starting reading through this issue and am still going through it and it's providing more helpful context: https://github.com/seraphis-migration/wallet3/issues/10
<jberman[m]> I'm still reading and thinking on it
<rbrunner7[m]> Yeah, those questions already have quite a history of going back and forth, it would be nice to make a breakthrough soon
<dangerousfreedom> <rbrunner7[m]> "dangerousfreedom[m]: I have..." <- Indeed. I was clarifying the work to be done as it is also clear to me now how exactly it should be. shalit[m] would you like to do that? Otherwise I would do it this week.
<dangerousfreedom> But for sure there are more tasks and unexplored fields to work on in the wallet too
<rbrunner7[m]> Also about my question about serializing transactions: https://github.com/seraphis-migration/wallet3/issues/7
<shalit[m]> dangerousfreedom[m]: > <@dangerousfreedom[m]:libera.chat> > <@rbrunner7[m]:libera.chat> dangerousfreedom[m]: I have basically only one question here: Did you coordinate with shalit in this matter? I mean, is this issue a "joint initiative" of the two of yours? I ask because what you wrote here Thursday sounded like you would put that job into their hands, and I think they understood it that way in fact.
<shalit[m]> > 
<shalit[m]> > Indeed. I was clarifying the work to be done as it is also clear to me now how exactly it should be. shalit[m] would you like to do that? Otherwise I would do it this week.
<shalit[m]> Yea! I would like to do that
<rbrunner7[m]> Nice that we have that cleared now. A little bit of project management, horray :)
<ghostway[m]> <rbrunner7[m]> "https://gist.github.com/tevador/..." <- That is what I used
<dangerousfreedom> Cool! Let me know if you have questions. You might need to use some modifications I did in the library too, so please consider using some of the codes in this [branch](https://github.com/DangerousFreedom1984/seraphis_lib/tree/keys_load/src/seraphis_wallet) (or you can fork it and start there)
<rbrunner7[m]> Maybe we could already start to do it "the right way", with PR'ing changes to our own repository?
<jberman[m]> +1
<rbrunner7[m]> Otherwise that can lead to confusion pretty quickly, I am afraid
<dangerousfreedom> Maybe a question for @vtnerd. When his serialization PR passes, will there any modification in using the library? 
<dangerousfreedom> For example the usual BEGIN_SERIALIZE()?
<dangerousfreedom> rbrunner7[m]: Would be nice
<rbrunner7[m]> I am quite sure that's another realm, not what we use now with "binary archive" or how it's called
<dangerousfreedom> I can make a minimum from what I have in the Transaction History
<dangerousfreedom> and then PR for your comments and approval
<rbrunner7[m]> Ok, looking ahead to this
<dangerousfreedom> Cool. Maybe we will start having something this week then :)
<rbrunner7[m]> The race is on for the first PR.
<rbrunner7[m]> Alright, we are past the hour, and probably at a good point. Thanks everybody for attending, and read you again next week at the latest!
<ghostway[m]> +1
````


# Action History
- Created by: rbrunner7 | 2023-05-26T16:48:46+00:00
- Closed at: 2023-05-29T19:16:41+00:00
