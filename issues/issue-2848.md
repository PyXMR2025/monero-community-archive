---
title: Testnet donation command breaks
source_url: https://github.com/monero-project/monero/issues/2848
author: ghost
assignees: []
labels:
- bug
created_at: '2017-11-20T21:42:54+00:00'
updated_at: '2018-01-10T10:49:20+00:00'
type: issue
status: closed
closed_at: '2018-01-10T10:49:20+00:00'
---

# Original Description
Trying to `donate` in the wallet-cli over testnet leads to the error beneath because of testnet's address incompatibility:

    Error: failed to parse address

This error could be prevented either by stating this command is not callable over testnet or by defining a testnet donation address. The later one has two advantages:

- Allowing the command to be called which should be the case for any command whether being on testnet or not.
- Allowing, before erasing a testnet wallet, to sweep and centralize TXMRs to a wallet which can be used to redistribute its content to people willing to use the testnet later.

I'd be happy to fix this either way.
The second option will however require someone from getmonero to create the testnet wallet first.

# Discussion History
## moneromooo-monero | 2017-11-22T09:08:53+00:00
The second option does not require someone from getmonero to create the testnet wallet first. Just make one, and print its seed when running just "donate" on testnet.

## ghost | 2017-11-27T19:48:25+00:00
We could have the testnet donate function send money to the Testnet Faucet


## ghost | 2017-11-27T19:52:46+00:00
@xmr-eric Is there any dev approved testnet faucet? I don't know if dis.gratis is one.

## ghost | 2018-01-03T19:27:36+00:00
> The second option does not require someone from getmonero to create the testnet wallet first. Just make one, and print its seed when running just "donate" on testnet.

Do you mean `donate` without an argument or just print the seed once a donation has been made on the testnet?
  

## moneromooo-monero | 2018-01-04T13:16:51+00:00
Maybe both.

## dEBRUYNE-1 | 2018-01-08T12:31:46+00:00
+bug

# Action History
- Created by: ghost | 2017-11-20T21:42:54+00:00
- Closed at: 2018-01-10T10:49:20+00:00
