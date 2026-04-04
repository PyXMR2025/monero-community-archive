---
title: 'Seraphis wallet workgroup meeting #32 - Monday, 2023-08-14, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/877
author: rbrunner7
assignees: []
labels: []
created_at: '2023-08-11T19:21:14+00:00'
updated_at: '2023-08-14T18:26:04+00:00'
type: issue
status: closed
closed_at: '2023-08-14T18:26:04+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/874

# Discussion History
## rbrunner7 | 2023-08-14T18:26:04+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/877
<d​angerousfreedom> Hi
<a​ck-j> Hi
<j​berman> hello
<v​alldrac> Hi
<r​brunner7> So there, anything to report from last week?
<d​angerousfreedom> I would like to give an update about my [CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377) as I believe I can see a clear path to its end now (probably by the end of September) but still have a lot to do..
<d​angerousfreedom> Briefly, what I have done so far:
<d​angerousfreedom> - Created the Transaction History class (maybe it should not be a class but a struct) to store the info (PaymentProposals) of authored txs. (WIP)
<d​angerousfreedom> - Created functions to verify/write from/to a file/string the sp_knowledge_proofs (WIP)
<d​angerousfreedom> - Got the minimal functions to generate/verify the legacy knowledge proofs and integrate them in the enotes style (WIP)
<d​angerousfreedom> - Created a similar function to simple_wallet::get_transfers to show the enotes (instead of transfers) and to export it (WIP)
<d​angerousfreedom> What I need to do:
<d​angerousfreedom> - legacy proofs: (https://github.com/DangerousFreedom1984/seraphis_lib/blob/initial_tx_history/src/seraphis_wallet/legacy_knowledge_proofs.cpp)
<d​angerousfreedom>     - tx_out_proof (how to recover tx key)? use jeffro wallet2 api?
<d​angerousfreedom>     - implement minimal reserve proofs
<d​angerousfreedom> - sp proofs: (https://github.com/DangerousFreedom1984/seraphis_lib/blob/initial_tx_history/src/seraphis_wallet/transaction_history.cpp)
<d​angerousfreedom>     - clean up
<d​angerousfreedom>     - add more unit tests and comments
<d​angerousfreedom> - show/export in/out ENOTES (https://github.com/DangerousFreedom1984/seraphis_lib/blob/initial_tx_history/src/seraphis_wallet/show_enotes.cpp)
<d​angerousfreedom>     - add unit_tests to show enotes by case when possible (in/out/all/pending/failed/pool/coinbase) and filtering by height (min/max)
<d​angerousfreedom>     - make sure one can get all info he needs to produce the knowledge proofs (for example ephemeral priv key)
<d​angerousfreedom>     - add legacy enotes
<d​angerousfreedom>     - create import/export functions
<r​brunner7> Wow, that's a lot in the pipeline.
<r​brunner7> Looks like work :)
<d​angerousfreedom> Well, I can see more or less the final shape so I'm less afraid now
<d​angerousfreedom> So I will probably ask for revisions and feedback in about a month
<r​brunner7> Does something want to discuss something in particular today? I have nothing from my side.
<r​brunner7> *Does somebody
<r​brunner7> There was a discussion today in this room and channel about the block cipher to use for the Jamtis view tag, but that's a pretty small corner ...
<r​brunner7> TwoFish compared with AES, hopefully hardware-accelerated
<r​brunner7> So looks like we are through already, thanks for attending, read you next week at the latest!
<d​angerousfreedom> No, nothing else from my side
<v​alldrac> I'll summarize it and send a pull-request, but I'm not sure where the repository is
<j​berman> sorry for delay.. update on my end: I implemented a basic http connection pool to enable cleaner concurrent http requests with the epee client: https://github.com/j-berman/monero/commit/0562fa8590389472539a5fb20054d70fe5c33565#diff-781b2dd1ee233adedc4ed7a70c7bfa58004381038de03b7e561bf4d027b65607
<j​berman> (as per this issue discussing concurrent network requests: https://github.com/seraphis-migration/wallet3/issues/58)
<j​berman> An interesting implementation note: I abstracted the RPC request to fetch blocks from the daemon such that a dev using the scanner can pass in their own network client gadget to handle network requests: https://github.com/j-berman/monero/blob/0562fa8590389472539a5fb20054d70fe5c33565/src/blockchain_utilities/blockchain_scanner.cpp#L202-L241
<r​brunner7> valldrac: https://github.com/UkoeHB/monero/tree/seraphis_lib
<j​berman> You basically just pass in a function to the "enote finder" that takes in the RPC request as a param and returns the RPC response. So the internal scanner doesn't care about how the client handles the network request, only that the function gets the response
<r​brunner7> Cool, isn't that called *dependency injection* or something?
<r​brunner7> Or at least the same core idea
<j​berman> that seems an accurate description
<r​brunner7> Alright, seems the time is near where Seraphis dev work starts to produce the first "real" code, i.e. code that might end up in the final hardfork to Seraphis code
<r​brunner7> A good time, in November it will be one year we meet here :)
<r​brunner7> Ok, seems that now we have all the reports. Thanks again.
<v​alldrac> Awesome, and very useful for my SDK. Thank you!
````


# Action History
- Created by: rbrunner7 | 2023-08-11T19:21:14+00:00
- Closed at: 2023-08-14T18:26:04+00:00
