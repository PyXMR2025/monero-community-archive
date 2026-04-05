---
title: Legacy/Carrot Wallet/Seed Handling
source_url: https://github.com/seraphis-migration/monero/issues/306
author: UkoeHB
assignees: []
labels: []
created_at: '2026-03-19T06:24:27+00:00'
updated_at: '2026-03-30T19:22:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md) introduces a new key structure with more capabilities than the existing legacy scheme. At the same time, Carrot is highly 'compatible' with the legacy scheme, to the extent that all Carrot addresses look like legacy addresses, and even to the extent that legacy wallets can be converted to Carrot wallets. This leads to questions.

- Should existing legacy wallets be allowed to convert to legacy/Carrot hybrids? I.e. scanning for both legacy and Carrot enotes?
  - Should this conversion be automatic (e.g. based on restore height), or manual?
  - What if a user wants to remain legacy-only?
- Should seeds like Polyseed define a new format for Carrot-only wallets, or rely on restore height?

Relevant:
- https://github.com/tevador/polyseed/issues/13#issuecomment-4007864335 comment from @tevador about Polyseed.
- https://github.com/monero-project/meta/issues/1350 Monero Tech Meeting \#160

There are two basic approaches.

### Approach 1: Separation

In this approach, wallet seeds are the 'source of truth' and there is no ambiguity allowed. To get a Carrot wallet, you need a Carrot-only seed.
- Seeds should include a bit flag, version, or formatting specialization to differentiate legacy-only from Carrot-only seeds.
- Opening the CLI gives you a message about what wallet type you have (CryptoNote/Legacy or Carrot). There is no option to switch/upgrade, nor to get a Carrot address from within a legacy-initialized wallet (or vice versa).
  - `wallet_info` will also state what the wallet type is.
  - Carrot wallets will send change enotes to a Carrot selfsend address. Legacy wallets will continue to use legacy-only change addresses.

Pros
- Simple, requires minimal UI layering
- Clear separation, easier to handle and less ambiguous from a DevX point of view

Cons
- Anyone who wants Carrot capabilities (even if only partially - i.e. for newly received enotes) must migrate all funds to a new wallet. This would increase churn around the fork that may be considered undesirable spam. Also it may be infeasible/unrealistic for hardware wallets that deal with multiple coins (BTC, ETH, XMR, etc.).
  - For hardware wallets where the seed is baked-in or semi-permanent, it may be feasible to migrate in-place to Carrot (including a wallet sweep, since we are assuming other wallet software can't operate as a hybrid). The hardware wallet would need to permanently store a flag indicating it is 'Carrot-only'.
- Seed versioning readability is unreliable. Users are likely to misunderstand what wallet type their seed corresponds to, then get confused when opening the seed doesn't match their expectations. They also may be prone to generating legacy seeds unintentionally (especially if seed-generating software UI isn't updated clearly). This unintentionality and ambiguity may be exacerbated by Carrot addresses looking exactly like legacy addresses - users may not realize right away that they are dealing with a legacy wallet.

### Approach 2: Hybridization

In this approach, wallet seeds do not by default differentiate between legacy/Carrot (although they may). Instead, restore height is the main 'source of truth'. (Alternative: user specifies wallet type on restore; this is a bit too manual for my taste) Note that legacy/pre-Carrot seeds will always be *extracted* to legacy keys, but then those keys will be migrated to a Carrot key structure. It is important that legacy/Carrot view keys be the same for balance recovery efficiency.
- Restore a legacy seed from below the Carrot-only block height: gives legacy-Carrot hybrid wallet. Note that the CLI can include the Carrot height as a reference point when requesting the user specify it on restore-from-seed.
  - Can obtain a Carrot address using `address new`.
  - Can obtain a legacy address using `legacy_address new`.
  - All wallet commands have results split between legacy/Carrot. E.g. `wallet_info` will list both `Legacy Address` and `Carrot Address`. Similarly with just `address`.
- Restore a legacy from above the Carrot-only block height, or restore a Carrot-only seed: gives Carrot-only wallet.
  - Causes `legacy_address new` to return an error.
  - Split-result wallet commands will elide all legacy content.
