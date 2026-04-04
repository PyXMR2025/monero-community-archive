---
title: Create network upgrade (hard-fork) checklist
source_url: https://github.com/monero-project/meta/issues/489
author: sethforprivacy
assignees: []
labels: []
created_at: '2020-07-19T18:14:03+00:00'
updated_at: '2020-08-17T18:10:30+00:00'
type: issue
status: closed
closed_at: '2020-08-17T18:10:29+00:00'
---

# Original Description
This issue will serve as a place to create, update, and discuss a checklist that can be used for each network upgrade (hard-fork) that occurrs in the future for the Monero network.

The checklist can be seen below:

	• Security audit
	• Code audit 
	• Ledger integration
		○ Implemented in Monero codebase (if needed)
		○ Ledger app integration coded by Ledger
	• Trezor integration
		○ Implemented in Monero codebase (if needed)
		○ Trezor app integration coded by Trezor
	• Fork height set
		○ Monero-announce mailer notice 
		○ Twitter announcement 
		○ Reddit announcement 
		○ Getmonero.org announcement 
	• Notify wallets
		○ MyMonero
		○ Coinomi
		○ Exa Wallet
		○ Wookey Wallet
		○ X Wallet
		○ Guarda
		○ ZelCore
		○ Cake Wallet
		○ Monerujo
		○ Edge Wallet
		○ Exodus
		○ XMRWallet
	• Notify exchanges
		○ https://web.getmonero.org/community/merchants/#exchanges
	• Notify 3rd party payment processors
		○ https://web.getmonero.org/community/merchants/#payment-gateways
	• Notify mining pools
		○ https://miningpoolstats.stream/monero
	• Release tagged
		○ Update src/version.cpp.in with new version AND new name (if necessary)
		○ Update Gitian YML files in contrib/gitian/ to the new version number
		○ Update README.md with new fork table entry (or at least update the Recommended Monero version)
		○ Update contrib/gitian/README.md so that the instructions reflect the current version
		○ Update src/checkpoints/checkpoints.cpp with a recent hardcoded checkpoint
		○ Update src/blocks/checkpoints.dat with ./monero-blockchain-export --output-file checkpoints.dat --block-stop <recent block height> --blocksdat
		○ Update expected_block_hashes_hash in src/cryptonote_core/blockchain.cpp with checkpoints.dat sha256 hash
	• Testnet forked
	• Testnet testing/verification
		○ Ledger
		○ Trezor
		○ Release-specific testing
		○ RPC testing/update RPC documentation
	• CLI reproducible builds validated
	• CLI released
		○ https://web.getmonero.org/downloads/ updated
		○ Update hashes.txt on website
		○ Update downloads.yml on website
		○ Update auto-update DNS records
		○ Update redirects on downloads box
		○ Update seed nodes
	• GUI released
		○ https://web.getmonero.org/downloads/ updated
		○ Update hashes.txt on website
		○ Update hashes.txt.sig on website
		○ Update downloads.yml on website
		○ Update auto-update DNS records
		○ Update redirects on downloads box
	• Monero-announce mailer notice 
	• Twitter announcement 
	• Reddit announcement 
	• Getmonero.org announcement

Edit list:

- Added Exodus to exchange list
- Added "Notify 3rd party payment processors"
- Added specifics on download update process
- Added specifics on code changes needed for tagging
- Added missing wallets from https://old.reddit.com/r/Monero/comments/hp7nna/rmonero_weekly_discussion_july_11_2020_use_this/
- Added "Update hashes.txt.sig on website" to GUI section

# Discussion History
## fluffypony | 2020-07-19T18:19:26+00:00
Please add Exodus to the list of wallets

## sethforprivacy | 2020-07-19T18:20:18+00:00
Done, thanks for the callout!

## sethforprivacy | 2020-07-19T19:11:02+00:00
I added a bunch of specifics for the tagging/download page updates from the below Release Engineering list provided by @fluffypony:

