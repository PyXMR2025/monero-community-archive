---
title: Offline wallet is considered as "Hot"
source_url: https://github.com/monero-project/monero/issues/9333
author: dev-warrior777
assignees: []
labels:
- question
created_at: '2024-05-16T20:06:07+00:00'
updated_at: '2024-05-17T00:58:35+00:00'
type: issue
status: closed
closed_at: '2024-05-17T00:58:35+00:00'
---

# Original Description
I am following <https://monero.stackexchange.com/questions/2868/is-there-any-way-to-construct-a-transaction-manually> sequence. Can successfully export outputs from a view only wallet using `monero-wallet-cli` but cannot import into an offline wallet with the unexpected error:
`Error: Failed to import outputs view.outputs: Failed to import outputs: Hot wallets cannot import outputs`

```bash


================================
Hot View only wallet
================================

$ ./monero-wallet-cli --daemon-address 127.0.0.1:18081  --wallet-file /home/dev/dextest/xmr/wallets/tx_builder_view/tx_builder_view  --allow-mismatched-daemon-version --log-level 2
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Fluorine Fermi' (v0.18.3.3-release)
Logging to ./monero-wallet-cli.log
Wallet password: 
Opened watch-only wallet: 46MdM2AoFHz8wAkRgBvjpBe6zmDaUTXqDEHU7SxpJjvULydszNoHLdn4qzCRjRzmEL3dBStqjFFkb1P31vBbVe5KEDzh6LV
**********************************************************************
Use the "help" command to see a simplified list of available commands.
Use "help all" to see the list of all available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
The daemon is not set up to background mine.
With background mining enabled, the daemon will mine when idle and not on battery.
Enabling this supports the network you are using, and makes you eligible for receiving new monero
Do you want to do it now? (Y/Yes/N/No): : n
Background mining not enabled. Set setup-background-mining to 1 to change.
Starting refresh...
Refresh done, blocks received: 0                                
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 46MdM2       84.000000000000       84.000000000000       Primary account
------------------------------------------------------------------------------------
          Total         84.000000000000       84.000000000000
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 84.000000000000, unlocked balance: 84.000000000000 (Some owned outputs have missing key images - export_outputs, import_outputs, export_key_images, and import_key_images needed)
Background refresh thread started
[wallet 46MdM2]: export_outputs view.outputs
Wallet password: 
Outputs exported to view.outputs

[wallet 46MdM2]: exit

================================
Cold wallet
================================

$ ./monero-wallet-cli --offline  --wallet-file /home/dev/dextest/xmr/wallets/tx_builder/tx_builder  --allow-mismatched-daemon-version --log-level 2
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Fluorine Fermi' (v0.18.3.3-release)
Logging to ./monero-wallet-cli.log
Wallet password: 
Opened wallet: 46MdM2AoFHz8wAkRgBvjpBe6zmDaUTXqDEHU7SxpJjvULydszNoHLdn4qzCRjRzmEL3dBStqjFFkb1P31vBbVe5KEDzh6LV
**********************************************************************
Use the "help" command to see a simplified list of available commands.
Use "help all" to see the list of all available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Background mining not enabled. Run "set setup-background-mining 1" to change.
Error: wallet failed to connect to daemon, because it is set to *offline* mode
Background refresh thread started
[wallet 46MdM2 (no daemon)]: import_outputs view.outputs
Wallet password: 
Error: Failed to import outputs view.outputs: Failed to import outputs: Hot wallets cannot import outputs
[wallet 46MdM2 (no daemon)]: exit

================================




```

# Discussion History
## dev-warrior777 | 2024-05-16T20:12:27+00:00
[monero-wallet-cli.log](https://github.com/monero-project/monero/files/15340378/monero-wallet-cli.log)


## selsta | 2024-05-16T21:18:56+00:00
This message means this wallet has been previously synced with an online node before. You have to create a separate file for the cold wallet that never touches a node.

## dev-warrior777 | 2024-05-16T21:28:18+00:00
Is there an easy way to do that given x.wallet and x.wallet.keys?


## dev-warrior777 | 2024-05-16T21:30:56+00:00
generate-from-keys perhaps


## selsta | 2024-05-16T21:31:41+00:00
Yes, generate-from-keys or seed should work but the whole idea is that the offline wallet gets generated on an offline system, so what you are doing is more of a workaround.

## dev-warrior777 | 2024-05-16T21:32:11+00:00
ok understand, thanks for help


# Action History
- Created by: dev-warrior777 | 2024-05-16T20:06:07+00:00
- Closed at: 2024-05-17T00:58:35+00:00
