---
title: 'Seraphis wallet workgroup meeting #12 - Monday, 2023-02-13, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/795
author: rbrunner7
assignees: []
labels: []
created_at: '2023-02-10T15:59:24+00:00'
updated_at: '2023-02-17T15:29:40+00:00'
type: issue
status: closed
closed_at: '2023-02-17T15:29:40+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #792

Two days ago now there was a very interesting discussion in the MRL IRC channel that starts here and continues on the next day: https://libera.monerologs.net/monero-research-lab/20230208#c201828

@kayabaNerve proposed, if I got the terminology right, to "switch the curve" together with the introduction of Seraphis and Jamtis.

It seems that such a switch could make possible quite interesting technological upgrade paths for Monero in the future without causing too much pain for Monero users, but could also make the work needed for introducing Seraphis and Jamtis quite a bit bigger. Therefore this could directly influence our workgroup and what we try to build.

If that's ok, I would love to have @UkoeHB and/or @kayabaNerve explain to us "crypto noobs" in the workgroup on a high conceptual level what this is about, and maybe speculate a bit what this could mean for the Seraphis migration project, e.g. how much bigger work could become, and how strongly this could impact Seraphis library and wallet.

One thing that I personally still wonder about is why doing this "curve switch" later, e.g. a few years after the hardfork to Seraphis, would be considerably more difficult, or disrupting for users, than switching early.

