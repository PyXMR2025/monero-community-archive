---
title: '[Feature Request] Remote node service advertising and remote refreshing through
  daemon'
source_url: https://github.com/monero-project/monero/issues/2204
author: Gingeropolous
assignees: []
labels:
- proposal
created_at: '2017-07-25T12:08:12+00:00'
updated_at: '2022-04-08T13:22:17+00:00'
type: issue
status: closed
closed_at: '2022-04-08T13:22:17+00:00'
---

# Original Description
# Monero Bootstrapping Server and Client Expected Behavior

## Rationale

Network synchronization takes forever and will continue to take even longer. The network survives because users run nodes that run the monero p2p protocol. Users may be discouraged to run nodes if the software does not provide a useful user experience. A useful user experience, in the context of Monero, is software that allows a user to send and receive monero. Here, we outline a bootstrapping protocol for new users where the user is able to use the monero network semi-instantaneously while the node is synchronizing. In theory, this will encourage more users to run the actual node software instead of finding faster alternatives like light clients. Thus, although the functionality is at first light wallet-like, the node eventually matures.

Ultimately, the goal is to get the user to keep turning their monero software on so that the node can synchronize and function as a peer. This will only happen if the monero software is useful to the user. 

## Current state
Currently, remote nodes are organized as a service via moneroworld.com , either via a round robin DNS entry or a list of IPs that are identified on the monero network by running a script to detect responsive 18089 ports. The first is centralized, the second is semi-centralized because anyone can run the script, but no one does. 

## Preamble

The following description has a primary narrative with some points have different designs, listed as A) functional B) better C) best. 

## Server Side (monero daemon. service provider)

User sets a flag when loading their daemon (e.g., --offer-bootstrap 18089;1) which binds the rpc port 18089 and sets the --restricted-rpc value to true. Value after the ; is a throttle flag. Will allow the user to set the amount of service they are providing. Throttle flag definitions are to be determined, but can be rate limiting, number of connection limiting, etc.  

This flag sets a p2p support flag to indicate that the node is offering bootstrapping services. 

## Client side (monero daemon, monero wallet - both CLI and GUI. service user)


### Daemon behavior
The user loads their daemon normally without any flags. The daemon begins network synchronization like normal. Daemon gets peer lists like normal, but now peer lists have a new support flag.

### Wallet behavior
User loads the wallet. The wallet connects to the local daemon. The wallet informs the user tha tthe daemon still needs to fully synchronize with the network, but a bootstrapping service is available. Wallet has a brief mention of risks involved. User decides whether to accept. If the user accepts, the following happens. 

1. Bootstrap node discovery: The Wallet instructs the daemon to find bootstrap nodes. These are nodes from the peer list with the p2p support flag. The daemon now has an index of these nodes. The daemon quickly checks each of these nodes with an rpc request for blockheight. The nodes that respond are considered active nodes. 

2. Bootstrapping service node selection: Design decision point  
Option A - the daemon selects one of these nodes at random and uses it for bootstrap.
Option B - the daemon compares the block heights of all of the active nodes and evaluates consensus amongst them (e.g., 8 out of 10 nodes say blockheight X, whereas the other 2 say blockeight Y). Daemon picks a random node from one of the consensus nodes for bootstrap service. 
Option C - the daemon picks multiple nodes either from consensus pool or active pool, and uses multiple for bootstrap service.

3. Data piping - Having selected a node, the daemon then pipes the data from that node to the wallet as if the users daemon itself was serving the wallet. 

4. Wallet refresh - The user now has a refreshed wallet. In most first user cases, this is the stopping point. The user now sees that there monero has arrived and they are now their own bank. Most users will stop needing to perform any actions at this point, and the daemon will continue to synchronize with the network. 

5. Bootstrap usage warning - If the user needs to perform a transaction at this point, a warning is presented to the user detailing the bootstrapped nature of their monero network connection. Explicitly, they are trusting a third party. 

6. Transaction formation: Design decision point
Option A - the daemon and wallet interact with the bootstrap node(s) exactly how the current remote node system works. When the user creates a transaction, the users software requests random outputs from the bootstrap node, just like the current remote node setup. 
Option B - The daemon requests random blockchain regions from the bootstrap node(s) and stores them in a database for future use. 
Option C - The daemon receives the header chain from multiple nodes (can be either bootstrap service providers or regular nodes), and performs hash validation of the header chain. Once the header chain is validated, the daemon requests block hashes from multiple nodes to create a new collection of hash-validated nodes. From theese hash validated nodes, the daemon starts populating a database with block information that is hash validated. These data can then be re-used during the normal synchronization process. 

7.  Transaction broadcast: the wallet crafts a transaction like normal and pushes it to the daemon like normal and the daemon broadcasts it to the network like normal (because the daemon has connected to a bunch of peers by now, even though its still synchronizing from them)

#### Wallet behavior after period of disconnection

A user may disconnect from the network for a long time, such that their node is no longer synchronized. The software should be able to recognize this, and decide (dependent on number of blocks required for full synchronization) whether to wait for the node to synchronize or re-bootstrap. 

credits go to everyone. 

