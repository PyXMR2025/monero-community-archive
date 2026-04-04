---
title: 'Monero Tech Meeting #133 - Monday, 2025-08-18, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1255
author: rbrunner7
assignees: []
labels: []
created_at: '2025-08-15T17:07:53+00:00'
updated_at: '2025-08-18T18:30:52+00:00'
type: issue
status: closed
closed_at: '2025-08-18T18:30:52+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1252).


# Discussion History
## rbrunner7 | 2025-08-18T18:30:52+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1255
<s​needlewoods> hey
<j​effro256> Howdy
<j​berman> *waves*
<r​brunner7> Alright, with that wave we can start with the reports from last week
<s​needlewoods> I wrote a wrapper so `wallet_keys_unlocker` can be used by the Wallet API ([commit](https://github.com/monero-project/monero/commit/c995b8dd03ab7a3d7e03cf078142144a49ae2bbd)), also based it onto jeffros improved version [#9860](https://github.com/monero-project/monero/pull/9860), was excited when the tests passed, but after testing `make_multisig` manually from the CLI it still doesn't work, so will have to do more debugging.
<s​needlewoods> Would be nice to get some feedback on the commit, it feels a little messy with all the forward declarations and I'm not sure there may be room for improvements
<v​tnerd> Hi
<s​yntheticbird> hi
<r​brunner7> Uh, that #9860 PR looks pretty wild, with all those issues about something so small ...
<r​brunner7> Is that not yet merged because a second review is missing?
<s​needlewoods> also re-review was requested after two small changes afaict
<j​berman> me: no significant update from last week (was mostly unavailable for personal reasons unrelated to the mainnet situation, I'm back at 100% now). Patched a bug reported by ofrn (fcmp++ wallet refresh recovering from daemon popping blocks correctly), currently investigating another. Once this final set of bugs is out of the way, I intend to take next steps on alpha stressnet (setting a start date, writing a post with instructions on how to join, etc.)
<r​brunner7> Sounds like the real fun can soon start then. allpha net will be a pretty milestone I think.
<j​effro256> Me: I mostly worked on consensus based hash changes, unrelated to Qubic stuff (e.g. https://github.com/monero-project/monero/pull/10038)
<r​brunner7> What is an "intermediate PoW hash"?
<j​effro256> I also want to propose a new Carrot math audit at the next MRL to address some small things: https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb
<j​effro256> It enabled tevador's idea to be able to partially check PoW without needed to use RandomX, but a much smaller, lighter function Blake2B
<j​effro256> SNeedlewoods: looking at that commit now
<sneedlewoods> +1
<o​frnxmr> got my fcmp testnet up to ~18mb blocks, mining stopped for now while jberman investigates an issue
<r​brunner7> Ah, I see. That's floating around for quite a while already
<r​brunner7> https://github.com/monero-project/monero/issues/8827
<j​effro256> Yes, exactly
<j​effro256> Will link that in the PR, thanks
<r​brunner7> So this Carrot follow-up audit will preferrably go again to CypherStack, to profit from pre-knowledge?
<j​effro256> Yes, it *should* be relatively quick I think
<j​effro256> Haven't solicited quotes yet, just wanted to see if anyone would be opposed to it
<j​berman> Proposed follow-up audit lgtm
<r​brunner7> Yeah, checking again can't be wrong. If a problem sneaked in, however unlikely that is, we must know.
<o​frnxmr> also to note that my fcmp testnet is using jbermans 128in pr, and i feel the public /alpha test/stress net should as well
<j​effro256> Agreed
<r​brunner7> For the record, and for visibility, here a link to kayabNerve's CCS proposal to harden Monero against certain attacks, the "Finality Layer Book": https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/604
<r​brunner7> Don't be shy, make your voice heard
<j​berman> I'll share a comment on that proposal soon
<j​berman> likely today
<rbrunner7> +1
<o​frnxmr> The ccs isnt to do any implementation, and shouldnt be misinterpreted as monero is going yo use a tfl, but solely the book, explaining/documenting the proposed solution
<r​brunner7> It's unfortunate that we probably will have *two* monster projects running side-by-side, at least for some time, but you can't choose that.
<o​frnxmr> So the ccs isnt "to harden monero against certain attacks", but to write a book about it
<r​brunner7> You are right, too easy to misunderstand the way I put it. But anyway, the *idea* is that this book will lead to a way to harden Monero - if we do anything at all in this direction of course.
<r​brunner7> I guess we have many quite controversial discussions ahead on the way to that.
<ofrnxmr> +1
<r​brunner7> Ok, do we have to discuss something today beyond these reports?
<r​brunner7> For mere length of meeting, MRL wins hands down for quite a while :) We might have more to coordinate once the alpha net starts.
<s​needlewoods> last MRL meeting no one told me to bring water, was very dehydrated at the end
<r​brunner7> Lol
<r​brunner7> I think we can close for today. Thanks everybody for attending, read you again next week!
<s​needlewoods> thanks everyone, cu
````


# Action History
- Created by: rbrunner7 | 2025-08-15T17:07:53+00:00
- Closed at: 2025-08-18T18:30:52+00:00
