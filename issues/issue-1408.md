---
title: 'Monero Tech Meeting #174 - Monday, 2026-06-22, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1408
author: rbrunner7
assignees: []
labels: []
created_at: '2026-06-21T07:34:48+00:00'
updated_at: '2026-06-22T18:45:40+00:00'
type: issue
status: closed
closed_at: '2026-06-22T18:45:40+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1403).


# Discussion History
## rbrunner7 | 2026-06-22T18:45:40+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1408
<sneedlewoods> Hey
<jberman> waves
<jeffro256> Howdy
<jpk68> Hello
<rbrunner7> Ok, what is there to report from last week? I myself went through most of the Polyseed PR comments from selsta and @jeffro256:monero.social
<sneedlewoods> Finally got all the functional tests working with the wallet-rpc based on Wallet API, just want to double check my TODOs before I make the PR.
<jeffro256> +1
<sneedlewoods> And started to work on a new branch based on fcmp++-beta-stressnet which includes 1. Updated Wallet API 2. wallet-cli based on Wallet API and 3. wallet-rpc based on Wallet API.
<sneedlewoods> There were a lot more conflicts than last time I checked, but I got it to build and at least was able to generate a new wallet, haven't tested more than that so far. There are some lines I just commented out and need to investigate and if no one has strong arguments against it or better ideas, that would be my next thing to focus on, apart from resolving review comments.
<sneedlewoods> I'm thinking, sooner or later the FCMP++/Carrot and the Wallet API work need to get merged. So I'm hoping that when looking at this, it may help make decisions for the Wallet API related PRs (thosee on monero master branch) to keep future changes smaller. Also I have the hopes, that through this, I'll get a little familiar with some of the new FCMP++ and Carrot code.
<sneedlewoods> I would hope to be able to make a PR to the seraphis-migration repo (soonish), and even if not for an official stressnet release, maybe someone is willing to help out testing it.
<rbrunner7> I think working towards merge with FCMP++ and Carrot can't be a bad idea.
<jpk68> Got I2P SAM working, finally. It can now broadcast transactions to remote nodes
<jeffro256> me: working on documentation and implementing feedback from j-berman and UkoeHB 
<jberman> me: mostly Carrot/FCMP++ hot/cold wallet PR review, and some final phase 1 audit tasks (still expecting the final report any day now, just followed up again) 
<rbrunner7> Did finally somebody at the hardware wallet companies take note about what's coming?
<rbrunner7> Not sure, maybe @jeffro256:monero.social reported he was in contact with somebody
<rbrunner7> Hmmm, maybe Matrix servers are slow today to propagate messages?
<sneedlewoods> Messages seem to arrive fine for me
<jeffro256> I keep bugging them. Recently my contacts at Ledger and Trezor have made more promising comments about actually getting development proposals started
<jpk68> +1
<jeffro256> But AFAIK, no development has actually taken place 
<rbrunner7> Ok, at least that
<jeffro256> @sneedlewoods: Ideally, I think that we should get the wallet API changes merged in soon, and maybe it could make it into the hypothetical v0.19.0.0 release 
<jeffro256> by that I mean a release whichs forks from master, uses GUIX, but doesn't include FCMP++ code 
<sneedlewoods> I was hoping to get more testers through stressnet, because I assume I haven't found every bug and (functional-/unit-/etc-)tests still far away from covering everything, though there could be issues with stressnet which are not present on master
<rbrunner7> Getting testers is often difficult ...
<sneedlewoods> Review comments have a bit stagnant, but I think with the final piece, the wallet-rpc, out, there should be no more big changes, except bugs found or review comments ask for it.
<sneedlewoods> s/have a bit/have been a bit
<rbrunner7> I lost track a bit - is the Wallet RPC code ready for review?
<sneedlewoods> not PR'd yet, will hopefully do so tomorrow, just fixed the final failing tests last week
<rbrunner7> +1
<sneedlewoods> (or maybe Wednesday)
<rbrunner7> If we are through with the reports, I would like to come back to last week's subject for a moment: Storing Polyseed passphrases in .keys files, and also re-displaying them from there with commands like seed in the CLI wallet app
<rbrunner7> I carefully went through the meeting log again to read about the various opinions, and also had quite some own thoughts about that subject
<rbrunner7> I finally landed in the "do not store, do not display" camp.
<koe000> Me: reviewing carrot_impl
<rbrunner7> For me, it's one of the "core value propositions" of passphrases, at least as used in the Monero CLI wallet app, that they are an additional secret that you are free to add, free to write down yourself or memorize, and free to apply when you restore. The wallet should not take matters into its own hands and insist on displaying it along with the seed.
<sneedlewoods> +1
<rbrunner7> If nobody can be found to strongly oppose, I will "operate out" passphrase storage and re-display from my PR
<rbrunner7> Also one factor in my opinion building: I checked that it's possible without a lot of effort and code to keep the now-stored passphrases in wallets written by the monero_c library intact.
<rbrunner7> And make them available as a member of account_keys, to offer some nice upgrade path if wallet app writers want that.
<rbrunner7> The Monero core software would otherwise totally ignore that.
<rbrunner7> The name would change from m_passphrase to e.g. m_monero_c_passphrase to make that clear.
<sneedlewoods> That sounds good to me, if other projects can use another system they prefer
<rbrunner7> Yeah, after all this room is called "no wallet left behind" :)
<sneedlewoods> +1
<jpk68> Does Feather store passphrases in the keys file? Is it done in the same way?
<rbrunner7> It goes into the wallet cache if I remember correctly, as "wallet attributes".
<rbrunner7> So, no, not the same way. monero_c based wallets could switch to Feather's attribute system, with the upgrade being "Take it from m_monero_c_passphrase and convert it to an attribute"
<jpk68> +1
<rbrunner7> Ok, maybe we will get some more opinions from people reading this later. Of course people can also review and comment the PR if they want.
<rbrunner7> Alright, something else to discuss today?
<selsta> small reminder to please help reviewing the remaining PRs here so that we can put out the release: https://github.com/monero-project/monero/issues/10545
<selsta> they are ordered most to least important, 10774 could be delayed
<jberman> > <@rbrunner7> For me, it's one of the "core value propositions" of passphrases, at least as used in the Monero CLI wallet app, that they are an additional secret that you are free to add, free to write down yourself or memorize, and free to apply when you restore. The wallet should not take matters into its own hands and insist on displaying it along with the seed.
<jberman> tbc, you'll still store the private spend key, so a user doesn't have to input their seed passphrase every time they open the wallet? And also, you'd store the original mnemonic as well, so that if the user wants to see their original seed, they can see it?
<rbrunner7> So 4 PRs left to review there?
<selsta> 10779 is already reviewed, so 3 basically
<rbrunner7> @jberman:monero.social: Yes. No drastic change in behavior, just dropping the passphrase storage and display
<jberman> Will review 10774 today, good change
<rbrunner7> No "encryption at rest" for the Polyseed either, but maybe that could get added later, with a new switch
<rbrunner7> Beyond normal wallet encryption by password of course, as discussed, with some minor confusion :)
<selsta> 10598 is an edge case where when the node goes into "target height decreases" branch safe sync mode could stay false, which means during power outage there could be corruption
<rbrunner7> Anyway, just my humble proposal, people are free to comment and also oppose in the PR. Will write a dedicated comment there about this my proposal.
<jeffro256> I will review #10781 today 
<rbrunner7> Looks like we are through now, thus let me close the meeting. Thanks everybody for attending, read you again next week!
<sneedlewoods> Thanks everyone, see ya
````


# Action History
- Created by: rbrunner7 | 2026-06-21T07:34:48+00:00
- Closed at: 2026-06-22T18:45:40+00:00
