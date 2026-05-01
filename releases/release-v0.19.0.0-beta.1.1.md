---
title: FCMP++ & Carrot beta stressnet v1.1
type: release
source_url: https://github.com/seraphis-migration/monero/releases/tag/v0.19.0.0-beta.1.1
author: j-berman
tag_name: v0.19.0.0-beta.1.1
published_at: '2026-04-30T06:23:01+00:00'
---

# Version: v0.19.0.0-beta.1.1

# Release Notes
## Overview

This is the v1.1 release of the FCMP++ and Carrot **beta** stressnet software. This release includes a wallet scanning fix (#346) and minor cleanup.

The FCMP++ and Carrot beta stressnet will hard fork from the current testnet on May 6, 2026, at block 2997100. Included below is the software you can use to participate in the beta stressnet.

[FCMP++](https://www.getmonero.org/2024/04/27/fcmps.html) is a proposed upgrade to replace ring signatures with membership proofs that span the whole chain. When spending Monero, instead of making a ring signature proving you own 1 of 16 Monero outputs, you make a proof that you own 1 of the 150 million+ Monero outputs from across the entire Monero blockchain.

[Carrot](https://github.com/jeffro256/carrot) is a proposed upgrade to Monero's addressing protocol, bringing new security, privacy, and usability features, while maintaining backwards compatibility with existing addresses.

Both FCMP++ and Carrot have been in development for over 2 years, while research, security reviews, and audits have progressed in tandem. This beta stressnet will be the second live network testing the FCMP++ and Carrot integration open to the public.

## Beta Stressnet Information

To participate, please follow the instructions below. If you encounter any issues/bugs/annoyances, please share a detailed issue [here](https://github.com/seraphis-migration/monero/issues). You can also join the stressnet matrix room: [#monero-stressnet:monero.social](https://matrixrooms.info/room/monero-stressnet:monero.social).

We want as many people testing and reporting issues as possible to help prepare for a smooth launch of FCMP++ and Carrot. Be warned: this is beta software, and will likely have bugs. Please share bug reports that are as detailed as possible! Try to describe the exact set of steps to reproduce any errors you encounter, and if possible, share wallet and daemon logs using log level 2. Detailed bug reports will help us solve bugs right away.

Some things to keep in mind:
- If you have an existing testnet daemon synced already, the initial database migration can take several hours to complete.
  - We recommend making a copy of the database so that you have a backup from before the migration.
- Your FCMP++ wallet MUST point to an FCMP++ compatible daemon.
- Constructing many input transactions takes some time.
- The following features are not yet functional:
  - Watch-only wallets & cold wallets.
  - Hardware wallet support.
  - Multisig.
  - Transaction proofs.

Thank you and happy testing!

## ❗❗❗ WARNING: stressnet anonymity set

The anonymity set of running a node on the mainnet Monero network is in the thousands. The anonymity set of running a node on this stressnet will be in the dozens at best. If you run a stressnet node on your machine, the IP address of your machine (or the proxy's IP address if your machine uses a proxy) will be visible to other nodes on the network. If you have an extreme threat model, this may be an unacceptable risk for you.

## Download daemon/CLI/RPC/GUI binaries

This beta release includes binaries you can download. Just find your machine below, and download the zip file. You will find the binaries inside.

## Using daemon/CLI/RPC/GUI wallet

You can run use these like normally, just remember to provide the `--testnet` flag for the daemon, CLI, and RPC.

For GUI, select the "testnet" network type from the drop-down menu in "advanced settings". The daemon port should be 28081.

## Compiling from source

[Here is a simple python script](https://gist.github.com/jeffro256/543932a8b9de3a42ce474e7aa9184c86) you can execute to compile and build from source yourself.