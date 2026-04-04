---
title: 'Seraphis wallet workgroup meeting #8 - Monday, 2023-01-09, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/777
author: rbrunner7
assignees: []
labels: []
created_at: '2023-01-04T19:45:39+00:00'
updated_at: '2023-02-03T15:32:06+00:00'
type: issue
status: closed
closed_at: '2023-02-03T15:32:06+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #774

Workgroup member @DangerousFreedom1984 will report about his work on proofs for Seraphis.

# Discussion History
## rbrunner7 | 2023-01-09T18:56:56+00:00
````
<rbrunner7[m]1> Hello! Meeting time. https://github.com/monero-project/meta/issues/777
<rbrunner7[m]1> Who is around?
<dangerousfreedom> Hello
<jberman[m]> hello
<one-horse-wagon[> Hello.
<UkoeHB> hi
<Rucknium[m]> Hi
<rbrunner7[m]1> Today I wold like to give the stage directly to dangerousfreedom[m] because he built some interesting things, and agreed to report today.
<dangerousfreedom>
So, from my side I would like to give an update regarding my work on the knowledge_proofs.
So, my mission is to implement the equivalent for seraphis of the knowledge proofs (audit proofs) like described at chapter 8 of [ZtM2](https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf). 

So what I have done and learned so far:
- I wrote down the theoretical framework and tried to implement the proofs more or less like discussed [here](https://github.com/seraphis-migration/wallet3/issues/42).
- I have "pure" C++ [implementations](https://github.com/DangerousFreedom1984/seraphis_lib/blob/knowledge_proofs_v1/src/seraphis/tx_knowledge_proofs.cpp)
and very dirty [unit_tests](https://github.com/DangerousFreedom1984/seraphis_lib/blob/knowledge_proofs_v1/tests/unit_tests/seraphis_audit_proofs.cpp) for the
TxSpendProof, EnoteSendProof and EnoteOwnershipProof (SpendProof, OutProof, InProof equivalents in seraphis).
- Implemented the serializations/deserealizations so it should be easy for the wallet to save/load the proofs in/from files.
- I'm really thankful to Koe who is frequently answering my questions and reviewing my code. I believe that I'm getting used to the seraphis library and its writing style now.

Next tasks:
- I still have the ReserveProof and UnspentProof to implement. Though the theoretical framework was already discussed.
- Improve the unit_tests. I'm just covering the basic cases so it is not comprehensive yet.
- I believe I will be on schedule (my initial plan was to have them finished by the end of January).
<UkoeHB> it is moving in the right direction, I think the final result will work well
<rbrunner7[m]1> So whith these proofs, you extend the Seraphis library, right?
<UkoeHB> I'm a bit surprised we actually came up with proofs that work with seraphis
<rbrunner7[m]1> Hmm, I think it would have been bad with no spend proofs available "for all time"? So I guess we are lucky.
<dangerousfreedom> rbrunner7[m]: Yeah, basically I will have tx_knowledge_proofs under seraphis added if everything goes well.
<jberman[m]> Very nice dangerousfreedom[m] :)
<Rucknium[m]> +1
<rbrunner7[m]1> +1
<dangerousfreedom> I changed/added some small things too but I'm constantly talking with Koe
<rbrunner7[m]1> What are "in proofs" and "out proofs", with a few words?
<dangerousfreedom> InProofs proves that you received a enote (or that you have ownership of it). Outproofs proves that you sent an enote to an address.
<dangerousfreedom> s/a/an/
<rbrunner7[m]1> So that exists for CryptoNote, but maybe is not present e.g. as commands in the CLI? I don't remember seeing such.
<dangerousfreedom> rbrunner7[m]: Well, we would have time to implement it during testnet I guess but the seraphis library is getting really complete now :p
<dangerousfreedom> I'm just wondering how we will move with the storage on the blockchain... Right now everything is done on memory and we have not even a single demonstrator to simulate a blockchain, right?
<rbrunner7[m]1> I understood UkoeHB to make a statement about constructs possible or not possible here, but maybe I misunderstood: "I'm a bit surprised we actually came up with proofs that work with seraphis"
<UkoeHB> well I wasn't certain all the knowledge proof types would be possible with seraphis, but turns out they are
<rbrunner7[m]1> I mean, is it natural / self-evident that you can do such proofs for every protocol? Think not.
<UkoeHB> and all are much simpler than the legacy proofs actually
<rbrunner7[m]1> Splendid!
<UkoeHB> or anyway - no need for bespoke proof structures
<rbrunner7[m]1> If things become simpler that's usually a very strong indication you are on the right way.
<UkoeHB> the dualbase vector proof is bespoke, but it already exists due to multisig lol (no new bespokeness)
<rbrunner7[m]1> Isn't there some mock blockchain somewhere in there? But not stored of course.
<rbrunner7[m]1> Just a store of transactions, if I understood that right.
<dangerousfreedom> Yeah, I spent a lot of time thinking about the UnspentProof, which is an innovation compared to legacy
<UkoeHB> the mock ledger context just stores information you'd find in monerod, but no actual chain
<rbrunner7[m]1> Whatever "bespoke" means :)
<rbrunner7[m]1> Sounds good, however.
<rbrunner7[m]1> Well, sooner or later we need a connection to the daemon, to fetch blocks, and maybe that's even one of the very next things to implement.
<jberman[m]> I'm workin on that now
<rbrunner7[m]1> Maybe we could start with a simplified component that can only do that, in some still quite rigid way, in the interest of better testing?
<rbrunner7[m]1> Because I can imagine that the complete "daemon communication" stuff will have quite a healthy size already
<rbrunner7[m]1> Ah, good to hear
<jberman[m]> Well I'm working on getting the scanner functioning pointing to an actual daemon, the connection part of my code so far is in a pretty crude state/isn't clean at all/not how I imagine it would be implemented at this point. But in the starting phase of getting that glue set up
<one-horse-wagon[> Elementary question.  Is "Seraphis Libraries" just an acronym for user defined header files? 
<dangerousfreedom> Cool.
<rbrunner7[m]1> one-horse-wagon: No, that's not only header files, not by far. That's a very big library of Seraphis-related code
<UkoeHB> one-horse-wagon[: it is all the files in the directories named seraphis* under src/
<one-horse-wagon[> +1
<rbrunner7[m]1> "Crude state" does not sound bad too me. IMHO that nicely conforms with the "bottom up" approach that we agreed to follow.
<rbrunner7[m]1> Build something first in a crude way, and by doing that, learn how it must be done in a good way, the second attempt will build that
<dangerousfreedom> As soon as I finish the knowledge proofs I will move again to the opening/close wallet problem. I believe I can make a demonstrator to open a wallet, make a tx (even make a tx proof), close a wallet and re-open it again with updated amounts. I might store the transactions in a file representing a primitive ledger just to see how it looks. I dont know if the work is worth but would be cool :p
<one-horse-wagon[> rbrunner7: I got the picture.  Thank you.
<rbrunner7[m]1> I see one aspect of those proofs that we probably could discuss now: their textual representation.
<dangerousfreedom> rbrunner7[m]: You mean how they are stored in a file?
<rbrunner7[m]1> Usually there is a textual representation of such proofs, so you can move them around, e.g. mail them.
<rbrunner7[m]1> I saw that now Base58 is used, like we do for such things in the current Monero codebase.
<rbrunner7[m]1> I wonder whether we should switch to Base32, following the lead of the addresses.
<rbrunner7[m]1> And the payment requests, as they are now in the pipeline
<dangerousfreedom> Yes. I did the encoding using base58. I guess we dont really care about that. Could even be raw string since people will probably send the file with it.
<rbrunner7[m]1> And if they need a checksum, of course take the same algorithm as for the addresses as well
<dangerousfreedom> Today on monero you actually need the file to verify the proofs
<dangerousfreedom> So nobody is reading what is inside actually
<dangerousfreedom> Maybe we could change that yeah, so you could simply copy and paste
<rbrunner7[m]1> Well, a while ago a switch was added to the CLI wallet to create such files as hex, or Base58, exactly because you are not always in an environment where you can easily send files
<rbrunner7[m]1> And some things are only text given out to console, I think
<rbrunner7[m]1> (Right now, in the CLI)
<dangerousfreedom> Good point.
<rbrunner7[m]1> But anyway, if we want text, maybe we standardize? What do people think?
<rbrunner7[m]1> Take the "standard" as given by the Jamtis addresses.
<dangerousfreedom> I'm using the character '/' to separate the info. If we strictly assume that we have to have base58 then I would have to change that
<rbrunner7[m]1> Ah, right now you simply concatenate things, and use "/" as a delimiter?
<dangerousfreedom> Oh I think it does not matter, any pc can recognize this character I guess :p
<Rucknium[m]> Pretty sure we want some sort of ASCII form for these proofs
<dangerousfreedom> rbrunner7[m]: More or less. Since the proofs change in size I also store their size with this delimiter
<rbrunner7[m]1> Hmm, ok. I think if you want to checksum them, what is probably a good idea, I think you have to stick to Base32. And also to get the small QR codes.
<UkoeHB> I think raw bytes doesn't work when handling them in python (at least I had that problem when updating multisig)
<rbrunner7[m]1> So you would have to work with lengths stored somehow
<rbrunner7[m]1> explicitely
<rbrunner7[m]1> But anyway, does anybody see a reason against following the lead of the Jamtis addresses and leave Base58 behind also here?
<UkoeHB> what's the advantage?
<dangerousfreedom> rbrunner7[m]: I dont know if we want a checksum. Maybe something simple like a hash but not the one that will be used for the addresses. The proofs can vary in size from 100 to 10k characters in size. I dont know the advantage of using it for this big range.
<rbrunner7[m]1> The same as with the addresses, I would say, the checksum-ability and the smaller QR codes.
<rbrunner7[m]1> Plus some standardization
<rbrunner7[m]1> Have some examples for big proofs? Just curious. That sounds surprising.
<dangerousfreedom> rbrunner7[m]: I made a tx_spend_proof with 60+ transactions and it was pretty big :p
<rbrunner7[m]1> Nice, but not something people will probably do every day :)
<rbrunner7[m]1> Ok, we are not in a hurry, we can come back to that in some time. Maybe I document that in an issue.
<rbrunner7[m]1> Alright, do we have some other subjects for today, that somebody would like to discuss?
<dangerousfreedom> dangerousfreedom: I mean one transaction with 60+ enotes. One proof has ~600 characters so you can have 36k characters in the proof.
<rbrunner7[m]1> Ah, ok, understood. That can happen of course.
<one-horse-wagon[> I think the project is moving steadily along.  No big snags or gotcha's so far.
<rbrunner7[m]1> Looks like this, yeah. I am glad to see first code being built.
<dangerousfreedom> From my side yeah, but Koe already did a huge and clean job. I think it will be much easier to implement the wallet than if we were working with the current legacy protocol.<rbrunner7[m]1> Eventually we will get there :)
<rbrunner7[m]1> So I close the formal meeting. Thanks for the report, dangerousfreedom[m] , and thanks everybody for attending!
````


# Action History
- Created by: rbrunner7 | 2023-01-04T19:45:39+00:00
- Closed at: 2023-02-03T15:32:06+00:00
