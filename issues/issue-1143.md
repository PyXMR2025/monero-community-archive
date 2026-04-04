---
title: 'Monero Tech Meeting #104 - Monday, 2025-01-20, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1143
author: rbrunner7
assignees: []
labels: []
created_at: '2025-01-17T15:30:08+00:00'
updated_at: '2025-01-20T18:48:59+00:00'
type: issue
status: closed
closed_at: '2025-01-20T18:48:58+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1139).

# Discussion History
## rbrunner7 | 2025-01-20T18:48:58+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues
<s​yntheticbird> hi
<j​berman> *waves*
<r​brunner7> Alright, maybe some more people will join in a bit, but let's start with reports anyway
<s​needlewoods> hi
<s​needlewoods> Was thinking about what I could do next and came up with:
<s​needlewoods> Start removing wallet2 from a) CLI and b) RPC wallet and make them use the Wallet API instead, as described in step 2 in [this proposal](https://github.com/seraphis-migration/wallet3/issues/64) by jberman.
<j​berman> me: implemented separate prove and verify functions over the FFI that can be called from the C++, rebased onto master and got CI builds passing (with @tobtoht's help), did some clean-up tasks. Planning to update the WIP PR with the latest then start on next steps for the proposed contest to optimize crypto arithmetic
<sneedlewoods> +1
<r​brunner7> SNeedlewoods: In any case you won't get any better testing for your improved and enlarged Wallet API than actually using it for the CLI wallet.
<r​brunner7> jberman, what do you think about this next step? It was the idea to use the Wallet API in this way, but maybe some doubts crept in, or maybe wait for some reason?
<s​needlewoods> The tests I wrote so far (scattered over multiple branches) helped here and there with the Wallet API, but are not closely complete enough to be considered a good starting point I think, could share the most recent one though in case anyone wants to take a look.
<s​needlewoods> I hope to improve the tests along working on the CLI
<r​brunner7> How is the current state of the PR regarding a possible review?
<s​needlewoods> This one  https://github.com/monero-project/monero/pull/9464 !? It's ready to review as far as I can judge
<r​brunner7> Yes, that one
<j​berman> I think it's a solid next step and makes sense for SNeedlewoods  to take on with their experience working with the wallet API already. I originally thought it might make more sense to start with step 1 (replace wallet2 with the Seraphis lib in the wallet API first), but it doesn't make a huge difference which to start with. It makes more sense for @sneedlewoods in particular to st<clipped messag
<j​berman> art with step 2 beacause they've worked with the wallet API at length already
<r​brunner7> Do we have to fear complications if you have to make some new calls in wallet2 for the FCMP++ stuff?
<j​berman> Potentially, but I think they will be minimal / relatively insignificant compared to the overall task
<rbrunner7> +1
<r​brunner7> I think SNeedlewoods currently would have a hard time working with the Seraphis lib ...
<s​needlewoods> I think so too, it's been a while and I only looked at small parts of it
<j​berman> credit to SNeedlewoods for taking initiative, thank you SNeedlewoods
<r​brunner7> Ok, that sounds like a "go" if you are ready to take on the CLI wallet. It's quite some mass of code. I might be able to help a bit along the way if questions arise.
<s​needlewoods> No problem, I'll give it a try
<r​brunner7> Splendid
<s​needlewoods> btw I'm planning to write another CCS proposal covering 2 months of work
<r​brunner7> I guess jeffro256 is still deep into his Carrot work
<r​brunner7> SNeedlewoods: That sounds reasonable to me.
<j​berman> +1
<r​brunner7> By the way, maybe you saw it, I found this quite interesting - from over in the Monero Community Workgroup room: https://gist.github.com/plowsof/0401c4823b842580cd0cb1d27b380150
<s​needlewoods> I assume this job will take longer, but I'll probably won't have enough time to spend in April and May that would justify to include them
<r​brunner7> It's amazing, if you add all the amounts spent, you still have a quite modest total, if you think how fast Monero can move forward
<s​needlewoods> my initial thought was Rucknium deserves a raise
<r​brunner7> Yeah
<r​brunner7> Ok then, if we are through with the reports, anything to discuss today beyond those?
<s​needlewoods> Not from me
<j​berman> nothing from me either
<s​yntheticbird> Question for the future, after FCMP++ is merged in mainnet and dev effort stabilize, could we expect a good fully fledged documentation of FCMP++ and Consensus?
<r​brunner7> Good question
<j​berman> Thoughts on the level of documentation in the WIP PR so far?
<r​brunner7> Have to confess that I did not yet look into it ...
<j​berman> My plan was for that documentation to cover my portion, could be ported to another place that can be updated in the future
<s​needlewoods> for the record https://github.com/monero-project/monero/pull/9436
<r​brunner7> Whoa, 127 commits :)
<j​berman> I have more commits incoming haha
<s​needlewoods> I have to admit I still understand way to little to judge
<s​yntheticbird> I haven't looked into it too, thx for remind jberman
<r​brunner7> In any case, I never saw such a long PR description
<r​brunner7> Looks promising to go through at least once
<s​yntheticbird> This is a good documentation indeed
<r​brunner7> Documentations *is* one of the weak points in the Monero core software so far, every little bit of improvement probably helps
<r​brunner7> Not everybody is fluent in C++ :)
<s​yntheticbird> I'm proposing consensus as top priority to document because this would permit to make audits of consensus for Cuprate easier.
<s​yntheticbird> If it eventually happens
<r​brunner7> I see. Makes sense.
<j​berman> ah you mean a general all-encompassing documentation on all of consensus
<s​yntheticbird> jberman: yes
<s​yntheticbird> boog did document a major part in a cuprate book but only relevant parts
<s​yntheticbird> boog did document a major part in a cuprate book but only relevant for Cuprate
<r​brunner7> Let's hope that Cuprate will reach production-ready state! I was very sceptical about the chances of this project once, but people pull through so far quite nicely.
<r​brunner7> It helps if you have people that just refuse to give up :)
<syntheticbird> +1
<j​berman> I think complete documentation of consensus would be excellent to have
<s​yntheticbird> Boog900's book: https://monero-book.cuprate.org/INTRO.html
<jberman> +1
<sneedlewoods> +1
<r​brunner7> Interesting, first time I learn about that
<s​yntheticbird> You should hang out more often in #cuprate channel
<r​brunner7> Oh, so many channels, so little time :)
<r​brunner7> I think this should be made known to a broader audience soon
<s​yntheticbird> don't remind me
<s​yntheticbird> It's been months I want to make some basic public relation
<s​yntheticbird> old reddit people have probably forgot about it
<r​brunner7> Yes, the Cuprate project is pretty much flying under the radar so far
<s​yntheticbird> hinto have is preparing a roadmap regarding communication, it still needs to be discussed.
<r​brunner7> Is it already possible to contribute to that book, or is it currently a one-person show?
<b​oog900> it's possible here it is: https://github.com/Cuprate/cuprate/tree/main/books/protocol
<s​yntheticbird> The book is located here: https://github.com/Cuprate/cuprate/tree/main/books/protocol
<s​yntheticbird> ah yes
<s​yntheticbird> too slow
<r​brunner7> Thanks for the info
<r​brunner7> Many "TIL" in this meeting, nice
<s​yntheticbird> fwiw the book is based upon monerod code so a few review and it could be considered canonical documentation
<r​brunner7> So, in the absolute worst case Cuprate may never reach production, but we will have that documentation
<s​yntheticbird> not only the documentation, the crates are also being used in other monero app. The RPC definition are used by someone else i don't remember for a WASM project.
<s​yntheticbird> the spy node detection software is based upon cuprate stack
<r​brunner7> Alright. I think we can close the meeting proper here. Thanks everybody for attending, read you again next week!
<s​yntheticbird> thanks
<s​needlewoods> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2025-01-17T15:30:08+00:00
- Closed at: 2025-01-20T18:48:58+00:00
