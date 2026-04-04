---
title: Monero Research Lab Meeting - Wed 14 January 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1324
author: Rucknium
assignees: []
labels: []
created_at: '2026-01-13T23:03:51+00:00'
updated_at: '2026-01-27T23:11:39+00:00'
type: issue
status: closed
closed_at: '2026-01-27T23:11:39+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Spy nodes](https://github.com/monero-project/meta/issues/1124).

4. [FCMP and CARROT reviews and audits status](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).

5. Post-FCMP scaling concepts.

6. [FCMP alpha stressnet](https://monero.town/post/6763165).

7. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1321 

# Discussion History
## Rucknium | 2026-01-20T23:08:05+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1324     

> __< rucknium >__ 1. Greetings     

> __< vtnerd >__ Hi     

> __< jberman >__ waves     

> __< rbrunner >__ Hello     

> __< articmine >__ Hi      

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Announced new MRL spy node ban list: https://github.com/monero-project/meta/issues/1124  https://monero.town/post/7271760 . Some fixes to moneronet.info     

> __< jberman >__ me: we released v1.5 of the alpha stressnet which mitigated OOM's and fixed a number of major issues on the stressnet (and includes GUI binaries), and I upstreamed a PR for the server connection code (to solve a segfault caused by xmrig on stressnet)     

> __< jeffro256 >__ Howdy     

> __< vtnerd >__ Me: currently focused on why asan is failing in master branch      

> __< jeffro256 >__ Me: reviewing the proposed scaling changes and working on an implementation. Once a couple of these issues get resolved on #44, a PR should be ready to go.     

> __< rucknium >__ 3. Spy nodes (https://github.com/monero-project/meta/issues/1124).     

> __< rucknium >__ I pushed out the new ban list announcement to GitHub and monero.town: https://github.com/monero-project/meta/issues/1124  https://monero.town/post/7271760  Reddit post should be going up soon.     

> __< rucknium >__ I made a little checklist of people & projects to inform about the ban list. Most of it is "automatic" since they reference the ban list URL instead of maintain their own copy.     

> __< jeffro256 >__ I verified that all the new subnets in the list contained an excessive amount of spy IPs as identified by the p2p-proxy-checker app     

> __< rucknium >__ Thanks, jeffro256:monero.social , hinto:monero.social  , and syntheticbird:monero.social  for adding their PGP signatures to the ban list repo     

> __< jeffro256 >__ Nice on that checklist to update     

> __< rucknium >__ * https://github.com/shermand100/PiNodeXMR/blob/master/home/pinodexmr/setup.sh#L746     

> __< rucknium >__ * https://github.com/greyhat-academy/lists.d/commit/f036e9b094ef0cba99bada1beae97aa64df0fdbd     

> __< rucknium >__ * https://github.com/MoneroNodo/Nodo/blob/master/update-banlists.sh#L15     

> __< rucknium >__ * https://github.com/sethforprivacy/simple-monerod-docker/blob/main/Dockerfile#L138     

> __< rucknium >__ ^ These automatically will get the new ban list     

> __< rucknium >__ Need to also inform wallet developers who host their own nodes, like Cake and Stack.     

> __< rucknium >__ selsta helped update the DNS-disseminated ban list. The old one was completely replaced with the new MRL ban list since none of the old nodes are active anymore.     

> __< syntheticbird >__ Always a pleasure digging up my drives for my PGP key > <rucknium> Thanks, jeffro256:monero.social , hinto:monero.social  , and syntheticbird:monero.social  for adding their PGP signatures to the ban list repo     

> __< rucknium >__ https://www.nslookup.io/domains/blocklist.moneropulse.se/dns-records/     

> __< rucknium >__ Because of the DNS ban list update, https://moneronet.info/ now shows that 50 percent of honest nodes are running the new ban list. That's because 50 percent of honest nodes have the DNS ban list enabled.     

> __< rucknium >__ I was surprised when I saw the big increase. I thought it was a false reading, but then I checked if the DNS records had been updated :)     

> __< rucknium >__ The network scanner cannot know directly what ban list nodes are using, since nodes don't provide that info to outsiders. But it can be approximately inferred by checking which IP addresses nodes share as their (partial) peer lists when they perform a Levin handshake in the initail node connection.     

> __< rucknium >__ initial*     

> __< rucknium >__ I cut the DNS ban list line in the chart in early December because it was showing all honest nodes had the DNS ban list enabled. That occurred because all of the nodes on the DNS ban list disappeared from the network, so no honest nodes shared them in the Levin handshake.     

> __< rucknium >__ I don't know how I'll show the info now that the DNS and MRL ban lists are the same. I will think of something.     

> __< boog900 >__ we will need need some sacrificial nodes to add to one list but not the other /s     

> __< rucknium >__ Honest nodes seem to be getting less concentrated in Autonomous Systems (ASes).     

> __< rucknium >__ The Herfindahl-Hirchman Index of AS concentration has decreased from 0.017 to 0.013 in the last 6 months.     

> __< rucknium >__ The HH index is the sum of the squares of the "market share" of each AS.     

> __< rucknium >__ It's used a lot in market concentration analysis in economics.     

> __< rucknium >__ Anything more on spy nodes?     

> __< rucknium >__ New ban list announcement now up on Reddit, thanks to plowsof:monero.social : https://www.reddit.com/r/Monero/comments/1qct02j/run_your_node_with_the_new_mrl_spy_node_ban_list/     

> __< rbrunner >__ Let's see how long it takes until the first "But centralization" comment :)     

> __< rucknium >__ 4. FCMP and CARROT reviews and audits status (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).     

> __< rucknium >__ IIRC, jberman:monero.social  maintains the linked ^ spreadsheet. Is all the info up to date?     

> __< jberman >__ I believe so, but I'll need to circle back with kayabanerve:matrix.org  and sgp_:monero.social     

> __< rucknium >__ I see two ongoning items: "GBP proof review round 2" by Cypher Stack and "helioselene review and audit" by Veridise.     

> __< rucknium >__ And four blanks: "EC Divisors impl audit", "GSP impl audit", "Torsion check review", and "Integration audit"     

> __< jberman >__ Yep, on the two ongoing: I don't recall an update on those. Will follow up     

> __< rucknium >__ Thanks, jberman:monero.social .     

> __< rucknium >__ The spreadsheet only covers FCMP. jeffro256:monero.social , can you share info about Carrot reviews and audits?     

> __< jeffro256 >__ One of the firms may or may not be performing the carrot_core audit pro bono, will wait until they finish on that, or bail, to make it public. Don't want to put pressure on them for free work ;)     

> __< jeffro256 >__ If that fails, one of the other firms is willing to do the audit for a 45% discount.     

> __< jberman >__ jberman: Sorry, I do recall Veridise giving their review on helioselene which led to changes that we discussed here too. I'll update the spreadsheet and we'll have a better discussion on FCMP++ research / audit status next week     

> __< jeffro256 >__ 40%, sorry      

> __< rucknium >__ jeffro256:monero.social: Thanks. Is that the last thing that CARROT needs?     

> __< jeffro256 >__ It depends on if we want to audit carrot_impl before launch. It doesn't contain much crypto code by itself, but it's the code that is called from wallet2     

> __< jeffro256 >__ It contains a lot of tx construction logic, device interfaces, tx scanning logic, etc.      

> __< jeffro256 >__ I wouldn't require it as a blocker for launch, personally, but it would be nice to get around to it at some point. carrot_impl changes a lot, lot faster than carrot_core at this stage of development, so IMO it wouldn't make sense to try to audit it right now.     

> __< jberman >__ I think it's reasonable to start with carrot_core with 100% effort / focus as an isolated audit item, and then progress to carrot_impl especially once it's in a more settled state     

> __< jberman >__ regarding auditing carrot_impl before launch or not, I think that is a decision we can make at a later time if it comes down to it, but for now aim for beginning the carrot_core audit sooner rather than later     

> __< jberman >__ the sooner the carrot_core audit begins, the better position we're in to have carrot_impl audited before launch anyway     

> __< jeffro256 >__ Also, a lot of things in carrot_impl can be changed after the fact without breaking backwards compatibility, whereas that isn't the case with carrot_core. Most changes to carrot_core would necessitate a separate scanning path at least     

> __< rucknium >__ Sounds good to me.     

> __< rucknium >__ I'll reiterate that I think it would be a good idea to get a third independent review of EC Divisors to complement the Veridise and Cypher Stack reviews, given how crucial its role is and how challenging the proofs were. I know not everyone agrees with me on that :)     

> __< jberman >__ I agree with you on that     

> __< jeffro256 >__ It would be very parallelizable, which is nice      

> __< jberman >__ I will follow up on that as well     

> __< rucknium >__ How could we make that a reality?     

> __< jeffro256 >__ I think that we should start scoping for a FCMP++ integration audit soon      

> __< rucknium >__ jberman: Very nice. Thank you, jberman:monero.social     

> __< jeffro256 >__ Would like Berman's opinion, of course      

> __< jberman >__ jeffro256: I agree, it's one of my very next tasks to start doing     

> __< jeffro256 >__ I can also start on an outline for that if that helps it along      

> __< jeffro256 >__ The only Rust code we would need to include in-scope is the FFI bindings, right?     

> __< jberman >__ I have some ideas brewing already which I want to get going on soonish too     

> __< jberman >__ jeffro256: I think that would be reasonable yep     

> __< jeffro256 >__ I know that for the carrot_core lib audit, forcing myself to put it in a state worth auditing forced me to fix some last wrinkles with it that I had been thinking about for a while     

> __< jberman >__ I think let's get unbiased hash to point done and preferable the rename from "global output ids" -> "unified ids", and then it should be in good position to begin auditing     

> __< jeffro256 >__ alright fair      

> __< jberman >__ will probably be able to complete both today     

> __< rucknium >__ More discussion on FCMP & CARROT reviews and audits?     

> __< rucknium >__ Is preland:monero.social  here?     

> __< rucknium >__ We will move directly into the stressnet agenda item     

> __< rucknium >__ 6. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< jeffro256 >__ Like I posted above, I have a mostly completed PR for the proposed scaling changes. Note: the dynamic minimum fee-per-byte will be going down ~23% compared to v16, but since FCMP++ txs start at ~4x bigger, the minimum dynamic fee will be going up ~3x.     

> __< jberman >__ v1.5 launched last week, we're now seeing some "tremors" as I'd call them, of some people reporting hiccups. Monitoring to see if they are what I'd consider major blocking issues (something that prevents the wallet/daemon from functioning). I argue that once blocking issues are solved, we should be in good position to move to  [... too long, see https://mrelay.p2pool.observer/e/1aqaudwKVi1zMnNz ]     

> __< jeffro256 >__ jeffro256: Larger FCMP++ txs can be less than 4x the size, and dynamic minimum fee-per-byte goes down quadratically as long-term block median increases, and new scaling changes increase the size of the minimum penalty-free zone size, so the multiple of fee increase from current transactions only goes down from there. I kn [... too long, see https://mrelay.p2pool.observer/e/jrWoudwKOWtyR1E3 ]     

> __< jeffro256 >__ To put it in perspective, a 2x increase in fee-per-byte would be ~6x increase in absolute fee after FCMP++      

> __< rucknium >__ jeffro256:monero.social , the plan you're working on assumes that the FCMP mainnet scaling parameters will be used for beta stressnet, right? (Mainnet stressnet scaling parameters have to be implemented eventually anyway.) So the amount of stress that we will be able to apply to the beta stressnet will be limited to the short-term scaling of FCMP mainet.     

> __< jeffro256 >__ Yes, so far. Should the scaling instead be relaxed to allow for more spam? Pros: may find more breakages faster, Cons: won't be an accurate representation of mainnet performance      

> __< jeffro256 >__ I have my opinion     

> __< jberman >__ I don't think so. I'm pretty strongly in favor of beta using mainnet scaling figures. I think it will help find real breakages sooner anyway because the pool will grow too, which has been its own source of headaches to manage on alpha     

> __< jberman >__ I would be in favor of a distinct always-on stressnet with more relaxed scaling as its own thing to focus on perpetually     

> __< jberman >__ But I don't think it would be maximally useful for FCMP++/Carrot beta     

> __< articmine >__ There is a strong case for beta to follow mainnet on scaling as long as we have a way to accelerate the time frame      

> __< rucknium >__ You could decrease the long term median window from 100,000 blocks to something lower     

> __< articmine >__ The easiest way is to increase the penalty free zone to accelerate time     

> __< articmine >__ While keeping all the other parameters the same      

> __< articmine >__ This simply provides a future mainnet assuming say a 1 year growth rate     

> __< articmine >__ At maximum      

> __< jeffro256 >__ rucknium: I like this idea, personally      

> __< jberman >__ I'm still in favor of mainnet params, but decreasing the LT window for beta seems acceptable to me     

> __< articmine >__ Go to say 10000 bytes?     

> __< jeffro256 >__ articmine: This only boosts you N times in the short-term, though, right? If you wanted to break out of it you'd still have to wait ~2.5 months to increase the median      

> __< articmine >__ Yes that is still the issue      

> __< articmine >__ So the shorter ML can work      

> __< jeffro256 >__ How about a long-term window of 6 days? That's 2x the default mempool expiry time      

> __< rucknium >__ Any predictions of how long beta stressnet will be active?     

> __< articmine >__ That is like 5000 blocks      

> __< rucknium >__ 6 days seems too short to me     

> __< jeffro256 >__ That means a 3 days of non-spam to increase LT median      

> __< jeffro256 >__ *non-stop spam     

> __< jberman >__ rucknium: I'm going to be ultra conservative with this and say 9 months. It would probably be helpful to keep it active even once testnet is live, just to have a place where people can spam to their heart's content     

> __< rucknium >__ I think at least we need the short term scaling to fully expand before the long-term scaling kicks in. At least, that "sounds" right to me.     

> __< rucknium >__ The speed of short-term scaling is affected by the fees of the spam txs.     

> __< jeffro256 >__ Short-term scaling is 100 blocks IIRC, which is 3 hours and 20 minutes      

> __< articmine >__ There is a strong case for keeping beta stressnet even longer to identify issues well ahead of mainnet      

> __< jberman >__ articmine: ya that's fine with me     

> __< articmine >__ jeffro256: No need to change that for stressnet     

> __< jeffro256 >__ rucknium: So short-term scaling is still ~43x shorter than long-term if we set long-term to 6 days      

> __< rucknium >__ jeffro256: That's how long it takes for the median to start adjusting, but to hit the short-term ceiling takes longer.     

> __< jeffro256 >__ Oh I see what you're saying      

> __< rucknium >__ Setting long-term median to 2 weeks (which would start to raise the short-term ceiling after 1 week in heavy spam), would sound good to me. I keep in mind what jberman:monero.social  said about encountering and fixing issues/bugs in their "scaling sequence".     

> __< rucknium >__ But I am persuadable :)     

> __< articmine >__ So 10000 blocks      

> __< jeffro256 >__ Since the short-term surge factor is being changed from 50x->8x, it should take 100*log2(8) = 300 blocks to hit short-term ceiling I think      

> __< jeffro256 >__ rucknium: This is fine with me so long as people are ready to spam non-stop for >1 week      

> __< articmine >__ One has to also allow for the final 2x so 400 blocks      

> __< rucknium >__ jeffro256: That's feasible, especially with all the stability fixes that you and jberman:monero.social  have worked on 🙏     

> __< jeffro256 >__ Awesome. Anyone object to setting the long-term window to 10080=142430 blocks?     

> __< jeffro256 >__ ughh matrix formatting.. = 14x24x30     

> __< jberman >__ no objection     

> __< rucknium >__ Sounds good to me     

> __< jeffro256 >__ Will take a little bit of business logic to handle switching long-term window lengths, but I'll see if I can implement it today      

> __< rucknium >__ Thanks a bunch, jeffro256:monero.social     

> __< jeffro256 >__ B/c to prevent premature HFs from testnet, it will need to respect old long-term window before v17 activates. Anyways, will figure it out      

> __< rucknium >__ Anything else on stressnet?     

> __< jberman >__ nothing from me     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< articmine >__ Thanks      

> __< jberman >__ thank you!     

> __< jeffro256 >__ Thanks everyone!     

> __< gingeropolous >__ guh, missed the meeting. im still working on monerosim. i've got it semi-working with 1k monerod agents. Turns out starting 1000 monerods takes a while :/ .      

> __< rottenwheel:unredacted.org >__ Ayo.     

> __< rottenwheel:unredacted.org >__ > Hi Cake. There is a new version of the MRL ban list. The spy nodes changed their IP addresses: https://raw.githubusercontent.com/Boog900/monero-ban-list/refs/heads/main/ban_list.txt     

> __< rottenwheel:unredacted.org >__ > https://www.reddit.com/r/Monero/comments/1qct02j/run_your_node_with_the_new_mrl_spy_node_ban_list/     

> __< rottenwheel:unredacted.org >__ > Please update your remote nodes with the new ban list. Thank you.     

> __< rottenwheel:unredacted.org >__ Someone is asking...     

> __< rottenwheel:unredacted.org >__ > is it possible to refresh ban list without restarting monerod ?     

> __< rottenwheel:unredacted.org >__ If anyone can chime in, I can relay the information.     

> __< plowsof:matrix.org >__ if they have --enable-dns-blockslist at start up or in config they will be using the same list already https://libera.monerologs.net/monero-research-lab/20260114#c645239 , there is a set_bans daemon rpc command to add these manually 1 by one, but i have not tested it personally, it accepts a seconds param which i would set [... too long, see https://mrelay.p2pool.observer/e/7aPmwdwKb3YwNVdV ]     




# Action History
- Created by: Rucknium | 2026-01-13T23:03:51+00:00
- Closed at: 2026-01-27T23:11:39+00:00
