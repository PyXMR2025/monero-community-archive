---
title: Testnet wallet didn't catch transactions
source_url: https://github.com/monero-project/monero/issues/3443
author: zhang111111111
assignees: []
labels: []
created_at: '2018-03-20T01:00:39+00:00'
updated_at: '2018-03-20T15:12:57+00:00'
type: issue
status: closed
closed_at: '2018-03-20T15:12:57+00:00'
---

# Original Description
Hello, I created a new testnet wallet and it didn't recognise incoming transactions. I think it was created using monero-wallet-cli. 

Out of curiosity I ran rescan_bc (it started at block height 1000000)

> [wallet 9y9Wat]: rescan_bc
Starting refresh...
Refresh done, blocks received: 0                                
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000

Following this, I restored the wallet using it's seed

> Specify a new wallet file name for your restored wallet (e.g., MyWallet).
Wallet file name (or Ctrl-C to quit): t2_restore
Generating new wallet...
Specify Electrum seed: alley alarms inquest light suture muddy twofold across pouch phase akin cylinder album waxing initiate scenic wolf shelter needed vain bevel biweekly luggage metro vain
Enter seed encryption passphrase, empty if none: 
Enter a new password for the wallet: 
Confirm password: 
Generated new wallet: 9y9WatmuLZqCxrGyewxbR8KP6nhjmTXPjBp18Gbnib3cJm7MXXRdpTeTM5VJHTotHtAJsFLS1T2Pv7GRmtZdNwQAAbmv1DZ
View key: 424888ee4585ca07173f41e856170a68eb984290782b31bcdc8354776aa1a20a
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Your wallet has been generated!
To start synchronizing with the daemon, use the "refresh" command.
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
Always use the "exit" command when closing monero-wallet-cli to save 
your current session's state. Otherwise, you might need to synchronize 
your wallet again (your wallet keys are NOT at risk in any case).

> NOTE: the following 25 words can be used to recover access to your wallet. Write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.

> alley alarms inquest light suture muddy twofold across
pouch phase akin cylinder album waxing initiate scenic
wolf shelter needed vain bevel biweekly luggage metro vain
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Starting refresh...
Height 1059092, txid <793d5a7b9569dfa3fcc32ea7cc3ab3f59db6197f1638c522e45122ff5419f8ba\>, 0.520000000000, idx 0/0
Height 1059147, txid <e67498cc11c997b2518511a7aefa180d745e491bfb174529e934cbea0b3e2761\>, 0.100000000000, idx 0/0
Height 1059207, txid <bb47fab1bbc6e8836eea15b921853c00e05ef143f64d0719bddb169a168c5af3\>, 0.520000000000, idx 0/0
Height 1063222, txid <29adeba784597e61a0acbf4fbabcc58ef82cd9e13ffbda8ffea434cd770ed138\>, 0.640000000000, idx 0/0
Height 1063257, txid <c0b1325dfb28fa9798c23c6bc5d7fe3ff519f027125ce07306ced8c8ebfb849a\>, 0.200000000000, idx 0/0
Refresh done, blocks received: 1063274                          
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 \*       0 9y9Wat        1.980000000000        1.980000000000       Primary account
\----------------------------------------------------------------------------------
          Total        1.980000000000        1.980000000000
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 1.980000000000, unlocked balance: 1.980000000000
Background refresh thread started

The "original" wallet file (password "changedforgithub") [t2.zip](https://github.com/monero-project/monero/files/1827482/t2.zip)
I do not know how I can give more information about the issue. e9f41e4

# Discussion History
## moneromooo-monero | 2018-03-20T10:24:25+00:00
Did you check what was the refresh height (using the "set" command) ? It's very likely it was wrong, and this is a known bug, which was fixed  a while back I think.

## zhang111111111 | 2018-03-20T13:36:36+00:00
You are right, refresh-from-block-height = 1208496
I think then something is still not quite right since I did not change any settings.

## moneromooo-monero | 2018-03-20T13:41:17+00:00
Was this wallet created using a monero source from a few months ago or older ?

## moneromooo-monero | 2018-03-20T13:43:20+00:00
In particular, the commit which fixes it is 74597bd1. A few other commits after it also make it better.

## zhang111111111 | 2018-03-20T15:12:57+00:00
I only build c7ace5f and e9f41e4 but maybe used 0.11.1.0 by mistake. Because I do not know exactly, I will close the issue for now. Thank you for your help @moneromooo-monero 

# Action History
- Created by: zhang111111111 | 2018-03-20T01:00:39+00:00
- Closed at: 2018-03-20T15:12:57+00:00
