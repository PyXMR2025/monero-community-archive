---
title: 'Monero Tech Meeting #171 - Monday, 2026-05-25, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1394
author: rbrunner7
assignees: []
labels: []
created_at: '2026-05-24T06:05:14+00:00'
updated_at: '2026-05-25T18:39:12+00:00'
type: issue
status: closed
closed_at: '2026-05-25T18:39:12+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1390).


# Discussion History
## rbrunner7 | 2026-05-25T18:39:12+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1394
<koe000> Hi
<sneedlewoods> hey
<spirobel> hi
<rbrunner7> Alright, maybe some more will join, but let's start with the reports already.
<jpk68> Hello
<vtnerd> Hi
<rbrunner7> I worked on Polyseed in the RPC wallet server. More to do than I knew first.
<koe000> Me: reported earlier, multisig mostly done, waiting on jeffro to rebase the hotcold branch.
<sneedlewoods> restore height approximation (still testing some things with the GUI, but mostly done), else reviews and mirrors
<sneedlewoods> will try to put my focus back into replacing wallet2 with the Wallet API in wallet-rpc
<spirobel> i implemented the serai based multisig dkg in my library and wrote an acceptance test for the typical escrow case: https://xcancel.com/spirobel/status/2056020125145600366#m  for context: https://xcancel.com/spirobel/status/2053101870768697645#m general overview of my library and wallet demo. Now i work on documenting the wallet / web app interaction 
<rbrunner7> @koe000: So soon it will be A) hop on stressnet, B) compile your PR branch, C) test multisig, right?
<rbrunner7> @spirobel: "dkg" being...?
<spirobel> @rbrunner7: distributed key generation
<jpk68> Me: was a bit busy with IRL stuff, but made some progress on I2P work and a few PRs
<rbrunner7> Ah, yes, of course, thanks
<koe000> rbrunner7: well no doubt I’ll have to grind through some mind-melting bugs first
<spirobel> rbrunner7  there is a blog post that gives and overview: https://monerochan.news/article/19
<rbrunner7> Thanks, will be an interesting read, I was just asking myself what you intend to use multisig for :)
<spirobel> +1
<rbrunner7> You seem to aim quite high, I hope you didn't bite off more than you can chew ...
<rbrunner7> "mind-melting bugs" hopefully not
<rbrunner7> (about potential multisig problems in koe's code)
<rbrunner7> I think quite in general a lot is happening regarding third-party projects based on Monero right now. Too bad not all are really solid.
<rbrunner7> Opening the source seems to be a step too far for some projects, for example.
<spirobel> i mean you can just try it the code is done now and it is really not that hard to grasp :D 
<spirobel> there is also this convo with alia https://xcancel.com/spirobel/status/2056082082913456234#m about the practice in xmrbazzar 
<rbrunner7> @vtnerd:monero.social: By all means you should mention that you have a 1.0 beta of LWS out now! https://github.com/vtnerd/monero-lws/pkgs/container/monero-lws
<sneedlewoods> +1
<spirobel> +1
<jpk68> +1
<rbrunner7> I have a suspicion that light-wallet servers might become more important with FCMP++. Let's see what happens with the larger transactions and the resulting faster blockchain growth. Might not take long to have blockchain file of half a terabyte ...
<rbrunner7> Alright, looks like we are through with the reports. Anything special to discuss today?
<rbrunner7> Does not look like it. Let's close already then. Thanks for attending everybody, read you again in 1 week!
<sneedlewoods> Thanks everbody
<jpk68> Thanks, everyone
<jpk68> @sneedlewoods: Jinx!
<vtnerd> Yeah there's nothing fcmp++ in that release, but it's got a lot of changes since last release 
<spirobel> here is the repo btw https://github.com/monerochan-ecosystem/monero-wallet-api
<spirobel> it can also do multiwallet multi threaded sync 
<spirobel> in the browser as well
<rbrunner7> Yes, that's what I meant, looks like lots of cutting-edge stuff in a single swoop, done single-handedly. Not the easiest thing to pull through.
<jberman> Augh, apologies I lost track of time
<spirobel> @rbrunner7: i agree. but the thing is done now. https://video.twimg.com/amplify_video/2053096986489057280/vid/avc1/3840x2160/4oKLjFzvpG_YokxK.mp4 you can watch the video of the acceptance test run to get a vibe for it. 
<jberman> my update: beta stressnet v2.0 review (preparing to roll back and restart stressnet), FCMP++ integration audit handling some suggestions (the phase 1 audit went well, only informational suggestions found, and it seemed solidly deep. Final report I anticipate will be ready soon) 
<jberman> > <@rbrunner7> I have a suspicion that light-wallet servers might become more important with FCMP++. Let's see what happens with the larger transactions and the resulting faster blockchain growth. Might not take long to have blockchain file of half a terabyte ...
<jberman> LWS is primarily good to avoid scanning in the wallet. FCMP++ txs don't impact scanning time, wallets only download pruned data (not FCMP++ proof data). Building the FCMP++ tree slows down scan time somewhat, Carrot speeds up scanning time somewhat. We haven't done a complete benchmark yet to see how scan time will shake out
<spirobel> +1
<rbrunner7> I see
````


# Action History
- Created by: rbrunner7 | 2026-05-24T06:05:14+00:00
- Closed at: 2026-05-25T18:39:12+00:00
