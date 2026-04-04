---
title: 'Seraphis wallet workgroup meeting #16 - Monday, 2023-03-13, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/809
author: rbrunner7
assignees: []
labels: []
created_at: '2023-03-10T16:59:55+00:00'
updated_at: '2023-03-14T01:00:40+00:00'
type: issue
status: closed
closed_at: '2023-03-14T01:00:40+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #806

I think now we really should be ready to discuss the question of managing very different types of transactions in the Monero code together: @ShalitMonero has mocked up some code to demonstrate a possible approach that you find in their new issue [A way to use 2 different transaction classes](https://github.com/seraphis-migration/wallet3/issues/50).

# Discussion History
## rbrunner7 | 2023-03-13T19:07:22+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/809
<UkoeHB> hi
<shalit[m]> hello!
<dangerousfreedom> Hello
<jberman[m]> hello
<one-horse-wagon[> hello.
<rbrunner7[m]> Any reports what went on during last week?
<UkoeHB> I came up with some adjustments to the balance recovery design that should maximize multithreaded performance. Won't implement it any time soon, since it requires some deeper refactoring of the scan machine.
<rbrunner7[m]> We had a very interesting discussion regarding dangerousfreedom[m] 's new CCS that led me to write this proposal: https://github.com/seraphis-migration/wallet3/issues/51
<rbrunner7[m]> Will that also have repercussions for the wallet, depending on how far we get until that refactoring happens?
<Rucknium[m]> Hi
<UkoeHB> no it's a backend thing
<rbrunner7[m]> My design review meeting proposal did not yet get any feedback. So until I hear from somebody that's a bad idea, or overkill, or whatever, I assume it's ok :)
<plowsof11> hi
<rbrunner7[m]> Alright, if that's it for the reports, we can make an attempt to tackle the subject I proposed for today, that transaction classes handling question.
<rbrunner7[m]> Did people come around to have a look?
<rbrunner7[m]> I mean, at my original issue from almost half a year ago already: https://github.com/seraphis-migration/wallet3/issues/7
<rbrunner7[m]> And shalit 's mockup class: https://github.com/seraphis-migration/wallet3/issues/50
<rbrunner7[m]> Any comments?
<UkoeHB> yeah, using a variant would work better because visitors enforce handling each subtype
<dangerousfreedom> rbrunner7[m]: Agree with that.
<UkoeHB> for example: https://github.com/UkoeHB/monero/blob/0fa70bd047149582cca675ebebb388ba342fb548/src/seraphis_core/legacy_enote_types.cpp#L49
<rbrunner7[m]> With "variant" you mean what I call a "naked variant"? The "generalized" transaction type is nothing more than a typedef for a `std::variant`, or your new improved variant class?
<UkoeHB> well I would recommend my `tools::variant<>`
<rbrunner7[m]> Hmm, never heard about such "visitors". Are those methods you can "attach" somehow to a variant then?
<rbrunner7[m]> Maybe almost everybody here knows C++ better than me :)
<UkoeHB> No, you apply a visitor to a variant and it calls a subtype-specific method on whatever subtype the variant currently holds. Visitors don't compile unless all subtypes are handled.
<dangerousfreedom> I started trying to mentally draft what is expected from this transaction history component and wrote some basic prototypes for it, I think we need discussion still
<rbrunner7[m]> And you can have any number of such visitors of course, right?
<rbrunner7[m]> per single variant type
<UkoeHB> yes
<rbrunner7[m]> And the advantage compared with the approach that shalit mocked up is compile time safety that you don't forget to handle one of the types?
<UkoeHB> for example: https://github.com/UkoeHB/monero/blob/0fa70bd047149582cca675ebebb388ba342fb548/src/seraphis_main/contextual_enote_record_types.h#L257
<UkoeHB> yes compile-time safety, and it discourages spaghetti in general
<dangerousfreedom> Feel free to add your 2 cents here: https://github.com/seraphis-migration/wallet3/issues/49
<rbrunner7[m]> So if we take one info query that is littered all over the place, getting the id for a transaction. That would be one of hose visitors, and I can call it like tx.id() or something?
<UkoeHB> you'd call `tx_id(tx_variant)`
<jberman[m]> it seems like a good idea to me. that's basically what I've been doing while working on the scanner as well but mainly in dm's with koe (discuss design first before coding). fine with shooting for a more collective design review approach from start to finish on most tasks of significant weight
<plowsof11> (im noticing some noticeable lag between messages appearing here / the other room just you are aware)  
<rbrunner7[m]> Well, the type probably does not interest me at that moment. I just want the id. What exactly would be the parameter there?
<UkoeHB> the generic tx variant object?
<rbrunner7[m]> Ah, no, it's just the other way round.
<rbrunner7[m]> If my transaction is in a variable tx, I call tx_id(tx).
<UkoeHB> sure
<rbrunner7[m]> Ok, sounds ok. And serialization would fit into this approach as well?
<rbrunner7[m]> > fine with shooting for a more collective design review approach from start to finish on most tasks of significant weight
<rbrunner7[m]> Good to hear, jberman !
<UkoeHB> shalit[m]: is modeling a tx object that contains what looks like cached metadata like size/hash. It may be wise to define a 'tx metadata' struct and wrap each tx type in a container that includes the metadata, then store those containers in the variant.
<dangerousfreedom> Just a question for this module. Would it be in wallet3? If so, that means we are accepting making legacy transactions too?
<rbrunner7[m]> That would have been my proposal as well, after learning about the extended back-and-forth for the designs of the proofs
<dangerousfreedom> Or would that be something for wallet2 transaction period?
<rbrunner7[m]> Which module?
<dangerousfreedom> Shalit's one
<rbrunner7[m]> That's just mockup code to demonstrate the general approach
<jberman[m]> wallet3 would still need to recover balances and spend enotes received in legacy txs, so will still need a way to interface with legacy transactions
<rbrunner7[m]> Ah, well, isn't that the starting point of all my thinking? That we will have a wild mix of all kinds of transactions streaming through our programs for a long time?
<UkoeHB> the tx variant is intended for e.g. the daemon which needs to pass txs around generically (I presume)
<rbrunner7[m]> Yes. And maybe also for the wallet interface, if you query. And the RPC stuff.
<jberman[m]> (fyi my matrix client or the matrix bridge in general (?) seems to be a bit buggy. my message about design review didn't send for a while, weird)
<rbrunner7[m]> Modern technology. Is all.
<rbrunner7[m]> Anyway, if somebody can confirm that serialization and those visitors will harmonize as well, I am almost convinced already
<rbrunner7[m]> And not only the single objects have to serialize, also vectors of them, those as members in structs, etc.
<UkoeHB> there is always a way in C++
<rbrunner7[m]> And the general variant serializing stuff probably has to get suppressed ...
<rbrunner7[m]> UkoeHB the optimist. Of course, it's only the question how expensive it is. Say, if we need spaghetti code to serialize if we go for visitors .... :)
<rbrunner7[m]> But well, I am certainly not the C++ crack here. Any tackers to study that particular point in, say, the next two weeks or so?
<rbrunner7[m]> *takers
<rbrunner7[m]> I think if we settle that point the way to start working on the daemon would be, at least in theory, open
<rbrunner7[m]> And maybe it also will lead to some nice Seraphis library extensions
<UkoeHB> not me, I have other things to do
<rbrunner7[m]> If shalit is enthusiastic about it, we could try something together.
<dangerousfreedom> It would be nice if it paves the way for a deamon :)
<shalit[m]> rbrunner7[m]: I would love to try!
<rbrunner7[m]> Ok, sold!
<rbrunner7[m]> If we get totally confused, we will prod jberman to explain things to us noobs
<rbrunner7[m]> There is no problem with C++ version, or how you call that? Visitors are "old enough" to have wide support?
<UkoeHB> it's working in the current seraphis_lib, no?
<rbrunner7[m]> Yeah, but did we push that already through all the compilers? Or aren't there several?
<rbrunner7[m]> Maybe GitHub CI did that automatically already
<shalit[m]> <UkoeHB> "shalit: is modeling a tx..." <- To be honest, the only purpose of my facade class was to create a nice abstraction for using the variant. but now, I read a bit about visitors and I see that we can just use visitors instead.
<rbrunner7[m]> It's a bit surprising for me, I didn't really expect a (for me) totally different approach to exist, but all the better. Modern C++ to the rescue.
<rbrunner7[m]> Ok, nice, so until we unexpectedly hit some roadblock, we will investigate further.
<rbrunner7[m]> And that will become a general pattern, right? If we want to have some generic enote that can hold old and new, to not always have two vectors to hold them for example, visitors will be the way.
<rbrunner7[m]> And enote V2, V3, V4 ...
<UkoeHB> A variant is good for piping similar data through a workflow.
<UkoeHB> but that doesn't mean always use it
<rbrunner7[m]> By the way, what is a coinbase enote as class? Something third already?
<rbrunner7[m]> Or are only the coinbase transactions something special?
<rbrunner7[m]> UkoeHB: Right. Carefully design per-case. E.g. maybe in the library different from the wallet enote query call.
<UkoeHB> https://github.com/UkoeHB/monero/blob/0fa70bd047149582cca675ebebb388ba342fb548/src/seraphis_main/tx_component_types.h#L60 I'd really encourage reading through the library. It's been a long time since code like this was pushed.
<rbrunner7[m]> Ok, guilty.
<rbrunner7[m]> Something else that anybody wanted to bring up today?
<dangerousfreedom> Regarding my CCS of this week. I thank you for the comments and inputs about it. I'm drafting it again to be more precise. I lowered the extension of my CCS from 18 to 10 weeks, the rate from 48 to 40eur and the weekly hours from 25 to 20h. But still, some tasks are unclear. Hopefully we will reach some consensus soon of what needs to be done and I we will come to a better 'expected' design of the components before I
<dangerousfreedom> start doing it.
<rbrunner7[m]> For me just really encourage people to discuss through issues and comments there, not through long chains of DMs, even it's more or less clear that only two people duke it out. It's good for several reasons.
<dangerousfreedom> That's what I learned.
<rbrunner7[m]> dangerousfreedom[m]: I am sure we will find a good way.
<rbrunner7[m]> People being flexible and listening to each other gives me hope.
<shalit[m]> UkoeHB: one question please, when we have a vector which contains many instances of some variant, every time we would use one of those instances, we would have to check what is the type of this object, and then we will act accordingly, right?
<rbrunner7[m]> In some places of code, problably. In others not, if those visitors do everything you want from the object. I guess.
<jberman[m]> Collecting thoughts/observations, I've got a proposed collective target to shoot for: an alpha version of an updated legacy CLI wallet that utilizes wallet3 (and wallet2 in a "box" as described here https://github.com/seraphis-migration/wallet3/issues/48) that people can start using/testing today
<rbrunner7[m]> But we can study and discuss together, shalit :)
<UkoeHB> shalit[m]: a visitor automatically selects the right method to call
<rbrunner7[m]> That's a pretty high target, but yeah, sooner or later we have to arrive there, and maybe there are no interesting points on the way to there ...
<rbrunner7[m]> In between, I mean
<rbrunner7[m]> But for me frankly the top-level wallet3 classes are still pretty nebulous right now.
<UkoeHB> shalit[m]: or rather, when you visit a visitor then the right method will be called
<rbrunner7[m]> Not even fully sure how many of those we will have at the end, right?
<jberman[m]> top-level wallet3 calsses?
<rbrunner7[m]> Yes.
<rbrunner7[m]> We will see in due course, I am sure.
<shalit[m]> UkoeHB: Ok yeah sounds reasonable, I mean if there are only a closed group of functions that will have to use those instances directly then it make total sense.
<jberman[m]> rbrunner: right, I'm thinking if we set our sights on a concrete target of a release-ready CLI wallet, the answer would be realized sooner rather than later
<UkoeHB> shalit[m]: for cases where you only want one of the subtypes and a visitor doesn't work, you can do this: https://github.com/UkoeHB/monero/blob/0fa70bd047149582cca675ebebb388ba342fb548/src/seraphis_main/enote_scanning_utils.cpp#L805
<rbrunner7[m]> Ok, we reached the full hour. I call it for the meeting, thanks everybody for attending!
````


# Action History
- Created by: rbrunner7 | 2023-03-10T16:59:55+00:00
- Closed at: 2023-03-14T01:00:40+00:00
