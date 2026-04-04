---
title: 'Monero Tech Meeting #126 - Monday, 2025-06-30, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1227
author: rbrunner7
assignees: []
labels: []
created_at: '2025-06-27T14:23:05+00:00'
updated_at: '2025-06-30T18:54:57+00:00'
type: issue
status: closed
closed_at: '2025-06-30T18:54:57+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1221).


# Discussion History
## rbrunner7 | 2025-06-30T18:54:57+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1227
<s​yntheticbird> hello
<j​effro256> Howdy
<s​needlewoods> hey
<j​berman> *waves*
<r​brunner7> Nice y'all are here :)
<r​brunner7> Alright, what do you have to report from the last 2 weeks?
<s​needlewoods> worked on WalletListener and refresh
<j​effro256> Monerokon was great. FCMP++ optimization competition submission deadline is now closed. Reviewing a *very* promising divisor submission. Cleared a bit of backlog on the FCMP++ integration. Fixed some transfer bugs and closing gaps in feature parity for the wallet.
<r​brunner7> It's still June 30 in some places on Earth ...
<s​yntheticbird> yes
<s​yntheticbird> UTC we're still June 30
<j​berman> Reduced db storage for each output in the tree (https://github.com/seraphis-migration/monero/pull/62), PR review / updates, worked on subaddress expansion (https://github.com/monero-project/monero/pull/9953), contest submission review
<j​berman> We received 2 helioselene submissions and 1 ec-divisors submission. All submissions look like quality submissions to me on first pass. We'll be reviewing both over the next week
<syntheticbird> +1
<r​brunner7> That already includes that "Triton" person that entered pretty late?
<j​effro256> Close time is technically 17:00 UTC, although I probably wouldn't completely disregard a submission from June 30th in some other timezone
<r​brunner7> I see
<j​berman> No I didn't see a submission from them
<j​effro256> Me neither
<s​yntheticbird> Are some of the submissions anonymous ?
<s​needlewoods> and here is a WIP branch https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_remove_wallet2_from_simplewallet
<s​needlewoods> if anyone wants to take a look at the current state of the Wallet API and the CLI, but keep in mind most stuff in the CLI is still broken
<j​berman> don't believe so
<j​effro256> I know one of the contestants personally, one I've heard of their usernames in passing, and the third I haven't heard of him before, but the submission is tied to their Github persona which has a decently long history
<r​brunner7> At least no deluge of AI slop, thankfully
<j​effro256> Oh we got that, don't worry ;)
<j​berman> There were a couple AI submissions early on that looked pretty clearly like AI and didn't pass the tests
<r​brunner7> Ok :)
<s​yntheticbird> HELLO HERE AN OPTIMIZATION (WITH SIMPLIFIED CODE) OF YOUR PROBLEM: 
<s​yntheticbird> ```
<s​yntheticbird> // useless code in another language
<s​yntheticbird> ```
<s​yntheticbird> Powered by EquationAIv9000 TRADEMARK
<s​yntheticbird> Please share the AI slop
<s​yntheticbird> for posterity
<r​brunner7> Nice try
<j​effro256> Yeah basically
<r​brunner7> If we are complete with reports, and heard what there is to know about the contest as of today, I have a technical Monero question for the people in the know that we have attending
<r​brunner7> Today the subject of transaction secret keys came up in the Monero subreddit, in connection with MyMonero which does not seem to suppor them, or at least does not feel like telling them in the UI
<r​brunner7> Is it correct that I need a transaction secret key in order to build a spend proof?
<j​effro256> Yes
<r​brunner7> And that key is info that you can't restore from the blockchain, using your seed / spend secret key, right? Once you lose it, it's gone for good?
<j​effro256> With the current wallet implementation, yes
<j​effro256> You could generate them deterministically, like addresses / BIP, etc, but we don't
<s​yntheticbird> proposal: encrypt the secret key and put in tx_extra
<j​effro256> plowsof ban this guy
<s​yntheticbird> deserved
<s​needlewoods> lol
<r​brunner7> No disadvantages or even dangers of exploits if we switch to deterministic tx secret keys?
<plowsof> moment 
<r​brunner7> I don't think dear plowsof has mod rights here ...=
<j​effro256> The disadvantage would be that if someone got a hold of your seed phrase, they could retroactively see outgoing payments, whereas currently they cannot
<j​effro256> (seed phrase or other master key depending on how you derive them)
<p​lowsof:matrix.org> emoji reaction rights are sufficient enough for this purpose
<r​brunner7> Hold on! If I restore a wallet using a seed I see the transactions I sent, no? I just don't see *where* I sent them
<j​effro256> Yes
<r​brunner7> So with a deterministic tx secret key there would be more to see, you mean?
<j​effro256> You can't see that you spent X XMR in a transaction, and only got Y<X change back, so you spent X-Y XMR in that transaction, but you don't know the addresses, or how the amounts are split up in a multi-destination tx
<j​effro256> * You *can* see that you spent X XMR...
<j​effro256> Stupid matrix formatting
<r​brunner7> I think I get what you mean :) Still did not get what exact difference compared to today a switch to deterministic would cause
<j​effro256> Yes, with deterministic tx secret key, someone who collects Monero addresses could determine that an output is addressed to a specific Monero address if they know that address
<r​brunner7> Behind my questions is - of couse - the ultimate question how this will be with Carrot, and whether there will be an improvement on that front
<s​needlewoods> so you also can't do tx proof from a restored wallet? with current non-deterministic tx secret key
<r​brunner7> SNeedlewoods: Exactly, that seems to be the problem. Which is not really nice, and unexpected
<j​effro256> It's the same with Carrot: not done by default in `wallet2`, but it *is* technically possible
<s​yntheticbird> that is by supposedly having the seed of the sender
<r​brunner7> Well, it must not only be technically possible, but also *feasible* in the sense that the trade-offs are ok, that the advantages are greater than the disadvantages
<j​effro256> Nope, not currently possible
<r​brunner7> Was this ever discussed in detail lately? Carrot would be a nice point to switch, seems to me, *if* it's ok to do that
<j​effro256> Yes
<s​yntheticbird> With the seed trust assumption I don't really see a danger here at switching to deterministic. Let's imagine that one individual get their seed leaked. At best the adversary will know he paid specific public addresses. In practice, most exchanges/merchants are generating new addresses for every transactions
<s​yntheticbird> The adversary being capable of collecting these addresses through say TLS, is actually a sign of a security cataclysm
<j​effro256> Unless they're using a payment processor which uses integrated addresses, e.g. Monerointegrations
<s​yntheticbird> very true
<j​effro256> Or donation links
<s​yntheticbird> yeah i included these ones in "specific public addresses"
<r​brunner7> Hmm. I would probably lean towards making the system more foolproof for users, with better UX, and take that small additional security problem - after my seed already leaked and I lost all funds! - in exchange any day. But I see that getting consensus here might be difficult.
<j​effro256> Or if we assume quantum computers become a thing someday, a state-level adversary could collect TLS traffic using non-PQ secure encryption to decrypt and collect addresses later
<syntheticbird> +1
<s​yntheticbird> I see a privacy reduction here regarding forensic. With a seed only you can't prove right now that you paid X. But with deterministic you can with X public address.
<s​yntheticbird> wouldn't there be some plausible deniability closing with this?
<s​yntheticbird> I would lean against just for that honestly
<j​effro256> Yes basically. For real-world use cases relevant to people today and known technology, the biggest threat vector is law enforcement or criminals seizing/coercing physical crypto wallets to extract seeds and checking where XMR was sent to
<j​effro256> If tx secrets are discarded after use as is done now, the sender has some plausible deniability
<j​effro256> But yeah I agree it sucks for UX
<r​brunner7> Well, as long as you still have the wallet file, somebody can force to go hand over *that*
<r​brunner7> *force you to
<j​effro256> This is true
<s​yntheticbird> Can't the spend proof be done in an handshake manner
<s​yntheticbird> requiring receiver participation
<s​yntheticbird> Receiver send some data and sender can use their public key to prove
<j​effro256> That A) doesn't solve the UX problem of not being restorable, and B) doesn't work if the receiver isn't cooperative (i.e. they *want* you to not be able to prove payment)
<r​brunner7> I think one of the often occuring use case is receiver having no idea where and when and how they should have received a transaction, and now they put the burden on you to prove you sent something. Hard to ask somebody like that for a handshake, maybe
<s​yntheticbird> true
<j​effro256> Or if the receiver goes offline ...
<j​effro256> If the receiver is willing to cooperate with you to generate a spend proof, you probably don't *need* a spend proof in that situation
<syntheticbird> +1
<s​yntheticbird> honestly sender plausible deniability is a huge deal in my eyes (i'm a good citizen). In democratic countries, in an ideal state where you don't suffer a wrench attack, you could just say you sent 5$ to your grandma and not your underground pet fighting tournament and they can't prove it, nor deny it. With this change they will be able to know when you lie.
<s​yntheticbird> I think this is significant
<r​brunner7> Ok, I learned a few interesting things. I have a gut feeling changing to deterministic couldn't achieve lose consensus today
<r​brunner7> So it's not a bug, it's a feature. Old dev wisdom :)
<s​yntheticbird> i might have repeated myself sorry about that
<r​brunner7> Ok, anything left for today's meeting?
<s​needlewoods> Not from me
<r​brunner7> Does not look like it. Thanks for attending everybody, read you again in 1 week!
<s​yntheticbird> thanks
<s​needlewoods> thanks everyone, delightful meeting
<j​effro256> Thank you, everybody!
````


# Action History
- Created by: rbrunner7 | 2025-06-27T14:23:05+00:00
- Closed at: 2025-06-30T18:54:57+00:00