```
Builds:

- DON'T FORGET TO UPDATE src/version.cpp.in with new version AND new name (if necessary)
- DON'T FORGET TO UPDATE Gitian YML files in contrib/gitian/ to the new version number
- DON'T FORGET TO UPDATE README.md with new fork table entry (or at least update the Recommended Monero version)
- DON'T FORGET TO UDDATE contrib/gitian/README.md so that the instructions reflect the current version
- DON'T FORGET TO UDDATE src/checkpoints/checkpoints.cpp with a recent hardcoded checkpoint
- DON'T FORGET TO UPDATE src/blocks/checkpoints.dat with ./monero-blockchain-export --output-file checkpoints.dat --block-stop <recent block height> --blocksdat
- DON'T FORGET TO UPDATE expected_block_hashes_hash in src/cryptonote_core/blockchain.cpp with checkpoints.dat sha256 hash
- DON'T FORGET TO POST ABOUT THE RELEASE ON THE MONERO-ANNOUNCE LIST


Final steps:

- Update hashes.txt on website
- Update downloads.yml on website
- Update auto-update DNS records
- Update redirects on downloads box
```

## glv2 | 2020-07-20T08:24:49+00:00
Maybe this checklist could be added to the monero-project/monero repository as a file named "RELEASE_PROCESS.md" or something similar, instead of keeping it in a github issue.

In order not to clutter up the root directory of the repository with documentation files, we could make a "doc" subdirectory, put "ANONYMITY_NETWORKS.md", "CONTRIBUTING.md", "LEVIN_PROTOCOL.md", "README.i18n.md" and "RELEASE_PROCESS.md" in there, and fix the links to those files in "README.md" if necessary.


## fluffypony | 2020-07-20T08:28:33+00:00
@glv2 good point - a docs subdirectory is a great idea!

## hyc | 2020-07-20T12:16:11+00:00
Might call it something like devdocs instead, since none of these are really relevant to end users.

## fluffypony | 2020-07-20T12:17:40+00:00
@hyc I *think* that whatever is in the source code is relevant to developers and not end-users anyway, so I'm not averse to either docs or devdocs

## hyc | 2020-07-20T12:50:39+00:00
Maybe most is. The "Using TOR" section of README.md is presumably for end users.

## erciccione | 2020-07-20T13:54:05+00:00
Yeah, when @sarangnoether proposed the checklist, we planned to  save it somewhere in the repository (either this repo or 'monero') and use iot for every release. We had only "personal" checklists before, that got easily lost in the logs. 'devdocs/RELEASE_PROCESS.md' sounds good.

As suggested during yesterday's meeting: After the checklist is created, we could make a github project based on the checklist: a single board with "todo" "in progress" and "done" tabs. Issues could be added to the board (as tasks) and people assigned to issues.

## sethforprivacy | 2020-07-24T16:56:38+00:00
Thanks for the feedback so far, everyone!

Any other outstanding items I’ve missed or you’d like to see added?

I’ll re-share this in IRC too just to make sure we get a good set of eyes on it, but we should probably finalize it soon to use for the CLSAG upgrade coming up.

## garlicgambit | 2020-07-30T22:04:26+00:00
Couple suggestions:  
  
- Update README.md (compile) instructions to the new version number  
- Check/update README.md software dependencies and version numbers  
- Sign git tag

## fluffypony | 2020-07-31T05:52:03+00:00
@garlicgambit the README changes are all in there already, do you think they need some clarification? Also every git commit (including tags) should be signed, if someone is dropping the ball on that I think it best to raise it with that contributor directly.

## Adreik | 2020-07-31T06:01:27+00:00
What about performing tests on the RPC daemon and wallet documentation, and preparing updates to those webpages if there is any issue?

## garlicgambit | 2020-08-01T18:44:08+00:00
@fluffypony if the current level of detail is appropriate for the people that will use the checklist, then you can ignore the suggestions.

## erciccione | 2020-08-02T19:01:23+00:00
@sethsimmons I would add: Check if seednodes are up and ready for the hard fork.

## sethforprivacy | 2020-08-17T17:55:23+00:00
Added all suggestions.

## sethforprivacy | 2020-08-17T18:10:29+00:00
Final version: https://github.com/sethsimmons/Miscellaneous-Monero/blob/master/Monero%20Release%20Checklist.md

# Action History
- Created by: sethforprivacy | 2020-07-19T18:14:03+00:00
- Closed at: 2020-08-17T18:10:29+00:00
