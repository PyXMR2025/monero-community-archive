---
title: Apple Silicon official binaries.
source_url: https://github.com/monero-project/monero/issues/8286
author: sweeden-ttu
assignees: []
labels: []
created_at: '2022-04-24T06:38:38+00:00'
updated_at: '2022-04-25T17:48:51+00:00'
type: issue
status: closed
closed_at: '2022-04-25T17:48:51+00:00'
---

# Original Description
Official Apple Silicon binaries available [here](https://github.com/web-sharp/monero/releases/tag/v0.17.3.0).  Website only has Intel.

monero-blockchain-ancestry
monero-blockchain-depth
monero-blockchain-export
monero-blockchain-import
monero-blockchain-mark-spent-outputs
monero-blockchain-prune
monero-blockchain-prune-known-spent-data
monero-blockchain-stats
monero-blockchain-usage
monero-gen-ssl-cert
monero-gen-trusted-multisig
monero-wallet-cli
monero-wallet-rpc
monerod

# Discussion History
## hyc | 2022-04-24T23:51:37+00:00
In what way are these "official" ?

If you had to pass any particular flags to the build process, it would be better to submit a PR to get those changes integrated into the Gitian build scripts, which are the actual mechanism for producing "official" binaries.

## jeffro256 | 2022-04-25T16:21:59+00:00
@web-sharp Can you explain how you built these, and if there was an tinkering necessary besides the default build scripts?

## sweeden-ttu | 2022-04-25T16:24:36+00:00
   No tinkering!  No tinkering.Except for nginx and tor.  I tinkered with those don’t distribute them   On Mon, Apr 25, 2022 at 9:22 AM, Jeffrey Ryan ***@***.***> wrote:  
@web-sharp Can you explain how you built these, and if there was an tinkering necessary besides the default build scripts?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you were mentioned.Message ID: ***@***.***>

## selsta | 2022-04-25T16:26:09+00:00
It sounds like these are just static binaries for ARM Mac, not built with gitian / depends.

## sweeden-ttu | 2022-04-25T16:27:12+00:00
   @selsta is right   On Mon, Apr 25, 2022 at 9:26 AM, selsta ***@***.***> wrote:  
It sounds like these are just static binaries for ARM Mac, not built with gitian / depends.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you were mentioned.Message ID: ***@***.***>

## selsta | 2022-04-25T17:48:51+00:00
I'll close this here as these are 3rd party binaries without reproducible builds.

@web-sharp it's fine for you to offer 3rd party builds but we can't advertise them as official.

# Action History
- Created by: sweeden-ttu | 2022-04-24T06:38:38+00:00
- Closed at: 2022-04-25T17:48:51+00:00
