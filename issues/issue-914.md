---
title: 'Seraphis wallet workgroup meeting #43 - Monday, 2023-10-30, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/914
author: rbrunner7
assignees: []
labels: []
created_at: '2023-10-28T05:43:16+00:00'
updated_at: '2023-10-30T19:23:12+00:00'
type: issue
status: closed
closed_at: '2023-10-30T19:23:11+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/911

# Discussion History
## rbrunner7 | 2023-10-30T19:23:11+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/914
<j​effro256> Howdy!
<r​brunner7> dangerousfreedom is excused, he can't make it today, but he left quite some info about where he currently stands a few hours ago here on Matrix
<j​berman> hello!
<r​brunner7> Alright. What is there to report?
<j​berman> Submitted a rough draft PR for the async scanner: https://github.com/UkoeHB/monero/pull/23
<jeffro256> +1
<j​effro256> I opened a new CCS proposal for Seraphis/Jamtis/wallet3 work
<r​brunner7> I tried to "sell" the unified transaction class problem to dangerousfreedom , but I am reading now "This problem is too big for me" ...
<r​brunner7> @jberman: Is the Seraphis library the right place for this scanner? Is it generic enough that it can scan without anything called "wallet"?
<r​brunner7> jeffro256: Saw your CCS proposal and left a short comment
<jeffro265> +1
<j​effro256> I'm also working on a fast persistent database to cache blockchain-style data. Right now, I specifically have in mind the RingCT output distribution, since that gets fetched every single transfer time
<j​berman> I don't know what the right place for it is :/ It's generic that it can scan without anything called wallet
<r​brunner7> Well, in this case it's probably in the right place, I would speculate. If we count it as part of "our" wallet somehow, it probably won't stay independent for long, and other people will get problems using it if they build something considerably different.
<jberman> +1
<r​brunner7> > I'm also working on a fast persistent database to cache blockchain-style data
<r​brunner7> Why not just serialize the same way like all the other stuff?
<j​effro256> For better speed and better memory usage. My DB can do O(1) reads, pushes, and pops. If you only want to access the "tip of the chain", you can do that without having to deserialize and re-serialize the entire blob of information. Seeing as this would be about 14 MB of data for the current RingCT distribution, doing it like we currently do for the wallet cache would slow down load/store times
<j​effro256> jberman: in one sentence, what are the main daemon changes ?
<r​brunner7> "My DB" is not LMDB?
<j​effro256> No, its built specifically for storing linear data
<j​effro256> It's pretty simple, but really fast for the specific use case of storing a vector of byte data persistenly
<j​berman> The `/getblocks.bin` RPC endpoint supports (1) an optional `max_block_count` request param, (2) the response includes the top block hash in addition to chain height, and (3) if the request includes a `start_height > chain tip` the server returns empty blocks + the chain height + top block hash instead of an error response
<jeffro256> +1
<r​brunner7> Well well, that sounds for me like a jump upwards in complexity as far as storing things for the wallet are concerned, introducing another storage format.
<r​brunner7> Something I would personally do only under great duress, if I had a tricky problem that is almost impossible to solve otherwise.
<r​brunner7> Kicking and screaming, do they say so in English, right?
<r​brunner7> And don't we all know how these "It's pretty simple" things usually go over time?
<r​brunner7> We would also need 1 file more, probably?
<j​berman> kayabanerve had a good idea to improve the output distribution fetching part of tx construction: the wallet could in theory update the output distribution as it scans the chain (and request the full distribution on wallet init), thus not needing to make the request for the output distribution at tx construction time
<j​berman> (and keep a local cache of the distribution while scanning)
<r​brunner7> Don't missunderstand, I believe in no time that jeffro256 is building something nice and clever; for me it's about the trade-offs
<j​berman> I would think that route^ would yield a more tangible improvement on this aspect fwiw
<r​brunner7> Say in 1 sentence what the "output distribution" is?
<j​effro256> Yeah that's a great idea, and it can also work together with a persistent database. If you fetch the information during scanning, then save it to file using a DB, you'll never have to fetch the output distribution outright, saving a lot of bandwidth
<r​brunner7> Dear jeffro256 , you don't really want to sell me the idea that nowadays you need a DB to manage 14 MB of data. Or do you?
<j​effro256> The number of tx outputs per blockl
<r​brunner7> Instead of a simple file where you just dump that
<j​effro256> Starts at RCT fork height
<r​brunner7> So a big mass of ints?
<j​berman> pretty much
<j​effro256> Yes
<r​brunner7> Oh, come on :) This merits 0% of drama as far as storage is concerned if you ask me
<r​brunner7> Not fetching it a hundred times a day is another story of course, well worth of optimizing in some clever way if reasonably possible
<r​brunner7> And of course this stays relevant for Seraphis?
<g​hostway> sorry for being late
<r​brunner7> Hi there ghostway !
<j​effro256> Yeah until we have FCMPs
<f​> TIL UTC doesn't just jump with my locally set cell phone alarm ^^
<r​brunner7> Alright, I am well aware that I don't have any veto power whatsoever, but please, jeffro256 , reconsider that proprietary DB stuff just for storing this ...
<j​berman> I'm generally with rbrunner7 here, exploring a DB seems a bit like premature optimization at this stage
<j​berman> First general thought after reading dangerousfreedom 's above comments: I think we should prioritize work to ship a wallet that functions *today* that uses the Seraphis wallet lib for wallet storage, scanning, and reuses wallet2 for constructing txs. The final wallet shipped for the Seraphis update would need to support this functionality (it must function for today's chain) and w<clipped message>
<j​berman> ill need to be tested extensively before shipping to end users, so the earlier we get this shipped and tested the better. This means de-prioritizing work focused on the Seraphis tx types and keys, and prioritizing work that moves us out of wallet2 and closer to wallet3 that works *today*
<r​brunner7> Interesting approach. Probably needs some thinking through how that could work.
<j​berman> My first thought on how to support Seraphis tx types across the code base (even though I think we shouldn't prioritize this work yet) is that trying to rewrite all places that currently use `cryptonote::transaction` to use a new transaction type would be way more (risky) work than modifying `cryptonote::transaction` to support the Seraphis tx types. If we want to try to get rid of<clipped message>
<j​berman>  the spaghetti code of `cryptonote::transaction`, then it could perhaps have logic like: if tx.version > 2, then the first field stored on the transaction is a Seraphis-specific variant and the Seraphis-specific variant contains all new tx-related logic (which would include pruning functions). Or we could try to re-use a lot of that `cryptonote::transaction` code and extend it for<clipped message>
<j​berman>  Seraphis. I would probably focus exploration in this direction, rather than trying to rewrite everything everywhere that uses `cryptonote::transaction`, but again reiterating I think this is lower priority than trying to get a Seraphis wallet that functions today out the door
<g​hostway> wait was the dispute over another key for jamtis settled?
<g​hostway> the thing tevador and jeffro256 have worked on
<r​brunner7> I somehow uncounsciously dismissed such an approach, extending `cryptonote::transaction`, because that way we will stay rooted too deep in the past.
<r​brunner7> Maybe also because of a gut feeling "How on earth we bring that past UkoeHB" :)
<r​brunner7> His almos perfect types wrapped in, of all things, the spaghetti monster itself, `cryptonote::transaction`
<j​effro256> I might tend to disagree on this one... I think a better design would be to leave `cryptonote::transaction` untouched, then have a new transaction type class, which you can convert into a `crytonote::transaction` class. This is a little less efficient, but would allow us to move away from that legacy codebase at some distant point in the future while not changing the concensus cod<clipped mess
<j​effro256> e at all for the moment
<r​brunner7> Does such a conversion work at all? Color me surprised
<j​berman> Ya I like that too. I agree that's a better approach than trying to rewrite everywhere that uses `cryptonote::transaction` today
<UkoeHB> If you can shoehorn seraphis into cryptonote::transaction then it's worth thinking about if that speeds things up significantly.
<r​brunner7> But is that able to hold everything that it would need to hold?
<j​effro256> I mean, have a method for the new class type, say `make_cryptonote_tx()` which instantiates a new `cryptonote::transaction` that represents the semantics of a cryptonote rules etched into the new Seraphis tx
<r​brunner7> That's too high for me now
<j​effro256> IMO it could speed things up *now*, but it would add technical debt
<r​brunner7> Loads of such debts, mountains even :)
<r​brunner7> Borders on cheating somehow
<r​brunner7> But well, rewriting much of the code is no walk in the park either, that's for sure
<r​brunner7> But again, can you "express" somehow all important things that there are to know about a Seraphis transacition in a standard `cryptonote::transaction` object?
<r​brunner7> Or would that need to learn at least some new tricks first?
<j​effro256> You don't need to since you can always *add* Seraphis-specific consensus rules and fail before/after
<r​brunner7> Maybe you could take the time and write an issue and flesh out that idea so that it's better to understand? You may be onto something very nice here, but it's still very rough, and I don't fully understand it yet
<r​brunner7> My example, if I think about transaction classes, is mostly the transaction pool in daemon memory in the transaction phase, with a wild mix of transactions old and new
<r​brunner7> transaction phase -> between the hardforks
<j​effro256> For example, one of the most important verification functions in the entire Monero codebase is `Blockchain::check_tx_inputs()`. If you want to verify legacy inputs, you first derive a copy of `cryptonote::transaction` from your new all-encompassing Seraphis tx type, pass it to `Blockchain::check_tx_inputs()`, then do Seraphis-specific checks afterwards (or before doesnt really mat<clipped mess
<j​effro256> ter) on the new object. Repeat this pattern for different parts of the legacy transaction...
<j​effro256> You're right though, I need to flush this out more
<r​brunner7> Yeah, but have you seen how wild the ways are the software shuttles transactions back and forth? Serializes and deserializes multiple times, out of the blockchain, into the pool, out of the pool, JSON to the wallet. Don't you need some nice data package containing *everything* about a particular transaction?
<j​effro256> Well yeah, that would be what the new tx type would be. But if you can make a (probably lossy) conversion from new tx type -> `cryptonote::transaction`, then you can interact with the consensus code without having to modify it all
<r​brunner7> And how do you store that stuff in the blockchain?
<r​brunner7> Because processing is one thing, storing is another
<j​effro256> When serializing/deserializing, use tx version 3. If you deserialize, get version code 3, switch to new transaction type serialization
<r​brunner7> So code within `cryptonote::transaction` would trigger to certain versions and act accordingly?
<r​brunner7> Yeah, well, maybe that class only needs to learn 1 new trick, "Now I am a Seraphis transaction, pointer to it is -> here"
<j​effro256> I'm saying that the new deserialization would be backwards compatible with `cryptonote::transaction` if version <= 2
<r​brunner7> That's so crazy that could work :)
<r​brunner7> Well, it almost has to be, otherwise we would force a blockchain conversion, people would jump up and down with joy
<j​berman> this is pretty much what I was saying, I agree this is the saner approach than rewriting everywhere that uses `cryptonote::transaction`
<j​berman> On argon2 for password-based key derivation, I think we are ok doing without it and with reusing cn_fast_hash, but I'm not opposed to switching. I think the encryption/decryption flow should be written such that this decision would ideally be a few line change in that code, so we can make the decision at any point later. I also agree that argon2 is the stronger choice and I think <clipped message>
<j​berman> the fact that it's used in randomx is also a solid reason to use it
<r​brunner7> I share your sentiment, I have a suspicion dangerousfreedom sees a future switch as more complicated than it will turn out to be
<r​brunner7> ghostway 's little "encrypted file" class may be a step into the right direction here, as far as some encapsulation is concerned
<f​> I'd like to throw in some thoughts on Pasta / FCMP's: I've been looking into the possibility of signing transactions using smart cards. The industry generally seems to be a bit behind and, currently, there don't seem to be any chips offering "our" Ed25519. I hope for this to change in the next couple of years.
<f​> Support for Pasta, however, is unlikely. Still, I wonder if someone can provide comparable data as far as computational demands are concerned: Could Pasta still work, technically on a smart card or exceed it's capabilities? (Note: I didn't research the scheme myself yet.)
<j​berman> jeffro256 can you give a quick status update on this/where you see things stand?
<r​brunner7> Really quick, we are already past the hour :)
<j​effro256> Sorry I meant to respond to that. I don't want to speak for tevador, but I think that he leans towards "yes" on the extra key *IF* the view tags changes are also implemented
<j​berman> view tag changes meaning dynamic view tags?
<r​brunner7> Viewtags becoming dynamic in size, it that it?
<j​berman> jinx haha
<j​effro256> The view tags actually remain the exact same size in-blob, either 2 or 3 bytes, but there's a value per-tx, which I call `num_primary_view_tag_bits` that controls how many bits to match on the "primary" view tag and how many to match on the "complementary" view tag
<r​brunner7> Wow, that's a plot twist
<j​effro256> I proposed that that value is enforced by relay rules, instead of consensus rules for simplicity and protocol and flexibility
<j​effro256> So its more of a "flexible" view tag versus "dynamic"
<r​brunner7> I trust that has some solid advantages, as an approach?
<j​effro256> I proposed that that value is enforced by relay rules, instead of consensus rules for simplicity and protocol flexibility
<j​effro256> Yeah basically you get the benefits of being able to adjust bandwidth requirements for light wallets as a community without consensus changes, but you don't have the complexity problems of having to fetch chain data in order to determine which view tag "size" to use
<j​effro256> Also if we do 2-byte flexible view tags, the transactions are 1 byte per-output smaller
<r​brunner7> Interesting
<r​brunner7> Alright, has been very interesting today, let's close nevertheless the meeting proper here, thanks everybody for attending!
<j​berman> would be nice to have a single consolidated post that has the different proposals on the table laid out with pros/cons
````


# Action History
- Created by: rbrunner7 | 2023-10-28T05:43:16+00:00
- Closed at: 2023-10-30T19:23:11+00:00
