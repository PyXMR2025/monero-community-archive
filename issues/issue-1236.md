---
title: 'Monero Tech Meeting #128 - Monday, 2025-07-14, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1236
author: rbrunner7
assignees: []
labels: []
created_at: '2025-07-11T14:45:46+00:00'
updated_at: '2025-07-15T08:36:38+00:00'
type: issue
status: closed
closed_at: '2025-07-14T18:47:59+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1232).


# Discussion History
## rbrunner7 | 2025-07-14T18:47:59+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1236
<s​needlewoods> Hey
<j​berman> *waves*
<r​brunner7> Could be that message propagation is slow today?
<r​brunner7> Anyway, any reports from last week?
<j​effro256> Howdy
<s​needlewoods> as mentioned earlier "began to remove the MMS, after a chat with tobtoht, with the idea we can re-introduce it post FCMP++"
<s​needlewoods> and worked on some more multisig related stuff in simplewallet
<s​needlewoods> and also fixed an issue I created
<s​needlewoods> idk seems normal to me
<j​effro256> Mainly this last week has been the FCMP++ optimization contest. Have been poking and prodding those submissions, bench-marking, etc. j-berman and I are more or less decided, and will hopefully post our decision soon
<r​brunner7> With dediciding among how many submissions?
<r​brunner7> *deciding
<j​berman> me: depcrated scan_tx scanning *future* txs relative to the wallet's current sync height and merged the FCMP++ impl into the fcmp++-stage branch (github.com/seraphis-migration/monero/pull/49), re-continued local work on supporting high input FCMP++/Carrot txs, and as @jeffro256 said lots of FCMP++ optimization contest handling
<r​brunner7> I would guess 2 or 3 submissions?
<j​berman> 5 distinct contestants (including the initial round prior to the deadline extension), and 1 contestant had multiple submissions
<r​brunner7> Wow
<j​effro256> For the second deadline, there were 4 submitters, with one of them submitting 4 submission variations
<r​brunner7> So it became a true contest in the end
<j​effro256> And one submitted 2 minutes before the deadline ;)
<r​brunner7> Lol
<j​effro256> Yes absolutely, which made it pretty hard to judge honestly. Lots of good stuff
<j​effro256> *"judge, honestly" ... *not* "judge honestly" lol
<sneedlewoods> +1
<r​brunner7> Understood :)
<r​brunner7> If that's it about the reports, I have a question, with the people in the know probably attending:
<r​brunner7> Somebody made a multisig related CCS proposal: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/595
<r​brunner7> As it looks to me, some serious work, for some serious money, 300 XMR
<r​brunner7> I wonder where we currently stand with Monero multisig
<r​brunner7> SNeedlewoods: You said you had a chat with tobtoht regarding this. Any interesting details?
<r​brunner7> Assuming it's ok to share them
<s​needlewoods> tobtoht: "I've mostly lost interest in finishing it before the FCMP++ fork, given how brittle the current multisig implementation is."
<j​berman> The plan floated for some months now is to replace the current internal multisig impl (not high level impl) with kayabanerve  's impl as the backend for the FCMP++ crypto logic
<tobtoht> +1
<s​needlewoods> my understanding of our multisig is slowly building up, but I still lack knowledge of many details and the great picture
<r​brunner7> Yeah, I know that there is something in the "Serai / Rust universe" of code, but does not know much more than that it exists
<j​effro256> When I see big multisig projects like this, I wonder what the actual real-world desire for general-purpose non-enterprise multisig wallets is. RINO multisig was about as user-friendly as it gets, and it basically died b/c it had no market
<r​brunner7> That's of course a whole different question, whether there is demand at all. I am so far mostly interested where we stand on the technical side.
<t​obtoht> The main motivator was getting CCS funds in a multisig wallet to mitigate another hacking incident.
<syntheticbird> +1
<j​effro256> And yeah, general-purpose multisig in Monero is going to suck at a protocol level (no non-interactive balances) until Carrot-keyed wallets are availble on FCMP++
<j​effro256> Or some other bespoke FCMP++ alternative
<tobtoht> +1
<r​brunner7> Remember that. Do I get it that you did not give up on multisig, but you wait for better preconditions after the FCMP++ hardfork?
<t​obtoht> Yes.
<r​brunner7> How is that, will it be much easier to use additional Rust code like that alternative multisig implementation after the codebase became dual-language C++ plus Rust after the hardfork, and all the details about interfacing back and and forth are crystall-clear?
<j​effro256> FROST would be nice for the CCS use-case since the secret shares are publicly verifiable IIRC
<j​effro256> But that's incompatible with the multisig wallets in the reference codebase
<r​brunner7> Yes, there is the question whether we would have to keep the "old" multisig alive, for compatibility reasons. I tend towards "yes" right now
<j​effro256> I'm of the opinion that future multisig developments should happen outside the core codebase NGL, as long as multisig is supported by consensus on a research level. There's so many different ways of doing multisig with different trade-offs, and like you say rbrunner7, once we do it one way, we have somewhat of an obligation to support it indefinitely so people's funds aren't lost
<j​berman> Tbc, IIRC, kayaba already does have crypto logic that is compatible with current multisig wallets that would also be compatible after FCMP++, so it's a matter of re-jigging the internal code to call the Rust
<jeffro256> +1
<r​brunner7> Interesting. Will the Rust multisig stuff be part of some code review?
<s​needlewoods> https://github.com/cypherstack/frostlass
<s​needlewoods> not sure if this is what we're talking about
<j​berman> this audit includes it in scope: https://ccs.getmonero.org/proposals/monero-serai-wallet-audit.html
<r​brunner7> It seems to link to the right repo
<j​berman> kayabanerve will probably have commentary / corrects / clarifications on this discussion as well fwiw
<r​brunner7> Good to know that it's included in that audit. After learning things here now, I stand by my comment below that CCS proposal: I don't think right now is a good time to throw 300 XMR at some multisig solution
<tobtoht> +1
<r​brunner7> I also dream there about a multisig workgroup that brings everything on the right tracks, with good project management and broad consensus :)
<r​brunner7> I am not sure how much of a precedent the demise of RINO is. That was an island of a solution, not some feature broadly available and interoperable over severaly important wallets
<r​brunner7> What I would imagine in the proverbial ideal world
<r​brunner7> But of course I readily admit that people can build whatever they like, and people can donate for what they like.
<j​effro256> Hopefully, once the FCMP++ foundation settles, then Carrot key derivation schemes can settle, then FCMP++/Carrot/OVK-compatible multisig cryptography can settle, and then perhaps multisig messaging standards can settle, and then a good UX application ecosystem can blossom. But right now, IMHO, so much of the multisig plumbing is in flux...
<r​brunner7> IMHO we also need code that has broad support. I am afraid that something planned, designed and built by a single person, without seeking consensus first with the dev community, is in danger of dying if the original author does not carry it forward anymore.
<r​brunner7> Alright. Maybe comment at the CCS proposal if you feel like it :)
<s​needlewoods> multisig workgroup sounds important for that
<j​effro256> Exactly. This CCS may be successful in the short-term, but it WILL need sweeping changes in the medium-term, and it may not be good for other people's use cases, so some other may fund a parallel 300 XMR CCS proposal that fits *their* use case
<r​brunner7> With a standalone GUI program I wonder anyway how to avoid ending up putting more and more wallet functionality in there if it also has the job of making multisig transactions ...
<r​brunner7> At least that was my own reason to stuff everything into the CLI wallet, and *not* making a standalone MMS thing
<j​effro256> Basically, I don't think that that CCS should be outright denied, but it needs more planning from the beginning so this doesn't happen: https://xkcd.com/927/
<r​brunner7> I see that we dream along the same lines, jeffro :)
<jeffro256> +1
<r​brunner7> Our super-strong project management capabilities will save the day. Ahem.
<r​brunner7> Alright, nice to see where we stand with multisig. Anything else to discuss today still?
<r​brunner7> Does not look like it. Thanks everybody for attending, read you again next week!
<s​needlewoods> thank you
````


## plowsof | 2025-07-15T08:36:38+00:00
1 comment more outside of the meeting window:
> _kayabanerve_: The FCMP++ libraries, which will be in the Monero tree, already have multisig protocols defined for CARROT and legacy wallets. The sole requirement is a C++ binding. I see no need to advocate continuing Monero's existing multisig nor integrating Serai's CLSAG this time, though the transition to Serai's CLSAG would do the work for the transition to the FCMP++ legacy wallet multisig protocol


# Action History
- Created by: rbrunner7 | 2025-07-11T14:45:46+00:00
- Closed at: 2025-07-14T18:47:59+00:00
