---
title: Allow specifying required fields for URI
source_url: https://github.com/monero-project/monero/issues/8063
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2021-11-15T18:47:58+00:00'
updated_at: '2021-11-15T18:47:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Related:
* https://github.com/monero-project/monero/wiki/URI-Formatting

Like with [BIP21](https://en.bitcoin.it/wiki/BIP_0021), we should be able to pass through a required parameter for any of the URI parameters. Wallets can then cancel and display an error should they not be able to support any important parameters.

Should a wallet address be considered required, a URI should specify `?req-address` instead of `?address`. Same for any other parameter.

This way, should Monero add future functionality to its URIs that passes through necessary context, wallets can easily understand when to throw an error if they don't understand them, instead of continuing to interpret the URI incorrectly.

# Discussion History
# Action History
- Created by: SamsungGalaxyPlayer | 2021-11-15T18:47:58+00:00
