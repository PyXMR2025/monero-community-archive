---
title: 'Monero Tech Meeting #125 - Monday, 2025-06-16, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1221
author: rbrunner7
assignees: []
labels: []
created_at: '2025-06-13T19:17:20+00:00'
updated_at: '2025-06-16T18:24:22+00:00'
type: issue
status: closed
closed_at: '2025-06-16T18:24:22+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1218).


# Discussion History
## rbrunner7 | 2025-06-16T18:24:22+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1221
<r​ucknium> Hi
<j​berman> *waves*
<r​brunner7> While we wait, and before I forget, let me propose that after today we meet again in **two** weeks, because of the MoneroKon weekend
<rottenwheel> +1
<r​brunner7> Alright, any reports about last week?
<s​needlewoods> hey
<s​needlewoods> lots of real life, no beach time, but made a little progress on the CLI
<j​berman> Nothing significant to report. Still continuing current open tasks (FFI cleanup, open PR fixups, PR review). I also started on supporting >8-input txs. In a past meeting, I shared some thinking behind the idea to group multiple FCMP++ proofs into 1 tx where each proof has a max of 8-inputs, primarily to avoid txs taking minutes to construct (so that even 128-input txs take seconds<clipped messag
<j​berman>  instead of minutes). I started dabbling in changes for that approach
<r​brunner7> So only the size goes up considerably, but not construction time as well?
<r​brunner7> The size of the tx
<j​berman> Correct
<r​brunner7> Certainly a worthwhile approach to think through
<r​brunner7> Just gives a whole new "hierarchical level" to transactions, and sometimes such new levels are a bit expensive to implement ...
<j​berman> Link to a past MRL meeting where I initially brought this up too: https://github.com/monero-project/meta/issues/1200
<r​brunner7> I somehow missed that idea ... never mind.
<r​brunner7> Ok, looks like that's it already about reports. Anything else to discuss today?
<r​ucknium> I wanted to ask jeffro256  if he thinks it's OK to disclose the spy node detection method at MoneroKon. I don't intend to rush anything, but it would be an opportunity to do so.
<r​brunner7> Not to discuss, but maybe interesting to mention, if you didn't see it already: It looks that at long last, somebody started to implement someting like a "layer 2" on top of the Monero blockchain in earnest. It's called *Grease* and made quite some waves already on Reddit.
<r​brunner7> I think there will be a presentation about it at MoneroKon
<rottenwheel> +1
<r​brunner7> I am very curious how that will turn out
<rottenwheel> +1
<r​ucknium> IIRC, someone said, late last year, that a project was looking for Rust developers for a Monero payment channel implementation. Probably, Grease is that project.
<r​brunner7> Ok, the gras was whispering already back then :)
<r​brunner7> I think somebody mentioned that so far it's two devs. Pretty big job for a duo
<j​berman> wonder how they deal with Monero's lack of HTLC-equivalent
<r​brunner7> In 1 week we will probably know
<r​brunner7> I am always a bit uneasy when people hear "L2" and immediately and without much questioning attribute almost magical properties to that thing ...
<r​brunner7> I as the old skeptic that I am
<s​needlewoods> I saw this in bounties today https://bounties.monero.social/posts/192/0-000m-creat-a-payment-channel-for-monero-based-in-monet-and-auxchannel
<s​needlewoods> haven't read the links yet
<r​brunner7> Hmm, looks a bit controversial, and a bit late frankly
<r​brunner7> Ok, looks like we can close already for today. Happy trip if you should travel to Prague, and read you again in **two** weeks!
<rucknium> +1
<r​ucknium> They have some docs here: https://github.com/grease-xmr/grease
<r​ucknium> https://github.com/grease-xmr/grease/blob/main/docs/introduction.md
<s​needlewoods> thanks, cu
<r​brunner7> Yes, so far I was just lazy to read those carefully, putting my hope on an easy-to-digest presentation
````


# Action History
- Created by: rbrunner7 | 2025-06-13T19:17:20+00:00
- Closed at: 2025-06-16T18:24:22+00:00
