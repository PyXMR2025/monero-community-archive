---
title: 'Monero Tech Meeting #170 - Monday, 2026-05-18, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1390
author: rbrunner7
assignees: []
labels: []
created_at: '2026-05-15T14:14:42+00:00'
updated_at: '2026-05-18T18:30:17+00:00'
type: issue
status: closed
closed_at: '2026-05-18T18:30:16+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1385).


# Discussion History
## rbrunner7 | 2026-05-18T18:30:17+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1390
<jpk68> Hello
<vtnerd> Hi
<jeffro256> Howdy 
<UkoeHB> Hi
<rbrunner7> Alright. Let's start with the reports about last week.
<rbrunner7> @jberman:monero.social reported before the meeting: "My update in advance: worked on diagnosing a stressnet-specific chain split, and patching / investigating other observed issues on the stessnet. I'm personally OK with moving forward with @jeffro256's patch for the chain split here: https://github.com/seraphis-migration/monero/pull/391"
<sneedlewoods> Hey
<rbrunner7> Me: Polyseed. To my surprise noticed only yesterday that monero-wallet-rpc also deals with seeds :)
<jeffro256> Me: trying to salvage the stressnet chain state, hot/cold stuff, knowledge proof stuff, and RPC improvements 
<vtnerd> Me: working on updating lws and lwsf patches for some minor changes to upstream code. This includes the curve tree serialization and rename of a carrot function 
<jpk68> Me: did some work on the main I2P integration PR; submitted a few patches related to Tor addresses and the build system; got some minor FCMP++ Rust build optimizations merged
<sneedlewoods> I was all over the place, now working on the restore height approximation again
<rbrunner7> @jeffro256:monero.social: What do you mean with "salvage the stressnet chain state"?
<koe000> me: multisig wip
<jeffro256> @rbrunner7:monero.social: there's a temporary fork in the network , I'm working on a fix which may or may not merge them
<rbrunner7> Ok :)
<rbrunner7> You mean right now we have two competing stressnets?
<rbrunner7> Do they have some consensus related disagreements?
<jeffro256> Yep ! 
<jeffro256> The block weight cache is different b/t them which in turn affects the coinbase tx reward 
<rbrunner7> @vtnerd:monero.social: By the way, is there any estimate about some first "production version" for lws? Or will this be some very gradual process, the software just becoming better and better?
<rbrunner7> Cool. So interesting case of chain split, interesting to study I guess
<ofrnxmr> @rbrunner7: 1.0 is either out or being prepared
<ofrnxmr> (and lws in use by edge wallet)
<rbrunner7> Well, if it's out, that was one stealth release :)
<rbrunner7> Where are the trumpets and the fanfares and the big applause
<rbrunner7> No, seriously, I see this as quite some milestone worthy of proper attention
<ofrnxmr> @rbrunner7: I think prepared. I dont aee 1.0 branch. Cant rememeber where i read about it - maybe a ccs update?
<rbrunner7> Anyway, good to hear that it's close.
<rbrunner7> So if I hop onto stressnet it's more or less random which of the two chains my daemon will chase down, right?
<jeffro256>  No necessarily 
<jeffro256> *not
<ofrnxmr> There were 10 competing chains at a specific height, but most nodes that got past that roadblock ended up on the same chain
<jeffro256> If you never restart, then you will be on the "main" chain. Or if you pop blocks then sync. If you restart your node tho, then you effectively fork from the network wherever you stopped 
<rbrunner7> The joys of beta testing
<jeffro256> Lol yeah except that it an issue which would never appeared on mainnet lol 
<ofrnxmr> So the nodes that synced past the roadblock, are on a non-consensus fork?
<ofrnxmr> If you didnt restart, the node just gkt stuck afaict
<rbrunner7> Not sure. I think moneromooo once tried to chase down a rare problem where daemons did not agree regarding, what was it, longtime difficulty average?
<rbrunner7> Anyway, that what testing is for. After all, stressnet could just crash and burn. It holds instead - more or less ...
<rbrunner7> Alright, after these reports, do we have something to discuss today?
<jeffro256> @ofrnxmr: There's not necessarily any single roadblock. The road block is every block if you restart your node 
<rbrunner7> A thousand blooming networks, cool
<rbrunner7> Looks like we are through. Short meeting, but with good attendance, which is nice. Thanks everybody, read you again next week!
<sneedlewoods> thanks everyone, see you
<jeffro256> @ofrnxmr: Depends on what you mean by non-consensus. It wasn't an intended consensus rule, but it is what it is. AFAICT, the fork which currently has the most PoW is the fork that all nodes can converge onto if they apply #391, and #391 works as intended
<jpk68> Thanks
<jeffro256> Thanks everyone
````


# Action History
- Created by: rbrunner7 | 2026-05-15T14:14:42+00:00
- Closed at: 2026-05-18T18:30:16+00:00
