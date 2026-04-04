---
title: 'Monero Tech Meeting #108 - Monday, 2025-02-17, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1157
author: rbrunner7
assignees: []
labels: []
created_at: '2025-02-16T18:06:33+00:00'
updated_at: '2025-02-17T18:36:12+00:00'
type: issue
status: closed
closed_at: '2025-02-17T18:36:10+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1153).

# Discussion History
## rbrunner7 | 2025-02-17T18:36:10+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1157
<j​berman> *waves*
<s​needlewoods> hi
<s​yntheticbird> hi
<j​effro256> Howdy
<r​brunner7> So, what are the reports from last week?
<r​brunner7> With some friendly support from jeffro256 I made this post: https://old.reddit.com/r/Monero/comments/1iph8fz/more_vitamins_for_monero_with_carrot_part_1/
<jeffro256> +1
<r​brunner7> It was well received, I think people do have interest in what happens in Monero development
<s​needlewoods> very nice write-up
<j​berman> yes thank you for that!
<r​brunner7> Welcome! It was a pleasure to write, but took some time
<j​berman> me: the FCMP++ competition is nearly ready for review, solved an issue with the wasm-cycles crate which caused inconsistent wasm cycle counts for ec-divisors (https://github.com/kayabaNerve/wasm-cycles/issues/1), and separately made some progress on getting the sum of inputs == sum of outputs for FCMP++. Last thing to do for the FCMP++ competition is to finalize how to score helio<clipped messag
<j​berman> selene benchmarks (since there are various ops with varying execution times)
<j​effro256> me: debugging release issues :(
<rbrunner7> +1
<syntheticbird> +1
<jberman> +1
<jberman> +1
<j​berman> what issues?
<s​yntheticbird> nuclear issues according to PR title
<j​berman> agh
<j​effro256> That windows PR plus an issue with release-v0.18 playing with xmrblocks. Can't figure out which is the problem, but it seems to work with v0.18.3.4, but crashes every few hours due to stale readers with latest release branch
<r​brunner7> It's only now that background sync goes into release, did I see this correctly in a quick glance?
<j​effro256> `xmrblocks` has a lot of memory issues and leaks but I can't run it with valgrind ....
<j​effro256> Yes AFAICT
<s​yntheticbird> jeffro256: tried heaptrack ?
<r​brunner7> What is "xmrblocks"?
<s​yntheticbird> it worked well for me on an lmdb powered software
<jeffro256> +1
<j​effro256> The xmrchain.net block explorer
<j​effro256> Okay I'll try this, thanks so much
<s​yntheticbird> np
<s​needlewoods> I've spent some time with a debugger observing memory. Initially my hope was to wipe the password from passwordDialog, after it fulfilled it's purpose, with something like `passwordDialog.password = "";` (ideally would use zero bytes for the length of the password I guess), but unfortunately that just seems to create a new string and leaves the old one in memory. It's not that eas<clipped m
<s​needlewoods> y to debug, because we use .cpp, .qml and .js files and I'm still learning about QT.
<r​brunner7> You slowly drift towards "hardcore hacker" :)
<sneedlewoods> +1
<j​effro256> mmmmmmmm we love memory tracing
<j​berman> If there's a way to use the wipeable_string type as the underlying type, and pass a pointer to that type around higher up the stack, might have some luck with that approach
<jeffro256> +1
<j​effro256> Will QT let you do that?
<s​needlewoods> Not sure that's possible in a .qml file
<r​brunner7> It also might be that somewhere, somehow QT itself offers something in this regard, problem might be to locate the feature
<s​needlewoods> also tried to find something in that regard
<j​berman> QT lets you at least interact with C++ types in some capacity, so maybe some interface wrapper for wipeable string might be possible, idk
<s​needlewoods> will look into it, thanks for the input
<r​brunner7> The use of the repository over at the Seraphis migration org is now ok, after everybody has the necessary rights?
<j​berman> Haven't used it yet. I'm planning on re-reviewing then rebasing on top of 9135 this week, so figure that would be a good time to switch over to developing in the Seraphis migration repo
<r​brunner7> Ok
<j​effro256> Yeah the fcmp++stage branch is already rebased on #9135
<j​effro256> * fcmp++-stage
<j​berman> (referring to what I have in my local right now for FCMP++ validation)
<j​effro256> Just thought I'd bring it up b/c it would make rebasing for prototyping easy
<r​brunner7> Alright. Anything to discuss today beyond these reports?
<r​brunner7> Doesn't look like it. So it's already back to work I guess, thanks everybody for atttending, read you again next week!
<s​needlewoods> Thank you, I'll maybe make a PR to monero-gui in the next couple days, will let you know here
````


# Action History
- Created by: rbrunner7 | 2025-02-16T18:06:33+00:00
- Closed at: 2025-02-17T18:36:10+00:00
