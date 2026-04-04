---
title: 'Monero Tech Meeting #83 - Monday, 2024-08-19, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1058
author: rbrunner7
assignees: []
labels: []
created_at: '2024-08-16T17:46:15+00:00'
updated_at: '2024-08-19T19:25:30+00:00'
type: issue
status: closed
closed_at: '2024-08-19T19:25:30+00:00'
---

# Original Description
Based on the [opinions given here](https://github.com/monero-project/meta/issues/1054) I decided to go back to the *No Wallet Left Behind* Matrix room and IRC channel for the next i.e. coming Monday's meeting,  and to not contiune to hold meetings like the [last one](https://github.com/monero-project/meta/issues/1053) in the -dev Matrix room and IRC channel.

Thus location is again Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

It seems there still is a unmet need for "dev meetings" to discuss and coordinate things like bug corrections, pending reviews, smaller feature additions, merges and merge conflicts, and so on. To differentiate, I came up with a working title of *tech meetings* for this series of Monday meetings.

# Discussion History
## rbrunner7 | 2024-08-19T19:25:30+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1058
<s​needlewoods> hello
<o​ne-horse-wagon> Hello.
<v​tnerd> Hi
<d​angerousfreedom> Hi
<r​brunner7> Let's see how long the normal topics take, if there is time left, we can do a little bike-shedding about naming this meeting at the end
<r​brunner7> Thus, on to the reports from last week
<j​effro256> Howdy sorry I'm late
<r​brunner7> 3 minutes only :)
<s​needlewoods> I have some local changes for this https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_api_add_new_functions I can push if anyone wants to take a look at the newest version
<s​needlewoods> and I shared this last week in monero-dev, but not sure if anyone saw it so: https://github.com/SNeedlewoods/seraphis_wallet/issues/1
<j​berman> *waves*
<d​angerousfreedom> Not much from my side. Just improving my understanding of fcmp in general and playing with some unit_tests that could hopefully be useful for the wallet sync. Maybe would be nice to organize a TODO list with some specific tasks for integrating fcmp into wallet2?
<r​brunner7> That's quite some collection you came up with there, SNeedlewoods
<r​brunner7> I saw you had some discussions during the week, dangerousfreedom . So this did not yet "converge" to a point where you can start to code something?
<s​needlewoods> I wasn't so diligent with the notes in the beginning, but midway through I thought it could be useful to write things down.
<j​berman> pushed the fcmp draft PR: https://github.com/monero-project/monero/pull/9436 , planning to open a new CCS
<r​brunner7> What are your next planned steps with that draft PR, jberman ?
<j​berman> address comments, work down the to-do list in the PR
<j​effro256> me: working with auditors on specifying exact scope and refining some definitions in the carrot doc
<r​brunner7> Ah, I see now, there are TODOs towards the end
<j​berman> the checklist in the beginning is what I was mainly referring to
<r​brunner7> Even better, checkboxes :)
<r​brunner7> I wouldn't even know how to do those in MarkDown ...
<j​effro256> sneedlewoods: as for the payment ID argument removal , the reason it is there is because payment IDs precede integrated addresses. Before, you had to enter the main address and payment ID separately
<j​berman> haha https://github.blog/news-insights/product-news/task-lists-in-all-markdown-documents/
<r​brunner7> So if dangerousfreedom would start to code, would he build on top of your PR, at least in part?
<j​effro256> You could probably remove that now. I genuinely don't know of any service which uses payment IDs outside of integrated addresses in 2024
<j​effro256> Which has been deprecated for years BTW
<d​angerousfreedom> Well, there were different opinions about the way to store the enotes path in the tree. I think we should start with the easiest one (just store the path directly and update it if there are reorgs) and somehow integrate this 'simple' function into a scanner. I need to check with jberman though yet. jeffro256 had different opinions too. So maybe it would be nice to start creating t<clipp
<d​angerousfreedom> his TODO list so at least we agree what needs to be done.
<r​brunner7> I see.
<s​needlewoods> iirc I tried some commands with long payment id and couldn't get them to work, because there were already checks that don't allow them, so imo it should at least be removed from the help command, which e.g. for `transfer` is already a bit cluttered.
<d​angerousfreedom> I dont know. What are your opinions?
<r​brunner7> Who do you address? In any case, I am not deep enough into all this tree stuff to have an opinion
<j​berman> Continuing the prior discussion on building the tree locally or having daemons serve all tree elems wallets need, personally I think it would make sense to optimize for minimizing bandwidth (wallets pointing to remote nodes are generally bandwidth constrained), and so it makes sense to build the tree locally
<d​angerousfreedom> I think it would be much simpler
<j​effro256> If you DIDNT want to build it every block then you need to store all transaction outputs for the whole chain
<j​berman> you don't need to save the entire tree locally, but not sure how you wouldn't effectively do all tree updates locally to get to the new root for each block range
<r​brunner7> With these "tree local" approaches, would this lead to code duplication, or could the wallet and the daemon use the same code?
<j​berman> with the approach I was initially saying, they could use mostly the same code
<j​berman> but sounds like danger has something else in mind?
<j​berman> ("approach I was initially saying" is referring to this approach)
<d​angerousfreedom> No, I want to reuse the same code. The point is that the wallet doesnt need to do the same thing as the daemon would be doing.
<j​berman> can you expand
<d​angerousfreedom> Well, building the tree everytime. Theoretically we should update the tree only when: 1) We receive an output. 2) There is some re-org and the output index change. 3) We spend this output.
<d​angerousfreedom> Am I missing a case?
<j​berman> once you've received an output, you need to make sure its path to the latest tree root is correct, which means you technically have to update every receive, every block, since the tree root changes every block
<d​angerousfreedom> If we want to build a tx, we just need to pass the path and the tree root that it refers to. So, maybe there is a 4th case, when we are building a tx and we want to check that everything is fine.
<j​berman> once you want to build a tx, you pass the latest path to root and latest root i.e. root 10 blocks from tip
<j​berman> making sense?
<d​angerousfreedom> Yes sure.
<d​angerousfreedom> But the path wont change. Thats the thing
<r​brunner7> I still don't understand half, but I still see some contradictions. danger: "Only update if ..." jberman: "update every receive"
<d​angerousfreedom> Or it may change if the tree grows too much
<d​angerousfreedom> In the case there is another layer added for example
<j​berman> if you keep the path and tree root constant from the point in time you receive the output, and then 10000 blocks later construct the fcmp referring to the static path and root you saved back when you received the output, you reveal to the chain you're constructing an fcmp using a root from 10000 blocks ago
<j​berman> to avoid that privacy leak, the idea is to construct the fcmp 10000 blocks later using the *latest* root, and the *latest* path to root, which changed from 10000 blocks prior (and changed every block since)
<j​effro256> The path DOES change while you're scanning though. For example, the root is always in the path. AND the root changes every block
<d​angerousfreedom> Yeah, that would be bad. I'm not saying to do that. We need to always refer to the tree minus 10 blocks
<s​needlewoods> If I may ask, how big in size will the tree approximately be? If for some reason I have 100 wallets and everyone saves its own tree, could that become problematic?
<j​berman> so the wallet sync has to update the path every block to avoid the privacy leak
<r​brunner7> Is the bandwidth problem regarding mobile wallets with remote daemons really so bad? I think we don't have to fetch decoys anymore, so we should be able to fetch tree elements instead, with not much more traffic caused?
<j​berman> GB's, but we're not proposing saving the tree, only building the tree once on sync (using what wallets already download on sync). wallets don't even need to keep the entire tree in memory btw, just chunks roughly equal to what's downloaded
<d​angerousfreedom> Yeah, I agree that the path changes, sorry. I didnt well explain. The changes would be minimal though. I think it is not worth to rebuild it everytime but I dont know the best algorithm for that though. I started thinking about this problem but don't have a solution yet
<j​effro256> It will be approximately (32×(7×30+1)+32×3x30)×N bytes in size where N is the number of owned enotes
<r​brunner7> danger: "Changes minimal" jberman: "root changes every time". Hmm.
<j​berman> decoys don't affect wallet sync, wallet sync with remote daemons today generally seems bandwidth constrained
<s​needlewoods> thanks
<r​brunner7> Ah, yes of course, I confused this with tx building
<r​brunner7> Is my intuition correct that this tree building while sync is far from trivial? And that tree building in the daemon isn't trivial either, but differently not trivial?
<j​berman> get_tree_extension only does what's minimally necessary to update all tree elems to get to the new root fwiw
<j​effro256> You have to either A) rebuild it everytime or B) store all on-chain enotes since the last time it was rebuilt. To save a lot of compute time, maybe you could just rebuild it at the end of refresh or the after consuming 1000 blocks , whichever comes first.
<j​berman> building the tree isn't trivial in that the logic isn't trivial, but get_tree_extension handles most of that complexity
<j​berman> get_tree_extension is doing the heavy lifting for tree building in my PR
<d​angerousfreedom> No, it shouldnt be that hard. jberman already laid out most of the work. If we just re-use it then it should be mostly done. I'm just trying to understand if there is a better way then making a loop and rebuilding the local tree everytime, more or less as the daemon is doing. But I believe that for a first approach we should try that and see how it performs. Maybe I should focus on that
<r​brunner7> Ah, you were on the verge of doing premature optimization then :)
<d​angerousfreedom> No, it shouldnt be that hard. jberman already laid out most of the work. If we just re-use it then it should be mostly done. I'm just trying to understand if there is a better way than making a loop and rebuilding the local tree everytime, more or less as the daemon is doing. But I believe that for a first approach we should try that and see how it performs. Maybe I should focus on that
<r​brunner7> One of the banes of modern programming
<d​angerousfreedom> Just brainfarts probably
<r​brunner7> Now I think you are too hard with yourself
<r​brunner7> But what you wrote last sounds somehow good to me. Try the most simple, even primitive way, to get it working in a technical correct way, and see how it does
<r​brunner7> If you can mostly only call that fine method you even don't loose too much code if a fundamentally different approach will be needed after all
<r​brunner7> And maybe if you do *not* try that first we will have people bickering for years about your "overly complex code" and "why did you not try the simple way first" :)
<r​ucknium> Will every wallet software that stores and sends XMR need to implement this method?
<d​angerousfreedom> Yeah, I will try to check with jberman again this week what still relevant to do and what I can help and start with the basic. Sorry for being slow and wasting time.
<d​angerousfreedom> Yeah, I will try to check with jberman again this week and see what still relevant to do and what I can help and start with the basic. Sorry for being slow and wasting time.
<r​brunner7> Probably only for the few cases that won't use the standard wallet code?
<r​ucknium> Of course, "third party" wallets can just import the C++/Rust code, but some of them are not written in those languages.
<d​angerousfreedom> They dont have to. But usually the wallets copy the monero code I think.
<r​brunner7> I think quite in general it will be a difficult issue how genuinely third-party code, e.g. with custom tx building, will fare with the introduction of all this new FCMP stuff
<d​angerousfreedom> You can also use the most primitive method of all. Just update the tree when you receive and output and when sending a tx you refer to the root of tree you built at that time. That would be the equivalent of choosing decoys that are very old only.
<d​angerousfreedom> You can also use the most primitive method of all. Just update the tree when you receive an output and when sending a tx you refer to the root of tree you built at that time. That would be the equivalent of choosing decoys that are very old only.
<r​brunner7> Yeah, but unlike the other approach that hasn't a chance in hell to stand, right?
<r​brunner7> That would only be something like a PoC
<r​ucknium> Probably at least one, if not many, third party wallets will use the simplest method, which will not necessarily be the best for user privacy.
<r​brunner7> Or experiment
<j​berman> I think this is how the different strategies wallets can use look:
<j​berman> Full wallets that are optimized for minimal bandwidth: build the tree locally
<j​berman> Full wallets that are optimized for minimal client-side computation: download all tree elems needed when syncing
<d​angerousfreedom> I guess there is not stopping them to do that but users wont choose these wallets to use I think.
<r​brunner7> Or, if you want to be pessimistic, give up on XMR altogether, aka "throwing in the towel"
<j​berman> Light wallets: scanning stays the same. on tx construction, they fetch decoy paths in the tree from nodes
<d​angerousfreedom> Probably there are no wallets today that use whatever distribution of only old enotes as decoys
<r​ucknium> This is the reality right now. For example, Exodus wallet. Arguably, MyMonero.
<d​angerousfreedom> Oh okay
<r​ucknium> There was a paper just published about a wallet using "differ-by-one" decoys sets. isthmus found it AFAIK
<r​brunner7> But well, you can't wish those trees away if you want to do it right. Some code has to care about them. If people don't want or can't use the standard code they have to write it themselves, without any way around that, seems to me.
<j​berman> AKCHUALLY once again, light wallets fetching decoy paths will only be useful when the "filter-assist" tier exists
<j​berman> Since light wallets already know received outputs, there's little to no benefit to fetching decoy paths
<jeffro256> +1
<j​berman> So really light wallets without filter-assist can just request the receive output paths from their lws
<j​berman> at tx construction
<j​berman> unless light wallets start pointing to daemons in addition to their backend lws
<endogenic> that is not only possible, but it's basically happening already by way of the LWS
<r​brunner7> So, if it seems we have reached a certain point with those issues now, so anything else to discuss in the short remaining time?
<endogenic> see get fee estimate
<endogenic> The LWS is basically a better front end
<t​obtoht> I'm working on reproducible/bootstrappable release builds for fcmp++ over at https://github.com/monero-project/monero/pull/9440
<jeffro256> +1
<dangerousfreedom> +1
<endogenic> well, I don't know about better
<t​obtoht> When ready, I will probably spin this off into a separate PR based on #8929 with the minimum set of changes we need to ship Rust, then PR fcmp++ specific build changes to jberman's branch (if that's okay)
<endogenic> I wish I had published already
<r​brunner7> tobtoht: Sounds good. Somehow surprising how you evolved in a build specialist :)
<r​brunner7> *into a build specialist
<j​berman> what I mean is light wallet client points to the LWS strictly for scanning, and then points to an entirely different backend daemon that is not colluding with the LWS, in order to fetch decoy paths and construct the tx, to avoid revealing to the LWS which output the user is spending
<j​berman> thank you @tobtoht  <3
<j​effro256> @jberman: are you planning at all to break up the FCMP++ PR at all for reviewers ?
<endogenic> ah my mistake
<t​obtoht> Feather releases have been bootstrappable since Jan 2023 ;) It did away with a bunch of release security related anxiety.
<endogenic> what about pointing to a different AWS rather than pointing to a Damón
<endogenic> ugh
<endogenic> lws
<endogenic> A few other people have had this idea before that you could sample random outputs from multiple oracles
<j​berman> I am, yep. I was thinking FFI would/could be a separate PR for sure
<endogenic> i'm trying to say you could still use the LWS for it
<j​berman> haha aws freudian slip
<endogenic> yeah, Siri is having some conniptions
<j​berman> ya that's fine, main point being it would be better privacy if those backends weren't colluding
<endogenic> yes, and I would like to massively promote distribution of LDS instances for this reason and I have a whole ton of work that I'm excited to share
<endogenic> lws lolll
<r​brunner7> Alright, feel free of course to continue discussing, I think we can close the meeting proper. Thanks everybody for attending, read you again next week!
<s​needlewoods> Thanks everyone, bye.
<j​effro256> Thanks everyone !
````


# Action History
- Created by: rbrunner7 | 2024-08-16T17:46:15+00:00
- Closed at: 2024-08-19T19:25:30+00:00
