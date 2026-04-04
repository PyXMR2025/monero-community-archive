---
title: 'Monero Tech Meeting #115 - Monday, 2025-04-07, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1183
author: rbrunner7
assignees: []
labels: []
created_at: '2025-04-04T15:21:52+00:00'
updated_at: '2025-04-07T18:57:09+00:00'
type: issue
status: closed
closed_at: '2025-04-07T18:57:08+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1179).

# Discussion History
## rbrunner7 | 2025-04-07T18:57:09+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1183
<j​effro256> Howdy
<s​needlewoods> hey
<r​brunner7> Ok, maybe somewhat smaller circle today. What are the reports about last week?
<s​needlewoods> I just pushed https://github.com/monero-project/monero-gui/compare/master...SNeedlewoods:monero-gui:x_replace_cached_password_with_verifyPassword & https://github.com/monero-project/monero/compare/release-v0.18...SNeedlewoods:seraphis_wallet:x_remove_cached_password
<j​berman> Sorry, *waves*
<j​berman> me: FCMP++ optimization contest launched! (blog post: https://www.getmonero.org/2025/04/05/fcmp++-contest.html). Coordinating with xmrack  on additional comms (reddit, twitter, and additional outreach)
<j​berman> Also finished including the FCMP++ tree root in the PoW hash for each block. After much discussion with jeffro256 , I settled on an approach that I think is very solid (it won't materially affect miners creating new block templates nor normal sync), and also happened to be straightforward to implement: https://github.com/seraphis-migration/monero/pull/22
<j​berman> This week I'm planning to implement caching pre-built blinds in the wallet in the background (so that tx construction is near-instant). Blinds construction takes on the order of seconds and does not have to run at tx construction time (i.e. can be pre-cached). The FCMP++ contest (on divisors specifically) will hopefully speed this up by at least 2x, but even a 2x speed-up remains on the order of seconds without caching
<j​berman> I will also likely finish my current CCS this week, and open another
<s​needlewoods> didn't make as much progress as I hoped for, but fixed a nasty bug that changed your password to zero bytes of the length of your original password when changing restore height, because that uses `setPassword()` to trigger rewrtite of .keys file
<j​effro256> me: integrated Carrot/FCMP++ transaction building into `wallet2` and am almost done with testing
<sneedlewoods> +1
<rbrunner7> +1
<r​brunner7> "didn't make as much progress as I hoped for" SNeedlewoods : Lack of time? Or did you finally stumble over something that you can't rectify regarding storing passwords in memory, for hard technical reasons?
<r​brunner7> jberman: Did you also consult some "mining people"? Or is the approach clear and simple enough that the two of you can be sure it flies?
<j​berman> The latter. Some miners who construct block templates themselves via some routes exposed by the daemon just need to read a new field `fcmp_pp_tree_root`, which the daemon just reads from the db / doesn't spend time doing crypto to feed it to the miners
<sneedlewoods> +1
<rbrunner7> +1
<jeffro256> +1
<tobtoht> +1
<plowsof> Tobtoht has been experimenting with feather + fcmp++ testnet. Constructing transactions and such :)
<jberman> +1
<sneedlewoods> +1
<r​brunner7> Sounds like some adventure for tobtoht :)
<s​needlewoods> lack of time, many unexpected distractions, also I feel the scope of just "remove cached password" increased and Qt has giving me trouble a couple times, but I'm still optimistic that I'll be able to finish this
<r​brunner7> Nice
<moneromooo> Preventing cached password in the GUI ? I long ago assumed it was not possible, unless you patch Qt.
<moneromooo> That's why I only did monero-wallet-cli. Unless you can override malloc in Qt...
<j​berman> Of note, there is a theoretically optimal approach to block template construction: the daemon could immediately serve new block templates (/ data used for new block templates) before verifying a block's contents , so that miners aren't wasting cycles mining a likely stale block template in the usual case
<moneromooo> You *could* override operator new and operator new[] though. I suppose you could wipe *everything*....... So disregard my comment...
<moneromooo> Assuming Qt always goes new and not malloc/calloc.
<j​berman> This is relevant because the approach to tree construction right now adds something like 5-15 milliseconds to block verification (depending on the machine), which is done before miners can get the new template. 5-15ms is a relatively small proportion of block verification at the moment, which is why I would say the above theoretical optimum is one that is sensible to keep on the back-burner and not a pre-req for FCMP++
<s​needlewoods> moneromoo my approach is to call this function to wipe the QStrings https://github.com/SNeedlewoods/monero-gui/blob/0d58e6b0663e973fa273a1089d2151b92e1a1c06/src/qt/utils.cpp#L218C1-L224C2
<r​brunner7> "FCMP++ optimization contest launched!" jberman , do you plan to follow up that blog post with a Monero subreddit post? Maybe we won't reach many potential contestants with such a Reddit post, but the community might be interested anyway.
<j​berman> yes coordinating with xmrack on it. From @xmrack also: "I’ve sent out emails to four groups of researchers who publish monero related works in the past. I also sent out emails to codeforce and zprize to see if we could advertise to their userbase" + "I also submitted an inquiry to Kaggle which is a long shot but curious what they say back"
<rbrunner7> +1
<jeffro256> +1
<moneromooo> That wipes *a* QString, but you have no idea where an edit widget put your data.
<moneromooo> In wallet2, I had to contend with std::cout (same thing, it might buffer) and made sure I avoided that potential buffering. But Qt might buffer a lot more.
<j​berman> the UI elems shouldn't be manging the password in memory at all though right? should just be those black dots
<moneromooo> Though, as I thought a few minutes ago, overringing delete/delete[] might work. Unless those widgets have long lived working data.
<j​berman> Or are you saying as it ingests the input
<moneromooo> You don't know though. That's the point.
<moneromooo> You might if you read the Qt source but it might change.
<moneromooo> I do know that std cin/cout do buffer stuff that stdio doesn't, for example.
<r​brunner7> I guess without looking through the source code of Qt  I guess what is left is looking in process memory for widget related copies of the password still left, and if none can be found that's a good probability it's not a problem.
<moneromooo> Well, the particular impl of cin/cout I used when testing.
<moneromooo> Right. I made a program to find my password in mapped memory when I did this.
<s​needlewoods> wouldn't it work to dump the memory after you typed in many different password fields and then search for the bytes to confirm you can't find them anymore?
<moneromooo> And cin/cout did leave droppings. I assume Qt can leave even more, since there's a lot more code dealing with I/O that we did not write.
<r​ucknium> jberman: tobtoht 's testing of FCMP showed a 1in/2out tx took 3 minutes to construct. Is it the un-cached "blinds" that are causing the very slow construction? If so, could you explain more about blinds, their role, when they need to be computed/cached, and their performance characteristics?
<moneromooo> Yes, it would mostly work.
<j​berman> ouch. I believe at the moment, wallet2 is *also* doing multiple rounds of tx construction (including blinds calculations) that jeffro256's code for carrot construction I believe should eliminate once integrated
<tobtoht> +1
<rucknium> +1
<r​brunner7> SNeedlewoods: Do I remember correctly, you actually did some such memory searches?
<j​berman> But yes, I'm guessing it's almost certainly tree branch blinding causing that slowness tobtoht is seeing
<moneromooo> https://paste.debian.net/hidden/7d665900/ is the code to grep for the password if this helps.
<s​needlewoods> I did only confirm that the memory the QString pointed to before the wipe was empty afterwards, I didn't check the entire memory though
<j​effro256> I'm not jberman, but yeah the blinds are going to take the majority of the CPU time when constructing FCMP++ txs. There's two types of blind: output blinds, and curve tree blinds. Output blinds can be calculated as soon as you scan on output. Curve tree blinds can be calculated whenever: they don't have any computational dependencies. You need 1 output blind per spend output, and  T-1 curve tree blinds per spent output, where T is the number of layers in the FCMP tree. At the moment for mainnet, this is 6-7 IIRC.
<rucknium> +1
<r​brunner7> Thanks for that code, moneromooo, interesting!
<moneromooo> wallet2 used to (when I did it) create txes to check size, as it adds inputs, just to see when it stops being valid. It is fairly brute force.
<s​needlewoods> thank you moneromoo, is it okay if I DM you on IRC if I have more questions?
<j​effro256> Only tx *provers* need to construct blinds, and they need to do so when making membership proofs.
<moneromooo> Note that a long password might only be partly present after a free, if some data is being reset (size, deltas...) but the main memory is left alone.
<r​brunner7> Although worst case using that code may end up with some frustration for SNeedlewoods  :)
<t​obtoht> Thanks jberman and jeffro256 for clarifying.
<moneromooo> Sure, dm me is fine.
<moneromooo> I've not hacked on monero in a long while though.
<j​berman> An output's path in the tree has to be blinded to construct the FCMP++ proof (which is part of avoiding revealing the output's path). This is part of the math that divisors is doing that is particularly slow, that the contest is targeted at speeding up
<r​brunner7> With that very early goalpost set at 3 minutes tx construction time, will be interesting to see where we will finally land for the fork code!
<j​effro256> The cache that jberman is talking about could startup a thread once a wallet is generated and create blinds in the background, so that when the user wants to construct a transaction, the blinds are already mainly ready
<jberman> +1
<s​needlewoods> as long as I'm the only one frustrated by my work it's okay for me, but I don't want to start frustrating you guys
<r​ucknium> Thanks for your responses. So we expect to have usable FCMP tx construction before the contest is done, correct? And even faster tx construction after it is done? I am thinking of stressnet and the need to spam txs.
<r​brunner7> Imagine construction time of 3 minutes for a PC on a somewhat old-ish smartphone :)
<j​berman> Final FCMP++ release also shouldn't be doing those blinds calculations >1 times per tx, so that will be fixed / looked into also
<j​effro256> Technically speaking, an output blind is composed 4 subparts, and we will basically always need to recompute of 1 of the 4 subparts of the output blind during transaction construction time, even with a good cache
<moneromooo> FWIW, IIRC the blind constructs bypass things like BP calc (using known size placeholders), exactly because it was starting to become slow enough to be annoying.
<j​berman> "So we expect to have usable FCMP tx construction before the contest is done, correct? And even faster tx construction after it is done?" -> yes and yes. Something like <3s tx construction should be feasible even before the contest
<tobtoht> +1
<r​ucknium> Should I put alpha testnet/stressnet/testnet planning on the next MRL agenda, or is it too early still?
<r​ucknium> Great. That was my understanding from the old Curve Tress discussion. About 2 seconds to prove.
<j​berman> "FWIW, IIRC the blind constructs bypass things like BP calc (using known size placeholders), exactly because it was starting to become slow enough to be annoying." -> can look into this approach for these new blinds calculations too
<j​berman> thank you moo :)
<j​effro256> The need for the subpart recomputation is because balancing a transaction's input and output amount commitments requires us to recompute what's called the "c_blind" or "amount commitment rerandomization blind". And the balancing process depends on knowing the amount blinding on the outputs, which we don't know until transaction construction time
<r​ucknium> By the way, you no longer have to worry about leaving Exodus Wallet behind, since they plan to end Monero support in August, anyway. According to Reddit.
<r​brunner7> Seems we enter a quite hot phase already with FCMP++ code, so much going on.
<r​brunner7> I wonder what the MyMonero people plan. Did anybody hear something already?
<moneromooo> Also, wrt your wipeQString function, I made a memwipe function, because at least one compiler (GCC) is known to be able to detect stores before a free, and removes those stores because it doesn't modify program behavior. So I would use memwipe instead of this.
<r​ucknium> Or you could decide to plan alpha testnet (at least) here in these meetings.
<moneromooo> memwipe isn't technically guaranteed to always work though, it just confuses the compiler enough to stop being a smartarse.
<r​brunner7> Lol
<j​effro256> I'm going to miss you dunking on how terrible their wallet software is
<r​brunner7> Soon we will see the first ChatGPT based compiler that you won't be able to fool anymore :)
<r​ucknium> Lol. I am of two minds on this Exodus dropping support
<r​brunner7> Yeah
<r​ucknium> Bad that Monero is available to fewer users with just the Exodus wallet, but good that their custom tx construction will come to an end.
<r​ucknium> Probably they are dropping it because of the resources needed. They have always had overloaded nodes AFAIK.
<r​brunner7> Ok, after that wealth of reports, do we have anything general left to discuss today?
<j​effro256> Probably non-trivial dev time to keep their custom wallet software working with the current mainnet, plus whatever features they support, plus Exodus-specific bug fixes
<j​effro256> Maybe they would be open to keep supporting Monero if there was a good general-purpose, community-maintained Monero light wallet library ? IIRC I think everoddandeven is working on something like that
<r​brunner7> Does not look like it. Thanks everybody for attending this interesting meeting, read you again next week!
<s​needlewoods> thanks everyone
<r​brunner7> jeffro256: That's why I wonder about MyMonero. If I remember correctly, a number of wallets run on their infrastructure, and/or their tech. If they throw in the towel, they might take a number of such wallets with them. Not that we could do much against that ...
<endogenic> well i can support that stuff easily with my infra
<endogenic> but it’s a liability
<endogenic> and do we really want some central party scanning all these view keys?
<endogenic> one compromise and it’s game over for that set
<endogenic> at least future tech will alleviate that concern
````


# Action History
- Created by: rbrunner7 | 2025-04-04T15:21:52+00:00
- Closed at: 2025-04-07T18:57:08+00:00
