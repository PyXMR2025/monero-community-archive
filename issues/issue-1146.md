---
title: 'Monero Tech Meeting #105 - Monday, 2025-01-27, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1146
author: rbrunner7
assignees: []
labels: []
created_at: '2025-01-24T15:19:20+00:00'
updated_at: '2025-01-27T19:00:37+00:00'
type: issue
status: closed
closed_at: '2025-01-27T19:00:36+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1143).

# Discussion History
## rbrunner7 | 2025-01-27T19:00:36+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1146
<jeffro256> Howdy
<sneedlewoods> Hey
<jberman> waves
<rbrunner7> Alright, what is there to report from last week?
<rbrunner7> I did something that was long overdue and studied the Carrot spec. I plan to write a series of posts for the Monero subreddit and Monero.Town to explain Carrot and heighten "awareness"
<sneedlewoods> +1
<rottenwheel> +1
<sneedlewoods> Began removing wallet2 from simplewallet.
<sneedlewoods> But before I continue there, vthor proposed I can add the changes from https://github.com/monero-project/monero/pull/9492 to my Wallet API PR. After discussing the idea with rbrunner and vthor I agreed to work on it.
<rbrunner7> So I will probably postpone my review of your PR until you took that code in
<sneedlewoods> Hopefully done by Wednesday
<jberman> Updated the WIP FCMP++ PR with the latest, continued with FCMP++ tx construction, nothing significant to report there yet. Hoping to get to drafting tests for the FCMP++ optimization competition today/tomorrow 
<sneedlewoods> Should I squash the changes or first add another commit?
<jeffro256> Testing/improving carrot integration code. Trying to minimize the amount of updates to the wallet2 flow. Also researching different key derivation schemes for different hardware wallets to sketch out better migration paths. Will post a CCS proposal later today. Also reviewing others' PRs
<jberman> Updated the WIP FCMP++ PR with the latest, continued with FCMP++ tx construction, nothing significant to report there yet. Hoping to get to drafting tests for the FCMP++ optimization competition today/tomorrow
<jeffro256> +1
<rottenwheel> +1
<jeffro256> Are the signing code tests passing yet?
<jberman> Nope not yet
<rbrunner7> SNeedlewoods: Maybe it does not matter much because the end result will be squashed anyway? Might be hard to keep the DiosDelRayo change separate to have them still visible?
<rbrunner7> Is Carrot excpected to be "final" spec-wise, only pending adding that QC stuff?
<j​effro256> It's pretty darn close
<r​brunner7> Good to hear
<r​brunner7> So it's also a good time to start making more "noise" about Carrot.
<j​effro256> Basically the only non-trivial changes I can see being added are changing subaddress derivation for Carrot-derived address such that it allows for quantum-proof opening
<j​effro256> But the addressing protocol should basically be set in stone AFAICT
<j​effro256> But even those changes might not be necessary
<r​brunner7> Maybe I asked this already but forgot: What's the path to a final decision regarding that quantum-proofing? Does this need reaching a consensus in the MRL, or more research?
<r​brunner7> Or maybe some benchmarking?
<j​effro256> Honestly just more research on efficient PQ proving systems. I think theoretically with the current subaddress scheme we get the same PQ spend protection as Bitcoin: a hash is stored on chain and is safe for arbitrary periods of time, and the original owner can reveal a preimage to spend those funds. But as soon as they do, there's a race to use that preimage to spend their funds
<j​effro256> In other words, very weak protection
<j​effro256> But also it's feasible that there exists some zero knowledge proving scheme to open ECC points that is statistically binding
<j​effro256> (and is efficient)
<j​effro256> In other words, it's probably better to let this issue rest for the moment until better research comes up
<r​brunner7> Hmm, wasn't the idea to "pick some low-hanging fruit right now" and leave more full PQ protection to later iterations? I was thinking about a decision what to do with Carrot in regard of PQ in a few weeks at the latest.
<r​brunner7> But it's possible I got the discussion wrong
<j​effro256> Yes and I already merged most of the low hanging fruit with the amount blinding factor bindings
<r​brunner7> Ah, I see. So it's further along already that I expected. Good.
<r​brunner7> *than
<r​brunner7> Is that already in the current version of the spec?
<j​effro256> Yup!
<r​brunner7> Then this crypto noob here simply missed it :)
<r​brunner7> I intend to make one post about the subject of Carrot and QC and will probably ask away in preparation of that
<j​effro256> Of course !
<j​effro256> Thank you for doing that
<r​brunner7> Welcome!
<r​brunner7> Alright, do we have something special to discuss today beyond these reports?
<j​effro256> jberman: do you want to sync on transaction construction later today now that there's a bit more code on the carrot side?
<j​effro256> Then we can decide whether or not to scrap it
<j​berman> yep, was planning to :)
<r​brunner7> By the way, where does the Rust side stand regarding Carrot? Also basically complete already?
<r​brunner7> I mean the Rust syncing code
<r​brunner7> for Serai
<j​effro256> Ah, I have not started Carrot code for Rust yet
<r​brunner7> That will also fall on your shoulders?
<j​effro256> I was planning to start that once the core repo code hits testnet
<j​effro256> I verbally agreed to it, so yes ;)
<jberman> +1
<r​brunner7> Will probably keep you busy for a while :)
<j​effro256> The carrot code in Rust shouldn't take very long, since that's the easier part
<j​effro256> the scanning is the easier part
<j​effro256> Integration into wallet construction / wallet scanning / transaction signing and the crypographic prototyping I've done such far is the hard part
<j​effro256> After we figure out all these wrinkles, it's just a matter of transcribing
<j​effro256> I hope ;)
<r​brunner7> Interesting. We will see how it goes. Alright, I think we can close the meeting proper here. Thanks for attending everybody, read you again next week!
<s​needlewoods> Thanks everyone
````

# Action History
- Created by: rbrunner7 | 2025-01-24T15:19:20+00:00
- Closed at: 2025-01-27T19:00:36+00:00
