---
title: 'Monero Tech Meeting #106 - Monday, 2025-02-03, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1150
author: rbrunner7
assignees: []
labels: []
created_at: '2025-01-31T16:33:14+00:00'
updated_at: '2025-02-03T18:55:23+00:00'
type: issue
status: closed
closed_at: '2025-02-03T18:55:22+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1146).

# Discussion History
## rbrunner7 | 2025-02-03T18:55:22+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1150
<d​oedl...:zano.org> I read nowhere that the contest is limited to new faces; otherwise ogs start this race at the finishig line :)
<s​needlewoods> Hello
<j​berman> The primary goal is faster code, however we get there doesn't make a difference imo
<j​berman> *waves*
<r​brunner7> Let's go quickly through the reports, to have that out of the way and discuss the contest :)
<r​brunner7> I reviewed SNeedlewoods 's Wallet API PR. Found no problems.
<j​effro256> I think this is good, especially for the narrow contest of Helios/Selene since Selene field arithmetic is exactly the same as Curve25519 field arithmetic, and it would more or less be a matter of transcribing SUPERCOP or some other fast implementation of your choice to Rust
<s​needlewoods> As you may have seen, I published a CCS proposal and started to investigate the tasks
<j​effro256> Or maybe Helios? One of the two shares the same field
<j​effro256> I forgot
<s​yntheticbird> hi
<j​berman> Selene you were right
<j​effro256> Howdy btw
<r​brunner7> For the log, jberman 's musings about the scope of the optimization competitions: https://paste.debian.net/1348220/
<j​berman> my report: implemented FCMP++ tx construction, got a test set up that's failing on verify (since verify is unimplemented), have been discussing aspects to the impl with jeffro256 , code is over here: https://github.com/j-berman/monero/commits/fcmp%2B%2B-dev/
<j​berman> Also started thinking through the FCMP++ tests, and wrote up the above proposal / rationale to change the contest to the more general approach of speeding up prove/verify/tree building versus the more narrow helioselene curve arithmetic and ec-divisors
<jeffro256> +1
<j​berman> Started thinking through the FCMP++ contest tests*, tbc
<r​brunner7> So I get it there are quite a number of possible approaches how to specify that contest? A wide-open fields, so to say, with corresponding difficulties to decide?
<r​brunner7> *field
<d​oedl...:zano.org> the jury is prohibited from participating i suppose. who would the jury be?
<r​brunner7> Hmm. Why? Being in the jury won't allow to magically produce speed-ups I would say?
<d​oedl...:zano.org> then its a house party.
<s​yntheticbird> love the expression
<j​berman> Sure
<d​oedl...:zano.org> ok - wish you all the best
<j​effro256> I was thinking of probably sitting out the competition anyways since I think my time is best put to use on integration work at least until we hit testnet, but I would be okay with judging if that's alright with everyone  else
<j​berman> I don't plan on participating in the contest, this isn't my wheelhouse. I intended on being part of the jury. Thinking about discussing with Cypher Stack to jump aboard the jury as well if interested
<j​berman> We can include a clause that good-faith jurors won't participate in the competition. Anon submissions are going to be allowed though
<j​berman> You definitely get a +1 from me
<r​brunner7> If Cypher Stack is in the jury, would you look at the persons involved? So one person from Cypher Stack being juror won't block any other employees of theirs to take part?
<s​needlewoods> +1
<s​needlewoods> to jeffro and jberman being part of the jury
<j​berman> seems like a fine approach to me
<r​brunner7> Yeah, jberman and jeffro256 looks like strong default jury ...
<r​brunner7> I can't judge any of that stuff anyway. Ok, I could see that this code runs faster than that code, but speed won't be the single and the absolute criterium, I am pretty sure. Terrible code that is a bit faster than beautiful code won't win the race, I guess.
<r​brunner7> And here we have subjectivity where a "no juror takes part in the contest" may make sense - who could judge their own code for "beauty" in any objective way, so to say.
<j​effro256> That and let's say that one team optimized prove(), and the other verify() must more than the other team, how do we decide who wins?
<j​effro256> *much more
<j​berman> I was thinking 1 distinct prize for prove, 1 for verify, 1 for tree build's hash_grow
<jeffro256> +1
<r​brunner7> What's the difference between "prove" and "verify", in simple terms?
<r​brunner7> Is "prove" building a proof?
<j​effro256> That's fine. One problem with that would be if each implementation required wildly different techniques for the underlying lower level arithmetic. Do we keep in both? Or try to merge them?
<j​berman> yep
<j​effro256> In Monero in general, wallet does "prove", node does "verify"
<r​brunner7> I see.
<j​berman> If there are wildly different, but acceptable distinct techniques that yield a faster prove and a distinct technique that yields a faster verify, then I would think the contest is a success and we may end up keeping both (assuming they aren't merge-able)
<jeffro256> +1
<r​brunner7> What about assembler code? Allowed? Allowed if delivered for *all* relevant architectures?
<j​effro256> That *does* increase review/audit costs, but I guess we will have to wait to make the value judgement to determine if the performance is worth that cost
<j​effro256> I would prefer that platform-specific code, at least for the verification functions, shouldn't be allowed
<r​brunner7> It would probably complicate things considerably.
<r​brunner7> Just thinking about it because it's often a way to optimize ...
<j​berman> IIRC the initial idea behind targeting wasm was to ensure it would work on all targets: https://github.com/kayabaNerve/fcmp-plus-plus-optimization-competition
<jeffro256> +1
<j​effro256> `verify()` is really the critical one that we get *sound*. If we have a good `verify()` and bad `prove()`, then the proof will fail, but we won't get infinite inflation. I guess absolute in the worst case is that a intentionally malicious `prove()` might leak the true spend and ruin everyone's privacy
<r​brunner7> I guess it's a good idea to submit your alternative approach also to the MRL audience on Wednesday
<r​brunner7> Alright, looks like that's it about the contest for the moment. Something else to discuss today?
<j​effro256> Should we allow C that can FFI into Rust, assuming it compiles on all valid architectures, including WASM? I think so, just as long as the C implementors are aware that the FFI overhead *will* be counted into their benchmark
<j​effro256> *Portable C* at that
<r​brunner7> Is C sometimes that much faster than Rust to even consider that as a contestant?
<j​effro256> For overflowing/saturating arithmetic and complicated array reads, sometimes, yeah
<r​brunner7> Does not look like much future-proof to me, frankly. Shouldn't we have a long-term goal of pure Rust code?
<j​berman> I would be ok with C too on those grounds. The original specification excluded unsafe code, and I believe the FFI would necessitate unsafe code. The crustaceans will not be happy about it
<r​brunner7> So later execution may pass from C++ code to Rust code and there down to some parts in C code? Shudder :)
<vThor> :/
<r​brunner7> Well, maybe we should not worry too much about that - IMHO - quite unlikely outcome of the contest ...
<r​brunner7> Alright, I think we are good to close the meeting proper. Discuss away of course after it. Thanks for attending everybody, read you again in 1 week!
<j​effro256> Thanks!
<j​effro256> Sorry one more thing rbrunner7 : would you be willing to give me and jberman write access to the `seraphis-migration` repo?
<r​brunner7> Yup, have that on my todo-list :)
<s​yntheticbird> *"unsafe code is just the dark side of Rust. and any good crustacean know how to will this power"* or something like that coming from the Rustonomicon.
````


# Action History
- Created by: rbrunner7 | 2025-01-31T16:33:14+00:00
- Closed at: 2025-02-03T18:55:22+00:00
