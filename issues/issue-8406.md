---
title: View_tag
source_url: https://github.com/monero-project/monero/issues/8406
author: Edan3blov
assignees: []
labels: []
created_at: '2022-06-27T13:59:06+00:00'
updated_at: '2022-07-19T15:48:37+00:00'
type: issue
status: closed
closed_at: '2022-07-19T15:48:21+00:00'
---

# Original Description
Hi,

As i saw on IIRC and elsewhere there is a need for view_tag function to create manually  tx even after HF.


Thank you.


# Discussion History
## j-berman | 2022-06-28T02:50:36+00:00
Your question is a little unclear. Are you a normal user of Monero, or a developer of software that manually creates Monero txs?

## Edan3blov | 2022-06-28T11:48:52+00:00
I'm developer that manually creates Monero txs.

Thank you.

## selsta | 2022-06-28T20:24:55+00:00
If you post more detailed information it will be easier to help you.

## j-berman | 2022-06-29T15:16:47+00:00
Every output in every tx will need to have a `view_tag` after the HF. It must be calculated correctly, otherwise other wallets won't be able to recognize received outputs.

A view tag is the first byte of `hash["view_tag" | derivation | output index]`
- The hash function is the same Keccak used across the code base (see `cn_fast_hash`)
- `derivation` is the shared secret

### Relevant code

You can see how to derive the view tag here: https://github.com/monero-project/monero/blob/9750e1fa103539b3e533455500610aae76e253a5/src/crypto/crypto.cpp#L753-L775

Here is where the default tx builder derives them: https://github.com/monero-project/monero/blob/9f814edbd78c70c70b814ca934c1ddef58768262/src/device/device_default.cpp#L341-L344

### Testing

View tags are live on testnet now. You can test by compiling master (commit 9750e1fa103539b3e533455500610aae76e253a5) and running `monerod` on testnet. Construct transactions using your tx builder, and then make sure a recipient using `monero-wallet-cli` is able to see those transactions.

There are also test vectors for `derive_view_tag` here: https://github.com/monero-project/monero/blob/9750e1fa103539b3e533455500610aae76e253a5/tests/crypto/tests.txt

### Original PR

#8061 

## Edan3blov | 2022-07-06T14:13:45+00:00
Hello again,

The best solution is a wallet-cli command line like --create-view-tag-from-spend-key  

## selsta | 2022-07-06T19:21:23+00:00
Again, if you don't explain in detail what you are trying to do we can't help you. And if there is some language barrier maybe you can try to give an example of what you are doing?

## selsta | 2022-07-19T15:48:21+00:00
Closing this as it's unclear what the issue creator is asking and there was no attempt at clarifying.

# Action History
- Created by: Edan3blov | 2022-06-27T13:59:06+00:00
- Closed at: 2022-07-19T15:48:21+00:00
