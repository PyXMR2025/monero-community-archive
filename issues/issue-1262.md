---
title: 'Monero Tech Meeting #135 - Monday, 2025-09-01, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1262
author: rbrunner7
assignees: []
labels: []
created_at: '2025-08-31T16:34:44+00:00'
updated_at: '2025-09-01T18:31:34+00:00'
type: issue
status: closed
closed_at: '2025-09-01T18:31:34+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1258).


# Discussion History
## rbrunner7 | 2025-09-01T18:31:34+00:00
````
<jberman> I won't be able to make today's meeting unfortunately (I will be at MRL on Wednesday). My update in advance: implemented a cleaner structure managing the curve tree in the daemon by separating curve trees consensus-based logic from strict db logic, sped up popping blocks/reorg handling in the wallet to handle trimming the tree quickly, fixed a bug in the wallet's tree builder path member reference counter, started benchmarking tx and membership proof verification using kayaba's latest (will share the complete figures hopefully within the next 24 hours)
<ofrnxmr> +1
<r​brunner7> Thanks for the report, jberman , will include it in the meeting log
<r​brunner7> Meeting in a bit more than 1 hour
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1262
<s​yntheticbird> hello
<s​needlewoods> hey, brb
<r​brunner7> jberman left a note that he won't be able to attend, and his report from last week. Again a really busy week.
<v​tnerd> Hi
<r​brunner7> Alright, what do the people who attend to report from last week?
<r​brunner7> I have still to make some smaller changes to my PR after the second review pass from jeffro256 . Can't take long now
<r​brunner7> The PR about peer selection
<s​needlewoods> Continued to reduce the amount of `m_wallet` in simplewallet, also some clean-up and bug fixes. E.g. I got callback `moneyReceived()` working like it did before now, I think, which was giving me a bit of trouble.
<s​needlewoods> `grep "\<m_wallet\>" src/simplewallet/simplewallet.cpp -c` gives 229 results (master branch has 635)
<s​needlewoods> If someone with access to hw devices wants to test `--generate-from-device`, I hope that works now.
<s​needlewoods> One thing I noticed in that regard: When using `--generate-from-device <wallet_name>` is there a reason why the CLI sets hw-device name to "Ledger", if no other name was given with flag `--hw-device`? [src](https://github.com/monero-project/monero/blob/125622d5bdc42cf552be5c25009bd9ab52c0a7ca/src/simplewallet/simplewallet.cpp#L4962)
<r​brunner7> Looks like a hopefully sane default to me, avoiding an error if you don't specify the device. Probably not terribly important.
<sneedlewoods> +1
<r​brunner7> Well, looks like we already ran out of reports :) Anything else to discuss today?
<r​ucknium> Not sure this is the right place to put this, but I worked on a tx spamming package for stressnet.
<r​brunner7> The last MRL meeting was like 3 hours, but I think none of the things discussed there would have been better here, for a better balance of meeting times.
<r​brunner7> Yeah, I think we are a good place to discuss stressnet things, once those get running in earnest.
<r​brunner7> What is that package written in, Rucknium ?
<r​ucknium> It's an extension of stressnet work for last year. I'm formalizing the spamming scripts into functions within a package. I've also automated the "next level" by automatically creating wallets and spawning `monero-wallet-rpc` processes.
<r​ucknium> R, as usual :P
<r​brunner7> Oh.
<r​brunner7> Is there an R-to-Python translator anywhere ...
<r​ucknium> Automatic wallet creation and spawning `monero-wallet-rpc` looks like it will be important for this FCMP stressnet because tx creation is slower. You want many wallet instances running at the same time to produce enough spam quickly.
<r​brunner7> I see
<r​ucknium> Hate to say it, but LLM could work for that
<s​needlewoods> is there an estimate how many spammers are needed, or the more the better?
<r​ucknium> Everything I do for my CCS is supposed to be open source, but could the spammer be an exception? Publishing it lowers the barrier to a potential spammer.
<r​ucknium> SNeedlewoods: You mean different spammer implementations in code, or number of spammer instances (of one implementation) running?
<s​needlewoods> Number of instances, or people helping out in the stressnet
<r​brunner7> Hmm, good question about open sourcing that. Could develop into a slippery slope if we start to hold back things somebody sees as "potentially dangerous".
<r​ucknium> I don't know how much spam it will be able to produce. Depends on how fast FCMP tx creation and submission is.
<r​brunner7> Regarding spamming the network, it seems there was a recent fork of Monero that claims to be better e.g. because of even lower fees. Like an invitation to spam, if you ask me :)
<r​ucknium> I'll leave the question open for now and bring it up in next stressnet discussion. That will probably be next MRL meeting.
<r​brunner7> For what it's worth, right now I lean towards publishing even such things. Just one opinion which may still change, of course.
<r​brunner7> Ok, anything else?
<s​needlewoods> nothing from me
<r​brunner7> Doesn't look like it. Thanks for attending, read you again next week!
<r​ucknium> AFAIK, spackle  and ofrnxmr  have their own spammer implementations. xmrack  has a published one here, but I don't know if it's optimized for volume: https://github.com/ACK-J/Monero-Dataset-Pipeline
<s​needlewoods> thank you
````


# Action History
- Created by: rbrunner7 | 2025-08-31T16:34:44+00:00
- Closed at: 2025-09-01T18:31:34+00:00
