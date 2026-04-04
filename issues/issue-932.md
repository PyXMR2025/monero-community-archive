---
title: Monero Research Lab Meeting - Wed 22 November 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/932
author: Rucknium
assignees: []
labels: []
created_at: '2023-11-22T14:35:29+00:00'
updated_at: '2023-12-17T17:14:51+00:00'
type: issue
status: closed
closed_at: '2023-12-17T17:14:51+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#928 

# Discussion History
## plowsof | 2023-12-17T16:59:51+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting in this room in one hour.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/932     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< vtnerd >__ hi     

> __< rbrunner >__ Hello     

> __< g​ingeropolous:monero.social >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< vtnerd >__ me: adding to LWS unit tests in preparation for adding "chain hardening" to LWS     

> __< g​ingeropolous:monero.social >__ having fun with fail2ban and monerod logs     

> __< vtnerd >__ not sure its worth do chain hardening - there's really no way great to determine if we've been forked away for instance     

> __< r​ucknium:monero.social >__ me: OSPEAD, as normal. Want to remind everyone while the CCS next steps post-theft are being discussed, the MAGIC Monero Fund is accepting proposals as usual: https://monerofund.org/apply     

> __< vtnerd >__ but the unit tests are worth it (the core scanner has yet ot be unit tested)     

> __< r​ucknium:monero.social >__ vtnerd: What is chain hardening?     

> __< vtnerd >__ verifying the hashes and PoW work in LWS itself. LWS currently (like wallet2 in monero) assumes the info from the daemon is valid     

> __< vtnerd >__ you can currently send blocks/txes with no connection to each other (as evident by the tests I just wrote)     

> __< vtnerd >__ you can verify just about everything, but could still be on a forked chain     

> __< r​ucknium:monero.social >__ Thanks. Is this related to the vulnerability reported by tevador this year? And would the proposed changes to RandomX help?     

> __< g​ingeropolous:monero.social >__ so this would be the usecase of user A connecting to user B's LWS server (so 3rd party LWS)?     

> __< vtnerd >__ the use case would be someone pointing LWS to a daemon they don't control     

> __< vtnerd >__ it may always be a bad idea, so I'm mixed on adding the feature to LWS. Depends on how much it wrecks the codebase to add it     

> __< g​ingeropolous:monero.social >__ yeah the only "solution" ive thought of is just connecting to multiple servers to get a consensus, sorta like electrum does     

> __< r​ucknium:monero.social >__ 3) Discussion. What do we want to discuss?     

> __< vtnerd >__ yes, that should help with verifying the chain tip, etc     

> __< h​into.janaiyo:matrix.org >__ hello     

> __< g​ingeropolous:monero.social >__ hello. re: discussions, are the itinerary topics on the github issue still relevant? or is that just the same its been     

> __< j​effro256:monero.social >__ Howdy sorry I'm late     

> __< g​ingeropolous:monero.social >__ because it still has the 10-block lock is an item of discussion     

> __< r​ucknium:monero.social >__ Still relevant, but no activity on them recently.     

> __< r​ucknium:monero.social >__ You can say "We should reduce/increase/eliminate the 10 block lock for X reason."     

> __< r​ucknium:monero.social >__ I have a question that jeffro256 might help with: With a new probability distribution, would it be a problem to revert the behavior of the wallet2 decoy selection algorithm to choose decoys starting from the 10 block lock instead of from chain tip? And eliminate the reallocation to a uniform distribution for the recent spend window?     

> __< r​ucknium:monero.social >__ So, similar to pre-September 2021     

> __< j​effro256:monero.social >__ jberman: would probably know best since he implemented those changes.     

> __< r​ucknium:monero.social >__ Anything else to discuss?     

> __< j​effro256:monero.social >__ https://www.getmonero.org/2021/09/20/post-mortem-of-decoy-selection-bugs.html     

> __< j​effro256:monero.social >__ Heres the relevant blog post     

> __< j​effro256:monero.social >__ I don't think removing the uniform spend window would be a problem as long as we can empirically verify that the curve by itself does enough to match REAL monero spends in practice, including the 10-block-lock     

