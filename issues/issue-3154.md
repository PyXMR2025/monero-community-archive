---
title: Double-blob transitions for new tech
source_url: https://github.com/monero-project/monero/issues/3154
author: Gingeropolous
assignees: []
labels:
- proposal
created_at: '2018-01-18T18:54:57+00:00'
updated_at: '2018-09-14T13:23:51+00:00'
type: issue
status: closed
closed_at: '2018-09-14T13:23:51+00:00'
---

# Original Description
# Double-blob transitions for new tech

## Rationale

Improvements occur in monero at an incredible pace. For instance, the new bulletproofs are an example of an optimization that is very new in the cryptography world, yet has been integrated into the monero source code and is ready for deployment. Due to the novel nature of this tech, there is uncertainty. There are obvious reasons to integrate it quickly (reduces blockchain bloat), but there are also obvious reasons to wait until the implementation has received adequate reviews. 

## We can have our cake and eat it too

Here I propose what I have called the double-blob, which buys us more time to review the implementation but also reduces blockchain bloat.

## The double blob

Simply put, we can include both the trusted Borromean proof (here called O, for old) and the new Bullet proof (here called N, for new) in the transaction data. Thus, each transaction will contain the transaction data (here called T) and both proofs, so a transaction will look like this: T-O-N. For simplicities sake, we'll put all of these transcactions into a block called B, and so a block would look like BON.

During the double blob period, transactions are made with both proofs. Once Bullet proofs become as trusted as borromean, we drop the borromean from the transaction data and keep the bullet.

here it is in ASCII art, where each entity between the dashes is a block

BO-BO-BO-BO-BO

This above is the existing chain, where the proof is O.

BO-BO-BO-BO-BO^BON-BON-BON-BON-BON

At the carrot (^), the chain forked, so now each transaction has an old proof (O = borromean) and a new proof (N=bulletproof).

BO-BO-BO-BO-BO^BON-BON-BON-BON-BON-BON-BON-BON^BN-BN-BN-BN-BN-BN

A lot of time has passed using the double blob, and bulletproofs become trusted. Thus, the chain forks again, and the double blob is dropped, and transactions are only made with the new proof (N=bulletproof)

Now, here's where it gets cool. We can take the chain and remove the borromean from the BON blocks *but still keep the chain fully verifiable!!!*. This is why it is called lossless pruning. 

BO-BO-BO-BO-BO^BN-BN-BN-BN-BN-BN-BN-BN^BN-BN-BN-BN-BN-BN

You can see in the above, after the original double-blob fork height, the blocks now only contain the new bulletproof.

## Practical matters

This lossless pruning can occur in a couple different fashions. A node can choose to prune them and they are gone forever. Optionally, after the second fork date, synchronizing nodes can request only the bulletproof data, so the source node still contains the borromean, but it only delivers the bulletproof. 

## Cost

During the double-blob era, there is an increased storage for the extra bulletproof. So ultimately, we add 10% (2.5 kb added to a 13 kb normal borromean transaction to get 15 kb) to be able to remove 80% later (15 kb transaction reduced to 2.5 kb).

During the double blob era, there could be an increased cost for verifying the bulletproof. *HOWEVER*, it may not even be necessary to verify the bulletproof, because we are still relying on the borromean for validity. The bulletproof is really just a compression that we initiate later after its trusted.  

As mentioned by @moneromooo , the transaction hash for a double blob transaction will need to include both the hash of the borromean and the bulletproof. So the double blob era will result in an extra 64 bits of data per transaction (which is a drop in the bucket compared to the borromean that we can drop entirely)

## Conclusion

Here I propose a way that the Monero blockchain/network can gain the benefits of new technology (here, reduced blockchain bloat) before the new technology is fully trusted. In this case, it is presented to offset the novel nature of bulletproofs, but it can also be applied to other improvements in the monero protocol as they come. Hopefully, a mechanism like the one described will permit the Monero network to be at the forefront of technological advancement, without the risks of using "fresh" cryptography and maths. 

The old proverb of "a man with two watches never knows what time it is" ... is flawed. If the man started with one watch that he trusted, and then bought a second watch, and then determined whether the second watch is as trustworthy as the first watch... then man can trust both watches and choose to get rid of the old one. 

+proposal

dunno if i have permissions for these flags but thought I'd try

# Discussion History
## dEBRUYNE-1 | 2018-01-18T23:53:39+00:00
+proposal

## moneromooo-monero | 2018-09-14T12:08:31+00:00
The man with three watches can use a voting protocol.

## fluffypony | 2018-09-14T12:11:37+00:00
I think we have a high degree of confidence for Bulletproofs, but moving forward this is a nice way to rapidly roll something out. After a period, say 24 months, the old stuff can be discarded as the new stuff is deemed sound. Similarly, if a bug is found then the new stuff can be discarded. It won’t work for everything but it’s certainly a nice design to keep in mind.

## fluffypony | 2018-09-14T12:13:18+00:00
This is similar to the approach Google took with post-quantum TLS: https://security.googleblog.com/2016/07/experimenting-with-post-quantum.html

## Gingeropolous | 2018-09-14T13:23:51+00:00
So I guess the issues closed?

Always good to know I can reinvent the wheel. :)

# Action History
- Created by: Gingeropolous | 2018-01-18T18:54:57+00:00
- Closed at: 2018-09-14T13:23:51+00:00