# Discussion History
## hyc | 2017-07-25T12:18:20+00:00
Sounds workable. In this case, the local daemon is simply acting as a wallet-RPC proxy. It will simply pass through the local wallet's requests and the remote node's responses without validating or storing the results. (Possibly it could store received blocks in a secondary structure, and use them when it catches up to that height. May not be worth the bother; for a newly created wallet there will be very few blocks fetched, if any.)

## thinkier | 2017-08-07T03:53:30+00:00
Dibs on HTTPS support.

## Jaqueeee | 2017-08-07T21:55:11+00:00
I'm implementing a "light" version of this in the GUI where the user can opt-in to use a remote node while the local node is syncing. When sync is finished, GUI switches over to use the local daemon instead. All this is client side, and local node isn't aware that the wallet is using a remote node. 

Maybe that's enough for this use case? Or is it really worth implementing this on a node level? As @hyc said, for a new wallet, data that can be reused by the daemon is almost negligible. 

+proposal

## Gingeropolous | 2017-08-11T00:31:03+00:00
@Jaqueeee  - hopefully, people will continue to be onboarded onto monero until the end of time, and block chain sync will only become longer and longer. Thus, I think bootstrapping will provide more and more of a benefit.

>  Or is it really worth implementing this on a node level? 

I think it is - otherwise, it relies on a centralized service to bootstrap new users, which is a nice and easy attack service. 




## hyc | 2017-08-11T18:52:00+00:00
I agree, at node level would be good. But this proposal needs to be fleshed out a little more. Is it only good for synching up a wallet, and not for any other wallet usage? I.e., you couldn't use this approach to send transactions?



## Gingeropolous | 2017-08-15T19:09:32+00:00
@hyc 

> I.e., you couldn't use this approach to send transactions?

that seems logical. In this scenario, you already have a daemon that is connected to the p2p network, you just dont have a blockchain. 

## hyc | 2017-08-15T19:11:38+00:00
OK, but that leaves us with a deceptive situation - the wallet will be fully synced with the network, but if you try to create a transaction and ask your local daemon for outputs to mix with, you'll only be getting very old outputs.

## Gingeropolous | 2017-08-15T19:14:57+00:00
Ah, i got caught up in semantics. You wrote "send transactions".... which breaks apart into transaction formation and transaction broadcast. So yeah, formation would still require remote data, but broadcast doesnt need the remote node.

if we want to get fancy, this is the point where a "bootstrapped node" could request random chunks of blockchain from the peer its leaching the wallet refresh from, and then pick outputs from that

## Jaqueeee | 2017-08-15T19:22:02+00:00
Picking outputs from remote node, submitting thru local node sounds like a solution that could make it into this release. Proper node integration would have to wait until next. 

## Gingeropolous | 2017-08-15T19:31:19+00:00
@hyc suggested on IRC

> hyc> gingeropolous: #2204 really needs an explicit list of actions and expected behaviors

So I will try to update the first post with those details. 

## Gingeropolous | 2017-08-18T03:17:19+00:00
the OP might be more rambly than you imagined it should be @hyc , but i dood it

## hyc | 2017-08-18T10:47:36+00:00
@Gingeropolous looks like a copy/paste error in your paragraph 5.

## QuickBASIC | 2017-09-06T19:22:57+00:00
> Picking outputs from remote node, submitting thru local node sounds like a solution that could make it into this release. Proper node integration would have to wait until next.

Forgive me if this question is due to my ignorance, but wouldn't that mean that the node that you get the outputs from would know which outputs in your transaction that are the dummies? Isn't the whole point of having the blockchain locally... making sure that the outputs my wallet select are indistinguishable from my own output. (The transaction is signed such that any one of the keys could be the actual signer.)

Even if you asked a different node for each output, someone running a multitude of modified nodes (unbeknownst to the rest of the network)  could keep track of and know which outputs are the dummies and that would reduce the privacy set of my transaction dramatically.

## hyc | 2017-09-06T19:46:09+00:00
The wallet could ask the remote node for *your* output too. Then the remote node won't know which is the real one.

## Gingeropolous | 2017-11-07T01:16:49+00:00
Adding this reference here, because relevant: https://getmonero.org/2017/03/26/overview-and-logs-for-the-dev-meeting-held-on-2017-03-26.html

## MonkofCoin | 2017-11-15T19:19:06+00:00
I couldnt tell from the logs, is this proposal still possibly going to be implemented?

## Gingeropolous | 2017-12-19T18:10:00+00:00
Monero runs on C4 ... if someone codes it up and makes a pull request it'll get merged, or at least discussed

## Gingeropolous | 2018-01-28T05:42:33+00:00
After extension discussion, the painfully obvious fact was brought forward that the self-scanning script proposed as part of this feature has an implicit trust model that is incompatible with core software implementation. 

As such, PR #3165 is possibly the best workable solution to provide the bootstrapping functionality in the core software but still require a user-initiated shift in the trust model. 

I still hold out hope that there's some way that I don't fully understand wherein a remote node can be trusted enough via some mechanism, but I dunno. .. edited to add, like a header chain check

## ThomasFreedman | 2018-11-18T14:39:09+00:00
Why is SPV not useful for Monero?

## Gingeropolous | 2022-04-08T13:22:17+00:00
wow, look at all that rambling from 5 years ago.





# Action History
- Created by: Gingeropolous | 2017-07-25T12:08:12+00:00
- Closed at: 2022-04-08T13:22:17+00:00
