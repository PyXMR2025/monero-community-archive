---
title: unspent_outputs don't work
source_url: https://github.com/monero-project/monero/issues/2915
author: Quark-Fusion
assignees: []
labels: []
created_at: '2017-12-13T06:55:05+00:00'
updated_at: '2017-12-25T20:08:24+00:00'
type: issue
status: closed
closed_at: '2017-12-25T20:08:24+00:00'
---

# Original Description
created new 2/3 multisig wallet on testnet, sent 5 tx to it, synced data
command unspent_outputs says 'There is no unspent output in the specified address'
balance detail command says 5 outputs
show_transfers show 5 incoming tx
incoming_transfers also show 5 tx with 'F' in spent column

moneromooo says same happens without multisig.

console:
[wallet 9x4Tgh]: unspent_outputs
There is no unspent output in the specified address
[wallet 9x4Tgh]:
[wallet 9x4Tgh]: balance detail
Currently selected account: [0] Primary account
Balance: 0.122000000000, unlocked balance: 0.122000000000
Balance per address:
Address Balance Unlocked balance Outputs Label
0 9x4Tgh 0.122000000000 0.122000000000 5 Primary account
[wallet 9x4Tgh]: show_transfers
1059526 in 10:48:39 AM 0.001000000000 2201ace2b2db06249276f86958ec92856735175ac57ba7a892b7a7ca507ff9f1 0000000000000000 0 -
1059526 in 10:48:39 AM 0.001000000000 00a7ed1b9053483a3e469bfd7c49fadf6fb387695b8533d6740992b7d916d5d9 0123456789012345678901234567890123456789012345678901234567890123 0 -
1059538 in 11:05:23 AM 0.010000000000 47b9f4a76beb78b70d71250b4771329ea720d670ff6c72cef4720407953b6b6d 0000000000000000 0 -
1059538 in 11:05:23 AM 0.010000000000 cf8dfd2bfb4af4f34f98864576f048efde9ef95a7a22b43c6b6cbb546c9cb9f3 0123456789012345678901234567890123456789012345678901234567890123 0 -
1059631 in 02:01:37 PM 0.100000000000 aa1ba0e9805e43ba44621a6edadd8f93d2654ad7cce0c64a5162b933086f91c1 0000000000000000 0 -
[wallet 9x4Tgh]: incoming_transfers
amount spent unlocked ringct global index tx id addr index
0.001000000000 F unlocked RingCT 344729 <2201ace2b2db06249276f86958ec92856735175ac57ba7a892b7a7ca507ff9f1> 0
0.001000000000 F unlocked RingCT 344731 <00a7ed1b9053483a3e469bfd7c49fadf6fb387695b8533d6740992b7d916d5d9> 0
0.010000000000 F unlocked RingCT 344747 0
0.010000000000 F unlocked RingCT 344748 <47b9f4a76beb78b70d71250b4771329ea720d670ff6c72cef4720407953b6b6d> 0
0.100000000000 F unlocked RingCT 344861 0

# Discussion History
## moneromooo-monero | 2017-12-13T10:11:03+00:00
https://github.com/monero-project/monero/pull/2918

## moneromooo-monero | 2017-12-25T20:07:40+00:00
+resolved

# Action History
- Created by: Quark-Fusion | 2017-12-13T06:55:05+00:00
- Closed at: 2017-12-25T20:08:24+00:00
