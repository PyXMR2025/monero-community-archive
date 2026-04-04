---
title: Remote Node connections dependent on client mining
source_url: https://github.com/monero-project/monero/issues/3049
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-01-03T04:47:39+00:00'
updated_at: '2023-08-26T17:11:55+00:00'
type: issue
status: closed
closed_at: '2023-08-26T17:11:54+00:00'
---

# Original Description
In the future I'll fill this in with more fanciness, but the idea is that in order for a client to connect and use a remote node, they must submit a proof of work towards a mining effort being performed by the server (remote node).

this would incentivize node operation and take some of the hashrate from conventional pools. 

The mining between client and server is already written in a license friendly fashion in this repo: https://github.com/OhGodAPet/wolf-xmr-miner




# Discussion History
## binaryFate | 2018-01-03T16:11:09+00:00
I had the same idea since a while and I've been discussing it with few people at the CCC to get feedback. So I'm all for it obviously! :)

The rational for me is: I really like the fact that using remote nodes is so practical to onboard new people. I don't think we should rely on keeping this going on purely altruistically in the future, and would rather solidify this mechanism via properly designed economic incentives.   

I was thinking of a "price" advertised on the p2p network by every public remote daemon, which would be a required number of hashes per operations. "Operations" would be for instance the number of blocks the wallet could synchronize; sending N transactions, etc. When running out of "credit" a connected wallet would have to mine again to perform new operations. This has the following advantages:
* We would have a market emerging, with "cheap" nodes (little mining required) that have poor performance and more expensive ones (more mining required) performing better.
* If daemons are run with "--price 0", it is just the same as now; thus backward-compatible.

And just to make clear, before everybody screams, this would be about few seconds of mining (even on a smartphone), so it would be a very low cost for a single person but becomes significant for the node supporting hundreds of wallets. If it is enough to pay for the hardware / VPS at the end of the month, bingo, goal achieved!
  

## fluffypony | 2018-01-03T16:13:47+00:00
I really like this idea. I know of someone that is already refactoring wolf's GPU mining code into Monero, so that part will be sorted.

## Gingeropolous | 2018-01-03T21:17:52+00:00
yes, @binaryFate , thank you for filling in those details!!! I got too tired to get it all out. 

@fluffypony , awesome news on the GPU mining code. Would it be the GPU or CPU that we'd use? I guess phones have both....

But yeah. A market would manifest. Nodes would also have to advertise their specs (or some network measured spec) as well.  Daemons could also advertise how many connection slots they allow, and also the price for persistent connection. I.e. the connection will drop if a particular hash / day isn't achieved. Because a remote node provider ultimately can receive more hash by providing service to more wallet restores than someone who just made a wallet.  

And somehow, an out of band market could crop up. I think I saw @fluffypony mention that in IRC - where you could use monero to buy hash / time on a node, or maybe even fiat.

In general, I'm pretty excited about the idea of using PoW hashes as currency, because they are offchain. 

## binaryFate | 2018-01-04T16:42:45+00:00
> In general, I'm pretty excited about the idea of using PoW hashes as currency, because they are offchain.

Me too. Because this is the only thing new people that we want to onboard can contribute. If you don't even have a wallet yet, you can only contribute computing power.

It's a detail, but if it gets implemented, nodes should have the capability to have (at least) two tiers with different "pricing", depending on the authentication used. The basic use-case that should be supported is people running their own node and not charging themselves or their friends (by authenticating adequately) but charging hashes to everyone else.

## hyc | 2018-01-04T16:49:46+00:00
Sounds like an interesting idea, but ... how many hashes? Is the node going to act like a pool, and accept hashes that are easier than the current network difficulty? What actual value are such hashes to the node operator, if they don't actually yield a block reward?

## binaryFate | 2018-01-04T16:57:11+00:00
> Sounds like an interesting idea, but ... how many hashes? 

Eventually node operators would chose how much they request.

> Is the node going to act like a pool, and accept hashes that are easier than the current network difficulty? 

That is what I had in mind.

> What actual value are such hashes to the node operator, if they don't actually yield a block reward?

