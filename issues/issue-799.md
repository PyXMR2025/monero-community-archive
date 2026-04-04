---
title: 'Seraphis wallet workgroup meeting #13 - Monday, 2023-02-20, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/799
author: rbrunner7
assignees: []
labels: []
created_at: '2023-02-17T15:29:26+00:00'
updated_at: '2023-02-24T16:29:20+00:00'
type: issue
status: closed
closed_at: '2023-02-24T16:29:20+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #795 

I don't have a special proposal for something to discuss, we will see what presents itself.

# Discussion History
## rbrunner7 | 2023-02-20T18:52:02+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/799
<one-horse-wagon[> Hello.
<jberman[m]> hello
<dangerousfreedom> Hello
<UkoeHB> Hi
<Rucknium[m]> Hi
<rbrunner7[m]> Anything to report dev-wise from last week?
<dangerousfreedom> I took a week off and I'm trying to catch up with the discussion of implementing a new curve...
<dangerousfreedom> It is crazy how things move around here. Some days ago people were too conservative to change the password-encryption algorithm and now we are talking about completely changing the underlying crypto. Love it. :p
<dangerousfreedom> I have many questions though as I couldnt really follow the conversation and didnt do my homework yet to see how mathematically things would work. Would someone be kind to answer them or point me to the answer?
<dangerousfreedom> Moving from CLSAG to Grootle proofs means changing proof size from linear to logarithmic (which enables us to have more ring members with the same transaction size) though the verification time is still linear. So far I believe I understood the math behind. Now you guys are also proposing to upgrade the verification time by somehow implementing a new curve that uses zk-SNARKS proofs to go for logarithmic (or even
<dangerousfreedom> constant) verification time, are these phrases accurate?
<rbrunner7[m]> I think it's still a bit early for answers regarding the curve switch ...
<rbrunner7[m]> I think that's one easy-to-make misunderstanding: Nobody and nothing is going "SNARKs" .... yet. But we want to prepare
<rbrunner7[m]> Without changing everybody's address yet again a few years down the line
<dangerousfreedom> My questions so far are:
<dangerousfreedom> 1) Is it possible to keep the Grootle proofs for the moment but change the underlying crypto to provide the ability to change into something like zk-SNARKS in the future?
<dangerousfreedom> 2) Do you think we should "lock-in" the new crypto but deploy a new membership proof in the future and launch Seraphis with the Grootle proofs?
<dangerousfreedom> 3) What is your best feasible scheme (considering the launch of Seraphis in 2 years) of membership proofs that we should have/try for the moment?
<dangerousfreedom> rbrunner7[m]: Yeah, okay. But I'm really excited with the idea of bringing logarithmic (or constant) verification time to Monero. I believe we would have an user experience similar to Bitcoin if we achieve that. Kudos to kayabanerve and tevador. :) 
<rbrunner7[m]> Maybe kayabanerve and/or tevador and/or UkoeHB will pick up your questions later.
<kayabanerve[m]> Hello
<rbrunner7[m]> It's certainly something exciting if - big if - we can pull it through successfully.
<rbrunner7[m]> The Rust capable people had quite some discussion here over the week. Does anybody know whether they already reached some tanglible results?
<kayabanerve[m]> dangerousfreedom[m]: We're not doing SNARKs now
<kayabanerve[m]> Seraphis will be Grootle. The point is eventually upgrading to SNARKs
<dangerousfreedom> kayabanerve[m]: I believe so :p
<dangerousfreedom> But what you think that could replace the grootle proofs?
<dangerousfreedom> Okay
<dangerousfreedom> So you think it could be something like the second point of my questions?
<kayabanerve[m]> Regarding Rust, that's been generally elided with tevador's proposal of a distinct cycle.
<rbrunner7[m]> I think Tevador did some benchmarks and find out it's not all rosy with that "Pallas" curve. Did I get that right?
<rbrunner7[m]> "elided" as in faded a bit into the background for the moment?
<kayabanerve[m]> We both did. Pallas is decent slowly. Tevador has a proposal for a distinct cycle accordingly.
<kayabanerve[m]> Elided, as in, the point of Rust was to not need to make a new curve impl. With tevador positing a new curve, we do need a new impl.
<rbrunner7[m]> Ah, surprise :)
<kayabanerve[m]> Since we need a new impl anyways, I don't care to suggest doing it in rust.
<tevador> If the new curve passes security review, I'm willing to do a C implementation (possibly with some assembly).
<rbrunner7[m]> Is Tevador even allowed to "make a new curve"? :) No, seriously, would that need some kind of study, review, checks?
<kayabanerve[m]> dangerousfreedom[m]: "something like the second point": Sure, except I'm not saying lock anything in. Seraphis is already launching with Grootle and we're already discussing how to ensure upgrades, which are possible by Seraphis's design, remain feasible.
<tevador> Ideally, Seraphis should be implemented on top of a generic group and not care about the curve underneath.
<kayabanerve[m]> It's from a modification of the scripts used for Pallas, which provide tooling to evaluate security of curves.
<kayabanerve[m]> While Ed25519 specifically has caused review, none of that review is specific to Ed25519, yet rather twisted Edwards curves, or curves with a cofactor 8, or...
<kayabanerve[m]> So we don't need curve specific review. We just need to properly identify and apply review. The newly posited curves are of the same structure as Pallas, with a better choice of primes. We can run the provided tooling, and then there's someone specific I want to get feedback from.
<kayabanerve[m]> But there's no reason we can't put forth a new curve.
<rbrunner7[m]> Ok, interesting.
<rbrunner7[m]> So I guess this will take its course over a few weeks until we have a solid proposal on the table.
<dangerousfreedom> kayabanerve[m]: Okay. Seems that we are being more conservative than I thought then. Good that we will keep Grootle proofs for a while instead of getting rid of it even before launching :p
<tevador> The new curve should be equally secure as Pallas or secp256k1 (used by Bitcoin).
<tevador> dangerousfreedom: we are not proposing any changes to Seraphis except to swap out the curve.
<dangerousfreedom> Okay
<tevador> Jamtis would also stay the same, except one fo they keys would be on the new curve.
<rbrunner7[m]> Only one key?
<tevador> yes, the spend key
<dangerousfreedom> Okay, a bit more reassuring
<ghostway[m]> Have you seen the rust bindings implementation thing dangerousfreedom[m]?
<tevador> the rest would stay on Curve25519 
<kayabanerve[m]> I thought it would've been all but one key
<dangerousfreedom> ghostway[m]: No. What is that?
<rbrunner7[m]> Doesn't matter much, I guess, key is key, no?
<rbrunner7[m]> Regarding work to implement, I mean
<tevador> The address has 3 keys: 1 would be on the new curve and the remaining 2 would stay on Curve25519 for DH
<ghostway[m]> I've made a demo on how you'd incorporate rust into the project. It's not too pretty (and I'd prefer to stay all-c++), but it's very possible
<kayabanerve[m]> Ah, there's two x25519 keys. Sorry, I thought there was just one.
<tevador> https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#511-address-keys
<tevador> D2 and D3 are only for DH
<ghostway[m]> Ah note there's a good library (zcash's one) for the pasta curves 
<tevador> Yes, Pasta has a rust implementation. But Pallas is about 60% slower than the proposed curve.
<ghostway[m]> Ah right (because of its prime I guess? Still need to learn more)
<ghostway[m]> What's the proposed curve? Does it have a cycle with vesta?
<tevador> It's a distinct cycle of two new curves. Actually we have 2 cycles that are being evaluated.
<rbrunner7[m]> Ok, if that's it more or less for the curves for the moment, and as we have time left, I have something I would like to get peoples' opinion about
<rbrunner7[m]> It's about reviews
<ghostway[m]> That's cool, is there an issue about that? tevador
<ghostway[m]> Oh ok 
<rbrunner7[m]> If you already made PRs to Monero yourself, or if you follow dev work closely, you know that getting reviews can be quite hard
<rbrunner7[m]> Some PRs wait for quite some time before they get a review
<shalit[m]> Hello
<rbrunner7[m]> And it seems sometimes there simply is no worktime around for reviews
<rbrunner7[m]> A natural idea how to achieve some improvement here is offering bounties for reviews
<tevador> If we go forward with the new curve, this will become relevant: https://github.com/UkoeHB/monero/issues/7
<rbrunner7[m]> I think there is already one running for one the PRs. Is that correct? Or is there a bounty on some implementation?
<UkoeHB> the blake2b test vectors from JoshBabb[m] 
<dangerousfreedom> But I'm still curious what is going on in your minds kayabanerve[m]  and tevador  regarding the substitute of the grootle proofs. Do you have a particular scheme that you think could be possible to replace it?
<JoshBabb[m]> :sweat_smile:
<rbrunner7[m]> To implement those test vectors, or to review done implemenation work?
<ghostway[m]> UkoeHB: Yea, that's the only one
<JoshBabb[m]> two months later
<ghostway[m]> To make them
<rbrunner7[m]> Ah, ok. Because I was thinking that bounties on reviews might a bit problematic.
<JoshBabb[m]> I really need to do that...  Personal time management issues, sorry
<tevador> dangerousfreedom: yes, we have at least two options and both require a curve cycle that Ed25519 doesn't have: https://github.com/monero-project/research-lab/issues/100#issuecomment-1423154798
<rbrunner7[m]> You see what I mean? How would you check whether the review was done in a resposible way?
<UkoeHB> review bounties don't make much sense, we should just hire reviewers as needed
<kayabanerve[m]> dangerousfreedom[m]: I'd be happy to PM you.
<rbrunner7[m]> And hire trustworthy "professional" reviewers?
<rbrunner7[m]> Ah, I see, like we did in the past for bigger things, like BP and BP+
<rbrunner7[m]> Ok, then it seems my worries were largely unfounded.
<BusyBoredom[m]> Another idea for reviews: Some organizations make reviews happen faster by having some automation that randomly tags a recent contributor for each PR and asks them to review it. This works well in my experience, because reviews suffer heavily from the bystander effect (people expect someone else to pick it up, and so nobody feels ownership). If the person tagged doesn't have the technical expertise to complete the review,
<BusyBoredom[m]> they are responsible for finding someone who does. 
<rbrunner7[m]> Do you have some good example? Would be interesting to research a bit.
<rbrunner7[m]> Of some organization that does this
<rbrunner7[m]> In any case, as we will produce much new code, and in fact koe already did, we will have a very big need for review, big and small
<BusyBoredom[m]> Sure, here's an example of the bot in action on the rust-lang github: https://github.com/rust-lang/rust/pull/108264
<BusyBoredom[m]> Just picked rust-lang as an example of an organization that does this, but this obviously isn't related to rust in any way. 
<rbrunner7[m]> Ok, if I don't forget, I will look around a bit. Sounds like an interesting approach. I doubt a bit we have enough people for that, but who knows.
<BusyBoredom[m]> +1
<rbrunner7[m]> Anything else for today?
<rbrunner7[m]> Alright, thanks for attending, read you again next week :)
<dangerousfreedom> I'm fine with some answers. Thank you rbrunner!
<kayabanerve[m]> Bye y'all
<ghostway[m]> See you
<ghostway[m]> I think that's interesting, but haven't seen it implemented tbh
````

# Action History
- Created by: rbrunner7 | 2023-02-17T15:29:26+00:00
- Closed at: 2023-02-24T16:29:20+00:00
