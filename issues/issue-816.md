---
title: 'Seraphis wallet workgroup meeting #18 - Monday, 2023-03-27, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/816
author: rbrunner7
assignees: []
labels: []
created_at: '2023-03-24T16:18:46+00:00'
updated_at: '2023-03-27T18:52:47+00:00'
type: issue
status: closed
closed_at: '2023-03-27T18:52:46+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #812

Nothing special to discuss from my side, let's see what develops in the meeting.

# Discussion History
## rbrunner7 | 2023-03-27T18:52:46+00:00
```
<JoshBabb[m]> Update on the blake2b unit tests, I haven't finished them and Feel Bad if I'm bogarting the bounty, I'm been slammed and sloth when I'm off
<JoshBabb[m]> I'll share some code or ask for help on something specific as soon as I can, I haven't got to testing the transcript function yet 
<rbrunner7[m]> Blame DST :)
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/816
<dangerousfreedom> Hello
<valldrac[m]> Hi
<hbs[m]> Hello
<UkoeHB> hi
<ghostway[m]> Hello
<jberman[m]> hello
<rbrunner7[m]> So, what's there noteworthy to report from the past week? Nothing from me, it has been a very quiet week Seraphis-wise for me
<rbrunner7[m]> Still waiting for the very first PR :)
<dangerousfreedom> I started implementing the transaction_history as discussed [here](https://github.com/seraphis-migration/wallet3/issues/49). I implemented some basic functions to add entries to the maps and to get the last N transactions by type (confirmed/unconfirmed/offchain). Still in the very beginning yet. (https://github.com/DangerousFreedom1984/seraphis_lib/tree/tx_history/src/seraphis_wallet).
<dangerousfreedom> I have one unanswered question for the moment that I would be looking to answer during the week: How the unconfirmed enotes are being tracked so when an attempt of a transaction is made then it would not pick the previously used key_images (still unconfirmed or offchain)? I tried to create a loop to send some unconfirmed txs but the function fails as the input selector or something similar might be choosing always the
<dangerousfreedom> same unspent enotes based on the blockchain status or I'm not updating the ledger properly or so... any ideas?
<ghostway[m]> I haven't gotten to do anything yet. Today was really bad (with a good ending, kinda). Tomorrow I'll try to start, but no promises 
<UkoeHB> I have been doing cleanup on all the scanning code that I updated
<dangerousfreedom> The plan is to get started this week with a basic wallet implementation of some knowledge proof.
<UkoeHB> I'll probably make a new CCS this week, since I am way over hours now
<rbrunner7[m]> Certainly a good idea
<ghostway[m]> If you could try to list what needs to be done for the basic wallet implementation/its structure, it would be awesome -- so that I/df could just start
<ghostway[m]> (I hope you don't care I called you df, dangerousfreedom)
<rbrunner7[m]> Hmm, not sure that's fully clear already
<dangerousfreedom> I think I saw this list somewhere but I also cant find
<ghostway[m]> Sure, what needs to be done at first?
<rbrunner7[m]> Well, the keys must be somehow permanent, for sure. But with the idea that UkoeHB brought up last week, maybe it's not sure the pattern to store them will stay the same.
<rbrunner7[m]> Now they are just a normal part of the .keys file, beside all the options and some other minor stuff.
<UkoeHB> I have said this before, but someone needs to go through all the wallet-creation code in simplewallet and wallet2 and tease out each of the things that are being done there.
<rbrunner7[m]> All behind the single wallet password, so to say.
<UkoeHB> I know for a fact there is at least one thing in the wallet creation code that can be extracted.
<rbrunner7[m]> Extracted = made into its own module?
<UkoeHB> de-spaghettified
<dangerousfreedom> But still many things will be incompatible. Since we have another layer called 'seraphis_implementation' or 'seraphis_engine' then things will be a bit different
<rbrunner7[m]> Sure, a detailed list of what is in a .keys file now, and how that gets in there, would probably be a good start.
<dangerousfreedom> But yeah I agree that a list with similar functions or classes to be done would be important
<dangerousfreedom> This transaction_history is one part of it for example
<ghostway[m]> Is the decoy selection algorithm going to change? For example
<dangerousfreedom> And I think I would be doing this module quicker than I thought and wont need as many hours as initially planned (though probably many new features might appear along the way and I would have to reconsider the plans :p)
<dangerousfreedom> (though my ccs is not getting much traction :p)
<ghostway[m]> I need to go through wallet2 anyway..
<rbrunner7[m]> Don't think that's in the .keys file? But well, if somebody is on it, they could as well also list the content of the cache file
<rbrunner7[m]> Decoy selection is done in the Seraphis library, not wallet code, I would say
<rbrunner7[m]> But enotes to spend selection would be a wallet job
<UkoeHB> decoy selection is abstracted out of the library
<rbrunner7[m]> " I would be doing this module quicker than I thought" dangerousfreedom[m] , not sure I understand, which module now?
<ghostway[m]> Ok
<ghostway[m]> Then input selection? I think I've seen that on koe's list?
<ghostway[m]> Id imagine the transaction_history?
<rbrunner7[m]> Ah, we don't have a full decoy selector yet? Only something like a mock one?
<UkoeHB>  ghostway[m] yes we will need some kind of cache that can be used by the input selector, with all the input selection heuristic bells and whistles
<dangerousfreedom> rbrunner7[m]: The transaction_history with the same wallet2 functionalities as proposed here: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377
<rbrunner7[m]> Alright. But if you are through with that surprisingly early, I am sure you fill find a follow-up module to work on
<ghostway[m]> UkoeHB: I'm an expert on caches now :)
<ghostway[m]> Joking ;)
<jeffro256[m]> UkoeHB: In light of the recent mordinals fiasco, would it be easy to add a validation check for outputs which take the containing transaction as input, in order to do something along the lines of if (transactionIsAMordinalsTransaction(transactionContainingOutput(o))) { markOutputAsUnusable(); } 
<rbrunner7[m]> So yeah, I think if ghostway goes through the existing code and makes a reliable list of the whole wallet content that later we can use to check and tick off ("forgot nothing"), everybody will probably be grateful
<jeffro256[m]> Could be extended to check for other non-standard steganography to keep obviously seperate anonymity pools seperate this minimizing output poisoning 
<ghostway[m]> That sounds intriguing, do they have some kind of magic?
<rbrunner7[m]> I would be very surprised if mordinals are still a problem then
<jeffro256[m]> Yes I believe so, the first output is all 0s
<ghostway[m]> +1
<rbrunner7[m]> I mean, in 2 years or longer
<jeffro256[m]> Maybe 
<jeffro256[m]> Greed is powerful
<UkoeHB> didn't you write a PR to brick the blackball utility?
<jeffro256[m]> That was @tobhoht 
<rbrunner7[m]> Anyway, we mostly have now a problem because we don't find a hardfork soon convenient. With a hardfork we could introduce strict rules to judge transactions illegal.
<rbrunner7[m]> And then we won't having them floating around in the system anymore
<jeffro256[m]> Which is exactly why I was hesitant to remove that functionality 
<UkoeHB> it probably wouldn't work well with binned reference sets
<jeffro256[m]> Too much looping if you have too many blackballed outputs?
<rbrunner7[m]> But well, what you refuse to accept in the blockchain you don't have to blackball, no?
<rbrunner7[m]> I am talking from a strict "After Seraphis hardfork" point of view
<jeffro256[m]> Maybe you could set a limit on the number of tries for getting perfect non-blockballed inputs but then just say "fuck it" if the blackballs are causing too much of an issue 
<UkoeHB> it opens some tough questions about the bin that contains the real spend
<rbrunner7[m]> You doubt whether defining stricter rules for "This transaction is valid" will do the job?
<jeffro256[m]> UkoeHB: Ohh like if a blackballed output is in the same bin as the real spend?
<UkoeHB> ?
<UkoeHB> jeffro256[m]: yes
<Rucknium[m]> Seems too early to be discussing particulars like this. IMHO, if you care about this, submit a workable PR to exclude coinbase outputs from rings for the current codebase
<jeffro256[m]> Why exclude coinbase? B/c of p2pool?
<UkoeHB> for example, if there is only one viable combination in the real spend's bin, it is low probability that will be randomly generated, so there is a higher probability that bin has the real spend
<jeffro256[m]> +1
<Rucknium[m]> Coinbase outputs are always special. You don't have to do any sort of whack-a-mole check
<Rucknium[m]> jeffro256: Yes
<Rucknium[m]> I've already explained the privacy risks: https://github.com/monero-project/research-lab/issues/109
<jeffro256[m]> +1
<ofrnxmr[m]> +1
<xmrack> +1
<Rucknium[m]> Waiting for consensus for a change and/or a dev to develop a solution
<Rucknium[m]> The p2pool network upgrade on March 18 helped reduce its outputs, but it is still an issue
<jeffro256[m]> I'll take a look at that post. Upon first thinking about it, making a solution probably wouldn't be hard, it'll probably be harder agreeing on how to approach it
<Rucknium[m]> +1
<xmrack> +1
<jeffro256[m]> Do you take a stance of reducing selection for coinbase or completely removing
<ofrnxmr[m]> Complete remove 
<ofrnxmr[m]> ArticMine: 
<jeffro256[m]> SHould then wallet2 by default only allow that you send coinbase to yourself?
<Rucknium[m]> Good question. My initial assumption would be that it would be completely eliminated, but low probability could work, too. You have to allow the real spends of coinbase outputs to work properly, too
<rbrunner7[m]> But then you need something like a new type of tx, an all-coinbase-input tx, right?
<rbrunner7[m]> I think the matter is more difficult than at first sight ...
<ofrnxmr[m]> jeffro256:  iirc that was the idea
<ghostway[m]> what if these are the only ones you have? I might be misunderstanding, anyway
<Rucknium[m]> rbrunner7: No. Not necessary. It would just be apparent when a tx contains a coinbase as a real spend.
<Rucknium[m]> I have code that scans the whole post-RingCT blockchain for effective ring sizee whether effective ring size = ring size - number of coinbase outputs in the ring
<rbrunner7[m]> Strange. But anyway, maybe we bring something on the way pre-Seraphis; Seraphis so far not / not yet affected?
<Rucknium[m]> The MRL issue I linked above just has the theoretical impact (i.e. using ideal binomial distribution
<jeffro256[m]> rbrunner7[m]: If non-coinbase aren't picking coinbase often, it would follow that txs spending coinbase should also use coinbase as decoys since the other txs won't do it for them, so yeah
<Rucknium[m]> This is not a Seraphis conversation. really
<jeffro256[m]> +1
<JoshBabb[m]> +1
<jeffro256[m]> But non a new type of tx 
<ofrnxmr[m]> Coinbase tx shouldn't use rings at all
<JoshBabb[m]> it's when they're used in a ring
<jeffro256[m]> Yes but spending coinbase does
<ofrnxmr[m]> +1
<rbrunner7[m]> Whatever you discuss, remember, we try to establish the term enote ...
<jeffro256[m]> But what if i want to intentionally confuse other people I'm talking to so I can correct them later and feel superior?
<rbrunner7[m]> Splendid :)
<rbrunner7[m]> Well, ok, jeffro256 surely got some food for thought. Do we have anything specifically Seraphis to still discuss today?
<jeffro256[m]> Sorry for derailing
<Rucknium[m]> I'm just glad I got your attention  ;)
<rbrunner7[m]> No problem. And I am sure we will have to look back and forth sometimes to get everything right.
<rbrunner7[m]> And yeah, those mordinals ... they are such a pest now.
<rbrunner7[m]> Alright, I think we can close the meeting proper then, thanks everybody for attending!
<jeffro256[m]> Thank you
<UkoeHB> thanks
```


# Action History
- Created by: rbrunner7 | 2023-03-24T16:18:46+00:00
- Closed at: 2023-03-27T18:52:46+00:00
