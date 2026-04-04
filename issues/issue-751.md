---
title: 'Seraphis wallet workgroup meeting #1 - Monday, 2022-11-14, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/751
author: rbrunner7
assignees: []
labels: []
created_at: '2022-11-08T21:13:06+00:00'
updated_at: '2022-11-18T09:40:30+00:00'
type: issue
status: closed
closed_at: '2022-11-18T09:40:30+00:00'
---

# Original Description
On Monday, November 14, we start with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind 2*, \#no-wallet-left-behind-2:haveno.network ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind-2:haveno.network)), Libera IRC channel \#no-wallet-left-behind.

Following the pattern of the MRL meetings, there will be an issue to announce each meeting (like [this here](https://github.com/monero-project/meta/issues/750) for the next such MRL meeting), to list possible things to discuss, and to finally post a meeting log.

For this first meeting I propose we discuss the following subjects that will help dev work to start in earnest if we can reach consensus and decide things. Feel free to comment, propose other subjects, declare some as "too early to discuss", etc.:

1. Confirm *Seraphis wallet* as our project name (see [issue #15](https://github.com/seraphis-migration/wallet3/issues/15)) which may influence naming, e.g. leading to a folder name of `seraphis_wallet`, namespace letters `sw`,  maybe also class names
2. Discuss how we name and how we may nest folders that we add to the Monero project (see [issue #29](https://github.com/seraphis-migration/wallet3/issues/29)); right now there is single, big new folder simply called `seraphis` in @UkoeHB 's development branch
3. Discuss and decide terminology questions: 
3.1 *enote* ([issue #1](https://github.com/seraphis-migration/wallet3/issues/1))
3.2 *transaction id* ([issue #14](https://github.com/seraphis-migration/wallet3/issues/14))
3.3 *Jamtis* ([issue #24](https://github.com/seraphis-migration/wallet3/issues/24))
3.4 *transfer* ([issue #18](https://github.com/seraphis-migration/wallet3/issues/18))
3.5 type names ([issue #13](https://github.com/seraphis-migration/wallet3/issues/13))

Note that we try a bottom-up approach for the first modules that will get coded, as discussed in an ad-hoc meeting we had recently (voice, no log available). While we certainly have a lot of important issues to discuss regarding architecture, design, and general implementation approaches, I feel that most of them are not yet ready because the project is still in a very early phase. Hopefully, things will become progressively clearer with that bottom-up work progressing, and that in turn will enable those discussions.

# Discussion History
## One-horse-wagon | 2022-11-08T22:39:22+00:00
Can we also discuss a projection as to when Seraphis will finally be completely implemented?  I'm thinking to do everything, we are looking at least 2 years away and more like 3 to 4.

## selsta | 2022-11-10T23:33:02+00:00
I created an IRC channel that is also accessible from matrix:

Matrix: #no-wallet-left-behind:libera.chat
IRC Libera: #no-wallet-left-behind

## rbrunner7 | 2022-11-12T20:22:45+00:00
We had to create a new Matrix room *No Wallet Left Behind **2*** to get a fully-featured Matrix room that is bridged to the Libera IRC channel \#no-wallet-left-behind and that the workgroup can properly administrate itself.  I updated the issue accordingly.

The original room *No Wallet Left Behind* is closed and redirects users to the new room so even people who will miss the update should find their way.

Posting in the Libera Matrix room technically works but is not recommended.

Thanks to @selsta and @ErCiccione for setting everything up!



## rbrunner7 | 2022-11-14T19:31:47+00:00
````
<one-horse-wagon[> Hello everyone.
<rbrunner7[m]> Hello. Meeting time. Agenda is here: https://github.com/monero-project/meta/issues/751
<rbrunner7[m]> I intend to follow the habits set by the MRL meetings, because those work well, so let's start with greetings. Who is around and dares to tell?
<one-horse-wagon[> I'm here.
<jberman[m]> hello :)
<JoshBabb[m]> Howdy!
<UkoeHB> hi
<rbrunner7[m]> @dangerousfreedom, one of our two devs (so far) is excused for private reasons, but I had a good session with him yesterday
<rbrunner7[m]> The bridge to the #no-wallet-left-behind IRC room seems to work
<dangerousfreedom> Hello. Yeah, I won't participate much today :p
<rbrunner7[m]> Alright. To get into the mood, so to say, I would like to pick up a suggestion and ask into the round for estimates: When will the hardfork to Seraphis take place? Too early to discuss anything, but curious for your estimates!
<rbrunner7[m]> A suggestion from one-horse-wagon 
<one-horse-wagon[> 3 years if all goes well.
<rbrunner7[m]> Alright, I came up with more optimistic 2 years.
<UkoeHB> 2 years if time is used well
<jberman[m]> Ya I'd go with an optimistic 2 years too
<rbrunner7[m]> Word!
<rbrunner7[m]> Let's try our best to not waste too much time. Would be a pity :)
<rbrunner7[m]> Ok, the first point on the agenda is the name of our project. I wrote an issue for that earlier: https://github.com/seraphis-migration/wallet3/issues/15
<rbrunner7[m]> It has a certain importance because it probably makes sense to derive some technical names from that name.
<rbrunner7[m]> "Seraphis wallet" is on the table and did not seem to run into much resistance. But "wallet3" is around as well.
<rbrunner7[m]> Or maybe something completely different, who knows
<jberman[m]> calling it "Seraphis wallet" would limit it to Seraphis imo. it wouldn't surprise me if there is some significant upgrade in the future that would then make it confusing to call the wallet "Seraphis wallet", even though that upgrade still uses most of the code we write under the "Seraphis wallet". I think "wallet3" is fine and doesn't have that sort of issue
<UkoeHB> wallet3 implies another monolith, I vote against
<UkoeHB> how about xmr wallet suite or something
<one-horse-wagon[> From an advertising point of view, "The Seraphis Project" has a futuristic ring to it.
<rbrunner7[m]> Yeah, but that's more than this workgroup actually tries to build now, no?
<UkoeHB> it is?
<rbrunner7[m]> Personally I find "wallet3" a bit boring, and non-descript. I wouldn't be ashamed to call this "Seraphis wallet" straight, it's really that in my eyes
<rbrunner7[m]> "it is?" Well, thinking about it, we will of course also adjust other parts of the code, to work with Seraphis ...
<one-horse-wagon[> One needs to think ahead.  This project is going to require a good amount of funding.  People will get on board for futuristic projects.  That's why we need a name that sells out there.
<JoshBabb[m]> As an outsider (don't mind me) I see wallet3 as related to wallet2 and by context I recognize it as related to Monero.  Do you want it related to Monero?  Seraphis doesn't relate to Monero to me yet.
<Rucknium[m]> IMHO, with these naming and publicity questions, threats of users being scammed should be top of mind.
<rbrunner7[m]> Josh Babb: But admittedly "wallet2" is also quite insider-knowledge
<JoshBabb[m]> Absolutely ^
<moneromoooo> Is it just me or did this just go pear shaped right from the start...
<JoshBabb[m]> +1
<rbrunner7[m]> Rucknium: Was do you derive from this interesting thought? How best make our name "non-scammy"?
<rbrunner7[m]> "pear shaped" as "going down wrong tracks"?
<Rucknium[m]> I don't know. Where is our social engineering penetration tester?
<Rucknium[m]> I just know with many hard forks, network upgrades, etc. on other blockchains there are scams running around.
<moneromoooo> Sorry. Means... going wrong. Blowing up. Breaking down :)
<moneromoooo> I mean, of all the things that could be interesting... starting on a subjective bikeshedding question ?
<rbrunner7[m]> And why would that be? Can't follow. Maybe do not let this dominate the meeting, and if we don't have consensus put it away
<JoshBabb[m]> +1
<interloper> +1
<rbrunner7[m]> Well, IMHO many very interesting and important topics are just not yet within reach of sensible discussion, like e.g. migration strategy and a host of other things.
<UkoeHB> Do wallet_suite as an umbrella category for the wallet types and wallet tools. You won't be building a single wallet anyway.
<UkoeHB> the marketing aesthetic, toss that out the door so we can move on
<rbrunner7[m]> Ok, maybe the people over in #monero-community can duke it out
<rbrunner7[m]> Next topic on my list, hopefully a bit less bikeshedding, is the source folder organisation in the Monero core repo source tree
<rbrunner7[m]> The corresponding issue: https://github.com/seraphis-migration/wallet3/issues/29
<rbrunner7[m]> I got a bit careful now - do people see this as an important question, and well suited to discuss now?
<UkoeHB> I plan to do a PR reorganizing things according to that issue later this week. Have been sick for a few days
<rbrunner7[m]> I could help set up a repository for our work soon.
<rbrunner7[m]> And guide UkoeHB when he reorganizes his library.
<UkoeHB> not PR, commit
<rbrunner7[m]> The two of us discussed in that issue two different approaches, basically, as I saw it:
<rbrunner7[m]> 1) Add a number of Seraphis-related "top level" folders, i.e. in /src.
<rbrunner7[m]> 2) Add something like 2 such top-level folders, and then go one level deeper within those.
<rbrunner7[m]> /src currently has 30 folders.
<rbrunner7[m]> Those two folders in variant 2) could be 1 for the library and one for the wallet.
<rbrunner7[m]> or wallets.
<rbrunner7[m]> Any opinions?
<UkoeHB> It doesn't make sense to me to have subfolders. Multisig utilities depend on seraphis crypto and seraphis mulitisig depends on the multisig utilities, and multisig utils are in the main src/
<UkoeHB> could easily imagine other dependencies trails like that
<rbrunner7[m]> Does anybody see a problem if we push the "top-level" folders maybe up to 40 over the course of this project?
<one-horse-wagon[> That's a big number.
<UkoeHB> It should be fine. Rearranging files and folders is a bit tedious but not a big deal
<UkoeHB> as needed
<rbrunner7[m]> Well, to avoid misunderstanding, I mean adding 10 to the existiing 30, arriving at 40
<rbrunner7[m]> In my experience people attach to such folders and folder names awfully fast and are not too happy if you re-arrange, even if technically not a big deal.
<rbrunner7[m]> But maybe for this the same is true as for the more difficult questions: Too early to tell, we have to decide as we move along?
<jberman[m]> I'd prefer to avoid a ton of new top-level folders, but if it's the cleanest way to navigate and avoids dependency issues, then no I don't have an issue with it. I'd like to see what UkoeHB does later this week. Sounds like he has a decently fleshed out approach in mind already and he's the one who's been navigating this code and understands its structure best toward organizing it. I'm good to move on
<rbrunner7[m]> Yeah, we will work in a quite small circle for quite some time, and maybe there we really are still free to reorganize if we see something does not fly.
<BusyBoredom[m]> Just chiming in from the perspective of a dev who has not worked with the monero codebase -- I would _expect_ to see a `wallet/` folder inside `src/` with contents broken out further bellow that (e.g. multisig wallet logic might live inside `src/wallet/multisig/*`). 
<BusyBoredom[m]> I would _not expect_ to see things relating to wallet internals inside `src/`
<rbrunner7[m]> Ok, noted. Probably still a good idea to move on, as far as this meeting is concerned. It does seem a bit early to decide something, and some experimentation is probably in order.
<rbrunner7[m]> Ok. Let's see what people say about those terminology questions that I put on the agenda :)
<rbrunner7[m]> 3.1 Enotes
<rbrunner7[m]> Everybody cool with leaving the term "output" behind for good and going for "enote", like UkoeHB coined it
<rbrunner7[m]> and used it througout his library?
<one-horse-wagon[> Enotes is a very good choice.
<interloper[m]> I'm just an outsider, but to chime in; enote is a modern, accurate, and simple to understand term. I think it's a good choice and better than 'output'
<rbrunner7[m]> I like the term. It grew on me. And it neatly avoids almost nonsensical statements like "the outputs have 2 roles: output and inputs".
<spacekitty420[m]> +1
<JoshBabb[m]> Does it matter that enotes is already a cryptocurrency? https://www.enotes.online/ Also it is a registered trademark for two different applications.  As an outsider I don't see good google results for enotes
<JoshBabb[m]> But, bikeshed
<spacekitty420[m]> tbf, everything is a cryptocoin nowadays
<rbrunner7[m]> Interesting that there is already a coin, but I don't see a problem there.
<JoshBabb[m]> Slap a blurb somewhere like in a README explaining the terminology and it's ok
<UkoeHB> JoshBabb[m]: never seen that before
<UkoeHB> huh been around since 2018
<rbrunner7[m]> Ok, I guess people have a last chance to object or try to veto after they will read the meeting log, but for now "enotes" is it, seems to me.
<rbrunner7[m]> A quite small one, 3.2, about two terms now used willy-nilly in the codebase: "transaction id" and "transaction hash"
<JoshBabb[m]> Just noting, if I can't google it, if should be explained somewhere what it means, if it's an abbreviation or shorter version of something else, etc.
<rbrunner7[m]> I vote for standardizing on "transaction id"
<spacekitty420[m]> +1
<jberman[m]> (I'm cool with enotes. Agree it should help avoid ambiguity when discussing the "inputs" and "outputs" in a tx)
<JoshBabb[m]> Is it a standard cryptographic or cryptocurrency term I'm overlooking?
<rbrunner7[m]> That the transaction identifier is - at least so far - a hash, is a technical detail. It's an id, period.
<rbrunner7[m]> (Just a little side-note - I learned on Friday that votes with emojis don't make it over to IRC. Maybe I will try to add them to the textual log.)
<UkoeHB> JoshBabb[m]: it's introduced in the seraphis paper
<JoshBabb[m]> Then I'm just unread!  Sorry.
<rbrunner7[m]> Well, pretty few people so far have read that :)
<JoshBabb[m]> "Skimmed" ;)
<UkoeHB> yes tx id is fine
<rbrunner7[m]> Alright, seems nobody really complains about my prososal to do away with "transaction hash". Good.
<rbrunner7[m]> Let's skip 3.3, with Jamtis, because we nearly filled the hour already, and move on to another such little terminology question
<spacekitty420[m]> rbrunner7: or for votes over irc could also just be like "type 1 in chat for option A", "type 2 in chat for option B", downside is that it would be spammy but at least can easily figure it out that way
<rbrunner7[m]> `wallet2` now uses the term "transfer" in various ways, and them from that also CLI wallet commands, RPC server commands, and so on.
<rbrunner7[m]> I say "transfer" as a term is confusing and potentially misleading, and I would like to avoid it for "our" wallet.
<rbrunner7[m]> Not sure anybody can relate who did not yet work with `wallet2` source.
<spacekitty420[m]> sweep is also used with current wallet
<one-horse-wagon[> Transfer for me was a catchall for everything.  Easily misunderstood.
<rbrunner7[m]> Yes, but "sweep" did not seep into C++ identifier naming at least, for structs and such.
<rbrunner7[m]> Where you now never are really sure whether it's info about a transaction or info about an enote in some role.
<rbrunner7[m]> Maybe jberman knows what I am talking about here.
<UkoeHB> rbrunner7[m]: tooo late lol https://github.com/UkoeHB/monero/blob/478fe97d0b69e9c47cd8ad72406fbb6bcb8adab6/src/seraphis/tx_builders_mixed.h#L145
<rbrunner7[m]> Lol
<UkoeHB> in our world a transaction is a thing and transfer funds is what it does
<UkoeHB> so I don't think it makes sense to fully ban
<rbrunner7[m]> Maybe restrict it to a role as a verb in methods? But not using it for objects and structs?
<jberman[m]> rbrunner7: There are function names and top-level commands called using the "sweep" term. Which is actually related to one of the questions I have for UkoeHB , I don't see any sweep-related code (either sweep all or sweep single) in the Seraphis input selection code yet. Am I missing it or does that also still need to be implemented?
<UkoeHB> jberman[m]: sweep has to be implemented separately
<UkoeHB> it doesn't make sense to use the input selector for that
<UkoeHB> the input selector is for when you know the output amount beforehand
<rbrunner7[m]> Makes sense.
<rbrunner7[m]> But things like accounts can probably complicate.
<jberman[m]> makes sense it would be implemented separately from the input selector. wasn't sure if it's implemented yet. got it
<rbrunner7[m]> Alright, we are past the hour, I think we call it quits for the meeting proper. Thanks everybody, hopefully see some of you again in 1 week.
<rbrunner7[m]> I take my bike out of the shed to drive home now :)
<UkoeHB> thanks rbrunner7[m] 
````

# Action History
- Created by: rbrunner7 | 2022-11-08T21:13:06+00:00
- Closed at: 2022-11-18T09:40:30+00:00
