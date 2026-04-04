---
title: 'Triptych Prioritization Meeting: 21 April 2021, 17:00 UTC  '
source_url: https://github.com/monero-project/meta/issues/568
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2021-04-19T13:01:27+00:00'
updated_at: '2021-04-30T16:30:20+00:00'
type: issue
status: closed
closed_at: '2021-04-30T16:30:20+00:00'
---

# Original Description
**Location**
#monero-dev on freenode (IRC)

**Time**
17:00 UTC

**Proposed Meeting Items**
Discussion of priorities of items relating to Triptych. Please comment on GitHub in advance of the meeting if you have suggestions. 

Supersedes #566.

# Discussion History
## Gingeropolous | 2021-04-19T13:51:37+00:00
As sarang has got his head fully around triptych, I think it would be great to hear his thoughts on priorities of items first and foremost. 

beyond that, I think multisig support should probably be on the list. 

thoughts on output selection would be good, but it seems that we may just be able to use what we have for now

## rbrunner7 | 2021-04-21T18:39:41+00:00
	<sarang> Hello
	<dEBRUYNE> Hi
	<dEBRUYNE> cc rehrar, binaryFate
	<rbrunner> Hi there
	<rehrar> Hu
	<krongle> hi
	<gingeropolous> hi
	<sarang> Who wishes to lead this meeting?
	<binaryFate> hello
	<dEBRUYNE> binaryFate: Would you mind leading?
	<rehrar> Unfortunately I cannot. Sorry.
	<rehrar> So we leave it to somebody.
	<binaryFate> I'll probably have to leave early. Sarang do you want to have a go?
	<sarang> OK
	<sarang> I am interested to know what Triptych research priorities should be, to determine if I should work on it as part of a CCS submitted by rehrar
	<sarang> Note that I would be working as a researcher employed by rehrar's company
	<sarang> I had previously understood that multisig was not considered a very high priority, but now it sounds like it should be, for example
	<moneromooo> I vote (1) correctness, (2) security, (3) multisig, (4) speedups.
	<sarang> So it seems best to identify priorities more directly; hence this meeting
	<ArticMine> Hi
	<binaryFate> proposal: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/222
	<dEBRUYNE> For people reading, sarang submitted a CCS proposal -> https://www.reddit.com/r/Monero/comments/mn3irk/triptych_research_and_optimizations_a_new_ccs/
	<sarang> No, rehrar did
	<sarang> Just to be very clear
	<rehrar> To be even more clear, Cypher Stack did.
	<sarang> There was much discussion about the nature of that arrangement, but I'd specifically like to determine the priorities to know if I am the best person to do that work
	<rehrar> But I, the individual, submitted it in behalf of the company because companies don't have typing hands.
	<vtnerd> mj-xmr_ : if the goal is compile-time reduction, then no doubt much could be moved using the pimpl method
	<nioc> would it be appropriate to add ring selection to mooo's list?  AIUI increasing the rind # would require a new selection algo
	<vtnerd> but I'm not sure why at a glance an vtable interface is needed
	<sarang> Here are some things that I had considered useful research?
	<sarang> s/?/:
	<sarang> - Output selection and binning algorithms
	<sarang> - Batching optimizations
	<sarang> - Verifier optimizations relating to scalar computations
	<sarang> - Updates to security model
	<sarang> As far as multisig goes, I had initial work on this but it's more complex than the current multisig solutions and would require much more coding using something like OpenSSL for RSA groups
	<krongle> Hey. I'm one of the xmr.to team. Multisig is definitely be an important enabler for at least one of our upcoming projects. And quite a major bummer if we lost it :-). So I would like to add my vote for multisig.
	<sarang> I do _not_ know how much complexity this would add to things like mobile wallets or hardware wallets
	<sarang> To be absolutely clear, this requires curve arithmetic that is not 25519-based
	<sarang> and is multi-round
	<moneromooo> I'd say it's an acceptable drawback if you have to use monero-wallet-cli to use multisig.
	<sethsimmons> I will add a vote for multisig support with the recent announcement and impetus behind Haveno. That's a high priority for me, personally, now.
	<sarang> I am not very familiar with OpenSSL or its alternatives when it comes to functionality required for this RSA group support, so the implementation side is something I'm much less confident in
	<hyc> sounds fine if it's only in wallet-cli for now. someone else can adapt it for mobile wallets at a future time
	<moneromooo> I'm thinkinf of people with large amounts of monero and mandated DD. Those would have to use multisig, most likely. Kind of a must have for those.
	<sarang> I am more confident in the underlying construction and algorithms
	<binaryFate> sarang: appart from significant additional coding, would the security model be fundamentally different for multisig than for singlesig?
	<moneromooo> I can help with openssl if needed. I'm not familiar with it, but I can become :)
	<rbrunner> A vague hope, but would it help anything if only 2/3 was supported? Because that's basically where almost all the shows take place.
	<sarang> binaryFate: the existing security model holds, since it doesn't care how you compute keys or linking tags as long as they're correct
	<ArticMine> I see backwards compatibility with existing multisig as a requirement
	<sarang> ArticMine: key image format changes
	<endogenic> why would only wallet-cli have access to the implementation?
	<krongle> for us "backwards compatibility with existing multisig as a requirement" would be a nice to have, but not a have to have
	<moneromooo> Assumes facts not in evidence. AFAIK the issue is processing power (for hw wallets) and more code to use the wallet2 impl.
	<endogenic> or was that just 'it might be too much to add to a hwdevice scheme for now'
	<vtnerd> I'll throw my support for openssl rsa groups too, man
	<endogenic> ty
	<hyc> I've worked pretty extensively with OpenSSL, am available to help on that front
	<ArticMine> So what happen to existing multisig outputs?  there needs to be a pathway
	<sarang> endogenic: hardware wallets would need to be able to do arbitrary RSA group computations, and I don't know enough about their capabilities
	<endogenic> yeah
	<sarang> Old outputs would continue to use the old key image format, and need to be "transitioned" to new outputs... this would likely just be a height cutoff
	<rbrunner> Are there any HW wallets that support *current* multisig? Don't think so.
	<sarang> This means a partitioning of the output set, which has important implications
	<moneromooo> They should be able to be spent normally. When spent, they'll generate triptych outputs. Whether those are multisig or not is unknown to the sender. The recipient can then send them normally.
	<sarang> However, I do not know of a way to avoid such a partitioning
	<hyc> this doesn't sound any different from transition to ringct, or transition to BP
	<sarang> As for optimizations, there's a neat optimization that was used in Beam and Firo's implementation of Lelantus (disclaimer: I do research on Lelantus as part of my role at Cypher Stack)
	<moneromooo> Similar to the ringct change, BP did not need such a change.
	<sarang> Correct
	<sarang> ^ moneromooo correct, not hyc
	<ArticMine> The transition like the ringCT model should not be an issue as far as I can see
	<hyc> reference to Lelantus doesn't give warm fuzzies, given Firo's recent problems
	<sarang> It means an initially limited anonymity set, which will cause initial chain reaction deanonymization
	<sarang> hyc: Triptych and Lelantus share the same "proving system ancestor"
	<sarang> as does Arcturus
	<sarang> and this optimization applies to part of the protocol that happens to be common among them
	<sarang> I have yet to determine the precise timing differences
	<dEBRUYNE> sarang: To be clear, in that case multisig should be able to 'hold' funds past the fork date right?
	<dEBRUYNE> A output conversion subsequently takes place when the 'old' outputs are consumed in a transaction
	<dEBRUYNE> That generates new Triptych outputs
	<sarang> Output conversion means that a transaction can include either _only_ pre-Triptych anonymity set elements or _only_ post-Triptych anonymity set elements
	<sarang> and the linking tag pool used for checking double-spends is specific to that cutoff
	<sarang> The output format itself isn't actually changed, but that's not really important here
	<rbrunner> Doesn't sound like a reason to fully kill multisig to me
	<rbrunner> More like "issues"
	<selsta> IMO if there is a known Triptych optimization it is worth exploring, even if the exact speedups are not known yet
	<rbrunner> Or "things to consider"
	<sethsimmons> <selsta "IMO if there is a known Triptych"> agreed
	<sarang> Yeah, there's a separate optimization that affects proof format (using `n`-ary Gray codes)
	<selsta> we want to consider and explore all known optimizations before deploying triptych
	<sarang> The other optimization is not consensus, but it could be important for setting network parameters for the proofs
	<selsta> to avoid multiple forks
	<gingeropolous> yeah that makes sense
	<sarang> Anyway, it does sound like multisig _at fork time_ should be considered a blocker now?
	<dEBRUYNE> sarang: Is this conversion only needed for multisig, or for all outputs?
	<sarang> All outputs
	<sarang> Very similar to the RingCT transition
	<dEBRUYNE> I don't see the issue then, at least for that aspect
	<sarang> Multisig outputs look identical (by design)
	<sarang> Well, the conversion is important because it _will_ initially lead to chain reaction analysis
	<moneromooo> The issue is lots of new code using RSA groups has to be done.
	<sarang> This should dissipate quickly
	<sarang> moneromooo: yes
	<hyc> sounds like a flag day. tell everyone to churn after the hardfork.
	<dEBRUYNE> sarang: What time frame would you estimate to get multisig properly working?
	<rbrunner> Any rough estimate possible already about how many person month we talk here?
	<rbrunner> For the implementation
	<sarang> That's the thing... I don't have a solid understanding of what full multisig implementation will take, since it's multi-round and uses a lot of new group arithmetic that we currently don't use anywhere
	<moneromooo> I can maybe add some wallet code to prefer spending pre-triptych outs. This means that there'll be fewer trpitych txes right after the fork, allowing for more new triptych outs to be created before the first ones get spent.
	<binaryFate> We also have to support old non-ringct -> triptych transactions no?
	<moneromooo> No, IIRC those go pre-rct -> rct.
	<sarang> This would make a chain pre-CT -> CT -> Triptych easy to detect, FWIW
	<gingeropolous> ah, so someone with pre-rct would have to do: pre-rct -> rct -> triptych?
	<dEBRUYNE> Similar to how 'unmixable' outputs are first transformed non-ringCT outputs I guess
	<sarang> Of course, spend patterns for CT -> Triptych may be easy to detect as well based on known distributions
	<moneromooo> They don't have to. The outputs are created in the type that matches consensus rules. They're always all spendable.
	<sarang> Anyway, I think a lot of this transition needs careful consideration since it's a big change
	<ArticMine> Yes I agree
	<sarang> The work I did previously was on the proving system and a _bit_ of the multisig stuff
	<sarang> But there's a lot to consider about the migration, and any side cases that might arise
	<rbrunner> But still enough for moneromooo to implement a POC, right?
	<sarang> as well as the practical implementation of multisig due to its RSA group requirements and round structure
	<sarang> rbrunner: my initial multisig work is almost certainly not enough for a proof of concept yet
	<sarang> But I can write it up in much more detail
	<rbrunner> No, I meant Triptych in general
	<sarang> The initial stuff was just to determine if such a thing was possible
	<sarang> Oh, I have working Triptych prover and verifier code already, with limited batch support
	<sarang> That was done earlier to get timing data
	<moneromooo> Well, the patch to add triptych to monero is done.
	<rbrunner> Yes, that's what I meant :)
	<moneromooo> I did that a couple months ago.
	<sarang> Big caveat that while the preprint has undergone review for publication, the code has undergone no such formal review
	<sarang> And, as always, the quality of peer review can vary greatly compared to a paid review
	<sarang> ^ for the preprint, I mean
	<rehrar> I know people are excited for the big ring sizes, but this shouldn't be rushed in any way. I would be shocked if we wanted to get this in before year's end.
	<rbrunner> sarang, you mentioned " - Updates to security model" as possible themes. What's that, in general?
	<rehrar> We can release with BP+ in the meantime.
	<dEBRUYNE> <sarang> Big caveat that while the preprint has undergone review for publication, the code has undergone no such formal review <= We would have to get multiple audits for Triptych anyway
	<sarang> rbrunner: the current security model focuses primarily on the proving system itself as a zkp system
	<dEBRUYNE> rehrar: I'd still be in favor to postpone BP+ until Triptych is ready, even if that means we have to postpone it to, say, early 2022
	<sarang> But less so on the resulting transaction model that you get by using our commitment-offset-based approach to amount balancing
	<sarang> FWIW the CLSAG security model is similar, as was MLSAG
	<sarang> Arcturus is a little different since it handles balance inside the zkp, whereas Triptych (and its predecessors) do not
	<binaryFate> would triptych multisig require specific paper peer review?
	<sarang> It would be nice if it did
	<sarang> Working up a separate security model for that would be a _lot_ more work (think about the previous multisig preprint!)
	<sarang> The most one could hope for without that would be a thorough description and proof of concept, but this is a very different review process
	<sarang> Also, multisig security models were really suraeNoether's expertise
	<sarang> The idea behind multisig is that to compute the linking tag between players requires a type of known MPC
	<sarang> and then this is worked into the rest of the proof construction, which is much more straightforward
	<sarang> The RSA group stuff only comes into play for this linking tag MPC
	<sarang> and there only because you need to jointly compute an inversion of the output secret key
	<sarang> (multiplied by a fixed curve group element, that is)
	<arnuschky> Hello everyone! Sorry I am late to the party... Is there a live transcript/log somewhere so that I can see was has been said till now?
	<dEBRUYNE> arnuschky: I'll send the logs in PM
	<rbrunner> https://monerologs.net/monero-dev/20210421
	<arnuschky> awesome, thanks
	<rbrunner> And solutions like allowing a mix of transaction formats for the foreseeable future fully out of question?
	<moneromooo> No.
	<sarang> How do you mean?
	<rbrunner> We freely allow people to produce the current tx format even after hardfork. People sneak in their multisig transactions that way.
	<dEBRUYNE> That would imply multisig holders performing current transactions, whereas the rest of the network performs Triptych transactions
	<rbrunner> Not necessarily. I mean crazy things would be possible, like random decision what to produce for *every* tx :)
	<moneromooo> Consensus rules cannot distinguished between outputs that were spent from a multisig wallet from outputs that were not.
	<dEBRUYNE> sarang: Given the potential volume of the multisig work, would it be prudent to start with that aspect of Triptych?
	<sarang> dEBRUYNE: certainly could do this
	<binaryFate> if there is general agreement that lack of multisig is not acceptable, doesn't that define an apparently large enough (listening to sarang) research direction already?
	<dEBRUYNE> binaryFate: Right
	<dEBRUYNE> moneromooo: I meant in case of a fork without multisig support for Triptych
	<sarang> If multisig is a blocker for deployment, that could be the initial scope; if it turns out not to work in practice for whatever reason, that minimizes any wasted effort
	<dEBRUYNE> Then multisig holders can only transact in the old format basically
	<gingeropolous> just curious: does arcturus lend itself to a better / easier multisig? or is it the same?
	<sarang> To be clear about any kind of mixing of transactions... outputs need to be separated by what transaction type can consume them
	<moneromooo> If we fork without MS, and if Alice has a MS wallet, and Bob sends Alice an output after the fork, then Alice cannot spend. That is bad.
	<sarang> Arcturus multisig requires this as well, as would Omniring, RingCT 3.0
	<rbrunner> You could not prevent that sending, right, because multisig is not visible in the address
	<ArticMine> So how would a transition from Triptych to Arcturus look like for example?
	<sarang> ArticMine: output pool stays the same
	<gingeropolous> yeah it sounds like multisig is the primary at this point
	<sarang> Proof format changes
	<sarang> No transition needed for outputs between Triptych and Arcturus
	<sarang> In that case, should the initial scope of work be multisig only?
	<ArticMine> Yes
	<rbrunner> Maybe, given how far along the "other" stuff is already ...
	<dEBRUYNE> If we cannot deploy without multisig, it is basically imperative to find out as soon as possible whether proper multisig can be implemented / achieved
	<sarang> Output binning/selection is important as well, but seems less important based on this discussion
	<hyc> binning sounds like a matter of refinement, MS sounds like a harder works/won't work
	<rbrunner> I mean we don't even have any graceful way out of multisig on the table if we really should drop support, right?
	<sarang> hyc: binning would likely need to be consensus to avoid miner shenanigans
	<arnuschky> If multisig is in such high demand, but seems conceptually not really an issue but much more a coding problem - would it be sensible to turn this into a separate CCS and fund that alongside the more theoretical Triptych work?
	<ErCiccione> I agree with dEBRUYNE. Nice to see all the support for multisig and haveno :)
	<rbrunner> Other than "People, please empty all those multisig wallets"
	<gingeropolous> true arnuschky . sarang, at this point, is multisig more a theoretical problem or an implementation problem?
	<gingeropolous> or is it in that wonderful gray area .....
	<sarang> Mostly implementation, but I think the transition should be reviewed in more specificity to ensure that existing multisig wallets are not affected
	<sarang> Loss of funds seems like the obvious blocker
	<binaryFate> We'll all agree on that
	<sarang> As would having to move to a separate multisig arrangement?
	<sarang> i.e. if multisig players need to collaborate to migrate to a new address
	<gingeropolous> well, theoretically, they can migrate whenever
	<dEBRUYNE> I suppose that is not necessarily a blocker as long as there is no time limit on it
	<rbrunner> Certainly unfortunate
	<arnuschky> I think migration is fine as long as it's not time-constrained
	<dEBRUYNE> Bit inconvenient, but still
	<arnuschky> ie if I want to recover my wallet two years from now, it should still be possible
	<sarang> Should it be considered a blocker if multisig players need to change addresses?
	<rbrunner> 2/3 looses sense, opens blackmail possibilities that were not there otherwise
	<arnuschky> rather than resulting in loss of funds due to a missed window
	<sarang> Or just a super duper annoyance
	<dEBRUYNE> Same answer I'd say
	<dEBRUYNE> Just inconvenient
	<arnuschky> for us that would be acceptable
	<ErCiccione> sarang: would be defintely be problematic. I'm not sure of how that would effect active trades on Haveno.
	<dEBRUYNE> sarang: I think it should be fine as long as a proper migration guide is provided
	<rbrunner> Better than no multisig in any case :)
	<dEBRUYNE> That lays out all necessary steps
	<sarang> Anyway, this is good to know. So the general consensus seems to be that limited scope initially to multisig is the best use of effort?
	<dEBRUYNE> I'd say so
	<arnuschky> inconvenience can always be softed by good software support / processes
	<ErCiccione> but if the price to pay for multisig support, i guess could be workable :)
	<sarang> I'd be hesitant to expand scope if one outcome could be "sorry, multisig doesn't work, so it's all canceled!"
	<gingeropolous> yeah
	<binaryFate> "limited scope initially to multisig is the best use of effort" +1
	<rehrar> So what say we leave the existing proposal as is, and just not merge. It'll just chill in Ideas. Make a new proposal for multisig work with the scope and price. Get discussion on that. Merge that one first once approved.
	<sarang> Why not close it?
	<rehrar> Then the Triptych optimizations can be merged after multisig is sorted out.
	<sarang> Any further work would need a more defined scope than existed in that CCS
	<dEBRUYNE> Why not change the existing one?
	<sarang> Up to rehrar I suppose
	<rehrar> dEBRUYNE: all of the comments will be for the old version, wouldn't be obvious
	<rbrunner> We are not short in possible proposals, aren't we. Cleaner certainly to make a new one, IMHO
	<rehrar> and there's a lot of comments. I think it's important for the transparency. A new lurker will see all of the comments and  think they are in support of the multisig stuff. Which those people may very well be in support. But I think it's best to be clear?
	<dEBRUYNE> I guess, but most of the discussion relates to the way sarang is contracted
	<dEBRUYNE> Not to the specifics of the proposal itself
	<rehrar> I will do what the community thinks is the best course of action for the proposal itself.
	<dEBRUYNE> I'd change the scope, cite this meeting as source
	<dEBRUYNE> And then simply merge it
	<selsta> Also think no reason to open a new proposal.
	<dEBRUYNE> Would be a bit of shame to lose another week here just for redundant administrative purposes
	<sarang> One issue is that I don't have a good sense of the time commitment required for this
	<sarang> Multisig, that is
	<sarang> As noted earlier
	<dEBRUYNE> sarang: I'd just work out the current hours and see how far you get?
	<rbrunner> Sounds reasonable.
	<dEBRUYNE> We could hold another meeting afterwards I suppose
	<rbrunner> Not much choice, given all the unknowns and uncertainties
	<rehrar> I agree. And since the time is on the smallish side (one month's worth of work hours) then we can reassess at the end of that. We're underestimating rather than over, so no risk to the community on unused funds.
	<Inge-> +1 I'm quite comfortable with letting Sarang work on it and revisiting status and progress once we know more.
	<hyc> agreed
	<sarang> Yeah I want to avoid the case where it takes much less time than expected, and funds were raised in excess
	<rbrunner> Buy a lambo then :)
	<sarang> oof
	<dEBRUYNE> Depending on the status of multisig, I presume those hours can simply be used to work on other aspects
	<Inge-> If it takes less time, and multi-sig is found to be likely to have solutions with Triptych, I would also be quite comfortable with sarang spending excess time on any of the other proposed tasks :P
	<rehrar> I'm sure core would be fine with any excess funds (if it were to ever happen) to be rolled into any next research project we do.
	<sarang> The worst-case scenario would be discovering that it won't work early on
	<sarang> making the other work moot
	<dEBRUYNE> sarang: I think the community is perfectly fine with letting you churn away on Triptych
	<dEBRUYNE> <sarang> The worst-case scenario would be discovering that it won't work early on <= Which is basically why multisig has to be prioritized
	<rehrar> dEBRUYNE: well, what he's saying is it seems multisig is a showstopper. So if we realize it's not workable, then Triptych is a no-go altogether.
	<moneromooo> Sorry, was afk for a bit, just reading this: "Should it be considered a blocker if multisig players need to change addresses?"
	<rehrar> Meaning excess hours can't be poured into Triptych.
	<moneromooo> I think it would be a massive problem, because you can't stop people from sending to the old address, where the outputs would apparently be burnt ?
	<dEBRUYNE> In what kind of scenario does a multisig wallet receive a lot of transactions though?
	<sarang> Without flagging the output type, yes
	<dEBRUYNE> Hot wallets (from services) are typically not multisig as far as I know
	<sarang> Again, need to carefully consider the transition and existing addresses
	<dEBRUYNE> <rehrar> Meaning excess hours can't be poured into Triptych. <= Right, but then we could discuss with the community what to do with the remaining funds
	<sarang> I believe we'd be ok provided keys are additive
	<h2017> why not put in the proposal: Excess hour can be used on Tryptich, provided that a proof of concept of multisig is established" (or something like that)
	<arnuschky> +1
	<sarang> What should happen in the case that multisig is shown not to be viable?
	<rehrar> I also need to adjust for new prices.
	<rehrar> A good problem to have :)
	<rehrar> sarang: dEBRUYNE suggested we discuss with the community how to spend.
	<rehrar> Given my position with core, I would say rolling into the GF isn't an option so there can be no COI. Whether it's put into other existing CCS proposals or something else can be for discussion.
	<sarang> In advance, I hope
	<rehrar> But in a sense, that's not your problem as a researcher. It's your problem to consider as a member of the Monero community though.
	<sarang> I mean, I would still (as a researcher) consider the other Triptych research areas to be of independent interest
	<sarang> But if it couldn't possibly lead to deployment, that's problematic as you say
	<Inge-> Are any of the alternatives to Triptych more likely candidates to be able to support multi-sig?
	<moneromooo> If not viable, then I guess we'd need to tag outputs, rather than use the fork height to determine their type.
	<moneromooo> I thought it was pretty much worked out in theory though ?
	<sarang> Most other options I've looked at (Omniring, RCT3, Arcturus) have the same key image format, and therefore the same challenges
	<sarang> Lelantus does not, but it has other problems relating to recipient addresses that I think are non-starters here
	<sarang> moneromooo: I want to write out a much more comprehensive analysis that accounts for these cases
	<sarang> To ensure that these are all considered properly and in a unified way
	<Inge-> So basically we forge ahead, with multi-sig and the other research areas, and assume that human ingenuity will eventually prevail over the "impossible"?
	<sarang> Other non-multisig work would be placed aside
	<sarang> Since those aren't blockers
	<rbrunner> Any idea yet whether wallet construction and transacting, as seen *by the user*, will be different (if it works)?
	<moneromooo> Not different.
	<rbrunner> Different order of commands, more key exchange rounds, stuff like that?
	<rbrunner> (For Multisig specifically)
	<moneromooo> Oh, for multisig itself ? If so, I dunno ^_^
	<sarang> This'll be a new multi-round MPC
	<sarang> I need to review my notes to see how many rounds :/
	<sarang> And there's been additional literature on similar constructions that I will need to review carefully
	<rbrunner> Alright. As I said, if 2/3 works out reasonable, we are (almost) set.
	<sarang> This particular construction (the author names escape me) has been studied pretty extensively because of its use in other signature MPCs
	<sarang> Yeah, I need to look over the threshold stuff again too
	<sarang> Most work initially starts with `n`-of-`n` and then builds threshold using additional round(s)
	<sarang> Unfortunately I don't know a way to reduce the rounds too far without sacrificing security expectations
	<rbrunner> Everything else pales in comparison with 2/3, I would say.
	<rbrunner> as far as practical importance goes
	<sarang> Sure, but if you have threshold, it's pretty much guaranteed you have arbitrary `n`-of-`n` in the math already
	<sarang> and `n-1`-of-`n` too
	<rbrunner> All the better then. I just remember we did not bother to implement that for quite some time.
	<binaryFate> I got to go sorry. Feels like it was very useful, thanks sarang and all. rehrar: I suggest we double-check with luigi1111 the phrasing for potential excess funds before you post updated proposal
	<sarang> The implementation differences exist, of course, no doubt
	<sarang> Thanks to everyone for the information on priorities; this was very helpful
	<sarang> I assume the meeting is now adjourned?
	<hyc> nobody feels like an issue was left out?
	<rbrunner> Not me. In any case relieved that multisig support is accepted as important.
	<gingeropolous> i mean, i think there are more, but the go/nogo of multisig seems like the primary
	<sarang> Yeah, I'm glad to know of its priority. From much earlier discussion I was under the impression it was not
	<moneromooo> Pailler ?
	<moneromooo> Or Paillier.
	<sarang> That's what is used for the MPC, yes
	<gingeropolous> well, i think that was before multisig was being used maybe. I mean, i still feel like its niche and beyond the scope of money, but the can of worms has been opened
	<rbrunner> In any case right now would probably the last decent point where to announce that we kill it for good.
	<sarang> It's not consensus though, and not detectable anyway
	<sarang> Anyone could be doing multisig in any number of ways
	<sarang> If you end up with a valid transaction, it's a valid transaction
	<rbrunner> Well, I am quite sure from the lack of feedback for and questions about "my" MMS that it probably *is* niche :)
	<rbrunner> At least until now.
	<dEBRUYNE> Wouldn't be surprised if some exchanges use it for cold wallets though
	<rbrunner> The story will change of course as soon as software like Haveno will start to use it under the hood, automatically
	<dEBRUYNE> Would anyone mind posting the logs on the Github meta ticket by the way?
	<ErCiccione> i think and hope that Haveno will make people use multisig more tbh


# Action History
- Created by: dEBRUYNE-1 | 2021-04-19T13:01:27+00:00
- Closed at: 2021-04-30T16:30:20+00:00
