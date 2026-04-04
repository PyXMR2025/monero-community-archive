---
title: 'Seraphis wallet workgroup meeting #23 - Monday, 2023-05-22, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/840
author: rbrunner7
assignees: []
labels: []
created_at: '2023-05-20T16:44:13+00:00'
updated_at: '2023-05-22T18:54:03+00:00'
type: issue
status: closed
closed_at: '2023-05-22T18:54:03+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #836

# Discussion History
## rbrunner7 | 2023-05-22T18:54:03+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/840
<shalit[m]> Hello!
<dangerousfreedom> Hi
<Rucknium[m]> waves
<plowsof> waves
<UkoeHB> Hi
<jberman[m]> hello
<rbrunner7[m]> Very quiet week, at least as far as activity in this Matrix room is concerned :) Something to report nevertheless?
<rbrunner7[m]> I remember what I wanted to do last week, but forgot: Merge UkoeHB 's latest code into our own repository fork
<rbrunner7[m]> The squashed version of the code, as I understand
<xmrack[m]> Hi
<dangerousfreedom> This week I have basically worked on the [serialization](https://github.com/DangerousFreedom1984/seraphis_lib/tree/keys_load/src/seraphis_wallet) of my structs (I can save/load to/from an encrypted file the data of the tx_history). After briefly discussing with @ghostway about [saving/loading](https://github.com/monero-project/monero/compare/master...ghostway0:monero:local-data-file) a wallet with the master keys, we
<dangerousfreedom> are a hopefully getting to a minimum design for that. 
<ghostway[m]> Hello
<dangerousfreedom> I have also created some [unit_tests](https://github.com/DangerousFreedom1984/seraphis_lib/blob/keys_load/tests/unit_tests/sp_wallet_tx_history.cpp)
<ghostway[m]> I'm probably getting up to speed this week somewhere 
<dangerousfreedom> I have some questions that may block me or alter my workflow:
<dangerousfreedom> 1) Since the wallet will be very dependent on the EnoteStore, how do you plan to load/save the EnoteStore when the wallet is opened? You will certainly need to serialize the member variables of the SpEnoteStore class, right? Have you done already any work on that?
<dangerousfreedom> 2) Do you think that the serialization done in seraphis_impl/serialization_demo_utils is appropriate and it should be the way to go for all structs of the wallet?
<ghostway[m]> dangerousfreedom[m]: Heh, that's the wrong commit/branch. I haven't pushed it yet iirc
<rbrunner7[m]> dangerousfreedom[m]: Is anything of that far enough that having a look and commenting makes sense already?
<dangerousfreedom> ghostway[m]: > <@ghostway[m]:libera.chat> > <@dangerousfreedom[m]:libera.chat> This week I have basically worked on the [serialization](https://github.com/DangerousFreedom1984/seraphis_lib/tree/keys_load/src/seraphis_wallet) of my structs (I can save/load to/from an encrypted file the data of the tx_history). After briefly discussing with @ghostway about [saving/loading](https://github.com/monero-project/monero/compare/master...ghostway0:monero:local-data-file) a wallet with the master keys, we are a hopefully getting to a minimum design for that.
<ghostway[m]> Heh, that's the wrong commit/branch. I haven't pushed it yet iirc
<dangerousfreedom> Haha okay. I just modified a bit what you did and the idea is to get some feedback to continue
<dangerousfreedom> rbrunner7[m]: Maybe we could briefly discuss the approach of the serialization of the master keys.
<rbrunner7[m]> After having a look at the `EnoteStore` class myself, I was wondering as well how and when to serialize that. Maybe UkoeHB can comment?
<rbrunner7[m]> What are the "master keys" here?
<dangerousfreedom> rbrunner7[m]: Here is a very simple way to do it: https://github.com/DangerousFreedom1984/seraphis_lib/blob/keys_load/tests/unit_tests/sp_wallet_encrypt_keys.cpp
<ghostway[m]> Jamtis_mock_keys struct I imagine
<dangerousfreedom> Would something like be the way to go or is there something radically wrong?
<dangerousfreedom> * something like that be the
<ghostway[m]> Question, why do we try to encrypt the keys? When you don't trust your own memory, then you also don't trust the other things in memory (aka, the key that encrypted it)
<rbrunner7[m]> You mean quite in general how the wallet content / file will get protected by encrypting it?
<ghostway[m]> Not the file, while in memory 
<UkoeHB> The enote store should not be serialized directly. The contents should be exported then reimported with the existing methods so that invariants are preserved.
<rbrunner7[m]> Are you and dangerousfreedom[m] really talking about the same thing here?
<UkoeHB> It may need some minor updates to improve the export interface
<ghostway[m]> rbrunner7[m]: Nope
<rbrunner7[m]> Did anybody try to get an overview what wallet2 currently does, so we can compare, find out where there is a need to improve, and similar?
<rbrunner7[m]> In regard to encrypting the various things
<ghostway[m]> In what regard?
<ghostway[m]> Ah 
<dangerousfreedom> UkoeHB: I didnt understand. How can you export or import without serializing? Are there methods for doing these imports/exports already?
<rbrunner7[m]> I think the aim of decrypting keys when needed and re-encrypting them, and making sure memory is wiped when freed, is to lower the chance that a debugger sees something, and things end up in swap files. Obviously you can't fully prevent that.
<UkoeHB> No, export the contents in c++ then serialize
<UkoeHB> Don’t serialize/deserialize directly in the enote store
<rbrunner7[m]> So for example take the simple array / list of enotes and write that to file? And probably some additional bits and pieces as well?
<rbrunner7[m]> (Assuming there is such an array in EnoteStore ...)
<UkoeHB> Yes something like that
<rbrunner7[m]> Maybe not trivial to find out exactly what needs to survice a write - load cycle, the class is quite complex. Maybe jberman has already quite a good overview here?
<UkoeHB> Just need to look at the existing import interface
<rbrunner7[m]> I guess you don't save a wallet in the middle of a sync process and expect to continue just like that after re-open, right? :)
<dangerousfreedom> <UkoeHB> "No, export the contents in c..." <- Ok. But how the wallet (or engine or something) will load the SpEnoteStore? Do you see it as part of the wallet?  
<rbrunner7[m]> Maybe now the harder parts of the work start, where sometimes nothing except having "total" understanding before coding can continue 
<rbrunner7[m]> helps
<Rucknium[m]> There is a paper about Monero info in RAM: Koerhuis, W., Kechadi, T., & Le-Khac, N.-A. (2020). "Forensic analysis of privacy-oriented cryptocurrencies." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=109&browserTabID=
<dangerousfreedom> I always need to use the variable     std::unordered_map<crypto::key_image, SpContextualEnoteRecordV1> m_sp_contextual_enote_records;
<dangerousfreedom> that is in the EnoteStore and I am always wondering how it will be updated and how precise are the information that I get from there
<Rucknium[m]> "In this paper, we address the privacy-oriented cryptocurrencies Monero and Verge and investigate which valuable forensic artefacts the software of these cryptocurrencies leaves behind on a computer system. We examine different sources of potential evidence like the volatile memory, network traffic and hard disks of the system running the cryptocurrency software. In almost all sources of evidence there are valuable forensic
<Rucknium[m]> artefacts. These artefacts vary from mnemonic seed phrases and plain text passphrases in the volatile memory to indicators of the use of a cryptocurrency in the captured network traffic."
<rbrunner7[m]> Rucknium: Amazing, there seem to be papers about almost anything
<rbrunner7[m]> dangerousfreedom[m]: Yeah, that's what I meant. Maybe you have to understand that store before your work can meaningfully continue. Of course try to get help where ever you can on this journey.
<UkoeHB> dangerousfreedom: the information is as precise as your latest scan
<dangerousfreedom> Yes I see. And how do you load the component?
<UkoeHB> I do think the enote store needs to be refactored a bit to provide a better information access interface with O(1) lookups.
<UkoeHB> it's loaded with the scanning framework
<dangerousfreedom> You are not scanning the blockchain everytime you open the wallet, right?
<UkoeHB> obviously not
<rbrunner7[m]> Only from the last point reached ... of course?
<dangerousfreedom> Yes, of course, so how would that be done? Is there something done in this sense?
<UkoeHB> there are no demos of reloading from a save yet
<rbrunner7[m]> So as already mentioned store the enotes themselves somehow, not the whole enote store object. And some other important things that you will need to re-create a proper working enote store the next time you open the wallet
<rbrunner7[m]> Ready to continue sync from the last height reached, to update
<dangerousfreedom> Okay.
<rbrunner7[m]> Maybe you search too far, or we are talking past each other now ...
<rbrunner7[m]> I guess this will keep you busy for quite a while :)
<dangerousfreedom> My 'problem' is that I'm relying very much on the EnoteStore and I'm not confident of all its capabilities yet :p
<rbrunner7[m]> But then an important step forward will be reached if you get that to work
<rbrunner7[m]> Put a printout under the pillow. Will come to you in sleep.
<dangerousfreedom> Okay. Thanks.
<ghostway[m]> <Rucknium[m]> "There is a paper about Monero..." <- Did you mean to answer my question?
<rbrunner7[m]> If you really meant what happens in RAM, probably?
<Rucknium[m]> ghostway: It's not a complete answer, but it can give more info.
<rbrunner7[m]> Anyway, if you tell the CLI wallet to only decrypt as needed, with every received enote you find yourself typing the password again. Gets very annoying very fast, IMHO.
<rbrunner7[m]> People looking over your shoulder will thank you for the many chances to watch you typing the password
<jberman[m]> <rbrunner7[m]> "I guess you don't save a..." <- Yea, rbrunner7  the goal generally with encrypting in memory does seem to reduce the the surface area for key extraction. Secret keys are wrapped with `mlock` to make sure key material isn't placed in swap on disk, and also wrapped with a wipeable that zeroes out the variable when it exits scope
<jberman[m]> When the spend key is encrypted in memory in wallet2, in theory there shouldn't be anything else in memory that enables you to recover the spend key by default I don't think. But apparently seems there are missing gaps as noted in that paper. I'm thinking that's a GUI thing and not the CLI, but it could probably use another deep look. IIRC with the GUI you don't have to decrypt the spend key when you're using the wallet by
<jberman[m]> default like you do with the CLI, which means it's known that it's accessible
<UkoeHB> rbrunner7[m]: the mlocked wrapper used in crypto secret keys prevents swapping to disk
<rbrunner7[m]> Alright
<rbrunner7[m]> Looks like we will have to copy that, because a downgrade in security does not sound appealing ...
<rbrunner7[m]> But maybe not in our first experimental versions of the wallet?
<rbrunner7[m]> So more work can go into finding out the overall structure that the wallet modules will sensibly have
<rbrunner7[m]> Like what we discussed today about the enote store and storing lists of enotes into file
<UkoeHB> there is nothing very complex to copy, just write hygienic code
<rbrunner7[m]> Any loose ends to discuss while we are still here? Or can detailed discussions continue in the coming days between people that are directly involved?
<dangerousfreedom> Yeah, the keys are in the mock version yet. I'm more worried about the structure and how the files will be divided than about storing it properly as we are not storing much things now :p
<dangerousfreedom> rbrunner7[m]: Not from me. But maybe I will ask some stuff to @koe and @ghostway during the week
<rbrunner7[m]> Right. Use this room, it feels a bit underworked right now :)
<rbrunner7[m]> Or, as already discussed in earlier meetings, open issues and discuss there, so that it's more focussed thematically
<rbrunner7[m]> Alright, let's call it here, thanks for attending!
````


# Action History
- Created by: rbrunner7 | 2023-05-20T16:44:13+00:00
- Closed at: 2023-05-22T18:54:03+00:00
