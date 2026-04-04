---
title: 'Monero Tech Meeting #159 - Monday, 2026-03-02, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1347
author: rbrunner7
assignees: []
labels: []
created_at: '2026-02-27T12:07:01+00:00'
updated_at: '2026-03-02T20:06:23+00:00'
type: issue
status: closed
closed_at: '2026-03-02T20:06:23+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1344).


# Discussion History
## rbrunner7 | 2026-03-02T20:06:23+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1347
<j​berman> *waves*
<s​needlewoods> Hey
<j​effro256> Howdy
<v​tnerd> Hi
<r​brunner7> Alright, on to the reports for last week. Me: Completed my analysis of Polyseed use in Monero wallets and wrote a report: https://github.com/tevador/polyseed/issues/13#issuecomment-3980281619
<r​brunner7> Unsure how to proceed
<s​needlewoods> Began to look deeper into the exceptions in wallet-rpc and so far it looks like most of them don't need special attention.
<s​needlewoods> My idea was to add a member `m_exceptionPtr`, but didn't come far enough for a nice writeup like rbunners proposal, or even compare the proposals.
<s​needlewoods> here is the idea quickly thrown into a pseudo patch https://paste.debian.net/hidden/d34a0690
<s​needlewoods> rburnners proposal: https://github.com/monero-project/monero/issues/10343
<j​berman> We got a minor refactor of FCMP++ type organization / dependency mgmt merged, I continued on upstream FCMP++ crypto PR's in prep for an audit, and reviewed beta FCMP++ scaling & implemented the new "max" fee priority category wallet-side
<j​babb> I should do you a favor and figure out exactly what Stack Wallet does... we use Cake Wallet's monero_c with some customizations but not polyseed_dart iirc
<j​babb> s/figure out/remember what we did and look it up
<s​needlewoods> rbrunner* sorry, butchered your name twice
<r​brunner7> Josh Babb: I did look already at Stack Wallet and didn't see any surprises there. Surprise would have been use of Polyseed "native" encryption.
<r​brunner7> SNeedlewoods: No problem :)
<j​babb> Stack Wallet should go in the `B) Apps that only offer basic Polyseed support` category for now
<j​effro256> Me: talking to an potential auditor atm and reworking the Rust lib for the PQ changes
<j​babb> I'll see what we can do about the rest sometime
<jpk68> I discussed the encrypted Polyseed issue with the Monfluo maintainer
<jpk68> We decided on supporting it eventually, but first just implementing some UI thing to notify the user
<r​brunner7> Josh Babb: Yes, I would say B) currently for Stack Wallet is correct
<j​berman> Question: so Cake Wallet doesn't support creating a new wallet with a polyseed + seed offset? But it *does* support restoring such a wallet?
<r​brunner7> Yes.
<r​brunner7> That's one way to do it, I guess.
<j​babb> that's likely how Stack Wallet would do it
<j​babb> we're averse to showing the user too many ways to lose their funds, but if they need to restore it it should be available
<j​berman> For any wallet2 wallet, I would think the seed offset is the more critical feature to support, since the wallet already does encrypt the keys file where the seed lives using the wallet password
<r​brunner7> I guess it depends on your view of Polyseed encryption, whether you "like" it, or whether you see problems with plausible deniability ...
<j​babb> as an advanced user I love it.  but I, too, have lost funds due to forgetting passphrases I didn't store with seeds
<r​brunner7> If you want to support both encryption and seed offset at wallet creation, you have to ask the user a potentially confusing question.
<j​berman> > B) simply ignore the feature bit, with the very unfortunate result that they take the encrypted bits as the private key to use and restore an altogether different wallet without warning, which is dangerous and can lead to confusion.
<j​berman> This sounds like a clear bug in those wallets :/ the feature bit AFAIU should be a totally distinct bit from what's used for entropy in deriving the seed
<jbabb> +1
<j​berman> ah wait, I misunderstood, I see
<j​babb> how so? that's my understanding
<j​berman> the entropy bits in the seed are already encrypted, and are meant to be decrypted with the seed's passphrase
<j​berman> so it's not using the encryption feature bit as entropy, rather just using the encrypted entropy bits as private key
<jbabb> +1
<j​berman> but yes still a clear bug
<r​brunner7> I have a strong opinion that for *restore* all wallets should standardize on Cake Wallet's method, that can restore everything, except combinations that don't make sense
<jbabb> +1
<jpk68> +1
<r​brunner7> What they do on wallet *create* is another story, and I wouldn't mind author's personal preference influencing that
<j​berman> "except combinations that don't make sense" -> what's an example of a combo that doesn't make sense?
<s​needlewoods> With "combinations that don't make sense" you are referring to seed offset + Polyseed encryption?
<r​brunner7> What do people think, do we need a proper "Polyseed spec" discussion first, before I go on and implement anything? Whether we see seed offsets with Polyseeds as "discouraged because out of spec"? Or are we pragmatic here; in any case, a handful of wallets do that now, so ...
<r​brunner7> jberman: Encrypting *and* seed offset, basically
<j​pk68> It would be nice to have a standardized, 'suggested' spec
<jbabb> +1
<s​needlewoods> >Plus, as argued in this thread, plausible deniability can be seen as better with seed offsets.
<s​needlewoods> I thought this argument meant it could make sense to have encryption + seed offset
<j​berman> I follow. I guess I don't understand why there is the option to either encrypt OR offset. Seems the effect is the same in either case at least from initial look?
<r​brunner7> Not sure what you mean. The effect of both is an additional level of protection, more or less of the same strength. So the two mechanisms are somewhat redundant, but now Cake Wallet created facts by using encryption, so we probably can't kill that anymore.
<r​brunner7> If it was a small wallet maybe, but the biggest smartphone wallet is a bit unfortunate
<r​brunner7> SNeedlewoods: Encryption is "visible" because of the set feature bit. A seed offset is not
<j​berman> Looks like the polyseed spec didn't define a seed offset because @tevador expected the encryption feature to take its place. Then wallet implementers ended up implementing the offset also
<r​brunner7> I think so as well, yes. But not sure whether using a seed offset really belongs into the Polyseed spec?
<r​brunner7> In any case, wallet app writers did not care and went ahead anyway, and the result is at least sensible. Just not right now on the restore side, if you encrypt.
<j​berman> I personally don't immediately have a strong opinion on best direction here. Need to think more on the discussion
<j​berman> it seems like it does, because the encryption feature is essentially the same thing
<j​berman> except that the offset has an additional layer of plausible deniability as pointed out
<r​brunner7> Alright, a change of subject then:
<r​brunner7> Are the necessary people here to talk about possible rewrite of FCMP++ in C++, like it came up in conjunction with dangerousfreedom  's proposal to add FCMP+ to this Monero inflation webapp? And does it make sense to talk about it today?
<r​brunner7> kayabanerve left a lot of interesting info here a few days ago that it should be doable.
<r​brunner7> I guess it's still quite a job, and not the easiest one ...
<j​babb> iirc it was deferred because it'd be quicker to get to FCMP++ without reimplementing the helios/selene curve "stack"
<r​brunner7> Well, "quicker" is not necessarily the main goal if you want to *verify*, and make sure there is no inflation, as I see it
<jbabb> +1
<r​brunner7> I mean, *really* verify, in an (almost) independent way
<j​berman> I think it comes down to if dangerousfreedom is interested in attempting it in C++. I agree with boog that a C++ rewrite could be more beneficial because it can actually be used in monerod, but a rewrite in python would also be beneficial (another deep eye on the impl & another impl that could be easier to read than rust)
<r​brunner7> Does this need somebody who is really *good* with C++? And also knows Rust, to make it not too easy? Or isn't that too hard in the case of the particular code on hand?
<j​berman> I don't think skill with C++ is nearly close to as relevant as skill with actually implementing the crypto
<r​brunner7> Hmm, so it's more about quite challenging crypto then, in your opinion?
<j​berman> I think so
<r​brunner7> Is FCMP++ currently in the stressnet daemon by binding to Rust code?
<jbabb> +1
<j​berman> yes
<r​brunner7> So we would'nt introduce a potentially problematic dependency if dangerousfreedom decides to attack a rewrite, but needs much longer than anticipated
<r​brunner7> (a time dependency)
<j​berman> I implemented *some* C++ crypto over here so you can kind of get a taste for some of the C/C++ involved with that: https://github.com/seraphis-migration/monero/issues/294
<j​pk68> I'm not very qualified to talk about this, but it is worth noting that the Rust implementation which is being used in the stressnet has several of its own dependencies
<j​pk68> Like, more than 5 IIRC
<j​pk68> They're from an online registry (crates.io) so there could be some concern over supply chain attacks
<j​berman> I mean it likely would end up taking some C++/C skill to do. At the end of the day, if there's a python impl, it would maybe make a C++ impl easier to implement too just to have another source to consult on possibly trickier code
<j​babb> https://github.com/seraphis-migration/monero/blob/fcmp%2B%2B-stage/src/fcmp_pp/fcmp_pp_rust/Cargo.toml
<r​brunner7> Ok. My advice to him was to open a CCS just for about 2 weeks of intensive study what possibilities there are, and arrive at reasonably good time estimates
<b​oog900> I wouldn't even say the main monerod repo has to move dangerousfreedom @dangerousfreedom's impl, if it was to be done. I think even a fork of monerod with their impl would be good and better than just doing it in python.
<jbabb> +1
<j​babb> more useful for actual code/software, potentially less academically beneficial
<j​babb> a python impl is useful in and of itself as a reference for academics imo--hard to measure those sorts of benefits tho
<j​babb> but they come in papers later on
<r​brunner7> Don't want to talk down anybody, or discourage, but when an IQ > 150 guy tells me "It's doable", it doesn't mean yet that *I* can do it as well ...
<j​berman> It's not going to be an easy task. If danger is much more inclined to implement in python, then I think there would still be wider benefits to doing so
<r​brunner7> Is Python to Rust any significant problem?
<r​brunner7> Because as we can see, there a tail of dependencies waiting
<jbabb> +1
<r​brunner7> from that Cargo.toml that was linked above
<j​berman> not sure what you mean
<r​brunner7> If you write core FCMP++ in Python, can you wait with writing Selene of whatever in Python and use that in Rust for the time being?
<r​brunner7> or the GBP
<j​babb> yes you can use ffi to bridge things together and defer work but part of the point would be to make the second implementation
<r​brunner7> Sure, as an end goal
<r​brunner7> That unfortunately may be out of reach, with some bad luck ...
<j​babb> that Cargo.toml is a good example of a pretty short dependency list too.  its monero-oxide dependency also only use a small amount of deps: https://github.com/monero-oxide/monero-oxide/blob/main/Cargo.toml
<j​babb> it can be done in c++ and python, just needs some motivation, gumption, and funding
<j​berman> hrm, I anticipate the python code will end up with dependencies itself too, and it won't necessarily make sense to say we should swap out Rust stuff for python stuff (for a host of other reasons as well, not just on cutting dependencies)
<r​brunner7> Cool, TIL "gumption" :)
<jbabb> +1
<j​berman> (speed and safety being the big ones too)
<r​brunner7> Ok, I see. So everything clear as mud right now, basically
<j​berman> The core benefits of a python impl: a secondary impl that acts as a sort of review on the crypto code, a reference impl for academics and/or others interested in learning how FCMP++ works
<rbrunner7> +1
<jbabb> +1
<j​berman> The core benefits of a C++ impl: a secondary impl that could be used to eliminate dependencies from the Rust code in a C++ monero daemon impl, in addition to a secondary impl that acts as a sort of review on the crypto code
<r​brunner7> Hmm, yes, but you probably still won't fully get rid of Rust dependencies, for the wallet
<j​berman> Python impl is likely somewhat easier to implement at the end of the day, but the main hard part imo is probably going to be the math and not making the language do what you want
<j​berman> well if the whole of helios selene lib & FCMP++ prove / verify is rewritten in C++ then it's theoretically possible to get rid of the Rust deps
<j​berman> so yes, I should have said monero daemon *and* wallet impl
<r​brunner7> Ok, nice. But then with regard to problems and optimizations you have to babysit *two* mission-critical implementations
<r​brunner7> And you can have the opinion that we shouldn't put our energy into producting yet more C++ code ...
<j​babb> well the python isn't critical and the introduction of a second implementation should be approached with care and with some in depth stressnet (splitnet) style testing to see if we can force chain splits with one or the other impl mining and producing edgecases or being malicious
<r​brunner7> If we have it already in Rust, I mean
<jbabb> +1
<r​brunner7> Yes, I mean that's an argument for a Python implementation, to be used primarily for the Monero inflation app, which after all is not mission critical
<j​babb> more c++, more rust, more python... :) let's get some go and the language of your choice into the mix... the only risk is when alternative implementations aren't faithful to the original (even to its bugs!) and chain splits occur
<r​brunner7> Touché
<j​berman> I think it's valid to eventually want monerod/wallet code entirely in C++, and a C++ impl moves closer to that than a python impl. Although yes, it's a whoooooole lot of work to get that code to production ready
<jpk68> +1
<r​brunner7> Probably even with external code reviews, if we are really serious, right?
<jbabb> +1
<r​brunner7> Ok, to this grumpy old boomer this all does not look like it will happen anytime soon. But I let developments surprise me.
<r​brunner7> Ok, discussions can of course continue, but let me close the meeting proper at this point. Thanks everybody for attending, read you again in 1 week!
<s​needlewoods> Final thought on Polyseed, as far as I understand it right now, I like the way Cake did it and IMO you can go for a similar implementation.
<s​needlewoods> So that for creating a wallet you could use Polyseed with the option to either encrypt or not.
<s​needlewoods> If you want to create a new wallet with Polyseed and seed-offset, you would 1. create an unencrypted Polyseed and 2. use that mnemonic to restore the wallet, which sees it's an unencrypted Polyseed, so if you provide a password that will be used as seed-offset.
<s​needlewoods> thanks everyone, good meeting, cu
<v​tnerd> One small benefit would be to wallets. They now need a c++ and rust runtimes to work. If a c++ impl was available it would remove the rust requirement. And a bug would be less problematic (alhough if funds get locked ...)
<jpk68> +1
<v​tnerd> Ah Berman basically said same thing
````


# Action History
- Created by: rbrunner7 | 2026-02-27T12:07:01+00:00
- Closed at: 2026-03-02T20:06:23+00:00
