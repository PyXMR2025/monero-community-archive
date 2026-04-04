---
title: 'Seraphis wallet workgroup meeting #55 - Monday, 2024-01-29, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/960
author: rbrunner7
assignees: []
labels: []
created_at: '2024-01-26T19:12:30+00:00'
updated_at: '2024-01-29T18:44:00+00:00'
type: issue
status: closed
closed_at: '2024-01-29T18:44:00+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/958

# Discussion History
## rbrunner7 | 2024-01-29T18:44:00+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/960
<s​needlewoods_xmr> hello
<d​angerousfreedom> Hello
<Douglas_McSqueak> Hello (lurking)
<r​brunner7> January almost over already :) What is there to report from last week?
<d​angerousfreedom> This week I was thinking about how to load the keys from a wallet2 and a sp keys file. So far I believe the best way will be using jeffro's lib to load the keys and once it is loaded we only use the functions that we will create for the seraphis wallet and we forget about the wallet2.cpp. I will probably have something to show by next week.
<sneedlewoods_xmr> +1
<s​needlewoods_xmr> no work directly on seraphis, but went studying some of the basics of general cryptography
<r​brunner7> dangerousfreedom: Sounds like a good approach
<s​needlewoods_xmr> I plan to look into this issue https://github.com/UkoeHB/monero/issues/27
<s​needlewoods_xmr> maybe could pick that up as my next task
<dangerousfreedom> +1
<r​brunner7> We didn't hear from jeffro256 here in the meeting for a while, but anyway, he left an interesting report on GitLab today: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/421#note_23289
<r​brunner7> SNeedlewoods: Sure, try your luck.
<r​brunner7> Worst case is probably that you will find that this goes over your head, and such a worst case isn't too terrible :)
<s​needlewoods_xmr> at worst I'm learning something
<r​brunner7> Exactly. Your case seems to show anyway that it's not exactly easy to start with Monero dev work, but it definitely can be done.
<j​effro256> Hi sorry I'm here
<r​brunner7> Ah, hello
<j​effro256> Thanks for the ping
<r​brunner7> Just curious, where do you stand with "Personal Wallet3 Design Research" right now?
<r​brunner7> I guess that's like juggling with quite a number of balls up in the air at the same time
<j​effro256> That was supposed to be my main focus this month, but I got a little distracted by PR 9135 since it was requested by quite a few people. Also reviewed jberman's big ol background sync PR
<r​brunner7> Well, that PR 9135 was a nice distraction. Sounds quite promising, this optimisation
<j​effro256> Reviewing that background PR actually helped me generalize in my mind what the Wallet internal design might look like a lot
<g​hostway> How so?
<r​brunner7> Interesting
<j​effro256> Well for one, it made me look into making the enote stores "composable", which they already are to a certain degree
<g​hostway> I like that pr a lot!
<j​effro256> The design Justin used for the background sync was probably the easiest refactoring involving the fewest new lines of code, but if we plan to do this ahead of time, it would be worth putting a little work into making the enote stores be able to combine their contents with ease and plenty of sanity checks
<j​effro256> Also, depending on how well we did this , we might not have to write special transport code specifically for payment handling and find received tiers if we could transmit their contents as a composable enote store
<r​brunner7> Sounds promising. It does have advantages if you can start out on a green field, certainly.
<g​hostway> What do you mean by compostable exactly?
<j​effro256> Being able to combine their contents in a way that makes sense and is modular
<g​hostway> Ok just wanted to make sure
<g​hostway> Sounds cool. If it's using the thing I wrote a while back (with... 80% rewritten by koe), then it should be fine
<r​brunner7> Fine speedwise mostly?
<g​hostway> Yes, it's sorted so should take nlogn
<g​hostway> Assuming ~same size of course
<g​hostway> If not same size then it's really just logn which sounds okay
<g​hostway> Oh wait, I wrote the block one; not the transaction one
<g​hostway> Sorry, nothing I said is much relevant
<r​brunner7> No problem! Anything special to discuss today? I saw earlier today jeffro256 ventured a rough estimate of having a Seraphis testnet running end of this year. Comments?
<k4r4b3y> looking
<r​brunner7> I think with a bit of luck that sound doable.
<r​brunner7> People then will probably underestimate how much it still takes to move from testnet to hardfork, but alas ...
<j​effro256> I feel like that's a doable target right? It might make sense to set a target like that even if we don't hit it so there's some sense of urgency
<<k4r4b3y> +1
<dangerousfreedom> +1
<r​brunner7> I agree. Good to have something to look forward to also.
<d​angerousfreedom> I agree and look forward to see someone working on writing things on a proto blockchain instead of having it in memory
<j​effro256> I some experience with modifying/working with the LMDB code in the codebase. Anyone else ?
<d​angerousfreedom> That's great jeffro256  :D
<r​brunner7> I always thought that stuff looks mighty strage and shied away
<r​brunner7> *strange
<j​effro256> The LMDB API can be very intimidating at times
<d​angerousfreedom> I would like to learn and help also. Let's see how things go
<j​effro256> best thing you can do to learn is to 1) understand what the methods of BlockchainLMDB are meant to acheive and then 2) study how that class uses LMDB to accomplish that
<dangerousfreedom> +1
<j​effro256> Theres a lot of common patterns used
<j​effro256> Then you can get a feel for how the cursors work
<j​effro256> And which flags mean what
<r​brunner7> Yeah, sometimes you just have to grok the overall approach, and then pieces fall into place
<j​effro256> Also if youre really stumped on something @hyc is the most knowledgeable person here about that
<r​brunner7> Just don't start to compare LMDB with other systems :)
<jeffro256> smile
<r​brunner7> (just joking, he sure knows his stuff)
<r​brunner7> Alright, anything else for today?
<r​brunner7> Doesn't look like it. I think we can close. Thanks for attending everybody. Read you again next week!
<<k4r4b3y> +1
<d​angerousfreedom> Thank you rbrunner7
<s​needlewoods_xmr> thanks everyone, bye
````


# Action History
- Created by: rbrunner7 | 2024-01-26T19:12:30+00:00
- Closed at: 2024-01-29T18:44:00+00:00
