---
title: 'Seraphis wallet workgroup meeting #59 - Monday, 2024-02-26, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/972
author: rbrunner7
assignees: []
labels: []
created_at: '2024-02-25T07:48:29+00:00'
updated_at: '2024-02-26T19:02:45+00:00'
type: issue
status: closed
closed_at: '2024-02-26T19:02:45+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/969

# Discussion History
## rbrunner7 | 2024-02-26T19:02:45+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/972
<d​angerousfreedom> Hi
<j​effro256> Howdy
<r​brunner7> Any reports about the past week? As you can see in the backlog, a rebase to current Seraphis lib for me, with help from jeffro256
<r​brunner7> Git is a just a bit less mysterious now to me
<j​effro256> Koe approved the Jamtis changes to the Impl Seraphis paper
<r​brunner7> Oh, nice. So that's the math, but not yet the code?
<j​effro256> Yup, although koe *did* start reviewing the code a couple days ago
<r​brunner7> Good news. So the even longer addresses probably *will* come :)
<d​angerousfreedom> I worked on the serialization of the enote_store. I hope Koe will merge jeffro's proposal to simplify how it is done. Seems much cleaner to me to have a header where you define the how all the seraphis structs get serialized instead of having intermediate structs to do the serialization
<r​brunner7> Is this a whole new approach then? I did not yet check in detail what that entails.
<d​angerousfreedom> No it is not new. It was already implemented on Monero and now jeffro made a macro to easily do it for the seraphis structs AFAIU
<r​brunner7> Do you have a link where we can see how this new approach works?
<j​effro256> https://github.com/UkoeHB/monero/pull/34
<d​angerousfreedom> I worked on the serialization of the enote\_store. I hope Koe will merge jeffro's proposal to simplify how it is done. Seems much cleaner to me to have a header where you define how all the seraphis structs get serialized instead of having intermediate structs to do the serialization
<r​brunner7> Does this work without a need to modify the Seraphis lib classes and structs themselves then?
<j​effro256> Yes
<d​angerousfreedom> Yes thats the goal
<j​effro256> Right now, it won't get merged as its a regression, taking up more bytes than the old format. That can be changed in a couple lines tho, but I'm working on https://github.com/UkoeHB/monero/pull/31 before I refactor the serialization PR, since #31 would remove redundant information from the transaction class
<r​brunner7> Ah, ok, koe's reservation there is about byte size of the serialization?
<j​effro256> Yes
<r​brunner7> So this is still a developing story.
<r​brunner7> Would be nice if this learns to fly, without compromises. The "serialization demo" approach of doubling classes keep complexity out of the Seraphis lib classes alright, but "elegant" is not something I would call this.
<r​brunner7> That "new" approach does not need to allocate any new objects?
<j​effro256> yep!
<r​brunner7> I would probably also gamble on a positive outcome, like dangerousfreedom seems to do by refactoring his code already along these lines :)
<r​brunner7> But well, with all these changes, and the new transaction class, and the Jamtis revision, we have considerably construction work going on
<r​brunner7> You will continue to work more or less fulltime on Seraphis, jeffro256 ? Or do you have other things still in parallel?
<j​effro256> If PR #9135 doesn't need any more work, I'm going to be going full stream ahead on Seraphis ;)
<dangerousfreedom> +1
<r​brunner7> Splendid.
<r​brunner7> It made me think a bit, when I did the rebase, that we have only 5 merged PRs to the Seraphis wallet so far ... we have to pick up steam.
<d​angerousfreedom> jeffro256: regarding your comment [here](https://github.com/seraphis-migration/monero/pull/17), I can reproduce and eliminate the problem by setting the extra bit to 0 but I cant reduce the size of the full address by packing all the 'extra' bits directly into the base32. Would you care to elaborate your idea here? Do you mean I need to have a special struct or a special way to se<clipped 
<d​angerousfreedom> rialize all the address together?
<j​effro256> Definitely, although most of my work is not being PR'ed to the seraphis_wallet branch
<r​brunner7> I see.
<j​effro256> Or yet to be PR'ed in some cases
<d​angerousfreedom> jeffro256: regarding your comment [here](https://github.com/seraphis-migration/monero/pull/17), I can reproduce and eliminate the problem of having two addresses that points to the same keys by setting the extra bit to 0 but I cant reduce the size of the full address by packing all the 'extra' bits directly into the base32. Would you care to elaborate your idea here? Do you mean I<clipped 
<d​angerousfreedom>  need to have a special struct or a special way to serialize all the address together?
<r​brunner7> Yes, those Jamtis changes are massive.
<j​effro256> dangerousfreedom: look at this link: https://github.com/UkoeHB/monero/pull/31
<j​effro256> If you add up all the bits in the header + address keys + address tag, divide it by 5 rounding up, that's how many characters should be in the address (minus the checksum)
<r​brunner7> It's about this review comment: "Related: the addresses can be made 1 byte shorter by packing in the X25519 pubkeys 255 bits at a time"
<j​effro256> Yes, you can see in the table that they take up 255 bits. When you combine that with the address tag, tightly packing, you have enough bits to shave off 1 character from the resulting address
<r​brunner7> Is this "packing" complex in any way? Even if only a little bit more complex? I ask myself how much a single byte is worth
<j​effro256> It's just bit shuffling
<r​brunner7> I think many people will implement Seraphis address functions in many languages. We should think before making their life hard, too hard for the gains that we achieve, if you understand what I mean.
<d​angerousfreedom> Yes, but you have to serialize them separately, right? I cant mix one bit that is not being used on a char[32] with other in another char[32] with other 3 in something else. Can I?
<d​angerousfreedom> The minimum data package in C++ and on the serialization is 1 byte, right?
<d​angerousfreedom> Not one bit
<j​effro256> Yes, not directly. What you should do is interpret the buffers as LE ints, then mask, shift, re-encode the bytes back into a buffer, then serialize that
<j​effro256> (sorry not serialize, encode as base32)
<r​brunner7> How many bytes are we talking about, where we have the chance to shave one off with these bit shufflings?
<j​effro256> 1 byte
<r​brunner7> No, I mean the data overall. 100 bytes? 150 bytes?
<d​angerousfreedom> Ok... we will need something ad-hoc for the addresses
<r​brunner7> Only if we really go down that road. I am less than enthusiastic, to be frank.
<j​effro256> 196 characters for the final Jamtis address without the extra key from the new Jamtis changes
<r​brunner7> So we are talking about "bit shuffling for about 0.5% less bytes overall", yes?
<j​effro256> Yes
<d​angerousfreedom> Ok. I will do it this week
<r​brunner7> You think this is an attractive tradeoff? More complex in and out of Base32 for 0.5% length reduction?
<j​effro256> Base32 remains the exact same, it's just which buffer gets passed to base32 functions
<d​angerousfreedom> The problem is that it leaves open space to people fill addresses with information
<r​brunner7> Yeah, that's what I really meant
<d​angerousfreedom> If we dont do
<j​effro256> Any library which does anything with the addresses needs the mx25519 library which is 1000x more complex than doing some bit shifting
<d​angerousfreedom> Like having two addresses like the below that points to the same address in your wallet
<j​effro256> Or twofish
<d​angerousfreedom> xmra1m95qawddtkd23856u12wynkin8e94ahi9y32tgcpgtt8dd4b92dt7h3gf4n4aau264uywsit34qhgj63g4n41sa02qyh3pf1fdsgkeq3cekdksx961t4gh9tddawcheag774uk3yf3fdwgnk7nk95xr2ad9cpjfd4frn55nbce0ym27cue3a51b02w6xpg3t
<d​angerousfreedom> xmra1m95qawddtkd23856u12wynkin8e94ahi9y32tgcpgtt8dd4b92dt7h3gf4n4aau264uywsit34qhgj63g4n41sa02qyh3pf1fdsgkeq3cekdksx961t4gh9tddawcheag774uk3yf3fdwgnk7nk95xr2a49cpjfd4frn55nbce0ym27cue3a51b0ehp053f1
<d​angerousfreedom> Maybe it is not a bug but a feature :p
<r​brunner7> I guess it depends what will be the format to move addresses e.g. over the RPC interface, or how the wallet API wants them.
<r​brunner7> If that's this complex bit-shuffling format, people will have to unpack that in various programming languages
<r​brunner7> I am not talking about address generation and such
<j​effro256> What's the most likely is that they just hand the address over to the Seraphis library anyways and it does the work anyways
<r​brunner7> We also have leftover bits in our current addresses, right? Did anybody ever hear that some people did nonsense with that, like putting extra info in there?
<r​brunner7> Also know as the argument "We should try to avoid to invent problems where there are none"
<d​angerousfreedom> Yeah,  that's what I thought initially. I dont know.
<r​brunner7> In any case to rely more on the textual address format and avoiding any "binary" address format would have to go into the design of the APIs properly.
<d​angerousfreedom> The worst case scenario that I see is that one where you have two human readable addresses pointing to the same keys. The performance cost is negligible I think
<r​brunner7> No, performance is absolutely *not* in my mind. Just complexity. We now have freaking 4 keys in our addresses, people :)
<r​brunner7> Do we aspire for any entries in the Guiness Book of records for most complex crypto addresses, lol
<r​brunner7> And if I see a reasonable chance to *not* put even more complexity on top of that, for saving *bits*, I do that.
<r​brunner7> It feels a bit lonely in the place where I stand, however :)
<d​angerousfreedom> Haha yeah. To be honest I don't know much yet about the 4th key. I need to study more too.
<r​brunner7> That's already with the Jamtis update included.
<d​angerousfreedom> I think I wont modify that yet then
<j​effro256> One could make the argument that since the Jamtis addresses are getting long, it's even more necessary to conserve space where we can
<r​brunner7> Sure. We do talk about difficulat trade-offs. It's a bit of a pity we are not more people here right now, to hear more opinions.
<j​effro256> New Jamtis addresses would be 244 characters long, where a tweet is 280 characters max
<j​effro256> Agreed about having more people in here
<r​brunner7> Ah, come on, nobody will notice if we don't go down to 243 from 244 :)
<r​brunner7> Down to 242 by eliminating "a" from "xmra", right?
<j​effro256> It'd be 244 from 245 technically
<j​effro256> True
<d​angerousfreedom> Yeah, I like the idea of using all the info to decode just 1 address also. The bit shuffling shouldnt be something complex. Just one more step to decode addresses for developers probably. But shouldnt be hard.
<r​brunner7> Right. That's also not my claim, that it's really hard. But things sum up, and accumulate.
<j​effro256> I can help you code it if you would like
<r​brunner7> Let us have a look at the code, we certainly don't have the need to make any final decisions now in this very meeting.
<d​angerousfreedom> You can help with the review for sure :)
<d​angerousfreedom> jeffro256: I will also ask for your help this week to review some of your PRs that I didnt have to do yet.
<r​brunner7> Alright, anything else? We are nearing the full hour. Ah, does anybody happen to know what jberman is doing? Still deep into those FCMPs? It's quite some time I saw him write anything anywhere.
<d​angerousfreedom> jeffro256: I will also ask for your help this week to review some of your PRs that I didnt have time to do yet.
<r​brunner7> jberman, for a proper ping, should he get that
<j​effro256> He was reviewing #9135 a couple days ago
<j​effro256> But IDK what he's mainly working on
<r​brunner7> Ok, let's close here, thanks for attending everybody, read you again next week!
<j​effro256> Thanks everyone
<d​angerousfreedom> Thanks
````


# Action History
- Created by: rbrunner7 | 2024-02-25T07:48:29+00:00
- Closed at: 2024-02-26T19:02:45+00:00
