---
title: FCMP++ & Carrot alpha stressnet v1.3
type: release
source_url: https://github.com/seraphis-migration/monero/releases/tag/v0.19.0.0-alpha.1.3
author: j-berman
tag_name: v0.19.0.0-alpha.1.3
published_at: '2025-10-21T23:25:13+00:00'
---

# Version: v0.19.0.0-alpha.1.3

# Release Notes
## Overview

This is the v1.3 release of the FCMP++ and Carrot alpha stressnet software. Changes include:

- Daemon: faster sync by verifying batches of FCMP++ proofs in parallel (#178)
- Wallet: CLI & RPC speed up refresh and show_transfers w/large pool (#162)
- Wallet: fix sporadic GUI / wallet API large tx construction failures (#187)
- Wallet: fast block popping (on reorg or bad password) + fix tree cache ref counter + better logging (#186)
- p2p: reduce bandwidth usage from tx re-relay (#177, #188)
- p2p: peers remained banned for only 2 minutes (#182)

The FCMP++ and Carrot alpha stressnet hard forked from the current testnet on October 3rd, 2025, at block 2847330. Included below is the software you can use to participate in the alpha stressnet.

[FCMP++](https://www.getmonero.org/2024/04/27/fcmps.html) is a proposed upgrade to replace ring signatures with membership proofs that span the whole chain. When spending Monero, instead of making a ring signature proving you own 1 of 16 Monero outputs, you make a proof that you own 1 of the 150 million+ Monero outputs from across the entire Monero blockchain.

[Carrot](https://github.com/jeffro256/carrot) is a proposed upgrade to Monero's addressing protocol, bringing new security, privacy, and usability features, while maintaining backwards compatibility with existing addresses.

Both FCMP++ and Carrot have been in development for over a year, while research, security reviews, and audits have progressed in tandem. This alpha stressnet will be the first live network testing the FCMP++ and Carrot integration open to the public.

## Alpha Stressnet Information

To participate, please follow the instructions below. If you encounter any issues/bugs/annoyances, please share a detailed issue [here](https://github.com/seraphis-migration/monero/issues). You can also join the stressnet matrix room: [#monero-stressnet:monero.social](https://matrixrooms.info/room/monero-stressnet:monero.social).

We want as many people testing and reporting issues as possible to help prepare for a smooth launch of FCMP++ and Carrot. Be warned: this is ALPHA software, and will likely have bugs. Please share bug reports that are as detailed as possible! Try to describe the exact set of steps to reproduce any errors you encounter, and if possible, share wallet and daemon logs using log level 2. Detailed bug reports will help us solve bugs right away.

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
  - The block explorer.

Thank you and happy testing!

## ❗❗❗ WARNING: stressnet anonymity set

The anonymity set of running a node on the mainnet Monero network is in the thousands. The anonymity set of running a node on this stressnet will be in the dozens at best. If you run a stressnet node on your machine, the IP address of your machine (or the proxy's IP address if your machine uses a proxy) will be visible to other nodes on the network. If you have an extreme threat model, this may be an unacceptable risk for you.

## Download daemon/CLI/RPC binaries

This alpha release includes binaries you can download. Just find your machine below, and download the zip file. You will find the binaries inside.

## Using daemon/CLI/RPC/GUI wallet

You can run use these like normally, just remember to provide the `--testnet` flag for the daemon, CLI, and RPC.

For GUI, select the "testnet" network type from the drop-down menu in "advanced settings". The daemon port should be 28081.

## Compiling from source

[Here is a simple python script](https://gist.github.com/jeffro256/543932a8b9de3a42ce474e7aa9184c86) you can execute to compile and build from source yourself.
