---
title: 'Seraphis wallet workgroup meeting #72 - Monday, 2024-05-27, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1013
author: rbrunner7
assignees: []
labels: []
created_at: '2024-05-24T17:11:05+00:00'
updated_at: '2024-05-27T18:38:36+00:00'
type: issue
status: closed
closed_at: '2024-05-27T18:38:36+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1011

# Discussion History
## rbrunner7 | 2024-05-27T18:38:36+00:00
````
<d​angerousfreedom> Hey guys, cant make it for today's meeting.
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1013
<s​needlewoods> hey
<jberman> *waves*
<r​brunner7> Judging from the writings in this room during last week, it has been pretty quiet. Something to report nevertheless?
<r​brunner7> Currently the Haveno people and the XMRBazaar people have much more fun :)
<jberman> me: close to finishing initial lmdb setup for the fcmp tree, finishing that this week and moving to `trim`
<s​needlewoods> been working on API definitions and improved my understanding a bit
<s​needlewoods> code is not pretty yet, but if anyone wants to take a look I should be able to push something maybe tomorrow
<s​needlewoods> else I'll silently continue
<jberman> I also squashed and rebased background sync 8619 (https://github.com/monero-project/monero/pull/8619), it would be nice to get that merged sooner rather than later, consistently dealing with merge conflicts for months has been not so fun
<r​brunner7> Please do. It can be a good idea to look at an API with more than 2 eyes, and before marching on into the implementation.
<jberman> +1 happy to take a look at the code too
<r​brunner7> jberman: Does that any concluding review? E.g. to check whether you didn't silently put in a backdoor while "rebasing"? :)
<r​brunner7> *Does that need
<jberman> yep :)
<r​brunner7> Ok, not sure, but I will try to find time
<jberman> ty
<r​brunner7> Anything special to discuss today?
<jberman> nothing from me
<s​needlewoods> since we still have time, maybe anyone here knows a little more about `wallet2_api.h`
<s​needlewoods> Can someone explain e.g. the benefits of having the `struct Wallet` there, then in `api/wallet.h` we have `class WalletImpl : public Wallet` which overrides all virtual functions and adds new functions. I assume a wallet dev would just import `api/wallet.h`, so why do we need to inherit from `struct Wallet`?
<s​needlewoods> If it's important do declare some functions in `api/wallet2_api.h`, is there a general rule which functions need to be virtual?
<r​brunner7> I don't remember the name, but I think that's a special C++ pattern to do things, with some advantages regarding information hiding, maybe compilation speed, and possibly more.
<r​brunner7> Maybe jberman knows more
<r​brunner7> I dimly remember to have checked that pattern once, already a few years back, and finding it mostly not worth, but really don't remember details
<r​brunner7> I guess now you probably should not worry and just continue with the already firmly established pattern, for better or worse
<s​needlewoods> So far I'm still focusing on `api/wallet.h`, but I feel I'm missing something.
<r​brunner7> What kind of "thing" could be what you miss?
<r​brunner7> Maybe it's just what it looks look: Some slightly over-intrumented and over-complicated, but of course working code
<s​needlewoods> I don't really know
<s​needlewoods> that could be it
<r​brunner7> Maybe you expect something more than is really there :)
<s​needlewoods> alright, nothing more from me, thank you
<r​brunner7> Ok, then we can close the meeting already, thanks for attending! Read you next week again, before some people head to Prague I guess.
<r​brunner7> I think it's PIMPL or something quite similar: https://www.geeksforgeeks.org/pimpl-idiom-in-c-with-examples/
<jberman> wallet2_api.h defines an abstract interface, api/wallet.h implements the interface
<jberman> one reason wallet2_api.h was implemented like that is that you can have a separate implementation of wallet2_api.h somewhere, separate from /api/wallet.h. I don't know of any other implementations/maybe that's how they thought the CLI could eventually work
<jberman> following the same pattern, you'd define all new functions as virtual functions in wallet2_api.h, and api/wallet.h would implement those functions
<jberman> I don't see a great reason for the pattern to exist that way as is.. but probably not worth changing for now
<r​brunner7> At my dayjob I am in a more or less constant fight against building such things in advance, and prematurely. With such "predictions" where things will go you will usually have a pretty bad "hit rate".
<s​needlewoods> jberman ty, sounds understandable
<s​needlewoods> and rbunner I'll take a look at the link
<jberman> one kinda weird pattern to look for also is wallet_manager.cpp/h versus wallet.cpp/h. wallet_manager seems to handle opening/creating/restoring/some wallet setting functionality at a higher level than wallet.cpp/h
<s​needlewoods> yeah I'm still trying to figure that out too
<s​needlewoods> `api/wallet.h` has a create function too
<r​brunner7> As I already mentioned, designing good APIs can be surprisingly hard
<s​needlewoods> and `wallet2.h` has `generate*()` and `make*()`, but it seems they're all used (in simplewallet and rpc_wallet) in a way that none is redundant
<r​brunner7> For such cases the F12 key in VSCode, to easily jump around definitions, is my friend
<s​needlewoods> "At my dayjob I am in a more or less constant fight against building such things in advance, and prematurely. With such "predictions" where things will go you will usually have a pretty bad "hit rate"." <- but in this case you agree that we continue with the existing pattern, because now it's already too late?
<r​brunner7> Basically, yes. The "damage" is long done, and now having two different approaches mixed up seems to me to be more "evil" than just continue with the slight overkill. A little bit similar to that naming question from last week.
<s​needlewoods> Yes, I see
````


# Action History
- Created by: rbrunner7 | 2024-05-24T17:11:05+00:00
- Closed at: 2024-05-27T18:38:36+00:00
