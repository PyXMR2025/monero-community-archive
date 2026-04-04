---
title: 'Seraphis wallet workgroup meeting #45 - Monday, 2023-11-13, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/927
author: rbrunner7
assignees: []
labels: []
created_at: '2023-11-10T20:56:59+00:00'
updated_at: '2023-11-13T18:47:46+00:00'
type: issue
status: closed
closed_at: '2023-11-13T18:47:46+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/918

# Discussion History
## rbrunner7 | 2023-11-13T18:47:46+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/927
<j​effro256> Hello!
<d​angerousfreedom> Hello
<s​needlewoods_xmr> hey
<j​berman> howdy
<r​brunner7> So, straight to the reports: What happened during the last week?
<d​angerousfreedom> From my side I made some comments to ghostway  key_container PR and I tried to talk to shalit  but wont successful. So I took over the serialization of the enote_store and I will probably have something to show by next week.
<r​brunner7> dangerousfreedom: Sounds good to me
<j​berman> I commented on dynamic view tags / auxiliary enotes on the jamtis proposal, and have been working mostly on background sync the past week (some debugging + the GUI implementation). Expecting GUI background sync implementation + debugging to take me most of this next week
<r​brunner7> What's the work in the GUI? Mostly views and controls to drive background synch?
<j​berman> ya, it's simple
<r​ucknium> On next Monero Research Lab meeting agenda (Wednesday at 17:00 UTC in #monero-research-lab ) will be how to move Monero's multisig from experimental to production-ready. It may involve writing security proofs for the current multisig implementation, exploring kayabaNerve's multisig implementation, or any ideas. Please come if you are interested in multisig.
<dangerousfreedom> +1
<jeffro256> +1
<jberman> +1
<tobtoht> +1
<SNeedlewoods> +1
<r​brunner7> Thanks for the pointer, Rucknium
<r​brunner7> dangerousfreedom: Do you currently intend to do *any* further work on the transaction type issue on your own? Maybe some experiments with the compiler, and regarding C++, that won't bite and won't go astray?
<r​brunner7> Could be groundwork for whoever will finally make a breakthrough there
<r​brunner7> Maybe jeffro256 will bring some ideas to the table on Wednesday :)
<r​brunner7> ghostway mentioned before the meeting that they are working on their 2 PRs. Would be good to be able to merge the simpler one for the encrypted file, to start the `seraphis_wallet`
<r​brunner7> (folder and library)
<s​needlewoods_xmr> not sure if worth mentioning, but I spent the most time setting up a dev environment, read through "Implementing Seraphis" (haven't studied it), then read through parts of the seraphis_lib and made a local branch to test some very basic stuff on
<jeffro256> +1
<rbrunner7> +1
<dangerousfreedom> +1
<jberman> +1
<r​brunner7> SNeedlewoods: If you have question, don't be shy to drop them here :) Any day, any hour
<SNeedlewoods> +1
<j​effro256> Yes I plan to review that soon. Which password hasher are we using again?
<r​brunner7> The one we use for years? I would say let's start with *something* and discuss and improve later ...
<d​angerousfreedom> By doing the serialization of the enote_store I was stuck with the problem of serializing a variant. I intend to solve that and then I think that could lead to a better understanding on how to solve the transaction types issue (at least give some clues)
<r​brunner7> Haha, so the problem sneaked up on you from an unexpected direction :)
<j​effro256> Which serialization format are you using?
<j​effro256> Because you might need to specify variant tags
<d​angerousfreedom> I guess jeffro commented on that last week. I'm just using the boost library (archive). I'm calling the BEGIN_SERIALIZE_OBJECT() ... END_SERIALIZE(). We can do conditionals inside it. So thats the plan now
<d​angerousfreedom> Yeah the use of variants is more pronounced with seraphis. So we need to find a way to properly serialize them
<j​effro256> Well that serialization format actually automatically can serialize variants if you supply variant tags
<r​brunner7> Well, that's not Boost, that's "our" `binary_archive`. Anything Boost would be inappropriate.
<j​effro256> https://github.com/monero-project/monero/blob/ac02af92867590ca80b2779a7bbeafa99ff94dcb/src/cryptonote_basic/cryptonote_basic.h#L572-L603
<j​effro256> Here's how to make variant tags. Then you can just use `FIELD()` etc as normal
<j​effro256> No custom node needed
<j​effro256> *code
<r​brunner7> Yeah, the standard `crytonote::transaction` has a variant somewhere in it that jberman had to extend for the viewtags, adding a variant
<d​angerousfreedom> Thanks jeffro256 !
<j​effro256> ofc
<j​effro256> One problem with variant tags like this is that the variant tag for a type has to be the same across all variants
<j​effro256> (for a given type of archive)
<j​effro256> But as long as you don't have that problem then you're good
<r​brunner7> Alright. Do we have something in particular to discuss today?
<d​angerousfreedom> Ok, I will try to use it during the week and ask you if I have problems. Thanks :)
<r​brunner7> Doesn't look like it. So I would say we are complete for today. Thanks for attending everybody, read you next week!
<s​needlewoods_xmr> thanks rbrunner
<j​effro256> Indeed thanks rbrunner
````


# Action History
- Created by: rbrunner7 | 2023-11-10T20:56:59+00:00
- Closed at: 2023-11-13T18:47:46+00:00
