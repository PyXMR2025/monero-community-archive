---
title: 'Seraphis wallet workgroup meeting #25 - Monday, 2023-06-05, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/845
author: rbrunner7
assignees: []
labels: []
created_at: '2023-06-02T16:52:45+00:00'
updated_at: '2023-06-05T18:45:09+00:00'
type: issue
status: closed
closed_at: '2023-06-05T18:45:09+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #842

# Discussion History
## rbrunner7 | 2023-06-05T18:45:09+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/845
<Rucknium[m]> waves
<dangerousfreedom> Hello
<rbrunner7[m]> A somewhat modest meeting today as it seems ...
<rbrunner7[m]> Anyway, still something to report? Nothing from me this time.
<dangerousfreedom> Haha
<UkoeHB> Hi
<UkoeHB> Nothing from me
<dangerousfreedom> How far did you get with shalit in that interface that you both were trying to build?
<rbrunner7[m]> Who both?
<dangerousfreedom> You and shalit I guess
<rbrunner7[m]> Well, I support shalit when they have questions. But nothing on my own initiative, at least so far.
<rbrunner7[m]> In my understanding there is still a PR from your side to make, as a base for their work?
<rbrunner7[m]> At least that's my understanding from last week's meeting ...
<dangerousfreedom> I had an accident in my shoulder this week and havent been able to stay longer with my hands on the keyboard so I have been structuring my work this week actually. I believe I can make all the generation of the seraphis knowledge proofs just using the EnoteStore but I will have to use the node to do the same for the legacy proofs... so I have just made my TODO list more precise this week 
<dangerousfreedom> But yeah, I will make a PR for purposes of getting feedback this week
<rbrunner7[m]> +1
<dangerousfreedom> There is nothing ready so far but hopefully we will start a cycle of feedbacks/improvements
<dangerousfreedom> I will do it before Friday. Sorry.
<rbrunner7[m]> Isn't there some code that may be directly useful for what shalit is trying to implement? So the PR is for more than just review and merging?
<dangerousfreedom> The code is available on my branch, I sent here and also directly to shalit
<dangerousfreedom> He is using it for sure
<jberman[m]> hello, nothing from me either (was working on serai this past week).  After last week's discussions, I'm planning on trying out using libcurl in the async wallet scanner to get a feel for it as a substitution for the epee http client library. Timeboxing that to a couple hours of work
<rbrunner7[m]> Yeah, and that's not the way this should work, ideally ... frankly, with such criss-crossing of code we will have a mess in no time.
<rbrunner7[m]> Same argument as in last week's meeting, I know, I repeat myself.
<rbrunner7[m]> Or is the idea that shalit will PR that, not you?
<dangerousfreedom> He will eventualy PR the serialization of the EnoteStore at some point I hope
<rbrunner7[m]> With your code parts included then?
<rbrunner7[m]> As part of their PR I mean
<dangerousfreedom> But there will be endless clean up PRs I'm sure. So I will try to make the most basic until Friday and then we will see.
<rbrunner7[m]> Ok. I hope PR cleanup won't acutally be endless :)
<ghostway[m]> hello! sorry for being late, my key container, apart from tests, is done (I can't compile because of some weird stuff going on with dependencies and updates). expect a pr in the coming weeks
<Rucknium[m]> +1
<dangerousfreedom> rbrunner7[m]: Why would he do that? I will do it soon
<dangerousfreedom> ghostway[m]: Nice! But something to show or discuss so far?
<rbrunner7[m]> ghostway: You could consider a "Do not merge" PR at some earlier point, so people could have a first look and impression.
<rbrunner7[m]> I think right now we have non-zero chances that people wander into directions that make other people wonder what the heck is that, if you know what I mean
<ghostway[m]> yes, there is. what do you think about a KeyGuard (something like lock_guard), that unlocks the keys and, by reference, increases/decreases references and when it reaches 0, it locks the keys again?
<ghostway[m]> I'll make a draft pr in the coming days, anyway
<rbrunner7[m]> Out of fundamental misunderstanding, for example
<rbrunner7[m]> I never studied locking in detail in wallet2, maybe jberman or jeffro256 know details
<ghostway[m]> I already have written it, but it could be moot, considering you can just use references (which, with my familiarity with koe, seraphis is exclusively using them in this case)
<ghostway[m]> apparently wallet2 has that already, and is using that
<rbrunner7[m]> If we can have a first look at the code, maybe things will get a lot clearer
<jberman[m]> yep this is what wallet2 does here: https://github.com/monero-project/monero/blob/94e67bf96bbc010241f29ada6abc89f49a81759c/src/wallet/wallet2.cpp#L1063-L1115
<ghostway[m]> yep
<rbrunner7[m]> Yeah, but with some strange user interactivity thrown it, which maybe you can hardly generalize, no?
<ghostway[m]> can you rephrase?
<rbrunner7[m]> Ah, maybe I misread, this here is merely a variable access, not a call, right: tools::wallet2::AskPasswordToDecrypt
<rbrunner7[m]> So no sudden asking the user interactively for the password from deep inside wallet2
<ghostway[m]> yea. the key is passed to it
<rbrunner7[m]> Good
<rbrunner7[m]> Anything else to discuss right in this meeting?
<dangerousfreedom> Not from me.
<rbrunner7[m]> Btw, I see more and more references to Seraphis on the Monero subreddit. I am just not sure whether people are aware how far out the hardfork to Seraphis still is. But nice to see that we "got their attention" :)
<ghostway[m]> btw I don't really like the use of static there in wallet2 (unless we are sure there are no multiple threads, and then why would we want to use that mutex), but I also don't really like to pass a reference/pointer to the chacha_key multiple times, unless it doesn't allocate on copy. can you confirm?
<rbrunner7[m]> I am not the best with C++, but can't you avoid any copies with const&?
<rbrunner7[m]> At least that's what I always assumed when coding ...
<ghostway[m]> true, that was my first version, but it could look better
<ghostway[m]> I guess it's always good to be explicit. consider my question answered I guess
<rbrunner7[m]> Not sure what you mean, but maybe just let us have a look if you are ready
<rbrunner7[m]> Alright, thanks for attending, read you again next week at the latest.
<plowsof11[m]> +1
<ghostway[m]> +1
<dangerousfreedom> Thanks
````


# Action History
- Created by: rbrunner7 | 2023-06-02T16:52:45+00:00
- Closed at: 2023-06-05T18:45:09+00:00
