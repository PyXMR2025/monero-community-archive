---
title: 'Research meeting: 9 December 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/417
author: SarangNoether
assignees: []
labels: []
created_at: '2019-12-05T13:13:16+00:00'
updated_at: '2019-12-09T18:02:43+00:00'
type: issue
status: closed
closed_at: '2019-12-09T18:02:43+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 9 December 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-12-09T18:02:43+00:00
    [2019-12-09 12:00:03] <sarang> Let's go ahead and get started with GREETINGS
    [2019-12-09 12:00:59] <kinghat> o/
    [2019-12-09 12:01:02] — suraeNoether waves
    [2019-12-09 12:01:05] <sgp_> hello
    [2019-12-09 12:02:25] — sarang waits a few minutes for others
    [2019-12-09 12:02:53] ⇐ DryStorm quit (~Android@172.58.239.31): Ping timeout: 250 seconds
    [2019-12-09 12:05:07] <sarang> That's long enough!
    [2019-12-09 12:05:23] <sarang> Let's move to ROUNDTABLE
    [2019-12-09 12:05:27] <sarang> suraeNoether: what up with you
    [2019-12-09 12:06:09] <suraeNoether> i'm terribly ill this morning, so my update will be very brief.  my work in this past week has involved three incomplete tasks:
    [2019-12-09 12:06:38] <suraeNoether> 1) CLSAG linkable anonymity proof required some thought. sarang and i have thought about it and we have a strategy to finish writing the proof. sarang: do you want to make the changes to our LA definition or do you want i should?
    [2019-12-09 12:07:02] <sarang> suraeNoether: I have a writeup for LA in my notebook that I'm transcribing to TeX
    [2019-12-09 12:07:06] <suraeNoether> and proof* not just the definition
    [2019-12-09 12:07:09] <sarang> it works just fine
    [2019-12-09 12:07:14] <sarang> On that note
    [2019-12-09 12:07:24] <sarang> Do you have any thoughts on linkability (not LA)
    [2019-12-09 12:07:32] <sarang> I don't particularly like the Backes definition
    [2019-12-09 12:07:44] <suraeNoether> uh one sec
    [2019-12-09 12:07:55] <sarang> Triptych has a version of linkability+non-frameability that I like better
    [2019-12-09 12:08:00] <suraeNoether> is there soemthing wrong with the definition we proposed initially?
    [2019-12-09 12:08:17] <suraeNoether> iirc that one's from bender
    [2019-12-09 12:08:28] <sarang> It's not formalized quite enough, in the apparent opinion of the reviewer
    [2019-12-09 12:08:34] <sarang> I think it needs just minor work
    [2019-12-09 12:08:41] <sarang> Triptych formalizes it a tad more IMO
    [2019-12-09 12:09:07] <sarang> I can add that to the writeup if you like
    [2019-12-09 12:10:01] <suraeNoether> well
    [2019-12-09 12:10:25] <suraeNoether> for the sake of the audience, can you describe the 3 different definitions you want to consider? or 2, assuming you want to bail on backes'
    [2019-12-09 12:11:04] <sarang> Backes requires the following for an LRS: completeness, linkable anonymity, linkability, non-frameability
    [2019-12-09 12:11:19] <sarang> Right now we combine linkability and non-frameability with non-standard terminology
    [2019-12-09 12:11:44] <sarang> Backes uses a particular linkability definition: can the adversary use `q` keys to generate `q+1` non-linking signatures?
    [2019-12-09 12:11:55] <sarang> Where `q` is scaled via the security parameter
    [2019-12-09 12:12:39] <sarang> I don't particularly like this definition over the "usual" one about producing two linking signatures, but I think it's important to frame the definition as a challenger-player interaction
    [2019-12-09 12:12:46] <sarang> Our current method does this very informally
    [2019-12-09 12:13:41] <sarang> I propose a combined linkability definition in my Triptych writeup that's a slight formalization of what CLSAG has now
    [2019-12-09 12:13:59] <sarang> (it could easily be split into linkability and non-frameability)
    [2019-12-09 12:14:08] <suraeNoether> hmmmm q scaling with the security parameter is the weird part to me: if the security parameter goes up, so does q... and so this means, for example, the adversary can't produce 3 signatures using 2 keys without some linking occurring. this feels *weaker* than the statement "can't produce two signatures using the same key without them being linked"
    [2019-12-09 12:14:18] <sarang> Yeah, which is why I don't really like it
    [2019-12-09 12:14:29] <sarang> didn't sit well with me
    [2019-12-09 12:14:36] <suraeNoether> and we want the property with q=1 anyway to prevent double-spending
    [2019-12-09 12:14:47] <sarang> So I am proposing not using the Backes definition, but simply formalizing what we have now, a la Triptych
    [2019-12-09 12:14:58] <sarang> then it's more clear what the linkability player has access to in terms of keys etc.
    [2019-12-09 12:15:09] <suraeNoether> okay, i'm going to read more deeply into that this afternoon
    [2019-12-09 12:15:20] <sarang> IMO it's a pretty straightforward formalization
    [2019-12-09 12:15:28] <sarang> doesn't affect much in practice
    [2019-12-09 12:16:03] <suraeNoether> backes' definition with q=1 seems to me to imply backes' definition with greater q, but it's possible that it doesn't technically reduce the way it seems. i'll think more about it
    [2019-12-09 12:16:25] <sarang> That definition doesn't make assumptions about linking tags being equal AFAICT
    [2019-12-09 12:16:33] <sarang> Whereas ours does
    [2019-12-09 12:16:38] <sarang> I think that's part of it
    [2019-12-09 12:17:10] <sarang> Anyway, you were talking about work you'd been doing, before I barged in =p
    [2019-12-09 12:17:32] <suraeNoether> moving along, my next incomplete task is reviewing triptych's security proofs more deeply, which dovetails with this :P
    [2019-12-09 12:17:40] <sarang> Yeah, a nice tie-in
    [2019-12-09 12:18:11] <suraeNoether> finally, i'm working on matching simulations today. i'm experiencing a data management and presentation issue, but i hope for the end of the day a nice graph displaying performance of Eve as a function of ring size and churn length
    [2019-12-09 12:18:19] <sarang> Nice!
    [2019-12-09 12:18:27] <suraeNoether> this will come along with a push to my repo with all the code used to generate that, and explanations so people can replicate it
    [2019-12-09 12:19:19] <sarang> word
    [2019-12-09 12:19:45] <suraeNoether> that's it, if i had presented in the other order then your "barging" would have been a great segue into *your* work for the week :P
    [2019-12-09 12:20:00] <sarang> We can pretend otherwise
    [2019-12-09 12:20:16] <sarang> I have completed a draft of the Triptych preprint, which is now in suraeNoether's hands
    [2019-12-09 12:20:17] <sgp_> suraeNoether: I'm really looking forward to that chart
    [2019-12-09 12:20:29] <sarang> it includes my proposed linkability+non-frameability definition
    [2019-12-09 12:20:53] <sarang> Figured out the CLSAG linkable anonymity definition, which is not as strong as Backes, but does the job IMO
    [2019-12-09 12:21:25] <sarang> I've also been working with Aram from Zcoin on some related Groth proving system stuff
    [2019-12-09 12:21:44] <sgp_> what's the shortfall on the linkable anonymity definition, even if there's no practical difference?
    [2019-12-09 12:21:45] <sarang> There will be a neat paper coming out from them on that shortly, which they graciously provided to me in advance
    [2019-12-09 12:22:01] <sarang> sgp_: Backes permits key corruption, which doesn't work with our DDH hardness assumption
    [2019-12-09 12:22:10] <sarang> Instead, we assume the adversary can obtain key images
    [2019-12-09 12:22:22] <sarang> And that the adversary can pack rings with their own malicious keys
    [2019-12-09 12:22:24] <sgp_> sarang: thanks
    [2019-12-09 12:22:31] <sarang> (which you can assume are trivially corrupted)
    [2019-12-09 12:23:00] <sarang> This is already stronger than the existing definition that was used
    [2019-12-09 12:23:41] <sarang> Otherwise, I also wish to update the DLSAG paper (which will appear next year in conference proceedings) with the CLSAG security model, since they are structurally extremely similar
    [2019-12-09 12:24:22] <sarang> So overall, a lot of tedious (but still interesting) stuff involving formal definitions and proofs
    [2019-12-09 12:24:42] <sarang> When suraeNoether finishes his review of the Triptych preprint, it'll go to the IACR archive
    [2019-12-09 12:24:49] <sarang> and presumably any CLSAG/DLSAG updates as well
    [2019-12-09 12:25:28] <suraeNoether> hmm Backes' linkability definition is a puzzle i have very little intuition about: should it be harder or easier to present 2 signatures from the same key without linking the signatures than it should be to present 201 signatures from 200 different keys without any of them linking? *taps chin*
    [2019-12-09 12:25:52] <sarang> The adversary picks which keys IIRC, right?
    [2019-12-09 12:26:12] <suraeNoether> yeah, adversary can use KeyGen or any other way of selecting the verification keys
    [2019-12-09 12:26:24] <suraeNoether> may not even know the secret key, so it's genuinely adversarial
    [2019-12-09 12:26:28] <sarang> ya
    [2019-12-09 12:26:59] <sarang> The adversarial generation isn't really a big deal, since soundness implies the adversary's choice of keys satisfy the verification equations
    [2019-12-09 12:27:15] <sarang> and then you rely on the one-way mapping
    [2019-12-09 12:27:28] <suraeNoether> actually, it's not clear; each verification key needs to be in \mathcal{VK}, and it's not specified where that comes from, i'm assuming from the challenger
    [2019-12-09 12:28:03] <suraeNoether> in which case the adversary has to pick challenge keys to break linkability, it's not enough for the adversary to pack all rings with fake pubkeys
    [2019-12-09 12:28:05] <sarang> Backes even notes that generating `q` such signatures is trivial, since you simply use separate keys
    [2019-12-09 12:28:20] <sarang> Fake pubkeys should be acceptable
    [2019-12-09 12:28:41] <sarang> since the adversary does all this offline, or otherwise generates the pubkeys in its own (seemingly) valid transactions
    [2019-12-09 12:29:39] <sarang> The `q=1` case feels like some kind of targeted linking attack, where the general `q` case seems like a broader "hope for a collision somewhere" attack
    [2019-12-09 12:29:57] → rubdos joined (~rubdos@2a02:578:859d:700:8b44:5716:382d:a7da)
    [2019-12-09 12:30:25] <sarang> suraeNoether: thoughts?
    [2019-12-09 12:31:47] <suraeNoether> nothing concrete. the way this definition is written feels very very counter-intuitive to the way you and i have discussed linkability in the past.
    [2019-12-09 12:32:18] <sarang> Yeah, and I haven't seen it anywhere else
    [2019-12-09 12:32:30] <sarang> Again, I don't feel any particular need to use it
    [2019-12-09 12:32:45] <sarang> But getting the existing definition more formalized in a challenger-player sense seems wise
    [2019-12-09 12:33:00] <suraeNoether> agreed
    [2019-12-09 12:33:03] <sarang> roger
    [2019-12-09 12:33:10] <sarang> OK, that's my update
    [2019-12-09 12:33:22] <sarang> Does anyone else have interesting (or uninteresting) research to share?
    [2019-12-09 12:33:23] <suraeNoether> ok, dude, i think i know the problem here
    [2019-12-09 12:33:27] <suraeNoether> with that definition
    [2019-12-09 12:33:31] <suraeNoether> or at least my problem with it
    [2019-12-09 12:33:31] <sarang> Ooh, go on
    [2019-12-09 12:33:35] — sarang takes a step back
    [2019-12-09 12:34:02] <suraeNoether> linkability is a property that has a "correctness" component and a "soundness" component. to correctly link two things means to link them when they should be linked. to soundly link two things is to *only* link them when they should be linked
    [2019-12-09 12:34:18] <suraeNoether> you called this positive and negative linkability at some point
    [2019-12-09 12:34:30] <suraeNoether> i feel like this definition is mashing the two together
    [2019-12-09 12:34:37] <suraeNoether> or attempting to
    [2019-12-09 12:34:43] ⇐ Febo quit (59d411cd@89-212-17-205.static.t-2.net): Ping timeout: 260 seconds
    [2019-12-09 12:34:46] <suraeNoether> anyway, my thoughts don't go deeper than that yet
    [2019-12-09 12:34:59] <sarang> Backes uses non-frameability to show that you can't make signatures that _appear_ to link without knowing/using the same key
    [2019-12-09 12:35:17] <sarang> and linkability to mean that you can't make sigs with the same key(s) but different tag(s)
    [2019-12-09 12:35:20] → DryStorm joined (~Android@2607:fb90:70e0:9032:8b76:967a:ec36:1492)
    [2019-12-09 12:35:31] <sarang> The reviewer didn't like the CLSAG paper's use of positive/negative/soundness in linkability
    [2019-12-09 12:36:12] <suraeNoether> hmm
    [2019-12-09 12:36:15] <suraeNoether> okay, that's going to require more thought
    [2019-12-09 12:36:18] <suraeNoether> anywya, now i'm done. :P
    [2019-12-09 12:36:33] <sarang> A lot of this is simply getting the right terminology for the definition(s) of choice
    [2019-12-09 12:36:45] <sarang> I happen to like using linkability to refer to both
    [2019-12-09 12:36:52] <sarang> since that's typically what you want
    [2019-12-09 12:36:59] <sarang> but it's two different concepts
    [2019-12-09 12:37:10] <sarang> OK, we can move on to any other research
    [2019-12-09 12:37:15] <sarang> or to the next topic, QUESTIONS
    [2019-12-09 12:37:26] — sarang waits patiently
    [2019-12-09 12:39:30] — sarang waits impatiently
    [2019-12-09 12:39:32] <suraeNoether> i have a pretty general observation
    [2019-12-09 12:39:47] <suraeNoether> which may be relevant in terms of independent interest
    [2019-12-09 12:40:01] <suraeNoether> a property like linkability applies to all ZK proofs. for example, our ring signatures are ZK proofs of knowledge of a secret key. but they are *linkable* proofs of knowledge, so that if the same witness data (keys) are used for two different proofs (signatures), then an observer can link them.
    [2019-12-09 12:40:17] <suraeNoether> so just like ZK proofs have a property of correctness (if you know a witness, the proof is valid) and a property of soundness (if you don't know a witness, your proof is invalid), a linkable ZK proof is going to have a dual pair of notions for linkability
    [2019-12-09 12:40:43] <suraeNoether> i bring this up so that the next version of snarks has an L floating around
    [2019-12-09 12:40:53] <sarang> There's a related-ish property in sigma protocols, quasi-unique responses
    [2019-12-09 12:41:01] <sarang> But that relates to responses to the verifier challenge
    [2019-12-09 12:41:32] <suraeNoether> more reading to do :\
    [2019-12-09 12:42:06] <sarang> There's probably a subtle relationship to (SHV)ZK
    [2019-12-09 12:42:13] <sarang> and therefore witness indistinguishability
    [2019-12-09 12:42:17] <sarang> (which follows from SHVZK)
    [2019-12-09 12:42:39] <suraeNoether> anyway
    [2019-12-09 12:42:40] <sarang> Normally, providing two proofs should not reveal distinguishing information about the witnesses
    [2019-12-09 12:42:50] <suraeNoether> right
    [2019-12-09 12:43:42] <sarang> Hopefully you will enjoy the Triptych paper, which builds a linkable construction on top of a sigma protocol :)
    [2019-12-09 12:44:31] <suraeNoether> i enjoyed it the last time i read it, and the tiem before that. it takes awhile to digest :P
    [2019-12-09 12:45:46] <suraeNoether> ok, i gotta bounce, i'm not feeling well; my list of 3 unfinished tasks is also my list of action items today
    [2019-12-09 12:46:17] <sarang> roger
    [2019-12-09 12:47:28] <sarang> My ACTION ITEMS are getting these new definitions and proofs typeset and finalized, determining their DLSAG applicability, a few other organizational issues on the CLSAG paper to prepare it for resubmission, and getting Triptych submitted on review
    [2019-12-09 12:47:49] <sarang> Any other final thoughts, comments, or questions before this meeting ends?
    [2019-12-09 12:48:34] <moneromooo> I have an unrelated question.
    [2019-12-09 12:48:43] <sarang> ?
    [2019-12-09 12:49:10] <moneromooo> I was wondering whether atomic swaps between two cryptonotes with hte same curve etc (ie, not the general case) is possible now.
    [2019-12-09 12:49:37] <moneromooo> Well, assuming the tooling was there of course, which it isn't.
    [2019-12-09 12:49:50] <moneromooo> In theory I mean.
    [2019-12-09 12:50:01] <sarang> I don't know of a good way that retains indistinguishability as well as DLSAG does, and that still has the tracing issue
    [2019-12-09 12:51:09] ⇐ midipoet quit (uid316937@gateway/web/irccloud.com/x-pasvabfzkhakemhq): Quit: Connection closed for inactivity
    [2019-12-09 12:51:12] <sarang> If you were willing to accept and mitigate the tracing issue, then its method could do it
    [2019-12-09 12:51:18] <sarang> its = DLSAG's
    [2019-12-09 12:51:46] <moneromooo> What is the tracing issue already ?
    [2019-12-09 12:53:28] <sarang> The fixed basepoint used for dual-address key images allows determination of unwanted signature linking
    [2019-12-09 12:54:21] <sarang> It isn't clear how to do a DLSAG-type construction with the variable-basepoint key images used currently
    [2019-12-09 12:55:40] <sarang> I should more precisely say, the use of a fixed basepoint and having output private keys used as the corresponding key image discrete log (this doesn't exist in more recent constructions that use a fixed basepoint but in a different way)
    [2019-12-09 12:56:49] <sarang> Oh, suraeNoether: do you think it's useful in the LA definition to include the linking tag oracle separately from the signature oracle?
    [2019-12-09 12:57:30] <sarang> The player can get the linking tag oracle result simply by querying the signature oracle on a public key by using a random ring and message (and ignoring everything but the returned linking tag)
    [2019-12-09 12:58:39] <sarang> Having a separate oracle only really serves to make it clear that the player doesn't necessarily need to convince a user to sign messages, but can obtain linking tags otherwise
    [2019-12-09 12:58:47] <sarang> (although in this security model, it can do both)


# Action History
- Created by: SarangNoether | 2019-12-05T13:13:16+00:00
- Closed at: 2019-12-09T18:02:43+00:00