Directly, nothing. But it's exactly the same idea as a pool with constant reward (coinhive does that) but instead of a direct monetary reward, you can use the node for a while.
However it's true that the total hashrate for a node operator would probably still be relatively low, and most would never actually find a block to compensate their efforts. Maybe they would need to funnel the hashes to an external pool.
  

## SamsungGalaxyPlayer | 2018-01-04T20:23:07+00:00
I'm trying to see if the benefit is significant.

Suppose a decent node costs $10/mo to run. This means that, at CURRENT price and difficulty, it would need to receive ~125-150 H/s to generate this amount on average. Of course, the required hashes are likely to increase over time with the emission curve and difficulty.

125 H/s comes out to 324,000,000 H/mo, and 150 H/s comes out to 388,800,000 H/mo. For reference, [Coinhive](https://coinhive.com/documentation/captcha) suggests using 1024 hashes for their Captcha. This would mean that 316,406-379,688 people need to perform this work each month. While the hash requirement can be raised (and could even be determined by the nodes themselves), this is still likely to be a high number.

What about the requirement that the client is mining with 1 core while connected to the node? This may be more reasonable.

Could the node easily pass these off to another pool without much overhead? With the current difficulty, the vast majority would not find a block on their own, so I imagine most people would want to use this option.

## binaryFate | 2018-01-04T21:40:38+00:00
> Suppose a decent node costs $10/mo to run

I fear this is quite off when we speak about the main public nodes everyone is relying on at the moment.
Next step IMO is get more precise feedback of the required hardware from operators of the main nodes everybody is relying on at the moment. I have the impression most people are very vague on this. And these nodes are absolute key to the on-boarding process of many people to Monero.

## SamsungGalaxyPlayer | 2018-01-04T21:52:03+00:00
@binaryFate I know that many nodes cost a lot more than this. However, if we had hundreds/thousands of nodes with less capacity, it would help reduce the stress on these important nodes.

## Gingeropolous | 2018-01-04T21:59:16+00:00
@hyc 
> What actual value are such hashes to the node operator, if they don't actually yield a block reward?

They *might* yield a block reward. I mean, its still technically possible for a solo miner to find a block - its all random, right? The idea is to boost the remote node operators solo mining effort. I've currently got 850 connections on my one node. If each of them had to submit, say, 15 hashes / second (which is on the low end for a desktop, and the high end for a phone), thats 12 Kh/s. Thats not great, but its much more likely to find a block than any solo effort that I could pull off on my own. 

And yes, it could be set up to send hashes to an actual pool, but to me this defeats the benefit of mitigating pool centralization. But hey, if more people run nodes, then thats fine too.

## binaryFate | 2018-01-05T21:06:19+00:00
@SamsungGalaxyPlayer
> However, if we had hundreds/thousands of nodes with less capacity, it would help reduce the stress on these important nodes.   
   
Sure, how do we ensure this happens?

## SamsungGalaxyPlayer | 2018-01-05T21:54:24+00:00
@binaryFate it's hard to "ensure" this happens, but let me walk through the logic.

Right now, there are 36 "MoneroWorld" nodes on xmr.be (port 18089). Most of these are very high capacity and expensive to run. They are run as a service to the network.

Suppose there are 1000 monthly users that want to connect to these 36 nodes. That equates to ~28 users per node.

If there was an economic incentive to run a node, even slight, it could increase the number of nodes. Suppose there are now 100 open MoneroWorld nodes, so 10 users per node.

Assuming each user puts the same stress on the nodes, the requirements for these nodes would be lowered by more than half (gross simplification).

Of course, it's possible that one node provider advertises their node to attract attention and get the hashrate.

## Gingeropolous | 2018-01-06T05:07:41+00:00
This actually could be a good reason for us to finally get a baked in p2pool ... though that could be some scope bloat

## hyc | 2018-01-06T06:45:16+00:00
On the notion of thousands of cheap nodes - they're really only good enough for private/personal use. E.g., today we've got ~36GB of blockchain DB. A box with sufficient RAM to cache all of that in memory can serve an arbitrarily large number of clients without getting bogged down (limited only by its network connection). A box with only 1-2GB of RAM would get bogged down very quickly, even if it uses a fast SSD, because multiple clients would all be requesting different parts of the blockchain, completely thrashing what little could be cached in RAM.

## binaryFate | 2018-01-06T23:06:00+00:00
@SamsungGalaxyPlayer
> If there was an economic incentive to run a node, even slight, it could increase the number of nodes

This is precisely what this idea is about! I don't understand what you disagree with (propose to implement nothing?) or what alternative you suggest (another mechanism to ensure we get enough offer of remote nodes for the demand?).

## Gingeropolous | 2018-01-07T05:51:00+00:00
@hyc , cheap nodes - 

> A box with only 1-2GB of RAM would get bogged down very quickly, even if it uses a fast SSD, because multiple clients would all be requesting different parts of the blockchain, completely thrashing what little could be cached in RAM.

Could this be addressed by queuing the requests from multiple remote node connections? I mean, in reality, a wallet needs to refresh upon connection, and then once every n minutes (if the user has it still connected after refreshing and performing whatever was needed). 

## iamsmooth | 2018-01-07T17:28:49+00:00
@hyc 
> today we've got ~36GB of blockchain DB. A box with sufficient RAM to cache all of that in memory can serve an arbitrarily large number of clients without getting bogged down

Far less than that is needed to serve remote clients. A huge amount of it is signatures and range proofs that are of no interest to wallets.  Though that might require reorganizing the database or perhaps some sort of 'optimized remote node' mode to store the 'hot' data in RAM apart from the database itself.

@SamsungGalaxyPlayer 
> What about the requirement that the client is mining with 1 core while connected to the node? This may be more reasonable.
  
This seems perfectly reasonable to me as an alternative to: a) signing up with a node provider and paying a fee, or b) not having a node to use at all because they are all overloaded or have given up on paying a lot of money to provide free service.

