---
title: 'Monero Tech Meeting #92 - Monday, 2024-10-21, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1094
author: rbrunner7
assignees: []
labels: []
created_at: '2024-10-18T09:28:06+00:00'
updated_at: '2024-10-21T19:02:51+00:00'
type: issue
status: closed
closed_at: '2024-10-21T19:02:51+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1091).


# Discussion History
## rbrunner7 | 2024-10-21T19:02:51+00:00
````
<k​ayabanerve> I won't be present. I've still been working on FCMP++. I extended the tests, had the prover support multiple inputs in a single FCMP (bandwidth savings since Bulletproofs only gain 64 bytes per doubling of their length), and jberman pointed out an author worked at zkSecurity. We've briefly talked about zkSecurity's candidacy for future research efforts.
<k​ayabanerve> I will clarify each input adds hundreds of bytes due to the commitments needed, but the BP itself only grows 64 bytes. It reuses the BP scaffolding which is itself ~1.5-2kB.
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1094
<r​brunner7> Thanks for the report, kayabanerve !
<s​needlewoods> Hey
<s​yntheticbird> Hello
<j​berman> *waves*
<r​brunner7> We already had a report from kaya, just minutes before meeting start. What do the people present to report?
<r​brunner7> *have to report
<s​needlewoods> Again some cleaning up and made progress on the remaining TODOs, mainly the `accept_func` situation, will hopefully be able to push soon.
<s​needlewoods> There is only a single one left (after removing `loadMultisigTxFromFile()`, `signMultisigTxFromFile()` and `loadTx()`*), I can share later where I'm currently stuck with the remaining `parseTxFromStr()`, but will be a little spammy.
<j​effro256> howdt
<s​needlewoods> * Should probably add these to the "List of public wallet2 methods that do not get a counterpart in the wallet API" ([here](https://github.com/monero-project/monero/pull/9464#discussion_r1750620895)).
<s​needlewoods> Also I think, it's probably a good time for reviews/feeback, I'm afraid I waste too much time on unimportant details, so a little nudge in the right direction would be appreciated.
<r​brunner7> Already now, or after that push that you will make soon?
<s​needlewoods> after the push
<rbrunner7> +1
<j​berman> Update: set up sync from scratch in wallet2 building the tree locally (and handling reorgs), testing it today. Also separately handled a bug in my migration code to handle db resizing correctly as needed. Once sync from scratch is tested, planning to implement "start sync from an arbitrary restore height", then planning to get back to fcmp++ tx construction
<j​effro256> Okay I'll take a deeper look this week
<sneedlewoods> +1
<j​effro256> SNeedlewoods @sneedlewoods:
<j​effro256> Me: refactoring the carrot integration out of the seraphis lib to reduce the diff size against master
<r​brunner7> Sounds like great fun
<j​effro256> Haha so much fun .....
<j​berman> CCS update: since I've spent quite some time implementing full wallet sync (while waiting on further fcmp++ prove/verify work from @kayabanerve#2620 ), there is a chance I won't be able to deliver all of fcmp++ tx construction, verification, and consensus changes within the allotted hours of my CCS (my CCS did not originally include implementing wallet sync as a deliverable, but d<clipped messag
<j​berman> id include the latter 3). I bring that up here with intention of bringing it up in the next community meeting this Saturday, hoping to give a far-in-advance heads up of the possibility and get feedback on it
<j​berman> I started on full wallet sync 4 weeks ago
<j​effro256> Wallet tree sync is no small thing , I'd be fine if you closed out this milestone IMO
<r​brunner7> I guess order of implementation does not matter much, seen independently, everyting is needed in the end, so that CCS story is just some "bookkeeping".
<j​effro256> Actually, on second thought, it should be good as long as you're earning 24 $/hour or less
<jberman> :joy:
<s​needlewoods> +1 on rbrunners reply and jeffros first reply
<jeffro256> :smile:
<r​brunner7> Yeah, if in doubt, you may cite the log of this meeting that I will later add to the GitHub meta issue.
<j​berman> ty :)
<r​brunner7> (For Saturday's meeting)
<j​effro256> TBC, this is the proposal yeah ? https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/491
<j​berman> yep
<j​effro256> Is there a public branch where we can watch wallet tree sync yet?
<j​berman> https://github.com/j-berman/monero/commits/fcmp%2B%2B-tree-sync/
<j​berman> this class is handling the bulk of the implementation: https://github.com/j-berman/monero/blob/f44e7f53ae9398e2bf5e3825e304365c6910b9a1/src/fcmp_pp/tree_sync_memory.h
<j​effro256> Awesome thanks
<j​berman> also, here's how I'm currently thinking about implementing "start sync from arbitary restore height": https://github.com/j-berman/monero/blob/f44e7f53ae9398e2bf5e3825e304365c6910b9a1/src/fcmp_pp/tree_sync.h#L75-L83
<j​berman> The approach might change a bit if we end up implementing @jeffro256 's idea to "quick-sync" outputs which unlock before the fcmp++ activation height (the wallet wouldn't need to know about locked outputs that unlock before the fcmp++ activation height): https://github.com/monero-project/monero/pull/9522#issuecomment-2420662734
<r​brunner7> Ok, if we are through with the reports: SNeedlewoods , you wanted to throw us some Wallet API questions to ponder?
<s​needlewoods> Sorry to IRC in advance
<s​needlewoods> I figured we can get rid of `load_tx()` [source](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/wallet/wallet2.cpp#L7961), all it does is: `load_from_file()` (API equivalent: `loadFromFile()`) and `parse_tx_from_str()` (API equiv.: `parseTxFromStr()`).
<s​needlewoods> AIUI ideally users of the API would be able to create their own `load_tx()` method that looks something like this (simplified to visualize the concept):
<s​needlewoods> ```
<s​needlewoods> bool load_tx(const std::string &file_name, PendingTransaction &ptx, std::function<bool(const PendingTransaction&)> accept_func)
<s​needlewoods> {
<s​needlewoods>     std::string file_content;
<s​needlewoods>     // API call
<s​needlewoods>     loadFromFile(file_name, file_content);
<s​needlewoods>     // API call (this should only do the first part of wallet2::parse_tx_from_str(), see below code block)
<s​needlewoods>     parseTxFromStr(file_content, ptx);
<s​needlewoods>     // non-API call, client is responsible
<s​needlewoods>     if (!accept_func || (accept_func && accept_func(ptx)))
<s​needlewoods>         {
<s​needlewoods>             // API call
<s​needlewoods>             importKeyImages(ptx.m_key_images)
<s​needlewoods>             // API call (doesn't exist yet)
<s​needlewoods>             insertColdKeyImages(ptx.tx_key_images);
<s​needlewoods>             return true;
<s​needlewoods>         }
<s​needlewoods>         return false;
<s​needlewoods>     }
<s​needlewoods> sorry for the mess, (re)wrote and rephrased until the last minute, lmk if it's unclear what I mean
<s​needlewoods> Don't need to get an answer right now, just wanted to get it out
<r​brunner7> I believe to recognize the first proposal to be along the lines that jeffro256 voted for in the last meeting, right: Provide "atomic" building blocks that clients can mix and match as they like, with much more flexibility than today's approach with that `accept_func`
<r​brunner7> For the price maybe of a slightly higher number of calls. But at least simple calls, with clearly defined jobs
<s​needlewoods> I tried to follow jeffros suggestions, but not sure how close I came with my interpretation
<r​brunner7> With "atomic" I mean something that you can't possible program yourself on your own, outside of the Wallet API
<r​brunner7> At first sight looks like a successful interpretation of the approach to me. The only question I can come up with right now would be compatibility: Do we alread have, in the "old" Wallet API, such "accept funcs"? That clients probably use now?
<r​brunner7> If yes, that might complicate the decision a bit
<s​needlewoods> If I understand you correctly, no, there are no such functions in the wallet API
<r​brunner7> Good. Then I would not introduce them, IMHO. Never mind that the work to modify clients that now use *wallet2* accept funcs would be a bit higher, that should not stop us.
<r​brunner7> So +1 for your first proposal.
<s​needlewoods> e.g. [wallet2 method](https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/src/wallet/wallet2.h#L1212) -> ["old" API method](https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/src/wallet/api/wallet.cpp#L1590) just ditches the accept_func
<r​brunner7> We may need such to properly migrate the CLI wallet to the Wallet API, however.
<r​brunner7> As maybe the only client ever needing such
<k​ayabanerve> rbrunner7:
<k​ayabanerve> > "atomic" building blocks
<k​ayabanerve> If only had built a wallet library which gives users the building blocks for their wallets
<s​needlewoods> I will come back to your offer to look at this together this week if you don't mind
<rbrunner7> +1
<k​ayabanerve> Maybe in Rust? With full API documentations? Ready for audit?
<r​brunner7> Yes. Yes. *That* library :)
<k​ayabanerve> :p
<r​brunner7> Alright. Anything else left for this very meeting?
<s​needlewoods> I'm still wondering if anyone has feedback on [this note](https://github.com/monero-project/monero/pull/9492#discussion_r1794199366) I left on vthors PR.
<j​effro256> I like the idea of pulling in kayabanerve 's Rust wallet library for implementing the new the C++ API that SNeedlewoods is drafting up
<j​effro256> I can't really speak to the toolchain effects of that path tho
<r​brunner7> You mean the non-wallet2-based successor?
<r​brunner7> That sound like a quite bold plan, but yeah, maybe after a closer look ...
<j​effro256> We're adding in Rust to our toolchain for FCMP++ anyways and the `monero-wallet` Rust crate will likely be officially audited
<s​needlewoods> would I need to learn rust first?
<r​brunner7> Things will stay interesting for quite a while, that's for sure.
<j​effro256> Probably not if there is an FFI provided
<r​brunner7> Maybe not, if you are only using the library
<s​needlewoods> then it may be not too scary
<r​brunner7> That library has FCMP++ support still ahead of it?
<r​brunner7> And Carrot
<j​effro256> That's a good question for kayabanerve . I know  it doesn't have Carrot code in it yet
<r​brunner7> I think we can close the meeting while of course we can chat on about all those rusty things. Thanks for attending, read you again neext week!
<s​yntheticbird> Thanks. Delicious meeting as always
<s​needlewoods> thanks everyone, cya
<r​brunner7> I don't doubt that kaya will make sure one way or another that his library will be ready at the FCMP++ hardfork
<j​effro256> Thanks all!
<r​brunner7> Otherwise things would make absolutely no sense
````

# Action History
- Created by: rbrunner7 | 2024-10-18T09:28:06+00:00
- Closed at: 2024-10-21T19:02:51+00:00