- Specify the `--legacy-only` flag on wallet startup: ignores restore height logic, gives legacy-only wallet. Errors if the seed is Carrot-only.
  - Causes `address new` to return an error.
  - Split-result wallet commands will elide all Carrot content.
- Carrot-enabled wallets will send change enotes to a Carrot selfsend address. Legacy-only wallets will continue to use legacy-only change addresses.
- Existing wallets opened with upgraded software will be required to migrate. Users are asked if they wish to upgrade to a legacy/Carrot hybrid (one-time ask, then it's stored in the migrated file). View-only wallets remain legacy-only until keys are provided to upgrade with (either the generate-address secret to remain view-received, or the generate-image key + generate-address secret to switch to a semi-view-balance legacy/Carrot hybrid).

Pros
- Users who want Carrot (especially hardware and cold wallets) don't need to migrate their funds.
- Seamless upgrade path for the common user, who will automatically get Carrot capabilities.

Cons
- Users who *don't* want Carrot capabilities will be automatically upgraded to using Carrot unless they are hyper-aware. Once a wallet has any Carrot-scanned enotes, it will be a pain to 'unravel' that.
  - This would be less of an issue if Carrot addresses looked different from legacy addresses.
  - Note that the Carrot view-balance and generate-address tiers are not useful for the typical medium/light-weight user who is just running with one full wallet and relying on remote nodes. They'd be much more greatly impacted by other Jamtis features (encoded address index, filter-assist key). Although that may change if 'light' wallets for the view-balance tier became popular.
- Users with hybrid wallets may try to use a view-balance tier wallet but fail to actually see their full balance and become confused.
- Users who specify a post-Carrot restore height but happen to have legacy addresses in the wild *could* receive legacy enotes but fail to scan for them.
  - Possible solution would be to scan for legacy enotes in the background just in case (for legacy seeds) and 'alert' the user. Or just silently upgrade them to a hybrid wallet (but would that be confusing? since they may not even be aware their wallet was configured as Carrot-only). Or just always do a hybrid wallet for legacy seeds, and only elide legacy stuff for Carrot-only seeds (or for dev simplicity, only ever do hybrid but show Carrot as 'disabled' for the anal legacy-only users).
- Requires a special upgrade for existing hardware wallets to export the generate-image key + generate-address secret (but retain key image export capabilities for legacy enotes). Hardware wallets will have to upgrade no matter what to get Carrot features, but in the hybrid case it may require more work.
  - If hardware wallets don't want to export generate-image keys, then additional logic/APIs would be needed to export just the generate-address secret and also Carrot key images.
- More complex wallet UI, with the addition of `--legacy-only`, `legacy_address new`, and display splits.
- More complex wallet implementation, e.g. with the need to manage two Carrot key structures (specifically how the legacy-to-Carrot view-received key is **not** derived from the view-balance secret). Affects full wallets and view-balance wallets.

# Discussion History
## tevador | 2026-03-19T11:44:08+00:00
I vote for approach 1 (separation).

Note that a third addressing protocol is in the works which will be released at some point in the future (it doesn't need a hard fork). It features post-quantum secure addresses with a different format (working name: Jamtis-PQ, see: https://github.com/monero-project/research-lab/issues/151). The hybrid approach clearly can't work in that case.

> Anyone who wants Carrot capabilities (even if only partially - i.e. for newly received enotes) must migrate all funds to a new wallet.

The following Carrot features will work out of the box for legacy wallets:

* Janus attack protection
* Forward secrecy (due to the added T term in the output key construction) 
* Burning bug resistance

Users will need to migrate if they want one of the following features that are only for Carrot wallets:

* Internal forward secrecy (special derivation for self-send enotes)
* Address generator tier
* Full view only wallets

The latter two are not very relevant for most users.

## hbs | 2026-03-19T13:06:15+00:00
I strongly support separation, especially due to the recent controversial debate on OVK.

## sneurlax | 2026-03-19T16:25:50+00:00
As a hardware wallet user I support Approach 2: Hybridization.  I want to make it as easy as possible for current day hardware wallet users to upgrade ~~without creating a bunch of sweeps that correlate old RingCT outputs together~~ *edit*: this is not an issue

Approach 2's main drawback is external--in the wallet ecosystem: the more complex the reference wallet is, the more deviations it'll induce in other implementations/integrations.

The nonexistent Approach 3: Just Use CARROT would be my preference: although obviously we have to support legacy keys and txs, my preference would be as clean of a break as possible and to just move on.  Infeasible, I know..

re: OVKs, I haven't heard a technical person criticize OVKs themselves, but rather most people I've talked to about it just want to respect the wishes of those that are complaining online.  In real life, at conferences etc., I've never met one single person AFK that has serious issues with OVKs.  But maybe I'm just not talking to the right people :)

## tevador | 2026-03-19T16:46:07+00:00
> As a hardware wallet user I support Approach 2: Hybridization

Actually, hardware wallets greatly benefit from a Carrot feature that won't be available to "hybrid" wallets: full view only wallet tier. Full view only wallets greatly simplify all hardware wallet workflows. Notably, there is no need to "import key images" from the hardware wallet to identify spends and calculate the correct balance.

>  I want to make it as easy as possible for current day hardware wallet users to upgrade without creating a bunch of sweeps that correlate old RingCT outputs together

If the sweep is made after the FCMP++ hard fork, no such correlation will be detectable because all spends will use a ring that covers the full chain. **Legacy wallets don't need to upgrade to Carrot to take advantage of the full chain anonymity set.**

## UkoeHB | 2026-03-19T23:10:28+00:00
> Actually, hardware wallets greatly benefit from a Carrot feature that won't be available to "hybrid" wallets: full view only wallet tier. Full view only wallets greatly simplify all hardware wallet workflows. Notably, there is no need to "import key images" from the hardware wallet to identify spends and calculate the correct balance.

A 'hybrid' hardware wallet can still use a view-balance wallet tier. They just need to import key images once, a clear advantage vs legacy hw wallets that need to do it over and over.

## tevador | 2026-03-19T23:22:48+00:00
> A 'hybrid' hardware wallet can still use a view-balance wallet tier. They just need to import key images once, a clear advantage vs legacy hw wallets that need to do it over and over.

Can you elaborate how that would work exactly?

A legacy wallet has existing legacy addresses and any future e-notes received to any legacy address will need key images to be imported.

## UkoeHB | 2026-03-19T23:35:37+00:00
> A legacy wallet has existing legacy addresses and any future e-notes received to any legacy address will need key images to be imported.

True, good point. However, if the wallet *doesn't* receive any new legacy enotes, then no extra importing is necessary. E.g. normal users who don't have any long-term public addresses would only make new Carrot addresses.

## tevador | 2026-03-20T11:24:46+00:00
Another argument against hybrid wallets is the fact that the wallet seed is recoverable by breaking the DLP, which makes the wallet non forward secret even if it uses the new Carrot derivations.

Here are the updated pros and cons of hybrid wallets:

Pros:

1. Full view tier for newly generated addresses. E-notes received to legacy addresses still need key images to be imported.
2. Address generator tier for new addresses.

Cons:

1. Lack of forward secrecy because the wallet seed can be recovered by breaking the DLP.
2. The need to perform two scans (for legacy and Carrot e-notes - this doesn't take 2x the time, but has nonzero cost).
3. Two different addresses for every address index.
4. Higher implementation costs.

## UkoeHB | 2026-03-20T23:30:38+00:00
> The need to perform two scans (for legacy and Carrot e-notes).

Hybrid wallets would share the view-received key, so scanning would be ~equivalent.

## tevador | 2026-03-21T10:46:18+00:00
> Hybrid wallets would share the view-received key, so scanning would be ~equivalent.

At the very least, the wallet would need 2 separate subaddress lookup tables, so the cost is nonzero. But yes, there would not be a lot of extra CPU cost compared to a normal scan.

## rbrunner7 | 2026-03-22T09:23:38+00:00
I strongly support approach 1, as clean a separation as possible between "legacy" wallets and Carrot wallets.

I am convinced that an attempt to establish hybrid wallets will end in confusion, maybe even on a large scale. Complexity makes a big jump upwards. And the possible problems of misunderstanding the state of the wallet at hand, not seeing transfers, getting into even bigger trouble than today should you ever manage to enter a wrong height when restoring, and many more things are  just waiting to bite you, as far as I can indefinitely into the future.

I also became quite pessimistic over the years regarding the significant difficulties of the "Monero wallet app ecosystem" to implement a common feature set that you can be sure to find on every dedicated Monero wallet app, even with the comparatively simple feature set we have today. How many years did it take until subaddress support became universal? Or subaccount support? We now already have a split between apps that support Polyseed because some support native Polyseed encryption, some don't and happily restore a wrong wallet without telling anything as a very dangerous bug.

And now trust that wallet app ecosystem to implement something as complex and complicated as those hybrid wallets? Yeah, good luck.

As an optimist, you can talk about hardware wallet producers implementing new firmware to support hybrid wallets, if the Monero community decides to go that way. As the pessimist that I am, I worry whether they will continue to support Monero *at all* or just throw in the towel, citing an unfavorable cost-benefit ratio for them, even if we "only" want them to implement a fully new wallet type with Carrot.

I understand that heavy hardware wallet users may be tempted to vote for option 2 with hybrid wallets, but frankly, how does that look seen over the totality of wallet owners? If we somehow burden the estimated 90% or even 95% percent of *non* hardware wallet users with additional difficulties to make life of the 10% or even only 5% of hardware wallet users easier, that would be quite unfortunate IMHO.


## jeffro256 | 2026-03-25T16:20:14+00:00
> Actually, hardware wallets greatly benefit from a Carrot feature that won't be available to "hybrid" wallets: full view only wallet tier. Full view only wallets greatly simplify all hardware wallet workflows. Notably, there is no need to "import key images" from the hardware wallet to identify spends and calculate the correct balance.

This will be available to hybrid wallets, assuming that eventually funds are moved off of old addresses eventually.

> Another argument against hybrid wallets is the fact that the wallet seed is recoverable by breaking the DLP, which makes the wallet non forward secret even if it uses the new Carrot derivations.

This is true for the default software wallet seed format. Others can see [my gist](https://gist.github.com/jeffro256/4155401274699e0437ba5b79b93c647f) for more info. However, seeds which have some "master" secret used in a one-way function to derive $k_s, k_v$ (e.g. BIP39, Ledger, Trezor) don't have this issue. Polyseed also may not have this issue, depending on how a hybrid key hierarchy would be implemented.

> At the very least, the wallet would need 2 separate subaddress lookup tables, so the cost is nonzero. But yes, there would not be a lot of extra CPU cost compared to a normal scan.

It wouldn't need two subaddress tables necessarily, but it would need at least a "merged" table. See this table in the FCMP++ unit test suite for an idea: https://github.com/seraphis-migration/monero/blob/7dbeb59ea3ffc55579f14128b40ce0d8e29076b4/tests/unit_tests/carrot_mock_helpers.h#L62-L79

This table interface also implements reverse lookup: index -> pubkey. An "extended subaddress index" in the code is a tuple of (major index, minor index, hierarchy type). Same storage cost, but only one lookup per potential received e-note. 



## jeffro256 | 2026-03-25T16:53:54+00:00
> Users who don't want Carrot capabilities will be automatically upgraded to using Carrot unless they are hyper-aware. Once a wallet has any Carrot-scanned enotes, it will be a pain to 'unravel' that. 

To be fair, an upgrade to a hybrid key hierarchy doesn't have to be automatic in the sense that it doesn't inform the human user about what is happening. Perhaps a message along the lines of "This wallet can be migrated to a hybrid key hierarchy, which gives you the following features: X , Y, Z. Your displayed receive addresses will change, but old receive addresses will continue to work. Would you like to perform this migration (y/n)?" The wallet software would then enable the hybrid code iff human consents.

The point about unraveling is true, but I would imagine that it would only be relevant if there was an implementation bug, or if the human was migrating to a new wallet vendor without hybrid support.

> Users with hybrid wallets may try to use a view-balance tier wallet but fail to actually see their full balance and become confused.

A view-balance tier with a share view-incoming key would capture everything that an existing hot wallet would I think? But yeah spend locations for new e-notes received to old addresses would not be calculable without importing key images. So it could differ from what is expecting from a pure new key hierarchy view-balance tier.

## jeffro256 | 2026-03-25T17:25:23+00:00
> I strongly support separation, especially due to the recent controversial debate on OVK.

If you would like to see my opinion on the OVK debate, please watch: https://www.youtube.com/watch?v=87xayqeQY2E. I believe that we shouldn't make design decisions purely based on vibes we get off people or bots on Reddit, when such parties may be misinformed or purposely muddying the waters. 

## tevador | 2026-03-25T18:53:39+00:00
> This will be available to hybrid wallets, assuming that eventually funds are moved off of old addresses eventually.

Moving funds off of old addresses is not sufficient. You can't stop someone from sending you funds to a legacy address you had previously published. For example, old donation addresses might linger in people's address books for quite some time etc.

> This is true for the default software wallet seed format.

The vast majority of legacy wallets use the default 25 word seed supported by the official Monero software. Yes, there are some niche seed formats that could be salvaged, but the benefits don't really outweigh the costs.

> It wouldn't need two subaddress tables necessarily, but it would need at least a "merged" table.

Yes, you correctly described the technical solution, but my point was that the cost is not zero, which is still true.

My [above comment](https://github.com/seraphis-migration/monero/issues/306#issuecomment-4097362410) summarizes the pros and cons of hybrid wallets. IMO, the costs don't justify the relatively small benefits for legacy wallets (an "almost-full-view-only" wallet tier and an address-generator tier).

## j-berman | 2026-03-30T19:21:14+00:00
My view is that a hybrid scheme would lead to security misunderstandings, would be difficult to manage smoothly in standardized UI/UX, and would add complexity to internal wallet logic. I'm pretty strongly in favor of keeping them separate.

#### 1. Security misunderstandings

@tevador raises a strong point that "hybrid" wallets with legacy receives lack forward secrecy, which is arguably the most significant security benefit that Carrot brings. I think the worst case is people misunderstanding this benefit, using "hybrid" wallets assuming they gain the security properties of Carrot, then losing their both their money and privacy from PQ.

I would much more strongly prefer the clean separation approach, so it's obvious to people with Carrot wallets **know** with 100% certainty they have the complete Carrot feature set with no watered down security concepts they need to be conscious of / think through.

#### 2. Difficult-to-manage UI/UX

It would obviously be confusing if a wallet app that already displayed legacy addresses would all the sudden start displaying different Carrot addresses.

@UkoeHB proposed that all wallets could continue displaying already-displayed legacy addresses, but all newly displayed addresses should be Carrot. Imo this sounds good in theory, but different wallets already have different display configurations. E.g. Feather displays something like 5 subaddresses at the start, Cake only displays 1, etc. I think as a result there is inevitable confusion to follow across the ecosystem.

Plus, all these already-displayed legacy addresses are still usable, which presents the security flaw of non-forward secret, non-Carrot-benefitting addresses.

Of course you could inform users with modals/pop-ups/sentences explaining these concepts to them, but I think that is bad UX. Most people will ignore English, and those that read it may not process it.

I think relagating UI/UX changes to **just** wallet creation / advanced settings is much simpler to manage.

#### 3. Technical complexity

I don't think technical complexity on its own is a sound enough con against hybrid wallets, but when weighed together with the above cons, and when weighed against separate wallets, I think it's absolutely worth considering.

The logic of internally managing a hybrid wallet involves keeping state for both types together under one umbrella, which necessarily involves functions that can accept both types that must incorprate logic that picks and chooses correctly among them. That is added complexity compared to functions that only need to take in one type.

I think "separate" wallets = marginally more complexity at wallet creation/restore (that can be abstracted to "advanced settings" and managed simply with a feature bit in the seed), whereas "hybrid" wallets = significantly more complexity in the actual wallet engine. I think it's unquestionable it would lead to greater wallet complexity. And managing wallet complexity is something Monero has struggled with for a long time. I echo @rbrunner7's sentiments [here](https://github.com/seraphis-migration/monero/issues/306#issuecomment-4105880724).

# Action History
- Created by: UkoeHB | 2026-03-19T06:24:27+00:00
