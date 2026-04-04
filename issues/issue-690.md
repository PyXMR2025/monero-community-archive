---
title: v15 Network Upgrade Checklist
source_url: https://github.com/monero-project/meta/issues/690
author: sethforprivacy
assignees: []
labels: []
created_at: '2022-04-17T18:18:21+00:00'
updated_at: '2022-08-19T12:15:21+00:00'
type: issue
status: closed
closed_at: '2022-08-19T12:07:11+00:00'
---

# Original Description
- [x] Bulletproofs+ Security audit
  - https://suyash67.github.io/homepage/assets/pdfs/bulletproofs_plus_audit_report_v1.1.pdf 
  - https://usercontent.irccloud-cdn.com/file/INrzUwkZ/bpp-audit-report-20210324.pdf
- [x] Bulletproofs+ Code audit
  - https://suyash67.github.io/homepage/assets/pdfs/bulletproofs_plus_audit_report_v1.1.pdf 
  - https://usercontent.irccloud-cdn.com/file/INrzUwkZ/bpp-audit-report-20210324.pdf
- [x] Ledger integration
  - [x] Ledger notified
  - [x] Pull request made against Monero codebase (if needed)
    - https://github.com/monero-project/monero/pull/8465/
  - [x] Pull request merged into Monero codebase (if needed)
  - [x] Ledger app integration coded by @j-berman
  - [x] Ledger Monero app update available (Date TBD)
- [x] Trezor integration
  - [x] Trezor notified
  - [x] Pull request made against Monero codebase (if needed)
    - https://github.com/monero-project/monero/pull/8299
  - [x] Pull request merged into Monero codebase (if needed)
  - [x] Trezor firmware update coded by Trezor
    - https://github.com/trezor/trezor-firmware/pull/2232
  - [x] Trezor firmware update available (~Aug 17th, 2022)
- [x] Fork height set
  - [x] Twitter announcement
    - https://twitter.com/monero/status/1516835820828823561
  - [x] Reddit announcement
    - https://www.reddit.com/r/Monero/comments/u820v7/blog_monero_will_undergo_a_network_upgrade_on/
  - [x] Getmonero.org announcement
    - https://www.getmonero.org/2022/04/20/network-upgrade-july-2022.html
- [ ] Notify wallets
  - [x] MyMonero
  - [ ] Coinomi
  - [ ] Exa Wallet
  - [ ] Wookey Wallet
  - [ ] X Wallet
  - [ ] Guarda
  - [ ] ZelCore
  - [x] Cake Wallet
  - [x] Monerujo
  - [x] Edge Wallet
  - [ ] Exodus
  - [ ] XMRWallet
  - [x] Feather Wallet
- [ ] Notify exchanges
  - [ ] https://www.getmonero.org/community/merchants/#exchanges
- [ ] Notify 3rd party payment processors
  - [ ] https://www.getmonero.org/community/merchants/#payment-gateways
  - [x] BTCPayServer
- [ ] Notify mining pools
  - [ ] https://miningpoolstats.stream/monero
    - [x] https://liberty-pool.com/
- [x] Release branch created (July 15th, 2022) - https://github.com/monero-project/monero/tree/release-v0.18
  - [x] Update src/version.cpp.in with new version AND new name (if necessary)
  - [x] Update Gitian YML files in contrib/gitian/ to the new version number
  - [x] Update README.md with new fork table entry (or at least update the Recommended Monero version)
  - [x] Update contrib/gitian/README.md so that the instructions reflect the current version
  - [x] Update src/checkpoints/checkpoints.cpp with a recent hardcoded checkpoint
  - [x] Update src/blocks/checkpoints.dat with ./monero-blockchain-export --output-file checkpoints.dat --block-stop <recent block height> --blocksdat
  - [x] Update expected_block_hashes_hash in src/cryptonote_core/blockchain.cpp with checkpoints.dat sha256 hash
- [x] Testnet forked (May 16th, 2022)
- [x] Testnet testing/verification
  - [x] Ledger (pending app release)
  - [x] Trezor (pending firmware release)
  - [x] Release-specific testing
  - [ ] RPC testing/update RPC documentation
- [x] Stagenet forked (~August 6th, 2022, height 1151000)
- [x] Stagenet testing/verification
  - [x] Ledger (pending app release)
  - [x] Trezor (pending firmware release)
  - [x] Release-specific testing
