---
title: 'Seraphis wallet workgroup meeting #29 - Monday, 2023-07-10, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/861
author: rbrunner7
assignees: []
labels: []
created_at: '2023-07-07T14:19:40+00:00'
updated_at: '2023-07-10T19:27:21+00:00'
type: issue
status: closed
closed_at: '2023-07-10T19:27:21+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #856

# Discussion History
## rbrunner7 | 2023-07-10T19:27:21+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/861
<Rucknium[m]> waves
<dangerousfreedom> Hello
<jberman[m]> hello
<rbrunner7[m]> Nice, not yet everybody on holidays :)
<rbrunner7[m]> Anything to report from last week?
<rbrunner7[m]> Nothing from my side
<dangerousfreedom> This week I added the generation/verification of the [legacy](https://github.com/seraphis-migration/monero/pull/1/files#diff-9e6c50722c8e5ced0bcd9bc0d411909b611b7623269c3dbb03b2efa62377b2f3R57) spend_proofs and in_proofs. I'm using jberman[m]  [scanner](https://github.com/DangerousFreedom1984/seraphis_lib/commit/c727f099b3de4f8fd66d593709a84b7c8aefdba4#diff-781b2dd1ee233adedc4ed7a70c7bfa58004381038de03b7e561bf4d027b65607R465) as a way to test it since these proofs require a node connection.
For the OutProof I don't have a solution yet since the tx_priv_key is stored in the wallet2 files and one needs to recover it in order to be able to reproduce these proofs. Maybe there is an easy way to recover it using jeffro256[m]  api for the wallet2?
I still have to solve the problem about how the node connection will look like (but we also dont know it) so for now it is working on a local node as a temporary solution. 
I will go through a surgery on my arm this week and will stay the next three weeks without touching a keyboard.
Meanwhile, I will prepare my TODO list for finishing the sp generate proofs and think about how could I simulate a node (or create one) to efficiently test these proofs as if they were in the wallet.
<rbrunner7[m]> Good look for your surgery then, take care. We need you back as a dev!
<rbrunner7[m]> Moving private tx keys between wallets would be job for the tool I dream about here: https://github.com/seraphis-migration/wallet3/issues/39
<jberman[m]> dangerousfreedom[m]: is `getTxKey` what you're looking for?
<rbrunner7[m]> ghostway  worked a bit on that one. Not sure where they stand with it.
<jberman[m]> https://github.com/monero-project/monero/blob/00fd416a99686f0956361d1cd0337fe56e58d4a7/src/wallet/api/wallet.cpp#L1791
<rbrunner7[m]> I guess the question is how to get that if you are running in a Seraphis context, with a Seraphis wallet underneath
<jberman[m]> First pass glance this looks solid dangerousfreedom[m] nice job
<shalit[m]> Hello
<jberman[m]> me: no update on no-wallet-left-behind work since last week; about to finish final updates to wallet2's background sync feature (PR 8619), same for monero-serai work, then moving primary work back over to no-wallet-left-behind + hoping to put out a new CCS
<dangerousfreedom> <rbrunner7[m]> "Good look for your surgery then,..." <- Thank you!
<ghostway[m]> rbrunner7[m]: I think I sent jberman something but not sure
<ghostway[m]> Good luck with your surgery
<dangerousfreedom> jberman[m]: Yes but the thing is that information is only saved at the wallet 2 files. We would need a way to transfer not only the private keys but also some other info like the transaction keys...
<ghostway[m]> Im pretty much done with the key container, just need to write tests that don't suck :)
<rbrunner7[m]> "My" tool would be able to do exactly that. You would do it beforehand, so you have all necessary info right there in the Seraphis wallet.
<rbrunner7[m]> *run it beforehand
<rbrunner7[m]> It would be a "transfer info from one wallet file into another one" tool
<dangerousfreedom> jberman[m]: Thanks for the scanner! I could finally test the spend proofs and inproofs. I'm building the minimum stuff that we will need from wallet2. https://github.com/DangerousFreedom1984/seraphis_lib/blob/tx_proofs_with_scanner/src/blockchain_utilities/blockchain_scanner.cpp#L465
<rbrunner7[m]> Most and foremost "private" info of course that you can't recover from the blockchain itself, like those keys. Or destination addresses.
<rbrunner7[m]> So it seems that we will get indeed a summer break, as far as Seraphis wallet related work in concerned. UkoeHB also is away from any Monero work for 2 months, if I got that correctly.
<jberman[m]> > Meanwhile, I will prepare my TODO list for finishing the sp generate proofs and think about how could I simulate a node (or create one) to efficiently test these proofs as if they were in the wallet.
<jberman[m]> UkoeHB's model for unit tests seems like an effective way to get these across the finish line for now (mock the node responses). have you done something like that? sorry if I missed it
<rbrunner7[m]> Yeah, I think he even mocks chain reorgs somewhere in there ...
<jberman[m]> yep
<dangerousfreedom> jberman[m]: I'm not aware yet how I can fully test the verification proofs (or anything that needs a connection to a node).
<rbrunner7[m]> You simulate the node! Like in the Matrix :)
<rbrunner7[m]> At least in principle. It might not be trivial in actual detail.
<dangerousfreedom> Are there unit_tests mimicking an extraction of a tx from the node for example?
<jberman[m]> kind of. get_onchain_chunk for example when scanning (might have a diff name). in your case you can have a test where you do all the set-up for the test (which includes your initial tx creation) at the beginning, and then you pass in a nested function that mocks the request to the daemon and retrieves that tx. like get
<jberman[m]> finding a line to show
<rbrunner7[m]> Basically you create first a tx that you later want to "retrieve" from the blockchain?
<jberman[m]> right
<rbrunner7[m]> Such an approach will test a large number of other things as a nice side-effect, like exactly tx construction :)
<jberman[m]> ya basically just search get_onchain_chunk in the code and follow it around
<jberman[m]> take this test for example: https://github.com/UkoeHB/monero/blob/fb3068016380f38aeb9c38d13ced43de57b06a1a/tests/unit_tests/seraphis_enote_scanning.cpp#L246
<jberman[m]> it adds an enote to a mock ledger, and then scans it later on with a nested call that reads it from the mock ledger
<jberman[m]> adds the tx to the mock chain here: https://github.com/UkoeHB/monero/blob/fb3068016380f38aeb9c38d13ced43de57b06a1a/tests/unit_tests/seraphis_enote_scanning.cpp#L282C1-L287C26
<rbrunner7[m]> Sounds cool.
<rbrunner7[m]> Who says that unit tests have to be "low level"
<dangerousfreedom> Oh okay. I see. Thanks. This is the closest thing to the function "epee::net_utils::invoke_http_json("/gettransactions", req, res, http_client)", right?
<jberman[m]> in that example it's closer to /getblocks.bin
<jberman[m]> and then a large portion of my scanning work was actually converting the response from /getblocks.bin to a format the wallet lib could understand fwiw
<rbrunner7[m]> In a way, it's not that important where exactly your tests get their txs from. That they get any at all, and can process them, is important. Sooner or later there will be a daemon, with easy ways to connect to it.
<rbrunner7[m]> No need to somehow "prove" that now, seems to me.
<jberman[m]> I'd say it would be good to try to model it around a mock /gettransactions response from the mock ledger to minimize the work involved later on if possible too, but ya daemon connection not absolutely necessary to move forward on it
<rbrunner7[m]> Alright. Anything else for this meeting here?
<dangerousfreedom> Yeah, for now I have some temporary code for the connection. But the most accurate I get, the less I need to change later.
<dangerousfreedom> Not from my side
<jberman[m]> on daemon connection work: the next thing I was hoping to get to on this front (or if someone else wants to take it up) was working with a new http client lib like libcurl in the scanner implementation. I still think jeffro256  's idea there had a lot of merit and shouldn't be too much effort
<rbrunner7[m]> Didn't he want to come up with an estimate?
<rbrunner7[m]> Between two surf sessions, maybe :)
<jberman[m]> ghostway check out jeffro256's PR here to export the wallet2 wallet files: https://github.com/monero-project/monero/pull/8923
<rbrunner7[m]> Er... isn't it reading wallet2 files, not exporting them?
<jberman[m]> ya true, reading*
<ghostway[m]> Oh, so basically what you wanted to do. I can give them the jamtis converter 
<ghostway[m]> With factoring out wallet2
<rbrunner7[m]> Let's close the meeting proper. Thanks for attending, read some of you again next week.
<jberman[m]> ty
<dangerousfreedom> Thank you
````


# Action History
- Created by: rbrunner7 | 2023-07-07T14:19:40+00:00
- Closed at: 2023-07-10T19:27:21+00:00
