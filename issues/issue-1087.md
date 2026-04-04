---
title: 'Monero Tech Meeting #90 - Monday, 2024-10-07, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1087
author: rbrunner7
assignees: []
labels: []
created_at: '2024-10-04T18:24:51+00:00'
updated_at: '2024-10-07T19:38:34+00:00'
type: issue
status: closed
closed_at: '2024-10-07T19:38:34+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1084).


# Discussion History
## rbrunner7 | 2024-10-07T19:38:34+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1087
<s​needlewoods> hey
<j​berman> *waves*
<r​brunner7> Well, let's see whether more people join in the next minutes. I think we can already start with the reports about last week
<s​yntheticbird> hello
<s​needlewoods> Fixed some compiler errors on the API PR, proposed a CCS (see last couple messages before the meeting) and I moved EnoteDetails to separate files for consistency, just about to push latest changes.
<r​brunner7> That will be a good point to do reviewing again?
<j​effro256> howdy
<j​berman> me: nearly completed a modular TreeSync class to sync the tree locally and update received output paths with minimal data saved + handle reorgs. While testing reorg handling I found an edge case bug in my trim_tree impl that I'm still working through
<r​brunner7> For the protocol, this is the CCS proposal in question: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/508
<s​needlewoods> Maybe, but there are still a couple things that need to be done before I'd call it complete
<r​brunner7> Ok
<r​brunner7> jberman: Sounds like some kind of milestone
<r​brunner7> I guess we will hear more about jeffro256 's Carrot review adventures in Wednesday's MRL meeting :)
<j​berman> not yet, next week likely yes
<j​effro256> Yes I think we should make a decision this Wednesday
<r​brunner7> Carrot is slowling working its way into community "conciousness", by the way, judging from the number of mentions on Reddit
<r​brunner7> *slowly
<s​needlewoods> Here is one of the things I still have the most struggle with: https://github.com/monero-project/monero/blob/e0c08ca628d6c83e519f038ca09b71da753b56d3/src/wallet/api/wallet2_api.h#L1360 
<s​needlewoods> I can try to explain more, but will take a minute
<j​effro256> Yeah I've received a lot of good questions about it, so that's nice to see. I think some people are confused as to how FCMP++ and Carrot play together, as some think Carrot *replaces* FCMP++. This is probably due to the fact that the current addressing scheme isn't named nor documented AFAIK
<r​brunner7> You mean the bog-standard, 10 years old CryptoNote addressing scheme?
<r​brunner7> (Well, a few years less for subaddresses)
<j​effro256> Well yeah Monero uses that, as well as the subaddressing ephemeral pubkey scheme, plus the way amount commitment blinding factors are transmitted, plus how amounts are encypted
<r​brunner7> When the question came up "Will the current address format stay with Carrot" I confess I wasn't sure about the answer as well, the Carrot spec could be clearer on that ...
<r​brunner7> I mean regarding UI/UX: 95 Base58 encoded characters
<j​effro256> Yes the current format will stay exactly as-is
<j​effro256> They will be computationally indistinguishable from previous addresses
<jbabb:cypherstack.com> +1
<r​brunner7> Downright boring, man
<j​effro256> lmao
<r​brunner7> Wallet app writers will surely thank you for that
<jbabb:cypherstack.com> +1
<r​brunner7> SNeedlewoods: It's about those "accept functions"? Never noticed them so far
<j​effro256> SNeedlewoods: I will take a look at `accept_func` rq
<r​brunner7> Ah, "real quick". Learned something.
<s​needlewoods> This is a quote from a previous meeting "I wanted to propose to remove these "accept functions" from the function parameters (as e.g. [here](https://github.com/monero-project/monero/blob/3d890fd0859b8e7992f917ebdfda270af7f16ffd/src/wallet/api/wallet2_api.h#L1354-L1362) used by the wallet-cli [here](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/simplewallet/simplewallet.cpp#L7850)) and "offload" this job to simplewallet as its done [here](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/simplewallet/simplewallet.cpp#L2316-L2335), where the accept function gets applied after the wallet2 call `m_wallet->cold_sign_tx(...)`, but then I realized not all of them are optional in wallet2 (e.g. [here](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/wallet/wallet2.h#L1200-L1201)). Should I still continue with the approach where the parameter is optional, as I did in [this commit](https://github.com/monero-project/monero/pull/9464/commits/4291ce04bda50a95ef71b7aa974423f5fd5f8c1e)? And how to handle the non-optional accept functions?"
<r​brunner7> Is this a case where code execution dives into wallet code and then is supposed to "resurface" to ask the user something interactively?
<r​brunner7> If yes, I always found such constructs quite questionably from an architectural point of view
<r​brunner7> You may have to support of course for backward compatibility ...
<r​brunner7> While I don't see much problems with a CLI based wallet, I ask myself how useful that is in the context of a GUI wallet or even smartphone app
<r​brunner7> Is it expensive to support such accept functions for the Wallet API, regardless of their usefulness, or lack thereof? If they are easy to implement, I ask myself whether you should just implement them
<s​needlewoods> I don't think they're easy to implement, but maybe I'm missing something. If you look they take different arguments e.g. `signed_tx_set` which is not available in the API
<j​berman> looks like it's there so the user can confirm the details of whatever was just loaded (e.g. cold wallet signing sending to the right address), and confirming details in cases like that is a necessary feaure. It also looks like trezor implemented one of these. Moving this out of wallet2 is going to break compatibility with other wallets relying on it today. Which I think is ok in this case, since we're trying to move functionality from wallet2 to the wallet API. It would probably be simplest for downstream wallets to update to a wallet API that re-implements the accept_func in the wallet API functions where it's expected, but so long as the feature is offered, it's alright imo. without accep_func's you would have to expose parse functions in the API, and then functions to do the action (so 1 function with the accept_func callback becomes 2 functions)
<r​brunner7> I guess however you do it there will be a need for additional structs to hold what there is to confirm, like that `signed_tx_set` you mentioned
<s​needlewoods> Alright, think I got it.
<s​needlewoods> iirc we could add one member to `PendingTransaction` to make it able to hold `signed_tx_set`, but would have to check my notes to make sure
<j​effro256> I think that when you have an "accept" function callback for performing a functional task, your API is leaking details, and shouldn't be doing input processing dependent on caller-specific conditions. For example, look at the the `wallet2` member function `sign_tx(const std::string &unsigned_filename, const std::string &signed_filename, std::vector<wallet2::pending_tx> &txs, std::function<bool(const unsigned_tx_set&)> accept_func, bool export_raw)`. This just loads the txset from the file, calls the "accept" callback, then sends the txset to the other overload of `sign_tx`. Nothing about parsing an object of a specific format in a file needs to be part of the `wallet2` API. You should leave in the other `sign_tx` method, but remove the helper overload. If someone else wants to use the helper overload, they can write a free function that does it. There's an infinite number of ways to store data strings, we can't have an overload for every single one in the new API
<j​effro256> So in short: if you're adding a new API endpoint, remove the "accept" callbacks and provide helper functions instead
<r​brunner7> > This just loads the txset from the file
<r​brunner7> Is that available in the API?
<r​brunner7> Or maybe dumb question, this *is* the call to load, and it would be trivial for users of the method to confirm whichever way they want?
<j​effro256> Loading a txset from file is currently a `wallet2` member function (`load_unsigned_tx()`), but it doesn't *need* to be part of a "wallet object" in the new API
<r​brunner7> That I don't understand. How would you load without such a method?
<j​effro256> Make it a free function
<j​effro256> There's nothing to inherit / overload here: the format is the format, regardless of the wallet object implementation
<r​brunner7> Ah, so maybe I don't understand what exactly you mean with "free function"
<j​effro256> It doesn't need to be a method since it stands on its own
<r​brunner7> Yeah, the format is the format, but isn't what wallet2 does some kind of "standard format" that we should support, and people should not have to rewrite themselves?
<j​effro256> By "free function" I mean a function not tied to any class or object, without any need to access any private or protected member variables of any of its inputs
<r​brunner7> You feed it a string then?
<r​brunner7> That you read out of the file
<j​effro256> That's one option. The other option is to have it take that unsigned tx set object directly, and have the caller parse it with a free function provided elsewhere
<r​brunner7> So for every such standard form that wallet2 reads or write, one such free function, and then it's upon the dev to confirm
<r​brunner7> *format
<r​brunner7> Yeah, sounds cleaner, and should not give too much work when migrating
<s​needlewoods> I'm a little lost rn, sorry, if I missed a question
<s​needlewoods> We have `loadUnsignedTx()` for `UnsignedTransaction` already and I added `loadTx()` for `PendingTransaction`.
<j​effro256> Like what I'm saying is that there should be one API object method if possible: `sign_tx` that is actually implementation-specific. We shouldn't have methods `sign_tx_from_file`, `sign_tx_from_string`, `sign_tx_from_url`, `sign_tx_from_file_validated`, `sign_tx_from_string_validated`, `sign_tx_from_url_validated`, etc, etc when all those helpers overloads are doing the exact same thing across all possible implementations
<r​brunner7> I think it's quite easy: For each such current method with an "accept" function parameter, whe basically need to provide a call in the API that does only what the method does *before* it calls that accept function, and just return that to the caller
<r​brunner7> And then of course we need what it does *afterwards* as well ...
<r​brunner7> This gives a much better, Lego like API, like jeffro256 argues
<j​effro256> Yes that's basically what I'm saying. But it doesn't need to be part of the *API*, in the sense that someone might override it in a different implementation. There can be one helper function overload that works for all `wallet2` implementations
<s​needlewoods> jeffro256, what you're saying should apply to the new added functions, not changing the old ones that already break this rule?
<r​brunner7> Do we have such in the Wallet API already?
<r​brunner7> I mean in the old, unenhanced version of yesteryears?
<j​effro256> Well you're *adding* API functions to the API interface, correct? So I would write the new function analogues without the `accept_func` callbacks simply the actual interface
<j​effro256> Well you're _adding_ API functions to the API interface, correct? So I would write the new function analogues without the `accept_func` callbacks to simplify the actual interface
<r​brunner7> If you think it's useful, we two SNeedlewoods could look at some actual examples together this week when you come to it. I think if we join forces we will succeed :)
<s​needlewoods> Sounds good to me
<r​brunner7> Splendid.
<r​brunner7> We are nearing the full hour. Something important left to mention in this very meeting?
<s​needlewoods> Have one minor question at hand
<j​effro256> Think of it like operating system syscalls versus the standard C library. The operating system only provides a very small number of extremely powerful interface endpoints. It's kinda hard to write in pure syscalls, but it's easier to reimplement the implementation of those syscalls and easier to document / understand the whole core API which shouldn't change. But at the end of the day, you can do *everything* by just using syscalls. However, if you want ease of development, you turn to the standard C library to do a lot of repetitive boilerplate for you. We should focus on making a good "syscall" wallet object API that is as minimal as possible while allowing for all features we want to see. We can write a "standard C library" (AKA helper functions) on top of it later to give all the ease of use of all of `wallet2`'s numerous endpoints
<j​effro256> IMO that's how it should be structured
<s​needlewoods> Do we need empty constructors for the interface ([https://github.com/monero-project/monero/pull/9464/files#diff-4814013f88381bf042b3adb2c1a10831a6f800ed956476828186d0fb5b51ba5aR36](src))) and the implementation ([https://github.com/monero-project/monero/pull/9464/files#diff-4814013f88381bf042b3adb2c1a10831a6f800ed956476828186d0fb5b51ba5aR55](src))? Just copied that behavior from other structs/classes in the API.
<r​brunner7> Uh, that I will leave to some C++ cracks to answer ...
<s​needlewoods> messed up the links  .. here interface: https://github.com/monero-project/monero/pull/9464/files#diff-4814013f88381bf042b3adb2c1a10831a6f800ed956476828186d0fb5b51ba5aR36
<s​needlewoods> here implementation: https://github.com/monero-project/monero/pull/9464/files#diff-4814013f88381bf042b3adb2c1a10831a6f800ed956476828186d0fb5b51ba5aR55
<j​effro256> Yes, all classes need to an implementation for the destructor, even if marked "pure virtual" because the C++ standards committee got lazy or something
<sneedlewoods> +1
<r​brunner7> Lol
<j​effro256> There's no technical reason for pure virtual destructors to require an implementation besides "that's how the standard is"
<s​needlewoods> jeffro256 it feels there is a lot of work waiting for me once you start reviewing the API :)
<jeffro256> +1
<r​brunner7> Ok, we got that answered :) I think we can close the meeting here. Thanks everybody for attending, read you again next week
<j​effro256> I usually write it as `virtual ~MyClass() = default;` for clarity
<s​needlewoods> Thanks everyone, lots of valuable feedback :) 
<s​needlewoods> cya
<j​effro256> Thanks everyone! Glad to see all the good work!
````


# Action History
- Created by: rbrunner7 | 2024-10-04T18:24:51+00:00
- Closed at: 2024-10-07T19:38:34+00:00
