---
title: 'Monero Tech Meeting #116 - Monday, 2025-04-14, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1187
author: rbrunner7
assignees: []
labels: []
created_at: '2025-04-11T15:58:02+00:00'
updated_at: '2025-04-14T18:55:30+00:00'
type: issue
status: closed
closed_at: '2025-04-14T18:55:29+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1183).

# Discussion History
## rbrunner7 | 2025-04-14T18:55:29+00:00
```
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1187
<j​effro256> Howdy
<s​needlewoods> hey
<u​nwantedfondue> Hello
<j​berman> *waves*
<v​tnerd> Hi
<r​brunner7> Alright. What is there to report from last week?
<s​needlewoods_xmr> Thanks to mooo again for the memory scanner, made this process a lot easier for me
<s​needlewoods_xmr> AFAICT the wiping works for the most part, but there is at least one issue: If you modify the typed password in any way other than just appending letters (e.g. if you use backspace, delete), it will copy the password and modify the copy, while keeping the other one in memory, similar for arrow key + typing, and selecting text + typing. The way wiping currently works, it will only <clipped 
<s​needlewoods_xmr> affect the password entered most recently.
<j​effro256> Progress made last week on my side was mainly a lot of bug fixes and reworking some of the finer part of wallet2 for the integration like the cold signing protocol and transaction proofs
<s​needlewoods_xmr> I think there is no easy way to ensure the user is not accidentally creating copies without making the UX much worse, e.g. we could override the behavior for key events in `components/LineEdit.qml` (or create a new component `SecretLineEdit.qml` for that matter) to either completely disable those keys, or just wipe the password and let the user enter the entire thing again.
<s​needlewoods_xmr> One hacky way to get around this with awful UX that's already working now: If you mistyped, close the password dialog. That should wipe everything properly, then try again.
<s​needlewoods_xmr> FWIW just pasting the password works fine, meaning the password will get wiped.
<jeffro256> +1F
<j​berman> me: implemented the blinds cache (to cache blinds for FCMP++ calculated in background threads in order to speed up tx construction time), continuing work on it (currently working on serializing blinds so they persist in the wallet cache after calculating), opened a new CCS proposal
<r​brunner7> SNeedlewoods: Still sounds like progress. And I would guess most of the time one does not need to edit the password. I would march on with this if I were you.
<sneedlewoods> +1
<j​berman> is it non-trivial to create a new SecretLineEdit.qml component that does not place the pw in memory but still allows backspace?
<j​berman> or is that internal qt behavior
<s​needlewoods_xmr> afaict that's qt behavior and I have a looked a bit through the qt source, but havn't figured out exactly what's causing this and if we could prevent it somehow
<r​brunner7> Anyway, the part of the password *before* edit will only very rarely be the complete password, no?
<s​needlewoods_xmr> it could be a copy of your password with one letter missing, which would be especially easy to guess if your password is a regular word
<j​berman> fair enough, potentially worth a bit of further investigation, but personally I think this would be pretty acceptable UX that I feel like I've seen before: "or just wipe the password and let the user enter the entire thing again."
<r​brunner7> Yeah, I usually start from scratch as soon as I know that I messed up typing the password ...
<s​needlewoods_xmr> thanks for the feedback
<r​brunner7> jberman: You will have results soon how much speedup, more or less, you get from that blinds cache?
<j​effro256> It would quite impressive if this cache managed to slow things down lol
<r​brunner7> Lol
<j​berman> I think makes sense to just wait until jeffro's CLI/RPC/wallet API integration is complete + combine that with this blinds cache, and then perhaps tobtoht  could give it a go again at that point? tbh a few minutes sounded way too high, there may be something else going on there that warrants a further look
<j​berman> because jeffro's Carrot stuff is slated to get rid of multiple rounds of blinds calculations too
<r​brunner7> I see.
<r​brunner7> Indeed no need to rush and maybe raise false expectations
<j​berman> it doesn't take a few minutes in the CLI on my machine, it's still on the order of seconds on my end, but I do have a good machine
<j​effro256> It takes about 30 second on my craptop
<r​brunner7> Ok. Guess we will see clearer quite soon.
<r​brunner7> Just curious: Anything interesting happened already as a reaction to go public with the contest?
<r​brunner7> That's the Reddit post, btw: https://old.reddit.com/r/Monero/comments/1jvxsyq/fcmp_coding_competition/
<r​brunner7> Ah, the "leaderboard" idea :)
<j​berman> there was one interesting idea a reddit user proposed I would +1: an anonymized leaderboard so people can gauge submissions + we can talk openly about number of submissions / how fast the speed-ups are as the contest is ongoing
<sneedlewoods> +1
<j​berman> seemed like a good idea to me
<r​brunner7> Yes
<j​berman> (for reference: https://old.reddit.com/r/Monero/comments/1jvxsyq/fcmp_coding_competition/mmk24sh/)
<j​effro256> Would the leaderboard include code ? If so, that opens the door to copy cats
<j​berman> no it wouldn't
<r​brunner7> But worst case can get a bit depressing, should there be a slow take-up, or everybody just stays hidden ...
<r​ucknium> Why would a contestant submit early and give competitors an advantage?
<jeffro256> +1
<j​berman> just a ranked table showing submission # and % speed-up
<r​brunner7> Ah, the game theory people spoil the fun :)
<j​berman> answer here: https://old.reddit.com/r/Monero/comments/1jvxsyq/fcmp_coding_competition/mmfnuyu/
<r​brunner7> I guess it's still worth a try.
<j​berman> is there a good option to further incentivize early submissions? Can't really imagine one, so
<j​berman> is what it is?
<j​effro256> Going back to what Rucknium said, how would we even enforce that?
<r​brunner7> 1 XMR for the first submission with more than 5% speedup? Just brainstorming a bit
<r​brunner7> Probably won't sway people, as so much is at stake
<r​brunner7> Maybe some people will do it for their ego alone, to see themselves on the leaderboard
<r​brunner7> Just thought about "Ready player one" ...
<r​ucknium> From the Reddit discussion, it looks like someone has experience with early submission leaderboards, but there is no context for that statement
<r​ucknium> AFAIK, having a leaderboard won't hurt anything, of course
<r​brunner7> Exactly
<r​ucknium> Related: I think the MRC box with the submissions should be off-limits to anyone other than jeffro, jberman, and gingeropolous until after the deadline has passed
<j​berman> this is fine with me, will ping ginger on it
<j​berman> maybe we could include a bonus: if the winning submission was submitted within the first month, they're entitled to a 5-10% bonus
<r​ucknium> The contest was posted on monero.town by a certain character: https://monero.town/post/5816534
<j​effro256> I can see it hurting expectations. If we have a running leaderboard, people will assume that it is somwhat accurate. Then if the actual top-scoring submissions blows all the leaderboard scores out of the water, because they didn't check in with the leaderboard, then perhaps people will feel cheated if they based their likelihood of getting a payout with how high up they were on the leaderboard
<r​ucknium> IMHO, the leaderboard is just cheap talk
<r​ucknium> https://en.wikipedia.org/wiki/Cheap_talk
<r​ucknium> > In game theory, cheap talk is communication between players that does not directly affect the payoffs of the game. Providing and receiving information is free. This is in contrast to signalling, in which sending certain messages may be costly for the sender depending on the state of the world
<j​berman> if there isn't consensus on a leader board, I don't have a strong opinion on it. I'm fine with not including one
<r​ucknium> Maybe a little bit of signaling, since the implementation must be _at least_ as fast as the contestant's actual code
<r​ucknium> I'm not against a leaderboard
<r​ucknium> I mean, no slower than
<r​ucknium> No faster than? Anyway, you know what I mean
<r​brunner7> I think this here "submitted within the first month, they're entitled to a 5-10% bonus" goes a bit too far. I also understand it as a problematic change of a contest that is, in a certain way, already running.
<j​berman> Then I think we keep it as is :)
<r​brunner7> Ok. Is there any other subject to discuss today beyond what was already mentioned?
<r​ucknium> Just keeping hardware wallet implementation in mind:
<r​ucknium> https://forum.zcashcommunity.com/t/binance-is-harmful-for-zcash/50844/25
<r​ucknium> > Binance is currently unable to transfer ZEC out of their cold wallet due to the ongoing issue with Ledger.
<jberman> +1
<r​ucknium> Of course, Binance has delisted Monero, but maybe other service providers also operate this way
<r​brunner7> Wonder how they managed to paint themselves into that corner ...
<s​pirobel:kernal.eu> do all the expensive work on the machine
<s​pirobel:kernal.eu> seems like a ledger problem
<j​effro256> Thanks, Rcuknium, I'm definitely keeping it in the front of my mind when designing the Carrot code. We're fundamentally in a better place than Zcash on our memberhsip proofs since they can be done off-device
<r​ucknium> I think this was actually transparent ZEC that Binance couldn't move. Even that functionality broke in the Ledger app. The latest post said Ledger just fixed it and withdrawals are now available.
<j​effro256> Oh really? That's surprising. Just a plain old developer support problem?
<r​brunner7> "Binance was able to use a beta version of Ledger’s app to transfer ZEC from their cold wallet to the exchange" Well, **that's** want I want to read about the exchange of my trust. Using beta versions on a hardware wallet
<j​berman> https://forum.zcashcommunity.com/t/zcash-stuck-in-a-wallet-check-here/49752/91
<j​berman> I did this for view tags. It would be nice if Ledger handles it this time around. We can also pencil in testing on our end before FCMP++ goes live. Same goes for Trezor
<r​brunner7> Ok, while chatting on, I think we can close the meeting proper. Thanks everybody for attending, read you again next week!
<j​effro256> Updating your HW to beta firmware to transfer funds gives the same energy as deleting database tables in production
<r​brunner7> Yeah :)
<r​brunner7> And maybe there are ZEC in there for a few hundreds of thousands of USD. Peanuts, really.
<s​needlewoods_xmr> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2025-04-11T15:58:02+00:00
- Closed at: 2025-04-14T18:55:29+00:00
