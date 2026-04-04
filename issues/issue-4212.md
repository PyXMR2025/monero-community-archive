---
title: Message signatures with view-only wallets broken, despite support in CLI /
  RPC
source_url: https://github.com/monero-project/monero-gui/issues/4212
author: selsta
assignees: []
labels: []
created_at: '2023-08-18T13:28:22+00:00'
updated_at: '2023-10-01T11:21:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
19:12 <m-relay> <d​atahoarder:monero.social> Hey, view-only wallets generate signatures within the advanced menu using the spend key, with the right spend public key but spend private key of zero. This makes these signatures not self-verifiable or proper.
19:12 <m-relay> <d​atahoarder:monero.social> monero-wallet-cli and RPC both allow setting either making the signature using the spend or view private key, and the code downstream supports this. Verification also returns which key signed the message.
19:12 <m-relay> <d​atahoarder:monero.social> Seems it is just a missing feature within GUI that is well supported within Monero code and RPC, and the method to sign/verify for both is documented.
19:12 <m-relay> <d​atahoarder:monero.social> The code TL;DR `get_message_hash mode=0, s_comm.key = spend_pub, but secret_key &sec = spend_zero`. On Monero GUI code, `QString Wallet::signMessage(const QString &message, bool filename) const` within `libwalletqt/Wallet.cpp` uses `m_walletImpl->signMessage()`, then signMessage() just takes the message and then calls `m_wallet->sign(message, tools::wallet2::sign_with_spend_key);`. This hardcodes to always use the spend key, even for view wallets.
```

![image](https://github.com/monero-project/monero-gui/assets/7697454/2e3c96c9-c07b-431d-9953-6df356b0d896)


# Discussion History
## Monero-support | 2023-09-20T10:40:10+00:00
Good afternoon!
Your error is due to the fact that you are in a test environment, the main network will be launched in Q1 November. But you will also be able to use the tendermint to use your XMR. Target launch on Q2 October

## plowsof | 2023-10-01T11:19:43+00:00
This "new" pull request added the feature to optionally select the spend / view key to sign data with https://github.com/monero-project/monero/pull/6600 

some issues i notice:
- if no signature_type is selected (for the rpc call), it will default to using the spend_key (even when we are using a view only wallet)

Where/how to fix this? is it the monero-gui's problem or a monero-core problem?
- should monero-core simply detect if the spend key is empty and return an error without returning bogus data?
- if no signature_type provided - auto detect if we're using a view only wallet and use the view key?

or is it the monero-guis problem to 'detect what mode we're in / pass the correct key' / add a radio button where the user can manually select the key (spend being greyed out if we're in view only)

i also have a patch for the wallet-rpc docs on site which may need a "if you are using a view only wallet it'll use a bogus spend key so please specify you want to use the view key" https://github.com/monero-project/monero-site/compare/master...plowsof:monero-site:sign_verify


# Action History
- Created by: selsta | 2023-08-18T13:28:22+00:00
