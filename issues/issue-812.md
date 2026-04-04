---
title: 'Seraphis wallet workgroup meeting #17 - Monday, 2023-03-20, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/812
author: rbrunner7
assignees: []
labels: []
created_at: '2023-03-17T15:56:17+00:00'
updated_at: '2023-03-20T18:49:16+00:00'
type: issue
status: closed
closed_at: '2023-03-20T18:49:15+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #809

We could discuss how to really start to use our own wallet implementation GitHub repository. I think we must be pretty close and maybe only need some quick decisions how to name folders for the wallet code.


# Discussion History
## rbrunner7 | 2023-03-19T13:56:32+00:00
Here a bit more info about the repository in question:

We had some discussions about this in early workgroup meetings, and the result from those is the following GitHub repository that I prepared quite a while ago already: https://github.com/seraphis-migration/monero

It's a fork of @UkoeHB's fork of Monero's repository where he develops his Seraphis library, which is this, with the branch in question displayed: https://github.com/UkoeHB/monero/tree/seraphis_lib

Our repository has a branch *seraphis_wallet*, and my proposal is to develop the Seraphis wallet on this branch, while periodically updating the Seraphis library from koe's branch: https://github.com/seraphis-migration/monero/tree/seraphis_wallet

We never talked in detail, as far as I remember, how changes in the Monero main repo will reach our repo. Maybe not directly, but by way of koe's repo.

Nothing interesting happened yet there. I just updated both the *seraphis_lib* and the *seraphis_wallet* branch to the latest commits from koe.

