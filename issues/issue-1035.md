---
title: 'Seraphis wallet workgroup meeting #77 - Monday, 2024-07-08, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1035
author: rbrunner7
assignees: []
labels: []
created_at: '2024-07-05T14:17:12+00:00'
updated_at: '2024-07-08T18:58:45+00:00'
type: issue
status: closed
closed_at: '2024-07-08T18:58:45+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1031

# Discussion History
## rbrunner7 | 2024-07-08T18:58:45+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1035
<s​needlewoods> hey
<jberman> *waves*
<j​effro256> Howdy
<r​brunner7> dangerousfreedom said he will join again next week ...
<r​brunner7> Still busy, it seems
<r​brunner7> So, any reports from last week?
<s​needlewoods> still working on missing API functions, but had a busy week too so not too much progress
<r​brunner7> They have to miss a little longer :)
<j​effro256> Dumped the idea of integrating the subaddress gap fix before FCMPs , and went back to working on Jamis RCT
<r​brunner7> Too big, basically?
<jberman> me: the updated trim_tree algo impl is working/tests passing, cleaning it up and implementing the db side this week. Next fcmp task is db migration placing current outputs in the tree
<r​brunner7> Do all existing enotes go into that tree? Thanks to compatibility?
<jberman> yep
<r​brunner7> Nice. No more whining about too small a privacy set, or how you call that
<r​brunner7> Wonder how much bigger that will make the blockchain file
<j​effro256> Yup too big and once FCMPs deploy, we have to store every single key image on the chain until we find a subaddress spend pubkey for an enote which missed the table. Similar problem as background view wallets currently , but we don't know beforehand of we are guaranteed to recover it
<r​brunner7> Alright, so I guess that problem also can wait a while longer for a solution.
<r​brunner7> People over in -communiy speculated a bit today about the ETA of the hardfork to FCMPs, by the way
<r​brunner7> *-community
<r​brunner7> It's on the radar :)
<jberman> "Wonder how much bigger that will make the blockchain file" -> ~100 bytes * ~100mn current enotes = ~10gb 
<r​brunner7> Anything in particular to discuss today? I was thinking to talk about "parcelling" the work on the wallet, but I think without dangerousfreedom present that's probably not yet a good time
<jberman> guess we're approaching 110mn enotes now, so we'll spitball around 10-15gb bigger
<r​brunner7> 10 GB sounds pretty reasonable
<sneedlewoods> +1
<s​needlewoods> Just a question about curve trees, what source do you recommend to get acquainted with them? I bookmarked this a while ago: https://eprint.iacr.org/2022/756.pdf
<j​effro256> Once we add that storage cost, we get to perform close to no database reads validating each input which is really nice
<r​brunner7> How does that work? Only very few lookups in the tree for verifying a single enote?
<jberman> this source is solid too: https://www.youtube.com/watch?v=6p8rqlNo0xs
<s​needlewoods> thanks
<jberman> " Once we add that storage cost, we get to perform close to no database reads validating each input which is really nice" +1, I think HDD sync may end up viable
<r​brunner7> By the way, for the record, I wrote my take on continuing with the wallet work despite it's now FCMPs instead of Seraphis, at least first: https://github.com/seraphis-migration/strategy/wiki/Our-Wallet-Rewrite-Project-After-Priority-Switched-From-Seraphis-to-FCMPs
<jberman> verifying an fcmp you only need the tree root + the proof, the root is a single lookup in the block header
<jberman> compared to random db reads for every ring member's pub key
<r​brunner7> I guess I will never understand how that FCMP magic works. Not that it matters much.
<r​brunner7> From the MRL meeting we learned that reviews are progressing nicely. The crypto and the math seems to hold.
<s​needlewoods> sounds all very promising
<jberman> @kayabaNerve 's specification is easier to understand for the actual integration side of things: https://github.com/kayabaNerve/fcmp-ringct/blob/develop/fcmp%2B%2B.pdf
<r​brunner7> Yeah, but still some hard work still ahead surely
<r​brunner7> Alright, seems that no particular subject presents itself to discuss today. Any closing remarks?
<jberman> integration side as far as actual code that needs to be written, I think setting up the tree *should* be the most challenging part, and I'm almost done with that
<jberman> (specifically the grow and trim algos)
<r​brunner7> You mean you leave the rest as an exercise of some aspiring new dev :)
<j​effro256> Is the tree code tightly coupled with LMDB?
<jberman> nay not entirely, I was still planning to keep going on integration, but this was the hard part I think
<jberman> it's not, I've explicitly tried to keep the db side of code very light, and move most of the algo logic into a separate CurveTrees class
<jberman> example: I say the trim_tree algo is done and tested, but I haven't implemented the db yet, which should be relatively simple given how the code is structured
<j​effro256> Okay okay I think I see
<r​brunner7> There are still traces in the code that hint at the possibility to use a DB backend other than LMDB, from the very early times, quite in general
<jberman> for grow_tree for example, this is the function doing most of the algo logic: https://github.com/j-berman/monero/blob/e0502e41843a9b74fbce22805d067ce73c517d13/src/fcmp/curve_trees.cpp#L493-L496
<jberman> and here's where it's called from the db code:  https://github.com/j-berman/monero/blob/e0502e41843a9b74fbce22805d067ce73c517d13/src/blockchain_db/lmdb/db_lmdb.cpp#L1322
<r​brunner7> Looks interesting.
<r​brunner7> Ok. I think we got everyhting for today. Thanks for attending then, read you again next week!
<s​needlewoods> thanks, cu
<j​effro256> Thanks !
<k​ayabanerve:matrix.org> jberman: Re: migration, it's a torsion clear *and* a check the output key is valid. Not all are :/
<k​ayabanerve:matrix.org> Credit to boog900 for the reminder.
<k​ayabanerve:matrix.org> rbrunner7: It's 'just' a merkle tree :) jbermam says you just need the tree root and that's correct. With a merkle tree root and a merkle tree proof, you can verify an element is in fact within a merkle tree.
<k​ayabanerve:matrix.org> We just specify the merkle tree root to use via specifying the block which created it. We can't exactly let users specify arbitrary merkle trees to spend outputs of :)
<k​ayabanerve:matrix.org> *I know you said you don't need to understand it, I just want to do my best to break it down and ensure accessibility.
<r​brunner7> Thanks, kayabanerve, no problem :)
````


# Action History
- Created by: rbrunner7 | 2024-07-05T14:17:12+00:00
- Closed at: 2024-07-08T18:58:45+00:00