With remote users running one (desktop) core you'd only need 3-4 full time users to generate the required $10/month. A cheap $10/mo host might be able to handle >3-4 users even if it can't handle hundreds.

## hyc | 2018-01-07T19:22:36+00:00
@Gingeropolous 
> Could this be addressed by queuing the requests from multiple remote node connections? I mean, in reality, a wallet needs to refresh upon connection, and then once every n minutes (if the user has it still connected after refreshing and performing whatever was needed).

Interesting idea. You could try to queue things up until all the clients hit the same height and then refresh them the rest of the way in lockstep. That's fine for refreshing since it's a linear sweep thru the DB. But if people are also using remote nodes for creating transactions then you also have to serve requests for randomly selected outputs. Again, this will thrash RAM. Also the queueing idea is tough in the first place - do you pause all the existing clients whenever a new one comes along asking to refresh from a lower height, until it catches up to the rest of the clients?

## hyc | 2018-01-07T19:25:52+00:00
Another idea might be clusters of cheap nodes, each advertising only a subsequence of the chain. Clients then connect to different nodes in succession to perform a full refresh, and each node only serves out the subsequence it has cached in RAM. Still it's only viable for refreshing.

## SamsungGalaxyPlayer | 2018-01-08T01:18:29+00:00
@binaryFate I think I'm agreeing with you :)

I just was throwing some numbers out to make sure the incentive is significant enough. It seems like there are two options:

