---
title: 'Idea: RID - Address database when Jamtis'
source_url: https://github.com/monero-project/monero/issues/8681
author: Gingeropolous
assignees: []
labels: []
created_at: '2022-12-18T12:33:37+00:00'
updated_at: '2022-12-19T00:56:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
So during the discussion of the Jamtis RID, someone (jokingly?) suggested a decentralized RID-Address database. 
Such that you could just enter the RID into the monero wallet, and the network would return the address for that RID.
I sorta went with it to see how it could be done.

I personally think the RIDs are a great advancement for the monero ecosystem. Yes, generally, you are able to snap a QR code
or simply copy and paste a gigantic address. But we're humans, and being able to simply write down your monero address for
any reason would be useful, in addition to being able to use your own eyeballs to compare written address.
Because otherwise stuff will probably be built out to make things "easier" for users but sacrifice privacy, permissionless, and decentralization. 

## This is from the perspective of a node.

Abrevation: RID-Address pair = RAP
Simplification of RID concept: hash[address] = RID

Your a node. You have a database of RID-Address pairs (RAPs). A request comes in from a random node [requester] "Do you have an address for this RID?". 

If you don't have the address, you send the same request to a random node [inquiry node] that you are connected to or from your node lists. You make a RAP entry for that RID, without the address. Eventually, the peer you sent the request to [inquiry] will return the address for the RID. You verify the integrity of the RAP such that hash(received address) = the RID you were requesting. You update your RAP database with the RID for that address, and then send that address to the [requestor].

If the [inquiry node] returns a RAP where hash (received address) != RID, you drop that node as a connection.

If you do have the address, you wait random seconds [wait1] and then return the address for that RID to the [requester]. [wait1] is a random delay such that the requesting node can't conclude that you are the node that actually had the data. 

Your database is large, but its not infinite. You store perhaps 1GB worth of RAPs. As requests and data come in, old RAPs will get deleted, and new ones are put on top. 

# How do RAPs get out into the network?

A user can run a node, and one of the new functions of running a node is to seed these RAPs. At random intervals (spanning .. months?), a node will broadcast (using Dandelion++) a RAP that is packaged with a PoW. Other nodes would see this incoming RAP and, depending on their local DB conditions, add the RAP to their database. This also provides a new incentive for running a node, because if a user is actively running a node, they can ensure that all they need to use is their RID. The relay protocol might be a bit different than Dandelion++, because I'm not sure if the best thing is to fluff at the end. It could just be an endless stem... ?

Miners can also store RAPs in the block header of blocks they find. This provides incentive for users to solo mine. Because if they find a block, they can always just use the RID for their transactions when requesting monero payment, because every monero node will now have a record of which address goes with that RID (until the end of time really). This could create economies for putting RAPs into block headers. A reasonable limit of RAPs per block could be implemented, or it could just follow the existing economics of block space. 

# All right, lets try to poke some holes in it.

So obviously there's the problem of IP association with a given RAP. Using the stem-like process from Dandelion, it should be equally as difficult to pinpoint the originator of the RAP seeding. However, unlike tx broadcast, the stakes are higher because a monero address is now associated with an IP... although addresses don't show up on the blockchain, so its not like the attacker could then monitor for txs. 

There's also the chain bloat for the approach of storing RAPs in block headers. Though they could be pruned if a user needs an absolulte minimal disk footprint. 

Comparing this to DNS solutions for namespace things, with this approach you don't need the ability to either run a DNS server and/or procure a domain name. 

Regarding the land-grab problem, an attacker could fill the network with fake RAPs, though becuase an RID is calculated from an address, they would be valid RAPs, they just wouldn't be useful. An attacker could operate a bunch of RAP seeders to flood the network. Perhaps part of the RAP seeding protocol (for the initiator of the seeding process) would be to perform a PoW. Thus, the seeder would have to hit a certain difficulty (perahps dynamic, based on the main difficulty to prevent magic numbers), and perhaps this effort could be merge-mined with finding a monero block itself, with a RAP in the header. This would ultimatley lead to more users having their RAPs embedded in the blockchain, which would reduce the overall noise and volume of the RAP chatter on the network. 

Dead addresses - it will be probable that users will deprecate their monero accounts. In the case of the blockchain-stored RAPs, the only problem is wasted space. In the case of a seeder, the user just stops seeding that RAP. Over time, the RAP databases of the network will forget the deprecated address. 

The hash(address) == RID verification could be a DOS vector, wherein a malicious peer could send a bad pair, and force the honest peer to verify the RAP. Each malicious IP could only get 1 attempt at this because they would be dropped as a connection. I guess it depends on how costly that calculation is. Though this would give another push to create a PoW for establishing a connection. 

ok, I think I've run out of thought tracks for this one at the moment. 

# Discussion History
## tevador | 2022-12-18T14:30:07+00:00
I thought about this some time ago. There is a much better way to do it that does not reveal the actual address to anyone except the person who knows the RID.

It uses something called [convergent encryption](https://en.wikipedia.org/wiki/Convergent_encryption). Essentially, it uses the RID as an encryption key and the look-up key is the hash of the RID. To "upload" an address, you do do the following:

1. Calculate `RID = hash(address)`
2. Calculate `LUID = hash(RID)`
3. `encrypted_addr = encrypt(address, RID)`
4. Upload `(LUID, encrypted_addr)` to the network.

To retrieve an address that corresponds to a specific RID:

1. Calculate `LUID = hash(RID)`
2. Make a request to the network to retrieve the `encrypted_address` corresponding to `LUID`.
3. `address = decrypt(encrypted_address, RID)`
4. Check that `RID ?= hash(address)`

Participants in the P2P network do not learn the addresses or RIDs they are storing and they cannot modify the encrypted addresses. They can still avoid storing duplicate addresses because those will have the same LUID.

## SChernykh | 2022-12-18T14:44:27+00:00
There is already https://en.wikipedia.org/wiki/Distributed_hash_table for this, and it's possible to use BitTorrent's DHT for this (millions of active nodes already).

## Gingeropolous | 2022-12-19T00:56:43+00:00
word. Well it seems there's not really an issue with having huge addresses if there are various ways to get these RID-Address pairs out there. 

# Action History
- Created by: Gingeropolous | 2022-12-18T12:33:37+00:00