> __< j​effro256:monero.social >__ But in reality that might be hard     

> __< r​ucknium:monero.social >__ IIRC the process was: Moser et al. (2018) estimated the gamma distribution from chain time. The gamma with the estimated parameters had a mode somewhere between 0 and the 10 block lock. I think it looked like that since they estimated it on data when the 10 block lock was not required by consensus. So a few wallets produced transactions with ring members before the 10 block lock.     

> __< j​effro256:monero.social >__ Think about how many users/services sit there and wait exactly the shortest amount of time available before they can spend     

> __< who-biz >__ why not guarantee an upper and lower bound for decoy selection, that rolls window with chain progression?     

> __< v​tnerd:monero.social >__ They used BTC as a model     

> __< vtnerd >__ and compared against monero spends that could be determined     

> __< r​ucknium:monero.social >__ IIRC (and I'm pretty sure), they did not use BTC for the final parameters that Monero uses. They determined the real spend of many XMR transactions (about 60-80%?) and estimated from the real XMR data.     

> __< vtnerd >__ I think there has always been a 10 block limit     

> __< r​ucknium:monero.social >__ w​ho-biz: Could you explain your idea more?     

> __< j​effro256:monero.social >__ Who-biz: would you be able to explain more , I'm not quite sure I understand     

> __< j​effro256:monero.social >__ Jinx     

> __< who-biz >__ I mean, we already have the 10 block limit. Why not make the lower bound of selection more uniform too? unless I'm missing something here, it would seem to level the playing field a bit for all auto-decoy-selection users     

> __< g​ingeropolous:monero.social >__ vtnerd: it was wallet enforced. became consensus enforced in 2019 ( I think) https://github.com/monero-project/monero/commit/a444f06e53b218cc8bd091e5283828beb3e7d9af     

> __< g​ingeropolous:monero.social >__ oh wait maybe i misread what u were sayin     

> __< r​ucknium:monero.social >__ BTC doesn't make sense as the data used to produce the gamma distribution parameters of Moser et al. (2018) since BTC usually (always?) has a monotonically decreasing empirical probability distribution, at least in the area close to chain tip. The gamma parameters that Moser et al. estimated produces a probability distribution function that rises first and then decreases (not monotonic).     

> __< j​effro256:monero.social >__ Rucknium one thing that might be worth investigating is whether the recent spend window needs to be so wide     

> __< j​effro256:monero.social >__ Because the recent spend window captures all spends from 10 blocks or less by is spread out 15 blocks wide which might not be realistic     

> __< r​ucknium:monero.social >__ My plan is to eliminate the concept of recent spend window.     

> __< r​ucknium:monero.social >__ But if there is a really good reason to keep it, then we could.     

> __< j​effro256:monero.social >__ Like if I'm sitting there waiting for the 10 block lock to go away it doesn't make sense that I'd somehow skip 30 minutes after it unlocked     

> __< vtnerd >__ I somehow didn't realize moo added this consensus change later. regardless, the early data would then be skewed because wallet2 was following the rule     

> __< r​ucknium:monero.social >__ Having the pre-10 block part of the distribution re-allocated as a uniform distribution is a good first approximation, but it creates an unnatural discontinuity. A drop off where the uniform distribution ends.     

> __< who-biz >__ adding to consensus was a good idea. pleased to see this also. I recall 2018 this could be easily worked around by simply changing a constant     

> __< r​ucknium:monero.social >__ Look at page 3: https://www.overleaf.com/read/ndbtkwrbrdjq     

> __< j​effro256:monero.social >__ Who-biz what do you mean by "uniform" and " lower bound" and "autos decoys selection" here?     

> __< r​ucknium:monero.social >__ At about output index 1,000 there is a drop in the probability. (It's different when you are at different block heights.)     

> __< j​effro256:monero.social >__ Oh I agree that the recent spend window could be made much better and smooth in with the gamma curve     

> __< who-biz >__ jeffro256: "uniformity" I don't mean distribution. I mean that the decoys should be selected from the same window of outputs (timewise) for all users, and reducing this variation would probably help strengthen privacy     

> __< who-biz >__ "lower bound": I mean introducing a "select outputs more recent than x utxos ago" or "x blocks ago"      

> __< j​effro256:monero.social >__ However i don't think  we should remove all conditional code that handles decoy selection during the 10 block locked window since that rule itself will create weird discrete artifacts that we should anticipate     

> __< who-biz >__ "auto decoy selection": not manually selecting your ring members, and not blacklisting certain outputs. default wallet settings     

> __< r​ucknium:monero.social >__ w​ho-biz: Do you mean that a specific decoy selection algorithm should be required as a consensus or tx relay rule instead of wallet software choosing it?     

> __< who-biz >__ Correct     

> __< who-biz >__ Or at least an enforcement of valid bounds for selection of decoys, if you still want to allow some implementation-specific legroom     

> __< r​ucknium:monero.social >__ I think it's a good idea. There is an MRL GitHub issue about it: https://github.com/monero-project/research-lab/issues/87     

> __< who-biz >__ nice, will read     

> __< who-biz >__ oh, good :) glad this has been discussed. worth pursuing imo.     

> __< h​into.janaiyo:matrix.org >__ maybe off-topic: i've been thinking about air-gapped data transmission solutions for a while and due to the CCS incident i've been working on stuff again     

> __< h​into.janaiyo:matrix.org >__ specifically data over sound - mapping audio frequencies to bytes such that devices with speaker/mic can transmit data     

> __< r​ucknium:monero.social >__ hinto: Great to hear :)     

