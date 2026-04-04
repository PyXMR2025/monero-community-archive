---
title: The Monero core software wallet API will (probably) switch from 'wallet2.h'
  to 'wallet2_api.h'
source_url: https://github.com/monero-project/monero/issues/9308
author: rbrunner7
assignees: []
labels:
- discussion
- wallet
created_at: '2024-04-28T15:08:43+00:00'
updated_at: '2025-01-21T18:08:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## The Short Version

The devs from the [Seraphis wallet workgroup](https://github.com/seraphis-migration/strategy/wiki/Seraphis-Wallet-Workgroup) currently build a new wallet implementation for the Monero core software. It will supersede `wallet2.h` plus `wallet2.cpp` which won't be available anymore for programs like the Monero CLI wallet or the Monero RCP server, and neither for any third-party wallet apps like Cake Wallet, Monerujo and so on. The API for the new wallet will be [wallet2_api.h](https://github.com/monero-project/monero/blob/master/src/wallet/api/wallet2_api.h) plus a number of related header files from the [/source/wallet/api](https://github.com/monero-project/monero/tree/master/src/wallet/api) folder of the Monero source code. All things that are now only in the `wallet2.h` "API" will be added to that, to cover 100% of the necessary functionality, and to make getting fully rid of `wallet2.h` possible in the first place.

## The Long Version

Right now as I write this, in Spring 2024, it's not fully clear how the path of the Monero software into the future will look exactly. Most probably it will use FCMPs, but apart from that there are several possible directions to take. What is clear however is that the wallet implementation of the core Monero software, with its massive 15,000 lines of complex code in a single source file called [wallet2.cpp](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp), is definitely ill suited for larger modifications to accommodate transactions that work rather differently.

We, i.e. the group of Monero devs that are engaged in the [Seraphis wallet workgroup](https://github.com/seraphis-migration/strategy/wiki/Seraphis-Wallet-Workgroup), are convinced that the time has finally come to retire `wallet2` and replace it with a full rewrite. Actually, work on this has started quite a while ago and will hopefully soon pick up speed considerably: We are already on the way.

One question left unanswered so far for quite a while already was this: How will the *API* of this new wallet look? Which C++ methods, structs, enums and so on will it offer, for wallet app writers to use?

Personally I once had a dream of a brand-new such wallet API, designed out on a green field, making things possible like keeping several wallets open at the same time seamlessly and syncing them in parallel, unify wallet API and RPC server API so that the only difference between the two would be that for the first you make direct C++ method calls and remote "calls" for the second, and maybe offering a clean superset API for multisig wallets instead of cramming them into a single API as well.

The progression of time and the realities of available dev capacity made this dream to be out of reach however. And hey, maybe such a drastic cut never was a really clever idea ...

Recently *jberman* made [this proposal](https://github.com/seraphis-migration/wallet3/issues/64). In short: In addition to `wallet2.h` there is already a second API in the Monero codebase in the form of [wallet2_api.h](https://github.com/monero-project/monero/blob/master/src/wallet/api/wallet2_api.h) plus a number of related header files also in the [/source/wallet/api](https://github.com/monero-project/monero/tree/master/src/wallet/api folder of the Monero source code) folder. The GUI wallet and a number of third-party wallet apps mainly use this instead of `wallet2.h`. Our new wallet shall use this as its API.

This proposal was very well received; I am not aware of even a single person voicing clear disapproval, at least until now. We discussed the proposal in our group meeting on April 22, and we approved it. You find details in the [meeting log](https://github.com/monero-project/meta/issues/993).

We currently plan to start with making the API feature-complete, i.e. adding all things to `wallet2_api.h` that so far are only available by using the lower `wallet2.h` directly, and then probably also providing an implementation internally based on `wallet2`. This should allow wallet app writers, if they so wish of course, to soon start any necessary move to the new API while we rewrite the implementation that will finaly replace `wallet2.cpp`.

Things happen in the open. People who are interested in these developments are invited to join our [Matrix room](https://matrix.to/#/#no-wallet-left-behind:monero.social) or the *#no-wallet-left-behind* IRC channel on Libera.chat. You find the announcements for the regular Monday group meetings [here](https://github.com/monero-project/meta/issues).

Now finally to the "probably" in the title: Can those people from that "wallet workgroup" really decide to throw `wallet2` out of the Monero codebase and force everybody to adjust to that `wallet2_api`? As I personally see it, yes and no. No because they don't have formal authority for this; in fact, nobody has any such "formal authority" in a true open source project like Monero is one! Yes because if they implement a new wallet, and it comes out decent, the rest of the Monero dev community at large will probably follow along nevertheless.

Anyway, Monero development rises and falls with engagement. Make your voice heard if the things mentioned here are important to you.



# Discussion History
## selsta | 2024-06-14T21:28:01+00:00
@tobtoht you worked a lot with wallet2_api, what is your opinion here?

## selsta | 2024-06-14T21:36:59+00:00
Developing a new wallet implementation sounds like significantly more work than the API itself, why do all this work but then inheret an unmaintained and buggy API? It seems like cutting corners in the wrong place.

## binarybaron | 2025-01-21T16:33:58+00:00
We are switching from `monero-wallet-rpc` to native bindings, and building a Rust FFI wrapper. Is `wallet2_api.h` the way to go or should we stick to `wallet2.h`?

## rbrunner7 | 2025-01-21T18:08:29+00:00
@binarybaron: The general direction, i.e. the switch from `wallet2.h` to the Wallet API still seems uncontroversial, and the PR #9464 that adds (almost) all still missing functionality to the Wallet API is nearing review and eventual merge into Master.

One of the next steps on the Monero side will probably be to switch the Monero CLI wallet to Wallet API, as discussed in yesterday's tech meeting.

# Action History
- Created by: rbrunner7 | 2024-04-28T15:08:43+00:00