1. Mining with 1 core while connected to a remote node, where less than 10 continuous connections (possibly among several users; the same 10 clients don't need to be connected 24/7) can support a "basic" node.

2. Let's say the maximum number of connections per day on a "basic" node is 100. That means that each client would have to contribute 108,000-129,600 hashes with current price/difficulty/emission. This would take significant time on many machines.

Based on this rough math, I think requiring continuous 1 core mining is the simplest and only reasonable way to have a large enough economic incentive to run a full node. And I think it should be sufficient.

@Gingeropolous @hyc I think deliberations regarding different caching methods should be included in a different issue. Let's keep this one focused.

## Gingeropolous | 2018-01-08T04:26:10+00:00
@SamsungGalaxyPlayer 

>  I think deliberations regarding different caching methods should be included in a different issue. Let's keep this one focused.

Sure. Those points are optimizations that will hopefully happen downstream if this core idea ever gets in.

So I guess in terms of having a viable working version, what are the parameters that are needed?

I like the flag that @binaryFate suggested, --price X . So the question is what does the price get you. Perhaps just per KB of transferred data, because bandwidth is the costly resource here. 

In addition, there needs to be an address to mine to. Perhaps we can use a delimiter. So, the flag would like like
```
--remote-price 200;[xmr-address-here]
```

Of course, now the daemon has to keep a database of users. Perhaps we can hack some of the work that @Snipa22 did for https://github.com/Snipa22/nodejs-pool , because he ended up using LMDB. 

It would be cool if the client (the remote node user) could have an ID so they could send hash from any miner they have, or if they use a different wallet than the one they are mining from. So from the client side, it would be

--remote-node-user XXXXX , where XXXX is perhaps .... I dunno, perhaps a sha256 hash of the users XMR address. 

--remote-node-hash 200

This is the hash per 1kb that the user is offering to pay

Unfortunately, I think the full functionality of this system will require a completely native remote node network as described in #2204  I.e., people don't put node.moneroworld.com in for --daemon-address, but instead use the --remote-node-user flag, and then the daemon scans through the advertised remote nodes that have been pulled from the network, and then matches the client with a node at the right price. But, we don't need to do this now and could move forward with people just advertising nodes out of band. 

On the client side, the client will record the speed at which it is getting data from the remote node, and keep a client-side log of the performance of the node for future reference. 
  

## iamsmooth | 2018-01-08T07:09:50+00:00
> Of course, now the daemon has to keep a database of users

Not users, the whole thing can be done per-connection without any persistent accounting. If you fall too far behind your required hashes (allowance could be 0, this is tbd) delivered on that particular connection, the connection is dropped.

> It would be cool if the client (the remote node user) could have an ID so they could send hash from any miner they have, or if they use a different wallet than the one they are mining from. So from the client side, it would be

This seems way overcomplicated for the initial implementation at least. The simplest approach is to just have the wallet itself mine (initially CPU but the above discussion mentions that GPU mining code is in the works too) and send some hashes. Initially the required H/s on the first deployed nodes using this mode can be low to avoid causing too many problems for people with low performance wallets (by comparison the current required H/s is zero, so anything >0 is an incremental benefit to the node operator relative to the status quo).

None of this precludes a more complex system (possibly partially or entirely out of band) where people can pay for access to nodes in coins, fiat, or hashes. In its simplest form this is just a baseline way for the node operator to get _some_ compensation with low friction. 

## Gingeropolous | 2018-01-08T15:01:21+00:00
> If you fall too far behind your required hashes (allowance could be 0, this is tbd) delivered on that particular connection, the connection is dropped.

So this would be instead of the per kb data transferred that I proposed above? Indeed, because that would require measuring the data transferred per connection.

So for the first implementation, the node operator has a flag 

```
--remote-price 200;[xmr_address]
```

And the client has to provide 200 hashes for every minute of connection. If that isn't met, then the connection is dropped. 

When the client is looking for a remote node, the flag could be something like

```
--remote-pay 200
```

And during the initial RPC connection handshake, if the pay <  price, then the connection is dropped and the client tries to find another one. 

The client will have to have some internal ability to see how many hashes it can offer - I imagine some part of the GUI that is used to set this up will have a "test hashrate" function, to see what is the maximum offer the client can provide. 

## SamsungGalaxyPlayer | 2018-01-08T16:33:24+00:00
@Gingeropolous I'm thinking of something even simpler. I imagine most people don't know what their hashrate is.

The node host could use a remote price as you stated, but I suggest asking for the average hashes per second to make things extremely simple to the user. It can be tested over 1 minute, but the user doesn't need to see that. So something like `--remote-price 5;[xmr_address]`.

When the client is looking for a remote node, they can offer to use a certain number of *threads*. I think this makes a lot more sense than trying to set a certain number of hashes. I don't think any mining software supports mining at a certain hashrate. It would look something like this: `--remote-pay 1` to mine with 1 thread.
  

## iamsmooth | 2018-01-08T18:03:31+00:00
@Gingeropolous 
> So this would be instead of the per kb data transferred that I proposed above? Indeed, because that would require measuring the data transferred per connection

I don't understand question. My suggestion would require measuring the data _per connection_, just not _per user_ (so no need for user logins, which are privacy-impairing anyway). Whether that is per minute or per-kb transferred was not specified.

@SamsungGalaxyPlayer EDIT: Never mind what I wrote. I see now that you were suggesting "threads" as UI for the client, which is fine. The software can handle any required estimation of the hash rate and conversion of that into a price in hashes-per-whatever.

I would just let the node operator set a minimum hashes minute or per kb (or maybe both; if you don't meet the generally-lower per-minute requirement, you get dropped, and if you don't meet the per-kb requirement you get throttled). There is no reason this cant be set very low initially to provide wide service. Later there are various ways to approach offering service at a higher price (that won't be achievable by everyone) it such as throttling, alternate methods of payment, different ports with high/low performance service, etc. 
  

## Gingeropolous | 2018-01-08T19:32:03+00:00
@iamsmooth , sorry, I didn't understand your statement. Now i do. 

@SamsungGalaxyPlayer , sure, threads make sense for the initial implementation. Most people don't know what there hashrate is, but I would imagine its trivial for the software to figure that out. And minimum hashes per second also makes sense in terms of the server price, averaged out over a minute. 

For the record, most mining software does offer the ability to modify the hashrate - this is done with an intensity setting (at least for GPUs). Furthermore, if we found a way to make it so the client does the bare minimum number of hashes (which could be doable with intensity settings etc), this would save the client from doing too much work. Because even 1 thread on a phone could be particularly power draining and heat producing (I think, I don't usually mine on my phone) 

On second though, I don't know how well the thread offer will function in an auto-selecting marketplace.... the client will have to know their hashrate so they know which servers to even bother trying to connect to. Otherwise, the client has to connect, try mining, and then get booted if their hashrate is below what is required by the server. 

## iamsmooth | 2018-01-09T06:15:18+00:00
Probably any mining on a phone (if on battery at least) is going to be too power draining. That might be okay for a really quick session but probably phones need another solution. That takes nothing away from this idea though, just because it does't solve the problem for every situation.

BTW, I thought of an enhancement idea which is to allow the user to specify an address to which mining rewards corresponding to any _extra_ hashes in excess of the price would be banked for future use (for example from your phone!) and/or paid out (if meeting some minimum payout threshold), making it attractive for those with higher end computers to mine more than the minimum. That makes each public node a sort of small mining pool. The node operator benefits because more hash rate means it is faster to find blocks. 

Trust is needed of course but I guess at least some public nodes would be operated by well known entities with some trust.

Some risk that these 'small' mining pools could become big, which I guess is no worse than the status quo.
  

## Gingeropolous | 2018-01-09T13:19:37+00:00
> BTW, I thought of an enhancement idea which is to allow the user to specify an address to which mining rewards corresponding to any extra hashes in excess of the price would be banked for future use 

Yeah - this is what I was getting at when I mentioned needing a database system with a user ID etc etc, so its kinda like a pool. I would probably include some type of decay though, where a node user can't just mine 1 million hashes and then never mine again - though that could be up to the node operator. 

## krtschmr | 2018-06-20T10:54:07+00:00
i think the issue is that we can't get the wallet running in windows as it would include miner code and for that reason defender will block and/or remove the file.

## Gingeropolous | 2023-08-26T17:11:54+00:00
I'm pretty sure this was implemented with RPC-pay #5357  , 

( which was then removed from the wallet #8724 

good times. You will rise again, glorious micropayment system, once monero is the worlds money. 

# Action History
- Created by: Gingeropolous | 2018-01-03T04:47:39+00:00
- Closed at: 2023-08-26T17:11:54+00:00
