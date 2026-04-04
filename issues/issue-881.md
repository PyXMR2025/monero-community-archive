---
title: 'Seraphis wallet workgroup meeting #33 - Monday, 2023-08-21, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/881
author: rbrunner7
assignees: []
labels: []
created_at: '2023-08-19T05:14:13+00:00'
updated_at: '2023-08-21T19:36:17+00:00'
type: issue
status: closed
closed_at: '2023-08-21T19:36:17+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/877

# Discussion History
## rbrunner7 | 2023-08-21T19:36:17+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/881
<j​berman> hello
<j​effro256> howdy
<r​brunner7> dangerousfreedom won't join us today
<r​brunner7> So, what's there to report from last week? Mostly from the protocol, because many things can be read already in the log of the room
<j​effro256> Yeah mainly just https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4665372#gistcomment-4665372 for me
<r​brunner7> "Just"? You are on a run, good man :)
<j​effro256> ;)
<j​effro256> I want to discuss what y'all think about the trade-offs
<j​berman> I spent this past week mostly working on view key background syncing PR 8619, which will likely be the last significant feature I work on in the core repo before focusing fully on the Seraphis lib, and should be done within 2 days
<r​brunner7> Not to forget your PR with the wallet reading code: https://github.com/seraphis-migration/monero/pull/4
<r​brunner7> Yeah, that background syncing is valuable stuff as well.
<j​effro256> I'm ready for this feature ;)
<r​brunner7> That's the thing. I think we as a dev and researcher community have pretty few established ways to come to a conclusion with important things like this one ... but we can certainly discuss it here.
<j​effro256> Are you saying we should sollicit community opinions on the trade-offs?
<j​effro256> B/c I know there will be a part of the community that will be understanably angry at even larger addresses
<r​brunner7> Not really, I am saying we don't have any established "protocols" how to reach decisions. "Lose consensus" is awfully ... well .. lose.
<j​effro256> I prefer win concensus
<r​brunner7> Well, one think is easy: I think we should make your proposal known wide and far, to get as much feedback as possible
<j​effro256> Justin what are the main hurdles at the background syncing? I haven't really spent any time looking at that PR but I'm interested
<r​brunner7> Maybe a dumb question, but can we already consider it "pretty" sure that what you came up with works? That the "crypto" is sound? I would guess yes, I think by now both UkoeHB and @Tevador had a look, and neither sounded any alarm
<j​effro256> I think so, it's honestly pretty straightforward: one more DH exchange so that there's 2 view DH keys. Use each DH key for respective view tags, and make sr_1 a function of both DH keys
<j​effro256> But I can't be the one to review my own work
<r​brunner7> Yeah, sure, but at least if we are pretty sure it works we can start discussing in earnest.
<j​effro256> Also that's not a dumb question
<j​effro256> B/c there's ostensibly solutions which use techniques which Jamtis doesn't already use that no one has thought of yet
<j​berman> My preliminary thoughts on jeffro256 's proposal: I'm for increasing the address size ~25% in exchange for stronger privacy for light wallet users. Stealth addresses are a core pillar of Monero's privacy. For some (potentially many) users to lose that pillar with absolute certainty seems a steep negative and makes it more difficult for all but the technical power users to mentally<clipped message>
<j​berman>  model Monero's privacy
<j​berman> I'm not as sold on the necessity for "dense" scanning (2 byte view tag checks), the perf benefits don't seem worth the complexity, though it seems that could use a deeper look/further testing
<j​berman> I'll share more of my thoughts on the post soon
<r​brunner7> The 2 view tags are not a necessity, we could have the proposal without them, with just the problem with the "wallet tiers" repaired?
<j​effro256> Without the dense scanning, I believe full wallet scanning will be incredibly slow since you would have to recompute `Ko` every 1:256 enotes
<r​brunner7> Oh, so it's complicated. Always those trade-offs :)
<j​effro256> You already have to do the DH key exchange to separate concerns anyways, so hashing it and comparing 2 bytes to knock out 99.998% of further computation saves a lot of time
<r​brunner7> Ok, I will read up the latest info there and post on the gist as well in the next days.
<r​brunner7> Currently I am pretty torn, I must confess. The tower of complexity, already incredibly high, just get higher ...
<j​effro256> It just so happens that since the view tags are computed independently of each other, you can have 2 view tag tiers. It's like a bonus feature, but if you didn't use that feature, you'd still have to do an extra DH every 1:256 enotes
<r​brunner7> Just curious, and hypothetically, jeffro256 , would you see yourself as capable and willing to rework the Seraphis library to implement this?
<r​ucknium> When it's mature, probably bring this idea to #monero-research-lab  at least. This channel isn't heavily subscribed nor logged at monerologs.net like the MRL channel is.
<j​effro256> That's a great question, and I've already been looking the `seraphis_lib` code b/c I don't want to drop this burden on Koe or jberman since they're already swamped. The code in `seraphis_lib` is honestly top quality, and it's been pretty easy to navigate. The crypto itself in the proposal is pretty simple so I think I could do it
<r​brunner7> Rucknium: I agree fully.
<j​effro256> That's a good idea Rucknium
<r​brunner7> jeffro256: Good to hear, because the best idea will fail if at the end nobody will be there to put it into actual code.
<j​berman> I have to review the recovery steps again more deeply, but if this ends up too slow (still a 99.6% speed-up compared to full scanning), couldn't the server just include the calculated shared secret when the client downloads find-received enotes?
<j​effro256> That's the thing: the light wallet will not be able to calculate the shared secret and decrypt address tags, which is how the privacy issues are addresses
<j​effro256> *light wallet server
<j​effro256> full wallets (those with both `k_dv` AND `k_sv`) can calculated the shared secret `sr_1`
<j​effro256> So the new "find-receive" tier (also has `s_ga`) can recompute both view tags and `sr_1` and thus `Ko`
<j​effro256> I thought about making a tier called "find-receive partial" which only has `k_sv` and `k_dv`, but not `s_ga`. This tier can recompute both view tags and `sr_1` but can't recompute `Ko` (unless it knows the public address). This tier is basically identical to the old find-receive tier in terms of privacy (just a lot slower). But then the tiers just got confusing so I excluded that one
<r​brunner7> As it gets pretty technical now, and as we probably don't have anything more for the meeting proper, I allow myself to withdraw for today. Thanks guys!
<j​berman> I follow, going to review it deeper and give more fleshed out thoughts on the perf side
<j​effro256> Thanks, I would appreciate it, even if you don't end up liking it
<j​berman> When I initially implemented view key background sync I didn't want to leave the view key in accessible state on disk at all times
<j​effro256> I just really like the idea of the light wallet ONLY being able to calculate view tags and nothing else. It's pure and private. What's cool about the different levels of view tags (for me) is that if/when the transaction volume gets really high and FCMPs are implemented, people on light wallets could start moving to sparse view tags (2 byte view tags) to again speed up processing <clipped mess
<j​effro256> time and bandwidth by 256x without loosing too much privacy in *most* threat models
<j​berman> I see that later point. At one point I considered a dynamic view tag that flexes in size based on tx volume, but seemed overly complex for v1
<j​berman> continuing background syc: after rbrunner7  re-raised the idea for view key/background cache to be always accessible in review, I got more feedback that that's the desired use case on mobile where an encryption key could live in secure KeyStore that is always accessible so the device can auto-start background sync even if the OS kills the app (thanks to valldrac  and sgp  for feedback)
<j​berman> So now I'm implementing it for that use case as described here: https://github.com/monero-project/monero/pull/8619#issuecomment-1668607595
<j​effro256> I like this idea. How easy is it to implement it in a portable manner?
<j​berman> portable as in usable for mobile devs?
<j​effro256> Like would the wallet2 code be directly storing the encryption keys in whatever device-dependent key store, or would you pass that encryption key into wallet2 and have it be the community devs responsibility to manage that key?
<j​berman> Ah, I'm implementing it in a way where the device would store that separate key, and can pass in a `background_cache_password` which wallet2 uses to encrypt the background cache and view key. wallet2 also stores the background cache and keys files, similar to how it handles wallet cache and keys, but encrypted with this key that the wallet API consumer can provide
<j​berman> aka the latter
<j​effro256> Okay sweet
<s​gp:magicgrants.org> waves
<j​effro256> One thing with the internal encryption that I didn't like it that `wallet2` doesn't know if it's currently encrypted or not. Would there be some kind of flag so it can throw an error if you try to encrypt/decrypt twice in a row ?
<j​berman> the keys unlocker does something like that. but no my current impl in my local doesn't do that. will reconsider it
<j​berman> it does indirectly, kind of difficult to explain without pointing to the code
<j​effro256> Yeah nothing better than just looking at the code ;)
<UkoeHB> I have not read the proposal yet, will try to get to it this week.
````


# Action History
- Created by: rbrunner7 | 2023-08-19T05:14:13+00:00
- Closed at: 2023-08-21T19:36:17+00:00