> __< h​into.janaiyo:matrix.org >__ signed pgp messages, or monero tx's could be signed like this - in around 2min~ from rough calculations     

> __< h​into.janaiyo:matrix.org >__ there's already a c++ impl of this including some reed-solomon error correction https://github.com/ggerganov/ggwave     

> __< h​into.janaiyo:matrix.org >__ almost like a TCP over sound     

> __< j​effro256:monero.social >__ Doesn't this just turn it back into a hot wallet with an unconventional "wire"?     

> __< h​into.janaiyo:matrix.org >__ i'm not sure if i should pursue this though, the target is extremely niche     

> __< j​effro256:monero.social >__ The threat model is the same as Bluetooth or WiFi yeah?     

> __< h​into.janaiyo:matrix.org >__ jeffro256: the flow would be: hot wallet -> plays raw_unsigned_tx over audio -> cold_wallet parses audio data into tx, signs it -> cold_wallet play signed_tx -> hot wallet broadcasts to network     

> __< h​into.janaiyo:matrix.org >__ the thread model is basically nothing, since the spend key would never leave the cold machine     

> __< h​into.janaiyo:matrix.org >__ it would be physical security at that point     

> __< who-biz >__ hinto: any idea as to range of sound->data reliability?     

> __< j​effro256:monero.social >__ Why not use an Ethernet cable to talk between machines ?     

> __< h​into.janaiyo:matrix.org >__ the c++ impl has 8-16 bytes per second with error correction     

> __< who-biz >__ if it is less distance than wifi/bluetooth... slightly different but in concept jeffro256 is making sense     

> __< h​into.janaiyo:matrix.org >__ which would take around 2min for a 40kb unsigned monero tx     

> __< vtnerd >__ who-biz: why would sound be better than usb? in either case there is some risk of bug     

> __< h​into.janaiyo:matrix.org >__ er, actually more than that, my impl seems to be around 20-30 bytes per sec     

> __< vtnerd >__ or hinto: sorry wrong person     

> __< h​into.janaiyo:matrix.org >__ there's been concerns with any physical connection, e.g usb/sd card/wire     

> __< h​into.janaiyo:matrix.org >__ qr codes are also viable but annoying to use practically     

> __< j​effro256:monero.social >__ Why is sound different ?     

> __< vtnerd >__ yes, but the threat model is identical: the reader on the airgapped machine has a vulnerability that can be exploited     

> __< vtnerd >__ and Im not certain that an audio algorithm would be simpler than a usb implementation (although perhaps not)     

> __< vtnerd >__ qr codes might an improvement, but its splitting hairs there too     

> __< h​into.janaiyo:matrix.org >__ it would boil down to the safety of the audio input -> byte software     

