---
title: Monero v15 hard-fork planning
source_url: https://github.com/monero-project/meta/issues/630
author: sethforprivacy
assignees: []
labels: []
created_at: '2021-11-19T16:30:55+00:00'
updated_at: '2023-12-18T04:24:19+00:00'
type: issue
status: closed
closed_at: '2023-12-18T04:24:19+00:00'
---

# Original Description
Now that we've semi-finalized the plan for the next hard-fork of Monero, and now that it's clear Triptych is a no-go and Seraphis is still some time off, I wanted to create this issue to start finalizing our plans for the next hard-fork/network upgrade for Monero.

# General info

- Release version: `v0.18.0`
  - https://github.com/monero-project/monero#scheduled-software-upgrades
- Release name: "Fluorine Fermi" #623
- Hardfork version: `v15`
  - https://github.com/monero-project/monero#scheduled-software-upgrades

# Primary features included

- Ring-size increase from 11 to 16 (https://github.com/monero-project/monero/pull/8178)
  - https://github.com/monero-project/research-lab/issues/79
- View tags by [@jberman](https://github.com/j-berman) (https://github.com/monero-project/monero/pull/8061)
  - https://github.com/monero-project/research-lab/issues/73
- Fee changes from [@arcticmine](https://github.com/ArticMine) (https://github.com/monero-project/monero/pull/7819)
  - https://github.com/monero-project/research-lab/issues/70
- Bulletproofs+ (https://github.com/monero-project/monero/pull/7170)
  - https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html

# Potential features

- Output binning changes by [@jberman](https://github.com/j-berman) (may not require HF)
  - https://github.com/monero-project/research-lab/issues/88
- Multisig refactor and vulnerability fix by [@UkoeHB](https://github.com/UkoeHB) (may not require HF)
  - https://github.com/monero-project/monero/issues/8237
- Daemon connection fixes (does not require HF)
  - https://github.com/monero-project/monero/pull/7760
- Optimize wallet RPC calls from 3 to 1 call (does not require HF)
  - https://github.com/monero-project/monero/pull/8076
- Faster value conveyance to wallets (does not require HF)
  - https://github.com/monero-project/monero/pull/8046

# Suggested time-frame

## Suggested Dates

- Branch/feature complete: May 16th, 2022
- Release date: June 16th, 2022
- Testnet hard-fork: May 16th, 2022
- Stagenet hard-fork: TBD
- Mainnet hard-fork: July 16th, 2022, block 2668888

# Release checklist

https://github.com/monero-project/meta/issues/690

# Discussion History
## SamsungGalaxyPlayer | 2021-11-19T18:23:43+00:00
March seems extremely late for the currently-listed items.

## sethforprivacy | 2021-11-19T18:27:59+00:00
> March seems extremely late for the currently-listed items.

I'm all for sooner if we can get it done with proper code freeze and notifications to ecosystem participants before then.

The other consideration is "lost time" due to holidays in the US and abroad over the next 6wks or so.

## luigi1111 | 2021-11-19T19:29:21+00:00
I'm good with March target. What are people's thoughts on freeze date lead time?

## sethforprivacy | 2021-11-19T19:32:25+00:00
> I'm good with March target. What are people's thoughts on freeze date lead time?

I would say 30d like we have done in the past? But obviously open to input.

## selsta | 2021-11-19T19:34:00+00:00
30d before hardfork is when we want to release binaries, ideally 60 days before a freeze.

## selsta | 2021-11-19T19:35:20+00:00
I would like to add https://github.com/monero-project/monero/pull/7760 to the list, it fixes a lot of the daemon issues and is well tested, bit it isn't fully reviewed yet.

## sethforprivacy | 2021-11-19T19:40:56+00:00
> I would like to add [monero-project/monero#7760](https://github.com/monero-project/monero/pull/7760) to the list, it fixes a lot of the daemon issues and is well tested, bit it isn't fully reviewed yet.

Does this require HF, or should/could it be included in a point release prior?

## selsta | 2021-11-19T19:41:53+00:00
Does not require a HF.

## sethforprivacy | 2021-11-19T19:42:48+00:00
I'll add as a possible one, we can discuss further in a future meeting whether it should be done before this HF or as part of it. I know some daemon changes are better off being done in a HF to ensure everyone is running them at once.

## Rucknium | 2021-11-19T21:21:47+00:00
[Someone asked me on Reddit](https://www.reddit.com/r/Monero/comments/qxo2rl/comment/hlawx9e/) whether [OSPEAD](https://github.com/monero-project/research-lab/issues/93) needs a hard fork. My response:

No. Right now decoy selection is not enforced by blockchain consensus in any way. A hard fork is only required for consensus changes. There are specific reasons why we may eventually want to [enforce a decoy selection algorithm at the consensus level](https://github.com/monero-project/research-lab/issues/87), however.

For now, wallet software does decoy selection. This, itself, can cause problems since some wallet software does it in a way that harms user privacy. Now, it is for this very reason that it *could* be advantageous to implement OSPEAD at the same time as a hard fork, since it can "force" an upgrade in wallets that follow the Monero reference wallet, i.e. the Monero GUI wallet.

However, the hard fork itself can be useful for gathering statistical, aggregate data on the decoy system since ring size will rise from 11 to (likely) 16. As a result, ArticMine suggested that I leverage the hard fork to help develop OSPEAD. I included this suggestion in [my CCS proposal](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html):

>The upcoming hard fork, which does not yet have a fixed date, will include an increase in the ring size. The discontinuity that the hard fork creates can be leveraged to better understand how ring signatures work in pratcice on the Monero blockchain. Therefore, some of the research work will occur after the hard fork.

## BlackRock-INC | 2021-11-20T01:39:25+00:00
February would be a ideal date, good luck guys.

## moneroexamples | 2021-11-20T03:09:03+00:00
That's nice. Are all these changes already merged in monero's master branch?  Also are these changes already on testnet?

## SChernykh | 2021-11-20T13:35:08+00:00
What exactly is meant by "code freeze"? Feature freeze and the creation of v0.18 branch? Because not allowing bug fixes would be stupid. 60 days from now is January 19th, so we're already tight on schedule.

## luigi1111 | 2021-11-20T18:55:13+00:00
> What exactly is meant by "code freeze"? Feature freeze and the creation of v0.18 branch?

Correct. I would like to propose January 15th for branch/feature complete, with target fork March 15th.



## sethforprivacy | 2021-11-20T19:52:42+00:00
> > What exactly is meant by "code freeze"? Feature freeze and the creation of v0.18 branch?
> 
> Correct. I would like to propose January 15th for branch/feature complete, with target fork March 15th.

That time frame seems very reasonable considering the key features are already PR'd (except ring size, which is a very minor PR).

## erciccione | 2021-11-21T09:22:47+00:00
Dev meeting to make it official?

## sethforprivacy | 2021-11-22T13:15:25+00:00
> Dev meeting to make it official?

Yes, that would be ideal and I've requested someone to run it in #monero-dev but have gotten no takers. I'll try to run it if I can, but I cannot do so during business hours and weekends are focused on family.

It would be great if someone else could schedule and facilitate a dev meeting to walk through this planning and set more firm next steps.

## sethforprivacy | 2021-11-23T14:31:14+00:00
A meeting has been proposed for 17:00UTC on November 28th by monerobull in Matrix -- any objections, or would that work? 

## Rucknium | 2021-11-27T17:35:30+00:00
Would it make sense to seriously consider enforcement of a very basic rule for decoy selection in light of the research of isthmus / @Mitchellpkt and @neptuneresearch revealing that tens of thousands of transactions have included the same set of outputs as decoys? See the recent MRL meeting log: https://github.com/monero-project/meta/issues/632

The rule to be enforced would be something like: No rings allowed where M - 1 ring members are identical to any other ring for a transaction already on the blockchain, where M is the number of ring members. As of now M = 11 and in the next hard fork M will likely be 16.

Monero started to enforce a particular ring size for a very good privacy reason. Allowing wallets or services to construct transactions that break the above rule is a backdoor way to allowing ring size = 1, thereby allowing the true spend to be easily identified.

@ArticMine has suggested that any decoy selection enforcement occur at the node level, i.e. monerod would reject any transaction that does not conform to a rule or rules about ring member selection. Among the benefits of enforcement at the node level is that the computational burden would not be borne by people that are just downloading and verifying the blockchain. I suspect that checking for rings that are effectively duplicates across the entire blockchain or even a portion of the blockchain may be somewhat computationally burdensome.

If enforcement was done in this way, a miner could still include a rulebreaking transaction in a block, but rulebreaking transactions would generally not be transmitted to the miners in the first place since monerod would not re-broadcast them throughout the network.

See also this MRL issue: https://github.com/monero-project/research-lab/issues/87

## sethforprivacy | 2021-11-29T15:45:14+00:00
A dev meeting discussed the topics of this issue in-depth:

https://github.com/monero-project/meta/issues/633

Rough consensus seemed to be gained for:

- Ring size 16
- Mar 15th 2022 hard-fork, Feb 15th release, Jan 15th tag

## moneroexamples | 2021-11-29T21:57:32+00:00
@sethforprivacy 

Will testnet and stagenet have hf before that? If yes, are the dates known?

## selsta | 2021-11-29T23:27:21+00:00
Stagenet: 1-2 weeks before
Testnet: 1.5 months before

At least that's what I think would make sense.

## sethforprivacy | 2021-11-30T13:38:05+00:00
Thanks for mentioning that, @moneroexamples, I had forgotten that portion of things.

Agreed with @selsta, those are key milestones to hit and prove the transition before the main net forks.

## SChernykh | 2022-01-14T11:12:46+00:00
> A dev meeting discussed the topics of this issue in-depth:
> 
> #633
> 
> Rough consensus seemed to be gained for:
> 
> * Ring size 16
> * Mar 15th 2022 hard-fork, Feb 15th release, Jan 15th tag

Jan 15th is tomorrow. Some important PRs like https://github.com/monero-project/monero/pull/8061 are still not merged.

## sethforprivacy | 2022-01-31T13:47:36+00:00
Update from the last dev meeting (thanks @carrington1859):

- There was consensus for the ringsize increase from 11 to 16. This brings better privacy to Monero transactions, and the bulkier transactions are mostly offset by Bulletproofs+.
- Bulletproofs+ (a more efficient version of Bulletproofs which help hide transaction amounts) are fully audited and considered good to go.
- View Tags, which will massively speed up blockchain scanning going forward, are ready pending some final tweaks and reviews.
- Changes to the way fees & dynamic blocksize work require more discussion. There are concerns about how fast blocks might be able to grow. You can read a good summary of the concerns here. A dedicated Monero Research Lab meeting is planned to discuss these issues.
- Fixes and improvements to multisig are awaiting a few final reviews.
- Other changes, such as improvements to networking connections, are making good progress but will probably be added in a minor release after the major update.

## moneroexamples | 2022-01-31T23:51:21+00:00
@sethforprivacy 

Thanks for the update. Where can read more about `View Tags` with possible examples of how to use them?

## selsta | 2022-02-01T00:12:12+00:00
@moneroexamples https://github.com/monero-project/monero/pull/8061 and https://github.com/monero-project/research-lab/issues/73

## carrington1859 | 2022-02-13T18:14:52+00:00
@sethforprivacy  could you add the ringsize PR to the main post?

https://github.com/monero-project/monero/pull/8178

## moneroexamples | 2022-02-14T10:16:38+00:00
When stagenet and/or testnet will for to v15?

## erciccione | 2022-02-14T11:00:26+00:00
@moneroexamples It's necessary to set up a dev meeting to decide that, i would say.

## sethforprivacy | 2022-02-14T13:06:01+00:00
> @sethforprivacy could you add the ringsize PR to the main post?
> 
> [monero-project/monero#8178](https://github.com/monero-project/monero/pull/8178)

Added, thanks!

## moneroexamples | 2022-02-15T10:13:46+00:00
@erciccione Thanks. Hopefully it will be well in advance of the HF on the mainnet.

## gs522084 | 2022-04-21T06:52:46+00:00
Please add the ability to create warehouse wallets. Thanks, I can withdraw my transaction at any time within the specified time. The warehouse wallet is only for my internal transfer, the time is 24 hours or 48 hours, and the transfer can also be cancelled at any time within 72 hours.The absolute security of the warehouse (1 million coins) must be guaranteed, and the revocation function is necessary

## selsta | 2022-04-30T10:22:45+00:00
Please add https://github.com/monero-project/monero/pull/8076 and https://github.com/monero-project/monero/pull/8046 to the potential features and remove the binning one.

Also link to https://github.com/monero-project/monero/issues/8237 instead of the multisig refactor one.

## sethforprivacy | 2022-05-02T13:39:15+00:00
> Please add [monero-project/monero#8076](https://github.com/monero-project/monero/pull/8076) and [monero-project/monero#8046](https://github.com/monero-project/monero/pull/8046) to the potential features and remove the binning one.
> 
> Also link to [monero-project/monero#8237](https://github.com/monero-project/monero/issues/8237) instead of the multisig refactor one.

Done, thanks for the updates.

On another note, should I keep this open alongside the checklist, or migrate some of that info into that issue and close this one?

## selsta | 2022-05-02T14:21:09+00:00
I'd keep this one open.

# Action History
- Created by: sethforprivacy | 2021-11-19T16:30:55+00:00
- Closed at: 2023-12-18T04:24:19+00:00
