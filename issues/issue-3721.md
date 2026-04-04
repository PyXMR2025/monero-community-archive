---
title: '[Feature] Implement 14-Word Feather-style Wallet Seed with Embedded Restore
  Height'
source_url: https://github.com/monero-project/monero-gui/issues/3721
author: CryptoGrampy
assignees: []
labels: []
created_at: '2021-10-29T03:23:54+00:00'
updated_at: '2022-02-13T08:53:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There was a discussion today in the Monero Research Lab about seed phrases that can replace the need for users having to remember block restore heights/dates, and it turns out Feather Wallet already gives users this option by default- a 14 word backup seed- when creating a new wallet (you can also restore a 14 or 25 word wallet in feather).

Restore heights/dates are confusing to most people and can cause a lot of frustration when one restores a wallet and the funds don't show up. Defaulting the Monero GUI wallet to a 14-word seed as implemented in Feather (while also allowing 25 word restoring) would be awesome, create a better user experience, alleviate frustration/issue tickets/chat questions and allow for simplification of the UI.  

Adding this feature into the Monero GUI- even as non-default for now- will especially make it easier for other wallet creators to feel confident in adding this feature.  

There are wallets that are coming down the pipeline as well- browser extensions, Molly.IM, etc.  and it would be great to have Monero Core/GUI support of this feature ASAP.   

https://github.com/tevador/monero-seed
https://docs.featherwallet.org/guides/seed-scheme
https://github.com/monero-project/monero/issues/6639


# Discussion History
## rbrunner7 | 2022-02-13T08:53:47+00:00
Just some info for people who may pass by here: @tevador reworked and improved their new seeds somewhat. The system is now called *Polyseed* and can be found here: https://github.com/tevador/polyseed

# Action History
- Created by: CryptoGrampy | 2021-10-29T03:23:54+00:00
