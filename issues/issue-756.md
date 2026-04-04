---
title: 'Seraphis wallet workgroup meeting #2 - Monday, 2022-11-21, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/756
author: rbrunner7
assignees: []
labels: []
created_at: '2022-11-18T10:32:53+00:00'
updated_at: '2022-12-02T14:37:48+00:00'
type: issue
status: closed
closed_at: '2022-12-02T14:37:48+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind 2*, \#no-wallet-left-behind-2:haveno.network ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind-2:haveno.network)), Libera IRC channel \#no-wallet-left-behind.

Possible things to discuss and maybe decide in this second meeting:

1. Repository organisation for Seraphis wallet development: How many such repositories, with which branches, with who merging and rebasing what, as per ongoing discussion in the Matrix room / IRC channel
2. Revisiting the Jamtis address checksum algorithm - see [issue \#37](https://github.com/seraphis-migration/wallet3/issues/37)
3. Convention for naming classes and structs - see [issue \#13](https://github.com/seraphis-migration/wallet3/issues/13)
4. For the proper bikeshedding: How many blanks to use to indent code 1 level - see [issue \#36](https://github.com/seraphis-migration/wallet3/issues/36)

Proposals for additional subjects or changes of subject welcome here.

# Discussion History
## rbrunner7 | 2022-11-18T14:00:21+00:00
Log of first meeting: #751 

## rbrunner7 | 2022-11-21T19:28:29+00:00
````
<rbrunner7[m]> Meeting time! Tentative discussion points are here: https://github.com/monero-project/meta/issues/756
<rbrunner7[m]> Greetings - who is around?
<dangerousfreedom> Hello!
<one-horse-wagon[> Hello.
<UkoeHB> Hi
<sneurlax[m]> o7
<rbrunner7[m]> Let's see whether jberman will join us later.
<rbrunner7[m]> Alright. Anybody having something to report about things done re Seraphis in the passed week?
<rbrunner7[m]> I didn't do much except writing some more issues ...
<jberman[m]> here, hello :)
<one-horse-wagon[> Don't know if any of you saw my post on Reddit asking to name this project.  https://www.reddit.com/r/Monero/comments/yvwamw/naming_the_seraphisjamtis_projectits_a_big_deal/    After 8,700 views, the two names that notably came up were 1. "Mantelo Project" which got 33 votes and 2. "Seraphis" which got 19 votes.  Mantelo means "cloak" in Esperanto and is very fitting.  Either name resonates well.  Personally, I see no
<one-horse-wagon[> reason to change and Seraphis already has traction out there.  The only question is do we want to call it Seraphis Protocol, Seraphis wallet, Seraphis Project or just Seraphis.  Minor detail but important enough.
<rbrunner7[m]> Yup, saw it. Sometimes I have a feeling I more or less live in that subreddit :)
<UkoeHB> I should be done with the coinbase tx type this week, that’s my last task
<rbrunner7[m]> The library got 2 new source code folders. Looks more tidy now, after a first glance.
<rbrunner7[m]> Good to hear that the library will complete soon, as far as planned work is concerned.
<dangerousfreedom> I have been trying to follow the bottom-up approach to open a wallet and I'm trying to work on the building blocks but it is still complicated to me how to get started managing the different tiers of wallets. I have just done a single file base32 (https://github.com/DangerousFreedom1984/seraphis_lib/commit/ebccdef5ef23fc058f07a1a22ba7a379d3efd891) and created some unit_tests for that (by using a different algorithm and
<dangerousfreedom> generating thousands of lines) but I just let 5 for simplicity. More tests will need to be added in the future when we know the exact address to encode/decode. I have also started looking at the transaction classes and tried to make a parallel with seraphis but I believe that there is no parallel to be made :p
<Rucknium[m]> IMHO, do not call it "Seraphis Wallet". I have already seen confusion among users about whether Seraphis is just another wallet implementation like Cake, Monerujo, Feather, etc. "Seraphis" or "Seraphis Project" sounds ok. _bikeshed out_
<rbrunner7[m]> Sounds good to me.
<dangerousfreedom> <one-horse-wagon[m]> "Don't know if any of you saw..." <- I think it is too soon for a consensus, right? Or do we have one?
<rbrunner7[m]> Alright, shall we move to the first point on my list of things to discuss and decide. (I think we can discuss the project name during the week, here.)
<rbrunner7[m]> Repository organisation for Seraphis wallet development
<rbrunner7[m]> We already had some discussion during last week. As I see it, we basically had two proposals on the table.
<rbrunner7[m]> 1) Development of the wallet takes place in the same branch / same repo as the Seraphis library did so far
<rbrunner7[m]> 2) Development of the wallet takes place in a second branch / second repo "on top" of the Seraphis library
<rbrunner7[m]> Would you agree about this simplification of the discussion
<rbrunner7[m]> Or do you see other possibilities? A 3) so to say?
<rbrunner> Ping - is it only for me, or is the Matrix room suddenly working very slowly?
<one-horse-wagon[> No.  it's fast enough.  I think everybody is thinking?
<dangerousfreedom> Since you will be the maintainer I believe that 2 is the only option. If we need to modify the seraphis contents, it would be better to make a PR to koe's library and let him decide if it is a good idea or not. Then you update based on his library.
<jberman[m]> +1^ had this typed out: I'm good with 2, especially since UkoeHB  is very close to finishing work on the seraphis_lib. Since you (rbrunner7)  are planning to be admin through this process, makes sense to move toward collabing in a repo you're managing
<rbrunner7[m]> I was myself leaning towards the 2-repo solution, for technical and organisatorial reasons, and UkoeHB as well. Seems to me we have a good consensus here, and I have work to do and create that repo this week.
<rbrunner7[m]> That will be a fork of koe's repo then, right?
<one-horse-wagon[> That will be a fork of koe's repo then, right?  That's what you really want.  His repo will be the ultimate back-up of his work.
<jberman[m]> yes
<rbrunner7[m]> Alright, that much git fu I have to manage that :)
<dangerousfreedom> Yes. You can make a fork and then create another upstream branch to update with koe's most recent updates or just go and click sync so it would update with koe's library. Maybe there are other ways too.
<one-horse-wagon[> Also, the only one that can approve pull requests should be you.
<rbrunner7[m]> We will see. I think that's the starting point, initially.
<rbrunner7[m]> How it looks if every week tons of new code streams in remains to be seen.
<rbrunner7[m]> Alright, seems ok to move to the second point, "Revisiting the Jamtis address checksum algorithm"
<rbrunner7[m]> I wrote down the story of that in this issue: https://github.com/seraphis-migration/wallet3/issues/37
<rbrunner7[m]> In short, at the end of the MRL meeting of the week before the last one, we were ready to go for a checksum, but about 1 hour later Tevador brought up some interesting additional arguments
<rbrunner7[m]> For the polynominal approach
<dangerousfreedom> Both approaches couldnt go wrong IMO so I don't have a say in this issue.
<dangerousfreedom> Anyway, I can try to implement the polynomial approach and see how it looks like so we can discuss later
<rbrunner7[m]> I have to say that I lean towards Tevador's original design in the meantime.
<rbrunner7[m]> I also had the idea - that I will probably expand later this week in written form somewhere - that it might be very positive if we could settle Jamtis pretty soon with a good probability so we would be able to build first small tools for it.
<dangerousfreedom> Ok. I will see how bitcoin does it and see if we can use their code and present findings for next week
<rbrunner7[m]> +1
<rbrunner7[m]> I think this could be very good "marketing" for our project.
<one-horse-wagon[> rbrunner7[m]: It would be terrific marketing!
<rbrunner7[m]> Yeah, it might be that people like it if there was a little tool to show their Jamtis address for one of their wallets.
<rbrunner7[m]> A gimmick only of course, but interesting nevertheless.
<rbrunner7[m]> Well, not only that of course, that could result in interesting work for dangerousfreedom[m] maybe.
<one-horse-wagon[> It's more than a gimmick.  It's a security feature.
<rbrunner7[m]> Alright, so in any case we try Tevador's polynominal checksum approach first, and if that works out, probably go for that.
<dangerousfreedom> rbrunner7[m]: It won't be possible to show exactly how their address would look like without having access to their private keys. The public address is made from a hash of the private keys so we would need to have access to that. So I dont believe that it would be possible as a 'simple tool'. 
<rbrunner7[m]> You are right, such a tool could run into issues of trust, it does need access to the "holiest" key of them all. Let's see what can be done there.
<rbrunner7[m]> Next is a naming issue, at least from what I would like to bring up here: Convention for naming classes and structs 
<dangerousfreedom> What could be made is a generator comparing how a normal address versus a jamtis address would look like.
<dangerousfreedom> But not exposing the user's keys
<dangerousfreedom> And explaining the differences
<rbrunner7[m]> Issue is, and was already for a long time, this: https://github.com/seraphis-migration/wallet3/issues/13
<one-horse-wagon[> dangerousfreedom[m]: Is it not that the private keys are not sent over the internet but just stay on the person's computer?  Only the polynomial hash is
<one-horse-wagon[> sent
<rbrunner7[m]> It's basically the question whether we follow UkoeHB 's lead in naming classes in camel case, or stick with the more common Monero convention of using snake case for everything.
<rbrunner7[m]> one-horse-wagon: It's probably more complicated than you assume. We could have a look after the meeting, if you like and still have time.
<JoshBabb[m]> rbrunner7[m]: I would like to collaborate with @dang
<dangerousfreedom> > <@one-horse-wagon[m]:libera.chat> > <@dangerousfreedom[m]:libera.chat> What could be made is a generator comparing how a normal address versus a jamtis address would look like.
<dangerousfreedom> > 
<dangerousfreedom> > Is it not that the private keys are not sent over the internet but just stay on the person's computer?  Only the polynomial hash is
<dangerousfreedom> Yes. You never expose your private or public keys. What you expose to the world, which is your address 4..., is a hash of that.
<JoshBabb[m]> @dangerousfreedom[m]:libera.chat * on that on maybe getting a little demonstrator in Stack Wallet or something similar
<dangerousfreedom> jbabb[m]: Sure! Let's talk and see how we can best work
<JoshBabb[m]> I'll be following along anyways and will be making sure that JAMTIS addresses for a given mnemonic match and will be trying to keep on top of implementing seraphis as it gets into testnet
<rbrunner7[m]> Alright, among all this enthusiasm about possible Jamtis tools, can we nevertheless quickly decide that naming issue? Might help with starting the coding.
<dangerousfreedom> > <@jbabb[m]:libera.chat> > <@rbrunner7:haveno.network> You are right, such a tool could run into issues of trust, it does need access to the "holiest" key of them all. Let's see what can be done there.
<dangerousfreedom> > 
<dangerousfreedom> > I would like to collaborate with @dang
<dangerousfreedom> I have a demonstrator working except for the checksum (https://github.com/DangerousFreedom1984/seraphis_lib/commit/9689a27cf7df806bb274381016b9565e642001d0)
<one-horse-wagon[> rbrunner7[m]: .What's your preference?
<rbrunner7[m]> I am alright with both approaches. I would wish for people to stick to one as closely as possible, whichever of the 2 we pick.
<one-horse-wagon[> Which one do you like personally?
<rbrunner7[m]> Hard to say, as koe's library sets a precedence. Maybe a good idea to just follow that, if nobody vetoes.
<one-horse-wagon[> And that was?
<rbrunner7[m]> Camel case.
* dangerousfreedom uploaded an image: (210KiB) < https://libera.ems.host/_matrix/media/v3/download/matrix.org/JgwiUNjXxNsfqzeARrupGOQy/image.png >
<dangerousfreedom> jbabb[m]: This a poor/fast written code but it should give you that 
<one-horse-wagon[> I totally agree, hands down.
<one-horse-wagon[> Snake case is harder to read and hence easier to make mistakes with.
<rbrunner7[m]> Well, it would be only for the names of types. All other things would stay snake case, which is Monero style to a large degree, and of course general C++ style.
<rbrunner7[m]> As far as I am concerned, I wouldn't propose to switch all. This is in any case not what koe actually used for the library.
<rbrunner7[m]> Ok, let's say if I don't get a veto from anybody until the end of the meeting, let us follow koe's lead and make names of types camel case.
<one-horse-wagon[> Done
<rbrunner7[m]> So if nobody has anything more important that they feel should discussed in the last 10 minutes, I have a terribly important question: How many blanks to use to indent code 1 level
<rbrunner7[m]> On the table are 2 blanks per level (probably the majority of "old" Monero files) and 4 (a number of files, including koe's library)
<rbrunner7[m]> Issue is here: https://github.com/seraphis-migration/wallet3/issues/36
<dangerousfreedom> I vote for 4
<one-horse-wagon[> Linus Torvalds in his Linux repo insists on 8 space tabs, no more than 3 levels and no more than 80 space lines.  Any possibility here?
<rbrunner7[m]> UkoeHB naturally also voted for 4 in the issue
<UkoeHB> Who cares what Linus does
<UkoeHB> 4 is a good balance of readability
<rbrunner7[m]> Yeah, I saw that info, and was quite surprised. It seems it wasn't a success outside the world of Linux programming.
<rbrunner7[m]> I don't think we make many friends if we jump from 2 to 8 :)
<JoshBabb[m]> Sounds good for Wownero though
<rbrunner7[m]> Do they use that?
<one-horse-wagon[> Probably so.
<JoshBabb[m]> 16 would be even better
<rbrunner7[m]> So ... in this case .... I quickly vote for 4, to prevent that ...
<jberman[m]> I'm good with 4
<one-horse-wagon[> 4 it is.  
<rbrunner7[m]> Alright, splendid. We achieved much today, seems to me.
<rbrunner7[m]> Any last minute remarks?
<UkoeHB> Thanks rbrunner7[m]
<one-horse-wagon[> Good meeting.
<rbrunner7[m]> Thanks, and thanks back to my friendly meeting participants
<jberman[m]> Backing up a bit, as has basically been mentioned before it looks like Bitcoin chose to go with a BCH code for error detection versus a hash because it has stronger error detection capabilities (you can identify the exact typo even though Bitcoin doesn't implement automatic error correction)
<jberman[m]> Of note they also had an issue in their original error detection implementation where it would sometimes miss detecting errors
<jberman[m]> Helpful link that has lots of other helpful links: https://bitcoinops.org/en/topics/bech32/
<jberman[m]> So a BCH code seems like a level of added complexity that can go wrong versus a hash, but one with stronger benefits. I agree it makes sense to start down the route using a BCH code
<rbrunner7[m]> Tevador showed us the code, and I nearly fell off the chair, it's so simple.
<rbrunner7[m]> I expected something like 500 lines or so of dense C++ code ...
<rbrunner7[m]> At least the checksum calculation code, that is.
<dangerousfreedom> Sometimes it is harder to understand 5 lines of code than 500 :p
<rbrunner7[m]> Lol, right.
<dangerousfreedom> Thank you for organizing the meeting rbrunner :)
<rbrunner7[m]> It looks pretty mysterious.
<one-horse-wagon[> What is the issue of exposing private keys with the polynomial checksum that was mentioned in the meeting?  
<rbrunner7[m]> Ok, I officially close the meeting, things above this will go into the log. Let's resume "normal" discussion.
````

# Action History
- Created by: rbrunner7 | 2022-11-18T10:32:53+00:00
- Closed at: 2022-12-02T14:37:48+00:00