- [x] CLI reproducible builds validated
- [x] CLI released - https://www.getmonero.org/2022/07/19/monero-0.18.0.0-released.html
  - [x] https://www.getmonero.org/downloads/ updated
  - [x] Update hashes.txt on website
  - [x] Update downloads.yml on website
  - [x] Update auto-update DNS records
  - [x] Update redirects on downloads box
  - [x] Update seed nodes
- [x] GUI released - https://www.getmonero.org/2022/07/19/monero-0.18.0.0-released.html
  - [x] https://www.getmonero.org/downloads/ updated
  - [x] Update hashes.txt on website
  - [x] Update hashes.txt.sig on website
  - [x] Update downloads.yml on website
  - [x] Update auto-update DNS records
  - [x] Update redirects on downloads box
- [x] Release Announcements
  - [x] Monero-announce mailer notice
  - [x] Twitter announcement
  - [x] Reddit announcement
  - [x] Getmonero.org announcement

# Discussion History
## sethforprivacy | 2022-04-17T18:20:12+00:00
Updates:

- Hard-fork date and height set per https://github.com/monero-project/meta/issues/684 and https://github.com/monero-project/meta/issues/700
  - Branch/feature complete: July 15th, 2022
  - Release date: July 20th, 2022
  - Testnet hard-fork: May 16th, 2022, (block 1,982,800 and 1,983,520)
  - Stagenet hard-fork: ~August 6th, 2022, (block 1,151,000)
  - Mainnet hard-fork: ~August 13th, 2022 (block 2,688,888)
- Shared checklist URL in monero-dev, monero-research-lab, monero-research-lounge, monero-community, monero-space, and feather-wallet IRC/Matrix channels
  - Pinned checklist URL in r/Monero as well: https://www.reddit.com/r/Monero/comments/u5wgp6/v15_network_upgrade_checklist_tentative_date_set/
- Shared official blog post broadly: https://www.getmonero.org/2022/04/20/network-upgrade-july-2022.html

## selsta | 2022-04-29T05:00:48+00:00
Just for completeness, we had a second BP+ code audit: https://usercontent.irccloud-cdn.com/file/INrzUwkZ/bpp-audit-report-20210324.pdf

## sethforprivacy | 2022-05-08T11:40:55+00:00
Updated dates/heights per https://github.com/monero-project/meta/issues/700 and added Stagenet steps to checklist.

## Gingeropolous | 2022-05-10T13:13:27+00:00
is there a name yet for the release? 

## sethforprivacy | 2022-05-10T13:23:19+00:00
> is there a name yet for the release?

"Fluorine Fermi" was chosen: https://github.com/monero-project/meta/issues/623

## Rucknium | 2022-07-02T22:01:50+00:00
@sethforprivacy , this need to be updated for the new network upgrade date.

## hundehausen | 2022-07-13T12:47:01+00:00
@sethforprivacy can you please give us an update on that checklist?

## sethforprivacy | 2022-07-13T13:45:06+00:00
> @sethforprivacy , this need to be updated for the new network upgrade date.

Done a few days ago, just forgot to reply :)

## sethforprivacy | 2022-07-13T13:45:42+00:00
> @sethforprivacy can you please give us an update on that checklist?

I unfortunately do not have any updates and haven't been able to keep up with meetings/convos in -dev.

@selsta are there any updates that need to be made to the checklist that you are aware of?

## selsta | 2022-07-13T23:27:29+00:00
@sethforprivacy we will branch and tag today / tomorrow and release in the next days.

## sethforprivacy | 2022-07-20T18:46:54+00:00
Updated with as much info as I have on what has been done now that binaries are out, and posted in #monero-community requesting people reach out to their favorite wallets and exchanges to notify them of the upgrade.

## gtbuchanan | 2022-08-18T21:58:14+00:00
[The Trezor firmware update is now available.](https://blog.trezor.io/trezor-suite-and-firmware-updates-august-2022-bitcoin-only-firmware-in-trezor-suite-a4e3d76214c1)

## sethforprivacy | 2022-08-19T12:07:11+00:00
AFAIK all Monero-sided work is complete at this point, so I'm closing this issue. I'll PR improvements to the checklist shortly as well that were learned from this.

## sethforprivacy | 2022-08-19T12:15:21+00:00
Updated check-list PR with lessons/steps learned from this fork:

https://github.com/monero-project/monero/pull/8516

# Action History
- Created by: sethforprivacy | 2022-04-17T18:18:21+00:00
- Closed at: 2022-08-19T12:07:11+00:00