> __< vtnerd >__ the electrical signal thing is likely just a red herring     

> __< vtnerd >__ yes, which is the same for usb? you have the same exact threat     

> __< h​into.janaiyo:matrix.org >__ usb in general is spooky since it can it is a just a bus that can do anything     

> __< j​effro256:monero.social >__ That's the exact same threat model as USB/Ethernet/WiFi/Bluetooth but those mediums tend to be a little bit more well studied     

> __< vtnerd >__ yeah Im not convinced that the audio technique is trivial in terms of implementation, but perhaps less than a full usb stack     

> __< j​effro256:monero.social >__ Its a bus that can do anything only if the code interfacing with it let's it do anything     

> __< vtnerd >__ you can still compile the linux kernel without many usb features, reducing the attack surface greatly     

> __< j​effro256:monero.social >__ If you have a hardened USB controller then it won't let the USB do anything     

> __< h​into.janaiyo:matrix.org >__ jeffro256: the usage would be on a cold device     

> __< vtnerd >__ I think he understands the situation, just pointing out the same thing I am. That if you have two-way communication then there's always a chance of lost funds     

> __< j​effro256:monero.social >__ If you have a constantly listening mic and speaker ready to receive and transmit instructions and byte data then your wallet is no longer "cold"     

> __< vtnerd >__ yeah the proble is complex reading/writing and two-way comms     

> __< vtnerd >__ *problem     

> __< r​ucknium:monero.social >__ There would be a physical confirmation by the user on the airgapped device, right?     

> __< h​into.janaiyo:matrix.org >__ to be fair, the audio -> byte code would be maybe a few hundred lines     

> __< h​into.janaiyo:matrix.org >__ Rucknium: of course, not always listening - you would init the back-and-forth     

> __< h​into.janaiyo:matrix.org >__ i would be shocked if somewhere were to create an exploit over this that somehow made your cold device spill secrets     

> __< h​into.janaiyo:matrix.org >__ someone*     

> __< vtnerd >__ few hundred lines seems optimistic, you'd probably need checksums and some other stuff too     

> __< r​ucknium:monero.social >__ hinto: I assume you are aware of the animated QR code projects: MoneroSIgner, Anonero, Feather.     

> __< h​into.janaiyo:matrix.org >__ yes - i pushed for monerosigner actually     

> __< h​into.janaiyo:matrix.org >__ trying to make qr codes work is very hard     

> __< vtnerd >__ I guess, and in both cases you still are probably interacting with complex audio/video drivers, no?     

> __< vtnerd >__ it just feels better because theres no physical "lines" connecting things     

> __< h​into.janaiyo:matrix.org >__ yes, i guess so     

> __< vtnerd >__ I support these projects if people like them, Im just not certain I would bother using them     

> __< j​effro256:monero.social >__ And if you want to make it portable you have to rely on your distros (or homemade) method of distributing firmware     

> __< h​into.janaiyo:matrix.org >__ jeffro256: i'm not sure what this means - the native audio stack would be used     

> __< j​effro256:monero.social >__ I guess because you seem like you want to reduce stack complexity, which is always good, but this might actually  increase it: its USB stack vs mic stack + speaker stack + digital transmission layer on top of analog mediums     

> __< r​ucknium:monero.social >__ How easy is it for malware to hitch hike on a USB and activate itself on another device when plugged in?     

> __< j​effro256:monero.social >__ Dont get me wrong, the idea would be intriguing. It be fun to bring back dial up modem noises for monero wallets :)     

> __< h​into.janaiyo:matrix.org >__ lol that's the first thing i thought of too     

> __< h​into.janaiyo:matrix.org >__ again i'm not advocating for it - just have been messing around with this as an "alternative"     

> __< h​into.janaiyo:matrix.org >__ Rucknium: surprisingly most cases of usb "attacks" are `.inf` script files that windows auto-runs by default on plug-in     

> __< h​into.janaiyo:matrix.org >__ i think ubuntu has this enabled by default as well     

> __< r​ucknium:monero.social >__ We can end the meeting here. Feel free to continue discussing :)     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-11-22T14:35:29+00:00
- Closed at: 2023-12-17T17:14:51+00:00
