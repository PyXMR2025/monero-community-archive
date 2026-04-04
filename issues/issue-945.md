---
title: 'Seraphis wallet workgroup meeting #50 - Monday, 2023-12-18, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/945
author: rbrunner7
assignees: []
labels: []
created_at: '2023-12-15T15:52:20+00:00'
updated_at: '2023-12-18T18:56:28+00:00'
type: issue
status: closed
closed_at: '2023-12-18T18:56:27+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/942

# Discussion History
## rbrunner7 | 2023-12-18T18:56:28+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/945
<s​needlewoods_xmr> hey
<j​berman> howdy
<r​brunner7> Alright, anything to report from last week?
<s​needlewoods_xmr> I learned how to run two debuggers with different branches in parallel, which is a major workflow improvement for me
<s​needlewoods_xmr> added some more commits and get no more failing tests for https://github.com/seraphis-migration/monero/pull/16
<jberman> +1
<jeffro256> +1
<s​needlewoods_xmr> made this reference https://paste.debian.net/1301470/, it helped me visualize where all the ContextualEnoteRecords are coming from, if this could be useful for someone else, I can add it as a comment to my PR!?
<s​needlewoods_xmr> I think I found all relations between Basic/Intermediate/"Full", but couldn't find the point where Legacy will become Sp, yet.
<j​berman> Submitted a new CCS proposal, worked on getting monero-serai ready for audit (and found a rare edge case bug in monero's seed algo: https://github.com/monero-project/monero/issues/9089), and about to shift back over to Seraphis wallet work (the async scanner) in the next couple days
<s​needlewoods_xmr> afai understand it, to be able to finish my PR, I need to access `enote_same_amount_ledger_index`, that needs to be implemented in legacy scanning and will come along jberman  's PR https://github.com/UkoeHB/monero/pull/23 (the first bullet point under "Other TODO's for this PR"), is this correct?
<h​into.janaiyo> hello
<r​brunner7> Our wiki could be another possibility for that page in the paste
<r​brunner7> I mean here: https://github.com/seraphis-migration/strategy/wiki/Seraphis-Wallet-Workgroup
<s​needlewoods_xmr> If so, I'm relatively certain now, that I'll be able to finish my PR next year
<s​needlewoods_xmr> okay, I'll see if I can convert it to pretty markdown format
<j​berman> hm, doesn't have to be done in my PR, probably easier if do it in yours actually since you already have the types now
<v​alldrac> hi
<r​brunner7> If you miss some rights to start a wiki entry, just shout
<r​brunner7> Anything special to discuss today?
<s​needlewoods_xmr> I won't be able to do much for the remainder of this year
<s​needlewoods_xmr> it was a great time for me and I learned a lot since I joined, it's a pleasure being around such smart and helpful people, appreciate y'all
<r​brunner7> Well, not much year left.
<r​brunner7> I think we can drop next Monday's meeting, right?
<r​brunner7> Monero never sleeps, but it's Christmas after all
<s​needlewoods_xmr> I think so, too
<g​hostway> Hello, sorry for being late
<r​brunner7> > it was a great time for me and I learned a lot since I joined
<r​brunner7> I hope much more such time ahead :)
<j​berman> I'm ok with dropping next Monday meeting
<g​hostway> Any updates?
<g​hostway> Btw dangerousfreedom: about your comment, generate_chacha_key is using cn_slow_hash internally
<g​hostway> And I'm taking chacha_key for convenience, I don't want to take strings everywhere, the wallet implementation can implement that however they want
<r​brunner7> You are talking about the key container, right?
<g​hostway> Yep
<r​brunner7> Will have to check the state of that, just remember to have made some review comments ...
<j​effro256> Howdy
<g​hostway> Hello jeffro :)
<j​effro256> Hi ghostway how's it hanging
<g​hostway> A lot better than a month ago :)
<j​effro256> I'm working on editing the "Implementing Seraphis" document, then I'm going to review jberman'' background scan PR
<j​effro256> Thats good to hear !
<g​hostway> That's cool, any help needed?
<g​hostway> Yea I started reviewing it too like a month ago but then saw it wasn't finished
<j​effro256> I'm glad to see sneedlewoods is working their way thru the codebase and getting familiar with it
<k4r4b3y> +1
<jberman> +1
<sneedlewoods_xmr> +1
<r​brunner7> Indeed
<j​effro256> Ghostway: I think it should br ready noe
<j​effro256> Be ready now* (for review) right jberman?
<j​berman> ghostay, the background scan PR is referring to this PR which is ready: https://github.com/monero-project/monero/pull/8619
<j​berman> it's my Seraphis async scanner PR that's still a WIP
<j​effro256> Oh yeah Justin has a couple scanning PRs open at the moment
<g​hostway> Oh right, yea that's what I looked at
<r​brunner7> jeffro256: Any news already how might review your Jamtis enhancements? Not many people able to do so in the first place, I am afraid
<r​brunner7> *who might review
<r​brunner7> Maybe already went back to coding :)
<j​berman> once it's ready would be cool to have koe do a first pass review if he's available. I can review as well/will review
<i​nit00x> hii
<r​brunner7> I think it should be ready, but I might mis-remember
<r​brunner7> Alright, anything else? Last chance still this year then
<r​brunner7> Meeting-wise at least
<j​berman> ah fair, the "implementing seraphis" doc is just documentation. worth pinging koe I think jeffro256
<j​berman> SNeedlewoods: shall we discuss `enote_same_amount_ledger_index`? I think since your PR sets up the type, makes sense your PR would make the changes in the scanner to support it
<j​berman> or at least, your PR would be needed for those changes
<s​needlewoods_xmr> imo we can chat via DMs if you don't care?
<s​needlewoods_xmr> at the moment I don't have any questions prepared
<r​brunner7> Feel free you use DMs or this channel. It's not that you would disturb anybody, and maybe it's interesting to read along while you discuss.
<s​needlewoods_xmr> if you don't mind*
<r​brunner7> We had isssues in the past alread where people where *too* private in a certain sense
<j​effro256> Hopefully the Jamtis document changes will help with that
<j​effro256> Then you just have to make it follow the math
<j​effro256> Will do !
<s​needlewoods_xmr> okay will try to mainly use this channel then
<j​berman> whatever you prefer SNeedlewoods :)
<j​effro256> sneedlewoods, just a general design note: instead of creating free functions on variants to return a variant type that encloses all information you want, it might be cleaner to create free functions that return small concrete fields
<j​effro256> As it relates to the LegacyEnoteContext, instead of having enote records return a context variant, maybe instead have a function which just returns block Id or txid etc
<s​needlewoods_xmr> thank you, will look into that
<j​effro256> Depends tho, sometimes you want the variant
<j​effro256> Just a style thing at the end of the day. For example, there's functions to extract the amount commitment from output proposals, but not the whole enote , which is very useful for doing balance sanity checks
<r​brunner7> Ok then. Thanks everybody for attending. Read you again in the new year at the latest.
<nioCat> thanks to all working on Seraphis  
<nioCat> and a special thank you to koe
<s​needlewoods_xmr> thanks everyone, cu
<j​effro256> See y'all next year
<j​berman> happy holidays :)
<s​needlewoods_xmr> yeah, happy holidays!
````


# Action History
- Created by: rbrunner7 | 2023-12-15T15:52:20+00:00
- Closed at: 2023-12-18T18:56:27+00:00