## rbrunner7 | 2023-03-20T18:49:15+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/812
<ghostway[m]> Hello!
<plowsof11> hi
<Rucknium[m]> Hi
<dangerousfreedom> Hello
<woodser[m]> hello
<UkoeHB> hi
<rbrunner7[m]> Anything to report? jberman can't make it for the meeting and left some info before the meeting, hope everybody has a means to read up
<rbrunner7[m]> In short, he is still refining scanning
<UkoeHB> I did some refactoring/updates to scanning to enable some speedups that jberman[m] wants
<UkoeHB> this week I plan to integrate the checkpoint cache into the enote store + update scanning to support it
<rbrunner7[m]> I had a longer session with shalit to look at the "variant with visitors" approach to bring the different transaction classes under a single roof. Doesn't look too bad, but it's pretty sure we need an angle to get serialization working with that approach, it won't work just "out of the box"
<UkoeHB> also had an idea about key management: don’t store keys in wallet, store keys in password-encrypted tool, then decrypt keys and pass them into wallet methods (also store wallet in password-locked tool)
<dangerousfreedom> I have been thinking about the basic functions and structures of the transaction_history but have nothing to show. Probably next meeting I will have some results to discuss about.
<rbrunner7[m]> shalit will be away for 3 weeks or so, but I don't think that will hold up something elese
<rbrunner7[m]> *else
<rbrunner7[m]> UkoeHB: With "tool" you mean just a separate code component, not literally a tool I assume?
<UkoeHB> yes
<rbrunner7[m]> In the interest of re-use?
<UkoeHB> right now wallet2 has a lot of spaghetti involved with password management, it would be nice to pull that out
<rbrunner7[m]> Yeah, why not :)
<plowsof11> pinging Josh Babb for an update (peer pressure) on https://bounties.monero.social/posts/75/6-422m-blake2b-c-dev-challenge-seraphis 
<dangerousfreedom> UkoeHB: So basically you propose to store two different things, the keys and the wallet_info ? Because right now they are all stored together and when you put your password you get it all.
<UkoeHB> yes
<dangerousfreedom> Ok, that could lead to two different types of passwords too. One very safe for the keys and one for wallet files... anyway this creates a lot of possibilities
<UkoeHB> I don't have a concrete idea for it, just as a design goal aim for password stuff to not be strewn across the wallet
<rbrunner7[m]> Shows again how many design loose ends we still have ... Alright, as you can read in the meeting announcement, I thought it might be time to the question of starting with our repository. dangerousfreedom[m] also mentioned some similar thought lately somewhere.
<dangerousfreedom> I like the idea, was just going further on thought. It opens many other questions too.
<rbrunner7[m]> As I see it, maybe we need nothing more than finally nailing some questions of structure, of folders and their names where to put code
<dangerousfreedom> Yeah, I think it is a good idea to start our repo. Now more people could concretely use the seraphis_lib and it will have to be more and more stable with time to not break the wallet.
<rbrunner7[m]> Status quo is decribed here, as mentioned yesterday: https://github.com/monero-project/meta/issues/812#issuecomment-1475267890
<woodser[m]> <rbrunner7[m]> "I had a longer session with..." <- maybe I'm missing some context, but each data model can implement a serializable type which serializes using e.g. rapidjson from the main code base. that's how [these](https://github.com/j-berman/monero-cpp/blob/98b9c2b4be0fb29e2e6e17fe33272b02b80a89a2/src/daemon/monero_daemon_model.h#L170) models are serialized now; it's been nice to consolidate all
<woodser[m]> serialization/deserialization using methods right on the models
<rbrunner7[m]> Can we quickly confirm the proposed handling model we came up in some early meeting last year? Koe's fork of Monero is our source, i.e. we are a fork of his Monero fork, and for wallet development we have our own branch?
<UkoeHB> rbrunner7[m]: yes that should be fine
<dangerousfreedom> I would say that we keep doing the wallet stuff in your fork of the seraphis_lib . I would say it is easier to update but it also works like that.
<rbrunner7[m]> Yes, it's one step more, but with a clearer separation of responsibilities.
<dangerousfreedom> (just naming basically)
<dangerousfreedom> Ok
<rbrunner7[m]> So, seems to me, if we can agree on some folders to put our wallet "stuff" into, we should be read to go. Or maybe a single folder.
<rbrunner7[m]> Obvious proposal seems to be seraphis_wallet
<dangerousfreedom> Yeah, so it should be at src/ . So you name it :p
<rbrunner7[m]> The other idea would be *wallet3*, but then it's less clear that it belongs to the Seraphis "family" of modules / parts.
<rbrunner7[m]> And yes, I think a top-level folder is in order, not some sub-folder in /wallet
<rbrunner7[m]> Beside, koe got already several, I also want one :)
<rbrunner7[m]> No, seriously, how does that sound?
<UkoeHB> seraphis_wallet should be fine, can rename as needed
<ghostway[m]> ^
<rbrunner7[m]> Yes, should be no problem as long as we are basically alone working on that. And also introducing sub-folders as soon as we overflow with files
<rbrunner7[m]> Does git allow to make a commit that merely adds an empty folder?
<UkoeHB> no
<ghostway[m]> .git_keep should do it
<ghostway[m]> .gitkeep
<rbrunner7[m]> Well, of course the first person to actually submit something can as well make that folder, so no git magic is needed
<UkoeHB> better not to have git cruft hanging around, just add a folder when it's needed
<rbrunner7[m]> So yeah, the repository is officially open for business, bring on those PRs
<dangerousfreedom> Maybe ghostway[m] could look at the basic structure of how the simplest wallet could look like?
<dangerousfreedom> If you have time
<ghostway[m]> Sure. First I'll finish rbrunner's wishes (I'll start on Thursday) and then I'll be free probably
<rbrunner7[m]> Er, well, proposals, not wishes ...
<ghostway[m]> Lol
<rbrunner7[m]> I was thinking about the general approach of merging / accepting code. Maybe for starting we should, in the spirit of some "rapid prototyping", not put the bar terribly high. We will constantly rework many things anyway.
<rbrunner7[m]> But that's easier if you have at least something before your eyes.
<rbrunner7[m]> At least it's like that for me.
<rbrunner7[m]> It might be different for the Seraphis library, which does, and which also can, already strife for production qualitiy
<ghostway[m]> I really don't think policies have to be in place. It will only slow down stuff. Check the thing actually does what it's supposed to, passes tests and maybe adds new ones when appropriate
<rbrunner7[m]> Yes. I will be content with a loose consensus of broad direction :)
<ghostway[m]> Lol
<rbrunner7[m]> But as nobody seems to oppose right now, we may start with that and see where it leads us.
<rbrunner7[m]> Anything else for today?
<dangerousfreedom> I can trim down even more my basic wallet so it would have only a terminal showing a hello message and an empty "help" command.
<dangerousfreedom> If useful
<dangerousfreedom> rbrunner7[m]: Not from my side
<rbrunner7[m]> Hmm. Not sure.
<rbrunner7[m]> Hard to say
<rbrunner7[m]> At least I don't feel any pressure there. If you have to try out something interactively, maybe it's not too hard to whip up some working frame to "see something". I gues jberman does such things for his scanning.
<UkoeHB> Only commit low quality code if you are committed to spending hours and hours in the future updating it to production quality.
<UkoeHB> keep in mind that a lot of what goes into a wallet is security-critical
<ghostway[m]> Yes, of course. Not shit code, that is unreadable. Just something that can be changed easily and understood easily
<rbrunner7[m]> I wasn't exactly thinking about low-quality code. But about code that for example does not yet handle all corner cases in some module, just the "basic" stuff yet, the low-hanging fruits.
<rbrunner7[m]> Because maybe we will throw away the component wholesale after somebody looks at it and has a much better idea
<rbrunner7[m]> Iterative programming? I am sure somebody once gave a name to that basic idea.
<rbrunner7[m]> We will see. Review will be team-work anyway, at least I hope so.
<rbrunner7[m]> Alright, thanks for attending. Until next week!
<dangerousfreedom> I was thinking about the functions to get the terminal working. I believe we could use very similar functions from those from wallet2. We dont need to reinvent the wheel here. Though we can. But could be a good beginning.
<dangerousfreedom> rbrunner7[m]: Have a good week.
<rbrunner7[m]> woodser: Those transaction class questions were discussed in last week's meeting. You may find some pointers there about the approaches.
<rbrunner7[m]> It's basically a "wrapper class holding the transaction objects in a variant" versus "naked variant that directly already contains the transaction objects, plus visitors"
````


# Action History
- Created by: rbrunner7 | 2023-03-17T15:56:17+00:00
- Closed at: 2023-03-20T18:49:15+00:00