# Discussion History
## rbrunner7 | 2023-02-13T19:20:27+00:00
````
<rbrunner7[m]> Hello! Meeting time. https://github.com/monero-project/meta/issues/795
<rbrunner7[m]> Who is around?
<UkoeHB> hi
<one-horse-wagon[> Hello.
<kayabanerve[m]> Hello
<rbrunner7[m]> Already 3 months of meetings. How time flies.
<Rucknium[m]> Hi
<dangerousfreedom> Hi
<jberman[m]> hello
<rbrunner7[m]> Alright. Maybe first, anything to report from dev work over the last week?
<ghostway[m]> Hello
<ghostway[m]> So maybe I'd start?
<rbrunner7[m]> Yes
<shalit[m]> Hello
<ghostway[m]>  the checkpoint cache koe has suggested is ready for feedback apart from styling and the pruning strategy; the rust demo has been sent if someone hasn't seen it, but it will probably be a little cleaner, and I think that's it
<jberman[m]>  +1
<rbrunner7[m]> +1
<plowsof11> +1
<rbrunner7[m]> We are already slowing rusting :)
<rbrunner7[m]> Ok, if other people are still on the way with what they already worked on last week, we can switch to my proposed discussion, as per meta issue
<ghostway[m]> Ah and also, not that I could help in the near future more than others, but I've started to look at Halo's docs which are quite cool and clrar
<jberman[m]> can you drop a link to the checkpoint cache code ghostway ?
<UkoeHB> ghostway[m]: can you make a PR against my branch? I can leave comments on that
<ghostway[m]> In ~30 minutes
<kayabanerve[m]> https://github.com/monero-project/research-lab/issues/100#issuecomment-1423491782 is the best current summary of the SNARKs discussion I'd like to put forth
<ghostway[m]> Ok
<rbrunner7[m]> As described in the issue, there was a proposal last week, mostly by kayabanerve , to change something quite fundamental in the "crypto" that Monero uses
<rbrunner7[m]> And as we here are the ones that try to implement Seraphis, I think it would be very interesting to hear what that could mean
<rbrunner7[m]> On a "high" level, what happened in the MRL IRC channel was chock full of stuff only cryptographers understand :)
<UkoeHB> it would mainly mean a big pita to switch
<ghostway[m]> Pita?
<kayabanerve[m]> The summary is:
- Modern ZK-SNARK technology is premised on either pairing or a curve cycle, aka a curve whose scalar field and field element field can be flipped to form another curve
- The pairing solutions are generally not with a transparent setup, hence why we focus on the curve cycle solutions
- Curve cycles are the only known way to achieve a *trustless* *succinct* NARK
- NARKs are the premise on which we can achieve a complete membership proof
<plowsof11> pain in the ass
<ghostway[m]> Ah well I thought it as something else lol
<kayabanerve[m]> UkoeHB: Agreed on PITA, disagree on big.
<kayabanerve[m]> My chicken scratch commentary on moving over:
+ rust
FFI the Pallas lib
Find/replace
Hash to point -> elligator squared
Extra migration step, hopefully not adding an entire migration process
Make sure everything still works
<kayabanerve[m]> ghostway: Already showed how trivially Rust can be added to the project. While their FFI wasn't exactly ready to deploy, it demo'd the very first step. 
<rbrunner7[m]> Well, maybe we could start with having this on a more "ELI5" level. "Changing the curve" would basically mean that we still do ECC, just in another "flavor"? Is that a correct simplification?
<kayabanerve[m]> *I'm premising this discussion on moving to the Pasta curves, distinguished as a cycle of Pallas/Vesta.
<UkoeHB> find and replace does not cut it, there's no way the new API will map 1:1 with what we have
<kayabanerve[m]> Bitcoin uses secp256k1. We use ed25519 for performance. This would be moving into a third option. My advocacy is pallas, tevador expressed interest in finding yet another choice.
<UkoeHB> not to mention the multisig_account thing, which would need a big rework
<kayabanerve[m]> UkoeHB: Mind specifying where? pallas also has 32-byte points and 32-byte scalars. The only API distinction should be the lack of torsion which pallas lets us *simplify*.
<kayabanerve[m]> *If discussing a brand new cryptsystem.  Obviously, there's still work needed on a migration and the current hash to curve is specific to Ed25519
<rbrunner7[m]> After the switch, what's the prediction, will Seraphis and/or Jamtis as cryptographical / mathematical constructs any changes?
<rbrunner7[m]> *need any changes?
<kayabanerve[m]> I, personally, see the only two actual pain points as the hash to point and extra migration step. The hash to point, an algorithm about a 100 lines, would be replaced with an academically formalized option. The extra migration step would be a ~100 byte proof recently published by COPZ.
<UkoeHB> how much of this file could be 'find and replaced'? https://github.com/UkoeHB/monero/blob/seraphis_lib/src/seraphis_crypto/sp_composition_proof.cpp
<kayabanerve[m]> UkoeHB: How does multisig change when we move from Ed25519 to a distinct group? The underlying principle, ECDH, should still be applicable.
<UkoeHB> kayabanerve[m]: sure, but now you need to A) support internal keys of different types, B) implement an account migration path using cross-curve math
<kayabanerve[m]> rbrunner7[m]: Largely no, IMO. The grootle proofs, in theory, are defined over *any* group. There's nothing in them specific to Ed25519.
<kayabanerve[m]> That's how Spark is using them with secp256k1.
<kayabanerve[m]> Uhhhhh
<kayabanerve[m]> A) We already have to do that. RingCT vs Seraphis keys.
<kayabanerve[m]> B) It's a 100-byte proof published under the IACR. It's quite simple.
<kayabanerve[m]> The migration proof should also be possible by anyone who knows the commitments values. There's no requirement the private key is known.
<rbrunner7[m]> UkoeHB: What's your take on this, except for things like maybe multisig: The constructs would stand? And just work on another curve?
<UkoeHB> presumably?
<UkoeHB> I don't really have the energy or gusto to think about it tbh
<rbrunner7[m]> Ok, that's good for me as a prediction, on the level we discuss today :)
<UkoeHB> kayabanerve[m]: you read the multisig account code didn't you? The ECDH is implemented with our library - if you now need to use ECDH with another library, the current code won't work. Just an example of how your 'ezpz' migration path is not so ez
<kayabanerve[m]> While I don't actually suggest a repo-wide F+R and call it a day, for https://github.com/UkoeHB/monero/blob/seraphis_lib/src/seraphis_crypto/sp_composition_proof.cpp
<kayabanerve[m]> rct::key -> seraphis::key, which is a pallas point
<kayabanerve[m]> crypto::key_image -> seraphis::key || crypto::linking_tag
<kayabanerve[m]> sc_mul, sc_mulsub we can exactly define for pallas.  Either as pallas_sc_mul OR we replace importing crypto.h with crypto_pallas.h
<kayabanerve[m]> I'd lean towards the former to prevent conflicts ambiguity at this time.
<one-horse-wagon[> I don't understand why we are considering changes horses in the middle of winning race?  I thought the parameters for Seraphis were already set and they just needed a little more development and then coding.
<Rucknium[m]> IACR preprints aren't really peer-reviewed, are they?
<kayabanerve[m]> None of the code in that file is premised on Ed25519. It's all already abstracted
<rbrunner7[m]> So, basically, we would need support, with a good API, with good performance, maybe in Rust, for calculating with the new curve, then rework maybe quite some code in the Seraphis library, probably not by koe, but his successor in this?
<kayabanerve[m]> unless I'm missing torsion handling in my brief glance
<rbrunner7[m]> one-horse-wagon: We will come to the switching horses in a bit
<kayabanerve[m]> UkoeHB: ECDH is literally just a scalarmul. I'm legitimately unsure what point you're raising.
<kayabanerve[m]> If we replace sc_mul with pallas_sc_mul, the ECDH, where EC stands for elliptic curve, as in, any one of them... will still work.
<Rucknium[m]> Is the paper under the IACR ePrint archive?: "The Cryptology ePrint Archive provides rapid access to recent research in cryptology. Papers have been placed here by the authors and did not undergo any refereeing process other than verifying that the work seems to be within the scope of cryptology and meets some minimal acceptance criteria and publishing conditions."
<kayabanerve[m]> The x25519 DH isn't just an ECDH. AFAIK, the multisig isn't using x25519 though.
<UkoeHB> sure you can duplicate the file, duplicate the maintenance cost
<kayabanerve[m]> Rucknium[m]: I'm unsure if it's peer reviewed. I don't expect it. We'd likely want to have sarang provide review.
<rbrunner7[m]> Anyway, leaving away details, and possible misunderstandings, we are problably still talking about quite a number of months of work to get everything hard-fork ready on the new curve.
<UkoeHB> tradeoffs and work, that's what the migration would be fraught with
<UkoeHB> not saying it definitely shouldn't be done, but be realistic
<rbrunner7[m]> Additional months of work I mean
<kayabanerve[m]> Arguably, sure, it's duplicating the file. I'd point out RCT multisig is already very distinct from Seraphis multisig so we already have two distinct multisig codebases in that regard.
<kayabanerve[m]> I don't see an issue with having the Seraphis multisig be purely premised on pallas.
<rbrunner7[m]> I am also all for "realistic".
<kayabanerve[m]> I'd see it as a month of work. I'm not trying to be unrealistic. I do think this is legitimately abstracted to the point it's largely grunt work to anyone who knows the basics of cryptography.
<kayabanerve[m]> Seraphis itself, of course, is by no means grunt work. It's a complex piece of code I don't mean to diminish.
<UkoeHB> kayabanerve[m]: I abstracted the multisig signing ceremony into a framework that works for both CLSAG and seraphis composition proofs
<kayabanerve[m]> But curves are curves. They're all inter-changeable. The only question is the one we want and if migration is feasible. The existing library for pallas, and COPZ's proof, offers a feasible migration IMO.
<UkoeHB> https://github.com/UkoeHB/monero/blob/8b1db55f8a20a9bdbd050a06b8cd0a5d1915e03c/tests/unit_tests/multisig_signing.cpp#L199
<rbrunner7[m]> So we have additional effort, and some risks, on the one side. Now we could look what is on the plus side. Or, if you like, "Why the hurry"? Or with one-horse-waggon, why switching horses in the middle of the race?
<kayabanerve[m]> UkoeHB: Thank you for clarifying. In that case, yes, I'm likely proposing duplicating those files yet I'd have to check. I'd also note the possibility of using a macro, but leave that for another point in time.
<rbrunner7[m]> That's for me maybe the biggest single question left.
<rbrunner7[m]> What do we gain? Or, what do we prevent?
<kayabanerve[m]> If we don't do it now, it's redoing the entire Seraphis migration in a few years.
<jberman[m]> one-horse-wagon: efficient full chain membership proofs are the ideal. kayabanerve shared research arguing why the ideal path here would require a migration to a new curve. New curve = new addresses. Ideally we wouldn't want to introduce Seraphis and then X years later require an additional migration to a new address when it can be avoided
<rbrunner7[m]> I am confused by the term "Seraphis migration". Please clarify on a EL5 level.
<kayabanerve[m]> Not doing it now, IMO, is either saying:
<kayabanerve[m]> 1) Monero will never have full-chain membership proofs
<kayabanerve[m]> 2) Seraphis address are only usable for a few years
<rbrunner7[m]> Because addresses depend on the curve used, right?
<kayabanerve[m]> Complete regeneration of wallets and addresses.
<rbrunner7[m]> And why number 1?
<kayabanerve[m]> Not to mention koe is discussing how annoying it'd be to have two multisig files for ed25519/pallas. Imagine how annoying it'll be to have two copies of the entire seraphis codebase. One for ed25519, one for pallas.
<kayabanerve[m]> Curve cycles are the only currently known way to achieve succinct ZK-SNARKS with a transparent setup.
<rbrunner7[m]> Why would, without a switch now, "full-chain membership" be impossible for all times?
<rbrunner7[m]> Sorry, that doesn't plausible yet for me.
<kayabanerve[m]> Succinct is defined as small by size and verification time, with arguments over the factor required to be "succinct".
<kayabanerve[m]> Bulletproofs, while capable of arithmetic circuits, are not succinct.
<kayabanerve[m]> They're small. They verify in linear time. They do not verify with logarithmic complexity.
<kayabanerve[m]> When we discuss a full-chain membership proof, each input would do TENS of hashes in ZK. That's difficult to then verify with linear complexity. It'd massively reduce our TPS to the point it likely wouldn't be considered feasible.
<rbrunner7[m]> Mind you, I don't understand what "full-chain membership" is, I just don't get where such a black-and-white missing of a chance for all times should spring up
<kayabanerve[m]> Right now, we have a ring of 16 inputs. Seraphis makes that 128. Full-chain membership means the entire chain is used.
<rbrunner7[m]> You mean we would amass some many inputs that they would be too much for that system to work?
<kayabanerve[m]> It's our last issue re: on-chain privacy.
<kayabanerve[m]> Eh, sure, uniformity, endless discussion there.
<kayabanerve[m]> But we don't have perfect sender privacy. Just perfect sender privacy in a subset Rucknium can attest has been attacked again and again.
<kayabanerve[m]> No. Each TX may take hundreds of ms to verify.
<rbrunner7[m]> 5 years of Seraphis, with rings, and we have too many to even try?
<kayabanerve[m]> Curve cycles means we can have a complete membership proof verify in tens of ms. Not hundreds of ms. The first I'd argue is worth it. The second I think can be agreed to be infeasible.
<kayabanerve[m]> rbrunner7[m]: Mind restating this?
<rbrunner7[m]> I am still working on that "chance missed for all times" point. I mean, if true, that's massively important. You don't want to miss a once-in-a-lifetime chance.
<rbrunner7[m]> I am frankly a little suspicous whether that's really so.
<tevador> The main point is that we don't want to switch to another (third) addressing scheme in 5 years or so to enable SNARKs.
<tevador> If we want Jamtis to last until some future PQ crypto, this is this only time we can switch the curve.
<rbrunner7[m]> That's a reasonable main point to have, but sounds much less dramatic than "new curve now or never" for more fundamental reasons, that I don't understand yet.
<tevador> Switching now means much less pain than switching later.
<kayabanerve[m]> > <@kayabanerve:matrix.org> Not doing it now, IMO, is either saying:
<kayabanerve[m]> > 1) Monero will never have full-chain membership proofs
<kayabanerve[m]> > 2) Seraphis address are only usable for a few years
<kayabanerve[m]> Please see this.
<rbrunner7[m]> Yes, the "never" there irritates me.
<kayabanerve[m]> I said, IMO, it's saying we'll never have full-chain proofs OR Seraphis addresses have an expiry date from the get go.
<kayabanerve[m]> ... except I said how it wouldn't be never? It just involves completely redoing wallets once again, as tevador is now noting?
<one-horse-wagon[> Don't mean to imply anything, but why is it necessary to wait 5 years to switch to snarks if that is your ultimate goal.
<rbrunner7[m]> That we won't be able, like not at all, to go through a second changing of all addresses is an assumption.
<rbrunner7[m]> We have no idea yet how the first one will go, for example.
<kayabanerve[m]> I don't believe anyone said it's necessary. No one has proposed doing with Seraphis at launch though, for complexity reasons. I believe there's a natural understanding it'd be 2-4y out from mainnet when Seraphis itself is still a bit out.
<kayabanerve[m]> rbrunner7: I explicitly list it as an option. I don't know what else you want me to say.
<rbrunner7[m]> Yes, it may well be that we have a misunderstanding on my side somewhere.
<kayabanerve[m]> If you only choose to read the first half of my message, that's on you. I'm here to argue against forcing us into a solution where we do need to change our addresses again in order for complete membership proofs to be feasible.
<kayabanerve[m]> That's the real question. Do we put forth a month or two of work now, to move curves now and prevent needing to move again in the future, for full chain membership proof to remain feasible?
<Rucknium[m]> Having seen a huge number of cryptography-dependent protocols be destroyed or found to have critical exploits over the last 12 months, I question whether  trustless zk-SNARKs are battle-tested enough for Monero. FWIW, I think it's reasonable to "prepare" for trustless zk-SNARKs, but I don't think we should assume that Monero will definitely use them.
<Rucknium[m]> Is there a 5% chance that there is a critical flaw in the cryptography? Probably
<kayabanerve[m]> While yes, we CAN move again in the future, I don't believe anyone wants that and its explicitly against the intent of Seraphis.
<kayabanerve[m]> I will note there's the assumption of feasibility is only via a cycle. I base that on how no one has made a SNARK, that's trustless, without pairings or a cycle. This is a massively hard problem I do not assume will be solved.
<rbrunner7[m]> I think the field is still rapidly evolving. Any danger that we choose the wrong new curve?
<tevador> The pasta curves are from 2020 IIRC
<kayabanerve[m]> While I disagree with how conservative Rucknium is, I do agree this is not currently saying we will deploy any specific code. It's solely saying we won't commit to a path in contradiction with SNARKs (Ed25519, which isn't SNARK friendly).
<rbrunner7[m]> I mean, we switch to that Pallas thingy, and a month later somebody brings a really wonderful system, but on another curve?
<kayabanerve[m]> We could choose a curve cycle, and the next day here about X curves! X curves have O(1) performance and do everything! They're even post quantum secure!
<kayabanerve[m]> In any field, new research can come and make our work dated/inferior.
<kayabanerve[m]> The curve cycle will make ZK-SNARKS feasible. While they may not be the most performant, they should be definitively usable to achieve full-chain membership proofs with.
<rbrunner7[m]> I am just brainstorming, and thinking aloud. I understand only few things until now, and I am eager to learn. Shouldn't be problem, much less a threat to anything.
<tevador> I think we should definitely do some benchmarks between pallas and ed25519 to see the perf impact on Seraphis.
<kayabanerve[m]> Based on current academia, Ed25519 doesn't feasibly enable full-chain membership proofs IMO.
<kayabanerve[m]> So while yes, we can always hear of X new thing making Y better, what we know now is Ed25519 is currently infeasible and pallas is currently feasible.
<rbrunner7[m]> What is "out of context"? What do you mean?
<kayabanerve[m]> tevador: Agreed, though I am worried they'll be used out of context.
<kayabanerve[m]> I'll work on a brief benchmark now...
<rbrunner7[m]> People would use the result to argue in bad faith?
<kayabanerve[m]> I wouldn't be surprised if Ed25519 is 20% faster than the current pallas library, with its years of optimizations and some natural properties.
<kayabanerve[m]> ... eh, 20% I would be surprised by.
<kayabanerve[m]> But the value of pallas isn't in being naturally faster. It's about enabling dramatically less complex algorithms (time-complexity, not academic-complexity)
<kayabanerve[m]> So even if pallas is X% slower, it offers future algorithmics which will execute in log N to Ed25519's N
<rbrunner7[m]> Well, I don't worry about something like 20%. I worry about things like overstretching ourselves, complete project failures and such. That's on the top of my non-cryptographer, mor project-management focussed mind. And here I would love to have some insight into possible risks, and possible rewards.
<rbrunner7[m]> Which I personally already got from this meeting
<rbrunner7[m]> In part
<kayabanerve[m]> The reward, based on current academic understanding, is full-chain membership proofs in the tens of ms, not the hundreds of ms (single core, non-threaded), which I'd argue makes them feasible.
<kayabanerve[m]> The downside is needing an additional proof, which can be argued as far simpler than the eventuality I hope pallas leads us to, and potentially a month or two of dev time (I'd say a few weeks of dev time, yet then a month actually go through discussions).
<rbrunner7[m]> I mean, Seraphis and Jamtis are already now massive undertakings, that few other projects ever took. And now we talk about adding risks, and work, but also for good rewards. Tricky.
<kayabanerve[m]> I'd also note my way of handling it would add Rust to the project. tevador is considering a distinct curve choice, which is its own discussion, which may require building a curve lib for it (or forking the existing Ed25519 lib for it).
<one-horse-wagon[> The other view to consider is we have just a few guys, pouring their heart and soul into coding.  I'm sure it is disheartening to hear discussions like we are having now.  
<rbrunner7[m]> Well, dev time is not dev time. If UkoeHB says that doing that curve switch is "not for him", that's ok, but may complicate things.
<kayabanerve[m]> There's discussions there on benefit. I solely note it as it relates to scope. I wouldn't mind whatever tevador can come up with, if an improvement, if we can handle the amount of development it is.
<one-horse-wagon[> Seraphis looks to be a huge improvement over what we have now.  My vote is to stick with it completely and go for it without divergencies.
<rbrunner7[m]> Well, those "full membership proofs" are even hugher :)
<rbrunner7[m]> As far as my little mind understands
<rbrunner7[m]> I don't mock, by the way, please don't take offense
<rbrunner7[m]> Well, I have to say that over the last few days, and over this meeting, my personal opinion about that curve switch thing has changed from "No way" and "Impossible" to "Risky, PITA, but maybe, just maybe, worth it".
<rbrunner7[m]> Would anybody else risk some opinion statement?
<rbrunner7[m]> Preliminary, very preliminary, of course.
<rbrunner7[m]> Maybe not :)
<kayabanerve[m]> Uhhh
<rbrunner7[m]> I think investigations will continue anyway, and that's a good thing.
<kayabanerve[m]> @tevador I get 405ms vs 930
<kayabanerve[m]> In favor of pasta
<rbrunner7[m]> More information is needed in any case.
<kayabanerve[m]> ... that can't be right, right?
<kayabanerve[m]> curve25519-dalek versus pasta curves, 10k scalar muls. Both compiled under release, printing the result of the algorithm in order to ensure the compiler doesn't optimize it out.
<rbrunner7[m]> Maybe we could go even as far as producing a proof-of-concept fully incompatible Pallas curve fork of Monero ...
<kayabanerve[m]> AFAIK, no asm nor processor specific opts for either.
<kayabanerve[m]> Still, that seems like an error in testing methodology. Even the complete Weierstrass formulas shouldn't kill twisted edwards by 2x. And dalek is dalek. It should be heavily optimized...
<kayabanerve[m]> rbrunner7[m]: Considering we need a developer to put forth the work, then that'd be PRd on top of the current work, I'd argue this is just part of the development process for moving to pasta
<kayabanerve[m]> The main thing to ensure is that if a developer can put forth a move to pasta, it'll be accepted. Else, it's a bit much work to ask for.
<rbrunner7[m]> Well, if it doesn't have to be compatible, you could take a number of shortcuts, for faster results about feasibility
<kayabanerve[m]> It may be optimal to just port BP+ and demo with that? Show the toolchain setup and a diff of that subset?
<rbrunner7[m]> Ok, maybe we have to put a point here because we are already past the hour as far as the meeting is concerned. I hope this meeting was a contribution to clear things up a bit, and help decision processes to start.
<kayabanerve[m]> Thanks rbrunner7, for effectively running the meeting :)
<ghostway[m]> <kayabanerve[m]> "curve25519-dalek versus pasta..." <- Well, prints aren't the best. You can use #[no_mangle] 
<rbrunner7[m]> Welcome. I try to do my best. See you next week at the latest, still on the same curve :)
````


# Action History
- Created by: rbrunner7 | 2023-02-10T15:59:24+00:00
- Closed at: 2023-02-17T15:29:40+00:00
