---
title: 'Monero Tech Meeting #158 - Monday, 2026-02-23, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1344
author: rbrunner7
assignees: []
labels: []
created_at: '2026-02-20T15:01:38+00:00'
updated_at: '2026-02-23T18:38:38+00:00'
type: issue
status: closed
closed_at: '2026-02-23T18:38:38+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1338).


# Discussion History
## rbrunner7 | 2026-02-23T18:38:38+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1344
<s​needlewoods> Hello
<j​pk68> Hello
<r​brunner7> From jberman about half an hour ago: "Likely won't be able to make today's meeting unfortunately. This week will work on audit coordination and getting beta ready"
<r​brunner7> In last week's MRL meeting it basically was also only Rucknium and me :)
<j​effro256> Howdy
<r​brunner7> Alright, what is there to report from the last 2 weeks? Me: Checking wallets and wallet source code regarding Polyseed support. Slowly arriving somewhere.
<j​effro256> Me: Cypherstack finished their carrot_core audit: https://github.com/cypherstack/carrot_core-audit/blob/main/carrot_core-audit.pdf. I finished with first round of review on beta scaling after talking with Artic and j-berman: https://github.com/seraphis-migration/monero/pull/282.
<r​brunner7> Found out that the `monero_c` build process is a true marvel.
<s​needlewoods> still mainly working on wallet-rpc, counting `m_wallet` 144/354 (354 is the count on `master` branch)
<jeffro256> +1
<j​effro256> Also me: gave a talk at Monerotopia and implemented RandomX V2 support in https://github.com/monero-project/monero/pull/10038
<j​effro256> Talking with some auditors about upcoming FCMP++ integration audits
<r​brunner7> A few words about Monerotopia? How was your talk received, live?
<j​pk68> Your talk was good, Jeffro :)
<interloper> +1
<j​pk68> I watched online
<r​brunner7> Are the talks online already, linked from the Monerotopia website then?
<i​ntr:unredacted.org> I don't know about a link from monerotopia but they are on twitter (cut into individual videos), and the entire livestreams are on youtube on the Monerotalk channel
<r​brunner7> This maybe: https://monerotopia.com/monerotopia2026-virtual-conference/
<s​needlewoods> https://www.youtube.com/@MoneroTalk/streams
<i​ntr:unredacted.org> and: 
<i​ntr:unredacted.org> https://x.com/XBTXMR/status/2022623288120250599
<i​ntr:unredacted.org> https://xcancel.com/XBTXMR/status/2022623288120250599#m
<j​effro256> Monerotopia was awesome, definitely recommended to anyone if they can make it. There was nowhere near the  OVK doomerism in person as online ;)
<r​brunner7> Good to hear!
<j​effro256> Lots of great talks in the dome and out of the dome
<j​effro256> Met the Cyperstack folks for the first and they're great too
<r​brunner7> You mean their new people?
<j​effro256> Any of them ;) Never met Diego in-person, nor Luke, nor Rigo, nor Josh, etc
<j​effro256> nor Brandon
<j​effro256> I guess I've met Sarang, who *used* to be at Cypherstack IIRC
<r​brunner7> I see. Yeah, it's nice to finally meet people in the real world, after so many virtual contacts
<r​brunner7> Alright, seems that's it about the reports. Do we have anything to discuss today beyond those?
<s​needlewoods> I noticed something in regards to exceptions in wallet-rpc
<s​needlewoods> in wallet-rpc we often have this pattern `try { m_wallet->some_method(); } catch (const std::exception &e) { handle_rpc_exception(std::current_exception); }` e.g. [here](https://github.com/monero-project/monero/blob/4efde0f4da05e908fd159b02a12dea3c46a6749a/src/wallet/wallet_rpc_server.cpp#L2367-L2384), meaning the exception comes directly from `wallet2`. Now the Wallet API handles<clipped 
<s​needlewoods>  exceptions on it's own (by `setStatusError(error_msg)` if there was something to catch) and does not propagate them.
<s​needlewoods> For now I added a macro to wallet-rpc that I call after `m_wallet_impl->someMethod()` to keep the pattern: `THROW_WALLET_EXCEPTION_ON_API_ERROR(tools::error::wallet_internal_error)`
<s​needlewoods> But this way we lose control of `handle_rpc_exception()` [src](https://github.com/monero-project/monero/blob/4efde0f4da05e908fd159b02a12dea3c46a6749a/src/wallet/wallet_rpc_server.cpp#L3809), most importantly the `er.code` for the response.
<s​needlewoods> Any suggestions are welcome.
<s​needlewoods> don't need an answer now, just wanted to get it out
<r​brunner7> My first naive reaction is the question why still handling anything with exceptions in the RPC code? Are there other sources of exceptions than then Wallet API?
<r​brunner7> Or better said, now that the Wallet API is no source of exceptions anymore, what is left?
<s​needlewoods> yes, a lot of arguments are getting pre validated
<j​effro256> Ah I see, I think that I would break the pattern in wallet-rpc then if we plan to keep using the check-type API. Very few endpoints in the `wallet2_api` actually throw exceptions, right?
<s​needlewoods> I mean e.g. something like this https://github.com/monero-project/monero/blob/4efde0f4da05e908fd159b02a12dea3c46a6749a/src/wallet/wallet_rpc_server.cpp#L651
<s​needlewoods> AFAIK if they throw exceptions, then the implementation is incorrect
<r​brunner7> I would also strongly suspect that exceptions are not part of the API, so to say
<j​effro256> Looking at the source, a lot of the multisig code throws exceptions, but that's all the exceptions that I can see which *originate* in the wallet2_api
<j​effro256> So that feels like a mistake
<j​effro256> So yeah if we plan to stay with the current `wallet2_api` exception handling, then it's RPC which hould be refactored
<s​needlewoods> if you are referring to [checkMultisigWalletReady()](https://github.com/monero-project/monero/blob/4efde0f4da05e908fd159b02a12dea3c46a6749a/src/wallet/api/wallet.cpp#L120) that method is called inside a `try` block [src](https://github.com/monero-project/monero/blob/4efde0f4da05e908fd159b02a12dea3c46a6749a/src/wallet/api/wallet.cpp#L1524)
<jeffro256> +1
<r​brunner7> Your question basically is whether people also see your approach as the "least bad" that is possible while keeping the general exception centric approach, SNeedlewoods ?
<j​effro256> If the `wallet2_api` exception handling isn't "rich" enough to keep the RPC API intact, then that information needs to be added to the `wallet2_api` exception handling
<s​needlewoods> Yes
<r​brunner7> Don't remember right now, does the RCP interface give back detailed error info to the remote caller?
<s​needlewoods> An alternative I see (which I think is very bad) is to read the error messages in the wallet rpc and then throw according to the messages
<r​brunner7> Or is it more a question of what goes into logs?
<s​needlewoods> The logs will change slightly, but that shouldn't be a big problem AFAICT. I'm more concerned about the error codes that get returned by failing RPC calls
<jeffro256> +1
<j​effro256> https://github.com/monero-project/monero/blob/4efde0f4da05e908fd159b02a12dea3c46a6749a/src/wallet/wallet_rpc_server_error_codes.h
<j​effro256> These errors code should absolutely retain their place in the API
<j​effro256> And also their corresponding error messages, but to a much lesser extent IMO
<s​needlewoods> I will focus on this during this week
<r​brunner7> Maybe there is some way to make codes available to callers that does not break the API? And then it's only question of translating Wallet API codes to RPC wallet codes.
<r​brunner7> That stuff is too far away, have to check again
<s​needlewoods> Alright, thanks for the feedback
<r​brunner7> Ok, looks like we can close the meeting here. Thanks everybody for attending, read you again next week!
<s​needlewoods> Thanks everyone, see you
````


# Action History
- Created by: rbrunner7 | 2026-02-20T15:01:38+00:00
- Closed at: 2026-02-23T18:38:38+00:00
