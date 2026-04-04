---
title: 'Seraphis wallet workgroup meeting #46 - Monday, 2023-11-20, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/930
author: rbrunner7
assignees: []
labels: []
created_at: '2023-11-17T16:04:21+00:00'
updated_at: '2023-11-20T19:18:55+00:00'
type: issue
status: closed
closed_at: '2023-11-20T19:18:55+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/927

# Discussion History
## rbrunner7 | 2023-11-20T19:18:55+00:00
````
<d​angerousfreedom> Hello, I cant stay the whole meeting but from my side I have almost finished the serialization of the enote_store. I will open a PR to the seraphis_lib this week. So now I believe we would have the three most important components serializable (the enote_store, key_container and transaction_history). If we could store transactions permanently (if we had a blockchain) then would be enough to save/load these components and call it a proto wallet haha.
<s​needlewoods_xmr> +1
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/930
<r​brunner7> Thanks, dangerousfreedom . Will include this in the meeting log.
<s​needlewoods_xmr> hi
<j​effro256> Howdy
<r​brunner7> So, anything to report?
<j​berman> Hello
<j​berman> Finished background sync GUI impl + some changes to the core repo PR while working on that, shared my 3/3 update on my latest CCS, my next main wallet3 task I'm working on is completing todo's in this async scanner PR: https://github.com/UkoeHB/monero/pull/23
<r​brunner7> To make it a little less "rough" then :)
<j​berman> to make it silky smooth :)
<r​brunner7> dangerousfreedom was reporting shortly before the meeting started that his enote store serialization is almost ready.
<s​needlewoods_xmr> Out of curiosity, I tested what happens if you choose 0 as spend key in the current version. Was surprised to see there are funds inside that wallet. Reached out to rbrunner, because I had no idea what to do. He told me it's a known thing and provided a reddit link. Then I spent my time on the pre seraphis code (mostly src/wallet/wallet2.cpp create_transactions_2() and related) trying to figure out if I would be able to move anything out of the wallet. Spoiler alert: I wasn't.
<r​brunner7> Yup. Anybody interested in the stories behind that can google for "abbey abbey abbey Monero" because the seed is the very first word, "abbey", just repeated 25 times
<s​needlewoods_xmr> jberman do you need testers for background sync?
<r​brunner7> For complicated functional upgrades there is no such thing as "too many testers" :)
<s​needlewoods_xmr> +1
<jeffro256> +1
<j​berman> +1^ :) reviewrs/testers always welcome
<r​brunner7> Alright. Anything in particular to discuss today?
<r​brunner7> If nothing from your side, I would like to mention the following: There is a quite lively discussion about the future of the CCS over in *Monero Community*, over the last few days and epsecially today. Ongoing right now
<r​brunner7> I mention that because we have people here more or less "living" on the CCS, so that future of the CCS is probably important and dear to them.
<r​brunner7> May do no harm to read what people discuss, and yeah, why not also chime in and have your say, from your point of view
<r​brunner7> Some of the ideas over there seem to to be a little ... out of touch with reality, frankly.
<r​brunner7> IMHO
<j​berman> I'd like to bring a discussion point up but before I do want to check my assumptions:
<j​berman> We expect that the Seraphis wallet lib will be usable before any fork/update to Monero consensus. A wallet should be able to use the Seraphis lib to scan the chain and populate an "enote store"
<j​berman> When a user wants to spend BEFORE a fork, the wallet would initialize a wallet2 instance taking as input the Seraphis lib enote store, and then construct a tx (as proposed here: https://github.com/seraphis-migration/wallet3/issues/48)
<j​effro256> That's probably the cleanest way to move forward and not have to worry as much about fingerprinting
<r​brunner7> Following you. I am still "standing at that point" today, no new revelations, no problems with the approach found in the meantime, just to confirm.
<j​berman> Ok so assuming the above is true, the Seraphis wallet lib would at minimum need to scan global output ID's keyed by amounts for pre-RingCT outputs, which it currently does not do. That would be a TODO
<r​brunner7> Doesn't tell me much, but well, you are the scanning specialist ...
<j​berman> In order to spend a pre-ringct output, the transaction you construct would need to reference that output by its global output index in the chain (which is the index it appears in the chain)
<j​berman> example: look at this tx
<j​berman> https://xmrchain.net/tx/f98b0bba24043df1579f6afbdf3e367d2371fcbb8545154026a31b5cea50ad13
<j​berman> and notice "amount idx"
<j​berman> that's following the pattern "<index> of <total number of outputs in the chain that have this exact amount>"
<r​brunner7> I see. Does this lead to some more data in those Seraphis library `legacy_transaction_x` classes, so the enote store has the info at hand if needed to pass it to any `wallet2` instance?
<j​berman> yes
<r​brunner7> Sounds doable. Do you aspire to make that library enhancement if we agree that's the way to go? If not, maybe write it down as an issue so somebody can pick it up.
<j​effro256> Shouldn't that information be covered in the legacy enote type structs?
<r​brunner7> Yes, same thought :)
<j​effro256> Well I guess thats actually "Contextual" information in the lib
<r​brunner7> I see now, yeah, it's not the legacy transaction types of course, it's the legacy enotes.
<r​brunner7> My bad
<j​berman> `enote_ledger_index`
<j​berman> that currently assumes all outputs pool into a global pool of outputs
<j​effro256> We would also need a `enote_ledger_amount
<j​effro256> Ah yes I agree
<j​effro256> I assumed there was different enote context structs for legacy enote records
<j​effro256> looking at it now, they all use `SpEnoteOriginContextV1`
<j​berman> the issue is that this doesn't differentiate the index by amount
<j​berman> the way the block explore lists "<index> of <total number of outputs in the chain that have this exact amount>", it doesn't capture that info
<j​effro256> Should we make a new origin context struct for legacy enotes (e.g. `LegacyEnoteOriginContextV1`), or add a field member to `SpEnoteOriginContextV1`?
<r​brunner7> `LegacyEnoteOriginContextV1` would be a bit funny, I really don't think we would ever need a "V2" of that :)
<j​berman> I think it could depend on how we largely intend for the Seraphis lib to treat pre-RingCT outputs, which is basically why I wanted to bring this up
<j​berman> the Seraphis lib currently implements this: https://github.com/monero-project/research-lab/issues/59
<j​berman> I think it would be helpful if we could move forward deciding how the Seraphis lib should generally treat pre-ringCT outputs
<r​brunner7> What alternatives do you see?
<j​effro256> I tend to disagree with mixing everything together during decoy selection despite the fact that there are obvious differences in how different enotes are used. These differences WILL be leveraged to do chain analysis by malicious third-parties, even if we choose to take the option of sticking our heads in the sand and pretending that these outputs are all the same
<r​brunner7> Ah, I remember now. That question is connected with spending coinbase outputs in general
<j​berman> The alternative to current Seraphis lib approach is that the Seraphis wallet lib would constrcut pre-RingCT ring signatures that are composed of outputs of the same amount, which matches wallet2/current consensus
<j​berman> I generally agree with your take jeffro
<j​effro256> If it made the protocol concensus code cleaner/easier to review and document, then I'd be fine with the consensus code treating pre-RingCT outputs the same as coinbase the same as RingCT, etc, but making the wallet code do decoy selection seperations
<j​berman> well, the consensus code as it currently exists would need to stay forever in order to verify outputs up until the change goes into effect. and this would be new changes to consensus code that separately need to be reviewed and documented in addition to what already exists
<r​brunner7> For pretty few transactions, as the analysis by Rucknium has shown.
<r​brunner7> From the department of dumb ideas: We have so large rings with Seraphis, just mix 3 or so pre-RingCT enotes into *every* ring :)
<r​brunner7> So the true pre-RingCT spend is still able to hide
<j​berman> in Seraphis these wouldn't be spent in the large rings, they would be spent in legacy CLSAG rings
<r​brunner7> Damned, I knew there is a catch
<j​berman> (in a migration tx which would then allow the newly constructed Seraphis-compatible enotes to be spent in a Seraphis ring)
<v​tnerd> dangerousfreedom: just saw your update. How is this going to clash with my serialization updates? Or does this use "cryptonote" serialization in `src/serialization` ?
<r​brunner7> I can answer that: That's all use of `binary_archive`
<v​tnerd> Ah ok, yeah the most compact
<r​brunner7> Back to that pre-RingCT question: I wonder how our decision-finding process could work, with such a specific question that from the people currently present only jberman and jeffro256 understand fully. Basically that's down to only 2 opinions ...
<r​brunner7> Quite in general, I am on the side of avoiding complexity to a large degree, but the trade-offs to judge do not seem simple in this case
<d​angerousfreedom> vtnerd: I havent fully seen your updates. I will comment here in the next days what I did but there are many things that I dont 100% agree but I was following the pattern done at seraphis_impl/serialization_demo_utils
<d​angerousfreedom> I will try to understand also if there is a better solution or not and see your updates.
<r​brunner7> Looks to me as if we should return to that pre-RingCT enotes question next week, as we run out of time for today's meeting
<j​berman> on pre-RingCT output differentiation, I actually don't think we have to make a decision here today on how exactly legacy outputs should be treated in the Seraphis upgrade. But I wanted to get wheels turning toward understanding how the Seraphis wallet lib would need to change on this front
<s​needlewoods_xmr> so with a pre-RCT enote, you would need to do one transaction to get it to current version and from there another transaction to get a seraphis enote!? That means a couple self sends will give you the full anonymity!? if that's the case and there are already very few pre-RCT enotes to begin with, I would agree on avoid complexity
<v​tnerd> If your using binary_archive, my updates don't change that.  Just epee/p2p, rpc (http and zmq). The internal format for txes and blocks is left untouched
<j​berman> in order for a wallet2 instance to be able to spend pre-RingCT outputs before a fork, I do think we should make the change in the scanner where `total_enotes_before_tx` is used to instead use the output index by amount though
<r​brunner7> That's a must if I understand the situation correctly
<j​berman> And I think a new origin context type in line with this proposal is a good idea (and agreed probably don't need a `V1` there)
<jeffro256> +1
<j​berman> It would also probably be a good task for someone new to take up ( SNeedlewoods ?) if anyone's interested
<r​brunner7> Yeah, it may take some time to read into all that big Seraphis library stuff, but on the other hand it's not ony critical time line, and nobody would depend on it for a long time, so the dev could take their time
<r​brunner7> Alright, we are past the hour. I think we can close the meeting proper here, channel stays open of course :) Thanks everybody for attending
<s​needlewoods_xmr> not sure I'm ready yet, but will definitely look into it
<jberman> +1
<s​needlewoods_xmr> thanks everyone was an insightful meeting for me
````


# Action History
- Created by: rbrunner7 | 2023-11-17T16:04:21+00:00
- Closed at: 2023-11-20T19:18:55+00:00
