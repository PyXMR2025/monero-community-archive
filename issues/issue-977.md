---
title: 'Seraphis wallet workgroup meeting #61 - Monday, 2024-03-11, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/977
author: rbrunner7
assignees: []
labels: []
created_at: '2024-03-08T14:49:29+00:00'
updated_at: '2024-03-11T19:06:29+00:00'
type: issue
status: closed
closed_at: '2024-03-11T19:06:29+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/975

# Discussion History
## rbrunner7 | 2024-03-11T19:06:29+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/977
<s​needlewoods_xmr> hey
<d​angerousfreedom> Hello
<j​effro256> howdy
<0​xfffc> Hi everyone
<r​brunner7> On to the the reports. ghostway wrote earlier today that they will go back to the key container this week, after a break.
<j​berman> hello
<s​needlewoods_xmr> I'm "back" and was finally able to fix the rebase here https://github.com/seraphis-migration/monero/pull/16 with help from jeffro and dangerousfreedom
<jeffro256> +1
<0xfffc> +1
<d​angerousfreedom> Not much to report from my side this week. I'm a bit stuck waiting for the final word about the enote_store serialization and was just reading books this week. Any idea when a decision will be made about continuing using the serialization_demo_utils and the ser_* structs for de/serialization?
<r​brunner7> Fine. Is that ready for squash and review already, SNeedlewoods ?
<j​berman> Update: scanner tests are going smooth. Pushed a test for all legacy enote versions: https://github.com/UkoeHB/monero/pull/23/commits/b27ad8966391d29336a7a718387754103313ef19
<jeffro256> +1
<s​needlewoods_xmr> +1
<0xfffc> +1
<j​berman> I'm nearing completion setting up a framework to test the full wallet <> daemon flow, where wallet2 sends/receives, then seraphis lib scans the txs (then eventually can be used to construct Seraphis txs as well once daemon code is set up). It's building off `functional_tests/transactions_flow_test.cpp`
<j​effro256> I'm waiting on reviews for https://github.com/UkoeHB/monero/pull/31 and https://github.com/UkoeHB/monero/pull/34 before  re-writing the serialization code
<d​angerousfreedom> +1
<s​needlewoods_xmr> +1
<0xfffc> +1
<s​needlewoods_xmr> the last commit was a WIP with a very small change I had in mind, then I would say it's ready for reviews
<j​effro256> Pining @UkoeHB for a discussion if available at the moment
<r​brunner7> jeffro256: So the way is to show that your new serialization system won't be worse, thanks to the modifications in those PRs, to get the final nod from UkoeHB?
<0​xfffc> Me: I have been busy on XMR side, haven’t started seriously working on LMDB for Seraphis. But I expect by next week I will have some updates.
<dangerousfreedom> +1
<j​effro256> I wanted to revert the way Seraphis txs reference legacy enotes from the flat index to the (amount, index_in_amount) pair
<j​effro256> Even though the flat indices make the transactions smaller, the DB in reality will likely be larger because now it needs to keep track of 2 methods of indexing. Also, we would need 2 methods in `TxValidationContext` for referencing legacy enotes. However, I do want the flat indices when reference Seraphis enotes
<s​needlewoods_xmr> jberman are you planning to work on this issue https://github.com/UkoeHB/monero/issues/27 yourself?
<s​needlewoods_xmr> if no one else has a suggestion for me to work on, I would resume to look into that
<j​effro256> Well those 2 PRs change the structure of the transaction classes slightly, and so the new serialization code depends on those PRs.
<j​berman> got for it :)
<r​brunner7> jeffro256: I see, but I think dangerousfreedom was speaking more of a general decision, whether the way to go is to eliminate those `ser_` classes for everything. And as far as I know UkoeHB may have some reservations until it's shown that the new system is not worse regarding memory and speed.
<r​brunner7> I was assuming that the PRs you mention will show that
<j​effro256> Ohh, yeah that's 90% likely the way to go IMO. Koe had a problem specifically with the way that I serialized certain fields redundantly, but that API will likely remain the same
<d​angerousfreedom> Yes. I think so, we briefly discussed the new scheme and I think he is coding the new scheme that should look like this: https://github.com/seraphis-migration/strategy/wiki/Key-Container#wallet-tiers-and-keys-hierarchy
<jeffro256> +1
<j​effro256> (i.e. we will likely remove the `ser_*` structs)
<r​brunner7> So you think that dangerousfreedom could go ahead, with only some small residual risk remaining?
<j​effro256> Yes, I think so
<j​effro256> I cam write a WIP PR that has the same API and dependencies on the other PRs that actually affect the in-memory structure of the transaction classes
<d​angerousfreedom> Yes. IMO it is just about notation. jeffro's macro would be doing the same thing. I just don't want to write thousands of useless lines.
<r​brunner7> Those `ser_` classes look out of place in the light of the elegance of the rest of the Seraphis library. I think nobody will shed many tears for them, if the alternative is viable.
<s​needlewoods_xmr> +1
<d​angerousfreedom> +1
<r​brunner7> So we leave it to dangerousfreedom whether he will wait a little longer or take the plunge already.
<d​angerousfreedom> Yeah, I will be more active this week
<r​brunner7> Do I see that right, things may change again if/when 0xFFFC can switch to LMDB for the enote store, but that may take a while?
<j​effro256> And i'll write a PR that he can use as a dependency. The internals may change, but the API shouldn't change much
<dangerousfreedom> +1
<r​brunner7> And so being able to read and write the enote store already is still useful.
<j​effro256> dangerousfreedom: what are you actually serializing at a top level? Enotes, Enote records, contextualized enote records, etc ?
<j​effro256> Do you actually serialize any transactions directly?
<d​angerousfreedom> Everything of the serialization_demo_utils and everything that is needed for the enote_store serialization
<j​effro256> So yes to actual full transactions?
<d​angerousfreedom> Yes
<d​angerousfreedom> Is there a way to easily serialize member variables of classes? Like we do to structs?
<j​effro256> Yeah, depends what it is, but if you use `FIELD_N`, that should cover most needs
<0​xfffc> Regarding serialization code? I expect not much needs change.
<d​angerousfreedom> Ok, thanks
<r​brunner7> That sound a bit surprising, but maybe I am not deep enough into this enote store thing ...
<d​angerousfreedom> Even if they are private members?
<j​effro256> Or you can use `FIELDS` if you don't want to tag the object
<j​effro256> Unfortunately, no
<j​effro256> Well, actually yes, if it's a member function
<j​effro256> it just follows normal c++ access rules. If the serialization function is a member function, it can access private member fields. If its a non-friend free function, then it can't
<d​angerousfreedom> Ok. Then we need to create special functions for it. Like I was doing for the ser_* thing.
<r​brunner7> Any special general subject to discuss today?
<r​brunner7> Ah, is there already new stuff waiting in the Seraphis library GitHub to merge into our repository?
<j​effro256> I wanted to discuss reverting the Seraphis legacy enote referencing scheme
<j​effro256> Yes, mainly stuff was merged from the core project that allows CI to finally pass
<r​brunner7> Thanks, will look at that.
<j​effro256> So rebasing should be pretty trivial IIRC
<r​brunner7> Why "reverting"? Was there once a different referencing scheme active in the library?
<j​effro256> Not in the library, but it generally useses a different referencing scheme that the rest of the cryptonote codebase
<j​effro256> Which would add extra data to the DB and make legacy validation a little more bloated
<r​brunner7> ... but has advantages that you see, I guess?
<j​effro256> Yes its more compact inside the txs
<j​effro256> And makes the function signature for retrieving legacy output info from a validation context simpler iff you aren't validating legacy txs
<d​angerousfreedom> The added extra data in the DB is not useful? What is that?
<j​effro256> It's useful for indexing in that flat manner, but we already have a way to index legacy enotes, and DB is already stuctured like that
<j​effro256> If we used the new flat referencing scheme for legacy enotes, it would require a length DB migration
<j​effro256> If we used the new flat referencing scheme for legacy enotes, it would require a lengthy DB migration
<d​angerousfreedom> Oh I see, you are talking about the indexing variable.
<d​angerousfreedom> Maybe an example or table comparing both would be good ?
<r​brunner7> So it might be that this design decision did not look far enough beyond the needs of the Seraphis libary proper to weight all trade-offs?
<r​brunner7> "lengthy DB migration" does not sound attractive, if indeed necessary
<r​brunner7> But well, it would be only once, and if there are good advantages of the new indexing scheme ...
<j​effro256> I personally think the negatives outweight the positives since for each CLSAG input, a max of 8 (but usually 1) bytes are saved inside the transaction, but we need at least 24 extra bytes per legacy enote output
<r​brunner7> Any cross-connections with FCMPs that you could imagine? Maybe a simplified indexing scheme is very beneficial for those?
<j​effro256> I'm only referring to how legacy enotes are referenced in the CLSAG inputs, not how Seraphis enotes are referenced. We can't do FCMPs on RingCT enotes
<r​brunner7> Ok :)
<r​brunner7> I guess judging those trade-offs are something that goes beyond my knowledge. Maybe jberman can chime in?
<d​angerousfreedom> I dont get the last part about the 24 extra bytes. Why do we need that? Isnt enough saving 1 to 8 bytes?
<j​effro256> So before, we index legacy enotes with a pair (amount, index) (`cryptonote::txin_to_key`). The way Seraphis lib does it now is just with one unified index number. Assuming that the amount=0 (i.e. a RingCT input), the Seraphis indexing scheme saves 1 byte per tx. However, since we have a new unified index, we need to support that in the DB. To do this, we need to map unified indiced -> (amount, index) pairs. This costs at least 24 bytes per output enote in the database
<j​effro256> *1 byte per input, not tx
<r​brunner7> dangerousfreedom 's proposal also crossed my mind: Maybe a GitHub issue with a nice comparison of the two indexing schemes would be useful.
<j​effro256> Will do
<r​brunner7> Splendid!
<r​brunner7> You can't get fully rid of the old scheme, right, because there are parts of the DB we can't rewrite in a suitable way?
<j​effro256> Probably not if we are supporting legacy tx validation since the data inside the transaction is given to us in the (amount, index_into_amount) form
<r​brunner7> Ok, hopefully the info in that issue will spark some further informed discussion.
<r​brunner7> Anything left for today? We are nearing the full hour.
<d​angerousfreedom> Thank you jeffro256 !
<r​brunner7> Does not look like it. Thanks everybody for attending, nice how we get more and more people working on this! Read you again next week.
<d​angerousfreedom> Thanks
<s​needlewoods_xmr> I think it's nice to see this group so active, too, thanks everyone
<jeffro256> +1
<0xfffx> +1
<j​effro256> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2024-03-08T14:49:29+00:00
- Closed at: 2024-03-11T19:06:29+00:00
