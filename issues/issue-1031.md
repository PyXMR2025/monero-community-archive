---
title: 'Seraphis wallet workgroup meeting #76 - Monday, 2024-07-01, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1031
author: rbrunner7
assignees: []
labels: []
created_at: '2024-06-29T15:19:43+00:00'
updated_at: '2024-07-01T18:52:57+00:00'
type: issue
status: closed
closed_at: '2024-07-01T18:52:57+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1026

# Discussion History
## rbrunner7 | 2024-07-01T18:52:57+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1031
<jberman> *waves*
<s​needlewoods> hey
<o​ne-horse-wagon> Hello
<r​brunner7> Any reports from last week?
<jberman> me: pushed the fix+updated design for fcmp's grow_tree I mentioned last week: https://github.com/j-berman/monero/commit/e0502e41843a9b74fbce22805d067ce73c517d13
<jberman> grow_tree and trim_tree are approaching production-grade ready for PR. Going back to trim_tree this week
<s​needlewoods> Still working on missing functions in the API, took notes on several things I found (most of them are not related to the API and nothing urgent, so will look into discussing/fixing those when there is time).
<r​brunner7> jberman: Where will this code go? Into Monero master already? Or will there be some "working repository" for FCMP?
<s​needlewoods> The most noteworthy discovery, in case I'm not missing something, currently in the API we create pending txs with either `createTransactionMultDest` or `createSweepUnmixableTransaction`. Then we need to commit the ptx to the daemon, but the API only has a method `submitTransaction` which submits a tx from a file for given file name and there is no function in the API to store the <clipped m
<s​needlewoods> ptx (we got from one of the `create*` functions) to file.
<s​needlewoods> I can't really believe that currently there is no way to create and submit a transaction from the API. But if that's actually the case, we could overload the method `submitTransaction` to accept a ptx vector instead of a file name and I think we should add a `[store/save]Transaction` function to store a ptx to file.
<r​brunner7> Sounds a bit confusing, SNeedlewoods . Maybe quickly check what the GUI wallet code is doing in this regard?
<jberman> I'm not sure where it will go yet (not planning to submit a PR yet even when the isolated components are "ready" for PR); for now I was thinking to just keep it in my working branch
<s​needlewoods> I'm not familiar with the GUI code, but will look into it later, thanks for the hint
<r​brunner7> A brute-force search for some identifier names usually does the trick :)
<jberman> (I branched from master)
<r​brunner7> I see, jberman.
<r​brunner7> Early days :)
<o​ne-horse-wagon> jberman.  FCMP is supposed to be written in Rust as I understand  it.  Is there any Rust code posted anywhere just yet?
<jberman> I'd say the main thing holding back submitting a PR would be settling on the rust FFI component. for the grow_tree and trim_tree code, I basically sectioned off the rust side, so it's not so intertwined with the C++ tree code and the tree code could be reviewed in isolation, but I don't think we're ready yet to get the rust FFI stuff into master
<j​effro256> Howdy
<j​effro256> Sorry I'm late
<r​brunner7> I wonder whether the path to indeed get Rust into master is already clear, at least. Sounds like quite some leap.
<r​brunner7> And of course Rust capable reviewers have to show up.
<jberman> @one-horse-wagon: here is the core fcmp rust code that @kayabaNerve wrote: https://github.com/kayabaNerve/fcmp-plus-plus
<s​needlewoods> not sure how to phrase it, but from a quick search it seems that GUI uses it's own function and doesn't use the API to commit a ptx https://github.com/monero-project/monero-gui/blob/master/src/libwalletqt/Wallet.cpp#L662
<jberman> here's my working code that uses an interface into that code in the fcmp_rust folder: https://github.com/j-berman/monero/tree/e0502e41843a9b74fbce22805d067ce73c517d13/src/fcmp
<k​ayabanerve> *waves*
<k​ayabanerve> I'm here, what I did last week is same as MRL. FCMP++ review and initial divisors proofs are done. Moving forward with organizing other research things.
<k​ayabanerve> jberman set up the FFI successfully and I did get it to cross compile.
<jberman> the bulk of the tree code is written in C++ in that working commit
<j​effro256> Nice !
<jberman> yes nice work from kayaba on cross-compilation here :) https://github.com/j-berman/monero/pull/11
<k​ayabanerve> I believe all cross compilation targets work. There's some linking errors yet I believe those to be some C++ error not immediately relevant to cross compiling (as even native builds on some platforms don't always like how some of the headers were). If resolving those then identifies cross compilation errors, I'll be happy to fix them.
<r​brunner7> With "cross compilation" you mean that a single compile process goes over everything be it C++ or Rust?
<k​ayabanerve> No. Building armv8 bins from an x86_64 host.
<r​brunner7> So just compiling over two languages is not difficult.
<k​ayabanerve> There was already a Rust CMake integration FYI. I'm not discussing that here. That was done.
<k​ayabanerve> Yeah, it's the added deps but the CMake integration means no extra commands.
<k​ayabanerve> Cross-compiling requiring reformatting CMake target config into a Rust target config and extending the CMake integration (just some build commands jberman added) with the relevant args.
<r​brunner7> Interesting. But anyway, complexity takes a step upward, as well as challenges for current and future devs. I for example do not know much more about Rust than that it exists ...
<k​ayabanerve> The only thing that should change is you'll learn how to install Rust ;)
<r​brunner7> Comforting :)
<j​effro256> Are there any systems that we could possibly be excluding by making them install rust toolchains ?
<r​brunner7> OpenBSD maybe?
<o​ne-horse-wagon> rbrunner7: Take a look at the Rust language.  It is more logical than C or C++ IMO.  I find it much easier to learn vs. C and the impossible C++.  I could never get anywhere with those two.
<r​brunner7> It's not one of our "official" targets but works pretty well - so far
<r​brunner7> official = our download page offers signed binaries for that platform
<r​brunner7> one-horse-wagon: Sounds good. Anyway, get to a point where I can read Rust code should not be that hard, I guess.
<r​brunner7> Alright. Anything more, about wallet stuff in particular?
<j​effro256> I wrote a first draft of of the temprosry sub address missing enote fix
<r​brunner7> That's about Jamtis RCT, right? Some special case there I guess
<k​ayabanerve> I setup cross compilation for all targets we cross compile for.
<k​ayabanerve> Even dragonfly has a rust target iirc
<k​ayabanerve> And the Solaris targets.
<r​brunner7> If you happen to get a look at OpenBSD support, kayabanerve , I would be curious
<r​brunner7> I think they definitely don't like any cross compiling there.
<j​effro256> rbrunner7: no its a problem that all cryptonote addresses have had since the invention of subaddresses
<j​effro256> If your subaddress table is too small at a given point in time you will miss scanning some enotes
<r​brunner7> Ah, ok, that problem. You try to find kind of a solution for that?
<j​effro256> You can fix that with masked amount enotes by recomputing C first instead of Ko
<j​effro256> (And checking that the tx pubkey is in the prime subgroup)
<j​effro256> You will only recompute C correctly if the enote is addressed to you (I.e. the mask is bound to a shared secret against your private view key)
<r​brunner7> Does that need a hardfork? Or would that be something to introduce together with FCMPs anyway?
<k​ayabanerve> I did do OpenBSD rbrunner7
<rbrunner7> +1
<j​effro256> Nope not even a change to the addressing protocol
<j​effro256> Just a scanning side logic trick
<r​brunner7> Astonishing, somehow. Something overlooked for so long a time then?
<jberman> how do we handle the UX of someone sending you an enote you can decrypt the amount but not spend (incorrect output pub key), or it's a super high indexed subaddress that the user doesn't add? just continue scanning after receiving the warning "you may have received this output to a subaddress you have not yet added"?
<j​effro256> Only was an option since RingCT
<j​effro256> And only performant with view tags
<r​brunner7> ? Are subaddresses older thatn that?
<r​brunner7> (older than RingCT)
<r​brunner7> jberman, don't we add all subaddresses automatically? Now with this trick even "super high" ones?
<jberman> (I meant with this proposed change)
<j​effro256> Jberman: yeah that's def the worst case. Ideally for advanced users we would probably let silence those warnings with the freeze command
<j​effro256> Or something silimar
<j​effro256> Justa n explicit flag on this output to permanently ignore
<r​brunner7> Not sure I understand. Does something prevent just adding *any* subaddress?
<j​effro256> Nope
<j​effro256> Kinda same concept with Janus attacks
<j​effro256> There's no deterministic sscure way to derive a specific subaddress spendkey
<j​effro256> So they could just send to a random subaddress spendkey
<k​ayabanerve> You can't recover the index. You can use a unrealistic index to permanently have an address with an unknown index accordingly.
<k​ayabanerve> Wallets should increase the scanahead upon detection of such an output yet not display it IMO.
<r​brunner7> So one problem solved, another one created? All a bit confusing for crypto noobs like me.
<j​effro256> Well its already a problem, you just don't see it happen, you just lose the enote entirely
<j​effro256> It silently fails
<k​ayabanerve> IMO, it just helps determine how far to try scanning ahead.
<r​brunner7> You mean today you never notice it's there, right?
<r​brunner7> That enote
<jberman> @rbrunner7 the user would still need to add subaddresses via an extra manual step. the benefit with this approach is that when scanning, the scanner can identify outputs the user may have received to a subaddress they have not yet added, and then either notify the user they may want to try manually adding subaddress(es) to see if the output is
<jberman> theirs or expand the lookahead some amount like kayaba just said (but it can still miss with this approach)
<j​effro256> Yes
<r​brunner7> Alright. Anything else for this meeting proper?
<r​brunner7> Maybe a little hint that we are having much fun over at "stressnet". Daemons struggle and fail in many quite surprising ways. Blocksize is currently approaching 4 MB.
<r​brunner7> Have a look if you are bored or have too much time on your hand!
<r​brunner7> Thanks for attending then, read you again next week!
<s​needlewoods> thank you, cu next time
````


# Action History
- Created by: rbrunner7 | 2024-06-29T15:19:43+00:00
- Closed at: 2024-07-01T18:52:57+00:00
