---
title: 'Seraphis wallet workgroup meeting #39 - Monday, 2023-10-02, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/902
author: rbrunner7
assignees: []
labels: []
created_at: '2023-09-29T16:33:45+00:00'
updated_at: '2023-10-02T18:37:15+00:00'
type: issue
status: closed
closed_at: '2023-10-02T18:37:14+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/898

# Discussion History
## rbrunner7 | 2023-10-02T18:37:14+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/902
<d​angerousfreedom> Hello
<j​berman> hello
<r​brunner7> So ... anything to report from last week? Not much from me, except that finally there was something to merge :)
<d​angerousfreedom> Nice :)
<d​angerousfreedom> Last week I started implementing some ideas for the interface of the two different transaction classes and was learning more about functional tests and debugging (thank you for those that I bothered who helped me during the week). I will probably have something to show by next meeting.
<r​brunner7> Sounds interesting
<r​brunner7> I guess jberman did not yet return to wallet work ...
<j​berman> nothing Seraphis related, but the background sync PR high level approach is ready for review (and separately did a bit of decoy selection algo cleanup for the rust monero-serai wallet lib), moving back to Seraphis wallet lib work this week (planning to continue exploring libcurl some more for the async scanner, then would like to get started on fcmp's)
<r​brunner7> Yup, left my review to that yesterday.
<r​brunner7> Anytime we add some functionality to `wallet2` still, I say to myself, splendid, now we will have to add *that* to wallet3 as well :)
<j​berman> ah missed that, thank you!
<j​berman> heh, agree :) this is also part of why I'm pretty happy saying/hoping it's the last major piece of functionality I want to work on for wallet3 and move forwards on wallet3
<r​brunner7> Do you think that something PR'able will result shortly from all your scanner work?
<j​berman> yes
<plowsof> +1
<r​brunner7> Fine, looking forward to have a good look at the code
<r​brunner7> Will also serve as good demo code how to use the Seraphis library, I guess
<d​angerousfreedom> Yes! Looking forward to that too! The work on the wallet is getting more and more entangled
<j​berman> *last major piece of functionality I want to work on for wallet3 (sorry)
<j​berman> wallet2* yeesh
<r​brunner7> I am waiting for a reaction of jeffro256 to a comment I left on this wallet reading PR, it's not yet reading wallets in ASCII. Maybe leave that for later, but I think it's up to him.
<r​brunner7> (You can arrange to have the .keys file written in ASCII)
<r​brunner7> But apart from that, IMHO, it's ready for merging.
<dangerousfreedom> +1
<r​brunner7> Anything to discuss today?
<g​hostway> Hello, still idle. Anything interesting?
<r​brunner7> Well, define "interesting" :)
<r​brunner7> Not much comes to my mind right now, but I remember that non-mock class for the keys. I wrote an issue about that.
<d​angerousfreedom> Not much from my side today.
<r​brunner7> https://github.com/seraphis-migration/wallet3/issues/61
<g​hostway> I don't know
<g​hostway> I have read the jamtis section in implementing seraphis, and it's well written (thanks koe and jeffro!). Any interesting problems you're trying to solve jeffro256?
<r​brunner7> I am still waiting for word from shalit what will happen with their work of making the enote store serializable.
<r​brunner7> I think last was they wanted to check how they left that job a while ago, and what was the holdup.
<r​brunner7> But I don't have an overview, maybe there are other Seraphis library classes that wait to become serializable?
<r​brunner7> But well, that's probably some pretty boring stuff, depending on how you look at it :)
<g​hostway> I see 
<g​hostway> I don't know
<g​hostway> Just searching for problems to think about at night :)
<r​brunner7> Ok :)
<r​brunner7> @Tevador and jeffro256 pretty much discuss the Jamtis and view tag modifications among themselves. Could probably do no harm if somebody else takes a look, in the sense of some "outside opinion".
<r​brunner7> And I think there are quite interesting problems to be had
<d​angerousfreedom> I think he did quite a lot of progress with that but then he was blocked as I said to not modify the seraphis_lib but it is impossible to do it without modifying it. I will pick up where he left if he doesnt want to continue.
<g​hostway> They are doing really cool stuff, but I also don't want to disrupt them, as, well, I'm certainly not a cryptographer
<r​brunner7> Not even at night?
<r​brunner7> Some of their discussions are about trade-offs, I saw, where probably mere mortals could go into the question and form an opinion. But sure, won't be easy, probably.
<r​brunner7> In any case I hope their discussion converges soon somehow, it makes me a bit nervous that a core part like Jamtis is still in flux right now
<g​hostway> At the end, if they want to shower me with problems theyre trying to solve I'll try to take a look (even if not digested yet)
<r​brunner7> I think it's more of the opposite, I saw a surprising number of possible approaches, all with their own trade-offs
<r​brunner7> 1 view tag, 2 view tags, flexible-size view tag, you name it ...
<g​hostway> Yea well, that's the thing, I'd need a little idea survey heh
<r​brunner7> Alright then. Looks like we have it for today and can close the meeting here. Thanks for attending, until next week!
````


# Action History
- Created by: rbrunner7 | 2023-09-29T16:33:45+00:00
- Closed at: 2023-10-02T18:37:14+00:00
