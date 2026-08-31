---
title: 'Monero Tech Meeting #183 - Monday, 2026-08-31, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1449
author: rbrunner7
assignees: []
labels: []
created_at: '2026-08-30T04:37:26+00:00'
updated_at: '2026-08-31T18:56:31+00:00'
type: issue
status: closed
closed_at: '2026-08-31T18:56:31+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1442).


# Discussion History
## rbrunner7 | 2026-08-31T18:56:31+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1449
<DataHoarder> hello
<jpk68> Hello
<sneedlewoods> Hey
<jberman> waves
<jpk68> Me: worked on review comments, submitted a few PRs, updating AUR packages for Cuprate, doing some HW wallet testing for SNeedlewoods, attempted to replace GNU Readline with linenoise in epee
<rbrunner7> Alright, what is there to report about the 2 last weeks?
<rbrunner7> Last week's meeting fell victim to a Matrix server which was down ...
<sneedlewoods> received lots of reviews for #9464, #10232, #10233 and #10819 and working through those
<rbrunner7> Yeah, you were committing almost daily
<sneedlewoods> sorry for the annoyance
<rbrunner7> @dangerousfreedom left a detailed report in this room earlier today. It seems he has reached quite some milestone, with a first working version of his MoneroInflation update for FCMP++. See e.g. here: https://github.com/monero-project/meta/issues/1449
<rbrunner7> Oh, no, wrong of course. This: https://github.com/DangerousFreedom1984/monero_inflation_checker
<jberman> I worked mostly on Serai this past week, no significant update on my end re: FCMP++. Checking back up on things today
<rbrunner7> He also made a post on Reddit about it: https://old.reddit.com/r/Monero/comments/1w3hcos/monero_inflation_checker_fcmp/
<DataHoarder> is the Python port of monero-oxide AI?
<tobtoht> I've been busy replacing Guix with Stagex, and glibc with musl+mimalloc for release builds. Benchmarks so far show greatly reduced memory usage for beta-stressnet sync and better performance on checkpointed syncs. https://github.com/monero-project/monero/pull/10223
<jpk68> +1
<sneedlewoods> +1
<rbrunner7> I don't read everything carefully, but I think he said something about no large-scale vibe coding. Not sure which parts he meant.
<ravfx:xmr.mx> Talking about monero oxide, it's it OK to start making a new wallet using that, instead of wallet2?
<DataHoarder> I'm finding large scale AI comments, so that's why I was asking. I have been (manually) been making a Go port of quite the same + other non-port from-scratch implementations which is why I was curious
<jpk68> @ravfx:xmr.mx: I think you'd want to be using monero-wallet-util instead, but a few projects are seemingly adopting it already
<jbabb> +1
<jpk68> https://github.com/monero-oxide/monero-wallet-util
<boog900> @ravfx:xmr.mx: it has been audited  
<rbrunner7> He might see your question here, DataHoarder ...
<ravfx:xmr.mx> oh cool, thanks for all answers
<rbrunner7> Jumping ship, eh? :)
<jberman> I'd use monero oxide over wallet2 if I was presented with the choice today fwiw
<ravfx:xmr.mx> +1
<DataHoarder> I made my own tooling to avoid wallet2 >.<
<jberman> gonna be quite a few things to need to work through though that wallet2 handles out of the box
<boog900> +1
<boog900> yeah, monero-oxide is not the same level of wallet lib as wallet2 
<jberman> like wallet state management, reorg handling, storing the wallet files encrypted, and a whole lot more
<rbrunner7> Sounds like some chances to shoot into your feet ...
<DataHoarder> yeah, it's utilities/scanners that can be used to make a wallet2 equivalent or better
<jbabb> +1
<boog900> +1
<jbabb> monero-oxide: monero blockchain impl
<jbabb> monero-wallet: wallet core implemented with the above
<jbabb> monero-wallet-utils: even more wallet tools
<jbabb> there's still a lot of gap to fill between those and wallet2[... more lines follow, see https://mrelay.p2pool.observer/e/lqCblKYLQzZCaXVO ]
<rbrunner7> Might be quite some way until things settle on a new wallet file format that is portable between apps, based on monero-oxide
<jbabb> you can import the wallet2 cpp files etc into monero-oxide et al or just transfer the relevant key material?
<rbrunner7> Or maybe that won't happen again, and it's restoring with seed if you change apps
<jpk68> @rbrunner7: Or a new one could be standardized, maybe using an actual KDF
<jbabb> @jbabb: and to be clear: I mean, with a custom reader.  I have code for this .keys->monero-wallet somewhere, let me find it...
<rbrunner7> I also have a subject that I want to bring up: I wonder how to bring my Polyseed PR over the finishing line and make it merge-ready. This here of course: https://github.com/monero-project/monero/pull/10765
<rbrunner7> A lot of people have reviewed and contributed, but now it's question how to walk the last few meters, so to say
<rbrunner7> Maybe selsta and/or @tobtoht:monero.social can have a look about the state and give some advice?
<rbrunner7> @jpk68: You talked about going through some points that an AI based review has found and submit what passes a first smell test? Is that still in the works?
<rbrunner7> And I just saw today that I have to rebase
<jpk68> @rbrunner7: Apologies, I will get around to that soon. Though I don't think it's found anything too noteworthy that hasn't been surfaced already.
<rbrunner7> +1
<sneedlewoods> Wanted to do a final review, but was too busy with my PRs. I can try to prioritize it this week
<rbrunner7> Ah, and I guess I wait for tevador's Polyseed licensing getting merged so that I can update the Polyseed submodule
<vtnerd> My apologies for being late to the meeting - @tobtoht:monero.social: are we dropping guix for stagex ? I installed guix on a purism box man, so much pain lol
<rbrunner7> *Polyseed re-licensing
<tobtoht> @vtnerd: That is the plan. No more pain.
<vtnerd> Ok, I guess I'm keeping this crazy box for stagex builds then, it's been interesting learning guix as an os
<jbabb> for wallet2 .keys files -> monero-oxide-land: https://github.com/ManyMath/monero-rust/blob/staging/rust/monero-rust/src/wallet_keys_file.rs
<rbrunner7> Alright, seems I will have some work still to do for that PR
<rbrunner7> So, anything left to discuss today?
<jpk68> I have a sort of open-ended question regarding some work I had planned to do, if that's fine
<rbrunner7> Shoot, we have still time to fill the hour :)
<jpk68> In my most recent CCS, I proposed working on integrating the Tor Control protocol into monerod, which would allow for automatic management and monitoring of Tor connectivity. Unlike I2P SAM, Tor Control isn't a replacement for SOCKS, and instead works alongside it.
<jpk68> However, I have recently become unconvinced that this integration is worthwhile, for a few main reasons:
<jpk68> 1. The protocol is being phased out in favour of a new JSON-based standard, which comes with Arti (a newer Tor implementation in Rust). Tor Control is only supported in the 'legacy' C implementation of Tor, which will also be deprecated in a few years.[... more lines follow, see https://mrelay.p2pool.observer/e/g5rFlKYLaUYtWEp3 ]
<jpk68> Open to feedback on this; there may be something else that is in greater need of more people working on it :)
<rbrunner7> Would that also need a bunch of new monerod interactive console commands and startup parameters? We have quite a number of those already ...
<jpk68> Not sure about console commands, but it would probably need one or two more startup flags, yes
<rucknium> @jpk68: I didn't see a great need to add Tor Control.
<jbabb> jpk, do you have a link to the new spec?  I see the old at https://spec.torproject.org/control-spec/index.html , might be helpful for context?  makes sense to move to arti to this rustacean but I know TC vs the new spec
<jpk68> @jbabb: https://people.torproject.org/~nickm/volatile/rpc-reference.html
<jbabb> +1
<jbabb> s/vs/whereas I'm new to
<jpk68> I think it could be somewhat useful, though it's worth noting that Arti is still considered somewhat 'unstable' for the time being
<jpk68> Not sure if people think this is something worth having in the core codebase; would be good to hear opinions :)
<rbrunner7> But on the other hand we would get more code, new dependencies, some more config
<jpk68> I don't think any dependencies would be required; I would just write it in C++ with existing machinery
<rucknium> Why would a Monero user want to control Tor circuits through monerod?
<jbabb> personally I like monerod and potentially more tools being more aware of if it has a real/alive tor connection
<jpk68> @rucknium: It can create ephemeral hidden services, rather than having the user manually set them up.
<rucknium> More knobs to twist so YouTubers have more things to fill their videos? :P
<jpk68> +1
<jbabb> jpk, you'd know better: what's the state of a killswitch if a tor conn drops etc?  have you looked into that?
<rucknium> @jpk68: I guess that's a little more convenience.
<jpk68> @jbabb: What do you mean? You can't run the daemon purely through Tor, at least not while syncing the chain
<jpk68> So, unlike something similar to Mullvad's kill switch, you'd just not be able to send transactions/some peer data anymore
<jbabb> +1
<jbabb> like if you are trying to broadcast a tx over tor, is there awareness of the state of the tor connection?  so if it goes down it doesn't transmit?  I haven't looked into this area in years and forget
<jbabb> anyways, my main point is just that that's an important function to work towards or maintain
<jpk68> I think most of that is opaque when using a regular Tor SOCKS proxy, and the Tor daemon itself will take care of that
<jpk68> @jbabb: Yes, that would be nice, if possible
<rbrunner7> Maybe you could put up a GitHub issue to hopefully get some feedback from people not attending right now
<jpk68> +1
<rbrunner7> In addition to the discussion here
<vtnerd> Tor socks generally does the "right thing" iirc, as in it generates a new circuit for each socks connection
<vtnerd> The tor browser doesn't use the control connection afaik, so it's designed with that use case in mind 
<rbrunner7> Regarding other things worthwhile to work on, I think we will have plenty of those in connection with FCMP++ and Carrot hardfork, but it may still take a while until it becomes clear what it really is
<jbabb> +1
<jpk68> Yes, if anyone has odds and ends they think I'd be qualified to work on, or PRs that need reviews, just throw them at me ;)
<rbrunner7> Alright. That flag is planted :) I think we can close the meeting proper here. Thanks everybody for attending. Read you again next week - if the Matrix server allows it lol
<sneedlewoods> +1
<jpk68> +1
<sneedlewoods> thanks everyone
<DataHoarder[m]> @rbrunner7: funnily restarted the bridge about 35s before the meeting for some updates :)
<rbrunner7> Oh. I use to take the meeting content from IRC to format it into the meeting log.
<rbrunner7> But have to say, the bridge works quite well now, with plenty of little details that "just work right". Solid.
````


# Action History
- Created by: rbrunner7 | 2026-08-30T04:37:26+00:00
- Closed at: 2026-08-31T18:56:31+00:00
